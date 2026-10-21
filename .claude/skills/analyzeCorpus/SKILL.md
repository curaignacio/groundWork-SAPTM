---
name: analyzeCorpus
description: Process source files dropped into an assistant's src/uploads/ — digest.py converts them to markdown, recovers their headings, maps large files in src/sections/, archives the originals and writes the index's mechanical fields; then write each entry's summary and key topics in src/index.{Subject}.md. Use when the creator asks to analyze, index, or refresh the corpus after adding source materials. Not for building a learning plan (learningPlanner) and not for answering questions from the corpus.
---

# Analyze corpus

Build-time skill. It runs when source files are added or updated. It gets every source
file into a readable form under `src/`, and builds the two layers retrieval relies on:

- **the index**, `src/index.{Subject}.md` — one short entry per file, read before every
  answer, so it stays small;
- **topic maps**, `src/sections/` — for each large file, its topics and the line where
  each starts, read only for the files the index points to.

It produces an index, not a curriculum. It never proposes sessions and never generates a
learning artifact.

**The script does the mechanical work; you write what needs judgement.**
`.claude/skills/analyzeCorpus/digest.py` converts, names, structures, maps, archives, and
fills every index field except `summary` and `key topics`. It does the same thing every
time. Never do by hand what it does — never convert, move, rename, archive, write a
heading, or write a map yourself. The protocol behind it is the creator's
`dev/sourceDigestion.md`.

The grounding discipline in `CLAUDE.md` applies throughout. Summaries and key topics say
what the files actually contain — never general knowledge of the domain.

**Never read a large file whole.** A file of more than 500 lines is understood through its
map and its opening.

**Ask nothing in a normal run.** The only questions this skill may ask are the ones named
below: which assistant (only when it is unclear), an upload clash, installing MarkItDown,
and the domain tokens on a first run.

## When to use

- "Analyze the corpus", "index the new files", "I added documents — refresh the index."
- Do NOT trigger for building or refreshing a learning plan (`learningPlanner`), for
  compiling artifacts, or for ordinary questions about the material.

## Where this skill runs

In groundWork Creator: the working directory holds `.assistantTemplate/`. Building and
maintaining an assistant happens here; the assistant itself is for project assistance and
learning. Anywhere else — inside an assistant included — say in one line that this skill
runs from groundWork Creator, and stop.

Pick the assistant from `assistants/registry.md`. If exactly one assistant has files
waiting in its `src/uploads/` (ignore `.gitkeep`), go on with it — and the first line of
your first reply names it, even when that reply asks a question.
Ask only when several have files waiting, or none does — list them, and ask which. The
target is `assistants/[gW] {Token}/`.

Run the script from the creator root, passing the target. Every other path in this skill,
and in the target's `CLAUDE.md`, is relative to the target. Read the target's `CLAUDE.md`
before anything else — its rules govern this skill, and the root `CLAUDE.md` does not
replace them.

## Step 1 — Resolve the subject

Read the Token cell of the Assistant table in the target's `CLAUDE.md`. That value is
`{Subject}`; the index is `src/index.{Subject}.md`. If the cell is empty, ask for it and
stop until it is given.

## Step 2 — Check the tools

Only if `src/uploads/` holds files other than `.md` and `.csv`. Check MarkItDown is
installed for the Python that runs the script:

```
python -c "import markitdown"
```

Exit code 0 means installed. If it is not, ask whether to install it, and on confirmation
run `python -m pip install "markitdown[docx,pdf,pptx,xlsx,xls]"` — the extras carry PDF,
Word, PowerPoint and Excel support, and the PDF extra brings the library the script reads
PDF structure with. If the creator declines, report which files are waiting and stop.

## Step 3 — Plan

```
python .claude/skills/analyzeCorpus/digest.py plan "assistants/[gW] {Token}"
```

One row per upload: what will happen to it and where it will go. Nothing changes yet.
Subfolders are always mirrored. A converted file is named `{stem}.md` — never
`{stem}.pdf.md`. An upload whose name already exists in `src/md/` or `src/csv/` is an
update: the old file is archived and replaced.

**Clash** — two uploads that would get the same name (`Spec.pdf`, `Spec.docx`): ask the
creator, in one message for all clashes, which to keep or what to rename one to. Rename
or remove the upload as they say. This is the only question at this step. **Skip** rows —
unfinished downloads and lock files — are left in place and reported, not asked about.

## Step 4 — Run

```
python .claude/skills/analyzeCorpus/digest.py run "assistants/[gW] {Token}"
```

The script, file by file:

1. converts with MarkItDown, and cleans the text — one kind of line break, no ligatures —
   so line numbers match what Read shows;
2. recovers a PDF's headings from its bookmarks, else its font sizes, else its running
   page headers, and writes each with its level; a file that already has markdown
   headings is left as it is;
3. maps every file over 500 lines that has headings;
4. archives the original to `.archive/src/uploads/`, timestamped from the clock;
5. writes the index entry's mechanical fields, with `summary` and `key topics` set to
   `(to write)`. It also re-indexes any file in `src/md/` or `src/csv/` edited or dropped
   there directly, and removes the entry and map of any file that is gone.

It prints one row per file — action, lines, structure method, topics, note — and lists
every entry left `(to write)`. A `failed` row leaves its upload in place.

## Step 5 — Write the summaries and key topics

For each entry the script listed as `(to write)`, read:

- **500 lines or fewer** — the whole file;
- **more than 500 lines** — its map and its first 150 lines, never the whole file;
- **a CSV** — its columns, already in the entry, and its first 20 rows.

Then replace the two `(to write)` values in that entry, changing nothing else:

- `summary` — one line on what the document covers, drawn from its own content. A file
  that describes other documents (a source list, an index) is summarised as exactly that —
  "a list of the source documents of another assistant", say — never as a description of
  this corpus, and never used as the basis for a domain token.
- `key topics` — its main topics, comma-separated; for a mapped file, from its map. As
  many as the document supports, never padded.

Where a file is marked `none — no structure found; search it`, the summary says what kind
of document it is, so a reader knows to search it.

## Step 6 — Propose the domain tokens if they are blank

Read the Domain configuration table in the target's `CLAUDE.md`. If every value is
filled, skip this step silently and never overwrite an existing value.

If any value is empty, infer it from what you read in Step 5 and present the whole set as
one table for approval — every value, `{SCOPE}` included, is the creator's to approve.

Ground every value in the corpus itself. The basis column names the files it rests on;
`{SCOPE}` lists only topics that appear in the index's key topics. Never base a value on
what one file says about documents that are not in the corpus. The three roles are short
noun phrases — "SAP TM consultant", not a clause — because `/welcome` builds sentences
around them.

| Token | Basis for the proposal |
|---|---|
| `{DOMAIN}` | the knowledge area the documents cover |
| `{SCOPE}` | one-line boundary of what the corpus actually covers — and implicitly what it does not |
| `{LEARNER_ROLE}` | who the material appears written for |
| `{PRACTITIONER_ROLE}` | who would apply this material on a project |
| `{MAINTAINER_ROLE}` | who would keep this assistant current |
| `{KNOWLEDGE_REDIRECT}` | the authoritative source behind these documents, for concept questions the corpus cannot answer |
| `{PRACTITIONER_REDIRECT}` | where to send applied questions beyond the corpus |

Write the values the creator confirms into `CLAUDE.md`.

## Step 7 — Check

```
python .claude/skills/analyzeCorpus/digest.py check "assistants/[gW] {Token}"
```

It verifies every corpus rule: each file has one complete entry and each entry a file; no
name keeps its source extension; every large file has a map or is marked search-only;
every map row sits on its heading; line counts match; nothing is left `(to write)`; the
text is clean. Fix what it lists — by re-running Step 4 for anything mechanical, by
editing the entry for a summary — until it reports `ok`. Uploads left on purpose (a
failed conversion, an unresolved clash, a skipped file) are the only acceptable
remainder; name them in the report.

## Step 8 — Report

One table, one row per file: file, action, lines, structure, topics. Under it, one line
each for anything left in `src/uploads/` and why, and — on a first run — that the domain
tokens were written. Then the next step: `/learningPlanner`. Nothing else.

## Does not

- Convert, move, rename, archive, write headings or write maps by hand — `digest.py`
  does all of it.
- Read a file of more than 500 lines whole, or read anything in `.archive/`.
- Ask the creator to review structures or outlines. The script's method is reported, not
  approved.
- Pad the index with general domain knowledge. If the document does not cover it, it
  does not appear.
- Propose, draft, or write a learning plan or any learning artifact.
- Invoke another skill. It names the next command; the creator runs it.
- Overwrite a Domain configuration value that is already filled.

## Quality gate (silent, before Step 8)

- `digest.py check` reports `ok`, or lists only uploads left on purpose.
- Every summary and key topics value was written from the file itself, after reading it
  as Step 5 says.
- No question was asked beyond those this skill names.
