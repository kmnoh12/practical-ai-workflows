# PDF Study Workflow Template: NotebookLM + ChatGPT

Use this template to turn a PDF, lecture handout, textbook chapter, research article, or policy document into source-grounded study notes, quiz questions, an answer key, and a short review plan.

This is a workflow template, not a promise that either tool is always right. Keep the original source open and verify claims before relying on the output.

## Who this is for

Use this if you are:

- A student turning PDFs or lecture notes into study material.
- A self-learner working through dense reports, manuals, papers, or books.
- A tutor, coach, or parent making review questions from assigned material.
- A professional who needs to learn a document without losing track of what the source actually says.

This is most useful when the source is long enough to need structure but important enough that generic AI summaries are risky.

## When to use NotebookLM

Use NotebookLM when source grounding matters most.

Good uses:

- Creating notes from one or more uploaded sources.
- Asking questions that should stay tied to the uploaded material.
- Finding where a statement came from in the source.
- Building a first-pass study guide with source-aware context.

Use NotebookLM first when you need the answer to stay close to the PDF.

## When to use ChatGPT

Use ChatGPT when you need flexible teaching, practice, and planning.

Good uses:

- Explaining confusing ideas in simpler language.
- Turning notes into quiz questions.
- Creating an answer key and checking it against quoted source lines.
- Building a 7-day review plan from weak topics.
- Rewriting explanations for a specific level, such as beginner, exam prep, or professional refresher.

Use ChatGPT after you have source-grounded notes, and keep the PDF or NotebookLM citations nearby for checking.

## Step 1: Prepare the PDF/source

Before using AI, prepare the source so the workflow has clean input.

1. Pick one PDF, chapter, article, handout, or set of class notes.
2. Give the file a clear name, such as `biology-chapter-4-cell-transport.pdf`.
3. Check that text can be selected or copied. If it is scanned, OCR it first.
4. Note the page range you need to study.
5. Write the study goal in one sentence.

Study goal:

```text
I need to understand [topic] well enough to [exam/task/presentation/use case] by [date].
```

Source details:

```text
Source title:
Author/class/source owner:
Page range:
Deadline:
Exam or task type:
Topics I already understand:
Topics I find confusing:
```

## Step 2: Generate source-grounded notes in NotebookLM

Upload the PDF or source material to NotebookLM. Ask for notes that stay inside the source and separate direct source content from interpretation.

Copy the notes into your study document. Keep any citation/source references visible if NotebookLM provides them.

After the first output, skim the notes and mark:

- Claims that seem important.
- Claims that seem surprising.
- Claims that you would not want to get wrong.
- Concepts you cannot explain in your own words yet.

## Step 3: Use ChatGPT for explanations, quiz questions, answer key, and review plan

Move only the needed material into ChatGPT. Use the NotebookLM notes plus selected source excerpts, not a vague request like "teach me this PDF."

Ask ChatGPT to:

- Explain confusing concepts.
- Generate quiz questions.
- Make an answer key.
- Flag which answers need source checking.
- Build a review plan based on weak spots.

Keep source excerpts in the prompt when accuracy matters.

## Step 4: Verify risky claims back against source

Do not verify everything with equal effort. Verify the claims where mistakes would hurt.

Check these back against the PDF or NotebookLM source references:

- Definitions.
- Formulas.
- Dates, numbers, thresholds, and named rules.
- Cause-and-effect claims.
- "Always," "never," "best," "most important," or "main reason" claims.
- Quiz answer keys.
- Anything that sounds useful but was not clearly present in the source.

If a claim is not supported, rewrite it or delete it.

## Copy/paste prompts

Replace bracketed text before using each prompt.

### 1. Source-grounded study notes prompt

```text
Use only the uploaded source or pasted source excerpt. Do not add outside facts.

Create source-grounded study notes for:
[topic, page range, or chapter]

My study goal:
[exam/task/use case]

Format the notes as:
1. Core ideas I must understand
2. Key terms and definitions
3. Important relationships or processes
4. Examples from the source
5. Things students are likely to confuse
6. Claims I should verify before relying on them

If the source does not support a point, write: Not in source.
```

### 2. Explain confusing concepts prompt

```text
Use the notes and source excerpts below. Stay faithful to the source.

I am confused about:
[concept 1]
[concept 2]
[concept 3]

For each concept:
1. Explain it in plain language.
2. Give one short example only if the source supports it.
3. Contrast it with a nearby concept I might confuse it with.
4. List the exact source line, quote, page, or section I should check.
5. Mark anything that is an interpretation rather than a direct source claim.

Source-grounded notes or excerpts:
[paste notes/excerpts]
```

### 3. Quiz generator prompt

```text
Use only the source-grounded notes and excerpts below.

Create a study quiz for:
[topic]

Include:
- 5 recall questions
- 5 application questions
- 3 "explain the difference" questions
- 2 likely exam-style questions

Do not show the answer key until the end.
For every answer, include the source section, page, quote, or note that supports it.
If an answer is not supported by the source, write: Not in source.

Source-grounded notes or excerpts:
[paste notes/excerpts]
```

### 4. Answer key verification prompt

```text
Check this answer key against the source-grounded notes and excerpts below.

For each answer, return a table with:
- Question number
- Proposed answer
- Supported / Partly supported / Not supported
- Source evidence
- Safer corrected answer

Be strict. If the source does not directly support the answer, mark it Partly supported or Not supported.

Quiz and answer key:
[paste quiz and answer key]

Source-grounded notes or excerpts:
[paste notes/excerpts]
```

### 5. 7-day review plan prompt

```text
Build a 7-day review plan from the source-grounded notes, quiz results, and weak areas below.

Constraints:
- I can study [minutes] minutes per day.
- My deadline is [date].
- Prioritize weak concepts and high-risk mistakes.
- Include retrieval practice every day.
- Include spaced review of older material.
- Include one final source-check pass before the deadline.

Output:
1. Daily plan
2. What to review
3. What to quiz myself on
4. What to verify against the source
5. What counts as "done" for each day

Source-grounded notes:
[paste notes]

Quiz results and weak areas:
[paste results]
```

## Verification checklist

Before you treat the study guide as reliable, check:

- The AI used the correct PDF, chapter, or source excerpt.
- The study guide covers the main source sections, not only the beginning.
- Key definitions match the source wording.
- Quiz answers are supported by the source.
- Any numbers, dates, formulas, or named frameworks were checked.
- Unsupported claims were removed or labeled.
- Confusing concepts were rewritten in your own words.
- The review plan includes retrieval practice, not only rereading.
- The final notes include page numbers, citations, quotes, or source sections where possible.

## Common failure cases

Watch for these problems:

- The AI gives a generic explanation that is true in the real world but not in your source.
- The output sounds confident but skips page references or evidence.
- Quiz questions test trivia instead of the important ideas.
- The answer key includes answers that are broader than the source.
- The model invents examples because you asked for examples without requiring source support.
- The study plan becomes a to-do list with no retrieval practice.
- You paste too much material into ChatGPT without saying what to focus on.
- You trust a summary without checking the PDF for high-risk claims.

## Optional next step

If people actually use this workflow, turn it into a small tool:

- Upload or paste a source.
- Generate source-grounded notes.
- Convert weak concepts into quiz questions.
- Require source evidence for every answer.
- Produce a 7-day review plan.
- Export the result as Markdown, Google Docs, or PDF.

Only build the tool after real users copy the template, ask for it, or repeat the workflow enough times to show demand.
