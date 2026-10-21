---
name: sessionNotes
description: Turn a user's post-study reflection into structured notes — what was understood, what was unclear, questions that came up, next steps — written to learning/session notes/ as a dated personal file. Use after a study session when the user wants to capture how it went, including reflections from a chatQuiz in the same conversation. Personal and gitignored; unrelated to project work.
---

# Session notes

Runtime skill, conversational. It structures the user's own reflection after studying a
session into a note they keep. The notes are personal: the folder is gitignored and
nothing here is ever pushed.

The content comes from the user, not from the source material. This skill is not a
summary of the session — it is a record of how the session landed for this person.

## When to use

- "Write up my notes", "capture how that session went", "note what I struggled with",
  after a study session or a `/chatQuiz` run.
- Do NOT trigger for project notes or meeting notes (`projectAssistant`), for writing
  study material (`sessionWrite`), or for quizzing (`chatQuiz`).

## Step 1 — Identify the session

Resolve `{Subject}` from the Token cell of the Assistant table in `CLAUDE.md`, then read
`learning/learningPlan.{Subject}.md` for the session numbers and titles.

Work out which session the reflection is about from the conversation. If it is not clear,
ask — one question. Confirm the number and title against the plan so the filename matches
the rest of the system.

## Step 2 — Gather the reflection

Draw the content from the conversation. Four things to capture:

- **what was understood** — what now makes sense that did not before
- **what was unclear** — the parts that remain shaky, in the user's own framing
- **questions that came up** — anything they want answered, whether or not it was resolved
- **next steps** — what they intend to do next

If the conversation already contains the material — a `/chatQuiz` run in this same chat,
or the user talking through the session — use it. Where a quiz exposed a gap, fold that
in: a missed question is a genuine signal of what is unclear.

Ask only for what is actually missing, and ask it in one pass rather than interrogating
the user field by field. A short honest note is better than a padded one — if the user
has nothing to say under a heading, leave it out rather than inventing it.

## Step 3 — Confirm, then write

Show the structured note for the user to approve or adjust. On approval, write:

```
learning/session notes/[notes] {NN} - {Session Title} - {YYYY-MM-DD}-{SUFFIX}.md
```

- `{NN}` and `{Session Title}` match the plan's session block. If the title holds a
  character Windows forbids in a filename, follow the naming rule in `CLAUDE.md` — propose
  a replacement and confirm it with the user. The `# ` heading inside the file keeps the
  original title.
- `{YYYY-MM-DD}` is the date of the study session — today's when the conversation shows
  the studying happened now, as after a `/chatQuiz` in this chat. If the user indicates
  they studied on another day, confirm the date with them rather than assume. Date only —
  never a time.
- `{SUFFIX}` is `00`, or the next free number (`01`, `02`, …) if a note for that session
  already exists for that date.

File contents:

```markdown
# Session {NN} — {Session Title}
Notes from {YYYY-MM-DD}

## What I understood
- {point}

## What was unclear
- {point}

## Questions that came up
- {question}

## Next steps
- {action}
```

Omit any heading the user had nothing for. Keep their wording — this is their record, not
a rewrite of it.

## Step 4 — Report

Report the file path in one line. Note that the file is local and gitignored, so it is not
pushed to GitHub — mention this only on the first note written in a conversation.

## Does not

- Link to, read, or update anything in `projects/`. Session notes and project work are
  entirely separate.
- Modify any source file or learning artifact — not `src/`, not the plan, not the study
  guides, not the compiled HTML.
- Carry state between conversations. Each invocation produces one standalone file.
- Overwrite an existing note. Same-day notes get the next free suffix.
- Summarise the session's material in place of the user's reflection.
- Push or sync anything. The folder is gitignored by design.

## Quality gate (silent, before Step 3)

- The session number and title match a session in the learning plan.
- Every point in the note came from the user or from this conversation.
- No heading is padded with invented content, and empty headings are omitted.
- The filename carries today's date and a free suffix.
