---
name: sessionWrite
description: Write the expanded study material for each session of the learning plan — theory, processes and practical content for every knowledge item — one approved session at a time into learning/study guides/{NN} - {Session Title}.md. Use when the creator asks to write session materials or study content. Not for building the plan (learningPlanner) and not for compiling the study guide HTML (studyGuideCreator).
---

# Session write

Runtime skill. It runs after the learning plan is complete. For each session it expands
the plan's knowledge items into study material a learner can actually read and learn
from, one approved session at a time.

It writes the markdown that `studyGuideCreator` compiles. It never compiles HTML itself,
and it never changes the plan.

The grounding discipline in `CLAUDE.md` applies throughout. The plan tells you what a
session covers; the source files tell you what is true about it. Explanations trace to
`src/`. Where the corpus is thin on a knowledge item, write the short honest version and
say what the material does not establish — never fill the gap from general knowledge of
the domain.

## When to use

- "Write the session materials", "write the study content", "rewrite session 04."
- Do NOT trigger for building or revising the plan (`learningPlanner`), compiling the
  study guide HTML (`studyGuideCreator`), or generating quiz items (`questionnaire`).

## Where this skill runs

In groundWork Creator: the working directory holds `.assistantTemplate/`. Building and
maintaining an assistant happens here; the assistant itself is for project assistance and
learning. Anywhere else — inside an assistant included — say in one line that this skill
runs from groundWork Creator, and stop.

Read `assistants/registry.md`. If only one assistant is registered, go on with it — the
first line of your first reply names it, even when that reply asks a question. If
several are, list them and ask which.
The target is `assistants/[gW] {Token}/`.

Every path in this skill, and in the target's `CLAUDE.md`, is relative to the target. Read
the target's `CLAUDE.md` before anything else — its rules govern this skill, and the root
`CLAUDE.md` does not replace them.

## Step 0 — Confirm the plan exists

Read the Token cell of the Assistant table in `CLAUDE.md` to resolve `{Subject}`, then
read `learning/learningPlan.{Subject}.md`.

If the plan is missing or holds no session blocks, say so in one line, tell the creator to
run `/learningPlanner` first, and stop. The format comment at the top of the plan is not a
session.

Note which sessions already have a file in `learning/study guides/` so you know where to
resume.

Write the material in `dev/config.json → learning_language`. If it is empty, settle it the
way `learningPlanner` does — propose the sources' language if they are consistent, ask if
they are mixed, confirm with the creator, and record it — before writing anything.

## Step 1 — Propose one session's material

Take the next session without a study guide file — or the session the creator named.

Read the plan's block for that session, then read the parts of the `src/` files that
cover its knowledge items — for a large file, its topic map in `src/sections/` shows where
each topic starts; never read a large file whole. Write the expanded material and present
it for approval.

Structure every session file the same way:

```markdown
# Session {NN} — {Session Title}

## Overview
{short paragraph: what this session covers and why it matters in practice}

## {Knowledge item 1}
{expanded explanation — the theory, the process, and how it shows up in practice}

## {Knowledge item 2}
{expanded explanation}

## Practice
{the session's deliverable from the plan, written as a task the learner can do}

## Self-check
{the session's self-confidence question from the plan}
```

- One `##` section per knowledge item, in the plan's order, using the knowledge item as
  the heading. Every knowledge item in the plan gets a section — none dropped, none added.
- Expand with theory, process, and practical content. Depth follows what the source
  supports, not a target length.
- `Practice` and `Self-check` carry the plan's deliverable and self-confidence question.
  Do not invent new ones.
- Do not carry the `(tier: inferred)` markers into this file, and do not reproduce the
  plan's `Important questions` or `Quiz questions` sections — those belong to the plan and
  to `questionnaire`.

## Step 2 — Wait for approval

Wait for the creator to approve or adjust. Incorporate adjustments and re-present if the
change is substantial. **Write nothing until the session is approved.**

## Step 3 — Archive, then write

Before writing, archive **every** file in `learning/study guides/` whose name starts with
`{NN} - ` — the same session number, whatever its title. A session retitled through
`learningPlanner` keeps its number, so the old file has a different name and must still
be cleared, or the study guide shows the session twice. Move each one to

```
.archive/learning/study guides/{YYMMDDHHMM}.{existing name}.md
```

where `{existing name}` is the archived file's own name without `.md`. Read the timestamp
from the system clock (`Get-Date -Format yyMMddHHmm`) at the moment of the move — never
guess it. If that name is already taken, add the seconds (`yyMMddHHmmss`).

Then write the approved material to `learning/study guides/{NN} - {Session Title}.md`.

The filename's `{NN}` and `{Session Title}` match the plan's session block exactly, except
for a forbidden-character replacement confirmed with the user under the naming rule in
`CLAUDE.md`. The `# ` heading inside the file always keeps the plan's original title —
`studyGuideCreator` orders panes by the filename's number and labels them from that
heading.

Then return to Step 1 for the next session.

## Step 4 — Propose the next skill

When every session in the plan has a file, report the folder path and the session count,
then propose `/studyGuideCreator` to compile the study guide HTML.

Propose it. Do not run it.

## Does not

- Write, or partially write, any session before the creator approves it.
- Modify `learning/learningPlan.{Subject}.md` in any way. If the plan looks wrong while
  writing, say so and point the creator at `/learningPlanner` — do not fix it here.
- Compile any HTML. That is `studyGuideCreator`.
- Generate or alter quiz questions. Those live in the plan and belong to `questionnaire`.
- Invent a deliverable or self-confidence question. Both come from the plan.
- Invoke another skill. It proposes; the creator runs.
- Delete a previous version. Superseded files are archived, never discarded.

## Quality gate (silent, before each write)

- Every knowledge item in the plan's session block has its own `##` section, in order.
- Every explanation traces to a source file; gaps are stated rather than filled.
- `Practice` and `Self-check` match the plan's deliverable and self-confidence question.
- No `(tier: inferred)` marker and no `Quiz questions` block appear in the file.
- The filename's number matches the plan; its title matches too, apart from any confirmed
  forbidden-character replacement. The `# ` heading carries the original title.
- Every previous file for this session number was archived before the write, whatever its
  title, with a clock-read timestamp prefix. No other file in `learning/study guides/`
  starts with the same `{NN} - `.
