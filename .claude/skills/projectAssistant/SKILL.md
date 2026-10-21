---
name: projectAssistant
description: Do the active work on a project item — take in the approved requirement, confirm the deliverable's template and section list, write the draft one approved section at a time, process meeting notes, track decisions (D-prefix) and open questions (O-prefix) with cross-referencing and conflict detection, and write the deliverable from the approved sections. Use when the user shares a requirement or meeting notes, records a decision, raises or closes an open question, or works on a draft or deliverable. Not for creating, classifying, or archiving folders and files — that is projectManager.
---

# Project assistant

Runtime skill. It does the work inside an item: the requirement, the draft, meeting notes,
decisions, open questions, and the deliverable. It never creates, restructures, or
archives project or item folders — that is `projectManager`.

The grounding discipline in `CLAUDE.md` applies, plus the file roles `projectManager`
records in the indexes. **Structure** — templates and writing guides — governs shape,
never substance. Content ranks: **the req is the source of truth for scope and business
rules**; active decisions refine it; the project's **rules** bind how it is done;
**foundations** are the base the work builds on; **examples** are pattern only and never
override anything. Drafts are work in progress — only approved sections are content. One
project's material never informs another's.

**Hands off:** never read, edit, or use anything in the item's `personal/` folder or in
`.archive/`. The assistant's settings block it; do not try. **Everything below the
archive header in a decisions or open questions file is history** — never use it as
active context, a source of truth, or the basis for a recommendation.

## When to use

- "Here's the requirement", "which template should we use?", "let's work on the draft",
  "here are the notes from today's call", "we decided X", "open question: Y", "that
  question is answered", "produce the deliverable."
- Do NOT trigger for creating a project or item, classifying uploads, or archiving a
  project or item (`projectManager`). Do NOT trigger for study-session notes
  (`sessionNotes`).

## Resolving which item

Work out the project and item from the conversation. If ambiguous, ask — briefly, listing
the candidates. Never act across items and never guess.

Before writing anything, read the item's `req.{Item ID}.md`, `decisions.{Item ID}.md`,
`openQuestions.{Item ID}.md`, and `index.{Item ID}.md`, the project's `index.{ABBR}.md`,
and the item's row in `project.{ABBR}.md`. `{ABBR}` is the project's abbreviation, in the
project's token table.

## Languages

- **Talk with the user in their language**, always — including while working a draft
  whose text is in another language.
- **Working records stay as given.** Meeting notes, decision entries, and open question
  entries are written in the language the material arrives in — one item may hold notes
  in several languages. Translate only when the user asks.
- **Drafts and deliverables use the item's delivery language** from
  `project.{ABBR}.md` — the item's own, otherwise the project's. If none is recorded,
  ask before writing and record the answer there, on the item's row or on the project line
  as the user says. If one is recorded, say in one line which language you are writing in,
  so the user can correct it.
- When translating, keep technical terms, codes, and transaction and field names exactly
  as the source writes them.

## Dates and times

- Dates in entries and headers are `YYYY-MM-DD`, with no time.
- **Two kinds of date — never confuse them.**
  - *Today* — when this skill writes something: `Last updated`, and entries the user
    records live in conversation.
  - *Meeting date* — when the meeting actually happened. Notes are often processed days
    later, so it is never assumed to be today.
- **Confirm the meeting date before writing anything from submitted notes.** If the notes
  state a date, show it and ask the user to confirm it. If they do not, ask for it,
  offering today only as a suggestion. Never fill it in silently.
- The confirmed meeting date names the meeting note, and is the opened date of every
  decision and open question recorded from those notes — and the closed date of any entry
  those notes close.
- **Times appear in only two places:** a draft's branch line and an archive file's
  timestamp prefix. Both are read from the system clock at that moment —
  `Get-Date -Format "yyyy-MM-dd HH:mm"` or `Get-Date -Format yyMMddHHmm` — never guessed.
- Each file keeps a `Last updated` date at the top — always today.

## The requirement — req.{Item ID}.md

`req.{Item ID}.md` carries the client's approved requirement, verbatim. It is **read-only
by default** — read it for context, never alter it. It arrives one of three ways:

1. **Pasted in chat.** The user asks you to put it in the req file.
2. **Written into the file by the user.** Read it; there is nothing to write.
3. **Dropped as a document** that the user classified as *Requirement* with
   `projectManager`. Read its text copy — the `{stem}.md` beside it in `uploads/` — and
   propose that text for the req file.

For 1 and 3, **double-confirm before writing a single character**: show exactly what will
be written and where, and get a second, unambiguous confirmation. Copy the client's text
as it is — its wording, labels, order and line breaks — and do not summarise, restructure,
reformat, or translate it. The only line you add is a first heading,
`# {Item ID} — {Item Title}`. Anything less than both
confirmations and you do not write.

After a document's text is in the req file, move the original and its text copy to the
archive, keeping their path and adding a timestamp prefix:
`.archive/projects/{Project}/{Item}/uploads/{YYMMDDHHMM}.{file name}.{ext}`. The req file is
then the only source; neither is read again, and nothing of the requirement stays in
`uploads/`.

**Reading project files.** A PDF, Word, Excel or PowerPoint file — a template, a context
file, a draft someone dropped — is read through its text copy, the `{stem}.md` beside it
that `projectManager` wrote. Never read the original. If a copy is missing, write it with
`python .claude/skills/analyzeCorpus/digest.py text "{file}"` first.

Never write to the req file as a side effect of anything else — not from meeting notes,
not from a decision, not while drafting.

## How a document gets made

**The user's confirmations are the source of truth for a document — never the draft
file.** The draft is a working artefact: text in it that the user did not approve, in
chat, section by section, is not content. Four phases, in order:

| Phase | What happens | Files written |
|---|---|---|
| 1. Shape | the template is confirmed, then its section list | the item index |
| 2. Discussion | the work: gaps, meetings, decisions, open questions | working records only |
| 3. Draft | on the user's word, one section at a time, each approved in chat | the draft, one approved section at a time |
| 4. Deliverable | on the user's word, in one pass, from the approved sections | the deliverable |

### Phase 1 — Shape

Once the requirement and the delivery language are known, settle the shape.

- **Check the project's `.{Folder}/templates/`** through `index.{ABBR}.md`. Templates are
  shared, and each item uses one. If one seems to fit the requirement, name it and say why
  in one line, then **ask the user to confirm it. Never pick a template silently**, even
  when only one exists. If several could fit, list them and ask.
- **Then show its section headers as a list in chat** — read from its text copy, in
  order — and ask the user to confirm the list: keep, drop, rename, or add.
- **If there is no template, or none fits,** propose the sections from the requirement as
  a list, and confirm it the same way.

**Only sections on the confirmed list exist.** Never add one because the template has it,
because a draft file has it, or because the subject usually has one; when in doubt, ask —
never include. Record the outcome in `index.{Item ID}.md`, so later sessions start from
it:

```markdown
- delivery template: ../.{Folder}/templates/{file} | none
- sections confirmed: YYYY-MM-DD
  1. {Section title} — open
  2. {Section title} — open
```

### Phase 2 — Discussion

This is where most of the work happens. Develop the content with the user in
conversation — arguments, points, data, open issues — in the user's language. Work toward
covering every gap the confirmed sections will need: when a section still lacks an input,
say which, so it can be settled here. Meeting notes, decisions, and open questions arise
in this phase — handle them as below. **No draft is written in this phase.**

### Phase 3 — Draft, section by section

Only when the user says to start the draft. The bookkeeping is done by a script, so no
approval is ever lost — run it from the assistant folder:

```
python .claude/skills/projectAssistant/sections.py init "{item folder}"
python .claude/skills/projectAssistant/sections.py approve "{item folder}" {n} "{file}"
python .claude/skills/projectAssistant/sections.py status "{item folder}"
python .claude/skills/projectAssistant/sections.py deliver "{item folder}" "{title}"
```

`init` creates `drafts/00.draft.{Item ID}.md` with the confirmed headings and nothing
else. Then, one section at a time, in the confirmed order:

1. **Render the section in chat** — its full text, in the delivery language, with the
   template's tables and required fields for that section where the template has them,
   and following what the project's writing guides require of it. If it rests on an open
   question, say so first.
2. **Wait** for the user's approval or edits. Rework it in chat until they approve.
3. **On approval, first save it:** write the approved text — exactly as approved, without
   its heading — to a scratch file, and run `approve` for that section. It writes the text
   under its heading and marks it `approved` in the index in one step, and it refuses text
   that carries an internal record. Only once it prints `OK` is the section approved.
4. Then move to the next section. Never render two sections at once, never write a
   section any other way, and never start the next one before `approve` printed `OK`.

A change to an approved section goes the same way: render it, get its approval, run
`approve` again — which rewrites it and re-dates its mark. A section the user has not
approved stays an empty heading. Write the section list in Phase 1 exactly in the format
shown there: the script reads it.

- **Never write to a draft without the user's confirmation.** Propose the change, show it,
  write it when they agree.
- Ground every point in the requirement first — scope and business rules come from it —
  then the decisions, the project's rules, the foundations, and the corpus, per
  `CLAUDE.md`. Each file's `use` line in its index says what to take from it. An example
  supplies pattern only; say so when you draw on one. Where an example — or a foundation —
  does something the req does not ask for, or differently, say so explicitly, the req's
  position first, and keep the draft to the req unless the user decides otherwise.
- Meeting notes, decisions, and open questions can still arise while drafting — handle
  them as below. A decision that changes an approved section sends that section back
  through steps 1–3.

### Internal records never reach the document

Decisions (`D…`), open questions (`O…`), who said what and when, and meeting references
are internal records. **They never appear in a draft section or a deliverable.** Fold the
substance of a decision into plain prose, as part of the design — never cite it, date it,
or attribute it. A reader of the document sees the technical design, not the process that
produced it. The one internal line a draft may carry is its branch line; it never reaches
a deliverable.

### Branching a draft

Drafts are numbered `{NN}.draft.{Item ID}.md` — `00`, `01`, `02` … — and only the current
one lives in `drafts/`. Ordinary changes rewrite the current draft in place.

**A new branch is created only at the user's request.** If you see a large change coming —
a decision that changes the approach, or a restructure of most of the document — *offer*
it: branch to the next number and archive the current draft, or rewrite the current one in
place. If the user declines, rewrite in place and archive nothing.

When the user branches:

1. Create `{NN+1}.draft.{Item ID}.md`. Its first line reads
   `Branched from {NN}.draft.{Item ID}.md on {YYYY-MM-DD HH:MM} — due to D{n}`, or
   `— at the user's request` when no decision caused it.
2. If a decision caused it, add `Led to {NN+1}.draft.{Item ID}.md` to that decision.
3. Move the previous draft to
   `.archive/projects/{Project}/{Item}/drafts/{YYMMDDHHMM}.{NN}.draft.{Item ID}.md`.

## Meeting notes

Write to the item's `meetings/`:

```
[meeting] {Title} {YYYY-MM-DD}-{SUFFIX}.md
```

`{YYYY-MM-DD}` is the confirmed meeting date — see Dates and times. `{SUFFIX}` is `00`, or
the next free number for another meeting on that date. If the title holds a character
Windows forbids in a filename, follow the naming rule in `CLAUDE.md` — propose a
replacement and confirm it; the heading inside the note keeps the original.

Structure the notes from what the user gives you, in the language they came in. Do not
invent attendees, outcomes, or agreements that were not stated. Where the notes imply a
decision or raise a question, say so and offer to record it — do not record it silently.

Run conflict detection (below) when the user submits notes.

## Decisions — decisions.{Item ID}.md

Entries are D-prefixed and sequential: `D1`, `D2`, `D3`, …

**Active decisions** live in the main body. These are the only entries treated as active
context.

```markdown
### D3 — {short title}
(opened: YYYY-MM-DD)
{the decision, stated plainly}
Addresses: O2, O5
```

**Superseded decisions** move to the archive section at the bottom of the file:

```markdown
## ARCHIVE — Superseded Decisions
## Do not use as active context. For historical reference only.
```

Each archived entry carries its closed date and an inline note — `Superseded by D7 on
YYYY-MM-DD.` for a decision that changed, or `Corrected on YYYY-MM-DD.` for wording that
was replaced. A corrected entry's archived copy keeps its number, marked `(replaced)` in
its heading, so it is never mistaken for the active D of the same number.

Never renumber decisions. A superseded D keeps its original number so cross-references
stay valid.

## Open questions — openQuestions.{Item ID}.md

Entries are O-prefixed and sequential: `O1`, `O2`, `O3`, …

**Active questions** live in the main body:

```markdown
### O5 — {the question}
(opened: YYYY-MM-DD)
{context, if any}
```

Two terminal states, both moving the entry to the archive section:

- **CLOSED** — the question was answered. Archive it with the answer and the closing date.
- **OBSOLETE** — the question no longer applies, because the approach it referred to was
  discarded. Archive it with a note explaining why.

```markdown
## ARCHIVE — Closed and Obsolete Questions
## Do not use as active context. For historical reference only.
```

Each archived entry carries its state, its dates, and a brief note:

```markdown
### O5 — {the question}  CLOSED
(opened: YYYY-MM-DD) (closed: YYYY-MM-DD)
Answer: {the answer}
Closed by D3.
```

Never renumber open questions.

## Cross-referencing (many-to-many)

When a decision closes or obsoletes an open question, **update both files in the same
pass**:

- the O entry gains `Closed by D{n}.` or `Made obsolete by D{n}.`
- the D entry gains or extends its `Addresses:` list

One decision can close several open questions. One open question can reference several
decisions. Neither side is complete until both files agree — a dangling reference in
either file is a defect.

## Conflict detection

**When it runs:** on explicit submission — the user submits meeting notes, or records a
new decision. It does not run continuously through the conversation.

**During conversation:** if you notice a possible contradiction without a formal
submission, flag it lightly and move on — *"this may contradict D3; confirm when you
submit the notes."* No resolution is needed in the moment and the conversation is not
interrupted.

**At submission:** when a conflict is detected, **pause**. Ask the question that separates
the first two options — *"Was D3 recorded wrong, or has the decision changed?"* — and
present three options:

1. **Replace — a correction.** The existing entry was recorded wrong. It keeps its number
   with the corrected text; the old wording moves to the archive marked
   `Corrected on YYYY-MM-DD.` Cross-references stay as they are, because the decision
   itself did not change.
2. **Supersede — the decision changed.** Add a new entry with the next number. The old one
   moves to the archive marked `Superseded by D{n} on YYYY-MM-DD.` Then check every open
   question that referenced the old entry, and repoint or update it with the user.
3. **Flag as unresolved** — both entries coexist temporarily, pending clarification.

Write only what the user confirms. Never pick an option on their behalf.

## Deliverables

Phase 4. Only when the user asks for it, and only when every confirmed section is marked
`approved` in `index.{Item ID}.md`. If one is not, name it and offer to work it in
Phase 3.

Write the deliverable **in one pass, from the approved sections only**, in the confirmed
order and as approved — they are not shown again. Run `status` first; then `deliver`,
which assembles the draft's approved sections and nothing else, and refuses while any
section is open or empty or the text carries an internal record. Never write a
deliverable by hand, and never from the conversation. If it refuses, name the reason and
take that section back through Phase 3. Names and dates of who said what are not caught
by the script: read the assembled text for them before running `deliver`. It writes, in
the delivery language, to the item's `deliverables/`:

```
{Item ID} - {Deliverable Title}.md
```

**Deliverables are markdown.** The user moves the content into whatever format the client
requires — Word, PDF, a client tool. Never produce or convert to another format yourself;
if the user asks for one, say that the deliverable is markdown and they carry it over.

Use the Item ID exactly as it appears in the item's folder name. If the deliverable title
holds a character Windows forbids in a filename, follow the naming rule in `CLAUDE.md`.
Then add it to `index.{Item ID}.md`.

### The proactive offer

Two moments earn one offer each, in the same reply that reaches them:

- **Ready to draft** — the item has had at least one open question, every one of them has
  reached CLOSED or OBSOLETE, the section list is confirmed, and no draft exists: offer to
  start the draft. If the section list is not confirmed yet, offer to settle the shape
  first. An item that has never had an open question does not qualify — a new item's
  empty file is not a finished one.
- **Ready to deliver** — every confirmed section is marked `approved`: offer to write the
  deliverable.

Before offering, check `index.{Item ID}.md` for that offer's line — `draft offered:` or
`deliverable offered:`. If it is there, say nothing. After offering, record it with the
date, then **wait for the user's word**, even if the conversation moves on. Do not
re-raise it and do not nudge.

**Never tell the user to run a command to continue work already in hand** — "run
`/projectAssistant` and say the word". Ask the question itself.

## Does not

- Create, rename, restructure, or archive project or item folders, or classify uploads by
  its own rules — those are `projectManager`'s. When the work needs one, follow
  `projectManager` for that step in the same conversation; never send the user to run it. Archiving a single file — a req original, a superseded
  draft — and archiving an *entry* inside the decisions or open questions file are this
  skill's job.
- Read, edit, or use anything in `personal/` or `.archive/`.
- Write to `req.{Item ID}.md` on anything less than double-confirmation, or alter the
  client's text when transcribing it.
- Pick a template silently, or start a draft before its template and section list are
  confirmed — or before the user asks for it.
- Include a section that is not on the confirmed list, or treat text in a draft file as
  content the user approved.
- Render or write more than one section at a time, or write a section before its approval.
- Put a decision or open question number, an attribution, or a meeting reference in a
  draft section or a deliverable.
- Write to a draft without the user's confirmation, or branch a draft unasked.
- Translate working records unasked.
- Renumber D or O entries, or reuse a retired number.
- Resolve a conflict without the user choosing one of the three options.
- Use anything below an archive header as active context.
- Produce a deliverable before every confirmed section is approved, or from anything but
  the approved sections; or repeat a proactive offer.
- Guess a time.

## Quality gate (silent, before delivering)

- The right project and item were resolved without guessing.
- The conversation was in the user's language; drafts and deliverables are in the
  recorded delivery language; working records kept the language they arrived in.
- `req.{Item ID}.md` is unchanged, unless the user double-confirmed a transcription of the
  client's text, unaltered — and any original document was then archived.
- The template and its section list were confirmed by the user and recorded in the item
  index before the first draft was written, and the draft was started on the user's word.
- Every section in the draft was rendered alone in chat, approved, and written by
  `sections.py approve`, which printed `OK`; `status` shows text and an `approved` mark for
  each.
- The deliverable was written by `sections.py deliver`.
- No draft section or deliverable holds a D or O number, an attribution, or a meeting
  reference.
- Every write to a draft was confirmed; any branch was requested or accepted, carries its
  branch line, and its predecessor is archived.
- Every new D and O entry has a sequential number and an opened date; every archived
  entry has a closed date, its state, and a note.
- Every cross-reference resolves in both directions — no dangling `Closed by`,
  `Addresses:`, or `Led to`.
- No entry was renumbered; no archived entry was used as active context.
- Any conflict was surfaced at submission with all three options, and only the user's
  choice was written.
- Every date taken from submitted notes was confirmed by the user; every time was read
  from the system clock.
- A deliverable was written in one pass from the approved sections only, in the confirmed
  order, and is indexed.
- Each proactive offer — draft, deliverable — was made at most once, when its moment came,
  and is recorded in the item index; the user was never sent to run a command to go on.
- No file name holds a forbidden character; any replacement was confirmed.
- Nothing in `personal/` or `.archive/` was read.
