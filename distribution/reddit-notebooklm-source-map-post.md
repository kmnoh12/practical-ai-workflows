# Reddit text-first post — r/notebooklm / source map angle

Status: draft. Do not post without checking subreddit rules.

## Title options

1. Stop asking NotebookLM to summarize first — ask for a source map
2. My first NotebookLM prompt for studying PDFs is no longer “summarize this”
3. Source map first, summary second: a safer NotebookLM study workflow

## Body

I’ve been testing a small PDF study workflow and the biggest failure mode was not “the AI wrote something obviously fake.”

The bigger problem was quieter: a clean summary can drift away from the PDF structure, and then I can’t tell which notes are source facts vs. study explanations.

So my first NotebookLM prompt is now this:

```text
Use only the uploaded source.
Create a source map with:
1. the main sections of the PDF,
2. the key concept in each section,
3. 1–2 claims worth checking later,
4. source cues or citations for each item,
5. one retrieval question per section.
If the source does not support something, write: Not in source.
```

Then I label each note as one of four things:

| Label | Meaning |
|---|---|
| source fact | directly supported by the PDF |
| study explanation | simplified from source facts |
| generated example | useful but not a source fact |
| check source | not clearly supported yet |

This made the workflow much less slippery for me. I use NotebookLM for the source map and verified notes, then ChatGPT only after that for quiz questions and review plans.

Curious: do you ask NotebookLM for summaries first, or do you start with source/citation mapping?

Optional link if allowed / in comment only:
https://practical-ai-workflows.pages.dev/how-to-use-notebooklm-to-study-a-pdf-without-losing-the-source-trail/
