# Module 13 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Files, S3, Presigned URLs and Artifact Lifecycle  
> **Purpose:** Prepare for deep file/artifact, S3, security, lifecycle, failure, troubleshooting and design-defense questions.

---

## Accuracy Rules

### Confident current claims

```text
PDF generation uses Groq-backed structured content + PDFKit.
PPT generation uses Groq-backed structured content + PptxGenJS.
Current PPT pattern is cover + 6 content slides + closing.
Image generation uses Groq-backed prompt preparation + Stability AI.
Generated PDF/PPT/image artifacts are uploaded to S3.
NovaMind returns presigned URLs for temporary access.
Code generation returns structured files[] and is displayed in Monaco/basic browser preview.
Temporary uploaded files are used in PDF/image processing.
S3 object lifetime is separate from presigned URL lifetime.
Old presigned links can expire while the object still exists.
```

### Current limitations

```text
no mature artifactId → owner → objectKey model
no mature presigned-URL renewal flow
no mature artifact retention policy
no mature coordinated deletion
no mature automatic orphan reconciliation
bucket versioning/lifecycle/encryption not fully verified
full tenant-isolated artifact access is not verified
```

### Do not claim

```text
all artifacts are public
presigned URL expiration deletes S3 object
all code artifacts are stored in S3
S3 versioning is enabled
specific S3 encryption mode is verified
mature artifact ownership
mature lifecycle rules
production readiness
```

---

# Artifact Fundamentals

## Q1. What is an artifact?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> An artifact is an application output such as a generated PDF, PPT, image or structured code files that can be stored, displayed or downloaded.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q2. What is the difference between an uploaded file and a generated artifact?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> An uploaded file comes from the user into the application; a generated artifact is created by the application for the user.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q3. What artifact types does NovaMind generate?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> PDF, PPTX, generated images and structured code artifacts.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q4. Are all artifacts stored in S3 in the same way?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No. PDF/PPT/image flows use S3 delivery, while code artifacts are handled as structured code files for Monaco/browser preview.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q5. What is the most important lifecycle distinction?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> An S3 object is not the same thing as a presigned URL.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# PDF Generation

## Q6. How does NovaMind generate a PDF?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> A Groq-backed model generates structured content, PDFKit renders the actual PDF, the backend uploads it to S3 and returns a presigned URL.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q7. Does Groq create the final PDF binary?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No. It generates content; PDFKit renders the PDF.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q8. What does PDFKit do?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> It creates the actual PDF file/binary.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q9. What happens after rendering?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The PDF is uploaded to S3.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q10. How does the user access it?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Through a presigned URL.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# PPT Generation

## Q11. How is PPT generated?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Groq-backed structured content is rendered with PptxGenJS, uploaded to S3 and delivered through a presigned URL.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q12. What library renders PPTX?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> PptxGenJS.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q13. What verified slide pattern exists?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Cover plus six content slides plus closing, for eight slides total.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q14. Does the LLM directly create the .pptx binary?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q15. Why separate content generation and rendering?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The model creates structured content while deterministic library code creates a valid file format.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Image Generation

## Q16. How does generated-image delivery work?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> NovaMind prepares/expands the prompt, Stability AI generates the image bytes, the backend uploads the image to S3 and returns a presigned URL.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q17. Which provider generates the image?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Stability AI.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q18. What is the configured endpoint/model family?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> `stable-image/generate/core`.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q19. What exists before S3 upload?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Image bytes/buffer in application memory.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q20. Is an in-memory image buffer durable?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q21. What if Stability succeeds but S3 fails?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The external generation succeeded but user delivery failed, creating partial success.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Code Artifacts

## Q22. How is code artifact generation different?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> DeepSeek returns structured `files[]`, the backend parses them, and the frontend shows them in Monaco Editor.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q23. Which access platform/model path is used?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> OpenRouter with DeepSeek.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q24. Is code output necessarily uploaded to S3?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The verified coding path is a structured code artifact rather than the same S3 binary-artifact flow.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q25. Can NovaMind run arbitrary generated server code?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q26. Does it install packages and compile a full project?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q27. What preview exists?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> A basic browser iframe preview for compatible HTML/CSS/JS.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# S3 Fundamentals

## Q28. What is S3?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Amazon S3 is object storage.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q29. What is an S3 bucket?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> A container for S3 objects.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q30. What is an S3 object?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Stored bytes addressed by an object key, plus metadata.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q31. What is an object key?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The object's path-like identifier inside the bucket.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q32. Is S3 a normal filesystem?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No; slash-separated paths are key naming conventions.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q33. What operation uploads an object?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Conceptually `PutObject`.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q34. Does NovaMind use S3 for generated artifacts?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes, for generated PDF/PPT/image delivery.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Presigned URLs

## Q35. What is a presigned URL?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> A temporary signed URL that grants a specific S3 operation without making the object public.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q36. Why use it?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> To provide temporary access to a private object.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q37. What operation is commonly signed for artifact delivery?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> GetObject-style access.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q38. What happens when the URL expires?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The URL stops granting access.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q39. Does URL expiry delete the object?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q40. Can an object be deleted while an old URL string still exists?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes; the URL will then fail to retrieve the object.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q41. Is the presigned URL the artifact's durable identity?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> It should not be; it is temporary access.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Object vs URL Lifecycle

## Q42. What is object lifetime?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> How long the S3 object exists.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q43. What is URL lifetime?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> How long a presigned URL remains valid.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q44. Why are they independent?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The object may remain after one or many signed URLs expire.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q45. What current limitation follows from storing URLs in answers?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Old conversation messages can contain expired links even while the underlying S3 object still exists.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q46. Does NovaMind have a mature URL renewal path?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q47. What would renewal require?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Stable artifact metadata, ownership authorization and the S3 object key.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Artifact Metadata

## Q48. What metadata would a mature artifact record contain?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Artifact ID, user ID, conversation ID, object key, type, content type, status, created time and retention information.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q49. Is that mature dedicated artifact model verified today?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q50. Why create artifactId?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> To reference the artifact independently of temporary URLs.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q51. Why store objectKey?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> So the backend can find the S3 object and create a new signed URL.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q52. Why store owner/userId?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> To enforce resource-level authorization.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q53. Why store conversationId?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> To associate the artifact with the conversation that produced it.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Ownership and Access Control

## Q54. Why must artifact access be authorized?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Artifacts can contain private user content.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q55. Is a presigned URL effectively bearer access?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes; someone who obtains a valid URL may use it until expiry.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q56. Should the browser choose an arbitrary S3 key to sign?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q57. What is the safer pattern?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Client sends artifactId, server loads metadata, verifies ownership and chooses the object key.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q58. Is complete artifact tenant isolation verified?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q59. What happens if User A obtains User B's valid presigned URL?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The URL itself can grant access until it expires, which is why URL handling and short appropriate expiry matter.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Private vs Public S3

## Q60. Should private user artifacts normally be public S3 objects?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q61. Why prefer private objects plus presigned URLs?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> It limits access to temporary authorized links.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q62. Does NovaMind code prove every bucket policy is perfectly hardened?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q63. Can you claim versioning/lifecycle/encryption are enabled?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Not without verifying the actual bucket configuration.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q64. Why not solve AccessDenied by making the bucket public?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> That would weaken security rather than fixing IAM/access design.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Retention and Lifecycle

## Q65. What is retention?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> How long an artifact remains stored.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q66. Is a mature artifact retention policy verified?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q67. Why is retention important?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Privacy, compliance, user expectations and cost.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q68. What is an S3 lifecycle rule?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> An S3 feature that can expire or transition objects automatically.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q69. Is artifact-specific lifecycle automation verified today?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q70. What should determine retention?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Product requirements, sensitivity and cost.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Deletion

## Q71. What should happen when a user deletes a conversation?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> A mature design should decide whether linked artifacts are also deleted or retained according to policy.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q72. Is coordinated cross-store deletion mature today?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q73. What is an orphaned artifact?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> An S3 object that remains without useful application metadata/ownership linkage.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q74. Why are orphaned artifacts bad?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> They create storage cost, privacy risk and cleanup complexity.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q75. Can deleting MongoDB metadata automatically delete S3?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No, not without explicit application/lifecycle logic.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Versioning and Encryption

## Q76. What is S3 versioning?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Retention of multiple versions of an object key.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q77. Is versioning verified as current?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q78. What are versioning trade-offs?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Recovery benefits versus more storage/cleanup complexity.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q79. What is encryption at rest?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Protecting stored object bytes using server-side encryption or related mechanisms.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q80. Can you state the exact current S3 encryption mode?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Not from the verified project summary.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q81. What protects data in transit?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> HTTPS/TLS.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# IAM and S3 Permissions

## Q82. Which IAM role is relevant to application S3 API calls?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The ECS task role used by application code.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q83. What is least privilege for S3?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Grant only required actions on required bucket/prefix resources.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q84. Should the Agent service have `s3:*`?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No, not by default.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q85. Does a role name prove least privilege?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q86. Were all effective IAM permissions live-inspected?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q87. What does an S3 AccessDenied usually suggest?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Incorrect IAM, bucket policy, key/prefix, account, region or related permissions/configuration.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Temporary Files

## Q88. What is the role of temporary local files?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> They support request-time processing such as uploaded PDF/image handling.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q89. Are temp files durable?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q90. What happens on container replacement?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Local temporary data can disappear.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q91. Why clean temp files?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> To prevent disk growth and reduce retention of sensitive data.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q92. Can cleanup itself fail?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q93. How should cleanup failure be treated?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> As an operational/security failure even if the AI response succeeded.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Partial Failure

## Q94. What if PDF rendering succeeds but S3 upload fails?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Artifact creation succeeded but durable delivery failed.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q95. What if S3 upload succeeds but presigning fails?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The object exists but the user cannot access it through the expected link.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q96. What if presigning succeeds but response serialization fails?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The URL may exist but never reach the client.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q97. What if the user gets the URL but Chat persistence fails?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The artifact may be accessible even though conversation history is incomplete.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q98. What if the URL expires later?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The object may remain but the stored link becomes stale.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q99. Why are these called partial failures?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Some stages succeeded and produced side effects while later stages failed.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Retry and Idempotency

## Q100. Why not rerun the whole artifact generation after an S3 upload failure?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> It may regenerate different content and incur more model/provider cost.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q101. What is a better retry strategy?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Retry the failed stage if the generated binary/object identity is still available and safe to reuse.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q102. How can stable artifact IDs help retries?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> They can map retries to the same logical artifact and avoid uncontrolled duplicates.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q103. Is idempotent artifact generation mature today?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Content Type and File Size

## Q104. Why set Content-Type?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> So browsers/clients know how to handle the object.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q105. What MIME type does PDF use conceptually?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> `application/pdf`.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q106. Why do large artifacts matter?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> They increase memory, upload/download time and storage/network cost.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q107. What is a buffer-memory risk?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Holding a large file entirely in memory can increase container memory pressure.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q108. Could streaming help?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes for large outputs, but it is a general improvement rather than verified current behavior.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Artifact Status and Async Design

## Q109. Is current artifact generation mostly synchronous?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q110. What statuses could a V2 artifact record use?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> REQUESTED, GENERATING, UPLOADING, READY, FAILED, DELETED.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q111. Are those current?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q112. Why use statuses?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> For progress, retry, recovery and debugging.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q113. When would async generation help?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> For large/slow jobs that should not keep one HTTP request open.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q114. Is an async worker/queue current?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Production V2 Artifact Model

## Q115. What is the first V2 artifact improvement?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Create a stable artifactId.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q116. What should artifact metadata map?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Artifact ID to owner, conversation, S3 key, type, status and retention.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q117. What should object visibility be?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Private by default for user-specific generated artifacts.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q118. How should later access work?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Authenticate, authorize artifact ownership, load objectKey, then generate a fresh presigned URL.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q119. Why not store the presigned URL as the permanent identifier?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> It expires.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q120. What should happen after retention ends?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Delete/expire object and update metadata according to policy.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q121. What is artifact reconciliation?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Detecting metadata/object mismatches such as object-without-record or record-without-object.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Security

## Q122. What is the biggest access-control rule for artifacts?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Never let client-selected object keys bypass server-side ownership checks.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q123. Should logs contain full presigned URLs?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Avoid unnecessary logging because valid URLs can grant temporary access.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q124. Should generated artifacts be treated as private data?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes, they can contain user content.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q125. What is the risk of very long presigned expiry?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> A leaked URL remains usable longer.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q126. What is the risk of very short expiry?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Links become unusable before users expect, so renewal is needed.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q127. How does least privilege reduce artifact risk?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> A compromised service can access only necessary bucket/prefix operations.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Observability

## Q128. What metrics would you track?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Generation time, artifact size, upload latency, presign failures, access failures, deletion failures, stale-link renewals and orphan count.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q129. What logs are useful?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Artifact ID, request ID, object key hash/reference, stage and error without leaking secrets/URLs unnecessarily.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q130. Why correlation IDs?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> To trace one artifact from Agent through rendering/provider, S3 and persistence.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q131. Is mature distributed tracing current?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Troubleshooting

## Q132. User says PDF was not generated. Where do you start?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Trace model content generation, structured parsing, PDFKit rendering, S3 upload, presigning and response.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q133. User gets AccessDenied. What do you check?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Object existence/key, S3 IAM task role, bucket policy, region/client configuration and URL validity.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q134. User gets an expired-link error. What is the likely cause?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The presigned URL lifetime ended even though the object may still exist.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q135. What is the mature fix for expired links?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Authorize the user and generate a fresh presigned URL using stored artifact metadata/object key.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q136. User gets NoSuchKey. What do you check?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Whether upload succeeded, key is correct, or object was deleted/expired.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q137. Image provider succeeded but image not visible. What do you trace?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Stability result, buffer handling, S3 upload, presign, response field and frontend rendering.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q138. PPT is generated but cannot open. What do you inspect?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Structured content parsing, PptxGenJS rendering, file integrity/content type and upload.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Cost and Scaling

## Q139. What costs exist in artifact delivery?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Generation provider/model cost, S3 storage, requests and data transfer.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q140. How does retention affect cost?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Longer retention increases stored bytes and potentially versions.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q141. Can ECS scaling fix expired URLs?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q142. Can more S3 storage fix missing ownership?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q143. What is the memory issue with large buffers?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Per-task memory pressure can increase and cause instability.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q144. What is a possible scaling improvement for large jobs?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Async generation and direct/streamed storage, if justified.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Design Defense

## Q145. Why use S3 instead of returning huge binary files directly?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> S3 provides durable object storage and decouples file delivery from the application response.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q146. Why use presigned URLs instead of making the bucket public?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> They provide time-limited access while keeping objects private.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q147. Why separate LLM generation and PDF/PPT rendering?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The LLM produces content, while deterministic libraries produce valid file formats.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q148. Why isn't URL expiry enough for retention?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The object remains after the URL expires.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q149. Why isn't S3 object existence enough for later access?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The application needs durable ownership/object metadata and an authorization/re-sign flow.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q150. Why not store only the object key in the browser?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> The server should keep authoritative ownership mapping and choose keys after authorization.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q151. What is the biggest current artifact-lifecycle gap?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No mature artifact identity/ownership/object-key/renewal/retention lifecycle.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Pressure Questions

## Q152. If the presigned URL expires, is the file gone?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No. URL lifetime and object lifetime are separate.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q153. If S3 is private, can anyone with the presigned URL still download?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Yes, while the URL is valid for the signed action.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q154. Why not use a one-year presigned URL?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> It weakens access control if the URL leaks; better to use shorter access plus authorized renewal.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q155. Why not make every generated file public?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Artifacts can contain private user content.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q156. If the object already exists, why can't you simply re-sign it?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> You need a durable object key and ownership mapping to know which object belongs to which authorized user.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q157. Why not regenerate instead of renewing?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Regeneration can change content and incur provider/model cost; the original object should be reusable if still retained.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q158. Is S3 your artifact database?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> S3 stores object bytes; application metadata/ownership still needs a database model.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q159. Is code generation the same artifact lifecycle as PDF?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No. Current code artifacts are structured files shown in Monaco rather than the same S3 binary-download flow.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q160. Can you claim S3 versioning is enabled?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No, not without verifying live bucket configuration.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q161. Can you claim server-side encryption mode?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> Not from the verified project facts.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

## Q162. Is artifact access fully production-ready?

**What the interviewer is testing:** Whether you understand the difference between file generation, durable object storage, temporary access URLs, ownership, retention and failure recovery.

**Word-for-word answer:**

> No. The current generation/storage flow is real, but ownership, renewal, retention and coordinated deletion need hardening.

**Likely follow-up:** Be ready to explain **where the bytes live, how the user gets access, what happens when the URL expires, what can fail, and how Production V2 would manage ownership and lifecycle**.

**Defense reminder:** A presigned URL is temporary access, not the artifact's durable identity.

---

# Rapid-Fire Revision

**Q163. PDF renderer?**  
PDFKit.

**Q164. PPT renderer?**  
PptxGenJS.

**Q165. PPT pattern?**  
Cover + 6 content + closing.

**Q166. Image provider?**  
Stability AI.

**Q167. Generated binary storage?**  
S3.

**Q168. Temporary access?**  
Presigned URL.

**Q169. URL expiry deletes object?**  
No.

**Q170. S3 object = URL?**  
No.

**Q171. Code artifact?**  
Structured files[] shown in Monaco/basic preview.

**Q172. All code artifacts S3?**  
No verified same flow.

**Q173. ArtifactId model mature?**  
No.

**Q174. URL renewal mature?**  
No.

**Q175. Retention policy mature?**  
No.

**Q176. Coordinated deletion mature?**  
No.

**Q177. Versioning verified?**  
No.

**Q178. Encryption mode verified?**  
No.

**Q179. Bucket policy fully verified?**  
No.

**Q180. Temporary upload durable?**  
No.

**Q181. PutObject role?**  
Store generated object.

**Q182. GetObject presign role?**  
Temporary retrieval access.

**Q183. Private artifact recommended?**  
Yes.

**Q184. Production-ready lifecycle?**  
No.

# Cross-Question Chain 1 — PDF Artifact

**Interviewer:** How do you generate PDFs?

> NovaMind uses a Groq-backed model to create structured content, PDFKit renders the actual PDF binary, the backend uploads it to S3, and the user receives a presigned URL for temporary access.

**Interviewer:** Does the LLM directly create the PDF?

> No. The model generates the content; PDFKit creates the file format.

---

# Cross-Question Chain 2 — Presigned URL

**Interviewer:** What happens when the URL expires?

> The URL stops granting access, but the S3 object may still exist.

**Interviewer:** Can you create a new URL?

> Architecturally yes if the application still knows the object key and can authorize the user, but a mature artifact identity and renewal flow is not implemented in the current project.

---

# Cross-Question Chain 3 — S3 Security

**Interviewer:** Why not make the bucket public?

> Generated artifacts can contain private user data. Private objects with short-lived presigned access are safer than public objects.

**Interviewer:** Can a leaked presigned URL be used?

> Yes, while it remains valid for the signed action, which is why expiry and careful handling matter.

---

# Cross-Question Chain 4 — Partial Failure

**Interviewer:** PDFKit succeeds but S3 fails. What state are you in?

> The artifact was created in the application process, but durable storage/delivery failed. I would retry the failed upload stage where safe instead of blindly regenerating the content.

---

# Cross-Question Chain 5 — Code Artifact

**Interviewer:** Is code generation stored the same way as PDFs?

> No. The verified coding flow receives structured `files[]`, parses them into a code artifact, and displays them in Monaco with a basic browser preview. It is not the same binary-S3 artifact flow.

---

# Cross-Question Chain 6 — Production V2

**Interviewer:** How would you fix expired links?

> I would create a durable artifact record containing artifact ID, owner, conversation, S3 object key, type, status and retention. When a user requests access later, the backend verifies ownership and generates a fresh presigned URL.

---

# 30-Second Interview Answer

> NovaMind uses S3 for generated PDF, PPT and image artifacts. The LLM generates structured content, PDFKit or PptxGenJS renders document files, and Stability AI generates image bytes. The backend uploads the result to S3 and returns a presigned URL. A key point is that an S3 object and a presigned URL have separate lifetimes: the URL can expire while the object still exists. The current gap is that NovaMind does not yet have a mature artifact identity, ownership, retention and URL-renewal lifecycle.

---

# 60–90 Second Interview Answer

> NovaMind has different artifact flows. PDF generation uses a Groq-backed content step followed by PDFKit, and PPT generation uses PptxGenJS. Image generation uses Stability AI after prompt preparation. These generated PDF, PPT and image binaries are uploaded to S3 and delivered through presigned URLs.
>
> The important design distinction is that S3 stores the actual object, while the presigned URL only grants temporary access. When that URL expires, the object can still remain in S3. Today, the project can return/store those URLs in conversation responses, but it does not have a mature durable artifact model mapping an artifact ID to owner, conversation and object key, so reliable later URL renewal is limited.
>
> Code artifacts are handled differently: DeepSeek returns structured files, which are shown in Monaco Editor and basic browser preview rather than following the same S3 binary-artifact path.
>
> For Production V2, I would store private S3 objects plus durable artifact metadata, verify ownership before every access, generate fresh presigned URLs on demand, define retention/deletion rules and reconcile orphaned objects or metadata.

---

# 2–3 Minute Project Defense

> NovaMind separates AI content generation from artifact rendering and storage. For PDF generation, a Groq-backed model creates structured content and PDFKit renders the actual PDF. For PowerPoint, structured content is converted into a `.pptx` by PptxGenJS, using the current cover plus six content slides plus closing pattern. For image generation, NovaMind prepares the prompt, calls Stability AI, receives image bytes and uploads those bytes to S3.
>
> S3 is the durable object store for those generated PDF, PPT and image outputs. After upload, NovaMind generates a presigned URL so the frontend can access the private object temporarily. I make a clear distinction between the S3 object and the presigned URL. The URL has an expiration time, but expiration does not delete the object.
>
> That distinction exposes the main lifecycle gap. The current implementation can store or return a presigned URL in the conversation response, but if the user opens the conversation later the URL may be expired even though the S3 object still exists. The project does not yet have a mature dedicated artifact record like `artifactId → userId → conversationId → objectKey → retention`, so there is no strong verified access-renewal lifecycle.
>
> Code generation is different. DeepSeek returns structured `files[]`, the backend parses them into an artifact, and the frontend shows them in Monaco with a basic browser preview. I do not describe that as the same S3 binary-file lifecycle.
>
> For Production V2, I would create the artifact record before or during generation, store generated objects privately in S3, persist owner and object-key metadata, and expose an authorized endpoint that returns a fresh presigned URL only after verifying ownership. I would also define retention, deletion and orphan reconciliation. For large jobs I would consider asynchronous generation, but only if the latency/size requirements justify it.

---

# Current vs Production V2

| Area | Current NovaMind | Production V2 Proposal |
|---|---|---|
| PDF | Groq content → PDFKit | Keep, harden validation/status |
| PPT | Groq content → PptxGenJS | Keep, version templates |
| Image | Stability AI → bytes | Keep, status/retry |
| Binary storage | S3 | Private S3 + lifecycle policy |
| Access | Presigned URL | Authorized fresh re-sign endpoint |
| Durable artifact ID | Not mature | Stable `artifactId` |
| Ownership metadata | Not mature | `userId`, `conversationId` |
| Object mapping | URL-centric/current flow | Durable `objectKey` |
| Retention | Not mature | Explicit retention + lifecycle rules |
| Deletion | Not coordinated | Metadata + S3 coordinated delete |
| Orphan cleanup | Not mature | Reconciliation job |
| Async jobs | Not current | Optional for slow/large artifacts |

---

# What Not to Say

Do not say:

- “Presigned URL expiry deletes the file.”
- “The presigned URL is the S3 object.”
- “All generated files are public.”
- “All code artifacts are uploaded to S3.”
- “S3 versioning is definitely enabled.”
- “I know the exact bucket encryption configuration.”
- “Artifact ownership and renewal are fully implemented.”
- “Conversation deletion automatically deletes every S3 artifact.”
- “Our artifact lifecycle is production-ready.”

---

# Final Self-Test

Before Module 14, explain without notes:

- uploaded file vs generated artifact
- PDF flow
- PPT flow
- image-generation flow
- code-artifact flow
- PDFKit
- PptxGenJS
- Stability AI
- S3 object
- bucket
- object key
- PutObject
- presigned URL
- GetObject access
- URL expiry
- object lifetime
- temporary files
- cleanup
- ownership
- bearer-link risk
- retention
- lifecycle rules
- deletion
- orphaned objects
- versioning concept
- encryption concept
- IAM task role
- least privilege
- partial failure
- retries
- content type
- buffer/memory risk
- artifact status
- artifactId
- URL renewal
- reconciliation
- observability
- Production V2 artifact model

**Module 13 interview preparation complete.**
