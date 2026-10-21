---
name: assistantCreator
description: Create a new groundWork assistant by cloning .assistantTemplate/ into a [gW] {Subject}/ folder, filling the subject token, and registering it in the root CLAUDE.md. Use when the creator asks to create, set up, or start an assistant for a subject. Not for corpus work (analyzeCorpus), not for git setup or publishing (repoSync).
---

# Assistant creator

Build-time skill. Runs once per new assistant. It clones the scaffold, fills the one
token known at creation time, and records the assistant in the creator's registry. It
does not touch git and it does not invoke any other skill.

Runs in the creator root folder — the one holding `.assistantTemplate/`. If
`.assistantTemplate/` is not present in the working directory, say in one line that
this skill runs from the groundWork creator root, and stop.

## When to use

- "Create an assistant for X", "set up a new assistant for X", "start a groundWork
  for X."
- Do NOT trigger for corpus indexing (`analyzeCorpus`), learning artifacts
  (`learningPlanner` and downstream), project folders (`projectManager`), or anything
  involving git or GitHub (`repoSync`).

## Step 1 — Confirm the subject

If the subject is explicit in the request ("create an assistant for SAP TM" → `SAP TM`),
restate it and ask the creator to confirm. If no subject was given, ask for one — that
question only, nothing else.

**Confirm the subject before filling any token or creating any file or folder.** This is
not optional and not skippable, even when the subject seems obvious: the name becomes
the folder name, the registry key, and five filenames, and renaming it afterwards is
manual work.

Use the subject exactly as the creator confirms it, including capitalisation. Do not
normalise, expand, or abbreviate it.

**Forbidden characters.** If the subject contains a character Windows forbids in a name —
`\ / : * ? " < > |` — or ends in a space or a period, do not substitute silently. Propose
a replacement, each forbidden character swapped for a hyphen (`SAP S/4HANA` →
`SAP S-4HANA`), and ask the creator to confirm it or give their own. The confirmed name
becomes the subject everywhere — folder, Token, registry, and the five filenames —
because every skill builds file paths from the Token, so it must be safe as a name. The
original spelling can live in `{DOMAIN}`, which is only ever displayed.

## Step 2 — Check whether it already exists

Check for `assistants/[gW] {Subject}/`. Every assistant lives in the creator's
`assistants/` folder.

- **If it exists:** create nothing. Tell the creator the folder is already there, report
  its path, and orient them to the next step based on what the folder contains — whether
  `src/uploads/` has unprocessed files, whether `src/index.{Subject}.md` has been
  written, whether a learning plan exists. Then stop.
- **If it does not exist:** the confirmed subject is the go-ahead — create it without
  asking again.

## Step 3 — Clone the scaffold

Copy the entire contents of `.assistantTemplate/` into a new folder
`assistants/[gW] {Subject}/`.

Preserve the structure exactly — every folder, every `.gitkeep`, the `.claude/` folder
with its skills and `settings.json`, and the dotfiles (`.gitignore`, `.archive/`). The new
folder goes inside `assistants/`, never inside `.assistantTemplate/` and never at the
creator root.

Do not edit file contents during the copy. Filling happens in the steps below.

## Step 4 — Fill the subject token

Three things carry `{Subject}`: the assistant's `CLAUDE.md`, its `README.md`, and five
filenames.

**In `[gW] {Subject}/README.md`** — replace every `{Subject}`. The README is what end
users see on the repository's GitHub page.

**In `[gW] {Subject}/CLAUDE.md`** — replace `{Subject}` in the title and in the Token
column of the Assistant table. Leave Repo and Maintainer empty, and leave every Domain
configuration value empty.

**Rename these five files**, replacing `{Subject}` with the confirmed subject:

| From | To |
|---|---|
| `src/index.{Subject}.md` | `src/index.{Subject-value}.md` |
| `learning/learningPlan.{Subject}.md` | `learning/learningPlan.{Subject-value}.md` |
| `learning/podcastPrompts.{Subject}.md` | `learning/podcastPrompts.{Subject-value}.md` |
| `learning/studyGuide.{Subject}.html` | `learning/studyGuide.{Subject-value}.html` |
| `learning/questionnaire.{Subject}.html` | `learning/questionnaire.{Subject-value}.html` |

Rename the files only — do not alter their contents. The `{Subject}` tokens inside those
scaffolds are part of their format comments.

**Do not fill `{Subject}` into the SKILL.md files.** The skills are subject-agnostic by
design: each one reads the subject from `CLAUDE.md` at runtime when it needs a literal
filename. Filling them would make every assistant's skills unportable.

## Step 5 — Leave local settings to /welcome

Do not create `dev/local.json`. It holds one person's preferences and setup status on one
machine, so `/welcome` creates it on first use. If the scaffold copy brought one along,
delete it from the new assistant. It is gitignored, and `repoSync` never pushes or pulls
it.

## Step 6 — Fill the subject in the welcome copy

In `dev/welcome.json`, replace `{Subject}` with the confirmed subject.

Leave every other token — `{DOMAIN}`, `{SCOPE}`, `{LEARNER_ROLE}`,
`{PRACTITIONER_ROLE}`, `{MAINTAINER_ROLE}` — exactly as they are. Those are resolved by
`welcome` at display time from `CLAUDE.md`, which is their single source of truth. They
are blank at creation and `analyzeCorpus` proposes them on its first run; baking them in
here would freeze them empty.

## Step 7 — Verify the .gitignore

Confirm the new `.gitignore` keeps local what must stay local — `dev/local.json`,
`.claude/settings.local.json`, the contents of `learning/session notes/`, and the
contents of `projects/`, everything in `.archive/` but its `.gitkeep` files, and the
contents of `src/uploads/`. The scaffold already contains all six.

Where an entry is present, change nothing — do not append a duplicate. Add an entry only
if it is genuinely missing.

## Step 8 — Register the assistant

Add one row to the table in `assistants/registry.md`:

| Column | Value |
|---|---|
| Token | the confirmed subject |
| Repo | leave empty |
| Maintainer | leave empty |

There is no location column: an assistant always lives at `assistants/[gW] {Token}/`.
Repo and Maintainer belong to `repoSync` and are filled on first push. Never guess them.

Change nothing else in the registry, and never modify the root `CLAUDE.md`, the root
`.claude/` folder, or `.assistantTemplate/`.

## Step 9 — Report and orient

Report the created path in one line, then the next two steps in plain language:

1. Drop source files into `assistants/[gW] {Subject}/src/uploads/`
2. Run `/analyzeCorpus`

Nothing else — no checklist, no summary of what was done. Do not elaborate unless asked.

## Does not

- Fill Repo or Maintainer, in the assistant's `CLAUDE.md` or the registry — `repoSync`
  owns both.
- Initialise a git repository, or run any git command. `repoSync` owns all git setup.
- Invoke any other skill. It names the next command; the creator runs it.
- Modify `.assistantTemplate/`, the root `.claude/skills/` files, or any existing
  assistant folder.
- Fill the Domain configuration tokens. They are the creator's to fill or
  `analyzeCorpus`'s to propose.

## Quality gate (silent, before Step 9)

Run these checks internally. They are never shown to the creator.

- The subject was explicitly confirmed by the creator — never assumed from context.
- The subject contains no character Windows forbids in a name; any replacement was
  proposed and confirmed, not applied silently.
- The new assistant is at `assistants/[gW] {Subject}/` — not at the root, not inside
  `.assistantTemplate/`.
- Internal structure matches the scaffold exactly: no file added, removed, or edited
  beyond `CLAUDE.md`, `README.md`, `dev/welcome.json`, and the five renames, and no
  `dev/local.json`. No `{Subject}` remains in `README.md`.
- All five `{Subject}` filenames were renamed; no `{Subject}` remains in any filename.
- `CLAUDE.md` Repo, Maintainer, and all Domain configuration values are still empty.
- `assistants/registry.md` has exactly one new row, with Repo and Maintainer empty.
- No git command was run and no other skill was invoked.
