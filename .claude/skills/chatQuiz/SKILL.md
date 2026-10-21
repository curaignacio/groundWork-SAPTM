---
name: chatQuiz
description: Run an adaptive quiz in the conversation on any topic from the source materials — one question at a time, nothing written to disk. Use when the user asks to be quizzed or tested ("quiz me on X", "test me"). Scopes to specific sessions if the user references the learning plan. Not for generating the quiz HTML file (that is questionnaire).
---

# Chat quiz

Runtime skill, conversational and ephemeral. It runs a quiz in the chat — no files, no
HTML, nothing written to disk. It is the quick "just test me" outlet, distinct from
`questionnaire`, which compiles a persisted artifact.

The grounding discipline in `CLAUDE.md` applies. Stems, correct answers, and explanations
trace to the source material. Distractors are the single ungrounded exception: plausible,
parallel in form, not source-bound.

## When to use

- "Quiz me on {topic}", "test me", "ask me some questions about {topic}", "quiz me on
  session 03."
- Do NOT trigger when the user wants a quiz **file** (`questionnaire`), when they are
  building the plan (`learningPlanner`), or when they want to write up notes
  (`sessionNotes`).

## Scope — where the questions come from

- **Default: source-direct.** The user names any topic. Read `src/index.{Subject}.md` to
  find which files cover it, then read only the sections that cover the topic — a large
  file's topic map in `src/sections/` shows where each starts. Never read a large file
  whole. No learning plan is required.
- **If the user references the plan or its sessions** — "quiz me on session 03", "test me
  on the settlement sessions" — scope to those sessions: read
  `learning/learningPlan.{Subject}.md` for the session's knowledge items, and draw on its
  `### Quiz questions` block if useful. Still re-ground against `src/`; never carry an
  item the source does not support just because it is written in the plan.
- **If the topic or session is not covered**, say so plainly and offer the nearest thing
  the corpus actually covers. Do not invent a topic, and do not fall back on general
  knowledge of the domain.

Resolve `{Subject}` from the Token cell of the Assistant table in `CLAUDE.md` when you
need the literal index or plan filename.

## How it runs

- **One question at a time.** Wait for the answer before revealing anything.
- **Multiple-choice by default** — four options, parallel in length and grammatical form,
  with the correct position varying. Switch to open-ended if the user prefers it or the
  material suits it better.
- **After each answer:** say whether it is right, give the one-line grounded explanation,
  then move on. Brief and encouraging, without inflated praise. A wrong answer gets the
  correction, not a lecture.
- **Adapt.** Getting them right — go deeper or broader. Missing them — slow down, revisit
  the underlying point, or come at it from an easier angle. React to the answers rather
  than running a fixed script.
- **No fixed length.** Keep going until the user stops. After a natural batch, it is fine
  to ask whether they want more.

## Handing off

If the user wants to capture what came out of the quiz — what they understood, what was
shaky — mention `/sessionNotes`, which can fold this conversation's reflections into
written notes. Mention it; do not run it.

## Does not

- Write any file. No HTML, no question bank, no score file, no notes. If the user wants a
  running tally, keep it in the conversation.
- Compile the questionnaire artifact or audit answer positions across a bank — that is
  `questionnaire`.
- Author questions into the learning plan — that is `learningPlanner`.
- Invent topics the corpus does not cover.
- Persist anything between sessions.

## Grounding discipline

- Stems, correct answers, and explanations trace to source. If the source does not cover
  something, do not ask about it — say what is covered instead.
- Distractors are free: plausible, parallel, not source-bound.
- Never let the correct option be identifiable purely by being the only grounded-sounding
  one. Keep the options parallel so the answer is not given away.
