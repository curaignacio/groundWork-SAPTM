---
name: projectManager
description: Manage project and item structure — create a project (its tokens, and .{Folder}/ with templates/ and userGuides/) and its items with their full structure, classify files dropped into a project's or an item's uploads/ by role (template, writing guide, rule, foundation, example, draft, personal, or the item's requirement), write their text copies, keep the project and item indexes, and archive finished projects or items. Use when the user asks to create a project or item, has dropped files for one, or says a project or item is finished. Not for meeting notes, decisions, open questions, drafts or deliverables — that is projectAssistant.
---

# Project manager

Runtime skill. It owns project *structure*: folders, file classification, and the index
files. It does not do project *work* — meeting notes, decisions, open questions, drafts,
and deliverables all belong to `projectAssistant`.

The grounding discipline in `CLAUDE.md` applies, plus the project rules this skill exists
to enforce: project material is grounded only within its own project, never merged into
general knowledge from `src/`, and never carried from one project into another.

## When to use

- "Create a project for X", "set up item 3521811", "I dropped files in the uploads
  folder", "scan the uploads", "that project is finished — archive it."
- Do NOT trigger for meeting notes, decisions, open questions, drafts, or deliverables
  (`projectAssistant`). Do NOT trigger for the knowledge corpus (`analyzeCorpus`) or any
  learning artifact.

## Structure

```
projects/{Folder}/
├── project.{ABBR}.md                tokens, delivery language, item list
├── index.{ABBR}.md                  index of the project's own files, in .{Folder}/
├── uploads/                         landing zone for files that apply to the whole project
├── .{Folder}/                       the project's own files, shared by every item
│   ├── templates/                   every template; each item picks one
│   └── userGuides/                  the ways of working: writing guides, rules, project-wide foundations
└── {Item ID} - {Item Title}/
    ├── req.{Item ID}.md             the approved requirement — see projectAssistant
    ├── openQuestions.{Item ID}.md   O-prefix entries, managed by projectAssistant
    ├── decisions.{Item ID}.md       D-prefix entries, managed by projectAssistant
    ├── index.{Item ID}.md           item index
    ├── context/                     this item's foundations and examples
    ├── meetings/                    [meeting] {Title} {YYYY-MM-DD}-{SUFFIX}.md
    ├── drafts/                      {NN}.draft.{Item ID}.md
    ├── deliverables/                finished outputs
    ├── personal/                    the user's own files — hands off
    └── uploads/                     landing zone for this item's files
```

`{ABBR}` is the project's abbreviation, chosen by the user. It appears in those two file
names only. `.{Folder}/` takes the project's folder name — `projects/Aurora/.Aurora/`.
Some search tools skip folders whose name starts with a dot: reach its files through
`index.{ABBR}.md` and their exact paths, and list it with `Get-ChildItem -LiteralPath`. **Item IDs are the client's own** — the number the client uses for the
feature or problem in their repository and calls. Never prefix one with the abbreviation
unless the user asks.

**Project material never leaves this machine.** `projects/` and `.archive/` are
gitignored, so client documents are never pushed, whatever else is published. Colleagues
on the same client share files the way they normally would, outside the assistant.

**`personal/` and `.archive/` are hands off.** The assistant's `.claude/settings.json`
blocks Claude's file tools from reading or editing anything in them. Never try to read,
edit, summarise, or use a file there — not even to check it. Moving a file *into* either
folder is the only operation this skill performs on them. Personal files exist per item
only.

**Project files are read through a text copy.** The original is the record and stays
where it was filed. Beside it, `digest.py` writes `{stem}.md` — its text, with headings
recovered — and that copy is what you read, search, and quote, never the original. Run it
on every filed file except Personal ones:

```
python .claude/skills/analyzeCorpus/digest.py text "{file}" ["{file}" ...]
```

It handles PDF, Word, Excel and PowerPoint; Markdown, plain text, CSV, JSON, XML, HTML and
images are read as they are and get no copy. It prints one row per file. On a row that
says:

- **no text found** — the PDF is a scan. Ask the user for its pages as images (PNG or
  JPG), which you can read; index it with `summary: (scan — pages requested as images)`.
- **clash** — a file of that `.md` name already sits there. Ask the user to rename one.
- **failed** — corrupt or password-protected. Tell the user, and index it with
  `summary: (could not be read)`.

If MarkItDown is missing (`python -c "import markitdown"` fails), tell the user to run
`/welcome`, which sets it up, and stop.

A file whose name ends in `.crdownload`, `.part`, or `.tmp` is an unfinished download:
flag it, and do not classify it until the complete file arrives.

**No `.gitkeep` inside a project.** `projects/` is gitignored — only `projects/.gitkeep`
itself is committed, so the empty folder ships — and nothing inside it ever is. Create
every project and item folder empty.

## File roles

Every file is tagged with one role. The role says what the work takes from the file, and
whether it can win a conflict:

| Role | Files | Where | What is taken from it | On a conflict |
|---|---|---|---|---|
| **Structure** | templates, writing guides | `.{Folder}/templates/`, `.{Folder}/userGuides/` | shape only — sections, fields, order, what each part must contain. Never a source | does not compete |
| **Requirement** | `req.{Item ID}.md` — one per item | item | scope and business rules | 1st |
| **Decision** | `decisions.{Item ID}.md` — one per item | item | what has been agreed | 2nd |
| **Rule** | client standards and procedures | `.{Folder}/userGuides/` | how it must be done, for every item | 3rd — never changes scope |
| **Foundation** | earlier work this builds on — a previous FS, an existing design | `context/`, or `.{Folder}/userGuides/` if project-wide | the base the work continues or extends | 4th |
| **Example** | past work elsewhere, under other conditions | `context/` only — an example belongs to one item | patterns to adapt | never — differences are named as adaptations |
| **Draft** | drafts | `drafts/` | only the sections the user approved | never a source |
| **Personal** | the user's own files | `personal/` | nothing | — |

Requirement and Decision are files the system keeps, not tags a dropped file can take: a
dropped requirement document is copied into `req` and archived, and decisions come only
from the conversation. How `projectAssistant` and `CLAUDE.md` apply the ranking is
described there.

## Resolving which project and item

Before acting, know what the user means.

- If they name it, use it. If no folder exists, treat it as a create request.
- If they do not name it and exactly one project (or item) exists, use that one.
- If several exist, ask which — briefly, listing the names.
- Never act across projects and never guess when it is ambiguous.

## Creating a project

Ask for the four tokens **in one message**, pre-filling whatever the request already
gave, and create nothing until the user has approved every value:

```
To set up the project, I need four values — confirm or change each:

1) Folder name   — {pre-filled with the project name}
2) Project name  — {…}
3) Client name   — {…}
4) Abbreviation  — {a 3–4 character proposal}, used in the names of the project's
                   two files: project.{ABBR}.md and index.{ABBR}.md
```

The folder name usually equals the project name; it differs only when two projects share
a name. If a value holds a character Windows forbids in a name, follow the naming rule in
`CLAUDE.md`: propose a replacement and confirm it.

Then create `projects/{Folder}/` with `uploads/`, `.{Folder}/templates/`,
`.{Folder}/userGuides/`, `index.{ABBR}.md` (its heading only), and `project.{ABBR}.md`:

```markdown
# {Project name} — Project
Last updated: YYYY-MM-DD

| Token | Value |
|---|---|
| Folder | {Folder} |
| Project | {Project name} |
| Client | {Client name} |
| Abbreviation | {ABBR} |

Delivery language:

## Items

| Item ID | Title | Status | Delivery language |
|---|---|---|---|
```

Reply with the path in one line, then one line each on what the three folders are for:
`uploads/` for files that apply to the whole project, not one item — the system files
and indexes them; `.{Folder}/templates/` for the client's templates, one of which each
item will use; `.{Folder}/userGuides/` for the ways of working — writing guides, client
standards and procedures, and earlier work the whole project builds on. They may stay
empty. Do not create any item folder yet.

## Creating an item

**Never infer an Item ID or a title.** Both appear in the folder name and in four
filenames; renaming afterwards is manual work. If the user gave both explicitly, create
the item and restate both in the reply's first line. If either is missing, or would have
to be taken from context, ask for it before creating anything. If either holds a
character Windows forbids in a name, follow the naming rule in `CLAUDE.md`: the folder
and filenames use the confirmed replacement, while `project.{ABBR}.md` and the file
headings keep the original.

Then create `{Item ID} - {Item Title}/` with the **full structure above, all at once** —
every folder and every file, even those that start empty. Item folders are never built up
retroactively.

- `req.{Item ID}.md` is created **empty**. It is populated only through
  `projectAssistant`, with double-confirmation.
- `openQuestions.{Item ID}.md` and `decisions.{Item ID}.md` are created with their
  heading and archive section so `projectAssistant` has the shape to append into:

```markdown
# {Item ID} — Open questions
Last updated: YYYY-MM-DD

## ARCHIVE — Closed and Obsolete Questions
## Do not use as active context. For historical reference only.
```

```markdown
# {Item ID} — Decisions
Last updated: YYYY-MM-DD

## ARCHIVE — Superseded Decisions
## Do not use as active context. For historical reference only.
```

- `index.{Item ID}.md` is created with its heading only.

Then add a row to `project.{ABBR}.md` with the Item ID, title, status `active`, and an
empty delivery language.

### Reply after creating an item

Report the path in one line, then ask for the two things the work starts from — in the
user's language, in one message:

1. **The approved requirement.** Say that `req.{Item ID}.md` exists and is empty, and ask
   for the requirement as the client approved it — typically *what* is needed, *why*, and
   the *proposed solution*, but in whatever structure the client's standards use. The
   user can paste it in chat, write it into the file themselves, or drop it as a document
   in the item's `uploads/`.
2. **The delivery language** for this item's drafts and deliverables. If the project
   already has one recorded, ask whether it applies to this item too.

Record the language in `project.{ABBR}.md`: on the item's row, or on the project's
`Delivery language:` line if the user says it applies to every item. Leave the item's
cell blank when it follows the project. The requirement itself is written under
`projectAssistant`'s rules, never by this skill — but when the user answers with it, hand
over in the same reply: show the text that would go into `req.{Item ID}.md` and ask for
the confirmation, as `projectAssistant` does. **Never send the user to run another
command** to continue work already in hand.

## Scanning uploads and classifying

Scan the `uploads/` the user means — the project's or an item's — for files not already
in its index. If there are none, say so and stop.

For each new file, ask the user its role. **Batch all new files into one turn** — one
question block per file — rather than a round trip each. In an **item's** `uploads/`:

```
How should I treat {filename}?

A) Template     — the structure of a deliverable
B) Writing guide — what the document's parts must contain
C) Rule         — a client standard or procedure that applies to every item
D) Foundation   — earlier work this item builds on
E) Example      — past work elsewhere, to adapt
F) Draft        — work in progress on this item
G) Personal     — keep it with the item; I will never open, edit, or use it
H) Requirement  — the client's approved requirement for this item
```

In the **project's** `uploads/`, offer A to D only, with D worded for the whole project —
earlier work every item builds on. Examples belong to one item: a file the user calls an
example at project level is asked about again, for the item it belongs to. Offer H only
while `req.{Item ID}.md` is empty; when it already has content, a requirement document is
a replacement — say so and ask whether it replaces the current one.

**Never guess a role, and never read a file to decide it.** The user gives every file's
role. When they already named it — "the Mexico FS, an example" — take it and restate it in
the filing report; ask only about the files whose role they did not give. In the same
turn, flag any unfinished download as described above.

Then, in the same turn as the answer, move each file, write its text copy, and index it.
**Every classified file leaves `uploads/`.** Only an unfinished download, an unresolved
clash, or a Requirement waiting for its double-confirmation may still be there afterwards.

| Answer | Moves to | Indexed in |
|---|---|---|
| A) Template | `.{Folder}/templates/` — templates are shared; each item picks one | `index.{ABBR}.md` |
| B) Writing guide | `.{Folder}/userGuides/` | `index.{ABBR}.md` |
| C) Rule | `.{Folder}/userGuides/` — a rule binds every item | `index.{ABBR}.md` |
| D) Foundation | the item's `context/` — from the project's uploads, `.{Folder}/userGuides/` | the item's index — or `index.{ABBR}.md` |
| E) Example | the item's `context/` | the item's index |
| F) Draft | the item's `drafts/`, keeping its name | the item's index |
| G) Personal | the item's `personal/`, unread | the item's index, by name only |
| H) Requirement | handed at once to `projectAssistant`, which proposes its text for `req.{Item ID}.md` from the text copy, writes it on double-confirmation, and archives the original and its copy | — |

Write the text copy right after the move, so it sits beside the filed original. A
Requirement gets its copy where it is, in `uploads/`.

### Summaries and use lines

The role is the user's; the summary and the `use` line are yours. Once the files are
filed, read each one's text copy — except Personal and Requirement files — and write:

- **summary** — one line on what the document contains.
- **use** — one line on what the work takes from it, by role. A template: its sections,
  and which carry tables or required fields. A writing guide: what it requires of which
  parts. A rule: what it binds. A foundation: what the work keeps and what it extends. An
  example: what applies here and what does not.

**Never ask the user to summarise a file.** For a long document, read its opening and its
headings (`#` lines), not the whole file. Show the summaries and use lines in the same
reply, so the user can correct one — do not ask for approval. If a file covers more than
this item — several features, several flows — say what it covers and ask which part
applies, as options, and record the answer in its `use` line.

### Files placed directly in a folder

A file that appears in `context/`, `drafts/`, `deliverables/`, `.{Folder}/templates/`, or
`.{Folder}/userGuides/` without passing through `uploads/` stays where it is. Ask its role —
the folder alone does not say — then write its text copy and index it. A text copy that
`digest.py` wrote is part of its original's entry; never index it on its own. A file the
user places in `personal/` themselves is indexed by name only.

## The index files

**`index.{Item ID}.md`** and **`index.{ABBR}.md`** — one entry per file, in the order
added. Update an entry in place when a file is reprocessed; never duplicate it.

```markdown
# {Item ID} — Item index                      (or: # {Project name} — Project index)
Last updated: YYYY-MM-DD

## {filename.ext}
- role: template | writing guide | rule | foundation | example | draft | personal
- location: {path relative to this index's folder}
- format: {original format, e.g. PDF}
- text: {path of the text copy, or "the file itself"}
- status: active | superseded
- summary: {one line on what the document contains}
- use: {one line on what the work takes from it}
```

`location` is relative to the folder the index sits in — `context/spec.pdf` in an item,
`.Aurora/userGuides/standards.pdf` in the project. Foundations and examples share
`context/`, and writing guides, rules and foundations share `userGuides/`, so the `role`
is the only thing that tells them apart: never leave it blank, and never infer it from
the folder. The project index lists only files in `.{Folder}/`; an example never appears
in it.

A **personal** entry carries only `role: personal` and `location` — no format, text,
status, summary, or use, because the file is never read or copied.

Where a document is table-heavy or numeric, note it in the summary so numeric claims get
verified against the original rather than paraphrased.

**`project.{ABBR}.md`** — the tokens, the item list, status, and delivery language. Keep
`Last updated` current. Status is `active`, `on hold`, `closed`, or `archived`; use the
user's own wording when they give one. An item's blank delivery language means it follows
the project's.

Dates are `YYYY-MM-DD`, with no time.

## Archiving

Archiving removes material from active retrieval, so it needs an explicit, unambiguous
request. **Do not archive on an offhand mention** — "that Acme thing wrapped up" is not a
request. Confirm the name, and confirm that archiving rather than just marking it closed
is what the user wants.

**The archive mirrors the live tree.** Folders keep their names; only files are renamed,
with a timestamp prefix:

```
{YYMMDDHHMM}.{file name}.{extension}
```

Read the timestamp from the system clock (`Get-Date -Format yyMMddHHmm`) at the moment of
the move — never guess it. A file that already starts with an archive timestamp keeps it.
If the prefixed name is already taken, add the seconds (`yyMMddHHmmss`).

- **A single item:** move every file in `projects/{Folder}/{Item}/` to the same relative
  path under `.archive/projects/{Folder}/{Item}/`, each renamed with the prefix, and
  create any folder the path needs. Then set the item's status to `archived` in
  `project.{ABBR}.md`.
- **A whole project:** do the same for everything left in `projects/{Folder}/` — its
  remaining items, `.{Folder}/` with both its folders, both project files, and `uploads/`. The items
  join any already archived under `.archive/projects/{Folder}/`, side by side.

If an archive folder for that project or item already exists — from earlier archived
files or items — move into it. The timestamps keep every file distinct. When the move is
complete, remove the emptied folders from `projects/`.

Once archived, everything is read-only history. Never read from `.archive/`.

## Grounding rules this skill enforces

Check a file's role in its index before using it — the folder does not say which it is.

- **Structure** — governs shape, never substance. Its content is not inherited as fact.
- **Requirement** — the source of truth for scope and business rules. Every other file is
  read against it, and none overrides it.
- **Decision** — what has been agreed; it refines the requirement, never silently
  replaces it.
- **Rule** — binds how the work is done on every item of the project; it never changes an
  item's scope.
- **Foundation** — the base the work builds on: what it states holds unless the
  requirement or a decision changes it, and any such change is stated explicitly.
- **Example** — read for pattern and analogy, never authoritative: how a solution was
  applied elsewhere, under other conditions. When drawing on one, say so. Never inherit
  its decisions as constraints. Where it differs from the requirement, say so explicitly,
  the requirement's position first.
- **Draft** — work in progress. Only the sections the user approved are content.
- **Personal** — never read, never used.
- **Isolation** — one project's material never informs another's answer or output.
- The knowledge corpus and a project's files are separate authorities. A project document
  never becomes general knowledge, and general knowledge never overrides a project's
  requirement, decisions, rules, or foundations for that project's own questions.

## Does not

- Process meeting notes, record decisions, track open questions, or write drafts or
  deliverables by its own rules — those are `projectAssistant`'s. When the work needs one,
  follow `projectAssistant` for that step in the same conversation; never send the user to
  run it.
- Write to `req.{Item ID}.md`. It creates the file empty and never touches it again.
- Create a project before all four tokens are approved, or an item folder partially.
- Prefix an Item ID with the abbreviation unasked.
- Archive on an ambiguous or offhand mention.
- Read, edit, or summarise anything in `personal/` or `.archive/`.
- Classify a file on the user's behalf, or read it to decide.
- Read an original PDF, Word, Excel or PowerPoint file — it reads the text copy.
- Write a text copy of, or read, a Personal file.
- Timestamp a folder name.

## Quality gate (silent, before delivering)

Run these checks internally. They are never shown to the user.

- The right project and item were resolved without guessing.
- A new project's four tokens were each approved by the user before anything was created.
- Item ID and title were both given explicitly by the user — never inferred — and the
  reply restated them.
- A new item has all ten entries of the structure, with `req` empty and the two tracking
  files carrying their archive headers — and the reply asked for the requirement and the
  delivery language.
- No folder or file name holds a forbidden character; any replacement was confirmed.
- Every filed file has an entry in the right index, with a role, and — unless personal —
  format, text, status, summary, and use.
- Every filed file other than a Personal one has its text copy, or its row said why not.
- Every summary and use line was written from the text copy; none was asked of the user.
- `uploads/` holds nothing but unfinished downloads, unresolved clashes, and a requirement
  awaiting its double-confirmation.
- No `.gitkeep` was created inside a project.
- No role was assumed, and no file was read to decide one.
- Nothing in `personal/` or `.archive/` was read.
- `project.{ABBR}.md` has a row per item with a current status and delivery language.
- Any archive move kept every folder name, prefixed every file with a clock-read
  timestamp, and was explicitly confirmed.
