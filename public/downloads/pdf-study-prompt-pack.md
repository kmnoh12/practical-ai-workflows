# PDF Study Prompt Pack

A source-bound prompt stack for turning PDFs into active recall, not prettier summaries.

## 1. Source boundary prompt

```text
You are helping me study from provided source material, not from memory.
Use only the PDF text, excerpts, or verified notes I provide.
If a claim is not supported by the source, write: Check source.
Separate source facts, study explanations, generated examples, and questions.
Do not create citations or page references unless they are present in the source material.
```

## 2. Source-map prompt

```text
Use only the uploaded source or pasted excerpt.
Create a source map with:
1. main sections,
2. the key concept in each section,
3. claims worth checking later,
4. source cues for each item,
5. one retrieval question per section.
If the source does not support something, write: Not in source.
```

## 3. Study guide prompt

```text
Turn the provided source into a study guide with:
1. a short overview,
2. key terms and definitions,
3. confusing concept pairs,
4. formulas, named steps, or important conditions,
5. likely exam traps,
6. a list of claims I should verify against the PDF.
Keep source facts separate from your explanations.
```

## 4. Retrieval practice prompt

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

## 5. Answer-key verification prompt

```text
Check this answer key against the source-grounded notes below.
For each answer, return:
- Supported / Partly supported / Not supported
- Source evidence
- Safer corrected answer
Be strict. If the source does not directly support the answer, mark it Partly supported or Not supported.
```

## 6. Missed-question repair prompt

```text
Here are the questions I missed and my wrong answers.
Explain the mistake pattern.
Then create a 30-minute repair plan using only the verified notes.
Include exactly what to reread, what to recall, and what to retest.
```

## 7. Three-day review prompt

```text
Create a three-day review plan.
Day 1: recall and definitions.
Day 2: mixed questions and applications.
Day 3: retest missed questions and compress the final sheet.
Include exact tasks, not motivational advice.
End each day with what counts as done.
```
