---
name: studyGuideCreator
description: Compile the study guide HTML from the session material in learning/study guides/ — one pane per session — into learning/studyGuide.{Subject}.html, archiving the previous version first. Use when the creator asks to compile, rebuild, or refresh the study guide. Not for writing session content (sessionWrite) and not for the quiz HTML (questionnaire).
---

# Study guide creator

Runtime skill. It runs after the session materials are written. It is a compiler: it
reads the session markdown files, converts each to an HTML fragment, and writes them into
the data block of `learning/studyGuide.{Subject}.html`.

It creates no content. If a session's material is thin or missing, the compiled guide
shows exactly that gap — fix it in `sessionWrite`, not here.

## When to use

- "Compile the study guide", "rebuild the study guide", "refresh the HTML."
- Do NOT trigger for writing or rewriting session material (`sessionWrite`), for the
  questionnaire HTML (`questionnaire`), or for in-chat quizzing (`chatQuiz`).

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

Check `learning/study guides/` for `.md` files. If there are none, say so in one line,
tell the creator to run `/sessionWrite` first, and stop.

Open `learning/studyGuide.{Subject}.html` and confirm it contains both marker comments —
`FILL PER COMPILE` and `ENGINE — verbatim`. If either is missing the file has been
damaged; say so and stop rather than writing a broken artifact. A clean copy lives in
`.assistantTemplate/learning/studyGuide.{Subject}.html` in the creator repo.

## Step 1 — Read the session files in order

Read every `.md` file in `learning/study guides/`, ordered by the `{NN}` prefix in the
filename. Each file is one session.

For each, take the session number from the filename (`{NN} - {Session Title}.md`) and the
title from the file's `# Session {NN} — {Title}` heading. The heading keeps characters a
filename cannot hold, so it is the display title. If the number in the heading disagrees
with the filename, trust the filename — that is what orders the panes — and flag the
mismatch in the report.

If two files share the same `{NN}`, stop and report both names. Compiling would show that
session twice; clearing the stale one into the archive is `sessionWrite`'s job.

Do not read `learning/learningPlan.{Subject}.md`, `src/`, or `.archive/`. The session
files are the whole input.

## Step 2 — Convert each session to an HTML fragment

Convert the markdown body to clean HTML:

| Markdown | HTML |
|---|---|
| `## Heading` | `<h2>Heading</h2>` |
| `### Heading` | `<h3>Heading</h3>` |
| paragraph | `<p>…</p>` |
| `- item` / `1. item` | `<ul><li>…</li></ul>` / `<ol><li>…</li></ol>` |
| `**bold**`, `*italic*`, `` `code` `` | `<strong>`, `<em>`, `<code>` |
| fenced code block | `<pre><code>…</code></pre>` |
| `> quote` | `<blockquote><p>…</p></blockquote>` |
| pipe table | `<table><thead>…<tbody>…</table>` |
| `---` | `<hr>` |
| `[text](url)` | `<a href="url">text</a>` |

Rules that matter:

- **Drop the `# ` title.** The engine renders the session number and title itself. A
  second `<h1>` in the fragment duplicates it.
- **Wrap the two closing sections** so they render as cards:
  `## Practice` → `<section class="practice"><h2>Practice</h2>…</section>`, and
  `## Self-check` → `<section class="selfcheck"><h2>Self-check</h2>…</section>`.
- **Strip every `(tier: inferred)` marker.** Tier markers never reach the learner. This
  holds even if one leaked into a session file.
- **Escape for the template literal:** inside the backtick string, every literal
  backtick becomes `` \` `` and every literal `${` becomes `\${`. Getting this wrong
  breaks the whole file, not just one session.
- Escape `<`, `>` and `&` that appear as literal text in the source rather than as markup.

## Step 3 — Archive the previous version

If `learning/studyGuide.{Subject}.html` already holds compiled sessions, archive it first:

```
.archive/learning/{YYMMDDHHMM}.studyGuide.{Subject}.html
```

Read the timestamp from the system clock (`Get-Date -Format yyMMddHHmm`) at the moment of
the move — never guess it. If that name is already taken, add the seconds
(`yyMMddHHmmss`).

Skip this when the data block is still the empty scaffold; there is nothing to preserve.

## Step 4 — Write the data block

Replace everything between the `FILL PER COMPILE` marker comment and the
`ENGINE — verbatim` marker comment with:

```javascript
const SUBJECT = "{Subject}";
const DOMAIN  = "{DOMAIN}";
const LABELS  = {};
const SESSIONS = [
  { n:"01", title:"First session title", html:`<h2>…</h2><p>…</p>` },
  { n:"02", title:"Second session title", html:`<h2>…</h2><p>…</p>` },
];
```

- `n` is the two-digit session number as a **string** — `"01"`, not `1`.
- `title` carries no number prefix; the engine renders the number separately.
- Entries are in session order.
- `DOMAIN` may be an empty string if the token is blank. Do not substitute a guess.
- `LABELS` is the interface text — "Sessions", "Previous", "Next" and the rest. Read
  `dev/config.json → learning_language`. For English, leave it `{}` and the engine uses
  its built-in labels. For any other language, give every key listed in the template's
  comment, translated, so the whole page reads in one language.

**Never edit anything below the `ENGINE — verbatim` line.** Not the CSS, not the
JavaScript, not the markup. The engine handles navigation, the session pager, keyboard
movement, deep links, visited marks, light and dark, and printing the current session. Changing it is how the
artifact breaks.

## Step 5 — Report

Report the output path and the session count. Flag any filename-versus-heading number
mismatch from Step 1, one line each. Then propose `/podcastPrompter` to generate the NotebookLM
prompts.

Propose it. Do not run it.

## Does not

- Create, expand, or edit session content. That is `sessionWrite`.
- Read the learning plan or the source files. Its input is `learning/study guides/*.md`.
- Generate quiz questions or compile the questionnaire. That is `questionnaire`.
- Run an in-chat quiz. That is `chatQuiz`.
- Render tier markers in the learner-facing HTML.
- Edit anything below the `ENGINE — verbatim` line.
- Invoke another skill. It proposes; the creator runs.

## Quality gate (silent, before Step 5)

- One `SESSIONS` entry per `.md` file in `learning/study guides/`, in `{NN}` order, with
  `n` as a two-digit string and no two entries sharing an `n`.
- Every `title` comes from the file's heading, with its original spelling.
- No fragment contains an `<h1>` or a `(tier: inferred)` marker.
- Every backtick and `${` inside a fragment is escaped.
- `Practice` and `Self-check` are wrapped in their sections.
- The two marker comments are intact and nothing below the engine line changed.
- No `{PLACEHOLDER}` token remains in the data block.
- The previous version was archived, with a clock-read timestamp prefix.
