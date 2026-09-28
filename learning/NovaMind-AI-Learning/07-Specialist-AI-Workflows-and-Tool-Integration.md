# Module 07 — Specialist AI Workflows and Tool Integration

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Purpose:** Understand exactly how NovaMind's eight specialist workflows execute, which models/tools each one uses, how LangGraph state moves through them, how they interact with Chat/Auth/S3/Qdrant/MongoDB/Redis, what can fail, and how to defend the design in interviews.  
> **Accuracy rule:** The eight specialists are predefined workflows inside the Agent service. They are not eight ECS microservices and they are not independently autonomous agents.

---

## Module 07 Visual Architecture

![NovaMind AI — Specialist AI Workflows and Tool Integration](images\07-specialist-ai-workflows-tool-integration.png)

> Place the image at: `learning/images/07-specialist-ai-workflows-tool-integration.png`

---

# Module 07 Mental Model

The core execution pattern is:

```text
Router
  ↓
Select Specialist
  ↓
Specialist reads LangGraph state
  ↓
Use task-specific model / tool / data store
  ↓
Parse / process result
  ↓
Update state
  ↓
Persist message or artifact where needed
  ↓
Return response
```

The eight verified specialists are:

```text
1. Chat
2. Search
3. Coding
4. PDF RAG
5. PDF Generation
6. PPT Generation
7. Image Generation
8. Image Analysis
```

---

# Concept 1 — What Is a Specialist Workflow?

A specialist workflow is a task-focused execution path.

Instead of one giant general-purpose function handling every request, NovaMind separates capabilities.

Example:

```text
Search Question
 ↓
Search Specialist
 ↓
Tavily
 ↓
Groq-backed synthesis
```

A specialist can have its own:

- prompt
- provider/model
- tools
- parsing logic
- artifact logic
- cost behavior
- failure behavior

---

# Concept 2 — Why Use Specialists?

Specialists improve separation of concerns.

Benefits:

- clearer prompts
- task-specific providers
- task-specific tools
- easier debugging
- narrower permissions
- easier testing

Trade-offs:

- more routing complexity
- more code paths
- more provider dependencies
- more different failure modes

---

# Concept 3 — Specialist Workflow vs Microservice

A specialist is not automatically a microservice.

In NovaMind:

```text
Agent Service
 ├── Chat
 ├── Search
 ├── Coding
 ├── PDF RAG
 ├── PDF Generation
 ├── PPT Generation
 ├── Image Generation
 └── Image Analysis
```

These live inside one Agent service.

Therefore:

```text
8 specialists
≠
8 ECS services
```

---

# Concept 4 — Common Specialist Lifecycle

A common pattern is:

```text
Read state
 ↓
Validate needed inputs
 ↓
Call tool/model
 ↓
Parse provider result
 ↓
Update state
 ↓
Persist if needed
 ↓
Return
```

Each specialist changes this pattern based on its task.

---

# Concept 5 — Specialist Inputs

Typical state inputs include:

- prompt
- userId
- conversationId
- selected workflow
- file
- previous context
- search results

Not every specialist needs every field.

---

# Concept 6 — Specialist Outputs

Possible outputs include:

```text
response
searchResults
images
artifacts
```

Examples:

- Chat → response
- Search → searchResults + response
- Coding → artifacts
- Image Generation → images/artifact
- PDF/PPT → artifact URL

---

# Concept 7 — Chat Workflow

Simplified flow:

```text
Prompt
 ↓
Relevant conversation context
 ↓
Groq-backed LLM
 ↓
Text response
 ↓
State update
 ↓
Persist assistant message
```

The configured Groq model ID is:

`openai/gpt-oss-120b`

Important:

The `openai/` prefix does not mean the OpenAI API is being used.

The verified provider/client is Groq.

---

# Concept 8 — Chat Memory Behavior

Chat explicitly loads conversation context.

That makes Chat the most memory-aware specialist.

However, the current memory implementation has limitations:

- potentially large history hydration
- duplicate current message behavior
- no mature token-aware summarization
- race/TTL issues

So Chat has useful memory behavior, but not a mature long-term memory architecture.

---

# Concept 9 — Chat Failure Cases

Possible failures:

- Groq timeout
- provider rate limit
- conversation context load failure
- Chat persistence failure
- credit handling failure

Example partial success:

```text
Groq succeeds
 ↓
assistant response exists
 ↓
Chat save fails
```

---

# Concept 10 — Search Workflow

Search is a chained workflow.

```text
User question
 ↓
Search Specialist
 ↓
Tavily
 ↓
Web results + images
 ↓
Groq-backed synthesis
 ↓
Text answer
```

Tavily performs retrieval.

The LLM performs synthesis.

---

# Concept 11 — Tavily's Role

Tavily is a web-search tool.

It is not an LLM.

The verified configuration retrieves up to about five results and can request images.

So:

```text
Tavily
= web retrieval

Groq
= language synthesis
```

---

# Concept 12 — Search-to-Chat Chain

The Search workflow passes retrieved results into a Chat-style language-generation step.

This is an example of a bounded handoff/chained workflow.

It does not mean autonomous agents are freely collaborating.

---

# Concept 13 — Search Cost

Search can be more expensive than normal Chat because it involves multiple operations.

Conceptually:

```text
Search retrieval
+
LLM synthesis
+
application credit operations
```

The verified flow can involve a 5-credit Search request plus a 1-credit Chat request, making a successful Search-to-Chat request effectively request 6 credits.

Application credits are not the same as real provider-dollar cost.

---

# Concept 14 — Search Limitations

Do not claim:

- verified citation alignment
- guaranteed fact checking
- guaranteed source correctness

The current project does not have a mature source/citation verification layer.

Search result text must also be treated as untrusted content.

---

# Concept 15 — Coding Workflow

Flow:

```text
Coding Prompt
 ↓
Coding Intent Classification
 ↓
OpenRouter
 ↓
DeepSeek
 ↓
Structured files[]
 ↓
Parse
 ↓
Code Artifact
 ↓
Frontend Monaco / Preview
```

---

# Concept 16 — Coding Intent Classification

The main Router decides:

> Is this a Coding request?

Then the Coding workflow can perform additional intent classification such as:

- generate
- explain
- review

This is different from the main LangGraph router.

---

# Concept 17 — OpenRouter vs DeepSeek

```text
OpenRouter
= model-access layer

DeepSeek
= coding model
```

Configured model:

`deepseek/deepseek-chat`

The verified coding configuration uses:

- temperature 0
- approximately 2500 max output tokens

---

# Concept 18 — Coding Structured Output

The Coding workflow expects machine-readable file structure.

Conceptually:

```json
{
  "files": [
    {
      "name": "index.html",
      "content": "..."
    }
  ]
}
```

This allows the frontend to render files individually.

---

# Concept 19 — Why Coding Parsing Can Fail

Possible problems:

- invalid JSON
- Markdown fences
- unexpected explanation text
- missing `files`
- broken escaping
- truncated output

Prompting for JSON is not a guarantee.

Production V2 should use stronger schema validation.

---

# Concept 20 — Coding Is Not Autonomous Software Engineering

The current Coding workflow does not provide:

- secure arbitrary backend execution
- dependency installation
- full compile/test runner
- autonomous debug/repair loop
- long-running coding planner

Accurate wording:

> structured code generation and browser-side preview for compatible frontend output.

---

# Concept 21 — PDF RAG Workflow

Flow:

```text
PDF upload
 ↓
Temporary file
 ↓
pdf-parse
 ↓
Text
 ↓
Chunking
 ↓
Gemini embeddings
 ↓
Qdrant
 ↓
Question embedding
 ↓
Top-5 similarity search
 ↓
Groq-backed answer generation
```

---

# Concept 22 — PDF Extraction

`pdf-parse` extracts text from text-based PDFs.

There is no verified OCR path for scanned/image-only PDFs.

So scanned PDFs are a known limitation.

---

# Concept 23 — PDF Chunking

Verified chunking:

```text
chunk size ≈ 1000 characters
overlap ≈ 200 characters
```

Overlap helps preserve context across boundaries.

---

# Concept 24 — PDF Embeddings

The embedding model is:

`gemini-embedding-001`

Embeddings convert chunks into vectors.

These vectors are used for semantic retrieval.

---

# Concept 25 — Qdrant Retrieval

Qdrant stores vector representations and returns similar chunks.

Verified retrieval:

```text
top 5 chunks
```

Qdrant does not generate the final answer.

---

# Concept 26 — RAG Generation

Retrieved chunks are added to the prompt.

Then the Groq-backed LLM generates the answer.

So:

```text
Gemini
→ embeddings

Qdrant
→ retrieval

Groq
→ answer generation
```

---

# Concept 27 — PDF RAG Limitations

Current limitations include:

- no OCR
- character-based chunking
- no mature page citations
- no reranking
- no mature retrieval threshold
- no durable user-document-index mapping
- no mature index cleanup
- no systematic RAG evaluation

---

# Concept 28 — Why Qdrant Failure Must Not Silently Become Chat

If Qdrant fails:

```text
PDF grounding unavailable
```

Falling back silently to normal Chat would create:

```text
Ungrounded answer
```

while the user may think it came from the PDF.

This is a semantic correctness problem.

---

# Concept 29 — PDF Generation Workflow

Flow:

```text
Prompt
 ↓
LLM structured content
 ↓
PDFKit
 ↓
PDF file
 ↓
S3
 ↓
Presigned URL
```

Important:

```text
PDF Generation
≠
PDF RAG
```

---

# Concept 30 — PDFKit's Role

PDFKit is a renderer.

The LLM creates content.

PDFKit creates the actual `.pdf` binary.

So:

```text
LLM
= content

PDFKit
= file rendering
```

---

# Concept 31 — PPT Generation Workflow

Flow:

```text
Prompt
 ↓
LLM structured slide content
 ↓
PptxGenJS
 ↓
PPTX file
 ↓
S3
 ↓
Presigned URL
```

The current prompt pattern targets:

- cover
- six content slides
- closing

approximately eight slides total.

---

# Concept 32 — PptxGenJS's Role

PptxGenJS creates the actual PowerPoint file.

The LLM does not directly produce a valid binary PPTX.

---

# Concept 33 — Structured Content Failure in Document Generation

If the LLM returns malformed structured data:

```text
Renderer receives bad content
 ↓
Render can fail
```

Production V2 should use:

- schema validation
- structured-output APIs where available
- repair/retry
- clear parse error semantics

---

# Concept 34 — Image Generation Workflow

Flow:

```text
Text prompt
 ↓
Prompt preparation/expansion
 ↓
Stability AI
 ↓
Image bytes
 ↓
S3
 ↓
Presigned URL
```

Verified provider:

Stability AI

Verified endpoint family:

`stable-image/generate/core`

---

# Concept 35 — Image Analysis Workflow

Flow:

```text
Uploaded image
+
Question
 ↓
Prepare image
 ↓
Gemini multimodal
 ↓
Text analysis
 ↓
Temporary file cleanup
```

Verified model:

`gemini-2.0-flash`

---

# Concept 36 — Image Generation vs Image Analysis

```text
Image Generation
text → image

Image Analysis
image → text
```

They use different providers and different execution paths.

---

# Concept 37 — Temporary File Handling

Uploaded PDF/image processing uses temporary local file handling.

A temporary upload should be removed after processing.

Failure paths can complicate cleanup.

Therefore:

```text
try
 ↓
process
 ↓
finally
 ↓
cleanup
```

is an important design idea.

---

# Concept 38 — Generated Artifact Handling

Generated:

- PDFs
- PPTs
- images

are uploaded to S3.

The backend can generate a presigned URL for user access.

The S3 object is the file.

The presigned URL is only temporary access.

---

# Concept 39 — Presigned URL Expiration

When a presigned URL expires:

```text
URL stops working
```

but:

```text
S3 object may still exist
```

So URL expiration is not object deletion.

---

# Concept 40 — Code Artifacts Are Different

Coding artifacts are structured source files.

They are not handled exactly like generated PDF/PPT/image S3 artifacts.

The frontend displays them in Monaco and may preview compatible browser code.

Do not generalize every artifact into one storage path.

---

# Concept 41 — Agent → Chat Service

The Agent service uses Chat for conversation/message persistence.

Conceptually:

```text
Agent
 ↓
Chat
 ↓
MongoDB
```

This preserves a Chat persistence boundary.

Trade-off:

- synchronous dependency
- extra network call
- partial-failure risk

---

# Concept 42 — Agent → Auth Service

Agent can call Auth for credit deduction/account-related operations.

This means AI execution is coupled to account state.

A provider can succeed while credit/account logic fails or vice versa.

That needs careful error semantics.

---

# Concept 43 — Credit Enforcement Weakness

The review found that Agent credit helper failures can allow provider work to continue in some paths.

That means:

```text
credit operation fails
 ↓
provider work may still occur
```

This is a correctness/cost-control weakness.

---

# Concept 44 — Specialist State Updates

Specialists update task-specific fields.

Examples:

```text
Chat
→ response

Search
→ searchResults + response

Coding
→ artifacts

Image Generation
→ images / artifact

PDF/PPT
→ artifact + response
```

State should contain only what later graph/application logic needs.

---

# Concept 45 — Specialist Memory Differences

Do not claim all specialists use the same conversation memory.

Chat explicitly uses conversation context.

Other specialists are more request-focused.

That means memory behavior is inconsistent across workflows.

---

# Concept 46 — Provider Failure Isolation

Each workflow depends on different providers.

```text
Chat → Groq
Search → Tavily + Groq
Coding → OpenRouter/DeepSeek
PDF RAG → Gemini + Qdrant + Groq
Image Gen → Stability
Image Analysis → Gemini
```

A failure in one provider should ideally affect only the workflows depending on it.

However, shared Agent service availability still affects all specialists.

---

# Concept 47 — Partial Success

Examples:

```text
Tavily succeeds
Groq fails
```

```text
LLM generates PDF content
PDFKit succeeds
S3 upload fails
```

```text
Stability generates image
S3 upload fails
```

```text
LLM responds
Chat persistence fails
```

These are multi-step consistency problems.

---

# Concept 48 — Safe Retry

A retry should ask:

```text
Which step failed?
What already succeeded?
What side effects happened?
Can I retry only the failed stage?
```

Do not blindly restart the entire workflow.

---

# Concept 49 — Idempotency

Idempotency means repeating the same logical operation does not duplicate its side effect.

Especially important for:

- credits
- payments
- artifact creation
- message creation
- retries

The specialist architecture does not automatically provide idempotency.

---

# Concept 50 — Specialist Latency

Different workflows have different latency profiles.

Normal Chat:

```text
model call
```

Search:

```text
search
+
model synthesis
```

PDF RAG:

```text
parse
+
chunk
+
many embeddings
+
vector search
+
generation
```

Image Generation:

```text
provider generation
+
S3 upload
```

So one global latency expectation is not appropriate.

---

# Concept 51 — Specialist Cost

Different workflows also have different cost profiles.

Examples:

- Chat → language-model tokens
- Search → search + language generation
- PDF RAG → embeddings + generation
- Image Generation → image-provider cost
- Coding → classifier + coding model
- PDF/PPT → model + render + S3

Application credits do not directly equal provider cost.

---

# Concept 52 — Tool Permissions

Each specialist should have only the permissions/tools it needs.

Example:

```text
Search
→ Tavily

Image Generation
→ Stability + S3

PDF RAG
→ Gemini embeddings + Qdrant + Groq
```

This follows least privilege.

---

# Concept 53 — Prompt Injection in Specialist Workflows

Untrusted content can enter through:

- user prompt
- uploaded PDF
- search results
- uploaded image content

Retrieved content should be treated as data.

It should not be allowed to override authorization or system-level application controls.

---

# Concept 54 — Search Security

Web content can be malicious or inaccurate.

Risks:

- prompt injection
- misleading information
- malicious instructions
- poisoned content

The model should not gain extra permissions because a webpage tells it to.

---

# Concept 55 — PDF RAG Security

Uploaded PDF text can contain malicious instructions.

The PDF is untrusted user data.

The RAG pipeline should:

- enforce authorization outside the model
- treat document text as source data
- limit available tools/actions
- validate outputs where needed

---

# Concept 56 — Coding Security

Generated code is untrusted output.

Do not execute arbitrary generated code directly on a trusted backend.

A future code-execution system should use:

- sandboxing
- isolation
- resource limits
- dependency controls
- network restrictions
- time limits

---

# Concept 57 — Testing the Chat Specialist

Test:

- normal prompt
- conversation context loading
- provider failure
- long history
- persistence failure
- credit failure

Expected behavior should be explicit.

---

# Concept 58 — Testing Search

Test:

- correct routing
- Tavily success
- empty results
- malformed result
- Tavily timeout
- Groq failure after retrieval
- prompt injection in retrieved content

---

# Concept 59 — Testing Coding

Test:

- generate intent
- explain intent
- review intent
- valid structured JSON
- malformed JSON
- truncated output
- missing file fields
- frontend preview compatibility

---

# Concept 60 — Testing PDF RAG

Test:

- text PDF
- scanned PDF
- empty PDF
- large PDF
- retrieval relevance
- Qdrant failure
- embedding failure
- Groq failure
- wrong retrieved chunks

---

# Concept 61 — Testing Document Generation

Test:

- valid structured content
- malformed JSON/content
- renderer failure
- S3 failure
- presigned URL failure
- large generated document

---

# Concept 62 — Testing Image Generation

Test:

- normal generation
- provider timeout
- provider rejection
- invalid image bytes
- S3 failure
- URL generation failure

---

# Concept 63 — Testing Image Analysis

Test:

- supported image
- corrupted image
- large image
- Gemini failure
- cleanup failure
- ambiguous content
- prompt injection-like text inside image

---

# Concept 64 — Specialist Observability

For every specialist track:

- route selected
- workflow start/end
- provider/tool call
- latency
- error stage
- output type
- retries
- credit behavior
- artifact success
- safe correlation ID

Current project has logs, but not mature per-specialist tracing/evaluation.

---

# Concept 65 — Specialist Evaluation

Evaluation is different by workflow.

Chat:

- usefulness
- correctness

Search:

- retrieval relevance
- synthesis quality

RAG:

- retrieval quality
- groundedness

Coding:

- schema validity
- compile/test in future sandbox

Image Analysis:

- correctness on labeled images

Document Generation:

- structure completeness
- renderer success

No mature automated AI evaluation suite is verified.

---

# Concept 66 — Scaling Specialist Workloads

All specialists live inside Agent.

Scaling Agent replicas can increase concurrency.

But it does not solve:

- provider quotas
- Qdrant limits
- Redis races
- repeated RAG indexing
- payment/credit consistency
- long synchronous requests

Measure first.

---

# Concept 67 — When to Split a Specialist Into a Separate Service

Possible reasons:

- very different scaling need
- different runtime
- high CPU/GPU requirements
- different security boundary
- independent deployment ownership
- long-running asynchronous jobs

Do not split merely because there are eight workflows.

---

# Concept 68 — When to Use Async Workers

Long operations may be better as background jobs.

Candidates could include:

- heavy document processing
- long image generation
- large report/PPT generation

Future pattern:

```text
API
 ↓
Job created
 ↓
Queue
 ↓
Worker
 ↓
Status store
 ↓
Frontend polling / notification
```

This is not currently verified.

---

# Concept 69 — Production V2: Structured Output Validation

Add schemas for:

- Coding `files[]`
- PDF document structure
- PPT slide structure
- route labels
- artifact metadata

This reduces fragile JSON parsing.

---

# Concept 70 — Production V2: Provider Abstraction

A stronger architecture could isolate provider-specific calls behind internal adapters.

Example:

```text
CodingService
 ↓
ModelAdapter
 ↓
OpenRouter / Alternate Provider
```

Benefits:

- easier testing
- clearer fallbacks
- less provider-specific code spread

But not every provider feature can be perfectly abstracted.

---

# Concept 71 — Production V2: Timeout Policy

Each external dependency should have explicit timeouts.

Example:

```text
Tavily timeout
Groq timeout
Qdrant timeout
S3 timeout
```

Without timeouts, synchronous requests can hang too long.

---

# Concept 72 — Production V2: Circuit Breakers

If a provider repeatedly fails:

```text
calls fail
 ↓
circuit opens
 ↓
temporary fail-fast
 ↓
recover/test later
```

Useful to prevent cascading failures.

Not currently verified.

---

# Concept 73 — Production V2: Workflow Cost Metrics

Track per workflow:

```text
route count
provider calls
token usage
embedding count
search count
image generations
latency
success rate
estimated cost
```

This supports pricing and optimization.

---

# Concept 74 — Production V2: Artifact Lifecycle

Persist artifact metadata:

```text
artifactId
ownerId
conversationId
objectKey
type
status
createdAt
retention
```

Then reauthorize and generate fresh URLs.

---

# Concept 75 — Production V2: Persistent Document Lifecycle

Add:

```text
documentId
ownerId
Qdrant collection/index mapping
page/chunk metadata
createdAt
retention
status
```

Then users can upload once and ask multiple later questions safely.

---

# Concept 76 — Production V2: Better RAG

Possible improvements:

- semantic-aware chunking
- page metadata
- retrieval thresholds
- reranking
- hybrid search
- evaluation dataset
- citations

Only add advanced retrieval if evaluation shows benefit.

---

# Concept 77 — Production V2: Better Memory

Possible improvements:

- token-aware history
- summaries
- recent-message windows
- atomic updates
- stable TTL policy
- workflow-specific memory policy

---

# Concept 78 — Production V2: Better Failure Semantics

Instead of:

```text
HTTP 200
"An error occurred"
```

use:

- structured status
- technical error type
- user-safe message
- retryable/non-retryable flag
- correlation ID

---

# Concept 79 — Design Trade-Off: Specialist Breadth vs Complexity

More specialists can improve task specialization.

But every new specialist adds:

- route label
- prompt
- provider/tool logic
- tests
- monitoring
- cost behavior
- security surface

Add specialists only when they represent a genuinely different task path.

---

# Concept 80 — Final NovaMind Specialist Story

A strong explanation:

> NovaMind's Agent service contains eight predefined specialist workflows. LangGraph routes each request to the appropriate specialist using explicit selection, file-aware rules and model classification. Each specialist then executes a task-specific pipeline. Chat uses a Groq-backed language model with conversation context. Search uses Tavily followed by Groq synthesis. Coding uses a coding-intent step and DeepSeek through OpenRouter to return structured files. PDF RAG parses and chunks the PDF, creates Gemini embeddings, retrieves the top relevant chunks from Qdrant and uses Groq for the answer. PDF and PPT generation use LLM-generated structured content followed by PDFKit or PptxGenJS and S3 artifact delivery. Image Generation uses Stability AI and Image Analysis uses Gemini multimodal. The workflows update LangGraph state and use Chat/Auth/S3 or other dependencies where required. Because the paths are predefined, this is bounded specialist orchestration rather than unrestricted autonomous agent behavior.

---

# Quick Revision — Module 07

```text
Chat
→ Groq-backed LLM
→ text

Search
→ Tavily
→ Groq synthesis

Coding
→ coding-intent classification
→ OpenRouter
→ DeepSeek
→ files[]

PDF RAG
→ pdf-parse
→ chunks 1000 / overlap 200
→ Gemini embeddings
→ Qdrant top 5
→ Groq answer

PDF Generation
→ LLM content
→ PDFKit
→ S3
→ presigned URL

PPT Generation
→ LLM slides
→ PptxGenJS
→ S3
→ presigned URL

Image Generation
→ Stability AI
→ S3

Image Analysis
→ Gemini 2.0 Flash
→ text
```

## Important boundaries

```text
Specialist ≠ microservice
Tool ≠ model
Provider ≠ model
Artifact URL ≠ artifact object
PDF RAG ≠ PDF Generation
Image Analysis ≠ Image Generation
Application credits ≠ real provider cost
```

## Current limitations

```text
No full code execution/test loop
No OCR for scanned PDFs
No persistent document-index lifecycle
No mature citation verification
No mature structured-output validation
No uniform specialist memory behavior
No mature per-specialist AI evaluation suite
No mature async job system
```

## Best interview sentence

> **NovaMind uses eight task-specific workflows inside one Agent service. LangGraph handles bounded routing, and each specialist uses the models, tools, storage and parsing logic appropriate to that task rather than forcing every request through one general LLM path.**

**Module 07 learning file complete.**
