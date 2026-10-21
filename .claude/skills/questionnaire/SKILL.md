---
name: questionnaire
description: Compile the multiple-choice questionnaire HTML from the quiz questions in learning/learningPlan.{Subject}.md, re-verifying every stem, correct answer and explanation against src/ before writing learning/questionnaire.{Subject}.html. Use when the creator asks to compile, rebuild or refresh the questionnaire or quiz HTML. Not for in-chat quizzing (chatQuiz) and not for the study guide (studyGuideCreator).
---

# Questionnaire

Runtime skill. It compiles the self-contained quiz artifact from the plan's quiz
questions, verifying them against the source material on the way. Each session becomes
one quiz unit.

This is the end of the artifact chain. It proposes nothing afterwards.

The grounding discipline in `CLAUDE.md` applies. The plan is trusted for structure; the
source files are the truth for content. The plan may have been hand-edited since
`learningPlanner` wrote it, so verify rather than assume.

## When to use

- "Compile the questionnaire", "rebuild the quiz HTML", "refresh the questionnaire."
- Do NOT trigger for in-chat quizzing (`chatQuiz`), for the study guide
  (`studyGuideCreator`), or for authoring new questions (`learningPlanner`).

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

Read the Token cell of the Assistant table in `CLAUDE.md` to resolve `{Subject}`, and the
`{DOMAIN}` value from the Domain configuration table.

Read `learning/learningPlan.{Subject}.md`. If it is missing, or no session has a
`### Quiz questions` block, say so in one line, point the creator at `/learningPlanner`,
and stop. The format comment at the top of the plan is not a session, and its example
quiz block does not count.

Open `learning/questionnaire.{Subject}.html` and confirm both marker comments are present
— `FILL PER COMPILE` and `ENGINE — verbatim`. If either is missing the file has been
damaged; say so and stop rather than writing a broken artifact. A clean copy lives in
`.assistantTemplate/learning/questionnaire.{Subject}.html` in the creator repo.

## Step 1 — Read the questions

For each `## Session` block in the plan, take the session number, the title, and the
fenced YAML in `### Quiz questions` — a list of items with `q`, `o`, `a`, `e`.

Ignore `Knowledge items`, `Skill items`, `Important questions`, `Deliverable`, and
`Self-confidence question`. Those belong to `sessionWrite` and `podcastPrompter`.

If a session's YAML does not parse, stop and report which session and what is malformed.
Do not silently drop a session.

## Step 2 — Verify grounding (do not skip)

For every question, confirm against the `src/` files that cover that session's topics —
for a large file, read only the sections its topic map in `src/sections/` points to,
never the whole file:

- the stem states something the source actually supports
- the option at index `a` is genuinely the correct answer
- the explanation `e` is true and traces to the source

Distractors need no grounding — they are the one free element.

Where a question fails verification, fix it against the source, or drop it if the source
cannot support it. **Flag every fix and every drop to the creator in the report.** Never
carry an ungrounded stem, answer, or explanation into the artifact, and never silently
rewrite the plan file. **Keep the plan and the artifact in step:** after the report,
show each fixed question as it stands in the plan and as fixed, and offer to write the
fixes into the plan's `### Quiz questions` blocks. On the creator's approval, change those
questions and nothing else; a dropped question is left for `/learningPlanner`. Other
skills — `chatQuiz` among them — read the plan, so a fix left only in the HTML would
leave them wrong.

## Step 3 — Check the authoring rules

Per session, before compiling:

- **Count:** at most 10 questions, roughly 2 per top-level knowledge item. A session under
  4 is not an error — the creator may have kept it short deliberately in
  `learningPlanner` — but list it in the report. If a drop in Step 2 takes a session
  lower, report that too rather than inventing a replacement.
- **Correct-index variation:** `a` varies across 0–3 within the session; no clustering and
  no value repeated more than twice in a row. Reorder a question's options — moving `a`
  with them — to break clustering.
- **Option parallelism:** all four options are parallel in length and grammatical form,
  and the correct one is not identifiable by being the longest or most specific. Where
  parallelism and distractor content conflict, parallelism governs the form.

## Step 4 — Archive the previous version

If `learning/questionnaire.{Subject}.html` already holds a compiled bank, archive it
first:

```
.archive/learning/{YYMMDDHHMM}.questionnaire.{Subject}.html
```

Read the timestamp from the system clock (`Get-Date -Format yyMMddHHmm`) at the moment of
the move — never guess it. If that name is already taken, add the seconds
(`yyMMddHHmmss`).

Skip this when the data block is still the empty scaffold.

## Step 5 — Write the data block

Replace everything between the `FILL PER COMPILE` marker and the `ENGINE — verbatim`
marker with the filled structures:

```javascript
const SUBJECT       = "{Subject}";
const DOMAIN        = "{DOMAIN}";
const QUIZ_SUBTITLE = "Self-assessment across {N} sessions";
const QUIZ_LEDE     = "Pick an answer to see whether it is right and why.";
const LABELS        = {};

const ACCENTS = ["#2f6f62","#7a5ea7","#b06a2c","#2c6a9e","#a2455f"];

const UNITS       = { s1:"Session 01 · {Title}", s2:"Session 02 · {Title}" };
const UNIT_ACCENT = { s1:ACCENTS[0], s2:ACCENTS[1] };
const FILTER_DEFS = [ { k:"all", label:"All" }, { k:"s1", label:"Session 01" } ];
const BANK        = [
  { u:"s1", q:"Stem?", o:["A","B","C","D"], a:0, e:"Why that option is correct." },
];
```

- `QUIZ_SUBTITLE` and `QUIZ_LEDE` are written in `dev/config.json → learning_language`,
  like the questions themselves — and so are the "All" filter label and the `UNITS`
  labels.
- `LABELS` is the interface text — "Question 2 of 6", "Correct", "Next" and the rest. For
  English, leave it `{}` and the engine uses its built-in labels. For any other learning
  language, give every key listed in the template's comment, translated, keeping the
  `{placeholders}` exactly as they are.
- `UNITS` — one entry per session, keyed `s1`, `s2`, … by session number (not `s01`).
  The label carries the session number and title.
- `UNIT_ACCENT` — one colour per unit, cycling: session *n* uses `ACCENTS[(n-1) % 5]`.
- `FILTER_DEFS` — `{k:"all",label:"All"}` first, then one `{k:"s{n}",label:"Session {NN}"}`
  per session, in order.
- `BANK` — every question from every session, each tagged with its unit id `u`. Preserve
  `q`, `o`, `a`, `e` exactly as verified in Step 2. `o` holds exactly four options and `a`
  is the zero-based index within it.
- `ACCENTS` stays exactly as above — the engine's styling depends on these five values.
- Escape `"` and `\` inside any string. Keep every string on one line.

**Never edit anything below the `ENGINE — verbatim` line.** The engine handles filtering,
one-at-a-time presentation, immediate feedback, scoring, progress, shuffle, the summary,
and retrying missed questions. Changing it is how the artifact breaks.

## Step 6 — Report

Report the output path, the question count, and the per-session counts. Then, one line
each:

- any question fixed during verification, and what was wrong
- any question dropped, and why
- any session below 4 questions
- any option reordering done to break index clustering

**The chain ends here.** Do not propose another skill.

## Does not

- Create or author new questions. That is `learningPlanner`.
- Edit `learning/learningPlan.{Subject}.md` beyond the approved fixes to questions it
  verified — never a question it did not fix, never any other part of the plan.
- Compile the study guide. That is `studyGuideCreator`.
- Run an in-chat quiz. That is `chatQuiz`.
- Invent a replacement for a dropped question to restore a count.
- Edit anything below the `ENGINE — verbatim` line.
- Propose a follow-up skill — the artifact chain terminates here.

## Quality gate (silent, before Step 6)

- Every session with a quiz block appears in `UNITS`, `FILTER_DEFS`, and `UNIT_ACCENT`.
- Every `BANK` item's `u` matches a `UNITS` key; accents cycle correctly by session number.
- Every stem, correct answer, and explanation was verified against `src/` in this run.
- Every `o` has exactly four options; every `a` is an integer 0–3.
- Per session: at most 10 questions, `a` varied across 0–3, options parallel in form; any
  session under 4 is listed in the report.
- No `{PLACEHOLDER}` token remains in the data block.
- The two marker comments are intact and nothing below the engine line changed.
- The file is self-contained — no external request of any kind.
- The previous version was archived, with a clock-read timestamp prefix.
