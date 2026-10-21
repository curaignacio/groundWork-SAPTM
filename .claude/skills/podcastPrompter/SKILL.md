---
name: podcastPrompter
description: Generate NotebookLM podcast prompts for every session of the learning plan into learning/podcastPrompts.{Subject}.md, collecting or confirming the podcast audience, format/tone and terminology rules in dev/config.json first. Use when the creator asks for podcast prompts or audio overview prompts. It writes prompts only — it does not generate audio.
---

# Podcast prompter

Build-time skill. It writes the prompts the creator pastes into NotebookLM to produce a
two-host audio overview per session. It generates every prompt in one pass, after the
podcast configuration is settled.

The prompts are assembled, not invented. Fixed wording comes from `dev/config.json` and
from the structure below; per-session content comes from the learning plan.

## When to use

- "Generate the podcast prompts", "make the NotebookLM prompts", "refresh the podcast
  prompts after I changed the audience."
- Do NOT trigger for producing audio, for compiling the study guide
  (`studyGuideCreator`), or for the questionnaire (`questionnaire`).

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

## Step 0 — Resolve and check

Read the Token cell of the Assistant table in `CLAUDE.md` to resolve `{Subject}`, then
read `learning/learningPlan.{Subject}.md`.

If the plan is missing or holds no session blocks, say so in one line, point the creator
at `/learningPlanner`, and stop. The format comment at the top of the plan is not a
session.

## Step 1 — Settle the podcast configuration

Read the `podcast` section of `dev/config.json`.

**If the values are empty**, collect them in conversation before anything else. Ask for
all three together, not one at a time:

| Field | What to ask for |
|---|---|
| `audience` | who the podcast is for — their role and level; offer the approved `{LEARNER_ROLE}` from `CLAUDE.md` as the default |
| `format_tone` | how it should sound; offer the default below as a starting point |
| `terminology` | pronunciation or rendering rules, as a list; e.g. `always render "S/4HANA" as "S-Four-Hannah"` |

Offer this as the default `format_tone`, and let the creator take it, edit it, or replace
it:

> natural back-and-forth; two distinct perspectives (one implementation/project-focused,
> one conceptual/framework-oriented); light and engaging; theory grounded in practice;
> prefer examples over definitions; avoid long numbers, keys, configuration paths;
> prioritize clarity over completeness

Write the confirmed values to `dev/config.json`. `terminology` is an array and may be
empty — an empty list is a valid answer, not a missing one.

**If the values are already filled**, show them back and ask whether they still apply.
On a change, update `dev/config.json` and regenerate every prompt. On confirmation,
continue without writing to the config.

This configuration is subject-specific and lives in `dev/config.json`, never in this
skill. The skill itself stays subject-agnostic.

## Step 2 — Read each session's data

For every session block in the plan, take:

- session number and title
- knowledge items
- skill items
- deliverable
- self-confidence question

Ignore `Important questions` and `Quiz questions` — they belong to the learner material
and to `questionnaire`.

## Step 3 — Identify source files and recommend a length

For each session, read `src/index.{Subject}.md` and list the source files whose topics
cover that session's knowledge items.

Use the index only. Do not open the source files themselves — file identification is the
only reason `src/` enters this skill at all.

Recommend a length from the session's knowledge item count:

| Knowledge items | Recommended length |
|---|---|
| 1–3 | short |
| 4–6 | medium |
| 7 or more | long |

## Step 4 — Assemble each prompt

Each session's prompt is one continuous block of text with every section labeled in ALL
CAPS, in this order:

```
TASK: Create an audio overview in podcast format with two hosts.

SESSION NUMBER AND TITLE: Session {NN} — {Title}

AUDIENCE: {dev/config.json → podcast.audience}

KNOWLEDGE TO ACQUIRE: {knowledge items joined with " | "}

SKILLS TO DEVELOP: {skill items joined with " | "}

DELIVERABLE: {deliverable description}

SELF-CONFIDENCE QUESTION: {self-confidence question}

FORMAT & TONE: {dev/config.json → podcast.format_tone}

TERMINOLOGY RULES: {each entry of dev/config.json → podcast.terminology, joined with "; "}

PODCAST STRUCTURE:
1. Brief opening: introduce session number and title; explain why it matters in real projects; set expectations.
2. Core discussion: connect concepts to practice and implementation; hosts clarify and challenge each other.
3. Learning focus: highlight knowledge and skills as practitioner capabilities.
4. Practice and reflection: present the deliverable; end with the self-confidence question.
5. Closing: recap the key takeaway and suggest next actions.
```

- Knowledge and skill items are joined with ` | ` on a single line — not bulleted.
- The PODCAST STRUCTURE five parts are fixed. Use the wording above identically in every
  prompt, for every session, in every subject.
- Write the prompts in `dev/config.json → learning_language`. If it is not English,
  translate the fixed wording faithfully once and use that translation identically in
  every prompt. If the setting is empty, settle it the way `learningPlanner` does before
  writing.
- Omit the `TERMINOLOGY RULES` line entirely when `terminology` is empty. Never write an
  empty label.
- Strip `(tier: inferred)` markers from the section headings you read — they are plan
  bookkeeping and do not belong in a prompt.

## Step 5 — Archive, then write

If `learning/podcastPrompts.{Subject}.md` already holds prompts, archive it first:

```
.archive/learning/{YYMMDDHHMM}.podcastPrompts.{Subject}.md
```

Read the timestamp from the system clock (`Get-Date -Format yyMMddHHmm`) at the moment of
the move — never guess it. If that name is already taken, add the seconds
(`yyMMddHHmmss`).

Then write all sessions to `learning/podcastPrompts.{Subject}.md`, in session order, below
the file's title and format comment — keep both in place:

```markdown
## Session {NN} - {Title}

### Recommended length
{length}

### Source files
- {filename}

### Prompt
{prompt}

---
```

Generate every session in this one pass. This skill does not seek session-by-session
approval — the approval happened in Step 1, on the configuration.

## Step 6 — Report

Report the output path and the session count, and note any session where the index
pointed to no source file. Then propose `/questionnaire` to compile the quiz HTML.

Propose it. Do not run it.

## Does not

- Generate audio. The prompts are for the creator to paste into NotebookLM.
- Seek session-by-session approval. Configuration is confirmed once, then all prompts are
  written together.
- Read source files for content. `src/index.{Subject}.md` is consulted only to name the
  files per session.
- Alter the learning plan, the session materials, or any compiled artifact.
- Keep subject-specific wording in this file. Audience, tone, and terminology live in
  `dev/config.json`.
- Invoke another skill. It proposes; the creator runs.

## Quality gate (silent, before Step 6)

- One block per session in the plan, in `{NN}` order, with no session skipped.
- Every prompt carries all sections in the Step 4 order, labeled in ALL CAPS.
- The PODCAST STRUCTURE wording is identical in every prompt.
- `AUDIENCE`, `FORMAT & TONE`, and `TERMINOLOGY RULES` match `dev/config.json` exactly.
- Knowledge and skill items are joined with ` | `, on one line each.
- No `(tier: inferred)` marker and no `{PLACEHOLDER}` token survives in the output.
- The recommended length matches the knowledge item count rule.
- The previous version was archived, with a clock-read timestamp prefix.
