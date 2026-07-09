# Reddit text-first post — r/GetStudying / active recall angle

Status: draft. Do not post without checking subreddit rules.

## Title options

1. A ChatGPT PDF prompt that makes quiz questions instead of prettier summaries
2. Most AI study prompts make summaries. This one forces active recall.
3. My PDF study prompt stack: source boundary → quiz → missed-question repair

## Body

A lot of “study this PDF with ChatGPT” prompts produce nicer summaries, but summaries are not studying.

The prompt stack I’m using now tries to force active recall:

1. source boundary,
2. study guide,
3. retrieval questions,
4. answer-key verification,
5. missed-question repair.

The first prompt is:

```text
You are helping me study from provided source material, not from memory.
Use only the PDF text, excerpts, or verified notes I provide.
If a claim is not supported by the source, write: Check source.
Separate source facts, study explanations, generated examples, and questions.
Do not create citations or page references unless they are present in the source material.
```

Then after the notes are verified, I ask:

```text
Using only the verified study guide above, create:
1. 12 short-answer questions,
2. 8 multiple-choice questions,
3. 5 application questions,
4. 5 confusing-pair questions,
5. an answer key at the end,
6. a list of the concepts each question tests.
Do not reveal answers directly under each question.
```

The part that changed my workflow is the missed-question repair prompt:

```text
Here are the questions I missed and my wrong answers.
Explain the mistake pattern.
Then create a 30-minute repair plan using only the verified notes.
Include exactly what to reread, what to recall, and what to retest.
```

This keeps ChatGPT as a practice generator, not the source of truth.

Question: for people using AI to study, do you get better results from summaries or from quiz/repair loops?

Optional link if allowed / in comment only:
https://practical-ai-workflows.pages.dev/the-chatgpt-prompt-i-use-to-turn-pdfs-into-study-guides/
