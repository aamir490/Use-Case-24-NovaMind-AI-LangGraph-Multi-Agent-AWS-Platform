# Module 08 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** RAG Foundations, Embeddings and Vector Search  
> **Purpose:** Prepare for deep RAG interviews from fundamentals through NovaMind's verified PDF-RAG implementation, troubleshooting, security, evaluation, trade-offs and Production V2 design.

---

## Accuracy Rules

You can confidently say:

```text
NovaMind implements genuine PDF RAG.
PDF parsing uses pdf-parse.
Chunk size is about 1000 characters.
Chunk overlap is about 200 characters.
Embeddings use gemini-embedding-001.
Qdrant stores/retrieves vectors.
The question is embedded.
Top 5 chunks are retrieved.
The Groq-backed model generates the answer.
```

Do **not** claim as current features:

```text
OCR
semantic-aware chunking
hybrid search
reranking
mature retrieval thresholds
mature page-level citations
persistent user-document-index mapping
long-term reusable document chat
mature RAG evaluation
guaranteed hallucination prevention
```

Also do not claim a specific vector dimension or Qdrant similarity metric unless you verify it from the exact current configuration.

---

# RAG Foundations

## Q1. What does RAG stand for?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval-Augmented Generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q2. What problem does RAG solve?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It gives a language model relevant external information at inference time so the answer can use data the model may not know from training.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q3. What are the three stages of RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval, augmentation and generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q4. What is retrieval?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Finding source passages that are relevant to the user's question.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q5. What is augmentation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Adding the retrieved passages to the model input as context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q6. What is generation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The language model produces the final answer using the question and retrieved context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q7. Is RAG the same as an LLM?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. RAG is an application architecture around one or more models and retrieval components.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q8. Is RAG the same as a vector database?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. The vector database is only one retrieval component.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q9. Why is RAG useful for private company documents?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Because those documents may not be part of the model's training data, so they can be supplied dynamically at inference time.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q10. Does RAG update the LLM's model weights?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q11. Is RAG training?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. RAG usually operates at inference time.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q12. Is RAG fine-tuning?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q13. Can RAG use data newer than the model's training data?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, if that newer data is available to the retrieval system.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q14. Can RAG answer questions from internal PDFs?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, if the system can extract, index and retrieve the relevant content.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q15. Does RAG guarantee a correct answer?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. Retrieval and generation can still fail.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q16. What is grounding?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Grounding means the answer is supported by supplied source context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q17. Does grounding mean guaranteed truth?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. The source may be wrong, retrieval may be incomplete, or the model may misinterpret the source.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q18. What is the key advantage of RAG over plain prompting?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The model receives external evidence rather than relying only on its learned parameters.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q19. What is the key cost of RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Extra complexity, latency and cost from parsing, indexing, retrieval and larger prompts.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q20. When might RAG be unnecessary?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> When the needed information is already small enough to include directly in the prompt, or when a structured database query is the better retrieval method.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# RAG vs Other Approaches

## Q21. RAG vs fine-tuning: what is the main difference?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> RAG retrieves external information at inference time; fine-tuning changes model parameters.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q22. When is RAG usually better than fine-tuning?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> When factual knowledge changes frequently or lives in private/external documents.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q23. When can fine-tuning be useful?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> For changing behavior, style, format or task specialization rather than simply injecting current factual knowledge.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q24. Does NovaMind fine-tune its RAG model?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q25. RAG vs web search: what is the difference?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> NovaMind PDF RAG retrieves from the uploaded document through embeddings/Qdrant, while web Search retrieves public web results through Tavily.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q26. RAG vs SQL lookup?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> SQL is better for structured rows/columns and exact filters; RAG is useful for unstructured text and semantic retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q27. RAG vs keyword search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Keyword search matches lexical terms; semantic RAG retrieval can match similar meaning.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q28. Can a RAG system use keyword search too?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, in a hybrid design, but that is not verified as current NovaMind behavior.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q29. Is web search automatically RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Not necessarily. For NovaMind, 'web search + LLM synthesis' is the clearer description.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q30. Can a RAG system exist without a vector database?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes. Retrieval can use other methods, but NovaMind uses Qdrant vector search.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q31. Can you build RAG with a relational database?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Potentially, especially if the database supports vector search, but the design depends on the workload.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q32. Is RAG always better than putting the whole document in the prompt?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. For a tiny document, direct-context prompting can be simpler.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q33. Why not fine-tune the model every time a PDF changes?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Fine-tuning is expensive and not designed for frequent factual updates; RAG can update the external knowledge independently.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q34. Why not use Search for private PDFs?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Public web search does not provide controlled access to a user's private document content.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q35. Why not use MongoDB full-text search instead of Qdrant?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> That is a possible alternative, but NovaMind currently uses Qdrant for semantic vector retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Document Parsing and OCR

## Q36. What is the first major RAG ingestion step?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Extract the document text.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q37. What parser does NovaMind use for PDF text?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> `pdf-parse`.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q38. What does `pdf-parse` do?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It extracts machine-readable text from a PDF.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q39. Can `pdf-parse` reliably read scanned image-only PDFs by itself?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No, not without OCR.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q40. What is OCR?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Optical Character Recognition, which converts text in images/scans into machine-readable text.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q41. Is OCR implemented in NovaMind PDF RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q42. Why does extraction quality matter?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Bad extracted text creates bad chunks, embeddings and retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q43. What happens if the PDF contains complex tables?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Text extraction may lose table structure; mature table-aware processing is not verified in NovaMind.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q44. What happens if the PDF is empty?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The workflow should detect insufficient text rather than building meaningless vectors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q45. What is a parser failure?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The file cannot be read or useful text cannot be extracted.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q46. What would Production V2 add for scanned PDFs?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> An OCR stage with document-type validation and quality checks.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q47. Would OCR guarantee perfect extraction?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. OCR can also make recognition errors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q48. Why should parser errors be surfaced separately from retrieval errors?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Because they occur at different pipeline stages and require different fixes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Chunking

## Q49. What is chunking?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Splitting a large document into smaller text units for embedding and retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q50. Why chunk a document?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> To retrieve focused relevant context and avoid embedding/searching only one huge text block.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q51. What is NovaMind's approximate chunk size?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> About 1000 characters.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q52. What is NovaMind's approximate overlap?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> About 200 characters.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q53. Is NovaMind chunking token-based?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The verified implementation is character-based.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q54. Why use overlap?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> To preserve some context when important text crosses a chunk boundary.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q55. What happens if overlap is zero?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A sentence or idea split across boundaries may lose context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q56. What happens if overlap is too large?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> You create duplicated content, more vectors and more storage/embedding cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q57. What happens if chunks are too small?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Meaning can become fragmented and vector count increases.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q58. What happens if chunks are too large?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval can become less precise and more irrelevant tokens reach the LLM.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q59. Is 1000 characters universally optimal?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q60. How should chunk size ideally be selected?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> By testing on representative documents and questions.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q61. What is semantic chunking?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Splitting by topic/meaning or document structure instead of fixed length.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q62. Is semantic chunking implemented in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No, not in the verified current flow.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q63. What is section-aware chunking?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Splitting based on headings, paragraphs or document sections.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q64. Why might section-aware chunking be useful?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It can preserve natural document boundaries and make citations easier.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q65. Could chunking affect hallucination?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Indirectly. Poor chunking can reduce retrieval quality and therefore weaken grounding.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q66. How would you evaluate chunk size?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Compare retrieval relevance and final answer quality across different chunking configurations.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q67. What is chunk explosion?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Creating too many tiny chunks, which increases indexing/storage/retrieval overhead.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q68. Why is chunking part of RAG quality rather than only preprocessing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Because it determines what units can be retrieved and supplied to the model.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Embeddings

## Q69. What is an embedding?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A numeric vector representing semantic meaning.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q70. What is the NovaMind embedding model?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> `gemini-embedding-001`.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q71. What goes into the embedding model?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Document chunks and the user question.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q72. What comes out?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Numeric vectors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q73. Does the embedding model generate the final answer?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q74. Why embed the question?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> So the query can be compared mathematically with document chunk vectors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q75. Why use the same embedding model for chunks and queries?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> They need to be represented in a compatible vector space.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q76. What is an embedding space?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The multidimensional space in which semantically related items tend to be located near each other.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q77. What is a vector dimension?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The number of numeric components in an embedding vector.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q78. What exact Gemini embedding dimension does NovaMind use?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The verified project evidence supplied here does not establish a specific dimension, so I would not claim one.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q79. Why do vector dimensions matter?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The vector database collection/index must be compatible with the embedding model output.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q80. What happens if you change embedding models?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Existing stored vectors may become incompatible and need re-embedding/re-indexing.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q81. Do embeddings contain readable sentences?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. They are numeric representations.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q82. Are embeddings the same as tokens?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q83. Are embeddings a database?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q84. Are embeddings encrypted text?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. They are learned numerical representations and should still be treated as sensitive derived data.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q85. Can embeddings perfectly represent meaning?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. They approximate semantic relationships.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q86. Can embedding quality affect retrieval?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, significantly.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q87. Can embedding latency affect RAG latency?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, especially when a document creates many chunks.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q88. Can embeddings be reused?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, if a persistent index exists and the document/version remains valid.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q89. Does current NovaMind persist reusable document indexes maturely?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q90. What would batch embeddings do?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Send/process multiple chunks efficiently if the provider/API supports it.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q91. Is batching verified in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q92. Why might multilingual documents need evaluation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Embedding quality can differ by language and domain.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q93. Can an embedding model hallucinate?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It does not generate answers, but it can produce representations that retrieve poor matches.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Vector Search

## Q94. What is vector search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Searching for vectors that are mathematically similar to a query vector.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q95. What vector database does NovaMind use?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Qdrant.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q96. What does Qdrant store?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Chunk embeddings and associated vector records for retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q97. What does Qdrant return?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The chunks/vectors that are most similar to the query according to the configured search.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q98. Does Qdrant generate text?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q99. Does Qdrant understand the entire PDF as a human would?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. It performs vector retrieval over stored representations.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q100. What is semantic similarity?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Similarity in meaning rather than exact wording.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q101. What is cosine similarity?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A common vector-comparison measure based on the angle between vectors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q102. Can I say NovaMind definitely uses cosine similarity?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Only if the metric is directly verified from its collection/configuration. The safe verified claim is Qdrant similarity retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q103. What is Euclidean distance?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A straight-line distance measure between vectors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q104. What is dot product?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A vector operation often used as a similarity measure depending on representation/index design.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q105. Why shouldn't I claim a metric without checking?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Because Qdrant collections can be configured with different vector distance metrics.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q106. What is nearest-neighbor search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Finding vectors closest to the query vector.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q107. What is approximate nearest-neighbor search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Using an index to find close vectors efficiently without exhaustively comparing every vector.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q108. Does a close vector guarantee the chunk answers the question?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q109. Can semantically similar chunks still be wrong?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q110. What is a vector index?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A data structure that speeds similarity search.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q111. Do we know the exact Qdrant index tuning used in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Not from the verified facts summarized here.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q112. Why is Qdrant one part of RAG, not the whole system?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> RAG also requires parsing, chunking, embeddings, context construction and generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q113. Could Qdrant be replaced by another vector store?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Technically yes, but behavior, APIs, indexing and operations would change.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Top-K Retrieval

## Q114. What is top-k retrieval?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Returning the k most similar chunks.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q115. What k does NovaMind use?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Top 5.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q116. Why retrieve more than one chunk?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A question may require evidence spread across multiple passages.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q117. Why not retrieve 100 chunks?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It would add irrelevant context, tokens, cost and potentially confuse the model.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q118. Is top 5 universally best?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q119. How would you tune k?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Measure retrieval and answer quality on a representative evaluation set.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q120. Can top-k hurt recall?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> If k is too small, relevant evidence may be omitted.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q121. Can top-k hurt precision?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> If k is too large, more irrelevant chunks may be included.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q122. What is a similarity score?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A numeric value produced by the retrieval metric representing closeness between vectors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q123. Does a high similarity score prove factual correctness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q124. What is retrieval thresholding?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Rejecting chunks whose score does not meet a defined relevance threshold.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q125. Is mature thresholding implemented in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q126. What could happen with no threshold?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The system may always return top chunks even when none are strongly relevant.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q127. Why is threshold calibration necessary?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Score scales depend on the metric/model and dataset.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q128. What is reranking?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Reordering retrieved candidates with a second relevance model/algorithm.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q129. Does NovaMind currently rerank?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q130. What is a typical reranking pattern?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieve a larger candidate set, rerank it, then send the best smaller subset to the LLM.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q131. What is the reranking trade-off?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Potential relevance improvement at the cost of extra latency and cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Keyword, Semantic, Hybrid

## Q132. What is keyword search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Lexical matching based on exact words or terms.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q133. What is semantic search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Embedding-based retrieval based on meaning.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q134. Which does NovaMind's PDF RAG primarily use?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Semantic vector retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q135. When is keyword search especially useful?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Exact IDs, names, codes or quoted terms.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q136. When is semantic search especially useful?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Paraphrases and conceptually similar wording.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q137. What is hybrid search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Combining lexical and semantic retrieval signals.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q138. Is hybrid search currently verified in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q139. Why might hybrid search help?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It can combine exact-term strength with semantic matching.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q140. Why not add hybrid search immediately?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It adds complexity and should be justified by measured retrieval failures.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q141. What is BM25?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A common lexical ranking algorithm; it is general background, not a verified NovaMind component.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q142. What is metadata filtering?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Restricting retrieval by metadata such as owner or document ID.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q143. Is mature metadata-filtered tenant retrieval verified in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q144. Why is metadata filtering important in multi-tenant RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It prevents searching another user's document vectors and narrows retrieval scope.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Augmentation and Context Construction

## Q145. What happens after retrieval?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The retrieved chunks are added to the model input along with the user's question and instructions.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q146. What is context construction?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Building the final model input from instructions, evidence and question.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q147. Why does context order matter?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Models may weight information differently depending on placement and context length.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q148. Can too much context hurt?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q149. What is the lost-in-the-middle problem?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Relevant information can receive less attention when buried in long context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q150. Why can duplicate chunks be harmful?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> They waste tokens and can bias the model toward repeated information.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q151. Should retrieved content be treated as trusted instructions?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. It is untrusted data.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q152. What is a RAG prompt?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The prompt/instruction structure that tells the model how to answer using retrieved context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q153. Should the prompt say when to abstain?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> That can be useful when context does not contain the answer.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q154. Does an abstain instruction guarantee abstention?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q155. Could context include conflicting chunks?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q156. How should conflicting evidence be handled?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Ideally through source-aware prompting, metadata/citations and explicit uncertainty handling.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q157. Does NovaMind have a mature conflict-resolution layer?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Generation and Grounding

## Q158. Who generates the final NovaMind PDF-RAG answer?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The Groq-backed language-model path.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q159. What does the generator receive?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The user question plus retrieved document chunks and instructions.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q160. What is grounded generation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Generating an answer supported by retrieved evidence.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q161. Can the generator ignore correct context?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q162. Can the generator add unsupported details?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q163. What is faithfulness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> How well the answer is supported by supplied context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q164. What is answer relevance?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> How directly the answer addresses the user's question.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q165. Can an answer be relevant but unfaithful?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q166. Can an answer be faithful but incomplete?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q167. What would improve groundedness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Better retrieval, source-aware prompts, constrained output and evaluation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q168. Does RAG eliminate hallucination?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q169. Why might RAG still hallucinate?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Poor retrieval, ambiguous context, model behavior, source errors or missing evidence.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q170. What should happen if no relevant evidence exists?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A well-designed system should indicate insufficient context rather than inventing an answer.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q171. Is a mature no-answer threshold implemented in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# RAG Evaluation

## Q172. Why evaluate retrieval separately from generation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Because a bad answer may come from wrong retrieval or from generation even when retrieval was correct.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q173. What is retrieval precision?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The fraction of retrieved items that are relevant.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q174. What is retrieval recall?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The fraction of all relevant evidence that was retrieved.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q175. What is Precision@K?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Precision measured over the top K retrieved results.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q176. What is Recall@K?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Recall measured over the top K retrieved results.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q177. What is hit rate?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Whether at least one relevant result appears in the retrieved set.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q178. What is MRR?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Mean Reciprocal Rank, which rewards placing the first relevant result near the top.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q179. What is context relevance?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> How useful the retrieved context is for answering the question.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q180. What is answer groundedness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> How well the answer is supported by the context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q181. What is answer relevance?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> How well the answer addresses the user question.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q182. What is factual correctness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Whether the answer is actually correct according to the source/ground truth.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q183. Do groundedness and correctness mean the same thing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. A source can itself be wrong.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q184. What does a RAG evaluation dataset contain?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Documents, questions, expected evidence and answer/quality criteria.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q185. Does NovaMind have a mature automated RAG evaluation suite?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q186. Why is manual testing insufficient?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It is hard to detect regressions consistently across many documents and questions.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q187. What should you benchmark when changing chunk size?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval metrics, answer groundedness, latency and cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q188. What should you benchmark when adding reranking?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Whether relevance gains justify extra latency/cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q189. What should you benchmark when changing embedding models?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval quality, storage/index compatibility, latency and cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q190. What is a regression evaluation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Running the same fixed cases after changes to detect quality degradation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# NovaMind Verified PDF RAG

## Q191. Give the full NovaMind PDF RAG flow.

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> PDF upload → pdf-parse → text → 1000-character chunks with 200 overlap → Gemini `gemini-embedding-001` embeddings → Qdrant collection → question embedding → top-5 similarity retrieval → retrieved chunks plus question → Groq-backed answer.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q192. Is this real RAG or just prompt stuffing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It is real RAG because it performs embeddings-based retrieval before generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q193. What is the parser?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> `pdf-parse`.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q194. What is the embedding model?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> `gemini-embedding-001`.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q195. What is the vector DB?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Qdrant.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q196. What is top-k?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> 5.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q197. What generates the answer?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Groq-backed generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q198. Is the uploaded PDF index persistent for later reuse?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Not as a mature feature.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q199. What kind of Qdrant collection lifecycle is current?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Request-oriented/new collection behavior tied to the upload flow.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q200. Is there a durable document ID to collection mapping?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No mature mapping is verified.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q201. Can a text-only question next week reliably reopen the same vector collection?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Not as a mature supported workflow.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q202. Is scanned PDF OCR supported?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q203. Are page-level citations mature?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q204. Is reranking implemented?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q205. Is hybrid search implemented?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q206. Is a mature relevance threshold implemented?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q207. Is a mature cleanup/lifecycle system for collections implemented?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q208. Is long-term document chat fully implemented?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q209. Is the RAG answer guaranteed to be from the PDF?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The system supplies retrieved PDF context, but model output is not a formal guarantee of faithfulness.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q210. What is the strongest factual claim about the implementation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It genuinely separates document extraction, embeddings, vector retrieval and final generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Document Lifecycle

## Q211. What is a persistent document index?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A vector index that remains associated with a document so it can be queried later.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q212. Why doesn't current NovaMind provide mature persistent follow-up?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> There is no strong durable mapping from user/document identity to reusable collection/index.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q213. What metadata would Production V2 need?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Document ID, owner ID, collection/index ID, status, source, created time, retention and version.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q214. Why store page/chunk metadata?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> For citations, debugging, deletion and source traceability.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q215. Why store document ownership?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> To enforce authorization and tenant isolation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q216. What is document versioning?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Tracking multiple revisions of the same source and deciding which vectors are active.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q217. Why does deletion need to remove vectors too?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Otherwise private document content may remain retrievable after source deletion.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q218. What is index cleanup?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Deleting expired/orphaned collections and vectors.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q219. Why is index cleanup important?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Cost, privacy and operational hygiene.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q220. What happens when the embedding model changes?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Existing documents may need re-embedding into a compatible index.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q221. What is an indexing status?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> For example PENDING, PROCESSING, READY or FAILED.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q222. Why is status useful?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Large documents can be indexed asynchronously and queried only when ready.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q223. Does current NovaMind have mature async ingestion status?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q224. What would async ingestion improve?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> User experience and reliability for large documents.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q225. What is the trade-off of async ingestion?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> More queues/workers/state management and operational complexity.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Security and Privacy

## Q226. What is the main tenant-isolation risk in RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieving vectors/chunks belonging to another user.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q227. How should access be enforced?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Deterministic server-side ownership checks and properly scoped retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q228. Can the LLM decide ownership?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q229. What is prompt injection in RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Malicious instructions embedded in user documents that try to manipulate model behavior.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q230. Should PDF text be treated as trusted?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q231. Can prompt injection make the model reveal server secrets by itself?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A secure application should never provide secrets as model-accessible context/tools in the first place.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q232. What does least privilege mean for RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The workflow can access only the document/vector resources and tools needed for the current user/task.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q233. Are embeddings sensitive?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> They can be derived from private text and should be protected accordingly.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q234. Why avoid logging full retrieved chunks?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> They may contain sensitive document data.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q235. What is data retention?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Rules for how long source files, vectors and metadata remain stored.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q236. Does current NovaMind have mature RAG retention/deletion policy?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q237. What security improvement would persistent indexes require?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Strong document ownership, metadata filters, authorized access and deletion controls.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q238. Can public S3 URLs be used for private RAG docs safely?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Public access would be risky; private access control is preferred.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q239. Does NovaMind's current RAG depend on S3 for uploaded PDFs?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The verified current RAG flow uses temporary local upload processing rather than a mature S3-backed document lifecycle.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q240. How can prompt injection be evaluated?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Use malicious test documents and verify the model cannot cross authorization/tool boundaries.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Performance and Cost

## Q241. Why is PDF RAG slower than normal Chat?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It adds parsing, chunking, embedding, vector operations and then generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q242. Which stage can dominate first-upload latency?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Embedding many chunks can be expensive in time and API usage.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q243. How does persistent indexing improve latency?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It avoids re-parsing and re-embedding the same document for each question.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q244. How does chunk count affect cost?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> More chunks create more embedding work and vector records.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q245. How does top-k affect generation cost?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> More retrieved chunks increase input tokens.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q246. How does long context affect latency?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> More input tokens generally increase model processing time.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q247. Can caching help?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, if designed with ownership and document-version correctness.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q248. What can be cached?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Parsed text, embeddings/indexes or repeated query results depending on requirements.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q249. What is the risk of caching private RAG results incorrectly?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Cross-user or stale-data leakage.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q250. What is batch embedding?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Embedding multiple chunks efficiently in fewer API operations where supported.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q251. Is batch embedding verified in NovaMind?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q252. Can adding more Agent ECS tasks remove embedding-provider quotas?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q253. Can adding more Qdrant capacity fix poor chunking?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q254. Can a faster LLM fix bad retrieval?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q255. What should you measure before optimizing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Stage latency, chunk count, embedding calls, retrieval latency, generation tokens, error rate and cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Troubleshooting

## Q256. RAG answer is wrong. What do you check first?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Verify the request routed to PDF RAG and the correct PDF was processed.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q257. What do you check after routing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Text extraction.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q258. What do you inspect after extraction?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Chunks and boundaries.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q259. What do you inspect next?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Embedding creation and the correct Qdrant collection.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q260. Then what?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieved top-5 chunks.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q261. If retrieved chunks are wrong, which stage is failing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval/indexing/chunking/embedding quality, not primarily generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q262. If retrieved chunks are correct but answer is wrong, what stage is likely failing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Generation/prompting.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q263. If no text was extracted, what is a likely cause?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A scanned/image-only PDF or parser problem.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q264. If Qdrant returns nothing, what can cause it?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Collection/index error, query embedding error, missing vectors or search/configuration failure.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q265. If Qdrant returns irrelevant chunks, what can cause it?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Chunking, embeddings, ambiguous question or retrieval configuration.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q266. If Gemini embedding API fails, can RAG continue normally?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No, not without a verified alternate embedding path.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q267. If Groq fails after retrieval, what happened?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval succeeded but generation failed.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q268. Should you rebuild the entire index when only Groq failed?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. Retry only the appropriate safe stage if possible.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q269. If the PDF question works once but not later, what lifecycle issue might exist?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The current request-oriented collection lacks a durable document-index mapping.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q270. How do you troubleshoot a slow upload?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Measure parsing, number of chunks, embedding duration, Qdrant writes and final generation separately.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q271. How do you troubleshoot high token cost?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Check chunk sizes, top-k, duplicated context, prompt size and conversation context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q272. How do you troubleshoot hallucination?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Inspect whether evidence was retrieved, whether the prompt constrained the answer, and whether the answer is supported by context.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q273. How do you troubleshoot wrong citations in a future citation system?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Trace answer claims back to chunk IDs/page metadata and verify alignment.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q274. What should a correlation ID help with?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Following the same RAG request across Agent, providers and data-store logs.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q275. Does current NovaMind have mature end-to-end RAG tracing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Production V2 Design

## Q276. What is the first lifecycle improvement?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Create durable document metadata with owner and collection mapping.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q277. What is the first retrieval-quality improvement?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Build an evaluation dataset before changing retrieval algorithms.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q278. Would you add reranking immediately?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Only if evaluation shows vector top-k quality is insufficient.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q279. Would you add hybrid search immediately?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Only if lexical misses are a measured problem.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q280. Would you add OCR?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes if scanned PDFs are a required use case.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q281. Would you add page metadata?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes for source traceability and citations.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q282. Would you add thresholds?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Potentially, after calibrating scores on real data.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q283. Would you add citations?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes, but only with reliable source/chunk mapping and answer-source alignment.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q284. Would you make indexing asynchronous?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> For large/reusable documents, likely yes.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q285. What would an async ingestion flow look like?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Upload → document record → queue → worker parse/chunk/embed/index → READY/FAILED.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q286. What would a query flow look like after persistent indexing?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Authorize document → embed query → metadata-scoped vector search → optional rerank → construct context → generate answer.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q287. Why add document status?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> So queries are allowed only after indexing is complete.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q288. Why add retention policy?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> To control privacy, storage cost and cleanup.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q289. Why add vector cleanup?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Deleting a document should also delete its retrievable embeddings.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q290. Why add evaluation before advanced RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Otherwise complexity can increase without proving quality improves.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q291. What metrics would you track?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Retrieval relevance, groundedness, answer relevance, latency, failure rate and cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q292. What security control becomes critical with persistence?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Document ownership/tenant isolation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q293. What is a safe no-answer design?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> If retrieval quality is too low, explicitly say the document does not provide enough evidence.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q294. Would a fallback to plain Chat be safe?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Not silently, because it changes the grounding guarantee.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q295. What should be versioned?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Embedding model, chunking strategy, prompt, document version and index schema.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Design Defense

## Q296. Why use RAG instead of putting the whole PDF in every prompt?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> RAG focuses the model on relevant passages, reduces unnecessary context and is more scalable for larger documents.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q297. Why use embeddings instead of keyword search only?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Embeddings can retrieve semantically similar text even when wording differs.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q298. Why Qdrant?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> NovaMind needs vector similarity retrieval, and Qdrant provides vector storage/search for the PDF chunks.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q299. Why top 5?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It is the current configuration balancing some context breadth against prompt size, but it should ideally be validated through evaluation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q300. Why use overlap?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> To reduce context loss at chunk boundaries.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q301. Why separate embedding and generation models?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> They solve different tasks: vectors for retrieval versus text generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q302. Why not let Groq read the whole PDF directly?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> That would increase prompt size/cost and can be less focused, especially as documents grow.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q303. Why not store the PDF as one vector?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> One vector loses passage-level retrieval granularity.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q304. Why not use a different embedding model per query?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Document and query vectors need compatible embeddings.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q305. Why not always retrieve more chunks?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> More context can introduce noise and cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q306. Why not add reranking now?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It should solve a measured relevance problem and justify extra cost/latency.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q307. Why not add hybrid search now?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Same reason: evaluate first.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q308. Why doesn't RAG guarantee correctness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Every stage can fail, and the model can still misinterpret or invent details.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q309. What is the strongest design strength of current NovaMind RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It has a genuine separated retrieval pipeline: parsing, chunking, embeddings, Qdrant retrieval and final generation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q310. What is the biggest architectural limitation?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The document/vector lifecycle is request-oriented rather than a durable reusable knowledge-base design.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q311. What would you improve before changing the model?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Measure extraction/retrieval quality and lifecycle correctness first.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q312. Why?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A stronger generator cannot reliably compensate for bad retrieval.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Pressure Questions

## Q313. Isn't RAG just copying document text into a prompt?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The augmentation step does add retrieved text to the prompt, but the important extra system is retrieval: parsing, chunking, embeddings and vector search decide which evidence to supply.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q314. If the model already knows the answer, why use RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Because the goal is to ground the answer in the user's document, not rely on unverifiable model memory.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q315. If the answer is correct but not from the PDF, is that acceptable?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> For a document-Q&A workflow, that is a grounding failure even if the answer happens to be true.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q316. If Qdrant is down, why not answer from Groq?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> That silently removes document grounding and changes the contract of the PDF-RAG workflow.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q317. If top 5 is arbitrary, why did you use it?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It is the current implementation value. I would treat it as a tunable hyperparameter and validate it with retrieval evaluation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q318. Why no reranker?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The current implementation is a simpler baseline RAG pipeline. I would add reranking only after measuring a retrieval-quality problem.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q319. Why no hybrid search?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Same principle: complexity should follow evidence.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q320. Why no OCR?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The current implementation targets text-extractable PDFs; scanned PDFs are a known limitation.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q321. Why no citations?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Mature citations require reliable page/chunk metadata and claim-to-source alignment, which are not yet implemented.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q322. Can a 1000-character chunk split a table badly?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Yes. Fixed character chunking is simple but not structure-aware.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q323. Does that make the RAG bad?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It makes it limited for some document types; quality should be measured on the intended corpus.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q324. Why create a new Qdrant collection per request?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> It simplifies isolation for the immediate request but sacrifices reuse and creates lifecycle/cleanup challenges.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q325. Is that production-ready?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. A production document-Q&A system should have durable document metadata, ownership and collection lifecycle.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q326. Why not use one collection for every user?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> You could, but then metadata isolation, filtering and deletion must be designed carefully.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q327. What is safer: collection-per-document or shared collection?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> There is no universal answer. The choice depends on scale, filtering, operations and tenant-isolation requirements.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q328. Can embeddings leak data?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> They can encode information about source content and should be treated as sensitive derived data.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q329. Can cosine similarity prove relevance?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q330. Can a high retrieval score prove correctness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q331. Can reranking guarantee correctness?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q332. Can citations guarantee truth?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. They improve traceability, but a cited source can still be wrong or misinterpreted.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q333. Why not fine-tune for every company PDF?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> That is inefficient for frequently changing factual documents; RAG is better suited to dynamic knowledge.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q334. Can RAG replace SQL?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. Structured data queries are often better handled directly.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q335. Can RAG replace search engines?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> No. It can incorporate search, but retrieval sources and requirements differ.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q336. If retrieval recall is low, what happens?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The answer model never sees relevant evidence and may fail or hallucinate.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q337. If retrieval precision is low, what happens?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> The model receives noisy/irrelevant context, increasing confusion and token cost.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q338. What is the first thing you'd measure in NovaMind RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Whether the top-5 retrieved chunks actually contain the evidence needed to answer representative questions.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q339. What would you improve before adding another vector database?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> Evaluation, document lifecycle, metadata/ownership, retrieval quality and observability.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

## Q340. What is the correct interview phrase for NovaMind RAG?

**What the interviewer is testing:** Whether you understand the RAG component itself, can identify which pipeline stage owns which responsibility, and can separate general RAG theory from NovaMind's verified implementation.

**Word-for-word answer:**

> A real PDF RAG pipeline with request-oriented indexing and known lifecycle/evaluation limitations.

**Likely follow-up:** Be ready to explain **why this stage exists, what can fail, how you would evaluate it, what the trade-off is, and what Production V2 would improve**.

**Defense reminder:** Never claim that vector similarity, RAG, grounding, or citations guarantee factual correctness.

---

# Rapid-Fire Revision

**Q341. RAG?**  
Retrieval-Augmented Generation.

**Q342. Three stages?**  
Retrieval, augmentation, generation.

**Q343. Parser?**  
`pdf-parse`.

**Q344. Chunk size?**  
~1000 characters.

**Q345. Overlap?**  
~200 characters.

**Q346. Embedding model?**  
`gemini-embedding-001`.

**Q347. Vector DB?**  
Qdrant.

**Q348. Top-k?**  
5.

**Q349. Final answer model path?**  
Groq-backed generation.

**Q350. OCR?**  
Not implemented.

**Q351. Semantic chunking?**  
Not verified.

**Q352. Hybrid search?**  
Not implemented.

**Q353. Reranking?**  
Not implemented.

**Q354. Retrieval threshold?**  
No mature verified threshold.

**Q355. Page citations?**  
Not mature.

**Q356. Persistent document index?**  
Not mature.

**Q357. Reusable follow-up next week?**  
Not reliably supported as a mature lifecycle.

**Q358. Embedding?**  
Text/content → numeric semantic vector.

**Q359. Query embedding?**  
Question → vector.

**Q360. Vector DB generates answer?**  
No.

**Q361. Qdrant = RAG?**  
No.

**Q362. Embedding model = LLM generator?**  
No.

**Q363. Keyword search = semantic search?**  
No.

**Q364. Top-k = relevance threshold?**  
No.

**Q365. Grounded = guaranteed true?**  
No.

**Q366. RAG eliminates hallucination?**  
No.

**Q367. Fine-tuning = RAG?**  
No.

**Q368. Web Search = PDF RAG?**  
No.

**Q369. SQL lookup = RAG?**  
No.

**Q370. Precision@K?**  
Relevant items among top K.

**Q371. Recall@K?**  
Fraction of relevant evidence found in top K.

**Q372. MRR?**  
Mean Reciprocal Rank.

**Q373. Hit rate?**  
Whether at least one relevant result is retrieved.

**Q374. Faithfulness?**  
Answer supported by context.

**Q375. Answer relevance?**  
Answer addresses the question.

**Q376. Context relevance?**  
Retrieved context is useful for the question.

**Q377. Exact vector dimension?**  
Do not claim unless verified.

**Q378. Exact Qdrant metric?**  
Do not claim unless verified.

**Q379. Request-oriented collection?**  
Yes.

**Q380. Durable user→document→collection mapping?**  
No mature mapping.

**Q381. Scanned PDF support?**  
Limited because no OCR.

**Q382. Application credits = RAG provider cost?**  
No.

**Q383. Mature RAG eval suite?**  
No.

**Q384. Best maturity phrase?**  
Real RAG implementation with lifecycle/evaluation limitations.

# Cross-Question Chain 1 — Explain RAG from Zero

**Interviewer:** What is RAG?

> RAG stands for Retrieval-Augmented Generation. Before the model answers, the application retrieves relevant information from an external source, adds that information to the model context, and then asks the model to generate the answer.

**Interviewer:** Why do you need retrieval?

> Because the model may not know private or current information and we want to ground the answer in the user's source.

**Interviewer:** Does RAG train the model?

> No. It supplies external context at inference time.

**Interviewer:** Does it eliminate hallucination?

> No. It reduces the risk by grounding the model, but retrieval and generation can still fail.

---

# Cross-Question Chain 2 — Embeddings

**Interviewer:** What is an embedding?

> A numeric vector that represents semantic meaning.

**Interviewer:** Why do you embed both chunks and questions?

> So they live in a compatible vector space and the vector database can compare the question with document passages.

**Interviewer:** What embedding model do you use?

> Gemini `gemini-embedding-001`.

**Interviewer:** What is the vector dimension?

> I would verify the exact current model/config before quoting a number; it is not established by the verified project summary I am using.

---

# Cross-Question Chain 3 — Chunking

**Interviewer:** Why chunk PDFs?

> To retrieve focused passages instead of treating a large document as one block.

**Interviewer:** What values do you use?

> About 1000 characters per chunk with 200 characters overlap.

**Interviewer:** Why overlap?

> To preserve some meaning across chunk boundaries.

**Interviewer:** Is that optimal?

> It is the current configuration, not a universal optimum. I would validate it on representative RAG questions.

---

# Cross-Question Chain 4 — Qdrant

**Interviewer:** What does Qdrant do?

> It stores the document-chunk embeddings and performs similarity retrieval against the question embedding.

**Interviewer:** Does it generate the answer?

> No.

**Interviewer:** Does Qdrant equal RAG?

> No. It is one retrieval component inside the RAG pipeline.

**Interviewer:** What happens if Qdrant fails?

> The PDF-RAG workflow loses document retrieval, so I would not silently fall back to ungrounded normal chat.

---

# Cross-Question Chain 5 — Top-K

**Interviewer:** What does top 5 mean?

> Qdrant returns the five most similar chunks for the query.

**Interviewer:** Why five?

> That is the current configuration balancing some evidence breadth against context size. I would evaluate it rather than claiming it is universally optimal.

**Interviewer:** Why not 50?

> More chunks can add noise, tokens, latency and cost.

---

# Cross-Question Chain 6 — Bad Answer Debugging

**Interviewer:** The RAG answer is wrong. What do you check?

> I separate the pipeline. First routing, then PDF extraction, chunking, embeddings/indexing, query embedding, retrieved top-five chunks, prompt construction and finally generation.

**Interviewer:** The correct chunk was retrieved but answer is wrong.

> Then the problem is likely generation/prompting rather than retrieval.

**Interviewer:** The correct chunk was never retrieved.

> Then I focus on extraction, chunking, embeddings, collection selection and retrieval configuration.

---

# Cross-Question Chain 7 — Lifecycle

**Interviewer:** Can I upload one PDF today and ask about it next week?

> Not as a mature persistent feature in the current implementation.

**Interviewer:** Why?

> The current design creates a request-oriented collection and lacks a durable user/document-to-collection mapping for reliable later queries.

**Interviewer:** How would you fix it?

> Persist document metadata and ownership, map the document to its Qdrant index/collection, authorize every query and manage retention/deletion.

---

# Cross-Question Chain 8 — RAG vs Fine-Tuning

**Interviewer:** Why not fine-tune the model on the PDF?

> Because the PDF is external factual knowledge that can change. RAG can retrieve current document content at inference time without retraining model weights.

**Interviewer:** When would fine-tuning make more sense?

> When I want to change behavior, style, format or task specialization.

---

# 30-Second Interview Answer

> RAG means Retrieval-Augmented Generation. In NovaMind's PDF RAG flow, the uploaded PDF is parsed with `pdf-parse`, split into roughly 1000-character chunks with 200-character overlap, and embedded using Gemini `gemini-embedding-001`. The vectors are stored in Qdrant. The user's question is embedded with the same model, Qdrant retrieves the top five relevant chunks, and those chunks are added to the prompt for the Groq-backed language model to generate the answer.

---

# 60–90 Second Interview Answer

> NovaMind implements a real PDF RAG pipeline rather than simply sending the whole document to an LLM. The uploaded PDF is first processed with `pdf-parse` to extract text. The text is split into overlapping character-based chunks, approximately 1000 characters with 200 overlap. Each chunk is converted into an embedding using Gemini `gemini-embedding-001` and stored in Qdrant.
>
> When the user asks a question, the question is embedded using the same embedding model. Qdrant performs semantic similarity retrieval and returns the top five relevant chunks. NovaMind then augments the generation prompt with those retrieved chunks and the user question, and the Groq-backed model generates the final answer.
>
> The implementation is genuine RAG, but it still has limitations: no OCR for scanned PDFs, no mature reranking, page citations, thresholding, persistent document-to-index mapping or automated RAG evaluation. So I would describe it as a real request-oriented RAG pipeline rather than a complete enterprise knowledge-base system.

---

# 2–3 Minute Deep Project Defense

> The PDF RAG workflow starts when a user uploads a PDF and asks a question. In Auto mode the LangGraph router recognizes the PDF and routes the request to the PDF RAG specialist. The backend uses `pdf-parse` to extract machine-readable text. It then splits that text into roughly 1000-character chunks with 200-character overlap. The overlap helps preserve context where ideas cross chunk boundaries.
>
> Each chunk is sent to Gemini `gemini-embedding-001`, which converts the text into a semantic vector. Those vectors are stored in a Qdrant collection. When the user asks the question, NovaMind creates a query embedding with the same model and performs similarity search in Qdrant. The current implementation retrieves the top five chunks.
>
> Those chunks are then added to the generation context along with the user's question. The Groq-backed language-model path generates the final response from that context. This separation is important: Gemini creates vector representations, Qdrant performs retrieval, and Groq performs final text generation.
>
> I do not claim that RAG eliminates hallucination. Retrieval can return weak chunks, the PDF extraction can be poor, and the LLM can still generate unsupported details. The current implementation also uses request-oriented Qdrant collection creation, so it does not yet behave like a mature persistent document knowledge base. It also lacks OCR, reranking, mature page citations, thresholding and automated RAG evaluation.
>
> For Production V2, I would first create a durable document lifecycle with document IDs, ownership, Qdrant index mapping and deletion/retention rules. Then I would build a labeled RAG evaluation set to measure retrieval relevance and answer groundedness before deciding whether techniques such as reranking, hybrid search or alternative chunking are actually needed.

---

# Whiteboard Flow

Draw:

```text
PDF
 ↓
pdf-parse
 ↓
Extracted Text
 ↓
Chunking
1000 / 200 overlap
 ↓
Gemini Embeddings
 ↓
Qdrant

Question
 ↓
Gemini Query Embedding
 ↓
Qdrant Top-5 Search
 ↓
Relevant Chunks
 +
Question
 ↓
Groq-backed LLM
 ↓
Answer
```

Then draw a second box:

```text
Current limitations:
No OCR
No reranking
No hybrid search
No mature threshold
No page citations
No persistent document mapping
No mature RAG evaluation
```

---

# What Not to Say

Do not say:

- “RAG prevents hallucinations.”
- “Qdrant is the RAG model.”
- “Gemini generates the final PDF-RAG answer.”
- “We fine-tuned the model on PDFs.”
- “Every PDF is permanently indexed.”
- “Users can always ask follow-up questions later.”
- “We support scanned PDFs with OCR.”
- “We have hybrid search.”
- “We use reranking.”
- “We provide verified page citations.”
- “Top five is the best retrieval setting.”
- “Vector similarity proves factual correctness.”
- “The exact vector dimension is X” unless verified from the current model/config.
- “Qdrant uses cosine” unless verified from the current collection configuration.
- “RAG is production-ready because retrieval works.”

---

# Final Self-Test

Before Module 09, you should be able to explain without notes:

- what RAG is
- retrieval / augmentation / generation
- RAG vs prompting
- RAG vs fine-tuning
- RAG vs web search
- RAG vs SQL
- parsing
- OCR
- chunking
- chunk size / overlap
- embeddings
- vector dimensions
- semantic similarity
- keyword vs semantic vs hybrid search
- Qdrant
- vector DB vs RAG
- query embedding
- similarity search
- top-k
- thresholds
- reranking
- context construction
- grounding
- hallucination
- retrieval vs generation failure
- Precision@K / Recall@K / MRR / hit rate
- answer faithfulness and relevance
- citations
- metadata
- persistent indexes
- document ownership
- prompt injection
- RAG latency/cost
- NovaMind's exact PDF RAG flow
- current limitations
- troubleshooting
- Production V2 architecture

**Module 08 interview preparation complete.**
