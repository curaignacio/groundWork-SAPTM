#!/usr/bin/env python3
"""Section bookkeeping for projectAssistant. Deterministic; it never writes content of its own.

  python sections.py status  ITEM            the confirmed sections, their marks, and
                                             whether the draft holds text for each
  python sections.py init    ITEM            create drafts/00.draft.{Item ID}.md with the
                                             confirmed headings and nothing else
  python sections.py approve ITEM N FILE     write the approved text in FILE under section N
                                             of the current draft, and mark N approved
  python sections.py deliver ITEM TITLE      write deliverables/{Item ID} - {TITLE}.md from
                                             the approved sections, in order

ITEM is the item folder. The section list lives in index.{Item ID}.md:

  - sections confirmed: YYYY-MM-DD
    1. {Section title} — open
    2. {Section title} — approved YYYY-MM-DD

approve and deliver refuse text that carries an internal record — a decision or open
question number, a meeting reference, a cross-reference line — and deliver refuses while
any section is open or empty. The last line printed is always OK or REFUSED.
"""
import datetime
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

MARK = re.compile(r"^(\s+)(\d+)\. (.+?) — (open|approved(?: \d{4}-\d{2}-\d{2})?)\s*$")
INTERNAL = [
    (re.compile(r"\b[DO]\d{1,3}\b"), "a decision or open question number"),
    (re.compile(r"\[meeting\]", re.I), "a meeting file reference"),
    (re.compile(r"\b(Closed by|Addresses:|Led to|Branched from)\b"), "a cross-reference line"),
    (re.compile(r"(?i)\b(as (agreed|decided) (in|on|at)|per (the )?(call|meeting)|in (the|today's|yesterday's) (call|meeting))\b"),
     "a reference to the process"),
]


def today() -> str:
    return datetime.date.today().isoformat()


def refuse(msg: str) -> None:
    print(msg)
    print("REFUSED")
    sys.exit(1)


def item_parts(item: Path) -> tuple[str, str]:
    name = item.name
    if " - " not in name:
        refuse(f"not an item folder: {name}")
    item_id, title = name.split(" - ", 1)
    return item_id, title


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def write(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def marks(index: Path) -> tuple[list[str], list[tuple[int, int, str, str]]]:
    """Index lines, and (line number, section number, title, mark) for each section line."""
    lines = read(index).split("\n")
    out, inside = [], False
    for i, l in enumerate(lines):
        if l.startswith("- sections confirmed:"):
            inside = True
            continue
        if inside:
            m = MARK.match(l)
            if m:
                out.append((i, int(m.group(2)), m.group(3), m.group(4)))
            elif l.strip():
                inside = False
    if not out:
        refuse(f"no confirmed section list in {index.name}")
    return lines, out


def current_draft(item: Path, item_id: str) -> Path | None:
    drafts = sorted((item / "drafts").glob(f"*.draft.{item_id}.md"))
    return drafts[-1] if drafts else None


def draft_sections(text: str) -> dict[int, str]:
    found = {}
    for part in re.split(r"(?m)^## ", text)[1:]:
        head, _, body = part.partition("\n")
        m = re.match(r"(\d+)\. ", head)
        if m:
            found[int(m.group(1))] = body.strip()
    return found


def internal_hits(text: str) -> list[str]:
    hits = []
    for pat, what in INTERNAL:
        m = pat.search(text)
        if m:
            hits.append(f"{what}: “{m.group(0)}”")
    return hits


def cmd_status(item: Path) -> None:
    item_id, _ = item_parts(item)
    _, secs = marks(item / f"index.{item_id}.md")
    d = current_draft(item, item_id)
    body = draft_sections(read(d)) if d else {}
    print(f"draft: {d.name if d else 'none'}")
    for _, n, title, mark in secs:
        print(f"{n}\t{title}\t{mark}\t{'text' if body.get(n) else 'empty'}")
    print("OK")


def cmd_init(item: Path) -> None:
    item_id, title = item_parts(item)
    _, secs = marks(item / f"index.{item_id}.md")
    if current_draft(item, item_id):
        refuse("a draft already exists — branch it instead")
    text = f"# {item_id} — {title}\n\n" + "\n\n".join(f"## {n}. {t}\n" for _, n, t, _ in secs) + "\n"
    p = item / "drafts" / f"00.draft.{item_id}.md"
    write(p, text)
    print(f"created {p.relative_to(item).as_posix()} with {len(secs)} headings")
    print("OK")


def cmd_approve(item: Path, n: int, src: Path) -> None:
    item_id, _ = item_parts(item)
    index = item / f"index.{item_id}.md"
    lines, secs = marks(index)
    sec = next((s for s in secs if s[1] == n), None)
    if not sec:
        refuse(f"section {n} is not on the confirmed list")
    body = read(src).strip()
    if not body:
        refuse("the approved text is empty")
    hits = internal_hits(body)
    if hits:
        refuse("the text carries internal records — fold them into prose first: " + "; ".join(hits))
    d = current_draft(item, item_id)
    if not d:
        refuse("no draft — run init first")
    text = read(d)
    head = re.compile(rf"(?m)^## {n}\. .*$")
    m = head.search(text)
    if not m:
        refuse(f"section {n} has no heading in {d.name}")
    nxt = re.compile(r"(?m)^## \d+\. ").search(text, m.end())
    end = nxt.start() if nxt else len(text)
    text = text[:m.end()] + "\n\n" + body + "\n\n" + text[end:].lstrip("\n")
    write(d, text.rstrip("\n") + "\n")
    i, _, title, _ = sec
    indent = MARK.match(lines[i]).group(1)
    lines[i] = f"{indent}{n}. {title} — approved {today()}"
    write(index, "\n".join(lines))
    print(f"section {n} written to {d.name} and marked approved {today()}")
    print("OK")


def cmd_deliver(item: Path, title: str) -> None:
    item_id, _ = item_parts(item)
    _, secs = marks(item / f"index.{item_id}.md")
    open_ = [f"{n}. {t}" for _, n, t, m in secs if not m.startswith("approved")]
    if open_:
        refuse("not every section is approved: " + ", ".join(open_))
    d = current_draft(item, item_id)
    body = draft_sections(read(d)) if d else {}
    empty = [f"{n}. {t}" for _, n, t, _ in secs if not body.get(n)]
    if empty:
        refuse("approved but empty in the draft: " + ", ".join(empty))
    out = f"# {title}\n\n" + "\n\n".join(f"## {n}. {t}\n\n{body[n]}" for _, n, t, _ in secs) + "\n"
    hits = internal_hits(out)
    if hits:
        refuse("the deliverable would carry internal records: " + "; ".join(hits))
    if any(c in title for c in '\\/:*?"<>|'):
        refuse("the title holds a character Windows forbids in a file name")
    p = item / "deliverables" / f"{item_id} - {title}.md"
    write(p, out)
    print(f"written {p.relative_to(item).as_posix()} — {len(secs)} sections")
    print("OK")


def main() -> None:
    a = sys.argv[1:]
    if len(a) < 2 or a[0] not in ("status", "init", "approve", "deliver"):
        sys.exit(__doc__)
    item = Path(a[1]).resolve()
    if a[0] == "status":
        cmd_status(item)
    elif a[0] == "init":
        cmd_init(item)
    elif a[0] == "approve" and len(a) == 4:
        cmd_approve(item, int(a[2]), Path(a[3]))
    elif a[0] == "deliver" and len(a) == 3:
        cmd_deliver(item, a[2])
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
