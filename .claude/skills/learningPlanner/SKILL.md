---
name: learningPlanner
description: Build the learning plan from the knowledge index — propose the session list, then each session's knowledge items, skills, questions, deliverable and quiz questions one session at a time, writing learning/learningPlan.{Subject}.md only as each session is approved. Use when the creator asks to build, draft, or revise the learning plan. Not for writing session study material (sessionWrite) and not for compiling artifacts.
---

# Learning planner

Runtime skill. It turns the knowledge index into the learning plan, one approved session
at a time. The plan file it writes is the source of truth for every learning artifact
downstream, so nothing reaches it that the creator has not approved.

The grounding discipline in `CLAUDE.md` applies throughout. Session titles, knowledge
items, and question content come from the corpus. Ordering, skill items, the deliverable,
and the self-confidence question are inferred, modest, and tethered to that session's
grounded content.

## When to use

- "Build the learning plan", "draft the plan", "revise session 03."
- Do NOT trigger for indexing source files (`analyzeCorpus`), for writing expanded
  session material (`sessionWrite`), or for compiling any HTML.

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

## Step 0 — Confirm the index exists

Read the Token cell of the Assistant table in `CLAUDE.md` to resolve `{Subject}`, then
check for `src/index.{Subject}.md`.

If the index is missing, say so in one line, tell the creator to run `/analyzeCorpus`
first, and stop. There is no plan to build without it.

If the creator asked to revise an existing session, go to the Revising an approved
session section instead of Step 1.

## Step 0b — Settle the learning language

Learning material is shared with everyone, so its language is an assistant-wide setting:
`dev/config.json → learning_language`.

- **If it is set,** write in it.
- **If it is empty,** look at the language of the sources. If they consistently use one
  language — usually English — propose it. If they are mixed, say so and ask. Either way,
  confirm with the creator before writing anything, then record the answer in
  `dev/config.json`.

The conversation with the creator stays in their language; only the plan's text is
written in the learning language. Every later learning skill reads the same setting.

## Step 1 — Confirm the session list

Read `src/index.{Subject}.md`. Propose the shape of the plan before any detail:

- the number of sessions
- each session's number and title, in `01`, `02`, `03` order
- one line on why they are ordered that way

Sessions come from the corpus's own divisions and topic groupings — one subject per
session. Propose as many as the corpus supports: never pad the count, never compress two
unrelated subjects into one session to hit a number.

Ordering is inferred. If teaching a later session depends on terms a prior one defines,
say so. If the material gives no basis for an order, say that and present the order as a
suggestion only.

Flag any proposed session that already looks thin from the index — one narrow topic
drawn from little material — and suggest which neighbour it could merge into. Restructuring
the list here is cheaper than at any later point.

Wait for the creator to confirm or restructure the list. Write nothing in this step.

## Step 2 — Propose one session in full

Take the next unwritten session from the confirmed list. Read the `src/` files the index
points to for that session's topics — this is the only reason to open source files, and
only for the session under discussion. For a large file, use its topic map in
`src/sections/` and read only the sections that cover those topics — never the whole
file.

Present the complete session block for approval, in the plan's format:

- **Knowledge items** — the concepts the source actually states for this session. As many
  as the source supports.
- **Skill items** *(inferred)* — capabilities the session's material genuinely supports.
- **Important questions** — the questions a learner should be able to answer after this
  session. These are learning prompts, not quiz items.
- **Deliverable** *(inferred)* — a small task doable with what this session teaches.
- **Self-confidence question** *(inferred)* — in the style "Can I explain {topic} to
  {a stakeholder} without notes?", answerable from this session's grounded content.
- **Quiz questions** — multiple-choice items, roughly 2 per top-level knowledge item. Ten
  is a hard maximum. Four is a target, never a reason to pad — see When a session cannot
  reach four questions. Stems, correct answers, and explanations must trace to the
  source files you read. Distractors are the one exception: freely authored, plausible,
  and parallel in length and grammatical form so the correct option is not the giveaway.
  Vary the correct index across 0–3 within the session; no clustering.

If a knowledge item cannot sustain two distinct grounded questions, reconsider whether it
belongs as a top-level knowledge item at all.

If something is genuinely ambiguous — is this one session or two, is this a prerequisite
or parallel — ask one clarifying question before proposing.

### When a session cannot reach four questions

Fewer than four grounded questions usually means the session is a fragment. **Merging is
the default.** Say how many grounded questions the material supports, propose merging, and
name the session it should merge into.

The creator may keep the session separate instead, but only for a stated reason:

- **procedural content** — the session is rich in steps and judgement but holds few facts
  with one right answer, so its deliverable is the real test, not the quiz
- **merging would mix subjects** — the only neighbour covers something unrelated, and one
  subject per session matters more than length
- **ordering** — later sessions depend on this one standing alone

Without one of these, merge. Either way, never pad to reach four.

How the merge works, given that sessions are written in order and only appended:

- **Into the next session** (not yet written): combine the two, re-propose the merged
  session in full, and renumber the remaining unwritten sessions. Confirm the updated
  session list.
- **Into the previous session** (already written): absorb this content through the
  revision flow below, drop this session from the list, and renumber the remaining
  unwritten sessions.

Renumbering only ever touches sessions not yet written, so nothing already in the file
changes number.

## Step 3 — Wait for approval

Wait for the creator to approve or adjust. Incorporate adjustments and re-present if the
change is substantial.

**Write nothing until the session is approved.** Reviewing a proposal in chat is far
cheaper than rewriting a file.

## Step 4 — Append the approved session

Append the approved session block to `learning/learningPlan.{Subject}.md`, following the
format in that file exactly:

````markdown
## Session {NN} — {Title}

### Knowledge items
- {item}

### Skill items (tier: inferred)
- {item}

### Important questions
- {question}

### Deliverable (tier: inferred)
{deliverable description}

### Self-confidence question (tier: inferred)
{question}

### Quiz questions
```yaml
- q: {stem}
  o: [{option 0}, {option 1}, {option 2}, {option 3}]
  a: 0
  e: {explanation}
```

---
````

- Session numbers are `01`, `02`, `03` — always two digits.
- `a` is the zero-based index of the correct option in `o`.
- Keep the `(tier: inferred)` markers. `studyGuideCreator` strips them from the
  learner-facing HTML; they must exist here.
- Sessions are separated by a horizontal rule.
- Append only. Never rewrite or reorder a session already in the file.

Then return to Step 2 for the next session.

## Step 5 — Propose the next skill

When every session on the confirmed list is written, report the plan path and the session
count, then propose `/sessionWrite` to write the expanded study material.

Propose it. Do not run it.

## Revising an approved session

When the creator asks to change a session already in the plan file:

1. Show the current block for that session as it stands in the file.
2. Take the creator's adjustment.
3. Re-propose the complete revised block — not just the changed lines — re-reading the
   relevant `src/` files if the change touches knowledge items or quiz questions.
4. On approval, replace that session's block in place. Leave every other session
   byte-identical, and keep the session number unchanged so downstream study guides,
   podcast prompts, and quiz units still line up.

The same rule holds: nothing is written until the creator approves the revised block.

## Does not

- Write, or partially write, any session before the creator approves it.
- Read source files to build the session list or the plan's structure — that comes from
  the index. Source files are opened only to author the session under discussion.
- Rewrite, reorder, or renumber sessions already approved and written, except in the
  revision flow above, and then only the one named session.
- Write expanded session material or compile any HTML. That is `sessionWrite`,
  `studyGuideCreator`, and `questionnaire`.
- Invoke `sessionWrite` or any other skill. It proposes; the creator runs.
- Pad knowledge items, skill items, or quiz questions to reach a number.
- Keep a session under four questions without first proposing a merge.

## Quality gate (silent, before each append)

- Every knowledge item, quiz stem, correct answer, and explanation traces to a source
  file read in Step 2.
- Quiz questions number at most 10. Fewer than 4 only when the creator kept the session
  separate for one of the stated reasons after a merge was proposed — never padded up.
- The correct index varies across 0–3 with no clustering; the four options are parallel
  in form and the correct one is not the longest or most specific.
- The three inferred sections carry their `(tier: inferred)` markers.
- The session number is two digits and continues the existing sequence.
- The YAML block parses: `q`, `o`, `a`, `e` on every item, `o` holding exactly four
  options, `a` within 0–3.
- No other session in the file was touched.
