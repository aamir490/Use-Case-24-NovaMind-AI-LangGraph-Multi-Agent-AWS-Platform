# Module 09 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** NovaMind PDF RAG, Qdrant and Document Lifecycle  
> **Purpose:** Prepare for deep implementation, architecture, lifecycle, troubleshooting, Qdrant, security, Production V2, and pressure questions about NovaMind's real PDF RAG system.

---

## Accuracy Rules

### Verified current implementation

```text
PDF upload is processed as a temporary file.
pdf-parse extracts text.
Chunk size is about 1000 characters.
Chunk overlap is about 200 characters.
Gemini gemini-embedding-001 creates embeddings.
A new/request-oriented Qdrant collection is created.
The question is embedded with the same embedding model.
Qdrant retrieves top 5 similar chunks.
Retrieved context + question go to a Groq-backed LLM.
The assistant response is persisted through Chat/MongoDB.
Redis is used for fast conversation/session state.
Temporary PDF cleanup occurs after processing.
```

### Do not claim as current

```text
Persistent PDF source storage in S3
OCR
durable documentId → collectionId mapping
reliable long-term text-only follow-up
page-level citations
reranking
hybrid search
mature retrieval threshold
automatic Qdrant collection cleanup
mature RAG evaluation
fully hardened tenant isolation
```

### Production V2 items must be described as proposals

```text
persistent source storage
document metadata
owner mapping
reusable Qdrant indexes
OCR
citations
reranking
hybrid retrieval
async indexing
retention/deletion
reconciliation
```

---

# Foundation and Architecture

## Q1. What is the purpose of NovaMind's PDF RAG specialist?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It lets a user ask questions about an uploaded PDF by retrieving relevant document chunks and using those chunks as context for answer generation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q2. Where does PDF RAG run?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Inside the Agent service as one of the eight predefined LangGraph specialist workflows.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q3. Is PDF RAG a separate ECS service?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q4. How does a PDF request reach the specialist?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> React sends the multipart request through the Express Gateway to Agent, and the LangGraph router selects PDF RAG in Auto mode when a PDF is uploaded.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q5. Does PDF upload always force PDF RAG?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. Explicit non-Auto workflow selection has higher priority.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q6. What is the simplest current flow?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Upload PDF → temporary file → parse → chunk → embed → Qdrant → query embedding → top-5 retrieval → Groq-backed answer → persistence/cleanup.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q7. Is NovaMind's implementation genuine RAG?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Yes, because it has a separate retrieval pipeline with embeddings and vector search before generation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q8. What is the best maturity description?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A genuine request-oriented PDF RAG implementation, not yet a mature persistent document knowledge base.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q9. What is the biggest architectural limitation?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> There is no mature durable user/document-to-Qdrant mapping for reliable later reuse.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q10. What is the biggest strength?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The separation of extraction, chunking, embeddings, vector retrieval and final generation is real and clearly implemented.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Upload and Temporary File Lifecycle

## Q11. How is the uploaded PDF received?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Through multipart upload handling using Multer in the backend.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q12. Where is the uploaded PDF kept during the current request?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> As a temporary local file.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q13. Is the uploaded PDF currently persisted as a reusable S3 document?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not in the verified current RAG lifecycle.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q14. Why is temporary storage simple?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It supports the immediate parse-and-answer flow without needing a durable document lifecycle.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q15. What is the downside of temporary storage?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The source cannot be reliably reused later unless it is uploaded again or separately persisted.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q16. What should happen after processing?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The temporary PDF should be deleted.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q17. Can cleanup fail?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q18. Why is cleanup failure important?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Private files can remain on disk and disk usage can grow.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q19. Would S3 persistence be a current project fact?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. That is a proposed Production V2 improvement for uploaded source documents.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q20. What would source persistence enable?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Re-indexing, audit, later reuse, OCR retry and versioning.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# PDF Parsing and OCR

## Q21. What library extracts PDF text?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> `pdf-parse`.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q22. What does `pdf-parse` return?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Machine-readable text extracted from the PDF.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q23. Does it perform OCR?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not in the verified current flow.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q24. What happens with a scanned image-only PDF?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Text extraction may be insufficient because OCR is not implemented.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q25. Why is extraction quality important?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Everything downstream—chunking, embeddings, retrieval and generation—depends on the extracted text.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q26. What should the system do if almost no text is extracted?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Return a clear document-processing limitation/error rather than indexing meaningless content.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q27. What Production V2 feature would help scanned documents?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> An OCR stage.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q28. Would OCR guarantee perfect extraction?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q29. What document types are particularly difficult?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Scanned PDFs, complex tables, multi-column layouts and image-heavy documents.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q30. Is table-aware extraction verified?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Chunking

## Q31. What chunk size does NovaMind use?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Approximately 1000 characters.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q32. What overlap does it use?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Approximately 200 characters.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q33. Why chunk at all?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> To retrieve focused passages rather than treating the whole PDF as one unit.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q34. Why use overlap?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> To preserve context across chunk boundaries.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q35. Is the current chunker semantic-aware?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No, the verified implementation is character-based.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q36. Is 1000 characters universally best?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q37. What happens if chunks are too small?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Context becomes fragmented and the number of vectors increases.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q38. What happens if chunks are too large?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retrieval becomes less precise and more irrelevant text enters the LLM context.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q39. What is structure-aware chunking?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Splitting by sections, headings, paragraphs or other document structure.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q40. Is structure-aware chunking current?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No; it is a future improvement.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q41. How would you choose better chunk size?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Use a labeled RAG evaluation set and compare retrieval/answer quality, latency and cost.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q42. Can poor chunking cause hallucination?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Indirectly, by causing poor retrieval and weak grounding.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Embeddings

## Q43. What embedding model is used?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> `gemini-embedding-001`.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q44. What is embedded?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Document chunks and the user question.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q45. Why embed the question with the same model?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> So query and chunk vectors exist in a compatible semantic space.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q46. Does the embedding model generate the final answer?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q47. What happens if embeddings fail?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The document cannot be indexed or queried correctly.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q48. Can a stronger answer model compensate for bad embeddings?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not reliably.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q49. What exact vector dimension is used?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The verified project summary does not establish a dimension, so I would not quote one without checking the exact current model/config.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q50. Why should embedding model/version be stored in Production V2 metadata?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Changing embedding models can make old vectors incompatible with new queries.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q51. Can embeddings be treated as non-sensitive?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. They are derived from private source content and should be protected.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q52. Would batch embedding help?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Potentially for throughput, but batching is not a verified current feature.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Qdrant Collections

## Q53. What does Qdrant do?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It stores chunk vectors and performs similarity retrieval.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q54. What is a Qdrant collection?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A logical container for vector records.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q55. What collection behavior does current NovaMind use?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A new request-oriented/timestamp-style collection is created in the PDF RAG flow.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q56. Why is that simple?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It isolates the immediate request without needing document lookup logic.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q57. What is the downside?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Repeated indexing, difficult reuse, orphaned collections and cleanup complexity.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q58. Does keeping the collection automatically enable later follow-up?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q59. Why not?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The application lacks a mature durable mapping from user/document identity to that collection.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q60. What is an orphaned collection?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A vector collection that exists but is not properly mapped into an application ownership/lifecycle record.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q61. Is automatic collection cleanup mature?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q62. Why does collection cleanup matter?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Storage cost, privacy and operational hygiene.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q63. Would collection-per-document always be best in V2?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. Shared collections with metadata filtering are another design option.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q64. What should determine collection strategy?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Scale, tenant isolation, filtering, deletion and operational constraints.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Query and Retrieval

## Q65. What happens when the user asks the PDF question?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The question is embedded, then Qdrant searches for similar chunk vectors.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q66. How many chunks are retrieved?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Top five.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q67. Does top five mean five definitely relevant chunks?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q68. Is top five universally best?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q69. What is the purpose of top-k?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> To limit retrieved context to the most relevant candidates.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q70. What is a retrieval threshold?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A minimum relevance/similarity requirement before using retrieved chunks.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q71. Does current NovaMind have a mature threshold?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q72. What is reranking?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Reordering an initial candidate set with a second relevance model or algorithm.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q73. Is reranking implemented?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q74. What is hybrid retrieval?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Combining lexical/keyword and semantic vector search.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q75. Is hybrid retrieval implemented?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q76. What is the safe statement about Qdrant's metric?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Qdrant performs similarity retrieval; I would not claim an exact metric unless I verify the collection configuration.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Context Construction and Generation

## Q77. What happens after retrieval?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The retrieved chunks are combined with the user question and instructions to form the generation context.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q78. Who generates the final answer?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The Groq-backed language-model path.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q79. Does Qdrant generate the answer?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q80. Does Gemini generate the answer in this flow?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. Gemini is used for embeddings.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q81. What does grounding mean here?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The LLM receives evidence from the PDF before answering.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q82. Does grounding guarantee correctness?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q83. Can the LLM ignore the retrieved evidence?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q84. Can the LLM add unsupported facts?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q85. What is faithfulness?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> How well the answer is supported by the retrieved context.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q86. What is answer relevance?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> How well the answer addresses the user's question.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q87. What should happen if no evidence is good enough?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A mature system should say there is insufficient document evidence rather than inventing an answer.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q88. Is a mature no-answer policy implemented?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Conversation Persistence and Redis

## Q89. Where is the assistant answer persisted?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Through the Chat service into MongoDB.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q90. What can Redis store in this architecture?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Sessions, fast conversation context and counters.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q91. Does Redis store the Qdrant document mapping?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not as a mature durable document lifecycle.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q92. Is Redis LangGraph checkpointing?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q93. Can chat history persistence identify the old Qdrant collection?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not reliably by itself.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q94. Why not?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Conversation persistence and document-index identity are separate concerns.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q95. Does MongoDB storing the old answer mean the old vectors are reusable?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q96. Can Redis survive a service restart?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Potentially, depending on the external Redis deployment, but that does not solve document mapping.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q97. What should V2 persist in MongoDB?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Document identity, ownership, collection/index mapping, status, source metadata, versions and retention information.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q98. What is the key distinction?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Conversation memory is not document-index lifecycle.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Current Lifecycle Limitation

## Q99. Can a user upload once and reliably ask about the same PDF next week?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not as a mature supported workflow.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q100. Why not?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> There is no durable document ID and collection mapping for later text-only questions.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q101. Could the Qdrant collection still physically exist?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Yes, but physical existence does not equal application-level discoverability/authorization.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q102. What makes reuse reliable?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Stable document identity, owner mapping, collection mapping and authorization.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q103. Why is long-term document chat different from chat memory?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It requires durable source/index identity, not only prior message text.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q104. What is request-oriented RAG?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A design optimized to answer the current upload/question rather than maintain a long-lived document knowledge object.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q105. What is persistent RAG?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A design where the document is indexed once, mapped to durable metadata, and authorized/reused across later requests.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q106. Why is this distinction important in interviews?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It prevents overclaiming a persistent knowledge-base capability that the project does not currently have.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Production V2 Document Identity

## Q107. What is the first V2 improvement?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Create a durable `documentId` at upload time.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q108. What else should be stored?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Owner/user ID, source metadata, collection/index ID, status, created time, retention and versions.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q109. Why does owner ID matter?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> To enforce tenant isolation and authorization.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q110. Why does collection ID matter?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> So later queries can find the existing vectors.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q111. Why does status matter?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The system should distinguish UPLOADED, PROCESSING, READY, FAILED and deleted states.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q112. Why store embedding version?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> So the application knows which model created existing vectors.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q113. Why store chunking version?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> So index behavior is reproducible and reindexing can be managed.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q114. Why store source filename?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> For display, audit and source tracking.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q115. Should document metadata be the only authorization control?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. Server-side authorization must still validate every request.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Production V2 Source Storage

## Q116. Would you persist source PDFs in V2?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> If reusable document chat is required, yes, private durable storage is a strong design option.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q117. What storage could be used?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Private S3 is a reasonable AWS design, but it is a proposed improvement rather than current project fact.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q118. Why keep the source file?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Re-indexing, OCR, download, audit and versioning.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q119. Why not keep every source forever?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Privacy, retention requirements and storage cost.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q120. What should protect the object?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Private access, least-privilege IAM, encryption and authorized delivery.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q121. Would presigned URLs be permanent?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q122. Should vector deletion be linked to source deletion?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Yes, according to lifecycle policy.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q123. What if source exists but vector index is missing?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Reconciliation should detect and repair/reindex or mark the document failed.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Production V2 Persistent Index

## Q124. What is persistent indexing?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Building vectors once and reusing them for future queries.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q125. What is the main benefit?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Lower repeated latency/cost and reliable follow-up.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q126. What new risk does it add?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Long-lived private data that needs ownership, retention and deletion controls.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q127. Should V2 use collection-per-document?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It is one option, not the only valid design.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q128. What is the alternative?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Shared collection with strong metadata filtering by owner/document.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q129. Why are metadata filters useful?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> They restrict retrieval scope and improve tenant isolation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q130. What should each chunk metadata contain?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> At minimum document ID, owner ID, chunk ID and source/page/section data where available.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q131. What happens when embedding model changes?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Reindexing may be necessary.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q132. What happens when chunking strategy changes?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Existing indexes may need versioned reindexing.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q133. When should a document be queryable?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Only after indexing is successfully marked READY.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Production V2 OCR, Citations, Reranking

## Q134. When should OCR be added?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> When scanned/image-only PDFs are a real requirement.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q135. What is required for citations?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Reliable source/page/chunk metadata and answer-evidence alignment.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q136. Would page numbers alone guarantee correct citations?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q137. When should reranking be added?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Only after evaluation shows top-k vector retrieval quality is insufficient.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q138. When should hybrid search be added?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> When exact lexical terms are a measured retrieval problem.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q139. Why not add all advanced techniques immediately?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> They add latency, cost, dependencies and operational complexity.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q140. What should come before reranking?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A labeled RAG evaluation dataset.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q141. What should come before citations?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Reliable source metadata and chunk traceability.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q142. What should come before OCR?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A requirement showing scanned PDFs matter to users.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Async Indexing and Jobs

## Q143. Why might indexing become asynchronous?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Large PDFs can take too long for one synchronous HTTP request.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q144. What would the async flow look like?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Upload → create document record → queue job → worker parses/chunks/embeds/indexes → mark READY.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q145. Is async indexing current?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q146. What is a job ID?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A durable identifier for one indexing operation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q147. Why must indexing jobs be idempotent?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retries should not create duplicate uncontrolled indexes.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q148. What is a job retry policy?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Rules for retrying transient failures without endlessly repeating work.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q149. What is a dead-letter path?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A place/state for jobs that repeatedly fail and need manual/reconciliation handling.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q150. Why is progress useful?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The frontend can show PROCESSING rather than timing out.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q151. What is the trade-off of async indexing?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> More infrastructure, state transitions and operational complexity.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Deletion, Retention and Reconciliation

## Q152. What should deleting a document remove?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Source file, document metadata, vector records/index and relevant caches according to policy.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q153. Why is vector deletion important?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Otherwise deleted private content can remain retrievable.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q154. What is retention policy?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Rules defining how long documents and vectors are kept.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q155. Why is retention important?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Privacy, compliance and cost.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q156. What is reconciliation?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Checking that metadata, source objects and Qdrant indexes agree.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q157. Give a reconciliation mismatch.

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> MongoDB says READY but Qdrant collection is missing.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q158. Give another mismatch.

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Qdrant collection exists but there is no document metadata owner mapping.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q159. Why is reconciliation useful?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Distributed operations can partially fail.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q160. Should failed deletion be silently ignored?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q161. What lifecycle events should be audited?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Upload, indexing, access, reindex, deletion and administrative changes.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Failure Modes

## Q162. What if `pdf-parse` fails?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Return a document-processing error and do not proceed as if indexing succeeded.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q163. What if chunking returns no useful chunks?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Treat the document as not indexable and surface a clear failure.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q164. What if Gemini embedding fails halfway?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The index may be incomplete; do not mark the document successfully indexed.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q165. What if Qdrant collection creation fails?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No vectors can be stored, so retrieval cannot proceed.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q166. What if only some Qdrant writes succeed?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The index is partial and should be treated as failed/incomplete.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q167. What if query embedding fails?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Similarity retrieval cannot be performed.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q168. What if Qdrant search fails?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Document-grounded answering is unavailable.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q169. What if Groq fails after retrieval?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retrieval succeeded, but generation failed.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q170. What if answer generation succeeds but Chat persistence fails?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The response exists, but durable conversation history can be incomplete.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q171. What if temporary cleanup fails?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The answer may still be correct, but local-file lifecycle cleanup failed.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q172. Should all these return the same generic 200 response?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. Production V2 should use structured error semantics.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Retry and Idempotency

## Q173. Why not retry the whole RAG request blindly?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Parsing/indexing/provider calls and persistence may already have produced side effects or cost.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q174. What is safe retry?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retry only the failed stage when it is idempotent or its side effects are controlled.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q175. What stages are good retry candidates?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Transient provider/network operations, if request identity and side effects are controlled.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q176. Why is Qdrant index creation idempotency important?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retries should not create multiple duplicate collections for the same logical document version.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q177. Why is message idempotency important?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retries should not duplicate conversation messages.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q178. Why is credit idempotency important?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retries should not deduct multiple times.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q179. What should a V2 indexing job key include?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Document/version identity so repeated attempts target the same logical work.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Security and Tenant Isolation

## Q180. What is the main RAG authorization rule?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> A user must only query documents they are authorized to access.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q181. Should the LLM enforce that?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q182. Where should authorization happen?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Deterministic backend/service logic before retrieval.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q183. What is a cross-tenant retrieval bug?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> User A's query retrieves chunks from User B's document.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q184. How can metadata filtering help?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Filter by owner and document identity before similarity retrieval.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q185. Can collection-per-document reduce cross-tenant risk?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It can simplify isolation, but authorization is still required.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q186. What is prompt injection in PDF RAG?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Malicious document text tries to manipulate model behavior.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q187. Should PDF text be treated as trusted instructions?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No, it is untrusted data.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q188. Could embeddings be sensitive?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q189. Why avoid logging full chunks?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> They may contain private document content.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q190. What security issue appears if old orphaned collections remain?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Private data may remain stored without proper ownership/lifecycle tracking.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q191. What should source S3 permissions be in V2?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Private and least-privilege.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Evaluation and Quality

## Q192. What should be evaluated separately?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Extraction, retrieval and generation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q193. How do you test extraction?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Compare extracted text with expected source content.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q194. How do you test retrieval?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Use labeled questions with known relevant chunks/pages.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q195. How do you test generation?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Measure groundedness, relevance and correctness using retrieved evidence.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q196. What is Precision@K?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The fraction of top-K chunks that are relevant.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q197. What is Recall@K?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> How much known relevant evidence appears in the top-K results.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q198. What is hit rate?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Whether at least one relevant result is retrieved.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q199. What is groundedness?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> How strongly the answer is supported by retrieved context.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q200. Does NovaMind currently have mature RAG evaluation?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q201. Why is evaluation required before reranking?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Otherwise you cannot prove reranking improves results.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q202. Why is evaluation required before changing chunk size?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Chunking changes retrieval behavior and should be measured.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q203. What would a regression suite protect against?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Quality drops after prompt/model/chunking/index changes.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Troubleshooting

## Q204. The answer is wrong. What is your first check?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Confirm the request actually routed to PDF RAG with the intended PDF.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q205. Next check?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Verify extracted text.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q206. Then?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Inspect chunks.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q207. Then?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Verify embeddings and collection creation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q208. Then?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Inspect the top-five retrieved chunks.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q209. If top-five chunks are irrelevant, what category of problem is this?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Retrieval/indexing quality.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q210. If top-five chunks contain the answer but output is wrong?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Generation/prompting issue.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q211. If first question works but later text-only follow-up cannot find the document?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Document-index lifecycle/mapping issue.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q212. If upload is very slow?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Measure parse time, chunk count, embedding time, Qdrant writes, retrieval and generation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q213. If many collections accumulate?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The missing collection cleanup/retention lifecycle is the likely issue.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q214. If another user's content appears?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Treat it as a severe tenant-isolation/authorization incident.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q215. If a scanned PDF gives nonsense?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> OCR is missing; extraction is the likely root cause.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Performance and Cost

## Q216. Why is first-question PDF RAG expensive?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It includes parsing, many chunk embeddings, vector writes, query embedding, search and generation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q217. What is the biggest repeated-cost problem?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Re-embedding the same document on repeated uploads.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q218. How does persistent indexing reduce cost?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Embed once and reuse.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q219. How does top-k affect generation cost?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> More chunks increase input tokens.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q220. How does chunk size affect index cost?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Smaller chunks increase vector count.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q221. Can more ECS Agent tasks reduce embedding provider cost?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q222. Can more Qdrant capacity fix poor retrieval quality?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q223. Can a faster LLM fix missing document mapping?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q224. What should be measured?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Chunk count, embedding calls, retrieval latency, LLM tokens, failures and per-document/index storage.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q225. When would async ingestion improve performance?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> When document indexing is long enough to make synchronous request handling impractical.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Design Defense

## Q226. Why use a new collection in the current request flow?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It simplifies immediate isolation, but it is not ideal for long-term reuse.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q227. Why is that acceptable for a prototype/portfolio workflow?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It demonstrates genuine end-to-end RAG with less lifecycle complexity.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q228. Why is it not enough for production?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Production requires ownership, reuse, retention, deletion, monitoring and recovery.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q229. Why not keep the temporary PDF forever on local disk?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Container-local storage is not a durable document store and creates privacy/operational problems.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q230. Why not use Redis to store the PDF mapping permanently?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Durable application metadata is better suited to persistent storage and clear ownership/lifecycle logic.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q231. Why not simply store all PDF text in MongoDB and skip Qdrant?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> MongoDB can store text, but the current design uses Qdrant for semantic vector retrieval; alternatives should be evaluated based on requirements.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q232. Why not fall back to Chat if Qdrant fails?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> That changes the semantic guarantee from document-grounded answer to ungrounded chat.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q233. Why not return all chunks to the model?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Too much irrelevant context increases cost/latency and can reduce focus.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q234. Why not delete the Qdrant collection immediately after every answer?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> That would prevent reuse even if you later wanted follow-up; lifecycle should match product requirements.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q235. Why not keep every collection forever?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Storage/privacy/cleanup risks.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q236. What would you build first in V2?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Document identity, owner mapping, persistent collection mapping and lifecycle state before advanced retrieval features.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Pressure Questions

## Q237. If Qdrant collections survive, why do you say the document isn't persistent?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Persistence is more than physical storage. The application needs durable ownership and document-to-index mapping to discover and authorize the correct collection later.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q238. Why can't Redis conversation memory remember which PDF was used?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It can remember conversation context, but the verified design does not provide a mature durable document-to-Qdrant identity mapping through Redis.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q239. Why not store collection name in the conversation message?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> That could be part of a stronger design, but it still needs ownership, lifecycle, deletion and authorization rules; the current project does not implement a mature version of that.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q240. Is request-based collection creation a bad design?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not inherently. It is simple for one-shot Q&A, but it is limited for reusable document chat and requires cleanup.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q241. What if the collection name contains a timestamp—can you search by timestamp later?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> That is not a reliable business identity. Later queries should use stable document/user metadata, not guess a collection from timing.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q242. Why not put userId in every Qdrant collection name?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> It can help naming, but naming alone is not enough for authorization, metadata lifecycle or retention.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q243. Can Qdrant metadata filters fully replace backend authorization?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q244. Why are page citations missing?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The current implementation does not have a mature page/chunk metadata-to-answer citation pipeline.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q245. Can you claim top-5 retrieval is accurate?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> I can say it retrieves the top five according to similarity, not that all five are factually relevant.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q246. Can you claim cosine similarity?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not unless I verify the exact current Qdrant collection metric.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q247. Can you claim vector dimension?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Not unless I verify the exact embedding model/config.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q248. Why no OCR?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The current scope targets text-extractable PDFs; scanned PDFs are a known limitation.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q249. Why no reranking?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> The implementation is a baseline RAG pipeline; I would add reranking only if evaluation proves it improves relevance.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q250. Why no hybrid search?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Same principle: add complexity based on measured need.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q251. What would make this enterprise-grade?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Durable document lifecycle, ownership, retention/deletion, reliable indexing status, evaluation, observability, citations, OCR where needed and hardened authorization.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q252. Is the current RAG production-ready?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> No. It is production-oriented and functionally real, but document lifecycle, security, evaluation and reliability need further hardening.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

## Q253. What's the most important thing you learned from this design?

**What the interviewer is testing:** Whether you understand both the current implementation and the document/index lifecycle problem rather than only memorizing the RAG pipeline.

**Word-for-word answer:**

> Building RAG is not only about embeddings and vector search; the harder production problem is managing document identity, ownership, index lifecycle, quality and failure recovery.

**Likely follow-up:** Be ready to explain **what survives after the request, how the application would find the same Qdrant data later, what fails at each stage, how ownership should work, and what is current vs proposed**.

**Defense reminder:** Physical vector persistence is not the same as a mature reusable document lifecycle.

---

# Rapid-Fire Revision

**Q254. PDF parser?**  
`pdf-parse`.

**Q255. Chunk size?**  
~1000 characters.

**Q256. Overlap?**  
~200 characters.

**Q257. Embedding model?**  
`gemini-embedding-001`.

**Q258. Vector DB?**  
Qdrant.

**Q259. Top-k?**  
5.

**Q260. Final generator?**  
Groq-backed LLM.

**Q261. Uploaded PDF current storage?**  
Temporary local processing.

**Q262. Persistent source S3 current?**  
No.

**Q263. New Qdrant collection per request flow?**  
Yes.

**Q264. Durable documentId→collectionId mapping?**  
No mature mapping.

**Q265. Reliable text-only follow-up later?**  
No.

**Q266. OCR?**  
No.

**Q267. Page citations?**  
Not mature.

**Q268. Reranking?**  
No.

**Q269. Hybrid search?**  
No.

**Q270. Mature threshold?**  
No.

**Q271. Automatic collection cleanup?**  
Not mature/verified.

**Q272. Conversation persistence?**  
Chat service → MongoDB.

**Q273. Redis role?**  
Sessions + fast conversation context/counters.

**Q274. Redis = Qdrant mapping?**  
No.

**Q275. Redis = LangGraph checkpointing?**  
No.

**Q276. Qdrant = LLM?**  
No.

**Q277. Qdrant = entire RAG system?**  
No.

**Q278. Embeddings = final answer?**  
No.

**Q279. Physical collection survives = persistent product feature?**  
No.

**Q280. Best current description?**  
Request-oriented genuine PDF RAG.

**Q281. V2 first priority?**  
Durable document identity + ownership + index mapping.

**Q282. V2 source storage?**  
Private durable storage such as S3, proposed.

**Q283. V2 later question flow?**  
Authorize document → reuse mapped index → retrieve → generate.

**Q284. Scanned PDF support current?**  
No OCR, so limited.

**Q285. Mature RAG eval suite?**  
No.

**Q286. Production-ready?**  
No; production-oriented with lifecycle gaps.

# Cross-Question Chain 1 — Current Flow

**Interviewer:** Explain your PDF RAG end to end.

> The uploaded PDF reaches the Agent service and is routed to the PDF RAG specialist. It is handled as a temporary local file, `pdf-parse` extracts the text, the text is split into roughly 1000-character chunks with 200-character overlap, and `gemini-embedding-001` creates embeddings. NovaMind creates a new Qdrant collection, stores the chunk vectors, embeds the user question with the same model, retrieves the top five similar chunks and gives those chunks plus the question to the Groq-backed language model for final generation. The answer is persisted through the Chat service and the temporary PDF is cleaned up.

---

# Cross-Question Chain 2 — Why Later Follow-Up Is Limited

**Interviewer:** If Qdrant stores the vectors, why can't I ask later?

> Because vector persistence alone is not enough. The application does not maintain a mature durable user/document-to-Qdrant mapping that can reliably identify and authorize the correct collection on a later text-only request.

**Interviewer:** Can't Redis remember it?

> Redis stores application sessions and fast conversation context, but that is not the same as a durable document-index lifecycle.

**Interviewer:** How would you fix it?

> Create a stable document ID, persist ownership and collection mapping, and authorize every later query before reusing the index.

---

# Cross-Question Chain 3 — Collection Lifecycle

**Interviewer:** Why create a new collection?

> It simplifies one-request isolation and demonstrates a clear RAG flow.

**Interviewer:** What's wrong with that?

> For reusable document chat it causes repeated embeddings, many collections, cleanup issues and no strong long-term document identity.

**Interviewer:** Should you delete it immediately?

> That depends on the product requirement. If the workflow is strictly one-shot, deletion may be appropriate. If reuse is required, it needs a persistent ownership/lifecycle model rather than ad hoc retention.

---

# Cross-Question Chain 4 — Qdrant Failure

**Interviewer:** Qdrant is down. What do you do?

> I would surface the retrieval failure rather than silently answer with normal Chat, because that would remove the PDF grounding guarantee.

**Interviewer:** Why not just send the whole PDF to Groq?

> That would be a different fallback strategy with different context, cost and size constraints and is not the current verified behavior.

---

# Cross-Question Chain 5 — Production V2

**Interviewer:** Design a production document lifecycle.

> At upload time I would create a document record with owner, document ID, source metadata and indexing status. I would persist the source privately, run parse/chunk/embed as a reliable indexing process, map the document to the Qdrant index/collection, store page/chunk metadata and mark the document READY only after indexing succeeds. Later questions would authorize access, reuse the existing index, retrieve context and generate the answer. Deletion would remove the source and vectors according to retention policy.

---

# Cross-Question Chain 6 — Citations

**Interviewer:** Why don't you show page citations now?

> Mature page citations need page-aware extraction/chunk metadata and reliable answer-to-evidence alignment. Those are not fully implemented in the current flow.

**Interviewer:** Can you just ask the LLM to invent page numbers?

> No. Citations should be derived from traceable source metadata, not model guesses.

---

# Cross-Question Chain 7 — OCR

**Interviewer:** Why doesn't a scanned PDF work well?

> The current parser extracts machine-readable PDF text but the workflow has no OCR stage for text that only exists inside page images.

**Interviewer:** What would you add?

> An OCR/document-processing stage before chunking, with quality checks and page metadata.

---

# 30-Second Interview Answer

> NovaMind's current PDF RAG is request-oriented. The uploaded PDF is processed as a temporary file, parsed with `pdf-parse`, split into about 1000-character chunks with 200 overlap, embedded with Gemini `gemini-embedding-001`, and stored in a new Qdrant collection. The question is embedded, Qdrant retrieves the top five relevant chunks, and a Groq-backed LLM generates the answer from that context. The main lifecycle limitation is that there is no mature durable document-to-collection mapping for reliable later reuse.

---

# 60–90 Second Interview Answer

> The PDF RAG specialist is inside the Agent service. In Auto mode, a PDF upload routes to that workflow. Multer handles the uploaded file temporarily and `pdf-parse` extracts text. NovaMind then performs character-based chunking at roughly 1000 characters with 200 overlap, creates embeddings with `gemini-embedding-001`, creates a new Qdrant collection and stores the chunk vectors. The user's question is embedded with the same model and Qdrant returns the top five similar chunks. Those chunks are added to the generation context and a Groq-backed LLM creates the final answer. The response is persisted through Chat/MongoDB and the temporary PDF is cleaned up.
>
> The key limitation is document lifecycle. The Qdrant collection can exist, but there is no mature durable user/document-to-collection mapping, so later text-only follow-up cannot reliably reopen and authorize the same document index. That is why I describe the current implementation as real but request-oriented RAG rather than a persistent knowledge-base system.

---

# 2–3 Minute Project Defense

> NovaMind's PDF RAG has a genuine separation between ingestion, retrieval and generation. When the user uploads a PDF and asks a question, the request reaches the Agent service and LangGraph routes it to the PDF RAG specialist. The uploaded file is temporary; it is not currently treated as a permanent document object. `pdf-parse` extracts the PDF text, and the text is split into approximately 1000-character chunks with 200-character overlap.
>
> Each chunk is embedded using Gemini `gemini-embedding-001`. The workflow creates a new Qdrant collection for that request/indexing flow and stores the chunk vectors. The user question is embedded using the same embedding model, Qdrant performs similarity retrieval and returns the top five chunks, and those retrieved chunks are added to the prompt for the Groq-backed language model to generate the answer.
>
> After generation, the assistant answer is persisted through the Chat service into MongoDB, Redis can hold fast conversation context, and the temporary PDF is cleaned up. The important limitation is that conversation persistence is not the same as persistent document retrieval. The project does not have a mature durable mapping between a user, a document ID and its Qdrant collection, so a later text-only question cannot reliably identify and reuse the same PDF index.
>
> For Production V2, I would first create a real document lifecycle rather than immediately adding advanced retrieval algorithms. At upload time I would create a document ID and ownership record, persist the source privately if reusable documents are required, run parsing/chunking/embedding as a reliable indexing process, persist the document-to-index mapping, store page/chunk metadata and mark the document READY only after indexing completes. Later queries would authenticate and authorize the document before retrieving. I would also define retention/deletion and collection cleanup. Only after building a RAG evaluation dataset would I decide whether OCR, reranking, hybrid search, retrieval thresholds or different chunking materially improve quality.

---

# Current vs Production V2 — Interview Table

| Area | Current NovaMind | Production V2 proposal |
|---|---|---|
| PDF source | Temporary local file | Durable private source storage if reuse is required |
| Identity | Request/conversation context | Stable `documentId` |
| Ownership | No mature document ownership lifecycle | `ownerId` + authorization |
| Chunking | ~1000 chars / 200 overlap | Versioned / possibly structure-aware |
| Embeddings | Gemini `gemini-embedding-001` | Same or evaluated replacement, versioned |
| Qdrant | New request-oriented collection | Persistent mapped index/collection |
| Later reuse | Not reliable | Authorized reusable index |
| OCR | Not implemented | Add if required |
| Citations | Not mature | Page/chunk metadata + source alignment |
| Reranking | Not implemented | Add only if evaluation proves benefit |
| Hybrid search | Not implemented | Optional if measured need |
| Threshold | Not mature | Calibrated no-answer/relevance policy |
| Cleanup | Temp PDF cleanup; collection cleanup not mature | Source/vector retention and deletion lifecycle |
| Evaluation | No mature suite | Retrieval + groundedness regression suite |
| Async ingestion | No | Optional queue/worker for large docs |

---

# What Not to Say

Do not say:

- “All uploaded PDFs are stored permanently.”
- “S3 currently stores my source PDFs for RAG.”
- “The same PDF can always be queried later without re-upload.”
- “Redis stores the PDF vector index.”
- “MongoDB stores Qdrant embeddings.”
- “Qdrant itself is the RAG system.”
- “Qdrant generates the answer.”
- “We support OCR.”
- “We use reranking.”
- “We use hybrid search.”
- “We provide reliable page citations.”
- “We have automatic Qdrant collection cleanup.”
- “Physical vector persistence means the document feature is persistent.”
- “RAG prevents hallucination.”
- “Top five always contains the correct answer.”
- “Our exact Qdrant metric is cosine” unless verified.
- “Our exact embedding vector dimension is X” unless verified.

---

# Final Self-Test

Before Module 10, explain without notes:

- current upload path
- Multer / temporary file
- `pdf-parse`
- OCR limitation
- 1000/200 chunking
- Gemini embeddings
- Qdrant collection creation
- question embedding
- top-five retrieval
- context construction
- Groq generation
- Chat/MongoDB persistence
- Redis context role
- temp PDF cleanup
- why later follow-up is limited
- physical persistence vs application lifecycle
- orphaned collections
- collection cleanup problem
- `documentId`
- owner mapping
- collection/index mapping
- persistent source storage
- metadata filtering
- page/chunk metadata
- async indexing
- versioning
- deletion/retention
- reconciliation
- failure handling
- safe retry/idempotency
- tenant isolation
- RAG evaluation
- V2 priority order

**Module 09 interview preparation complete.**
