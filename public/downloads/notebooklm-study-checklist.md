# NotebookLM Study Checklist: Source Map First

Use this before trusting AI-generated study notes from a PDF.

## 1. Source setup

- [ ] The PDF/source text is uploaded or pasted.
- [ ] The task says: `Use only the provided source.`
- [ ] The prompt asks for source cues, citations, or section references.
- [ ] The prompt says what to do when the source does not support a claim.
- [ ] You know the exam/task deadline and the page range you care about.

## 2. First-pass source map

| Section / page range | Key idea | Source cue | Check later? | Study action |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

Prompt:

```text
Use only the uploaded source.
Create a source map with:
1. main sections,
2. the key concept in each section,
3. claims worth checking later,
4. source cues for each item,
5. one retrieval question per section.
If the source does not support something, write: Not in source.
```

## 3. Definitions and confusing pairs

| Term | Source-grounded meaning | Source cue | Possible confusion | Safer wording |
|---|---|---|---|---|
| | | | | |
| | | | | |

Prompt:

```text
Based only on the source, list concepts students are likely to confuse.
For each pair, include:
- the difference in one sentence,
- a quote or source cue,
- one exam-style trap,
- what not to say.
Only include pairs supported by the source.
```

## 4. Verification pass

- [ ] Definitions checked against the PDF.
- [ ] Numbers, dates, formulas, and named steps checked.
- [ ] Examples labeled as `source example` or `generated example`.
- [ ] Unsupported claims removed or marked `check source`.
- [ ] Final notes separate source facts from study explanations.
- [ ] Quiz answer key checked before use.

## 5. Move to practice

After the source trail is clean, ask ChatGPT for retrieval practice:

```text
Use only the verified notes below.
Create:
1. 10 short-answer questions,
2. 5 confusing-pair questions,
3. 5 application questions,
4. an answer key at the end,
5. a list of what each question tests.
Mark unsupported answers as: Check source.
```
