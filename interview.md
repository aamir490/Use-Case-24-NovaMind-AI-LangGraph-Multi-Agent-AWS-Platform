# Project Interview Guide

**NovaMind AI — AWS Generative AI / Agentic AI portfolio preparation**

Start with a short answer, then use the technical sections for follow-up questions. Timings are rehearsal targets; speak in your own words.

**Evidence rule:** “Implemented” means visible in application code or checked-in configuration. “Documented deployment” means described in the provisioning guide, not live-verified. “Future improvement” means proposed work. Screenshots do not establish current health, availability or scale. No measured latency, cost savings, customer adoption or throughput is established by this repository review.

This guide was cross-checked against frontend and backend source, every specialist, graph/configuration files, Dockerfiles, task definitions, deployment workflow, README and other project documentation. Package inventories distinguish dependencies from active integrations. Older documentation is context, not proof where it conflicts with executable code.

## Navigation

- [Introduction](#project-introduction)
- [Architecture diagram](#architecture-diagram)
- [Architecture speaking scripts](#how-to-explain-the-architecture-in-an-interview)
- [Project storytelling](#how-i-tell-the-story-of-this-project)
- [Tell me about your project](#tell-me-about-your-project)
- [Request flow](#end-to-end-request-flow)
- [Six user scenarios](#end-to-end-scenarios)
- [LangGraph](#langgraph)
- [RAG pipeline](#rag-pipeline)
- [AWS services](#aws-services-and-why-they-are-used)
- [Security](#security)
- [Implemented versus proposed](#implemented-vs-production-improvements)
- [Why questions](#why-questions)
- [Question bank](#interview-question-bank-and-cross-questions)
- [Troubleshooting](#troubleshooting-interview-scenarios)
- [Documentation corrections](#documentation-corrections-and-evidence-boundaries)
- [Quick revision](#10-minute-interview-revision-sheet)

## Project Introduction

NovaMind AI is an authenticated workspace for chat, research, coding, document generation, image generation and questions about uploaded files. React provides the interface; five Express services handle API routing, identity, conversations, AI workflows and payments. LangGraph connects the AI processing steps. AWS configuration supports container deployment and static frontend delivery.

**Remember: five backend services, eight specialist agents, nine named graph nodes including the router.** The eight agents are functions inside the Agent service, not eight separately deployed containers.

## Problem Statement

A user may need different tools to search the web, explain a document, write code and create a presentation. This project brings those tasks into one interface with identity, history and usage credits. The repository does not establish customer research or measured productivity improvements.

## Solution

The user sends a prompt, optionally selects a specialist or attaches a file, and receives a result from the appropriate workflow. Text appears in chat; generated code appears in a code panel; documents and images can be downloaded through S3 links.

## Business/Technical Use Case

An example user researches a topic, requests an explanation, generates example code and creates a presentation. Another uploads a text-based PDF and asks a question about its contents. These are example use cases, not claims of paying customers. Technically, the project demonstrates model integration, workflow state, identity, persistence, usage accounting and AWS delivery.

## Key Features

- Firebase Google sign-in and Redis-backed session cookies.
- Automatic or explicit workflow selection.
- Groq chat, Tavily search and DeepSeek coding assistance.
- PDFKit documents, PptxGenJS presentations and Stability AI images.
- Gemini image analysis and Gemini/Qdrant PDF retrieval.
- MongoDB conversation history, credit plans, Razorpay verification and admin views.
- Read-only Monaco code display and a sandboxed HTML/CSS/JS iframe preview.
- Browser speech recognition where supported; no AWS speech service integration.
- Five Dockerized services, ECS task definitions and GitHub Actions deployment.

## Technology Stack

| Area | What this project uses |
|---|---|
| Frontend | React 19, Vite 8, React Router 7, Redux Toolkit, Tailwind CSS 4, Axios |
| Output UI | React Markdown, syntax highlighting, Monaco, Motion, Lucide/React Icons |
| Backend | JavaScript ES modules, Node.js 22 Docker base, Express 5, Mongoose, ioredis, Multer |
| Orchestration | LangGraph StateGraph, LangChain messages/provider integrations |
| Text and multimodal models | Groq `openai/gpt-oss-120b`, Gemini `gemini-2.0-flash`, OpenRouter `deepseek/deepseek-chat` |
| Retrieval | pdf-parse, recursive character splitting, `gemini-embedding-001`, Qdrant |
| Tools | Tavily, Stability AI REST, PDFKit, PptxGenJS, AWS S3 SDK |
| Identity/payment | Firebase browser and Admin SDKs; Razorpay and HMAC verification |
| Data | MongoDB Atlas, Redis/ElastiCache, Qdrant Cloud, S3 |
| AWS configuration | ECS Fargate, ECR, Cloud Map URLs, Secrets Manager references, IAM roles, CloudWatch Logs |
| Network/frontend guide | VPC, subnets, ALB, NAT, security groups, S3 frontend and CloudFront |

Model names above are configured identifiers, not verified current availability or benchmark rankings. Bedrock's runtime SDK is installed but is not used by the active agent code. No fine-tuning or self-hosted inference is implemented.

# Architecture Diagram

[![NovaMind AI — AWS architecture poster](new-project-pic/novamind-aws-architecture-poster.png)](new-project-pic/novamind-aws-architecture-poster.png)

This is the **exact image used by README.md**, reused without copying or editing it. Its five services, eight specialists, provider assignments, retrieval steps and deployment pipeline match the main implementation. Its AWS network layout represents the documented deployment design.

**Explain these qualifications when using the picture:**

- The browser calls the API; S3 does not forward API requests. Locally the browser goes directly to Gateway on port 8000.
- ALB forwards to Gateway, which independently proxies the four domain services. Auth, Chat, Agent and Billing are not a processing chain.
- Subnet boxes do not prove multi-AZ replicas, failover or autoscaling. The poster's least-privilege label still requires real IAM policy review.
- PDF indexing and answering occur in one request. The panel does not establish persistent PDF follow-up retrieval.
- ECR, IAM and Secrets Manager are supporting AWS services, not containers hosted inside the VPC. The poster groups them visually.
- Application source and task definitions take precedence over illustrative labels. No live AWS inventory was queried in this review.

# How to Explain the Architecture in an Interview

## Architecture Walkthrough

Begin with what the user does, follow the request, then explain the supporting infrastructure.

### 30-Second Explanation

“The user opens a React website delivered through CloudFront and S3. API requests go through an ALB to my Gateway, which checks the session and routes the request. AI requests reach an Agent service where LangGraph selects one of eight workflows. Those workflows call external models and tools. MongoDB saves conversations, Redis supports sessions and memory, and S3 holds generated files.”

### 1-Minute Explanation

“There are two paths in the diagram. CloudFront and S3 deliver the website. Separately, the browser sends API requests through the ALB to an Express Gateway. After checking the Redis session, Gateway calls Auth, Chat, Agent or Billing depending on the route.

“For AI requests, Agent runs a LangGraph workflow. It respects an explicit selection first, checks file types next, and otherwise asks Groq to classify the prompt. All eight specialists run inside this service. Search uses Tavily followed by Chat; PDF questions use Gemini embeddings and Qdrant before Groq answers.

“The task definitions run the services on Fargate with logging and secret configuration. The network layout comes from the deployment guide. I would verify live resources before claiming availability guarantees.”

### 3-Minute Explanation

“I explain the architecture in three parts: getting into the application, processing a request, and operating the system.

“First, the React frontend is built with Vite. S3 stores the files and CloudFront delivers them. A user signs in with Google through Firebase. The browser sends the Firebase ID token to Auth, which verifies it, finds or creates a MongoDB user, and creates a Redis session. The browser receives an HTTP-only session cookie.

“Second, the browser sends API requests to its configured endpoint. In the deployment design, an ALB forwards them to Gateway on port 8000. Protected routes look up the cookie in Redis. Gateway then forwards the user ID and proxies to a domain service. Auth handles accounts and credits; Chat handles persistence; Billing handles Razorpay; Agent handles AI processing. Cloud Map URLs let the services find each other internally.

“Agent saves the user's message through Chat and invokes LangGraph. The router uses an explicit choice before checking PDF or image attachments. Without either, Groq classifies the prompt. The graph has eight specialists, but they are functions in one process. It is a bounded workflow, not an autonomous planner.

“A search request calls Tavily and passes the results into Chat for synthesis. Coding uses Groq for intent classification and DeepSeek through OpenRouter for the answer. A PDF question extracts and chunks the file, creates Gemini embeddings, retrieves useful Qdrant chunks and asks Groq to answer from context. Generated documents and images use S3 download links. The controller updates memory, saves the assistant message and returns JSON to React.

“Finally, Fargate runs containers. ECR stores images, Secrets Manager supplies configured startup values, IAM roles grant permissions and CloudWatch collects logs. GitHub Actions rebuilds images and requests ECS redeployments, then publishes the frontend.

“The next steps are authorization fixes, reliable billing and failures, persistent PDF retrieval and tested readiness checks. I would not claim autoscaling, full high availability or benchmark results from the current repository.”

### 5-Minute Technical Walkthrough

**Frontend — about 45 seconds.**

“The product is one account-based workspace for different AI tasks. The static React application has Redux slices for users, conversations, messages and artifacts. CloudFront delivers the S3 build. The browser has a separate Axios client using VITE_SERVER_URL and credentialed requests. The static website does not process prompts. In local development that client calls Gateway directly.”

**Identity and entry — about 50 seconds.**

“Google sign-in produces a Firebase ID token. Auth verifies it with Firebase Admin, finds or creates the user, and writes a UUID session into Redis. The cookie is HTTP-only; production settings enable Secure and SameSite=None. Gateway reads the session for protected routes and supplies x-user-id to a downstream service. ALB is the documented public API entry, and Cloud Map provides private service names. Login must be public, but the current public Auth proxy is broader than login and needs hardening.”

**Services and graph — about 70 seconds.**

“The five services are Gateway, Auth, Chat, Agent and Billing. Each has a Dockerfile and task definition. Agent first asks Chat to save the input, then invokes a StateGraph with the prompt, conversation ID, selection, user ID and optional file. Nine nodes are named: a router and eight specialists. Explicit selection wins over file detection. A PDF in Auto selects PDF RAG; an image selects image analysis. Otherwise Groq returns a label. Unknown labels fall through to Chat in the graph switch. Search is the special two-stage path: Tavily retrieval followed by Chat. There are no graph checkpoints, approval stages or autonomous planning loops configured.”

**AI, data and response — about 70 seconds.**

“Groq handles most text tasks and routing. DeepSeek through OpenRouter handles coding; Gemini supplies image analysis and embeddings. PDF RAG extracts text, splits at one thousand characters with two hundred overlap, creates a Qdrant collection and retrieves five chunks. Groq receives the context and an instruction to answer only from it. That is grounding, not a guarantee against hallucination. The collection ID is not saved to the conversation, so persistent document follow-up is missing.

“Document agents ask for JSON, create files locally and upload to S3. Image generation refines a prompt with Groq and calls Stability AI. Code generation returns files for Monaco and a limited iframe preview; there is no server-side execution. The controller records the answer through Chat, updates Redis memory, and returns answer, images and artifacts.”

**AWS operations — about 45 seconds.**

“The task definitions select Fargate and awsvpc networking. Agent requests one vCPU and two GiB; the other services request half a vCPU and one GiB. ECR stores images, the execution role supports startup operations, task roles grant application access, and awslogs sends container output to CloudWatch. The guide places tasks in private subnets with NAT for external providers. It describes security groups, but those instructions are not proof of current rules or multi-AZ resilience.”

**Delivery and trade-offs — about 40 seconds.**

“GitHub Actions pushes five mutable image tags and calls force-new-deployment. The frontend job builds React, syncs S3 and invalidates CloudFront. There is no ECS stability wait or automated test stage. Before production, I would close exposed mutations and missing ownership checks, rotate exposed credentials, make payment updates idempotent, and add deadlines, consistent failures and readiness tests. That distinguishes an integrated portfolio implementation from production guarantees.”

# How I Tell the Story of This Project

Use this outline naturally. The code cannot verify your motivation, exact development timeline or personal incident history. Only add personal details you can substantiate.

1. **Problem:** “The application brings multiple AI tasks into one workspace rather than making users switch tools.”
2. **Why I built it:** “It is my portfolio example connecting generative AI to a usable application and AWS delivery.” Add your actual personal motivation.
3. **Initial design:** “The design separates the UI, accounts, conversations, AI processing and payments.” Do not invent a previous monolith or development sequence.
4. **Why Agentic AI:** “A request selects a workflow and tools, instead of always making one generic model call.”
5. **Why LangGraph:** “I can point to the router, named nodes and Search-to-Chat edge in one graph definition.”
6. **Why specialists:** “Code, images and documents require different preparation and output handling.”
7. **Application architecture:** “Five services separate responsibilities, with Gateway as the intended browser entry.”
8. **Containerization:** “Each service has a Node 22 Alpine image built with the shared backend directory.”
9. **AWS delivery:** “Task definitions and the workflow show container delivery; the guide describes network provisioning.”
10. **Security:** “Firebase verifies identity, Redis stores sessions, and IAM/Secrets Manager support access. I can also explain remaining authorization gaps.”
11. **Monitoring:** “CloudWatch collects logs. Tracing and business metrics are future work.”
12. **Challenge:** “A possible engineering challenge is separating a provider failure from a persistence or network failure.” Do not claim a hypothetical outage happened to you.
13. **Solution:** “I would investigate each boundary and add typed errors, deadlines and correlation IDs.” These are proposed controls.
14. **Learning:** “An AI answer is only one part of reliability; authorization, retries, billing and operations matter too.” Personalize this with a verified example.
15. **Next step:** “First protect users and balances, then make processing recoverable, then optimize scale using measurements.”

For behavioral answers, use **situation → task → action → verified result → lesson**. Old notes mention a model retirement, S3 region errors and a secret-scanning incident. Those notes alone do not establish the cause or your personal experience. Say “Here is how I would investigate it” when evidence is missing.

# Tell Me About Your Project

### 30-second answer

“NovaMind AI is my portfolio project for bringing multiple AI tasks into one authenticated workspace. Users can chat, search, generate code and documents, or ask about uploaded files. It uses React, five Node.js services and eight LangGraph specialists, with AWS container deployment. The interesting part is the complete request path—from identity and routing to AI tools, storage and delivery.”

### 1-minute answer

“NovaMind AI combines AI workflows in one interface with sign-in, history and credits. React handles the UI. The backend is split into Gateway, Auth, Chat, Agent and Billing.

“The Agent service contains a LangGraph router and eight specialists. Users can choose a workflow, or the router uses the file type and prompt. Search uses Tavily, coding uses DeepSeek through OpenRouter, and PDF questions use Gemini embeddings with Qdrant before Groq answers. Generated documents and images go to S3.

“The repository includes Dockerfiles, Fargate task definitions and GitHub Actions deployment. I can explain both the integrated design and its limitations: synchronous generation, missing persistent PDF retrieval, and authorization and billing controls that need hardening.”

### 2-minute answer

“The problem is switching between separate tools for chat, research, coding, presentations and document questions. NovaMind AI puts those tasks behind one Google-authenticated interface with history and usage credits.

“The frontend uses React and Redux. Firebase verifies identity, and Auth creates a Redis session. API requests go through an Express Gateway to separate account, conversation, AI and payment services. The AWS design runs those services on Fargate, while S3 and CloudFront deliver the website.

“The AI implementation is a bounded LangGraph workflow. It does not invent an open-ended plan. It has routing rules, a classifier, eight specialists and a Search-to-Chat chain. Each specialist has its own integration: DeepSeek for coding, Stability AI for generation, Gemini for image analysis, and Groq for most text work.

“For PDF questions, Agent parses and chunks the upload, embeds it with Gemini, stores vectors in Qdrant, retrieves five useful chunks and asks Groq to answer from them. The answer returns to chat, and the Chat service persists messages. Generated files use S3 download links.

“The workflow builds ECR images and redeploys ECS services; task definitions configure CloudWatch and Secrets Manager. I would not call the whole system production-ready yet. The next steps are stronger authorization, atomic and idempotent billing, consistent failure handling and a persistent document index. I also have no load-test results to justify a claim about thousands of concurrent users.”

### Detailed technical answer

“I explain three boundaries. At the identity boundary, Firebase verifies the user, Redis stores a session, and Gateway forwards identity to domain services. At the workflow boundary, Agent saves input, invokes LangGraph and runs a specialist that calls APIs or creates files. At the data boundary, Chat persists messages, Auth stores credits, Billing records payments, Qdrant stores vectors and S3 stores generated binaries.

“These boundaries expose trade-offs. Separate services still share dependencies and trust assumptions. The graph expresses workflow structure but has no configured durable checkpointing. Redis is useful but critical to access. Generating content, charging credits and saving the answer are not one transaction. I would prioritize correctness and security before increasing replica counts.”

Continue with the five-minute walkthrough above when asked for deployment details rather than repeating the introduction.

## End-to-End Request Flow

This is the precise answer to **“What happens after Send?”**

1. `ChatInput.jsx` requires non-empty prompt text and no request in progress. A file selection alone is not an upload.
2. It creates a conversation if needed using `GET /api/chat/create-conversation`, updates a New Chat title, and adds the user message optimistically to Redux.
3. It sends multipart `FormData`: `prompt`, `conversationId`, lowercased `agent`, optional `file`, to `POST /api/agent/chat`. Axios includes credentials.
4. AWS deployment uses ALB → Gateway; local development goes directly to Gateway. Gateway checks the Redis session and injects `x-user-id` for this protected route.
5. The proxy strips its mounted prefix; Agent handles `/chat`. Multer writes allowed PDF/images to local `temp/`, capped at 20 MiB.
6. Agent calls Chat `/save-message` for user input. These internal calls send a body, not a verified user header.
7. `graph.invoke` passes state to the router and specialist. The specialist checks a rate bucket, calls models/tools, and requests credit deduction at its own point in processing.
8. The controller appends user and assistant text to Redis memory and saves assistant content/images/artifacts through Chat.
9. It returns JSON `{ answer, images, artifacts }`, normally HTTP 200. A caught specialist failure can also return via this path as text.
10. React clears loading/file state, renders the answer and sets the artifact panel. Helpers returning `null` are not handled safely at every caller.

Sources: [ChatInput](frontend/src/components/ChatInput.jsx), [Axios](frontend/utils/axios.js), [Gateway](backend/gateway/index.js), [proxy](backend/gateway/utils/proxyWithHeader.js), [Agent controller](backend/services/agent/controllers/agent.controller.js), [Chat controller](backend/services/chat/controllers/chat.controller.js).

## End-to-End Scenarios

All six use the authenticated path above. Not every node consumes Redis history or creates S3 objects.

### 1. Normal chat question

“Explain Docker containers.” Explicit Chat or Auto selects `chat`. Agent saves input; the node checks the chat bucket, loads Redis history (fetching Chat/MongoDB messages on a miss), creates LangChain messages and invokes Groq. It requests one credit deduction. The controller persists the answer and React renders it. No vector lookup or generated file is required.

### 2. Coding question

“Generate an HTML landing page.” `coding` checks its bucket, uses Groq to classify coding intent, then DeepSeek via OpenRouter. Exact `CODE_GENERATION` expects JSON containing `files`; other intents return Markdown. It requests ten credits. Chat stores the Project artifact; React displays read-only Monaco tabs and can preview an `index.html` with CSS/JS in an iframe. It does not execute generated code on the server, install its packages or run its tests.

### 3. Web search

“Find recent developments in this topic.” Search calls Tavily for up to five results and images, requests five credits, then the fixed graph edge runs Chat. Chat includes search context and history, invokes Groq and requests one more credit. Normal total: **six credits**, with both Search and Chat rate buckets consumed. Search image URLs are returned; they are not uploaded to S3. Grounding does not verify every generated citation.

### 4. Upload a PDF

The file picker only changes local UI state. Enter a prompt and click Send with **Auto** selected. Multipart data goes through Gateway and Multer; PDF MIME selects `pdfRag`. Explicit PDF selection instead chooses PDF generation, because explicit selection wins. Extraction, indexing and answering occur in the same request; there is no separate ingestion endpoint or document selector.

### 5. Ask questions about the PDF

**With the file attached:** read temp file → pdf-parse → 1,000-character chunks/200 overlap → Gemini embeddings → new `pdf-<timestamp>` Qdrant collection → five retrieved chunks → Groq context-only answer. It uses the shared PDF bucket and ten-credit cost. The controller saves the answer and returns it; the node attempts temp deletion in `finally`.

**A follow-up without the file:** React has cleared the attachment. Neither the conversation nor router retains a document/collection mapping. Auto may choose Chat, and a previous answer in history is not retrieval from the original document. Reattach the PDF in Auto mode to use the implemented RAG path. Persistent multi-turn PDF retrieval is future work.

### 6. Upload an image

Attach a chart and ask for an explanation in Auto. Multer writes the image; routing selects `imageAnalyzer`. It checks the shared image bucket, base64-encodes the file and sends text plus image to Gemini. It requests the ten-credit vision cost and attempts cleanup in `finally`. Chat saves the text response and React displays it. The original image is not automatically stored in S3. Explicit Vision means **generate an image**, not analyze this upload.

## Multi-Agent Architecture

Multi-agent here means specialized behaviors with different prompts/tools, selected by a router. It does not mean autonomous agents negotiating or running concurrently. All specialists are functions in one Agent process.

The UI has six explicit specialist buttons plus Auto. PDF RAG and Image Analyzer are reached normally through Auto file detection, explaining why eight specialist implementations do not mean eight buttons or containers.

## LangGraph

- `Annotation.Root` holds prompt, response, agent, conversation ID, search results, images, artifacts, user ID and file.
- Start → Router → conditional specialist edge; Search → Chat; other specialists → end.
- Priority: explicit non-Auto selection → PDF MIME → image MIME → Groq classifier.
- Unknown labels fall through to Chat in the graph switch; router exceptions are a separate failure.
- `compile()` has no checkpointer. Application Redis memory is not LangGraph checkpointing.
- `invoke()` is used; no parallel branches, streamed token implementation, approval interrupts, evaluator node or planner/replanner loop.

Sources: [graph](backend/services/agent/graph/graph.js), [router](backend/services/agent/graph/router.js), [state](backend/services/agent/graph/state.js).

## Individual AI Agents

| Node | Processing | Requested credits / rate bucket |
|---|---|---|
| chat | Redis/Chat history → Groq | 1; chat 20/60s |
| search | Tavily → Chat through graph edge | 5 plus Chat's 1; search 5/60s plus chat |
| coding | Groq intent → DeepSeek/OpenRouter → JSON files or Markdown | 10; coding 5/60s |
| pdf | Groq JSON → PDFKit → S3 | 10; pdf 5/60s |
| ppt | Groq JSON → PptxGenJS → S3 | 10; ppt 5/60s |
| vision | Groq refinement → Stability AI → S3 | 10; image 5/60s |
| pdfRag | Extract/split → Gemini embeddings → Qdrant → Groq | 10; shared pdf bucket |
| imageAnalyzer | Base64 file + text → Gemini | 10; shared image bucket |

Costs describe the normal path, not transactional guarantees. PDF/PPT deduct before file rendering/upload finishes. The helper swallows deduction failures. Most nodes catch errors; Image Analyzer's rate check is outside its `try`.

The PPT prompt requests six content slides; the renderer adds cover and closing slides, producing eight if the model follows the prompt. JSON parsing lacks comprehensive schema validation. PDF/image URLs request 1,440 seconds; PPTX requests 86,400 seconds, despite inconsistent user-facing expiry strings.

Sources: [agents](backend/services/agent/agents/), [rate limits](backend/services/agent/config/agentLimit.js), [helpers](backend/services/agent/utils/).

## RAG Pipeline

An embedding represents text numerically. Retrieval finds relevant passages; generation writes an answer from them. This does not retrain the model.

**Implemented:** text extraction, recursive character splitting, overlap, Gemini embeddings, a fresh Qdrant collection, similarity search with `k=5`, and a context-only Groq prompt. The vector-store integration embeds the query. The application does not explicitly configure a distance metric, so do not claim a tuned cosine setup from this source alone. The installed Qdrant integration can read `QDRANT_API_KEY` from the environment even though the application only passes URL and collection name.

**Not implemented:** OCR, persistent document IDs, conversation/document mapping, tenant metadata filtering, deduplication, collection cleanup, reranking, hybrid search, confidence thresholds, verified citations or evaluation datasets. A file-size cap is not a token/page/time budget.

**Proposed evaluation:** build representative PDF/question pairs with known supporting passages, plus unanswerable questions. Measure retrieval recall at five, correctness, answer support, abstention quality, latency and token cost. Test scanned documents, tables, repeated uploads and document prompt injection separately. Tune chunking, k and reranking against this dataset, not one demo. Do not invent scores.

Sources: [PDF RAG](backend/services/agent/agents/pdfRag.agent.js), [vectors](backend/services/agent/config/vectorDb.js), [embeddings](backend/services/agent/config/embeddings.js).

## Frontend Architecture

`App.jsx` defines `/` and `/admin`; `main.jsx` supplies Redux. Home performs Firebase popup login and sends the token to Auth. `/api/me` hydrates user state. SideBar selects conversations; ChatArea reloads messages and the latest stored artifact. ChatInput owns prompt/selection/file state. MessageBubble renders Markdown/images; Artifact provides read-only Monaco and an iframe with `sandbox='allow-scripts'`; BillingDrawer opens Razorpay checkout. AdminPage shows statistics, users and payments.

The React admin email check is a navigation guard, not the authorization boundary. `VITE_*` values are public build configuration. API helpers often return null/empty arrays on errors; callers do not consistently distinguish failure from an empty result. There is no streamed token renderer. Speech recognition uses the browser, not a backend transcription service.

## Backend/Microservices Architecture

| Service | Port | Responsibility |
|---|---|---|
| Gateway | 8000 | CORS, cookie parsing, Redis lookup, proxy routing, Morgan logs |
| Auth | 8001 | Firebase verification, User model, sessions, credits, admin APIs |
| Chat | 8002 | Conversations and messages |
| Agent | 8003 | Uploads, graph, providers, generated files, memory/rates |
| Billing | 8004 | Razorpay orders/signature verification, Payment records |

Communication is synchronous HTTP with Axios or proxy middleware, not an event bus. Task environments use Cloud Map names; local environments use localhost URLs. Database connections start after servers begin listening, so root responses do not prove dependency readiness. Auth's admin functions also read Chat/Billing databases directly, weakening strict domain isolation.

## Database and Storage

- **User:** Firebase UID, profile, plan, credits, total credits, expiry and timestamps.
- **Conversation:** user ID, title, timestamps. **Message:** conversation reference, role, text, image URLs and artifact files.
- **Payment:** user/order/payment IDs, amount, currency, plan, credits, status and timestamps.
- **Agent database:** Agent connects to MongoDB on startup, but persists messages through Chat; no agent-owned message model exists.
- **S3:** frontend assets and generated binaries have different bucket purposes. Generated code is a JSON artifact stored through Chat, not necessarily an S3 object.
- **Qdrant:** text/vectors per upload with no lifecycle cleanup or retained document mapping.

Separate database URIs do not establish independent clusters or failure domains. No tested backup/restore or Atlas HA configuration is established by the active source. Source: [Chat models](backend/services/chat/models/), [User](backend/services/auth/models/user.model.js), [Payment](backend/services/billing/models/payment.model.js).

## Redis/Cache

Gateway, Auth and Agent actively use Redis. Chat and Billing do not directly use it.

| Key | Actual behavior |
|---|---|
| `session-<uuid>` | JSON user snapshot; seven-day expiry on login and relevant credit/plan updates |
| `user-session-<userId>` | One mapped session ID per user |
| `messages-<conversationId>` | JSON string array, not a Redis list; hydrated from Chat |
| `rate:<userId>:<bucket>` | INCR counter; first request separately sets a 60-second expiry |

Memory hydration sets a 24-hour TTL, but `addMessage` uses plain SET and removes it. It shifts only one entry when length exceeds 20; an oversized database history is not strictly trimmed to 20. Concurrent read/modify/write can lose updates. On a cold load, history can include the input already saved by the controller, then Chat appends the same current prompt again. Rate INCR and EXPIRE are not one atomic operation.

**Future:** ordered/limited history queries, proper trimming/TTL, atomic rate updates and conversation concurrency controls. Source: [memory](backend/services/agent/config/memory.js), [rate limits](backend/services/agent/config/agentLimit.js), [shared Redis](backend/shared/redis/redis.js).

## Docker and Containerization

All five Dockerfiles are **single-stage** `node:22-alpine` builds. They install the backend root package, install service dependencies, copy the service and shared directory, then use `npm start`. Build context is `backend/`, for example:

```sh
docker build -f backend/services/agent/Dockerfile -t agent-service backend
```

This includes shared Redis code; using only the service folder as context breaks the COPY paths. Compose starts Redis only. Dockerfiles do not set a non-root USER, container HEALTHCHECK or production-only dependency installation.

**Build exclusion gap:** `.dockerignore` files exist inside service directories, but there is no context-root `backend/.dockerignore` or Dockerfile-specific ignore file. Root `.gitignore` also ignores `.dockerignore`. For the workflow's build context, those nested files do not provide the intended exclusions. Broad COPY instructions can include local environments, service-account files or dependencies if present during a local build. A clean CI checkout reduces some risks but does not prove every image is secret-free. See [Docker build-context rules](https://docs.docker.com/build/concepts/context/).

## AWS Services and Why They Are Used

| Service | Evidence and purpose |
|---|---|
| ECS Fargate | Five task definitions request FARGATE/awsvpc; backend container runtime |
| ECR | Workflow pushes five images referenced by tasks |
| Cloud Map | Internal `novamind.local` URLs; discovery provisioning described in guide |
| ElastiCache | Redis endpoints in tasks; sessions, memory and counters |
| S3 | Active SDK upload/presigning; frontend sync workflow |
| CloudFront | Frontend URL and invalidation workflow; static distribution in guide |
| Secrets Manager | Task `secrets` references for database, model, Firebase and billing values |
| IAM | Execution/task role references and guide policies |
| CloudWatch Logs | awslogs configuration on all five tasks |
| VPC, ALB, NAT, security groups | Manual provisioning documented; not a live inventory |

“API Gateway” in project descriptions means the Express service, not the managed Amazon API Gateway product. The current inference path does not use Bedrock, EKS or Lambda.

## ECS/Fargate Deployment

Agent requests 1024 CPU units and 2048 MiB; the other services request 512 CPU units and 1024 MiB. All use awsvpc and FARGATE. Task definitions specify image, resources, environment, secrets, roles, logs and ports. They contain no container healthCheck.

Desired count, subnet selection, target group and deployment settings belong to ECS service provisioning. The guide proposes one task per service; this is not a freshly verified live count. ECS service replacement can maintain desired count after a task stops, but does not resume an in-flight graph or recover a temporary upload. See [AWS service replacement behavior](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-parameters.html).

## Networking

**Documented:** us-east-1 VPC, public/private subnets, public ALB, private tasks, Cloud Map DNS, NAT egress, private Redis on 6379 and external provider/database connectivity. Atlas access is via external routing and its allowlist, not a demonstrated PrivateLink connection.

Route tables, security groups and DNS determine reachability; a private subnet alone is not an authorization control. The guide uses one NAT AZ to save cost and a Redis development example with zero replicas. Multiple subnet definitions do not establish application HA.

ALB targets should use task IPs for awsvpc; the guide targets Gateway on 8000 with `/` as its check. CloudFront supplies website viewer HTTPS. The guide includes HTTP API and optional custom-domain HTTPS variants, so do not claim an active certificate or CloudFront API origin without inspection. [AWS ALB integration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/alb.html).

## Security

**Implemented:** Firebase token verification; HTTP-only session cookies with production Secure/SameSite settings; Gateway checks on protected prefixes; an Auth admin email check; MIME/size filtering; IAM/secret references; sandboxed browser preview.

**Important code-review findings, not exploitation claims:**

1. Gateway's entire `/api/auth` prefix is public. Auth exposes `/update-plan` and `/deduct-credits` there without internal authentication.
2. Auth mounts admin routes at the same service root. The public Auth proxy also creates an alternate route to admin operations, which trust an `x-user-id` header. Protecting `/api/admin` alone does not close this path.
3. Chat lists conversations by user but does not check ownership on individual message reads, saves or title updates.
4. `task-defs/auth.json` contains credential-bearing plaintext admin database URIs. Do not copy their values into interview material; rotate and externalize them.
5. Auth has no cookie-parser middleware, while logout reads `req.cookies`. Clearing the browser cookie does not demonstrate Redis-session revocation. Admin updates/deletions do not reliably invalidate cached sessions either.
6. No dedicated CSRF controls, comprehensive schema validation or prompt-injection guardrails are configured. CORS and HTTP-only cookies are not substitutes.
7. Logs expose user/session data and full results; the frontend logs login tokens. Redaction is needed.

Sources: [Gateway](backend/gateway/index.js), [Auth routes](backend/services/auth/routes/auth.route.js), [Auth initialization](backend/services/auth/index.js), [admin middleware](backend/services/auth/middleware/admin.middleware.js), [Chat controller](backend/services/chat/controllers/chat.controller.js), [Auth task](task-defs/auth.json).

## IAM and Secrets

The **execution role** supports ECS startup operations: image pull, configured secret retrieval and logs. The **task role** supplies credentials to application code. Agent has an S3-oriented task-role reference; Auth also has a task role. Role names do not prove least privilege: inspect resource/action scope and any KMS dependencies.

Firebase Admin parses `FIREBASE_SERVICE_ACCOUNT` directly or reads a local JSON file. It does not download that file through an AWS CLI startup script. Secrets injected as environment variables need a new task to pick up a changed value. Frontend VITE variables are public build content, not secret storage.

**Future:** rotate exposed URIs, fix build exclusions, scope policies, verify image contents and use GitHub-to-AWS OIDC instead of the workflow's configured static credentials. Do not say all credentials are already externalized.

## Monitoring and CloudWatch

Console output and Gateway Morgan logs go to `/ecs/novamind-*` groups through awslogs. No configured distributed tracing, correlation IDs, custom business metrics, RAG dashboard or alarm definitions are present in active code/configuration.

During diagnosis, inspect ECS events/stopped reasons, target health and available AWS metrics. Do not assume ALB access logs, Container Insights or alarms are enabled. **Proposed instrumentation:** node latency, provider errors, token cost, credit-update failures, retrieval quality and success/failure counts, with sensitive fields removed.

## CI/CD

**Implemented:** push to main → AWS authentication → five image builds/tags/ECR pushes → five ECS force-new-deployment commands → dependent frontend npm install/build → S3 sync with delete → CloudFront invalidation.

The workflow uses mutable latest tags. It does not register updated task-definition JSON, wait for service stability, run tests/lint, scan images, deploy only changed services, configure concurrency control or automate rollback. A successful backend job means commands succeeded, not that every service is healthy.

**Future:** immutable commit-SHA images, registered task-definition revisions referring to those images, service-stability and smoke-test gates, then frontend promotion. Rollback must select a known-good revision and image digest; a service update does not directly replace an image tag without a corresponding task definition.

Source: [deploy.yml](.github/workflows/deploy.yml).

## Scalability

Services are separate deployment units and much state is external. Uploads and in-flight graph work are local to a task. No autoscaling policy or measured capacity is established. More replicas still share provider quotas, Redis and databases, and can worsen non-atomic updates.

**Future:** measure request mix/concurrency, fix correctness, separate long jobs into queued workers, persist job inputs, bound provider concurrency, then scale using workload signals and load tests. CPU alone may not reveal slow external-model I/O.

## High Availability

Fargate and ALB are building blocks, not an end-to-end guarantee. One task per service, a single NAT AZ and a no-replica Redis example create interruption risks. Active task definitions do not prove multi-AZ replicas, Redis failover, database backups or recovery testing.

**Future:** service replicas across AZs, resilient egress, tested Redis/database failover and restore, and a measured SLO. Failover time and zero data loss must not be promised without testing.

## Fault Tolerance

Most specialist exceptions become fallback text and may be persisted with HTTP 200. Rate-limit errors therefore do not consistently produce HTTP 429. Image Analyzer checks its rate before its try block. Agent's generic error middleware also references undefined `error` instead of `err`.

No explicit application-level deadline, cancellation propagation, durable job retry or provider-fallback policy exists. SDK defaults may retry; that is not a coordinated end-to-end recovery design. Model work, credit deduction, S3 upload and message storage are separate effects.

**Future:** typed errors, deadlines, transient-only backoff, idempotency, compensation, durable job state and graceful shutdown. Avoid blind retries on payment or credit operations.

## Cost Optimization

Discuss cost drivers: task resource-hours, ALB, NAT hours/data, Redis capacity, S3 storage/requests, CloudFront transfer, logs, vectors and external models. User count alone is not a cost model. The repository establishes neither a current bill nor model speed/cost benchmarks.

**Future:** right-size from measurements, reduce repeated embeddings with document hashes, trim prompt context, expire unused artifacts/vectors, set log retention and compare egress options based on traffic. Five always-running services have overhead; a smaller deployment can be a sensible portfolio trade-off.

## Production Readiness

This demonstrates integrated features and deployment configuration. It still requires hardening before handling sensitive user documents or real balances. A screenshot or green deploy badge does not resolve authorization or billing defects.

Validation should cover login/logout, revoked users, cross-user access, all routes, missing keys, provider failures, insufficient credits, replayed payment verification, file cleanup and crashes during generation. The backend test command is a placeholder. Frontend has lint/build scripts; this guide does not claim fresh test or deployment results.

## Limitations

The largest limitations are exposed alternate routes, missing ownership checks, plaintext credentials/build exclusions, non-atomic billing, hidden failures, synchronous processing, nonpersistent PDF retrieval, imperfect memory lifecycle and unverified resilience. No autonomous planner, fine-tuning, verified hallucination prevention or 10,000-user test is implemented.

## Future Improvements

1. Protect users and balances: close alternate routes, verify ownership, rotate credentials, fix revocation, make credits atomic and payments idempotent.
2. Make workflows reliable: typed results, validation, deadlines, durable jobs and safe retries.
3. Make RAG reusable: persistent document IDs, authorization, deduplication, cleanup and evaluation.
4. Make delivery repeatable: infrastructure as code, immutable images, task revision deployment, effective exclusions and automated tests.
5. Then scale: multi-AZ replicas, tested data failover, provider-aware concurrency, telemetry and capacity measurements.

## Implemented vs Production Improvements

| Topic | Implemented / repository evidence | Proposed or unverified |
|---|---|---|
| Graph | Router + eight specialists; Search-to-Chat | Planner loops, checkpointer, approval stages |
| RAG | Per-upload indexing/top-five retrieval | Persistent follow-ups, tenant filters, reranking/evaluations |
| Identity | Firebase and Redis sessions | Complete route/ownership checks and revocation |
| Billing | HMAC verification and credit updates | Idempotency, atomic ledger, webhook reconciliation |
| Runtime | Five Fargate task definitions | Live health, tested sizing, durable jobs |
| Networking | Guide and discovery URLs | Confirmed active TLS/SG/subnet/HA configuration |
| Delivery | ECR push, ECS redeploy, S3 sync, invalidation | Stability gates, automatic rollback, task revisions |
| Monitoring | Console/Morgan and awslogs | Tracing, custom metrics, alarms/SLOs |
| Security | IAM/secret references, iframe sandbox | WAF, complete guardrails, verified image exclusions |
| Scale | Separate services and external data | Autoscaling, 10,000-user capacity, multi-region DR |

## Why Questions

These are defensible design explanations, not claims about undocumented personal decisions or benchmarks.

### Why this project?

It demonstrates the whole product path: identity, AI selection, provider calls, persistence, generated files, payments and deployment. A strong portfolio discussion connects those boundaries instead of stopping at a model API call.

### Why Agentic AI?

Different intents trigger different tool workflows. Search-to-Chat is a clear example of retrieval followed by synthesis. Call it bounded agentic orchestration, not autonomous planning.

### Why LangGraph?

It makes state and transitions explicit. A plain switch could handle this scale, but graph nodes and conditional edges make the workflow easier to inspect and extend. Durability does not appear automatically; it would require checkpoint configuration.

### Why multiple agents?

Code JSON, slide JSON, image binary and document retrieval require distinct prompts and post-processing. Specialists localize those concerns. They do not create independent runtime failure domains because they share one process.

### Why microservices?

Identity, messages, AI and payments have different responsibilities and dependency sets. Separate services permit independent changes. The cost is five deployments and network failure modes; a modular monolith would be a reasonable smaller starting point. Admin database access and synchronous calls limit isolation today.

### Why Node.js?

The implementation uses JavaScript on both sides and integrates HTTP APIs naturally. PDF parsing and file processing can still consume CPU/memory or block the event loop. Async syntax is not a guarantee that heavy work is nonblocking.

### Why React?

The UI has shared account, conversation and result state, reusable components and client-side routes. Redux centralizes updates. React itself does not secure API access or store durable messages.

### Why Docker?

It packages the runtime and dependencies used by ECS. The project benefits from consistent startup commands, but reproducibility still needs pinned artifacts, lockfile installs and clean build contexts.

### Why AWS?

The deployment uses managed container hosting, object storage, CDN, discovery, roles/secrets and logs. AWS hosts the application; model inference currently comes from external APIs.

### Why ECS Fargate?

It matches the existing service containers without requiring host OS administration. Task definitions express resources, ports and roles. It does not remove application operations, networking or reliability design.

### Why not EC2?

EC2 would add host patching, capacity management and placement responsibilities. It may be appropriate with measured steady utilization or host requirements; there is no benchmark proving Fargate is always cheaper.

### Why not EKS?

The current five-service design has no demonstrated need for Kubernetes APIs or operators. EKS would add cluster operations. Consider it when organizational requirements justify that complexity, not to add another logo.

### Why ALB?

The guide uses it as an HTTP entry to the Gateway task IPs with health-based routing. HTTPS listener/certificate configuration remains deployment-specific; ALB does not replace application authorization.

### Why CloudFront?

It delivers the static frontend and supports cache invalidation on deployment. It is separate from model processing. A CDN does not automatically accelerate a synchronous provider call.

### Why Redis/ElastiCache?

Sessions and rate counters need quick lookups and expiry semantics; memory caching avoids repeated history reads. ElastiCache supplies a managed endpoint, but replication/failover must be configured. It is also a critical dependency.

### Why S3?

Generated binaries need durable storage and direct download links. S3 separates download traffic from the Agent response. Code artifacts can remain in MongoDB. Bucket privacy, lifecycle and expiry still need explicit verification.

### Why MongoDB?

Messages, artifacts and profiles fit document-shaped models, and the code uses Mongoose. Credit updates still require transactional/atomic design; flexible schema does not solve payment consistency.

### Why these model providers?

Groq serves general text/routing, DeepSeek via OpenRouter supplies the configured coding model, Gemini handles image input and embeddings, Stability generates images, and Tavily supplies search. This is functional separation; no measured model superiority or current free-tier claim is established. Provider comparisons should use an evaluation set.

### Why this RAG design?

Per-upload parsing/indexing is simple to demonstrate and avoids requiring a permanent knowledge-base UI. Its trade-off is repeated embedding cost, collection growth and no persistent follow-up retrieval. Production work should separate ingestion from authorized retrieval.

## Interview Question Bank and Cross-Questions

Start with the short answer. Add the follow-up detail when asked; do not recite every caveat in your opening pitch.

### 1. What is the strongest technical contribution here?

**Answer:** The repository connects a frontend, identity verification, session-based APIs, specialized AI workflows, persistence, payments and container deployment. The strongest design story is how a request moves through those boundaries. Describe your own contribution only for work you actually performed.

**Follow-up:** What proves these are integrated rather than separate demos?

**Follow-up answer:** Agent persists messages through Chat, invokes the graph, updates memory and returns artifacts to React. Agents also call Auth for credit deduction. These connections demonstrate integration; successful live deployment requires separate evidence.

### 2. What exactly happens after the user clicks Send?

**Answer:** The UI creates a conversation when needed and posts the prompt, selected agent and optional file to `/api/agent/chat`. The gateway resolves the Redis session and forwards the user identity. Agent saves the prompt, runs the graph, stores the result and returns JSON for the UI.

**Follow-up:** Is the response streamed?

**Follow-up answer:** No. The controller awaits `graph.invoke`. Streaming needs coordinated changes to graph execution, the HTTP response, gateway and frontend, including handling partial messages and disconnections.

### 3. How does LangGraph know which agent to select?

**Answer:** Explicit selection comes first. In Auto mode the router checks PDF and image MIME types, then asks Groq to classify text requests. Conditional edges map labels to specialist nodes; an unknown label routes to chat.

**Follow-up:** Can a PDF override an explicit Coding selection?

**Follow-up answer:** No. Explicit selection wins. Router exceptions are also different from unknown labels: there is no general router-exception fallback.

### 4. Is this an autonomous team of agents?

**Answer:** It is a routed set of specialized workflows inside one Agent service: eight specialists plus a router. Most requests run one specialist; search runs search and then chat.

**Follow-up:** Where are planning, reflection and parallel collaboration?

**Follow-up answer:** They are not implemented. The value here is explicit routing and shared workflow state. More complex coordination should be added only when its benefits justify extra latency, cost and failure modes.

### 5. Is LangGraph state durable?

**Answer:** State carries the prompt, agent, conversation/user IDs, file, answer, search results, images and artifacts during an invocation. The graph is compiled without a checkpointer.

**Follow-up:** Does Redis memory let a failed graph resume?

**Follow-up answer:** No. Conversation history is different from an execution checkpoint. Retrying starts another request and may repeat provider calls, writes or credit operations unless those effects become idempotent.

### 6. What happens if an agent fails?

**Answer:** Many agents catch errors and return fallback text, so failure can still produce HTTP 200. Other errors propagate to Express. The generic error middleware path itself contains an undefined-variable defect.

**Follow-up:** How would you improve it?

**Follow-up answer:** Define typed errors and a consistent response contract, propagate request IDs and distinguish retryable dependency failures from invalid input. Credit handling should follow a defined successful operation rather than fallback text.

### 7. What happens if an LLM API times out?

**Answer:** There is no application-wide deadline, retry and cancellation policy across providers. SDK or HTTP errors reach the selected agent's error handling. I would not promise an automatic retry or fallback model.

**Follow-up:** Would you retry every failure?

**Follow-up answer:** No. Retry appropriate transient errors with backoff and jitter inside a bounded deadline. Do not blindly retry invalid credentials or input. Repeated operations must not duplicate charges or artifacts.

### 8. Why did you not use Lambda?

**Answer:** The backend is five persistent Express services with HTTP dependencies and file processing. Fargate deploys this container model directly. Lambda could suit selected event-driven jobs, but migrating the application requires evaluating duration, concurrency and database connections.

**Follow-up:** Where could Lambda fit later?

**Follow-up answer:** A bounded asynchronous cleanup or ingestion step could be a candidate after measuring the workload. Neither option is universally cheaper or better.

### 9. Why ECS instead of EKS?

**Answer:** These services need scheduling, networking, discovery and deployment. ECS provides that without operating Kubernetes. EKS would need a concrete ecosystem or organizational requirement to justify its complexity here.

**Follow-up:** Does Fargate remove operations work?

**Follow-up answer:** No. Image maintenance, task sizing, IAM, networking, health checks, deployment and dependency failures remain application responsibilities.

### 10. What happens if an ECS container crashes?

**Answer:** An ECS service attempts to maintain its configured desired count by replacing stopped tasks. That does not preserve an in-flight graph or temporary file. One replica can leave the service unavailable during replacement.

**Follow-up:** Is replacement the same as high availability?

**Follow-up answer:** No. HA needs healthy replicas across failure domains and resilient dependencies. The deployment instructions use one task per service and do not prove live HA.

### 11. How does ALB know a container is healthy?

**Answer:** Target-group health checks call a configured path and port. The guide uses `/`, but a root response does not prove MongoDB, Redis or providers work. The committed task definitions do not add container health checks.

**Follow-up:** What would you add?

**Follow-up answer:** Separate liveness from readiness. Readiness should check critical dependencies with bounded checks without making every optional provider outage disable the whole service.

### 12. How are containers communicating?

**Answer:** HTTP calls use Cloud Map names such as `novamind-auth.novamind.local` and service ports. ALB fronts the gateway for external API traffic. Security groups must permit intended internal traffic.

**Follow-up:** Is discovery also authentication?

**Follow-up answer:** No. DNS locates a service; it does not establish the caller's identity. Trusted identity headers and publicly reachable proxy paths require explicit authorization controls.

### 13. Where are your secrets stored?

**Answer:** Several task definitions reference Secrets Manager; local development uses environment variables. Auth's task definition also contains credential-bearing database URIs in plain environment entries, so secret handling is incomplete.

**Follow-up:** How would you correct that?

**Follow-up answer:** Move sensitive values to managed secrets, rotate exposed credentials and review history and build artifacts. Grant narrowly scoped access and never display the existing values during an interview.

### 14. How do you prevent secrets from entering Docker images?

**Answer:** The current setup does not provide sufficient assurance. Builds use `backend` as context, while ignore files sit inside service directories. Those nested files do not automatically filter the parent context; local environment files could be copied.

**Follow-up:** What does a reliable fix include?

**Follow-up answer:** An effective context-level or Dockerfile-specific ignore file, runtime secret injection and image inspection/scanning. `.gitignore` controls Git tracking, not Docker copying.

### 15. What is the difference between execution role and task role?

**Answer:** The execution role supports ECS operations such as pulling images, configured logging and injected secret retrieval. A task role grants permissions used by container code, such as Agent's S3 calls. Referenced roles do not establish their deployed permission scope.

**Follow-up:** Can you claim least privilege?

**Follow-up answer:** Only after inspecting actual policies and resource restrictions. A role reference proves configuration, not minimal permissions.

### 16. What happens if Redis goes down?

**Answer:** Protected gateway requests depend on Redis sessions, so access can fail while MongoDB and providers remain healthy. Agent memory and rate limiting also depend on Redis. A tested degraded mode is not implemented.

**Follow-up:** Should authentication be bypassed?

**Follow-up answer:** No. Return a clear temporary failure and improve dependency availability. Optional history caching can have a separately designed fallback; session validation must remain enforced.

### 17. Does memory always expire after 24 hours and stay below 20 messages?

**Answer:** No. Hydration sets a TTL, but later `SET` calls do not preserve it. Trimming removes only one item, so oversized hydrated history may remain oversized. Concurrent read-modify-write updates can lose messages.

**Follow-up:** What would you change?

**Follow-up answer:** Define the TTL policy, atomically append/trim, load bounded history and avoid duplicating the current prompt after it has already been persisted.

### 18. How would this handle 10,000 users?

**Answer:** First distinguish registered users from concurrent requests and define request mix and latency targets. There is no load-test evidence for this capacity. Measure gateway throughput, agent concurrency, database pools, Redis and provider quotas.

**Follow-up:** What would you scale first?

**Follow-up answer:** The measured bottleneck. Long jobs may need queues and concurrency control. More Agent tasks alone can exhaust provider quotas, and shared credit/state correctness must survive concurrency.

### 19. How would you troubleshoot an ALB 502?

**Answer:** Correlate the request timestamp with target health, gateway logs and ECS events. Determine whether the gateway restarted, closed a connection or returned an invalid response. Compare internal gateway behavior with ALB traffic.

**Follow-up:** Does healthy target status rule out an application problem?

**Follow-up answer:** No. A root health check can succeed while real requests fail. Diagnose the failing route and connection rather than treating health status as proof of end-to-end success.

### 20. How does PDF RAG work here?

**Answer:** Auto routes PDFs to parsing, 1,000-character chunks with 200 overlap, Gemini embeddings and a new Qdrant collection. The current question retrieves five chunks; Groq answers from that context. The temporary upload is removed.

**Follow-up:** Can a later question retrieve the PDF without another upload?

**Follow-up answer:** No persistent document-to-collection lookup is implemented. Conversation history may inform a text answer, but that is not fresh PDF retrieval.

### 21. How do you prevent hallucination?

**Answer:** RAG supplies context and instructions to answer from it, but cannot guarantee correctness. This project lacks verified citations and grounding evaluation. Say it aims to reduce unsupported answers, not eliminate hallucination.

**Follow-up:** What if the document does not answer the question?

**Follow-up answer:** The system should abstain. Reliable abstention needs retrieval relevance checks and evaluation of model behavior; it is not a verified guarantee today.

### 22. How do you evaluate RAG quality?

**Answer:** No evaluation suite is committed. I would label questions and supporting passages, including unanswerable examples, then measure retrieval coverage, faithfulness, correctness, latency and cost separately.

**Follow-up:** Would increasing top-k always help?

**Follow-up answer:** No. More chunks can introduce irrelevant context and cost. Compare chunking, top-k and reranking on the same evaluation set.

### 23. Why several providers, and can startup use only one key?

**Answer:** Providers supply different functions, but add credential, quota and failure dependencies. Clients are constructed eagerly, and SDK initialization can validate credentials before any request. Startup may therefore need more than the selected agent's key.

**Follow-up:** Is this the optimal provider mix?

**Follow-up answer:** No benchmark establishes that. Evaluate quality, latency, cost and operational requirements; consider lazy initialization and explicit configuration validation.

### 24. Is generated code executed on the server?

**Answer:** No. Coding returns Markdown or project files. React displays a read-only editor and can preview HTML/CSS/JavaScript in a sandboxed iframe. There is no server build/test execution service.

**Follow-up:** Does a preview prove correctness?

**Follow-up answer:** No. A future execution service would require isolation, resource limits and controlled networking, plus actual validation of dependencies and files.

### 25. Are microservices completely data-isolated?

**Answer:** Auth, Chat and Billing have their own models/connections, but Auth's admin controller directly connects to Chat and Billing databases. That couples administration to their schemas and credentials.

**Follow-up:** How would you improve boundaries?

**Follow-up answer:** Service-owned admin APIs or a reporting read model could replace direct cross-database reads, at the cost of additional coordination.

### 26. Are payments and credits safe under retries?

**Answer:** Not fully. Credit updates can race. Payment verification checks an HMAC but lacks requester ownership and idempotent completion, and saves payment state before updating Auth. Credit helpers also swallow some errors.

**Follow-up:** What is the production design?

**Follow-up answer:** Bind orders to users, process each payment once, use atomic balance operations and maintain a durable ledger with recovery/reconciliation across services.

### 27. Is billing a recurring subscription system?

**Answer:** It creates Razorpay orders and applies plan/credit updates. Expiry fields exist, but a complete recurring subscription lifecycle and consistent expiry enforcement do not. Describe it as payment-backed plan and credit management.

**Follow-up:** What about insufficient credits?

**Follow-up answer:** Provider work can happen before deduction, and credit-helper failures can be swallowed. Define reservation, settlement and refund behavior before production.

### 28. What is the biggest limitation before production?

**Answer:** Authorization and payment correctness come before throughput. Conversation operations lack ownership checks, and the public Auth proxy exposes routes that trust identity headers. Payment verification needs replay and ownership protection.

**Follow-up:** What would you fix first?

**Follow-up answer:** Close unintended public routes, enforce identity and resource ownership, make payments idempotent, then repair secret and session/logout handling before expanding access.

### 29. Does CORS or the frontend admin route secure the API?

**Answer:** No. CORS controls browser cross-origin access, and the frontend route controls navigation. Neither replaces server authentication and authorization. Credentialed cookies also require careful origin, cookie and CSRF design.

**Follow-up:** What is the specific boundary problem here?

**Follow-up answer:** Public Auth proxy routes can reach handlers that rely on trusted user headers. Every sensitive operation needs server-enforced authorization independently of the UI.

### 30. What monitoring is implemented?

**Answer:** Task definitions configure `awslogs`; the application has console logs and gateway request logging. Tracing, dashboards and alarm coverage are not established by the repository.

**Follow-up:** What would you add first?

**Follow-up answer:** Request IDs, route/agent latency and error metrics, dependency failures, task restarts, provider usage and billing reconciliation alerts. Remove sensitive token/session logging.

### 31. What does CI/CD guarantee, and how do you roll back?

**Answer:** Pushes to main build/push five images, force ECS deployments and publish the frontend. The workflow does not wait for ECS stability or run application tests, so completion does not prove runtime health.

**Follow-up:** Is `latest` enough for rollback?

**Follow-up answer:** No. Use immutable tags/digests and versioned task revisions, deploy a known-good revision and verify stability. Mutable tags weaken source-to-runtime traceability.

### 32. Are containers stateless?

**Answer:** Durable data mainly lives in MongoDB/S3, with Redis for sessions and cached state. In-memory graph execution and local temporary files still disappear on task termination.

**Follow-up:** How would document jobs survive crashes?

**Follow-up answer:** Durable authorized uploads, queued jobs, persisted status and idempotent workers. These are proposed improvements, not the current synchronous workflow.

### 33. How would you reduce cost?

**Answer:** Measure provider usage, repeated embeddings, task utilization, NAT traffic and storage growth. Reuse authorized indexes, apply retention, right-size tasks and set budgets. Do not invent monthly costs without billing/workload data.

**Follow-up:** Would removing NAT always help?

**Follow-up answer:** External SaaS calls still need outbound connectivity. Evaluate AWS endpoints separately from internet-bound traffic and consider availability as well as cost.

### 34. How would you make it multi-region?

**Answer:** Start with recovery-time and recovery-point objectives, then design regional stacks, failover, artifact replication and database recovery. Sessions, vector indexes and payment processing also require a plan. This is future work.

**Follow-up:** Why not immediately use active-active?

**Follow-up answer:** It adds write conflicts and duplicate-processing risks, especially for credits. Tested backup/restore or warm standby may meet the requirement with less complexity.

### 35. What evidence would you bring to an interview?

**Answer:** Show the graph, request controller, task definitions and workflow. Bring sanitized runtime evidence only if personally verified. Repository configuration does not prove uptime, scale or production success.

**Follow-up:** How would you answer a behavioral outage question?

**Follow-up answer:** Describe an incident only if it actually happened to you. Otherwise explain the investigation approach as a hypothetical scenario rather than personal history.

## Troubleshooting Interview Scenarios

These are investigation exercises, not claims of past incidents. Root causes remain candidates until evidence confirms them. Additional metrics or access logs may need enabling; do not imply they already exist.

### 1. ECS task unhealthy

- **Symptoms:** Failed health checks, unsettled deployment or intermittent failures.
- **Investigation:** Inspect service events and target-health reasons; compare the target port/path with the listener and inspect startup.
- **Logs/metrics:** ECS stopped reason, exit code, `/ecs/novamind-*` logs and ALB healthy/unhealthy target counts.
- **Possible causes:** Wrong port, security-group rule, startup exception or unsuitable health-check timing. A successful root response can also hide dependency failures.
- **Fix:** Correct the confirmed configuration/process issue and validate a real authenticated request.
- **Prevention:** Meaningful readiness/container checks, measured startup allowance and CI service-stability checks.

### 2. ALB 502

- **Symptoms:** Frontend loads but API requests return 502.
- **Investigation:** Determine whether ALB or an application proxy generated the error; correlate timestamps with gateway restarts, target health and upstream failures.
- **Logs/metrics:** ALB/target 5xx metrics, access logs if enabled, gateway logs and ECS events.
- **Possible causes:** Connection closed mid-request, gateway crash, malformed response or upstream proxy failure. Distinguish timeouts from other failures.
- **Fix:** Repair the specific connection/process/proxy fault and retest the same route; change timeouts only with evidence.
- **Prevention:** Graceful shutdown, request deadlines, stable deployments and route-level monitoring.

### 3. ECR image pull failure

- **Symptoms:** Replacement tasks cannot start and report image-pull errors.
- **Investigation:** Verify the image URI/tag exists in the expected region, then inspect execution-role permissions and outbound connectivity.
- **Logs/metrics:** Service events and stopped-task reason; CloudTrail authorization events where available. Application logs may not exist yet.
- **Possible causes:** Missing image, incorrect URI, denied pull or unavailable network path.
- **Fix:** Reference the correct image and repair the confirmed IAM/network issue, then redeploy.
- **Prevention:** Immutable image references, pre-deployment image checks and validated role/network configuration.

### 4. Redis connectivity problem

- **Symptoms:** Session validation fails or agents error during memory/rate checks.
- **Investigation:** Identify the client; verify endpoint, port, transport/authentication requirements and task-to-Redis reachability.
- **Logs/metrics:** Gateway/Auth/Agent Redis errors and available ElastiCache connection, CPU, memory and failover signals.
- **Possible causes:** Incorrect endpoint, blocked traffic, configuration mismatch, exhaustion or service interruption.
- **Fix:** Restore the confirmed connectivity/configuration issue without bypassing authentication.
- **Prevention:** Tested failover where required, bounded retries, capacity alerts and separate policies for sessions versus optional caching.

### 5. Database connectivity problem

- **Symptoms:** Login, history, payments or admin queries fail while the process may still answer `/`.
- **Investigation:** Identify the service/database, check secret mapping without printing credentials, then inspect network access and connection pools.
- **Logs/metrics:** Mongoose errors, database monitoring and ECS startup logs.
- **Possible causes:** Invalid credentials, access restrictions, unavailable database or exhausted connections. Listening before database readiness can mask failure.
- **Fix:** Repair the connection and confirm the affected read/write, not just a root response.
- **Prevention:** Readiness, safe rotation, connection budgets and appropriate database availability/backups.

### 6. CORS error

- **Symptoms:** Browser blocks a response or subsequent requests lack a usable login session.
- **Investigation:** Inspect URL, OPTIONS response, origin and cookie behavior; compare `VITE_SERVER_URL`, `FRONTEND_URL` and production cookie settings.
- **Logs/metrics:** Browser Network panel, cookie rejection details and gateway logs; backend failures can also appear as CORS symptoms.
- **Possible causes:** Wrong build-time URL, origin mismatch, HTTPS/cookie mismatch or failed preflight.
- **Fix:** Correct the exact configuration and rebuild if Vite values changed; retest credentialed requests.
- **Prevention:** Environment validation and a browser login-to-chat smoke test. Do not allow arbitrary origins to solve credentialed CORS.

### 7. Secrets Manager permission error

- **Symptoms:** Task initialization fails or a required runtime value is unavailable.
- **Investigation:** Check secret reference, region and role; distinguish ECS injection through the execution role from code's task-role calls.
- **Logs/metrics:** ECS initialization/stopped errors and relevant CloudTrail denied calls.
- **Possible causes:** Wrong ARN, missing secret-read/applicable KMS permission or network failure.
- **Fix:** Correct the reference or narrowly scoped permission/network issue and start replacement tasks.
- **Prevention:** Validate mappings before deployment, rotate deliberately and keep secret values out of logs/plain environment entries.

### 8. LLM timeout

- **Symptoms:** Long spinner, failed response or fallback text.
- **Investigation:** Identify agent/provider and request size; compare provider timing/quota errors with client and gateway behavior.
- **Logs/metrics:** Agent exceptions, provider usage/errors and duration metrics if added.
- **Possible causes:** Provider degradation, quota pressure, large input or unavailable outbound access.
- **Fix:** Correct confirmed configuration/network issues; otherwise report a useful temporary failure and retry only appropriate transient errors within a deadline.
- **Prevention:** Explicit time budgets, cancellation, concurrency limits, provider monitoring and asynchronous long jobs.

### 9. Agent failure

- **Symptoms:** Missing artifact, fallback text or errors while another agent works.
- **Investigation:** Confirm router choice, then isolate model call, JSON parsing, generation, upload, persistence and credit update.
- **Logs/metrics:** Agent/provider errors, Chat/Auth logs and S3 error details for upload failures.
- **Possible causes:** Invalid model JSON, missing key, file-processing error, denied S3 write or an exception outside the catch block.
- **Fix:** Repair the failed stage and report its outcome accurately; avoid retries that duplicate side effects.
- **Prevention:** Structured-output validation, representative agent tests, typed errors, idempotency and corrected error middleware.

### 10. RAG returns irrelevant results

- **Symptoms:** Unrelated answer, missing document facts or unsupported PDF follow-up answer.
- **Investigation:** Confirm Auto selected `pdfRag`; inspect extraction and retrieved chunks. Distinguish a new upload from text-only follow-up.
- **Logs/metrics:** Sanitized retrieval diagnostics if added, labeled examples, Qdrant and embedding errors. Avoid logging private document text by default.
- **Possible causes:** Scanned PDF without OCR, poor extraction/chunking, irrelevant top-five retrieval or no persistent collection lookup.
- **Fix:** Correct extraction/retrieval; implement authorized document mapping for durable follow-ups. A prompt change alone cannot repair missing retrieval.
- **Prevention:** Evaluation set, source/page metadata, relevance checks, abstention and index lifecycle management.

### 11. Repeated container restarts in CloudWatch

- **Symptoms:** Startup logs repeat and ECS repeatedly replaces tasks.
- **Investigation:** Correlate streams with task IDs/deployments; check stopped reason, exit code, memory and initialization.
- **Logs/metrics:** ECS events, stopped-task details, application logs and CPU/memory metrics.
- **Possible causes:** Startup exception, missing eagerly validated model credentials, document-processing memory pressure, failed health checks or repeated deployments.
- **Fix:** Resolve the observed exception/configuration problem, measured resource shortage or deployment issue; use a known-good revision when available.
- **Prevention:** Startup validation, concurrency/memory limits, representative document tests and service-stability checks. More memory is not a universal fix.

## Documentation Corrections and Evidence Boundaries

Reuse the architecture poster with this guide's qualifications: a diagram or deployment instruction does not prove that every feature is enabled in AWS.

- **Agent count:** Eight specialists plus the router; search continues into chat.
- **Upload routing:** Explicit selection wins; file MIME routing applies in Auto.
- **PDF follow-ups:** No persistent collection lookup or verified citations.
- **Memory:** Hydration TTL is lost on later writes; trimming is not a strict cap after large hydration.
- **Download expiry:** PDF/generated-image URLs use 1,440 seconds; PPT uses 86,400 seconds. Some user-facing labels disagree.
- **Containers:** Single-stage builds; nested ignore files do not filter the parent build context.
- **Secrets:** Managed references coexist with credential-bearing Auth environment entries.
- **Payments:** Signature verification does not establish ownership, replay protection or atomic credit grants.
- **Data boundaries:** Auth administration directly accesses Chat/Billing databases.
- **Failure reporting:** Fallback text can return HTTP 200; generic error middleware also needs repair.
- **Availability:** Subnet layout does not prove replica redundancy, autoscaling or live HA.
- **Deployment:** CI forces updates without tests or a service-stability gate.
- **Performance:** No benchmark establishes claimed latency, provider superiority or production capacity.

### Evidence to revisit before an interview

Use [README](README.md), the [existing poster](new-project-pic/novamind-aws-architecture-poster.png), [architecture notes](Architecture.md) and [deployment workflow](.github/workflows/deploy.yml) as orientation. The technical sections above link implementation files for the detailed claims. Treat source/configuration as evidence of implementation intent and behavior, and live observations as separate evidence of successful operation.

### Questions to ask the interviewer

- How does your team evaluate grounded answers and abstention?
- Which failure and recovery objectives matter most for AI workloads?
- How do you manage provider budgets, quotas and document retention?
- What evidence is required before promoting an AI workflow to production?

# 10-Minute Interview Revision Sheet

**Project in one sentence:** NovaMind AI combines chat, coding, search, document and image tasks in a React/Node.js application, using specialized LangGraph workflows and an AWS container deployment design.

**Problem solved:** One interface integrates several AI tasks with identity, history, artifacts and payment-backed credits.

**Architecture in one sentence:** CloudFront/S3 serves React; ALB fronts the gateway; ECS services handle identity, chat, agents and billing; providers, MongoDB, Redis, Qdrant and S3 supply AI and data functions.

- **Frontend:** React, Vite, Redux, Axios, Firebase sign-in and artifact rendering.
- **Backend:** Gateway, Auth, Chat, Agent, Billing; ports 8000–8004.
- **LangGraph:** Explicit selection → Auto MIME checks → text classification. Conditional edges; no durable checkpointer.
- **Agents:** Chat, search, coding, PDF generation, PPT generation, image generation (`vision`), PDF RAG, image analysis.
- **RAG:** PDF text → 1,000-character chunks/200 overlap → Gemini embeddings → new Qdrant collection → top five → Groq. No persistent follow-up lookup.
- **AWS:** S3, CloudFront, ALB, ECS/Fargate, ECR, Cloud Map, ElastiCache, Secrets Manager, IAM, CloudWatch; verify live settings separately.
- **Request:** UI → session-checked gateway → Agent → save prompt → graph/provider → persistence → JSON → UI.
- **Deployment:** Main push → five images → ECR → ECS update → frontend build → S3 → CloudFront invalidation; no stability gate.
- **Security:** Firebase verification and Redis cookie sessions; authorization, payments, secrets and logout need fixes.
- **Networking:** Documented public ALB/private tasks, internal Cloud Map HTTP and outbound SaaS access; not proof of HA.
- **Monitoring:** ECS/application logs; tracing and alarms not established.
- **Scaling:** Independent scaling is possible; policies and tested capacity are not demonstrated.

**Five design decisions:** (1) One UI with specialists. (2) LangGraph routing. (3) Five containerized services. (4) Redis sessions/rate counters/memory. (5) S3 artifacts and Qdrant retrieval.

**Five strongest points:** (1) Traceable frontend-to-agent integration. (2) Eight specialist workflows. (3) Embedding/retrieval pipeline. (4) Artifact storage/rendering. (5) Docker, ECS and CI/CD configuration.

**Five limitations:** (1) Authorization gaps. (2) Payment/credit concurrency and replay. (3) No persistent PDF retrieval. (4) Synchronous jobs without durable recovery. (5) Unverified HA/capacity and incomplete observability.

**Five improvements:** (1) Fix authorization/secrets/sessions. (2) Make payments/credits atomic and recoverable. (3) Persist authorized document indexes and evaluate RAG. (4) Add durable jobs, deadlines and idempotency. (5) Add tests, immutable deployment, readiness, monitoring and measured scaling.

**Likely questions:** What happens after Send? Why LangGraph and ECS? How does routing work? What if Redis/provider fails? Can PDF follow-ups retrieve the file? How do you evaluate RAG? Is billing retry-safe? What changes before production?

**Speaking reminder:** Distinguish implemented code, deployment guidance and verified runtime behavior. Never invent a personal incident, benchmark or production guarantee.
