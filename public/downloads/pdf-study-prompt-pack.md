# PDF Study Prompt Pack

## Source boundary prompt

```text
Use only the PDF or notes I provide in this chat as the source of truth.
Do not add outside facts unless I explicitly ask for them.
If a claim is not supported by the source, write: Check source.
```

## Study guide prompt

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

## Retrieval practice prompt

```text
Using only the verified study guide above, create:
1. 12 short-answer questions,
2. 8 multiple-choice questions,
3. 5 application questions,
4. an answer key at the end,
5. a list of the concepts each question tests.
Do not reveal answers directly under each question.
```

## Missed-question repair prompt

```text
Here are the questions I missed and my wrong answers.
Explain the mistake pattern.
Then create a 30-minute repair plan using only the verified notes.
```

## Three-day review prompt

```text
Create a three-day review plan.
Day 1: recall and definitions.
Day 2: mixed questions and applications.
Day 3: retest missed questions and compress the final sheet.
Include exact tasks, not motivational advice.
```
