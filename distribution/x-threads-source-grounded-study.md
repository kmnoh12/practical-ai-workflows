# X / Threads distribution pack - source-grounded PDF study workflow

Status: ready for manual posting after final human pass.
Rule: do not put the link in post 1. Put it in the final reply/post only.

## Thread 1 - Stop summarizing PDFs first

1. Stop asking AI to summarize a PDF first.

That is how you get fluent notes with no source trail.

Start with a source map instead.

2. The first prompt should not be:

"summarize this PDF"

It should be:

"List the source sections, define what each section is responsible for, and mark any claim that needs citation before you explain it."

3. My current workflow:

- NotebookLM first for source trail
- ChatGPT second for retrieval practice
- unsupported claims go into a failure log
- only then do I write study notes

4. The useful output is not a prettier summary.

The useful output is knowing:

- where a claim came from
- which claim is unsupported
- which part you should quiz yourself on
- what you still cannot answer

5. I tested this with one PDF-style handout, one prompt, NotebookLM, and ChatGPT.

The interesting result: NotebookLM was better as the citation-first layer. ChatGPT was better after the notes were source-checked.

6. If you want the exact prompt and evidence files, I put them here:

https://practical-ai-workflows.pages.dev/notebooklm-chatgpt-pdf-study-evidence/

## Thread 2 - NotebookLM first, ChatGPT second

1. The best PDF study workflow I have found is not "NotebookLM or ChatGPT."

It is order of operations:

NotebookLM first.
ChatGPT second.

2. NotebookLM is useful when the question is:

"Which part of the source supports this?"

ChatGPT is useful when the question is:

"Can you turn these verified notes into practice questions?"

3. If you reverse the order, ChatGPT often gives you a confident study guide before you know whether each claim is grounded.

That is the trap.

4. My current rule:

No quiz generation until the source map exists.

No final study guide until unsupported claims are logged.

5. Full comparison:

https://practical-ai-workflows.pages.dev/notebooklm-vs-chatgpt-for-studying-pdfs/
