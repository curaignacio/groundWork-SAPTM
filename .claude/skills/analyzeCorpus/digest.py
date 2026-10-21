#!/usr/bin/env python3
"""Source digestion for analyzeCorpus. Deterministic: the same files always give the same result.

  python digest.py plan  TARGET   what a run would do, file by file; changes nothing
  python digest.py run   TARGET   convert, structure, map, archive, and write the index's
                                  mechanical fields; summaries are left "(to write)"
  python digest.py check TARGET   verify every corpus rule; exit 1 with a list if any fails
  python digest.py text FILE...   project files: write a readable {stem}.md beside each

TARGET is the assistant folder. See dev/sourceDigestion.md in the creator for the protocol.
"""
import collections
import csv
import datetime
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

LARGE = 500          # a file of more lines than this gets a topic map
MAP_MIN = 5          # a map starts at the shallowest heading level with at least this many
MAP_MAX = 60         # deeper levels are added while the map stays within this many rows
TODO = "(to write)"
FF = chr(12)
LIGATURES = {chr(0xFB00): "ff", chr(0xFB01): "fi", chr(0xFB02): "fl", chr(0xFB03): "ffi",
             chr(0xFB04): "ffl", chr(0xFB05): "st", chr(0xFB06): "st"}
# Every character str.splitlines() treats as a line break, other than \n itself. Left in a
# file, they make Python and Claude's Read tool count lines differently.
BREAKS = [chr(c) for c in (0x0B, 0x0C, 0x1C, 0x1D, 0x1E, 0x85, 0x2028, 0x2029)]
UNFINISHED = (".crdownload", ".part", ".partial", ".tmp", ".download")
SKIP_NAMES = {".gitkeep", "desktop.ini", "thumbs.db"}
MD_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
CONVERTED_EXT = re.compile(r"\.(pdf|docx?|docm|dotx|pptx?|xlsx?|xls|html?|txt|rtf|epub|csv)\.md$", re.I)


# ── helpers ────────────────────────────────────────────────────────────────────────────

def norm(s: str) -> str:
    """Comparison key: no heading marks, ligatures folded, letters and digits only."""
    s = unicodedata.normalize("NFKC", re.sub(r"^\s*#+\s*", "", s))
    return re.sub(r"[^\w]+", "", s).lower()


def clean(text: str) -> str:
    """One line-break character, no ligatures, no trailing spaces."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    for b in BREAKS:
        text = text.replace(b, "\n")
    for lig, plain in LIGATURES.items():
        text = text.replace(lig, plain)
    return "\n".join(l.rstrip() for l in text.split("\n")).rstrip("\n") + "\n"


LIST_START = re.compile(r"^([•▪◦\-*]|\d{1,3}[.)])\s")


def join_wrapped(text: str) -> str:
    """Join prose that a narrow PDF column broke into a few words per line, so a phrase
    search finds it. Only short-line prose blocks are joined: headings, blank lines and list
    markers start a new block, and a block without sentence punctuation (a field list, a
    table column) is left as it is."""
    out, block = [], []

    def flush():
        if len(block) >= 2:
            lens = sorted(len(l) for l in block)
            joined = " ".join(block)
            if lens[len(lens) // 2] < 35 and re.search(r"[.!?]", joined):
                out.append(joined)
                block.clear()
                return
        out.extend(block)
        block.clear()

    for raw in text.split("\n"):
        s = raw.strip()
        if not s or s.startswith("#"):
            flush()
            out.append(raw)
        elif LIST_START.match(s):
            flush()
            block.append(s)
        else:
            block.append(s)
    flush()
    return "\n".join(out)


def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def write_text(p: Path, text: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def lines_of(text: str) -> list[str]:
    """Lines exactly as Claude's Read tool numbers them."""
    return text.rstrip("\n").split("\n") if text else []


def md_headings(lines: list[str]) -> list[tuple[int, int, str]]:
    found, fence = [], False
    for i, raw in enumerate(lines, start=1):
        s = raw.strip()
        if s.startswith("```") or s.startswith("~~~"):
            fence = not fence
            continue
        m = None if fence else MD_HEADING.match(s)
        if m:
            found.append((i, len(m.group(1)), m.group(2).strip()))
    return found


def stamp() -> str:
    return datetime.datetime.now().strftime("%y%m%d%H%M")


def archive(src_file: Path, archive_dir: Path) -> Path:
    """Move a file into the archive, prefixed with the clock time; never overwrite."""
    archive_dir.mkdir(parents=True, exist_ok=True)
    dest = archive_dir / f"{stamp()}.{src_file.name}"
    if dest.exists():
        dest = archive_dir / f"{datetime.datetime.now().strftime('%y%m%d%H%M%S')}.{src_file.name}"
    shutil.move(str(src_file), str(dest))
    return dest


# ── PDF structure ──────────────────────────────────────────────────────────────────────

def pdf_bookmarks(path: Path) -> list[tuple[int, str, int | None]]:
    from pdfminer.pdfdocument import PDFDocument, PDFNoOutlines
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfparser import PDFParser
    from pdfminer.pdftypes import PDFObjRef, resolve1
    from pdfminer.psparser import PSLiteral

    out = []
    with open(path, "rb") as f:
        doc = PDFDocument(PDFParser(f))
        pages = {p.pageid: i for i, p in enumerate(PDFPage.create_pages(doc), start=1)}
        try:
            for level, title, dest, action, _ in doc.get_outlines():
                if not title or not title.strip():
                    continue
                d = dest
                if d is None and action:
                    a = resolve1(action)
                    d = a.get("D") if isinstance(a, dict) else None
                d = resolve1(d)
                if isinstance(d, (bytes, str, PSLiteral)):
                    try:
                        d = resolve1(doc.get_dest(d.name if isinstance(d, PSLiteral) else d))
                    except Exception:
                        d = None
                if isinstance(d, dict):
                    d = resolve1(d.get("D"))
                page = None
                if isinstance(d, list) and d and isinstance(d[0], PDFObjRef):
                    page = pages.get(d[0].objid)
                out.append((level, title.strip(), page))
        except PDFNoOutlines:
            pass
    return out


def pdf_layout(path: Path):
    from pdfminer.high_level import extract_pages
    from pdfminer.layout import LTChar, LTTextContainer, LTTextLine

    rows, sizes = [], collections.Counter()
    for pno, page in enumerate(extract_pages(str(path)), start=1):
        for box in page:
            if not isinstance(box, LTTextContainer):
                continue
            prev = None
            for line in box:
                if not isinstance(line, LTTextLine):
                    continue
                chars = [c for c in line if isinstance(c, LTChar) and c.get_text().strip()]
                if not chars:
                    continue
                size = round(max(c.size for c in chars), 1)
                sizes[size] += len(chars)
                font = chars[0].fontname.lower()
                text = line.get_text().strip()
                if prev is not None and rows and rows[-1] is prev and prev["size"] == size:
                    prev["text"] += " " + text          # a heading wrapped inside its box
                    continue
                prev = {"page": pno, "size": size, "text": text, "y": line.y1,
                        "odd": "icon" in font or "mono" in font or "courier" in font}
                rows.append(prev)
    return rows, sizes


def font_headings(rows, sizes):
    if not sizes:
        return []
    body = sizes.most_common(1)[0][0]
    pages = max(r["page"] for r in rows)
    heads = [r for r in rows if r["size"] >= body * 1.15 and not r["odd"] and len(r["text"]) <= 150]
    seen = collections.Counter(norm(r["text"]) for r in heads)
    heads = [r for r in heads if seen[norm(r["text"])] < max(5, pages * 0.3) or len(r["text"]) < 40]
    tiers = collections.Counter(r["size"] for r in heads)
    top = max(tiers) if tiers else None
    keep = sorted((s for s, n in tiers.items() if n > 1 or s == top), reverse=True)
    level = {s: i + 1 for i, s in enumerate(keep)}
    return [(level[r["size"]], r["text"], r["page"]) for r in heads if r["size"] in level]


def header_headings(rows):
    """A running header — the topmost line, repeated on several pages. Each change starts a topic."""
    top = {}
    for r in rows:
        if r["page"] not in top or r["y"] > top[r["page"]]["y"]:
            top[r["page"]] = r
    seq = [(p, top[p]["text"]) for p in sorted(top)]
    count = collections.Counter(norm(t) for _, t in seq)
    out, last = [], None
    for p, t in seq:
        k = norm(t)
        if count[k] >= 2 and k != last and not k.isdigit():
            out.append((1, t, p))
            last = k
    return out


def match(heads, lines, page_of):
    """Find each heading, in order, on its own page (or the next). Returns (index, span, level)."""
    normed = [norm(l) for l in lines]
    n, cur, hits = len(lines), 0, []

    def span_at(i, want):
        joined = ""
        for k in range(i, min(i + 4, n)):
            joined += normed[k]
            if joined == want:
                return k - i + 1
            if not joined or not want.startswith(joined):
                return 0
        return 0

    for level, text, page in heads:
        want = norm(text)
        if not want:
            continue
        for i in range(cur, n):
            if page and page_of[i] > page + 1:
                break
            if page and page_of[i] < page:
                continue
            k = span_at(i, want)
            if k:
                hits.append((i, k, level))
                cur = i + k
                break
    return hits


def structure_pdf(pdf: Path, raw: str) -> tuple[str, str, int, int]:
    """Return (text with headings, method, matched, found)."""
    lines, page_of = [], []
    for pno, page in enumerate(raw.replace("\r\n", "\n").split(FF), start=1):
        for l in page.split("\n"):
            lines.append(l)
            page_of.append(pno)

    # Sources in order of trust. The first that places at least 80% of its headings wins;
    # failing that, the one that placed the most.
    rows = sizes = None
    best = ("none", 0, [])
    for method in ("bookmarks", "fonts", "running headers"):
        try:
            if method == "bookmarks":
                heads = pdf_bookmarks(pdf)
            else:
                if rows is None:
                    rows, sizes = pdf_layout(pdf)
                heads = font_headings(rows, sizes) if method == "fonts" else header_headings(rows)
        except Exception:
            heads = []
        if len(heads) < 2:
            continue
        hits = match(heads, lines, page_of)
        if len(hits) > len(best[2]):
            best = (method, len(heads), hits)
        if len(hits) >= 2 and len(hits) >= 0.8 * len(heads):
            best = (method, len(heads), hits)
            break
    method, found, hits = best
    if len(hits) < 2:
        return "\n".join(lines), "none", 0, 0
    for i, k, level in sorted(hits, reverse=True):
        title = " ".join(re.sub(r"^\s*#+\s*", "", l).strip() for l in lines[i:i + k])
        lines[i:i + k] = ["#" * min(level, 6) + " " + title]
    return "\n".join(lines), method, len(hits), found


def to_markdown(src_file: Path, raw: str) -> tuple[str, str, str]:
    """MarkItDown output → clean markdown. Returns (text, structure method, note)."""
    method, note = "", ""
    if src_file.suffix.lower() == ".pdf":
        raw, method, hit, found = structure_pdf(src_file, raw)
        if method != "none" and hit < found:
            note = f"{found - hit} of {found} headings not found in the text"
        raw = join_wrapped(raw)
    return clean(raw), method, note


# ── project files: a readable text copy beside the original ────────────────────────────

NATIVE = {".md", ".txt", ".csv", ".json", ".xml", ".html", ".htm", ".png", ".jpg", ".jpeg",
          ".gif", ".webp"}
COPY_MARK = "<!-- text copy of {name}, written by digest.py — read this, not the original -->"


def cmd_text(paths: list[Path]) -> None:
    """For each file, write {stem}.md beside it: the text Claude reads in place of the
    original. Prints: file, text copy, lines, structure, note."""
    print("file\ttext\tlines\tstructure\tnote")
    failed = False
    for f in paths:
        if not f.is_file():
            print(f"{f.name}\t\t\t\tnot a file")
            failed = True
            continue
        if f.suffix.lower() in NATIVE:
            print(f"{f.name}\t{f.name}\t\t\tread as it is — no copy needed")
            continue
        dest = f.with_suffix(".md")
        if dest.exists() and not read_text(dest).startswith(COPY_MARK.format(name=f.name)[:30]):
            print(f"{f.name}\t\t\t\tclash: {dest.name} already exists and is not a text copy")
            failed = True
            continue
        try:
            from markitdown import MarkItDown
            raw = MarkItDown().convert(str(f)).text_content
        except Exception as e:
            print(f"{f.name}\t\t\t\tfailed: {str(e)[:120]}")
            failed = True
            continue
        if not raw or not raw.replace(FF, "").strip():
            print(f"{f.name}\t\t\t\tno text found — probably a scan; ask for the pages as images")
            failed = True
            continue
        text, method, note = to_markdown(f, raw)
        text = COPY_MARK.format(name=f.name) + "\n\n" + text
        write_text(dest, text)
        lines = lines_of(text)
        method = method or ("markdown" if md_headings(lines) else "none")
        print(f"{f.name}\t{dest.name}\t{len(lines)}\t{method}\t{note}")
    if failed:
        sys.exit(1)


# ── maps and index ─────────────────────────────────────────────────────────────────────

def map_rows(lines: list[str]) -> list[tuple[int, str]]:
    heads = md_headings(lines)
    if not heads:
        return []
    by_level = collections.Counter(l for _, l, _ in heads)
    levels = sorted(by_level)

    def repeats(level):
        # A level whose titles recur ("Use", "Prerequisites", "More Information") holds
        # the parts of a topic, not topics.
        titles = [norm(t) for _, l, t in heads if l == level]
        return 1 - len(set(titles)) / len(titles) > 0.3

    start = next((l for l in levels if by_level[l] >= MAP_MIN and not repeats(l)), None)
    if start is None:
        start = next((l for l in levels if by_level[l] >= MAP_MIN), levels[-1])
    chosen, total = {start}, by_level[start]
    for l in levels:
        if l > start and total + by_level[l] <= MAP_MAX and not repeats(l):
            chosen.add(l)
            total += by_level[l]
        elif l > start:
            break
    return [(i, t) for i, l, t in heads if l in chosen]


def write_map(target: Path, md: Path, lines: list[str], method: str) -> int:
    rel = md.relative_to(target / "src" / "md")
    mp = target / "src" / "sections" / rel.parent / f"{md.stem}.sections.md"
    rows = map_rows(lines)
    if len(lines) <= LARGE or not rows:
        if mp.exists():
            mp.unlink()
        return 0
    body = [f"# {md.name} — Sections",
            f"Source: src/md/{rel.as_posix()} · {len(lines)} lines · structure: {method} · "
            f"built {datetime.date.today().isoformat()}", "", "| Line | Topic |", "|---|---|"]
    body += [f"| {i} | {t.replace('|', '/')} |" for i, t in rows]
    write_text(mp, "\n".join(body) + "\n")
    return len(rows)


def parse_index(text: str):
    """Split the index into its head (title, date, format comment) and entries keyed by location+name."""
    end = text.find("-->")
    cut = end + 3 if end != -1 else 0
    head, rest = text[:cut], text[cut:]
    entries = collections.OrderedDict()
    for block in re.split(r"\n(?=## )", "\n" + rest):
        block = block.strip("\n")
        if not block.startswith("## "):
            continue
        name = block.split("\n", 1)[0][3:].strip()
        fields = collections.OrderedDict()
        for l in block.split("\n")[1:]:
            m = re.match(r"^- ([a-z ]+): (.*)$", l)
            if m:
                fields[m.group(1)] = m.group(2)
        entries[(fields.get("location", ""), name)] = fields
    return head, entries


def render_index(head: str, entries) -> str:
    head = re.sub(r"(?m)^Last updated:.*$", f"Last updated: {datetime.date.today().isoformat()}", head, count=1)
    out = [head.rstrip("\n")]
    for (_, name), f in entries.items():
        out.append("")
        out.append(f"## {name}")
        out += [f"- {k}: {v}" for k, v in f.items()]
    return "\n".join(out) + "\n"


def index_path(target: Path) -> Path:
    found = sorted((target / "src").glob("index.*.md"))
    if not found:
        sys.exit("no src/index.{Subject}.md in the target")
    return found[0]


# ── plan ───────────────────────────────────────────────────────────────────────────────

def plan(target: Path) -> list[dict]:
    up = target / "src" / "uploads"
    items = []
    for p in sorted(up.rglob("*")):
        if not p.is_file() or p.name.lower() in SKIP_NAMES:
            continue
        sub = p.parent.relative_to(up)
        ext = p.suffix.lower()
        item = {"upload": p, "sub": sub, "name": p.name}
        if p.name.startswith("~$") or ext in UNFINISHED:
            item.update(action="skip", note="unfinished download or lock file")
        elif ext == ".md":
            item.update(action="move", dest=target / "src" / "md" / sub / p.name)
        elif ext == ".csv":
            item.update(action="move", dest=target / "src" / "csv" / sub / p.name)
        else:
            item.update(action="convert", dest=target / "src" / "md" / sub / f"{p.stem}.md")
        items.append(item)
    dests = collections.Counter(str(i["dest"]).lower() for i in items if "dest" in i)
    for i in items:
        if "dest" not in i:
            continue
        if dests[str(i["dest"]).lower()] > 1:
            i.update(action="clash", note=f"another upload also becomes {i['dest'].name}")
        elif i["dest"].exists():
            i["update"] = True
    return items


def cmd_plan(target: Path) -> None:
    for i in plan(target):
        dest = i["dest"].relative_to(target).as_posix() if "dest" in i else ""
        flag = "update" if i.get("update") else i.get("note", "")
        print(f"{i['action']}\t{(i['sub'] / i['name']).as_posix()}\t{dest}\t{flag}")


# ── run ────────────────────────────────────────────────────────────────────────────────

def cmd_run(target: Path) -> None:
    src = target / "src"
    idx = index_path(target)
    head, entries = parse_index(read_text(idx))
    idx_mtime = idx.stat().st_mtime
    report, touched = [], set()

    for i in plan(target):
        rel_name = (i["sub"] / i["name"]).as_posix()
        if i["action"] in ("skip", "clash"):
            report.append({"file": rel_name, "action": i["action"], "note": i["note"]})
            continue
        dest: Path = i["dest"]
        method, note = "", ""
        if i["action"] == "convert":
            try:
                from markitdown import MarkItDown
                raw = MarkItDown().convert(str(i["upload"])).text_content
            except Exception as e:
                report.append({"file": rel_name, "action": "failed", "note": str(e)[:120]})
                continue
            if not raw or not raw.strip():
                report.append({"file": rel_name, "action": "failed", "note": "no text extracted"})
                continue
            text, method, note = to_markdown(i["upload"], raw)
        if i.get("update"):
            mirror = "md" if dest.suffix.lower() == ".md" else "csv"
            archive(dest, target / ".archive" / "src" / mirror / i["sub"])
        if i["action"] == "convert":
            write_text(dest, text)
            archive(i["upload"], target / ".archive" / "src" / "uploads" / i["sub"])
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(i["upload"]), str(dest))
            if dest.suffix.lower() == ".md":
                write_text(dest, clean(read_text(dest)))
        touched.add(dest)
        report.append({"file": rel_name, "action": "updated" if i.get("update") else
                       {"convert": "converted", "move": "moved"}[i["action"]],
                       "dest": dest, "method": method, "note": note,
                       "source": i["name"]})

    # Files edited or dropped straight into src/md or src/csv also need their entry and map.
    live = {p for p in (src / "md").rglob("*.md")} | {p for p in (src / "csv").rglob("*.csv")}
    known = {(f.get("location", ""), n) for (_, n), f in entries.items()}
    for p in sorted(live - touched):
        loc = p.parent.relative_to(src.parent).as_posix() + "/"
        if (loc, p.name) not in known or p.stat().st_mtime > idx_mtime:
            if p.suffix.lower() == ".md":
                write_text(p, clean(read_text(p)))
            touched.add(p)
            report.append({"file": p.relative_to(src).as_posix(), "action": "reindexed", "dest": p,
                           "method": "", "note": "", "source": p.name})

    # Entries and maps for every touched file.
    for r in report:
        p = r.get("dest")
        if p is None or p not in touched:
            continue
        loc = p.parent.relative_to(src.parent).as_posix() + "/"
        old = entries.get((loc, p.name), {})
        f = collections.OrderedDict()
        f["source"] = old.get("source", r["source"]) if r["action"] == "reindexed" else r["source"]
        f["location"] = loc
        if p.suffix.lower() == ".csv":
            with open(p, encoding="utf-8-sig", errors="replace", newline="") as fh:
                sample = fh.read(65536)
                fh.seek(0)
                try:
                    dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
                except csv.Error:
                    dialect = csv.excel
                reader = csv.reader(fh, dialect)
                header = next(reader, [])
                rows = sum(1 for _ in reader)
            f["rows"] = str(rows)
            f["columns"] = " | ".join(h.strip() for h in header)
            f["summary"], f["key topics"] = TODO, TODO
            f["sections"] = "none — search its rows"
            r.update(lines=rows, topics="—")
        else:
            lines = lines_of(read_text(p))
            method = r["method"] or ("markdown" if md_headings(lines) else "none")
            topics = write_map(target, p, lines, method)
            f["lines"] = str(len(lines))
            f["summary"], f["key topics"] = TODO, TODO
            if len(lines) <= LARGE:
                f["sections"] = "none — read it whole"
            elif topics:
                rel = p.relative_to(src / "md")
                f["sections"] = f"src/sections/{(rel.parent / (p.stem + '.sections.md')).as_posix()} ({topics} topics)"
            else:
                f["sections"] = "none — no structure found; search it"
            r.update(lines=len(lines), method=method, topics=topics or "—")
        entries[(loc, p.name)] = f

    # Entries whose file is gone, and maps whose file is gone.
    for key in [k for k in entries if not (src.parent / k[0] / k[1]).exists()]:
        del entries[key]
    for mp in (src / "sections").rglob("*.sections.md"):
        rel = mp.relative_to(src / "sections")
        if not (src / "md" / rel.parent / (mp.name[: -len(".sections.md")] + ".md")).exists():
            mp.unlink()

    write_text(idx, render_index(head, entries))
    print("file\taction\tlines\tstructure\ttopics\tnote")
    for r in report:
        print(f"{r['file']}\t{r['action']}\t{r.get('lines', '')}\t{r.get('method', '')}\t{r.get('topics', '')}\t{r.get('note', '')}")
    todo = [f"{k[0]}{k[1]}" for k, f in entries.items() if TODO in f.values()]
    print(f"# to write: {len(todo)} entr{'y' if len(todo) == 1 else 'ies'}")
    for t in todo:
        print(f"# {t}")


# ── check ──────────────────────────────────────────────────────────────────────────────

def cmd_check(target: Path) -> None:
    src = target / "src"
    idx = index_path(target)
    head, entries = parse_index(read_text(idx))
    problems = []

    def bad(msg):
        problems.append(msg)

    waiting = [p for p in (src / "uploads").rglob("*") if p.is_file() and p.name.lower() not in SKIP_NAMES]
    for p in waiting:
        bad(f"waiting in uploads: {p.relative_to(src).as_posix()}")
    live = {p for p in (src / "md").rglob("*.md")} | {p for p in (src / "csv").rglob("*.csv")}
    for p in sorted(live):
        rel = p.relative_to(src).as_posix()
        if CONVERTED_EXT.search(p.name):
            bad(f"name keeps its source extension: {rel}")
        loc = p.parent.relative_to(src.parent).as_posix() + "/"
        if (loc, p.name) not in entries:
            bad(f"no index entry: {rel}")
    for (loc, name), f in entries.items():
        p = src.parent / loc / name
        if not p.exists():
            bad(f"entry without a file: {loc}{name}")
            continue
        need = ["source", "location", "summary", "key topics", "sections"]
        need += ["rows", "columns"] if p.suffix.lower() == ".csv" else ["lines"]
        for k in need:
            if not f.get(k):
                bad(f"{loc}{name}: missing {k}")
        if TODO in f.values():
            bad(f"{loc}{name}: summary or key topics still {TODO}")
        if p.suffix.lower() != ".md":
            continue
        text = read_text(p)
        if "\r" in text or any(b in text for b in BREAKS):
            bad(f"{loc}{name}: line breaks other than \\n (run digest.py run to clean)")
        if any(l in text for l in LIGATURES):
            bad(f"{loc}{name}: ligature characters left")
        lines = lines_of(text)
        if f.get("lines") and f["lines"] != str(len(lines)):
            bad(f"{loc}{name}: index says {f['lines']} lines, file has {len(lines)}")
        rel = p.relative_to(src / "md")
        mp = src / "sections" / rel.parent / f"{p.stem}.sections.md"
        sec = f.get("sections", "")
        if len(lines) > LARGE:
            if mp.exists():
                if not sec.startswith("src/sections/"):
                    bad(f"{loc}{name}: has a map the index does not point to")
                rows = re.findall(r"^\| (\d+) \| (.+?) \|$", read_text(mp), re.M)
                wrong = [n for n, t in rows if not (0 < int(n) <= len(lines)
                         and lines[int(n) - 1].lstrip().startswith("#")
                         and norm(lines[int(n) - 1]) == norm(t))]
                if wrong:
                    bad(f"{loc}{name}: {len(wrong)} map rows not on their heading (first: line {wrong[0]})")
                m = re.search(r"\((\d+) topics\)", sec)
                if m and int(m.group(1)) != len(rows):
                    bad(f"{loc}{name}: index says {m.group(1)} topics, map has {len(rows)}")
            elif "search it" not in sec:
                bad(f"{loc}{name}: over {LARGE} lines with no map and not marked search-only")
        elif mp.exists():
            bad(f"{loc}{name}: {LARGE} lines or fewer but has a map")
    for mp in (src / "sections").rglob("*.sections.md"):
        rel = mp.relative_to(src / "sections")
        if not (src / "md" / rel.parent / (mp.name[: -len(".sections.md")] + ".md")).exists():
            bad(f"map without a file: {mp.relative_to(src).as_posix()}")
    if problems:
        print("\n".join(problems))
        print(f"# {len(problems)} problem(s)")
        sys.exit(1)
    print(f"# ok: {len(entries)} entries, every rule holds")


def main() -> None:
    if len(sys.argv) >= 3 and sys.argv[1] == "text":
        cmd_text([Path(a).resolve() for a in sys.argv[2:]])
        return
    if len(sys.argv) != 3 or sys.argv[1] not in ("plan", "run", "check"):
        sys.exit(__doc__)
    target = Path(sys.argv[2]).resolve()
    if not (target / "CLAUDE.md").is_file() or not (target / "src" / "uploads").is_dir():
        sys.exit(f"not an assistant folder: {target}")
    {"plan": cmd_plan, "run": cmd_run, "check": cmd_check}[sys.argv[1]](target)


if __name__ == "__main__":
    main()
