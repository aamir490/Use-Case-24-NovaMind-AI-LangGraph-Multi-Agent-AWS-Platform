**PROJECT ANALYSIS REPORT — NovaMind AI**

**Scope:** Read-only analysis of `E:\GenAi-Project-Cloudage\1.cortexAI`.

I inspected application source, configuration, service relationships, Dockerfiles, deployment workflow, ECS task definitions, documentation, and important architecture/application/AWS screenshots. I did not run the application, invoke providers, test payments, access live AWS resources, install packages, or change files. The existing untracked files remained unchanged.

“Implemented” below means supported by source or configuration. It does **not** mean successfully tested during this review.

---

**1. Executive summary**

NovaMind AI is a web application that combines several AI tasks behind one interface:

- General conversation.
- Web search and answer synthesis.
- Code generation, review, and explanation.
- PDF and PowerPoint generation.
- Image generation.
- Questions about an uploaded PDF.
- Analysis of an uploaded image.

It includes Google sign-in, conversation history, usage credits, Razorpay payment integration, and administration screens.

The actual architecture contains a React frontend and **five separately containerized Express services**: Gateway, Auth, Chat, Agent, and Billing. The Agent service contains **eight specialist workflows plus a router**, implemented with LangGraph.

**RAG is genuinely implemented.** Uploaded PDF text is extracted, split, embedded with Gemini, stored in Qdrant, retrieved through similarity search, and supplied to Groq for answering.

**LangGraph is genuinely implemented.** However, its graph is a bounded routing workflow. It does not implement an autonomous planner, iterative tool-selection loop, reflection loop, or durable graph execution.

**AWS deployment configuration is substantial:** Dockerfiles, Fargate task definitions, ECR publishing, ECS redeployment, S3 frontend upload, CloudFront invalidation, Secrets Manager references, and CloudWatch logging configuration exist. Network provisioning is primarily documented rather than defined through comprehensive infrastructure as code.

**Maturity assessment:** An integrated portfolio application with meaningful breadth and demonstrable engineering concepts. It is **not defensibly production-ready** in its current form.

The most important weaknesses are:

1. Publicly reachable account/credit mutation routes.
2. An alternate route to admin handlers that undermines the intended authentication boundary.
3. Missing conversation ownership checks.
4. Non-idempotent payments and unreliable credit enforcement.
5. Credential exposure in tracked configuration.
6. Inconsistent failures, session invalidation, and memory behavior.
7. No substantive automated test or AI evaluation suite.
8. Deployment automation without release-health gates.

These weaknesses should become part of your technical explanation, not something concealed behind architecture terminology.

---

**2. Evidence map**

The following references identify the main implementation evidence. Later sections use these labels to avoid repeating long paths.

- **E1 — Frontend entry and routing:** [main.jsx](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/main.jsx), [App.jsx](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/App.jsx), [Home.jsx](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/pages/Home.jsx).
- **E2 — Request construction:** [ChatInput.jsx](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/components/ChatInput.jsx:44), [sendMessage.js](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/features/sendMessage.js), [Axios configuration](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/utils/axios.js).
- **E3 — Gateway boundary:** [Gateway entry](E:/GenAi-Project-Cloudage/1.cortexAI/backend/gateway/index.js:14), [session middleware](E:/GenAi-Project-Cloudage/1.cortexAI/backend/gateway/middleware/auth.middleware.js), [identity forwarding](E:/GenAi-Project-Cloudage/1.cortexAI/backend/gateway/utils/proxyWithHeader.js).
- **E4 — Authentication and credits:** [Auth controller](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth/controllers/auth.controller.js), [Auth routes](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth/routes/auth.route.js), [Auth entry](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth/index.js), [Firebase initialization](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth/config/firebase.js).
- **E5 — Administration:** [admin middleware](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth/middleware/admin.middleware.js), [admin routes](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth/routes/admin.route.js), [admin controller](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth/controllers/admin.controller.js), [AdminPage.jsx](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/pages/AdminPage.jsx).
- **E6 — Conversations and messages:** [Chat controller](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/chat/controllers/chat.controller.js), [Chat routes](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/chat/routes/chat.routes.js), [conversation model](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/chat/models/coversation.model.js), [message model](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/chat/models/message.model.js).
- **E7 — Agent entry:** [Agent controller](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/controllers/agent.controller.js), [upload route](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/routes/agent.route.js), [Agent entry/error middleware](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/index.js).
- **E8 — LangGraph:** [graph](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/graph/graph.js), [router](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/graph/router.js), [state](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/graph/state.js).
- **E9 — Models:** [model selection](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/llmModels.js), [embedding model](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/embeddings.js).
- **E10 — Chat and search:** [chat agent](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/chat.agent.js), [search agent](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/search.agent.js), [Tavily configuration](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/tavily.js).
- **E11 — PDF RAG:** [PDF RAG agent](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/pdfRag.agent.js), [Qdrant integration](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/vectorDb.js).
- **E12 — Coding:** [coding agent](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/coding.agent.js), [artifact viewer](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/components/Artifact.jsx).
- **E13 — Document generation:** [PDF agent](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/pdf.agent.js), [PPT agent](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/ppt.agent.js), [PDF renderer](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/utils/generatePdf.js), [PPT renderer](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/utils/generatePpt.js).
- **E14 — Images:** [image generation](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/vision.agent.js), [image analysis](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/agents/imageAnalyzer.agent.js).
- **E15 — Memory and limits:** [memory](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/memory.js), [rate limits](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/agentLimit.js), [shared Redis client](E:/GenAi-Project-Cloudage/1.cortexAI/backend/shared/redis/redis.js), [credit helper](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/utils/deductCredits.js).
- **E16 — Uploads and S3:** [Multer configuration](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/multer.js), [S3 client](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/config/s3.js), [upload helper](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/utils/uploadToS3.js), [presigning helper](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/utils/getFromS3.js).
- **E17 — Billing:** [Billing controller](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/billing/controllers/billing.controller.js), [plans](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/billing/config/Plans.js), [payment model](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/billing/models/payment.model.js), [BillingDrawer.jsx](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src/components/BillingDrawer.jsx).
- **E18 — Delivery:** [GitHub Actions workflow](E:/GenAi-Project-Cloudage/1.cortexAI/.github/workflows/deploy.yml), [Agent Dockerfile](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent/Dockerfile), [local Compose](E:/GenAi-Project-Cloudage/1.cortexAI/backend/docker-compose.yml).
- **E19 — AWS task configuration:** [Gateway](E:/GenAi-Project-Cloudage/1.cortexAI/task-defs/gateway.json), [Auth](E:/GenAi-Project-Cloudage/1.cortexAI/task-defs/auth.json), [Chat](E:/GenAi-Project-Cloudage/1.cortexAI/task-defs/chat.json), [Agent](E:/GenAi-Project-Cloudage/1.cortexAI/task-defs/agent.json), [Billing](E:/GenAi-Project-Cloudage/1.cortexAI/task-defs/billing.json).
- **E20 — Documentation:** [README](E:/GenAi-Project-Cloudage/1.cortexAI/README.md), [architecture](E:/GenAi-Project-Cloudage/1.cortexAI/architecture.md), [interview guide](E:/GenAi-Project-Cloudage/1.cortexAI/interview.md), [AWS deployment guide](E:/GenAi-Project-Cloudage/1.cortexAI/deploy-guide-aws-original.md), [archived README](E:/GenAi-Project-Cloudage/1.cortexAI/archive-files/README.md).

---

**3. Project overview and implementation classification**

**Problem addressed**

The application brings several AI tasks into one workspace with a shared account, conversation interface, history, and billing mechanism.

This is supported by its feature integration. The repository does not establish customer interviews, business adoption, measured productivity gains, or commercial revenue.

**Target users**

The feature set reasonably targets learners, developers, researchers, and people creating documents or images. This is an interpretation of the product capabilities, not verified market research.

**IMPLEMENTED**

- React application and Redux state.
- Google authentication through Firebase.
- Redis-backed session creation and lookup.
- Five Express services.
- LangGraph routing and eight specialists.
- PDF extraction, chunking, embedding, vector storage, and retrieval.
- Tavily web search followed by Groq synthesis.
- Code artifacts and browser preview.
- PDF/PPT rendering and S3 upload.
- Stability image generation.
- Gemini image analysis.
- MongoDB conversations, users, and payment records.
- Payment signature checking.
- Basic per-user rate counters.
- Docker/ECS/deployment workflow definitions.

**PARTIAL**

- Authorization and tenant isolation.
- Credit-based usage enforcement.
- Payment processing consistency.
- Session revocation.
- Chat memory limits and expiry.
- Persistent document question answering.
- Structured model output validation.
- Upload cleanup.
- Operational monitoring.
- Production release verification.

**DOCUMENTED/INTENDED**

- Public ALB and private ECS placement.
- VPC, subnet, security-group, and NAT setup.
- Cloud Map provisioning.
- HTTPS API configuration.
- Some IAM policies and manual rollback procedures.

**FUTURE/PROPOSED**

- Durable document indexes and authorized follow-up retrieval.
- Atomic credit reservation and settlement.
- Idempotent payment processing and reconciliation.
- Reliable asynchronous jobs.
- Automated tests, AI evaluations, tracing, and alarms.
- Immutable releases and infrastructure as code.

**UNVERIFIED**

- Current live deployment and resource health.
- Actual IAM permissions and network rules.
- Current provider/model availability.
- Successful production payments.
- Current bucket access policies.
- Current database separation.
- Capacity, latency, uptime, recovery capability, and operating cost.

**NOT PRESENT in active implementation**

- Bedrock model invocation.
- Bedrock Agents or Knowledge Bases.
- Autonomous planning/reflection loops.
- LangGraph checkpointing.
- Server-side execution/testing of generated code.
- A model training or fine-tuning pipeline.
- MLflow, DVC, model registry, or drift monitoring.
- Kubernetes deployment.
- Comprehensive Terraform/CDK/CloudFormation provisioning.
- A substantive automated test/evaluation suite.

The Bedrock SDK dependency is present, but an installed dependency does not establish a working integration.

---

**4. Technology stack and project structure**

**Frontend**

React supplies the component model; Vite builds and serves the application; React Router implements `/` and `/admin`; Redux Toolkit stores user, conversation, message, artifact, and loading state.

Axios centralizes calls to the configured Gateway and includes cookies. Firebase handles browser Google sign-in.

Tailwind and Motion implement styling and animation. React Markdown, GFM support, and syntax highlighting render answers. Monaco presents generated files. The artifact iframe supports a limited HTML/CSS/JavaScript preview.

Evidence: E1, E2, E12 and [frontend manifest](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/package.json).

**Backend**

Node.js runs five Express applications. The source uses JavaScript ES modules, not a TypeScript application.

Mongoose provides schemas and MongoDB access. ioredis supports sessions, cached conversation context, and counters. Multer accepts uploaded PDFs/images. Morgan logs Gateway HTTP requests. Axios handles several service-to-service calls.

**AI**

LangGraph defines routing and execution order. LangChain integrations wrap model calls, embeddings, Tavily search, text splitting, and Qdrant storage.

These are orchestration/integration libraries. They do not train the models.

**Artifacts**

PDFKit renders PDFs. PptxGenJS renders presentations. AWS SDK v3 uploads generated files and produces presigned download URLs.

Python diagram scripts are documentation tooling, not the backend runtime or an ML pipeline.

**Important folders**

- [frontend/src](E:/GenAi-Project-Cloudage/1.cortexAI/frontend/src): UI, API helpers, routing, Redux.
- [backend/gateway](E:/GenAi-Project-Cloudage/1.cortexAI/backend/gateway): browser-facing proxy and session lookup.
- [backend/services/auth](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/auth): identity, credits, administration.
- [backend/services/chat](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/chat): conversation/message persistence.
- [backend/services/agent](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/agent): graph, specialists, providers, uploads, artifacts.
- [backend/services/billing](E:/GenAi-Project-Cloudage/1.cortexAI/backend/services/billing): orders, signatures, payment records.
- [backend/shared](E:/GenAi-Project-Cloudage/1.cortexAI/backend/shared): Redis client.
- [task-defs](E:/GenAi-Project-Cloudage/1.cortexAI/task-defs): ECS task configuration.
- [.github/workflows](E:/GenAi-Project-Cloudage/1.cortexAI/.github/workflows): delivery automation.
- [new-project-pic](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic) and [project-pic](E:/GenAi-Project-Cloudage/1.cortexAI/project-pic): diagrams and screenshots.

**Why these technologies were selected**

Their responsibilities are clear from usage. The original historical reasons for choosing them are not established by implementation alone. Later trade-off discussions are engineering reasoning, not invented accounts of your decisions.

---

**5. Visual assets found and inspected**

**Architecture diagrams**

1. [Technical architecture PNG](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/novamind-aws-architecture.png), with [SVG counterpart](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/novamind-aws-architecture.svg).

   This is the most useful existing architecture diagram for technical discussion. It correctly separates frontend delivery from API calls, shows the five services, places specialists inside Agent, identifies external providers, and depicts the release workflow.

   Qualification: private subnet placement and NAT topology remain deployment-guide claims. The phrase “eight nodes” should be explained as eight specialists; source registers nine named nodes including the router.

2. [Architecture poster](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/novamind-aws-architecture-poster.png).

   Shows ten panels covering users, AWS, specialists, providers, RAG, security, and deployment. Its principal flows mostly agree with code.

   Labels such as “secure,” “scalable,” and “least privilege” exceed what the code/configuration proves. The [poster notes](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/architecture-poster-notes.md) explicitly identify it as generated illustration.

3. [Older architecture image](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/architecture.jpg).

   Contains important contradictions: Billing is duplicated; Auth is described as managing conversations/messages without Redis; graph arrows suggest relationships that do not match the source. Do not use it as an authoritative implementation diagram.

4. [Root architecture PNG](E:/GenAi-Project-Cloudage/1.cortexAI/novamind-aws-architecture.png).

   Depicts AWS, services, external providers, and the graph in a very tall layout. Its small labels are difficult to read at normal display size. It is a documentation visualization, not proof of provisioned infrastructure. It was already untracked before this review.

**AWS screenshots**

- [ECS](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/aws-ecs.png): visibly shows five Fargate services and one running task per service at capture time. This supports historical deployment evidence, not current health or HA.
- [ECR](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/aws-ecr.png): shows five repositories with mutable tags.
- [ElastiCache](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/aws-elastic-cache.png): shows one Redis node, Multi-AZ disabled, automatic failover disabled, and encryption at rest/in transit disabled at capture time.
- [S3](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/aws-s3-bucket.png): shows image, PDF, and PPTX objects. Does not establish access policy or successful current downloads.
- [CloudFront](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/aws-cloudfront.png): shows a frontend distribution; standard logging is visibly off. It does not show a verified API origin.
- [IAM](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/aws-iam-role.png): shows role names, not their complete permissions.
- [CloudWatch](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/aws-cloudwatch-logs.png): visible rows include unrelated application logs. This image alone does not demonstrate NovaMind request observability. The task definitions are stronger evidence of intended log delivery.

**CI/CD screenshots**

[Run list](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/Novamind-ai-multiagent-github-action-1.png), [in-progress run](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/Novamind-ai-multiagent-github-action-2.png), and [successful run](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/Novamind-ai-multiagent-github-action-3.png) show both failed and successful historical workflow executions.

A green workflow confirms its commands completed, not that all application paths passed tests. The current workflow has no automated test stage or ECS stability gate.

**Application screenshots**

- [Login](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-platform-loginpage-1.png) and [Google popup](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-platform-login-aunthentication-1.png): visible authentication UI consistent with Firebase code.
- [Workspace](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-1.png): conversation sidebar and agent picker.
- [Billing drawer](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-2.png): matches configured plan prices and credits.
- [Code view](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-4.png) and [preview](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-5.png): support the artifact viewer implementation.
- [PDF/image result](E:/GenAi-Project-Cloudage/1.cortexAI/project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-9.png) and [PPT result](E:/GenAi-Project-Cloudage/1.cortexAI/project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-10.png): show result links, not verified downloadable content.
- [Admin overview](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-1.png), [users](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-2.png), [payments](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-3.png), and [later user list](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-4-users.png): support visible administration features. The payment screenshot shows `created` orders, not completed revenue.

**Significant screenshot mislabeling**

- [“RAG capability 1”](<E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/Novamind-ai-multiagent-platform-rag-capabiliti-1 .png>) actually shows an image-generation request returning an S3 endpoint error.
- [“RAG capability 2”](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/Novamind-ai-multiagent-platform-rag-capabiliti-2.png) shows a résumé summary. It supports visible document-answer behavior but does not prove persistent follow-up retrieval or factual accuracy.
- [Dashboard 3](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-3.png) contains an answer **about** Bedrock. It does not demonstrate use **of** Bedrock.
- [Dashboard 7](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-7.png) contains generated architecture suggestions involving additional AWS services. Those suggestions are answer content, not this project’s implementation.
- [Dashboard 6](E:/GenAi-Project-Cloudage/1.cortexAI/new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-6.png) shows a model describing its capabilities. Model self-description is not execution evidence.

I treated repetitive legacy screenshots and decorative logos/icons as supporting material rather than independent architectural evidence.

---

**6. Current architecture**

```text
Browser
  |
  +-- Website delivery: CloudFront --> frontend S3 bucket
  |                       [deployment configuration/documentation]
  |
  +-- Firebase Google sign-in
  |
  +-- API calls --> configured API endpoint
                     |
                 ALB [documented AWS entry]
                     |
                 Express Gateway :8000
                     |
         +-----------+-----------+-----------+
         |           |           |           |
      Auth :8001  Chat :8002  Agent :8003  Billing :8004
         |           |           |           |
       Users      Messages    LangGraph    Payments
       MongoDB    MongoDB         |         MongoDB
         |                       |           |
       Redis          +----------+--------+ Razorpay
                      |          |        |
                 Models/tools  Qdrant    S3 artifacts

Agent --> Chat: save/read messages
Agent --> Auth: request credit deduction
Billing --> Auth: grant plan/credits
Gateway/Auth/Agent --> Redis
Auth admin --> Chat/Billing databases directly
```

**Architecture style**

It is reasonable to call this a microservice architecture because services have separate processes, manifests, Dockerfiles, ports, and task definitions.

However, independence is incomplete:

- Agent synchronously depends on Chat and Auth.
- Auth administration directly reads other services’ databases.
- Shared conventions and unauthenticated internal calls couple services.
- The release workflow rebuilds/redeploys every backend service together.

**Important distinction:** the Express “Gateway” is not the managed AWS API Gateway service.

**Important distinction:** specialist agents are JavaScript functions inside one Agent service, not eight independent ECS services.

---

**7. Application and request flows**

**A. Login**

```text
Google popup
  → Firebase ID token
  → POST /api/auth/login
  → Auth verifies token
  → find/create MongoDB user
  → create UUID Redis session
  → HTTP-only session cookie
  → frontend stores returned user in Redux
```

Auth stores both:

- `session-<sessionId>`: user snapshot.
- `user-session-<userId>`: pointer to one session.

Both receive seven-day expiry at login.

Protected Gateway requests read the cookie, retrieve the session snapshot, and set `x-user-id` for downstream services.

The application session is an opaque UUID backed by Redis. It is not a locally issued JWT session. Firebase’s ID token is a separate authentication artifact.

Evidence: E1, E3, E4.

**B. Sending a message**

1. `ChatInput` requires nonblank prompt text.
2. If no conversation exists, it requests one from Chat through Gateway.
3. It updates a “New Chat” title.
4. It builds multipart form data: prompt, conversation ID, selected agent, optional file.
5. It adds an optimistic user message in Redux.
6. Axios posts to `/api/agent/chat`.
7. Gateway checks the Redis session and forwards identity.
8. Agent’s Multer middleware handles the optional file.
9. Agent saves the user message through Chat.
10. Agent invokes the graph.
11. The chosen specialist calls its providers/tools.
12. Specialist code requests credit deduction at its particular stage.
13. Agent appends user/assistant content to Redis memory.
14. Agent saves the assistant response through Chat.
15. A JSON response returns answer, images, and artifacts.
16. React renders the result.

```text
ChatInput → Gateway → Agent controller → Chat persistence
                                    → LangGraph → specialist/providers
                                    → Redis memory
                                    → Chat persistence
                                    → JSON → Redux/rendering
```

This is a synchronous request. The loading animation does not represent streamed tokens or actual backend execution stages.

Evidence: E2, E3, E7, E8.

**C. Automatic routing**

Priority is:

1. Explicit non-`auto` selection.
2. Uploaded PDF → `pdfRag`.
3. Uploaded image → `imageAnalyzer`.
4. Groq classification of the text prompt.
5. An unrecognized returned label falls through to Chat in graph routing.

An exception in the classifier is not the same as an unrecognized label; there is no general classifier-error fallback.

Selecting “PDF” explicitly invokes document generation even if a PDF is attached. Selecting “Vision” invokes image generation. File-aware analysis is normally reached through Auto.

Evidence: E8.

**D. Web research**

```text
Search node
  → rate counter
  → Tavily query, up to five results and images
  → request five-credit deduction
  → Chat node
  → chat rate counter
  → Groq with search results and history
  → request one-credit deduction
  → final answer
```

A successful Search → Chat flow requests **six credits**, not five.

The system supplies search results to the model; it does not implement verified citation alignment or a fact-checking engine.

Evidence: E10, E15, E4.

**E. PDF question answering**

Example: attach a text PDF and ask, “What skills are listed in this résumé?”

```text
Upload → temporary disk file → pdf-parse extraction
       → 1,000-character chunks / 200-character overlap
       → Gemini embeddings
       → new Qdrant collection
       → similaritySearch(question, 5)
       → retrieved context + question
       → Groq answer
       → credit request
       → temporary PDF deletion
```

The PDF is not simply placed wholesale into the model prompt. Retrieval exists at `similaritySearch`.

However, no document ID or collection mapping is persisted for later questions. A text-only follow-up does not reopen the original PDF index.

Evidence: E11.

**F. Code generation**

1. Groq classifies the coding request into categories such as generation, review, debugging, or explanation.
2. Generation prompts DeepSeek through OpenRouter for a JSON `files` array.
3. The response is directly parsed as JSON.
4. File contents become a Chat artifact.
5. Monaco displays them.
6. A browser iframe can preview `index.html`, `style.css`, and `script.js`.

Other coding intents return Markdown.

There is no package installation, compilation, execution of Python/server code, test runner, or automated repair cycle.

Evidence: E12.

**G. PDF/PPT generation**

Groq produces JSON describing content. Application code parses it, requests credit deduction, renders the document, uploads it to S3, and returns a presigned link.

The PPT prompt requests six content slides; the renderer adds a cover and closing slide. Therefore, compliant output produces eight total slides, not six total slides.

Evidence: E13.

**H. Images**

Image generation:

```text
Prompt → Groq prompt expansion → Stability REST API
       → image buffer → S3 → signed URL
```

Image analysis:

```text
Uploaded image → read file → base64 data URL
               → Gemini multimodal request
               → text answer → cleanup
```

These are different workflows and providers.

Evidence: E14.

**I. Payments**

```text
Choose plan → Billing creates Razorpay order
            → MongoDB Payment(status=created)
            → browser Razorpay checkout
            → callback to Billing verification
            → HMAC verification
            → Payment(status=paid)
            → Auth adds credits and updates plan
```

Important ordering: the payment is saved as paid **before** Auth confirms the credit grant. There is no transaction covering both services.

Evidence: E17, E4.

**J. Administration**

The UI requests statistics, filtered user lists, user changes/deletion, and payment lists.

Auth obtains its own users and opens additional Mongoose connections to Chat and Billing databases. Therefore, admin reporting crosses service database boundaries directly.

“Active users” is calculated using user `updatedAt`, not a dedicated login/activity event stream.

Evidence: E5.

---

**8. Generative AI, RAG, and agent analysis**

**Configured models**

- Groq: `openai/gpt-oss-120b`.
- Gemini image analysis: `gemini-2.0-flash`.
- OpenRouter coding: `deepseek/deepseek-chat`, temperature `0`, maximum output tokens `2500`.
- Gemini embeddings: `gemini-embedding-001`.
- Stability image generation: direct `stable-image/generate/core` REST endpoint.
- Tavily: search tool, maximum five results, images enabled.

These are source-configured identifiers. Their current availability and quality were not tested.

The `openai/` prefix in the Groq model name does not mean the application invokes the OpenAI API. The configured client is Groq.

**Prompt construction**

Prompts are embedded in specialist source files. They describe roles, output style, JSON structure, or grounding requirements.

There is no centralized versioned prompt registry, schema-enforced structured response contract, prompt evaluation suite, or systematic prompt-injection defense.

**Context**

Only Chat explicitly loads conversation memory. Search reaches that same Chat node. Other specialists generally use the current request and their own immediate input.

Consequently, “the application saves conversation history” does not mean every specialist reasons over that history.

**What makes this agentic?**

There is model-based routing, specialist selection, an external search tool, and multi-stage workflows.

A defensible description is:

> A LangGraph-orchestrated collection of specialized AI workflows with automatic routing and a Search-to-Chat chain.

Avoid:

> Autonomous agents collaborate, plan freely, select tools repeatedly, and recover through reflection.

Those behaviors are absent.

**Graph state versus memory**

Graph state holds the current prompt, response, selected agent, conversation ID, user ID, search results, images, artifacts, and file.

The graph is compiled without a checkpointer. Redis conversation history does not make graph execution durable or resumable after task termination.

**RAG strengths**

- Real extraction and retrieval.
- Separation between embeddings and answer generation.
- A bounded retrieved context of five chunks.
- An instruction to abstain when the answer is absent.

**RAG limitations**

- Text extraction only; no OCR pipeline for scanned PDFs.
- Character-based chunking, not explicitly token-based or document-structure-aware.
- One new timestamp-named collection per request.
- No saved user/document/collection ownership model.
- No stable index reuse.
- No page-aware citation response contract.
- No explicit similarity threshold.
- No reranking or hybrid search.
- No retrieval-quality evaluation.
- No collection deletion/retention process.
- No demonstrated multilingual or table extraction evaluation.
- Grounding instructions do not guarantee grounded answers.

**Qdrant API key verification**

The application passes the Qdrant URL and collection name without explicitly passing `apiKey`. I checked the relevant installed adapter because this could otherwise produce a false bug report. Version 1.0.3 reads `QDRANT_API_KEY` from the environment.

Therefore, **omitting the explicit argument is not itself a verified authentication defect**.

**Cost controls**

The code has per-agent counters and fixed credit prices. It does not record actual token usage, embedding usage, image-generation spend, or cost per successful request.

Automatic routing adds a model call. Coding adds an intent-classification call. Search adds a search request and synthesis call. Repeated PDF uploads repeat parsing, embedding, and indexing.

---

**9. Data, state, and memory**

**MongoDB**

Logical models:

- User: Firebase UID, profile, plan, credits, total credits, expiry.
- Conversation: title, user ID.
- Message: conversation ID, role, content, images, artifacts.
- Payment: user/order/payment IDs, amount, plan, credits, status.

Agent opens a MongoDB connection at startup but does not show a corresponding Agent-owned business model.

**Database-name configuration issue**

Auth’s checked-in admin database URIs place `/billing` and `/chat` inside the `appName` query value, while the URI database path is empty.

That syntax does not select the intended database. Whether reporting happens to work depends on where actual data was stored and runtime configuration. Do not claim verified database isolation. MongoDB documents the database as a path before query options. [MongoDB connection-string reference](https://www.mongodb.com/docs/v7.0/reference/connection-string-formats/).

**Redis**

Three roles share one client/service:

1. Authentication sessions.
2. Conversation context cache.
3. Rate counters.

These have different reliability needs. Losing cached history is recoverable from MongoDB; losing sessions forces reauthentication; losing counters resets limits.

**Memory defects**

- Cache hydration fetches all conversation messages without an explicit limit.
- The current user message is saved before hydration, then appended again to the model input.
- Cache updates use read–modify–write JSON arrays, allowing lost updates under concurrency.
- A single `shift()` does not reduce an already oversized history to twenty messages.
- Hydration sets a 24-hour TTL, but subsequent plain `SET` calls remove it. Redis documents this overwrite behavior. [Redis SET reference](https://redis.io/docs/latest/commands/set/).
- Memory stores role/content, not complete document or image context.
- There is no summarization or token-aware context selection.

**Frontend state**

Redux state is in browser memory. On refresh, the application reloads the user/session and fetches conversations/messages through APIs. No durable Redux persistence mechanism was found.

**Files**

- Uploads: temporary local Agent disk.
- PDF vectors/text chunks: Qdrant.
- Generated PDF/PPT/images: S3.
- Generated code: message artifacts in MongoDB.
- Presigned links: embedded in stored answer content.

No application mechanism renews expired artifact links from stable object metadata.

**Restarts**

- MongoDB/S3/Qdrant data can outlive an Agent process, subject to external persistence.
- Local upload processing and in-flight graph execution do not survive replacement reliably.
- Redis survival depends on deployment persistence/failover configuration.
- No resume protocol ties these pieces together.

---

**10. AWS/cloud architecture**

**ECS Fargate**

Task definitions specify `FARGATE` and `awsvpc`.

Declared allocations:

- Gateway, Auth, Chat, Billing: 512 CPU units and 1,024 MiB each.
- Agent: 1,024 CPU units and 2,048 MiB.

These are allocations, not benchmark-derived requirements. Desired task count and subnet placement are service-level settings, not established by these task files.

**ECR**

Five repositories/image references correspond to the services. The workflow pushes mutable `latest` tags.

**S3**

Two distinct uses:

- Frontend build delivery.
- Generated artifacts.

The SDK performs `PutObject` and presigned `GetObject`. Bucket privacy, lifecycle policies, and versioning are not established by those calls.

**CloudFront**

The workflow invalidates the frontend distribution after S3 synchronization. This does not establish CloudFront as the API proxy.

**ElastiCache**

Task environments point Redis clients at an ElastiCache endpoint using `redis://`. The screenshot shows a nonredundant, unencrypted configuration at capture time.

**Cloud Map**

Internal HTTP URLs use the `novamind.local` namespace. This is evidence of intended DNS-based service discovery. Service discovery does not authenticate callers or authorize requests.

**IAM and Secrets Manager**

Execution roles are referenced for container startup operations; Agent has an application task role for its AWS work. Secret references configure database/provider credentials and Firebase JSON.

Execution roles and application task roles have different responsibilities. AWS documents the execution role as supporting ECS/Fargate operations such as image pulls and configured secret retrieval. [ECS execution-role documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

Actual effective permissions were not inspected live. Role names do not prove least privilege.

**CloudWatch**

All five task definitions specify `awslogs`. This supports container log collection configuration.

No application tracing, request correlation, alarm definitions, or service-level objectives were found.

**VPC, ALB, subnets, NAT**

The deployment guide describes public ALB/NAT and private tasks. That is plausible for services requiring outbound access to external model APIs, Atlas, Firebase, Qdrant, and Razorpay.

The repository does not provide complete declarative provisioning or live verification of this topology.

**Regional considerations**

Task definitions use `us-east-1`. The configured Qdrant endpoint indicates `eu-west-1`. This creates a potential cross-region dependency, but no measured latency or transfer cost is established.

**Availability**

Multiple subnet boxes do not prove redundant replicas. The ECS screenshot shows one task per service, and Redis shows one node with failover disabled. Current HA claims would be unsupported.

---

**11. Deployment and CI/CD**

**Local execution**

The documented development arrangement is six Node processes/terminals: frontend plus five backend services. Compose starts only Redis, not the full stack.

Service ports are 8000–8004; frontend development uses 5173; Redis uses 6379.

External providers are still external during local development.

**Configuration**

- Backend: environment variables, `.env` examples, and ECS-injected values.
- Frontend: `VITE_*` build-time values.
- Firebase: environment JSON or local service-account file.
- S3: explicit local credentials if both custom variables exist, otherwise SDK credential chain.

The Agent example omits `STABILITY_API_KEY`. Auth’s example omits additional admin database URIs.

**Local environment initialization concern**

Gateway and Auth import modules that initialize Redis or Firebase before their entry-module `dotenv.config()` body executes. Values supplied only through `.env` may therefore be unavailable during dependency initialization. ECS-injected process environment values are available earlier.

This is a static initialization-order finding, not a reproduced startup failure.

**Docker**

All five Dockerfiles:

1. Use `node:22-alpine`.
2. Install backend-root dependencies.
3. Install service dependencies.
4. Copy the service and shared code.
5. Run `npm start`.

They are single-stage builds and do not declare a non-root user or health check. They use `npm install`, although lockfiles exist.

**Build-context problem**

The workflow builds with `backend` as the context. Local `.dockerignore` files are nested inside service directories and are ignored by Git. There is no effective context-root ignore file or corresponding Dockerfile-specific ignore file for these builds.

Consequences for local builds include copying `.env`, service-account files, temporary uploads, or local dependency trees. Git ignore rules do not filter Docker contexts. [Docker build-context rules](https://docs.docker.com/build/concepts/context/).

**Release flow**

```text
Push main
  → checkout
  → AWS credentials
  → ECR login
  → build/tag/push five images
  → force ECS redeployment of five services
  → frontend job
  → install/build frontend
  → S3 sync
  → CloudFront invalidation
```

**Missing release controls**

- No automated tests or lint stage.
- No immutable image identifiers.
- No task-definition registration from changed JSON.
- No wait for ECS service stability.
- No application smoke tests.
- No image scanning gate.
- No explicit deployment concurrency control.
- No automatic rollback.
- No verified zero-downtime procedure.

Changing a task-definition JSON file in Git does not cause this workflow to register that change.

The frontend job depends on completion of backend deployment commands, not verified backend readiness.

---

**12. Security**

**Implemented controls**

- Firebase token verification.
- HTTP-only session cookies.
- Production `Secure` and `SameSite=None` cookie settings.
- Gateway session checks on several prefixes.
- User identity overwrite on protected downstream proxies.
- Server-side admin email comparison.
- Multer MIME filtering and 20 MiB limit.
- Razorpay HMAC verification.
- S3 presigned access.
- Sandboxed artifact iframe.
- Secrets Manager references.

These are useful controls, but their composition leaves serious gaps.

**High-severity findings**

**A. Public account/credit mutation**

**Evidence:** E3, E4.

`/api/auth` is publicly proxied, and Auth exposes `/update-plan` and `/deduct-credits` without authentication. The handlers accept a user ID from the request body.

**Why it matters:** sensitive account changes do not require a verified internal caller or authenticated owner. Private service placement does not close a route exposed through Gateway.

**B. Alternate public path to admin handlers**

**Evidence:** E3, E4, E5.

Auth mounts its admin router at the service root. The public Auth proxy can reach those same root handlers. Admin middleware trusts `x-user-id` and then compares the corresponding user’s email.

**Why it matters:** protecting only the `/api/admin` prefix is insufficient. A client-supplied identity header through the other prefix can undermine the intended boundary.

This was derived from route composition, not actively exploited.

**C. Missing resource ownership**

**Evidence:** E6, E7.

Conversation listing filters by user, but message retrieval, title updates, and message creation do not verify that the conversation belongs to the current user.

**Why it matters:** authentication alone does not isolate users’ data.

**D. Credentials in tracked configuration**

**Evidence:** [Auth task definition](E:/GenAi-Project-Cloudage/1.cortexAI/task-defs/auth.json:21).

Credential-bearing MongoDB connection strings appear in plain environment values in a tracked file. A local Firebase private-key file also exists, although it is ignored rather than tracked.

**Why it matters:** tracked credentials require rotation and history/exposure assessment. Local private-key storage requires correct build exclusions. I have not reproduced the values or changed the credentials.

**E. Payment replay and credit integrity**

**Evidence:** E17, E4, E15.

A valid callback can reach credit granting repeatedly. No “already processed” condition prevents repeated credit addition. Balance changes use read–modify–save rather than an atomic conditional update.

**Why it matters:** payment authenticity is not the same as processing exactly once, and concurrent operations can corrupt accounting.

**F. Credit failures are swallowed**

**Evidence:** E15.

The Agent credit helper returns `null` on failure. Specialist callers continue.

**Why it matters:** users can receive provider work when a deduction fails, including insufficient-credit cases.

**Other security limitations**

- Logout reads `req.cookies` in Auth, which does not install cookie-parser.
- Browser cookie clearing does not establish server-side session revocation.
- Admin edits/deletion do not invalidate all session snapshots.
- Only one session pointer per user is maintained, while older sessions may remain.
- No explicit CSRF protection was found.
- CORS is an origin response policy, not authorization.
- Prompt/file contents can influence model behavior; no robust prompt-injection control exists.
- Search and document text are untrusted model context.
- MIME checks trust upload metadata rather than validating actual file contents.
- Sensitive tokens/session data/results are logged.
- Internal calls use HTTP and lack independently verified service identity.
- No demonstrated retention/deletion policy covers user documents and generated content.

The iframe uses `sandbox="allow-scripts"` without `allow-same-origin`, which is a useful isolation boundary. It is still not a complete resource-limited execution environment, and generated pages may contact external resources.

---

**13. Error handling and troubleshooting**

**Current behavior**

Most specialist catches return an error sentence as `aiResponse`. The controller can then save that sentence and return HTTP 200.

Consequences:

- HTTP success counts can hide AI failures.
- Failure text becomes conversation history.
- Search can fail, return empty results, and still continue to Chat.
- Partial side effects may already exist.
- A retry can repeat charges, uploads, or message writes.

**Specific code defects**

- Agent’s generic error handler references undefined `error` instead of `err`.
- `generatePdf` registers `doc.on("error", () => reject)` instead of invoking rejection with the error.
- Multer’s filename uses `${Date.now}` instead of `${Date.now()}`.
- PDF cleanup can throw from `finally` and replace the original error.
- Image rate checking occurs before its cleanup `try/finally`.
- Explicit file-incompatible routes can leave uploaded files uncleaned.
- Frontend `sendMessage` returns `null` on failure, but `ChatInput` accesses `data.artifacts`.
- Conversation creation failure can leave the UI in an inconsistent loading state.
- MongoDB connection failure is logged while the process may continue listening.

**Troubleshooting procedures**

**HTTP 500 after Send**

Symptom → inspect browser response and chosen workflow → correlate Gateway, Agent, Chat, and Auth logs → identify whether failure occurred during upload, persistence, routing, provider call, or final save → isolate that stage → fix the specific cause → verify success and failure behavior without duplicate side effects.

**Works locally, fails on AWS**

Symptom → inspect ECS events and stopped reasons → compare required environment names with task definitions → verify Cloud Map resolution, security groups, NAT egress, Atlas allowlist, Redis connectivity, and secret access → isolate network versus application startup → correct configuration → verify a complete authenticated request.

**LLM is slow**

Symptom → separate routing time, history load, provider response, rendering, S3, and persistence → inspect provider errors and task resource pressure → identify the dominant stage → apply deadlines/concurrency limits or change the expensive stage → compare measured latency and failure rates.

The current repository lacks these per-stage timings; instrumentation is a proposed prerequisite.

**S3 endpoint error**

Symptom → compare bucket region with S3 client region → inspect exact provider error and task environment → distinguish region mismatch from IAM denial → correct the specific configuration → verify upload and signed download.

The screenshot demonstrates that an endpoint error was displayed historically; it does not prove who fixed it.

**Payment paid but credits missing**

Symptom → locate payment by order ID → inspect Billing’s Auth call → check whether payment was saved before credit granting failed → reconcile exactly once → verify balance and payment ledger.

Blindly replaying the callback is unsafe with the current code.

**RAG answers incorrectly**

Symptom → confirm Auto actually selected PDF RAG → inspect extraction quality → inspect retrieved chunks using sanitized diagnostics → distinguish empty/scanned input, retrieval failure, and generation failure → correct the failing stage → evaluate answerable and unanswerable cases.

**Redis unavailable**

Symptom → distinguish authentication failures from Agent memory/limit failures → inspect endpoint, network, connection errors, resource saturation → restore connectivity or service → verify sessions and request behavior.

Redis is a shared availability dependency, not merely an optional acceleration layer.

---

**14. Testing and quality**

**Actually present**

- Frontend ESLint configuration and lint script.
- Frontend build script.
- Dependency lockfiles.
- Manual deployment/verification instructions.
- Screenshots of visible application and deployment behavior.

**Not found**

- Backend unit tests.
- API integration tests.
- Frontend automated interaction tests.
- End-to-end test suite.
- Authorization regression tests.
- Payment replay/concurrency tests.
- RAG evaluation dataset or metrics.
- Router accuracy evaluation.
- Generated artifact validation.
- Load testing.
- Fault injection.
- Restore/failover testing.
- Backend type checking.

The backend root `test` script is a placeholder that exits with an error. It is not a test suite.

I did not run lint, builds, or application tests because this was an inspection-only task. No passing test result is claimed.

**Highest-value future tests**

1. Unauthenticated and cross-user access rejection.
2. Admin route isolation through every proxy path.
3. Duplicate payment callbacks grant credits once.
4. Concurrent deductions cannot overspend.
5. Insufficient credits prevent provider work.
6. Provider errors preserve correct HTTP/application status.
7. Cache misses do not duplicate prompts.
8. Large histories remain bounded.
9. Upload cleanup works across failures and route choices.
10. RAG answers cite relevant evidence and abstain when unsupported.
11. Restart/retry does not duplicate job side effects.
12. Deployment smoke tests verify login, chat, and dependency readiness.

---

**15. Cost, scalability, and reliability**

**Cost drivers**

- Always-running ECS tasks.
- ALB and NAT infrastructure.
- Redis.
- Model input/output usage.
- Routing and coding-classification calls.
- Tavily searches.
- Stability image generation.
- Gemini embeddings.
- Qdrant storage and indexing.
- S3 storage, requests, and delivery.
- Logs and retained output.

The repository contains no measured operating-cost report. Fixed application credits are not equivalent to provider dollars or guaranteed profit margin.

**Current scaling constraints**

- Synchronous long-running requests.
- Provider quotas.
- Redis dependency.
- Non-atomic accounting and memory updates.
- Unbounded history retrieval.
- Repeated PDF indexing.
- Local upload disk.
- In-memory file buffers and PDF parsing.
- Admin queries loading all paid payments for aggregation.
- Missing pagination for ordinary message/conversation reads.
- No application admission control or durable backlog.

**What can scale horizontally**

The separate HTTP services can be replicated in principle. Shared storage allows requests to reach different replicas.

However, more replicas do not repair concurrency defects. They can increase duplicate side effects, memory races, and provider throttling.

**What should be measured**

- Per-workflow request volume.
- End-to-end and per-stage latency.
- Provider error/throttling rates.
- Input/output tokens and embedding volume.
- Cost per successful outcome.
- Concurrent jobs and memory/disk usage.
- Redis latency, memory, and evictions.
- Database query latency and result sizes.
- Retrieval quality.
- Payment reconciliation discrepancies.
- Artifact failures and expired-link incidence.

No user-capacity, throughput, or latency figure can be defended from this repository.

---

**16. What is good**

**Strength: a traceable full-stack request path.**  
**Evidence:** E1–E8.  
**Why it matters:** the UI, session gateway, persistence, orchestration, and response rendering are connected rather than isolated demos.

**Strength: real retrieval implementation.**  
**Evidence:** E11.  
**Why it matters:** the project supports a substantive RAG discussion about extraction, chunking, embeddings, retrieval, grounding, and evaluation.

**Strength: clear specialist separation.**  
**Evidence:** E8–E14.  
**Why it matters:** model/provider responsibilities can be explained and changed independently within the Agent service.

**Strength: multiple output modalities.**  
**Evidence:** E12–E16.  
**Why it matters:** it goes beyond returning text and handles structured code, rendered files, and images.

**Strength: real deployment artifacts.**  
**Evidence:** E18–E19.  
**Why it matters:** container build, task configuration, secret injection, and delivery mechanics can be inspected directly.

**Strength: current technical documentation acknowledges limitations.**  
**Evidence:** E20.  
**Why it matters:** the newer architecture/interview documents distinguish implementation from proposed improvements more carefully than older material.

---

**17. Problems and gaps by severity**

**HIGH**

- Public credit/plan mutations and alternate admin path — E3–E5.
- Missing conversation ownership enforcement — E6–E7.
- Tracked credential-bearing configuration — E19.
- Payment replay and non-atomic balances — E4, E17.
- Credit failures allowing continued AI usage — E15.
- Ineffective Docker build exclusions for local sensitive files — E18.
- No automated regression coverage for these boundaries — manifests/workflow.

**MEDIUM**

- Logout/session invalidation defects — E4–E5.
- Misleading success responses and broken generic error middleware — E7, E10–E14.
- Memory TTL, trimming, duplication, and concurrency defects — E15.
- Nonpersistent PDF document mapping and collection accumulation — E11.
- Upload naming/cleanup defects — E14, E16.
- Incorrect admin database URI placement — E19.
- Startup environment ordering — E3–E4.
- No release-stability gate or immutable image reference — E18.
- No validated readiness or restart recovery — service entries/E19.
- Expiring links persisted without refresh mechanism — E13–E16.
- Inadequate structured output validation — E12–E13.
- Sparse operational telemetry and sensitive logging — E3, E7, E19.

**LOW**

- NovaMind/CortexAI branding inconsistency in prompts and metadata.
- Misleading screenshot captions.
- Documentation link case mismatch such as `Architecture.md` versus `architecture.md` on case-sensitive environments.
- Some UI labels and generated-link expiry descriptions disagree with implementation.

Severity reflects potential application impact, not proof that a live incident occurred.

---

**18. Documentation and visuals versus implementation**

**Claim: production-grade.**  
**Actual:** significant authorization, accounting, reliability, and testing gaps.  
**Evidence:** archived README versus E3–E19.  
**Classification:** unsupported/contradicted as a current readiness claim.

**Claim: Pollinations image generation.**  
**Actual:** Stability REST API.  
**Evidence:** archived README versus E14.  
**Classification:** outdated.

**Claim: Gemini 2.5 Flash.**  
**Actual:** configured image-analysis model is Gemini 2.0 Flash.  
**Evidence:** archived README versus E9.  
**Classification:** contradicted by current configuration.

**Claim: Search costs five credits.**  
**Actual:** Search requests five, then Chat requests one.  
**Evidence:** E8, E10, E4.  
**Classification:** incomplete older documentation; newer README correctly describes six.

**Claim: strict last-twenty-message memory.**  
**Actual:** oversized hydration and one-item trimming violate a strict cap.  
**Evidence:** E15.  
**Classification:** contradicted.

**Claim: PDF follow-up retrieval.**  
**Actual:** no persistent collection lookup.  
**Evidence:** E11.  
**Classification:** partial capability; do not infer from conversation UI.

**Claim: six-slide presentation.**  
**Actual:** six requested content slides plus cover and closing slide.  
**Evidence:** E13.  
**Classification:** ambiguous/misleading.

**Claim: displayed download expiry.**  
**Actual:** PDF/image request 1,440 seconds; PPT requests 86,400 seconds. Some labels say ten minutes or twenty-four hours inconsistently.  
**Evidence:** E13–E16.  
**Classification:** contradicted.

Actual presigned access may end earlier when signing credentials expire. [AWS presigned URL documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html).

**Claim: Firebase secret downloaded to disk by startup AWS CLI.**  
**Actual:** current Auth reads injected JSON directly from `FIREBASE_SERVICE_ACCOUNT`, with a local-file fallback.  
**Evidence:** deployment guide versus E4/E19.  
**Classification:** outdated guide procedure.

**Claim: secure/private deployment implies safe internal routes.**  
**Actual:** Gateway exposes sensitive routes regardless of intended private task placement.  
**Evidence:** E3–E5.  
**Classification:** contradicted security inference.

**Claim: `secure:false` prevents cookies being sent over HTTPS.**  
**Actual:** that explanation in deployment prose is incorrect. The Secure flag restricts sending to secure connections; its absence does not itself forbid HTTPS. Cross-site cookie acceptance has additional requirements.  
**Evidence:** deployment guide and E4.  
**Classification:** incorrect explanatory text.

**Claim: successful CI/CD means healthy deployment.**  
**Actual:** no service-stability wait or smoke tests.  
**Evidence:** E18.  
**Classification:** unsupported inference.

**Claim: least privilege/HA/fully monitored.**  
**Actual:** role names, diagram boxes, and log settings do not establish these properties; screenshots show important limitations.  
**Classification:** unverified or overstated.

---

**19. Prioritized improvements and realistic Production V2**

These are recommendations only. Nothing was implemented.

**HIGH PRIORITY**

1. **Repair authorization boundaries.** Restrict public Auth routing, authenticate internal mutations, reject client identity spoofing, and enforce ownership in Chat/Agent. This protects accounts and user data.
2. **Rotate exposed credentials and repair build exclusions.** Move sensitive values out of tracked task configuration and prevent local secrets entering images.
3. **Make payments and credits atomic and idempotent.** Bind orders to users, prevent repeated processing, reserve credits before provider work, and reconcile partial failures.
4. **Repair session revocation.** Parse cookies correctly and invalidate sessions after logout, deletion, or relevant account changes.
5. **Introduce reliable error contracts.** Separate failure from successful answer content, fix broken middleware, and make the UI handle rejected requests.
6. **Add regression tests for the preceding controls.**

**MEDIUM PRIORITY**

- Persist authorized document metadata and reusable vector mappings.
- Add page/source metadata, retrieval evaluation, and cleanup.
- Fix memory bounds, TTL, ordering, and concurrency.
- Validate prompt sizes, IDs, file contents, and model output schemas.
- Add deadlines, cancellation, and bounded concurrency.
- Store artifact object identifiers and issue fresh links after authorization.
- Add readiness and graceful shutdown.
- Use immutable release identifiers and stability/smoke gates.
- Add structured redacted logs, correlation IDs, metrics, and alerts.
- Make infrastructure reproducible.

**OPTIONAL/FUTURE**

- Durable asynchronous workers for long PDF/PPT/image jobs.
- Streaming for appropriate text workflows.
- More advanced retrieval only after evaluations demonstrate a need.
- Alternative providers based on measured quality/cost.
- Richer RBAC if more than one administrator role is required.

**Production V2**

**THIS IS A PROPOSED FUTURE ARCHITECTURE, NOT THE CURRENT IMPLEMENTATION.**

**KEEP**

React, the service boundaries where useful, LangGraph’s explicit workflow structure, external model providers, MongoDB, Redis, Qdrant, S3, and Fargate.

**CHANGE**

Authorization, accounting, sessions, document identity, errors, deployment identity, logging, and readiness.

**ADD**

- Credit/payment ledger and idempotency records.
- Document/collection ownership metadata.
- Artifact metadata and renewal endpoint.
- Automated tests and RAG/router evaluation.
- Infrastructure definitions and measured operational objectives.

**OPTIONAL LATER**

A queue and workers, only when durable long-running execution is a real requirement.

```text
Browser → authenticated Gateway → domain services
                                → Agent orchestration
                                      |
                           credit reservation + request ID
                                      |
                         synchronous text / optional job queue
                                      |
                         model, retrieval, artifact stages
                                      |
                           settlement + durable result
                                      |
                              response or job status

Shared supporting capabilities:
ownership checks · idempotency · document metadata
redacted telemetry · tested backups · immutable releases
```

For AWS deployment authentication, GitHub OIDC would avoid storing long-lived AWS credentials in repository secrets. This is a proposed change, not current behavior. [GitHub OIDC guidance](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-aws).

**Roadmap**

```text
Current implementation
 → authorization and credential fixes
 → payment/credit/session correctness
 → failure and input handling
 → regression tests and AI evaluations
 → document/memory lifecycle
 → reproducible deployment and release gates
 → observability and measured load testing
 → durable jobs and resilience where justified
```

---

**20. Architecture and design decisions**

The following are reasonable engineering explanations. The original decision history must be confirmed by you.

**Five services**

- **Requirement:** separate identity, persistence, AI work, billing, and ingress.
- **Choice:** independently containerized Express services.
- **Why:** boundaries can clarify responsibilities and allow separate resource allocation.
- **Trade-off:** more deployment, networking, consistency, and security work.
- **Alternative:** modular monolith.
- **When unsuitable:** when operational overhead exceeds the benefit of independent services.

**LangGraph**

- **Requirement:** route to specialized workflows and chain Search into Chat.
- **Choice:** explicit state graph.
- **Why:** visible nodes/edges and extensible orchestration.
- **Trade-off:** additional framework concepts for a graph that is currently simple.
- **Alternative:** ordinary functions and a switch statement.
- **When unsuitable:** if the workflow remains trivial and framework overhead impedes maintenance.

**Redis sessions**

- **Requirement:** server-side session lookup shared across Gateway replicas.
- **Choice:** opaque cookie plus Redis state.
- **Why:** centralized revocation and session storage are possible.
- **Trade-off:** every protected request depends on Redis availability.
- **Alternative:** short-lived signed access tokens with carefully designed refresh/revocation.
- **When unsuitable:** if the operational dependency or regional architecture makes centralized sessions inappropriate.

**Qdrant plus Gemini embeddings**

- **Requirement:** semantic retrieval over extracted PDF text.
- **Choice:** managed vector storage and external embeddings.
- **Why:** supplies retrieval without building vector indexing.
- **Trade-off:** additional service, latency, credentials, lifecycle, and data governance.
- **Alternative:** a database with vector support, or bounded direct context for very small files.
- **When unsuitable:** when documents are tiny or an existing data platform already satisfies retrieval needs.

**Fargate**

- **Requirement:** run existing Node HTTP services in containers.
- **Choice:** managed container tasks.
- **Why:** fits long-lived service processes without managing hosts.
- **Trade-off:** baseline compute and networking costs.
- **Alternative:** a simpler hosted container platform or function-based design.
- **When unsuitable:** when workload/operations strongly favor another execution model.

**S3 artifacts**

- **Requirement:** deliver generated binary files without serving them from application memory.
- **Choice:** object storage plus signed URLs.
- **Why:** separates file delivery from application processing.
- **Trade-off:** lifecycle, ownership, region, and expiry must be handled.
- **Alternative:** short-lived direct download for small ephemeral outputs.
- **When unsuitable:** when persistent storage is unnecessary and its complexity outweighs benefits.

---

**21. Interview-critical facts**

**You can confidently claim**

- Five Express services and eight specialist workflows.
- Real LangGraph orchestration.
- Real PDF retrieval using Qdrant and Gemini embeddings.
- Groq, Gemini, OpenRouter/DeepSeek, Tavily, and Stability integrations.
- MongoDB persistence, Redis sessions/memory/counters, and S3 artifacts.
- Dockerfiles, Fargate task definitions, and GitHub Actions deployment automation.
- Firebase authentication and Razorpay signature verification.

**Explain carefully**

- “Multi-agent” means fixed specialist workflows inside one Agent service.
- “RAG” currently applies to the uploaded PDF request, without persistent follow-up lookup.
- “Microservices” does not imply complete data or release independence.
- “Memory” has implementation defects and is used explicitly by Chat.
- “Billing” exists but is not robust against replay/concurrency.
- “AWS deployed” requires distinguishing historical screenshots from current live verification.
- “Monitoring” currently means basic logs/configuration, not comprehensive observability.

**Do not claim**

- Bedrock-powered inference.
- Autonomous planning or dynamic repeated tool calling.
- Production readiness.
- Proven least privilege, HA, autoscaling, or zero downtime.
- Verified recurring subscriptions.
- Guaranteed prevention of hallucination.
- Verified citations.
- Tested multi-user capacity or measured performance improvements.
- Successful commercial revenue.
- Personal ownership of every component.

---

**22. Roles, responsibilities, and personal ownership**

**PERSONAL OWNERSHIP MUST BE CONFIRMED BY THE USER.**

Repository branding, commit author names, screenshots, and file presence do not establish who personally designed or implemented each component.

**Possible responsibilities supported by project areas**

- **AI integration:** model configuration, specialist prompts, output handling — E8–E14.
- **RAG engineering:** parsing, chunking, embeddings, retrieval, evaluation design — E9/E11.
- **Backend integration:** routes, service calls, schemas, error contracts — E3–E7/E17.
- **Cloud/container work:** Dockerfiles, task definitions, secrets, CI/CD — E18/E19.
- **Frontend integration:** authentication, multipart requests, Redux, artifacts — E1/E2/E12.
- **Security/reliability work:** authorization, sessions, idempotency, observability — relevant evidence above.

If you claim one of these responsibilities, prepare:

1. The precise files/functions you changed.
2. The requirement you were addressing.
3. Alternatives you considered.
4. A failure you actually observed.
5. How you diagnosed and verified it.
6. What another contributor or tool supplied.
7. What remains incomplete.

Do not turn findings from this review into invented personal incident stories.

---

**23. Project-specific learning curriculum**

These are suggested future study-file names only; no files were created.

1. **FILE:** `01-Project-Overview.md`  
   **MAIN TOPIC:** Product purpose and capability boundaries.  
   **WHY I NEED IT:** Must master a truthful project introduction.

2. **FILE:** `02-Current-Architecture.md`  
   **MAIN TOPIC:** Five services, dependencies, and deployment boundaries.  
   **WHY I NEED IT:** Must master architecture without confusing specialists with services.

3. **FILE:** `03-Application-Flow.md`  
   **MAIN TOPIC:** Login, Send, persistence, response, billing, and admin flows.  
   **WHY I NEED IT:** Must trace requests across actual functions.

4. **FILE:** `04-Technology-Stack.md`  
   **MAIN TOPIC:** Responsibilities of the actual libraries and services.  
   **WHY I NEED IT:** Must explain what each component contributes.

5. **FILE:** `05-JavaScript-Express-Service-Foundations.md`  
   **MAIN TOPIC:** Async execution, ES modules, middleware, proxies, initialization.  
   **WHY I NEED IT:** Must understand the runtime beneath the AI layer.

6. **FILE:** `06-Firebase-Redis-Sessions-Authorization.md`  
   **MAIN TOPIC:** Identity verification, cookies, sessions, ownership, admin trust.  
   **WHY I NEED IT:** Must defend security boundaries and identify their gaps.

7. **FILE:** `07-LangGraph-State-And-Routing.md`  
   **MAIN TOPIC:** Nodes, conditional edges, state, bounded execution.  
   **WHY I NEED IT:** Must explain exactly what makes this workflow agentic.

8. **FILE:** `08-Models-Prompts-And-Provider-Calls.md`  
   **MAIN TOPIC:** Groq, Gemini, DeepSeek, prompt construction, output contracts.  
   **WHY I NEED IT:** Must distinguish provider integration from training.

9. **FILE:** `09-PDF-RAG-End-To-End.md`  
   **MAIN TOPIC:** Extraction, chunks, embeddings, Qdrant, retrieval, grounding.  
   **WHY I NEED IT:** Must master the project’s central retrieval claim.

10. **FILE:** `10-RAG-Quality-And-Document-Lifecycle.md`  
    **MAIN TOPIC:** Evaluation, citations, ownership, index reuse, deletion.  
    **WHY I NEED IT:** Must explain limitations and realistic improvements.

11. **FILE:** `11-Search-Coding-And-Multimodal-Workflows.md`  
    **MAIN TOPIC:** Tavily synthesis, coding classification, generation versus analysis.  
    **WHY I NEED IT:** Must trace each specialist without conflating them.

12. **FILE:** `12-PDF-PPT-S3-Artifacts.md`  
    **MAIN TOPIC:** Structured content, rendering, object storage, presigned links.  
    **WHY I NEED IT:** Should understand file production and delivery failures.

13. **FILE:** `13-MongoDB-Redis-State-And-Concurrency.md`  
    **MAIN TOPIC:** Schemas, cache hydration, TTL, races, session consistency.  
    **WHY I NEED IT:** Must master shared-state correctness.

14. **FILE:** `14-Razorpay-Credits-And-Idempotency.md`  
    **MAIN TOPIC:** Orders, signatures, repeated callbacks, atomic balances.  
    **WHY I NEED IT:** Must understand why payment verification alone is insufficient.

15. **FILE:** `15-React-Redux-And-Artifact-Preview.md`  
    **MAIN TOPIC:** UI state, API helpers, errors, Markdown, iframe isolation.  
    **WHY I NEED IT:** Should understand the complete user journey.

16. **FILE:** `16-AWS-Networking-And-Service-Discovery.md`  
    **MAIN TOPIC:** ALB, private tasks, NAT, Cloud Map, external dependencies.  
    **WHY I NEED IT:** Must explain the AWS deployment design.

17. **FILE:** `17-IAM-Secrets-And-Container-Security.md`  
    **MAIN TOPIC:** Task roles, execution roles, secret injection, build contexts.  
    **WHY I NEED IT:** Must distinguish implemented controls from assumptions.

18. **FILE:** `18-Docker-ECS-And-GitHub-Actions.md`  
    **MAIN TOPIC:** Builds, releases, task revisions, health gates, rollback.  
    **WHY I NEED IT:** Must explain deployment beyond naming services.

19. **FILE:** `19-Testing-Evaluation-And-Observability.md`  
    **MAIN TOPIC:** Regression tests, AI quality, logs, metrics, tracing.  
    **WHY I NEED IT:** Must explain how correctness would be demonstrated.

20. **FILE:** `20-Troubleshooting-And-Failure-Recovery.md`  
    **MAIN TOPIC:** Stage isolation, partial failures, restarts, retries.  
    **WHY I NEED IT:** Must answer scenario questions systematically.

21. **FILE:** `21-Cost-Scalability-And-Reliability.md`  
    **MAIN TOPIC:** Provider usage, bottlenecks, concurrency, HA, measurements.  
    **WHY I NEED IT:** Must avoid unsupported scale/cost claims.

22. **FILE:** `22-Limitations-Design-Decisions-Production-V2.md`  
    **MAIN TOPIC:** Prioritized changes and alternatives.  
    **WHY I NEED IT:** Must defend trade-offs and improvement sequencing.

23. **FILE:** `23-Complete-Project-Storytelling.md`  
    **MAIN TOPIC:** Evidence-backed project narrative and confirmed ownership.  
    **WHY I NEED IT:** Must connect technical details into a coherent story.

24. **FILE:** `24-Interview-Questions-And-Answers.md`  
    **MAIN TOPIC:** Practice answers and follow-up reasoning.  
    **WHY I NEED IT:** Must prepare for this repository’s likely challenges.

25. **FILE:** `25-Mock-Interview-Preparation.md`  
    **MAIN TOPIC:** Code walkthroughs, pressure questions, and honest uncertainty.  
    **WHY I NEED IT:** Must explain concepts naturally without memorizing claims.

Exact package versions, diagram-rendering coordinates, icon assets, and presentation styling details can remain reference knowledge.

---

**24. Complete project-specific interview question and answer bank**

The practice answers are training wheels. Replace them with your own words after you can explain the referenced implementation.

**Q1. Tell me about the project.**

**Difficulty:** Beginner.  
**Why the interviewer asks:** Tests whether you understand the product rather than only its tools.  
**Must understand:** User problem, core features, evidence boundaries.

**Practice answer:**  
“NovaMind AI combines chat, search, coding, document generation, image tasks, and PDF questions in one authenticated workspace. React provides the interface, and five Express services handle the backend. LangGraph routes AI requests to specialized workflows. The repository includes AWS deployment configuration, but I distinguish that from verified production readiness.”

**Evidence:** E1–E20.

**Follow-up 1:** Who uses it?  
**Answer:** “The features suit learners, developers, and people working with documents. I do not have repository evidence of measured customer adoption.”

**Follow-up 2:** What is its strongest technical feature?  
**Answer:** “The traceable integration of authenticated requests, specialist workflows, retrieval, persistence, and generated artifacts.”

**Common mistake:** Inventing business impact or user counts.

**Q2. What did you personally implement?**

**Difficulty:** Beginner, but high importance.  
**Why:** Tests ownership and honesty.  
**Must understand:** Your actual contribution history.

**Practice answer template:**  
“My confirmed contribution was [specific component]. I worked on [specific files and behavior]. I can explain the requirement, implementation, and verification. Other parts were [accurate attribution], and I would not claim ownership of those.”

**Evidence:** Use the relevant E references only after confirming ownership.

**Follow-up 1:** What was your hardest problem?  
**Answer template:** “The issue I actually encountered was [real symptom]. I investigated [evidence], changed [specific behavior], and verified [actual result].”

**Follow-up 2:** What did you not work on?  
**Answer template:** “I did not implement [confirmed boundary], although I understand how it connects to my component.”

**Common mistake:** Presenting this review’s findings as incidents you personally solved.

**Q3. Walk me through the architecture.**

**Difficulty:** Intermediate.  
**Why:** Tests boundaries and dependencies.  
**Must understand:** Frontend delivery versus API execution.

**Practice answer:**  
“The browser loads the React application separately from making API calls. In the AWS design, CloudFront and S3 deliver the frontend, while an ALB fronts the Express Gateway. Gateway proxies Auth, Chat, Agent, and Billing. Agent contains the LangGraph specialists and calls external providers. MongoDB, Redis, Qdrant, and S3 hold different kinds of state.”

**Evidence:** E3–E19.

**Follow-up 1:** Is Gateway AWS API Gateway?  
**Answer:** “No. It is our Express reverse-proxy service.”

**Follow-up 2:** Are the eight agents separate services?  
**Answer:** “No. They share the Agent process and deployment.”

**Common mistake:** Drawing all services as one sequential chain.

**Q4. What happens after the user presses Send?**

**Difficulty:** Intermediate.  
**Why:** Tests actual code knowledge.  
**Must understand:** E2/E7 ordering.

**Practice answer:**  
“The frontend creates a conversation if needed and posts multipart data. Gateway validates the session. Agent saves the user message, invokes the graph, updates Redis memory, saves the assistant response, and returns JSON. Provider calls and credit requests happen inside the selected specialist.”

**Evidence:** E2, E3, E7.

**Follow-up 1:** Is the answer streamed?  
**Answer:** “No. The controller waits for the graph and returns JSON.”

**Follow-up 2:** Can a failure leave partial data?  
**Answer:** “Yes. Input persistence, generation, accounting, and final persistence are separate operations.”

**Common mistake:** Claiming an atomic end-to-end transaction.

**Q5. Why use microservices?**

**Difficulty:** Advanced.  
**Why:** Tests whether complexity is justified.  
**Must understand:** Deployment independence versus coupling.

**Practice answer:**  
“The boundaries separate identity, chat storage, AI work, billing, and ingress. That can support different resource needs and ownership. The cost is extra networking and distributed consistency. A modular monolith would also be reasonable at this scale. I cannot infer the original decision history from the code.”

**Evidence:** E3–E7, E17–E19.

**Follow-up 1:** Are the databases fully isolated?  
**Answer:** “No. Auth administration directly reads Chat and Billing data.”

**Follow-up 2:** What would you simplify?  
**Answer:** “I would evaluate whether independent deployment is actually needed before adding further services.”

**Common mistake:** Saying microservices automatically improve scalability.

**Q6. How does authentication work?**

**Difficulty:** Intermediate.  
**Why:** Tests identity/session understanding.  
**Must understand:** Firebase ID token versus application cookie.

**Practice answer:**  
“Firebase handles Google sign-in. The browser sends the resulting ID token to Auth, which verifies it and finds or creates the MongoDB user. Auth creates a UUID session in Redis and sets an HTTP-only cookie. Gateway looks up that session for protected requests.”

**Evidence:** E1, E3, E4.

**Follow-up 1:** Is the session a JWT?  
**Answer:** “No. The application cookie contains an opaque session identifier.”

**Follow-up 2:** Why Redis?  
**Answer:** “It provides shared server-side session state, but also becomes an availability dependency.”

**Common mistake:** Treating Firebase authentication as complete application authorization.

**Q7. Is authorization secure?**

**Difficulty:** Advanced.  
**Why:** Tests whether you inspect trust boundaries.  
**Must understand:** Proxy paths, identity headers, object ownership.

**Practice answer:**  
“Some controls exist, but the current boundary is incomplete. The public Auth proxy exposes sensitive mutations and an alternate route to admin handlers. Chat also lacks ownership checks for several conversation operations. I would fix those before calling the application production-ready.”

**Evidence:** E3–E6.

**Follow-up 1:** Do private subnets solve this?  
**Answer:** “No. Gateway can still expose a private service’s dangerous route publicly.”

**Follow-up 2:** Does CORS solve it?  
**Answer:** “No. CORS does not authenticate callers or enforce resource ownership.”

**Common mistake:** Equating authentication, network placement, and authorization.

**Q8. How does logout work, and what is wrong with it?**

**Difficulty:** Intermediate.  
**Why:** Tests session lifecycle reasoning.  
**Must understand:** Cookie parsing and server-side revocation.

**Practice answer:**  
“The logout handler intends to delete the Redis session and clear the cookie. However, Auth reads `req.cookies` without installing cookie-parser. Clearing the browser cookie therefore does not prove that the server session was revoked. Older sessions and admin account changes also need consistent invalidation.”

**Evidence:** E4, E5.

**Follow-up 1:** Why are multiple logins relevant?  
**Answer:** “The user-to-session key points to one session, while other session keys can remain valid.”

**Follow-up 2:** What would you change?  
**Answer:** “Track and revoke the intended sessions explicitly and test logout, deletion, and account updates.”

**Common mistake:** Saying cookie deletion alone invalidates a stolen session.

**Q9. Explain the LangGraph graph.**

**Difficulty:** Intermediate.  
**Why:** Tests implementation versus framework name recognition.  
**Must understand:** Nodes, state, conditional edges.

**Practice answer:**  
“The graph starts at a router. It chooses one of eight specialist nodes. Most specialists go directly to the end; Search goes to Chat for synthesis. State includes the prompt, IDs, selected agent, file, and results. There are nine named nodes including the router.”

**Evidence:** E8.

**Follow-up 1:** Can nodes run in parallel?  
**Answer:** “No parallel specialist branches are configured.”

**Follow-up 2:** Can it resume after a crash?  
**Answer:** “No durable checkpointer is configured.”

**Common mistake:** Confusing saved chat history with graph checkpointing.

**Q10. What makes it agentic?**

**Difficulty:** Advanced.  
**Why:** Challenges an easily exaggerated claim.  
**Must understand:** Routing, tools, autonomy boundaries.

**Practice answer:**  
“It performs model-based routing and specialized tool-assisted workflows. Search calls Tavily and passes results to Chat. I describe it as bounded agent orchestration. It does not dynamically plan and repeatedly choose tools until a goal is complete.”

**Evidence:** E8, E10.

**Follow-up 1:** Why not one LLM call?  
**Answer:** “Search, retrieval, document rendering, and image generation require different processing and external services.”

**Follow-up 2:** How do you prevent infinite loops?  
**Answer:** “The current graph has no loop edges, so that risk is structurally limited.”

**Common mistake:** Claiming autonomous multi-agent collaboration.

**Q11. Why LangGraph instead of ordinary functions?**

**Difficulty:** Advanced.  
**Why:** Tests design judgment.  
**Must understand:** Current graph complexity.

**Practice answer:**  
“LangGraph makes state and workflow transitions explicit and offers room for richer orchestration. However, this graph could be implemented with ordinary functions and routing logic. The trade-off is framework overhead versus a consistent workflow abstraction; the repository does not prove the historical selection rationale.”

**Evidence:** E8.

**Follow-up 1:** What features are unused?  
**Answer:** “Durable checkpointing, human interrupts, parallel branches, and iterative loops are not configured.”

**Follow-up 2:** Would you remove it?  
**Answer:** “Only after considering maintenance needs and expected workflow evolution.”

**Common mistake:** Claiming LangGraph is technically required for this logic.

**Q12. How does routing work?**

**Difficulty:** Intermediate.  
**Why:** Tests precedence and edge cases.  
**Must understand:** Explicit selection, MIME routing, classifier fallback.

**Practice answer:**  
“An explicit selection wins. In Auto, PDF files go to PDF RAG and images go to image analysis. Otherwise Groq returns a route label. Unknown labels fall through to Chat, but a classifier exception does not have the same fallback.”

**Evidence:** E8.

**Follow-up 1:** What if I attach a PDF while selecting Chat?  
**Answer:** “Explicit Chat wins; attaching a file does not force PDF retrieval.”

**Follow-up 2:** What should be tested?  
**Answer:** “Ambiguous prompts, invalid labels, classifier failures, and file/selection conflicts.”

**Common mistake:** Saying uploaded files always override user selection.

**Q13. Which models are used?**

**Difficulty:** Beginner.  
**Why:** Tests provider accuracy.  
**Must understand:** E9 and image generation.

**Practice answer:**  
“Groq’s configured GPT-OSS model handles general text tasks and routing. Coding uses DeepSeek through OpenRouter. Gemini handles image analysis and embeddings. Stability generates images, and Tavily supplies search results. These are configured identifiers, not a claim of current provider availability.”

**Evidence:** E9, E10, E14.

**Follow-up 1:** Is Bedrock used?  
**Answer:** “The dependency exists, but active model invocation does not use Bedrock.”

**Follow-up 2:** Why these models?  
**Answer:** “Their responsibilities are visible; a benchmark-based historical selection is not established.”

**Common mistake:** Calling every model request an OpenAI or Bedrock call.

**Q14. How are hallucinations and token costs handled?**

**Difficulty:** Advanced.  
**Why:** Tests whether prompts are mistaken for guarantees.  
**Must understand:** Grounding, context size, evaluation.

**Practice answer:**  
“PDF and search workflows provide external context and grounding instructions. Those instructions reduce neither risk nor cost with a guarantee. There is no measured hallucination evaluation or token-cost ledger. Coding has an explicit output-token limit, while memory is message-based and currently imperfect.”

**Evidence:** E9–E11, E15.

**Follow-up 1:** Is temperature zero enough?  
**Answer:** “No. It does not establish factual correctness.”

**Follow-up 2:** What would you measure?  
**Answer:** “Groundedness, abstention, task quality, tokens, latency, and cost per successful request.”

**Common mistake:** Claiming “do not hallucinate” prevents hallucination.

**Q15. Show exactly where RAG happens.**

**Difficulty:** Intermediate.  
**Why:** Tests whether retrieval actually exists.  
**Must understand:** Ingestion versus query stages.

**Practice answer:**  
“The PDF agent extracts text, creates chunks, and passes them to the Qdrant vector-store adapter with Gemini embeddings. It then calls `similaritySearch` with the question and a limit of five. Those chunks become context for a Groq answer.”

**Evidence:** E11, especially `pdfRag` and `similaritySearch`.

**Follow-up 1:** What is embedded?  
**Answer:** “Document chunks are embedded for indexing, and the retrieval adapter embeds the query for similarity search.”

**Follow-up 2:** Why is this different from direct prompting?  
**Answer:** “The answer receives selected document passages retrieved from an index.”

**Common mistake:** Calling PDF generation RAG.

**Q16. Why 1,000-character chunks and 200 overlap?**

**Difficulty:** Advanced.  
**Why:** Tests empirical reasoning.  
**Must understand:** Chunking unit and retrieval trade-offs.

**Practice answer:**  
“Those are the configured values. Overlap can preserve context near boundaries, while chunk size affects retrieval granularity and prompt volume. I cannot claim those values were optimized. I would compare alternatives on representative PDFs using retrieval and answer-quality measurements.”

**Evidence:** E11.

**Follow-up 1:** Are these token counts?  
**Answer:** “No. The configured splitter is character-based.”

**Follow-up 2:** What about tables or scanned pages?  
**Answer:** “The current extraction pipeline does not provide dedicated table understanding or OCR.”

**Common mistake:** Inventing an evaluation that selected the settings.

**Q17. Can a user ask follow-up questions about the same PDF?**

**Difficulty:** Advanced.  
**Why:** Tests document-state understanding.  
**Must understand:** Collection lifecycle versus chat history.

**Practice answer:**  
“The current upload request performs retrieval, but its collection name is not saved in a document mapping. A later text-only question does not reconnect to that PDF index. Chat may remember the earlier answer, which is different from retrieving the original document again.”

**Evidence:** E8, E11, E15.

**Follow-up 1:** Are vectors deleted after answering?  
**Answer:** “No collection cleanup is implemented.”

**Follow-up 2:** What would durable follow-ups need?  
**Answer:** “A document ID, owner, stored collection mapping, authorized retrieval, and deletion policy.”

**Common mistake:** Treating persistent vectors as usable document memory automatically.

**Q18. How would you evaluate RAG?**

**Difficulty:** Advanced.  
**Why:** Tests quality engineering.  
**Must understand:** Retrieval and generation must be evaluated separately.

**Practice answer:**  
“I would build representative document/question cases with known supporting passages and unanswerable questions. First I would check extraction and whether retrieval finds the evidence. Then I would evaluate groundedness, answer correctness, and abstention. The repository currently has no such evaluation suite.”

**Evidence:** E11 and absence of evaluation artifacts.

**Follow-up 1:** What if the answer is wrong?  
**Answer:** “Identify whether the evidence was missing from retrieval or the model misused available evidence.”

**Follow-up 2:** Would you immediately add reranking?  
**Answer:** “Only if evaluation shows retrieval ranking is a material problem.”

**Common mistake:** Measuring only whether an answer sounds fluent.

**Q19. How does web search work?**

**Difficulty:** Intermediate.  
**Why:** Tests tool integration and failure propagation.  
**Must understand:** Search → Chat edge.

**Practice answer:**  
“Tavily receives the prompt as a query and returns up to five results plus images. The graph then invokes Chat, which inserts the results into its system prompt for synthesis. There is no autonomous repeated search loop.”

**Evidence:** E8, E10.

**Follow-up 1:** What happens when search fails?  
**Answer:** “The node returns empty results, but Chat still runs, so failure can be obscured.”

**Follow-up 2:** Does it guarantee valid citations?  
**Answer:** “No citation-validation contract is implemented.”

**Common mistake:** Describing arbitrary browsing or verified fact checking.

**Q20. How does code generation and preview work?**

**Difficulty:** Intermediate.  
**Why:** Tests structured outputs and execution boundaries.  
**Must understand:** Classification, JSON artifacts, iframe.

**Practice answer:**  
“Groq classifies the coding intent. For generation, DeepSeek returns JSON containing files. The application parses and stores them as artifacts. Monaco displays the files, and the browser assembles basic HTML, CSS, and JavaScript into a sandboxed iframe.”

**Evidence:** E12.

**Follow-up 1:** Can it run a generated backend?  
**Answer:** “No server-side execution environment is implemented.”

**Follow-up 2:** What can fail?  
**Answer:** “Invalid or truncated JSON, unexpected file structure, and incompatible preview content.”

**Common mistake:** Claiming generated projects are automatically compiled and tested.

**Q21. Explain PDF/PPT generation and S3 links.**

**Difficulty:** Intermediate.  
**Why:** Tests the difference between AI content and deterministic rendering.  
**Must understand:** JSON parsing, renderers, storage.

**Practice answer:**  
“The model generates document content as JSON. PDFKit or PptxGenJS renders that content, and the Agent uploads the resulting buffer to S3. A presigned URL is returned in the answer. The model does not directly produce the final binary file.”

**Evidence:** E13, E16.

**Follow-up 1:** How long do links last?  
**Answer:** “The code requests twenty-four minutes for PDFs/images and twenty-four hours for PPTs; some displayed labels are wrong.”

**Follow-up 2:** Does expiry delete the object?  
**Answer:** “No. Object retention is separate.”

**Common mistake:** Equating signed-link expiry with storage cleanup.

**Q22. What is the difference between Vision and Image Analyzer?**

**Difficulty:** Beginner.  
**Why:** Tests a confusing naming boundary.  
**Must understand:** Generation versus understanding.

**Practice answer:**  
“Vision generates a new image. Groq expands the prompt, then Stability generates it and S3 stores it. Image Analyzer reads an uploaded image and sends a multimodal request to Gemini to answer questions about it.”

**Evidence:** E14.

**Follow-up 1:** Does Gemini generate the image here?  
**Answer:** “No, not in the current workflow.”

**Follow-up 2:** Is uploaded-image context retained for later questions?  
**Answer:** “There is no durable image-context retrieval mechanism.”

**Common mistake:** Assigning the same provider and behavior to both paths.

**Q23. How is conversation memory implemented?**

**Difficulty:** Advanced.  
**Why:** Tests cache correctness.  
**Must understand:** Hydration, TTL, trimming, concurrency.

**Practice answer:**  
“Chat reads a JSON history array from Redis, falling back to Chat’s MongoDB history. The controller later appends user and assistant content. The intended twenty-message cache has defects: large hydration is not properly bounded, writes lose the TTL, and concurrent updates can overwrite each other.”

**Evidence:** E6, E7, E15.

**Follow-up 1:** Why can the current prompt appear twice?  
**Answer:** “It is persisted before a cache-miss history load, then explicitly added to model input.”

**Follow-up 2:** Do all agents use it?  
**Answer:** “Only Chat explicitly loads it; Search reaches Chat.”

**Common mistake:** Claiming a reliable token-aware sliding window.

**Q24. How do rate limits differ from credits?**

**Difficulty:** Intermediate.  
**Why:** Tests admission control versus accounting.  
**Must understand:** Redis counters and Auth balance updates.

**Practice answer:**  
“Rate limits count calls per user and agent bucket over roughly sixty-second windows. Credits are stored in the user record and represent application pricing. They solve different problems. The current credit deduction happens after provider work in many paths and failures are swallowed.”

**Evidence:** E4, E15.

**Follow-up 1:** What are the limits?  
**Answer:** “Chat allows twenty per window; the other defined buckets allow five.”

**Follow-up 2:** Is increment plus expiry atomic?  
**Answer:** “No. They are separate Redis operations.”

**Common mistake:** Saying rate limiting guarantees budget enforcement.

**Q25. How does payment verification work, and is it retry-safe?**

**Difficulty:** Advanced.  
**Why:** Tests distributed consistency.  
**Must understand:** HMAC versus idempotency.

**Practice answer:**  
“Billing computes an HMAC from the order and payment IDs and compares the callback signature. It then marks the payment paid and calls Auth to add credits. This verifies a signature but is not retry-safe: the same valid callback can trigger another credit grant.”

**Evidence:** E17, E4.

**Follow-up 1:** What if Auth fails?  
**Answer:** “The payment can remain paid while credits were not granted.”

**Follow-up 2:** What is the fix?  
**Answer:** “Idempotent processing, atomic credit effects, durable reconciliation, and order ownership checks.”

**Common mistake:** Claiming exactly-once payment handling from signature verification.

**Q26. Why use ECS Fargate?**

**Difficulty:** Intermediate.  
**Why:** Tests compute choice.  
**Must understand:** Containers, tasks, resources, alternatives.

**Practice answer:**  
“The application already consists of long-lived Node HTTP services, so Fargate is a natural container execution option. It removes host management, while task definitions specify resources, environment, roles, and logs. The trade-off is baseline compute and network cost. This is engineering reasoning, not verified historical rationale.”

**Evidence:** E18, E19.

**Follow-up 1:** Why not Lambda?  
**Answer:** “That would require evaluating request duration, execution limits, workload shape, and application changes.”

**Follow-up 2:** Is it highly available?  
**Answer:** “The repository does not establish redundant healthy replicas.”

**Common mistake:** Saying managed compute automatically makes the application highly available.

**Q27. Explain ALB, private subnets, NAT, and Cloud Map.**

**Difficulty:** Advanced.  
**Why:** Tests actual network paths.  
**Must understand:** Inbound traffic, outbound traffic, DNS.

**Practice answer:**  
“The guide places ALB at the public entry and tasks privately. NAT provides outbound access to external APIs. Cloud Map supplies internal service names used by HTTP calls. The task files reference those names, but live routing and security rules were not verified.”

**Evidence:** E19, E20.

**Follow-up 1:** Does Chat need outbound access?  
**Answer:** “Yes, it connects to external MongoDB Atlas.”

**Follow-up 2:** Does Cloud Map secure calls?  
**Answer:** “No. Name resolution is not authentication.”

**Common mistake:** Treating NAT as the inbound API path.

**Q28. What are task roles, execution roles, and Secrets Manager doing?**

**Difficulty:** Advanced.  
**Why:** Tests AWS permission boundaries.  
**Must understand:** Startup operations versus application API calls.

**Practice answer:**  
“The execution role supports ECS startup operations such as pulling images and retrieving configured secrets. The Agent task role provides application AWS permissions, such as S3 access. Secrets Manager references inject values into containers. Actual least privilege still requires policy inspection.”

**Evidence:** E19, E16.

**Follow-up 1:** Does Auth run AWS CLI to fetch Firebase JSON?  
**Answer:** “The current code reads injected environment JSON directly.”

**Follow-up 2:** Are all secrets managed correctly?  
**Answer:** “No. Plain credential-bearing MongoDB values remain in tracked Auth configuration.”

**Common mistake:** Treating role names as proof of permission scope.

**Q29. Why separate CloudFront/S3 frontend delivery from the API?**

**Difficulty:** Intermediate.  
**Why:** Tests browser and server responsibilities.  
**Must understand:** Static assets versus API requests.

**Practice answer:**  
“Vite produces static frontend assets that S3 and CloudFront can deliver. Once loaded, JavaScript calls the configured API endpoint separately. S3 does not process prompts or forward chat requests to the backend.”

**Evidence:** E1, E2, E18.

**Follow-up 1:** Are `VITE_*` values secret?  
**Answer:** “No. They become browser build configuration.”

**Follow-up 2:** Can an HTTPS frontend use an arbitrary HTTP API safely?  
**Answer:** “Browser mixed-content and cookie rules can prevent that; the API endpoint and TLS setup must be correct.”

**Common mistake:** Drawing S3 as the request-processing service.

**Q30. What happens if Redis fails?**

**Difficulty:** Advanced.  
**Why:** Tests shared dependency impact.  
**Must understand:** Sessions, memory, and counters.

**Practice answer:**  
“Gateway cannot validate normal sessions, Auth cannot create or update them normally, and Agent memory/rate operations can fail. Redis is therefore an availability dependency. MongoDB can restore history after recovery, but it does not replace session lookup automatically.”

**Evidence:** E3, E4, E15.

**Follow-up 1:** Is failover configured?  
**Answer:** “The screenshot shows it disabled at capture time; current state is unverified.”

**Follow-up 2:** Would you bypass authentication during failure?  
**Answer:** “No. Recovery must preserve the security boundary.”

**Common mistake:** Saying a cache outage merely slows requests.

**Q31. Explain the Dockerfile and its main risk.**

**Difficulty:** Intermediate.  
**Why:** Tests build-context understanding.  
**Must understand:** Context, COPY, dependencies, runtime.

**Practice answer:**  
“The image installs backend-root and service dependencies, copies the selected service plus shared code, and starts Node on Alpine. The build context is the backend directory. Nested ignore files do not filter that context, so local sensitive files and dependencies can be included.”

**Evidence:** E18.

**Follow-up 1:** Does `.gitignore` protect the image?  
**Answer:** “No. Docker build filtering is separate.”

**Follow-up 2:** What else would you improve?  
**Answer:** “Reproducible production installs, a non-root user, health checks, and image verification.”

**Common mistake:** Describing these as multi-stage hardened images.

**Q32. How does CI/CD work, and how would you roll back?**

**Difficulty:** Advanced.  
**Why:** Tests release correctness.  
**Must understand:** Mutable tags, revisions, health gates.

**Practice answer:**  
“A push to main builds and pushes five images, forces ECS redeployment, then builds and publishes the frontend. It does not register task JSON changes or wait for application health. Reliable rollback needs immutable image references and known-good task revisions, which this workflow does not establish.”

**Evidence:** E18, E19.

**Follow-up 1:** Does green mean healthy?  
**Answer:** “Only that the configured commands completed.”

**Follow-up 2:** What is your first improvement?  
**Answer:** “Versioned releases with stability and smoke-test gates before promotion.”

**Common mistake:** Claiming automated zero-downtime rollback.

**Q33. What monitoring exists?**

**Difficulty:** Intermediate.  
**Why:** Tests observability precision.  
**Must understand:** Logs versus metrics/traces.

**Practice answer:**  
“Gateway uses Morgan, services log to the console, and ECS task definitions configure CloudWatch logs. There are no implemented distributed traces, correlation IDs, quality metrics, or alarm definitions. Some logged content is sensitive and should be redacted.”

**Evidence:** E3, E7, E19.

**Follow-up 1:** What would you monitor first?  
**Answer:** “Request failures and latency by workflow, provider failures, resource pressure, and payment reconciliation.”

**Follow-up 2:** Why are HTTP metrics insufficient?  
**Answer:** “Specialist failures can currently return HTTP 200.”

**Common mistake:** Equating CloudWatch log configuration with full observability.

**Q34. What tests currently exist?**

**Difficulty:** Beginner.  
**Why:** Tests honesty and quality awareness.  
**Must understand:** Scripts versus actual suites.

**Practice answer:**  
“The frontend has lint and build scripts, but I did not find a substantive automated application test or AI evaluation suite. Manual screenshots and deployment checklists are supporting evidence, not regression tests.”

**Evidence:** Manifests, frontend ESLint configuration, E18.

**Follow-up 1:** What would you test first?  
**Answer:** “Authorization, payment replay, concurrent credits, and failure contracts.”

**Follow-up 2:** How would you test model-dependent behavior?  
**Answer:** “Use deterministic integration boundaries plus representative live evaluation cases.”

**Common mistake:** Claiming tests pass because the UI once worked.

**Q35. The application returns HTTP 500. What do you do?**

**Difficulty:** Advanced.  
**Why:** Tests systematic isolation.  
**Must understand:** Request stages and error defects.

**Practice answer:**  
“I would capture the failing workflow and response, then follow Gateway, Agent, Chat, and Auth evidence. I would isolate upload, routing, provider, storage, or final-persistence failure before changing anything. The generic Agent error handler itself also references an undefined variable, so error reporting can obscure the original cause.”

**Evidence:** E7 and downstream references.

**Follow-up 1:** Would you retry immediately?  
**Answer:** “Only after checking whether earlier side effects already occurred.”

**Follow-up 2:** How would you verify a fix?  
**Answer:** “Exercise the successful path and the original failure case, checking data and accounting consistency.”

**Common mistake:** Restarting everything without isolating the cause.

**Q36. ECS tasks keep restarting. How do you investigate?**

**Difficulty:** Advanced.  
**Why:** Tests deployment troubleshooting.  
**Must understand:** Startup failure versus resource exhaustion.

**Practice answer:**  
“I would inspect ECS stopped reasons, exit codes, events, and the corresponding log stream. Then I would distinguish missing secrets or eager client initialization errors from memory exhaustion, health-check failure, or repeated deployment. Resource increases should follow evidence.”

**Evidence:** E9, E18, E19.

**Follow-up 1:** Does a root endpoint prove readiness?  
**Answer:** “No. Database connections start after listening, and root responses do not check all dependencies.”

**Follow-up 2:** What happens to in-flight jobs?  
**Answer:** “They are not durably resumed.”

**Common mistake:** Treating every restart as insufficient memory.

**Q37. The LLM is slow. How do you investigate?**

**Difficulty:** Advanced.  
**Why:** Tests measurement and latency decomposition.  
**Must understand:** More than model time contributes.

**Practice answer:**  
“I would measure routing, history retrieval, provider latency, artifact rendering, S3, and persistence separately. Automatic routing and coding classification add calls. PDF ingestion adds parsing and embeddings. The repository lacks those stage metrics, so I would add instrumentation before claiming the bottleneck.”

**Evidence:** E7–E16.

**Follow-up 1:** Would streaming solve it?  
**Answer:** “It can improve perceived responsiveness, but does not remove slow work or provider failures.”

**Follow-up 2:** What limits would help?  
**Answer:** “Deadlines, bounded concurrency, and provider-aware admission control.”

**Common mistake:** Assuming all latency is caused by the final LLM.

**Q38. What happens at ten times the traffic?**

**Difficulty:** Advanced.  
**Why:** Tests scaling beyond replica counts.  
**Must understand:** Quotas, state, concurrency, capacity.

**Practice answer:**  
“I cannot provide a capacity number without load tests. More replicas could help HTTP concurrency, but provider quotas, Redis, database queries, file processing, and accounting races remain. I would fix correctness, measure representative workloads, then scale the limiting stage.”

**Evidence:** E4, E6, E11, E15, E19.

**Follow-up 1:** What scales independently?  
**Answer:** “The five services can be replicated separately in principle.”

**Follow-up 2:** What needs durable workers?  
**Answer:** “Long jobs that must survive restarts or wait safely under load.”

**Common mistake:** Claiming horizontal scaling alone solves correctness and quotas.

**Q39. How would you reduce cost?**

**Difficulty:** Advanced.  
**Why:** Tests cost-aware engineering.  
**Must understand:** Baseline infrastructure plus variable provider usage.

**Practice answer:**  
“I would measure infrastructure spend and per-workflow provider usage. Likely opportunities include avoiding repeated PDF embedding, controlling context size, eliminating unnecessary routing calls when the user explicitly chooses a workflow, applying artifact retention, and sizing resources from actual load. I would not promise savings without measurements.”

**Evidence:** E8–E19.

**Follow-up 1:** Do credits equal actual cost?  
**Answer:** “No. They are fixed application prices.”

**Follow-up 2:** What is a hidden cost risk?  
**Answer:** “Provider work continues when credit deduction fails.”

**Common mistake:** Repeating unverified monthly estimates from old notes.

**Q40. What would you change before calling it production-ready?**

**Difficulty:** Advanced.  
**Why:** Tests prioritization and engineering maturity.  
**Must understand:** Correctness before expansion.

**Practice answer:**  
“I would first fix public mutations, admin routing, resource ownership, and exposed credentials. Next I would make payments and credits idempotent and atomic, repair sessions and errors, and add regression tests. Then I would improve document lifecycle, deployment gates, telemetry, and measured resilience.”

**Evidence:** Entire report.

**Follow-up 1:** Would you add Kubernetes or more agents first?  
**Answer:** “No. Those additions do not solve the current highest-impact failures.”

**Follow-up 2:** What is your largest uncertainty?  
**Answer:** “Live operational behavior and performance remain unverified because the repository cannot prove them.”

**Common mistake:** Treating more technologies as evidence of production maturity.

---

**25. Interview chains**

**Product to architecture**

Q1 → Q3 → Q4 → Q5 → Q38 → Q39 → Q40.

**Agent claim under pressure**

Q10 → Q9 → Q12 → Q11 → Q13 → Q14 → Q37.

**RAG deep dive**

Q15 → Q16 → Q17 → Q18 → Q23 → Q38.

**Security boundary**

Q6 → Q7 → Q8 → Q28 → Q31 → Q34.

**Payment correctness**

Q25 → Q24 → Q35 → Q33 → Q40.

**AWS operations**

Q26 → Q27 → Q28 → Q32 → Q36 → Q30.

Use these as code-walkthrough exercises. Each answer should lead naturally to the next implementation detail.

---

**26. Top interview questions**

**Top 10 you absolutely must answer**

Selected because they cover the project’s defining implementation and its most consequential weaknesses:

1. Q1 — What is the project?
2. Q2 — What did you personally implement?
3. Q3 — What is the architecture?
4. Q4 — What happens after Send?
5. Q9 — What does the LangGraph graph actually do?
6. Q15 — Where exactly does retrieval happen?
7. Q17 — Can PDF follow-ups retrieve the same document?
8. Q7 — Where are the authorization gaps?
9. Q32 — What does deployment automation actually guarantee?
10. Q40 — What prevents production readiness?

**Top 20 technical questions**

1. Q4 — Request lifecycle.
2. Q6 — Authentication.
3. Q7 — Authorization.
4. Q8 — Session revocation.
5. Q9 — Graph/state.
6. Q12 — Routing precedence.
7. Q13 — Providers/models.
8. Q15 — RAG implementation.
9. Q16 — Chunking.
10. Q17 — Document persistence.
11. Q18 — RAG evaluation.
12. Q20 — Code artifacts.
13. Q21 — Generated files/S3.
14. Q23 — Redis memory.
15. Q24 — Limits/credits.
16. Q25 — Payment idempotency.
17. Q27 — AWS networking.
18. Q28 — IAM/secrets.
19. Q31 — Docker context.
20. Q32 — Release/rollback.

**Top advanced/pressure questions**

- “You said agentic. Where is the autonomous loop?” — Q10.
- “You said RAG. Show me the retrieval call.” — Q15.
- “How does the second PDF question find the first collection?” — Q17.
- “Can one user access another conversation?” — Q7.
- “What stops a payment callback granting credits twice?” — Q25.
- “What happens when credit deduction fails?” — Q24.
- “Why does a green deployment not prove readiness?” — Q32.
- “How do you know the application supports ten times the traffic?” — Q38.
- “Which AWS permissions have you actually verified?” — Q28.
- “What did you personally build?” — Q2.

---

**27. Verified project fact sheet**

**PROJECT NAME:** NovaMind AI; CortexAI remains in some internal prompts/metadata.

**PROJECT TYPE:** Full-stack AI workspace with multiple specialist workflows.

**PURPOSE:** Integrate conversational AI, retrieval, search, coding, and content creation behind a shared account/UI.

**TARGET USERS:** Learners, developers, and document/content users inferred from features; market adoption unverified.

**ARCHITECTURE STYLE:** Five containerized Express services with synchronous HTTP dependencies; one React SPA.

**MAIN ENTRY POINT:** Browser UI; backend traffic enters Express Gateway on port 8000.

**LANGUAGES:** JavaScript/JSX, CSS, JSON/YAML configuration; Python for diagram tooling.

**FRAMEWORKS:** React, Express, LangGraph; Vite build tooling.

**IMPORTANT LIBRARIES:** LangChain integrations, Mongoose, ioredis, Axios, Multer, Firebase SDKs, Razorpay, PDFKit, PptxGenJS, AWS SDK.

**FRONTEND:** React/Redux, Google sign-in, chat, billing, admin, artifact viewing.

**BACKEND:** Gateway, Auth, Chat, Agent, Billing.

**APIs:** Auth, current user, conversations/messages, agent chat/upload, billing, administration.

**AI/ML:** External inference, embeddings, tool integration, and retrieval. No training/MLOps pipeline.

**AWS/CLOUD:** S3 application integration; ECS/ECR/CloudFront/Secrets Manager/IAM/CloudWatch deployment configuration; ElastiCache/Cloud Map references; documented ALB/VPC/NAT design.

**DATABASE/STORAGE:** MongoDB, Redis, Qdrant, S3, temporary local disk.

**EXTERNAL SERVICES:** Firebase, Groq, Gemini, OpenRouter/DeepSeek, Tavily, Stability, Razorpay, MongoDB Atlas, Qdrant Cloud.

**DEVOPS:** Five Dockerfiles and GitHub Actions release workflow.

**TESTING:** Frontend lint/build scripts; no substantive automated application or AI evaluation suite found.

**MAIN REQUEST FLOW:** Browser → Gateway session check → Agent → persist input → graph/specialist → memory/output persistence → JSON response.

**STATE/MEMORY:** MongoDB durable records, Redis sessions/context/counters, per-request graph state; no durable graph checkpoint.

**AUTHENTICATION:** Firebase verification plus opaque Redis-backed session cookie.

**AUTHORIZATION:** Partial; important route and ownership defects.

**DEPLOYMENT:** Fargate task definitions and deployment automation; current live health unverified.

**MONITORING:** Console/Morgan logging and ECS `awslogs`; tracing/alarms not implemented in repository.

**IMPORTANT VISUAL ASSETS:** Technical architecture diagram, poster, historical AWS/CI screenshots, application examples; several older captions/diagrams are inaccurate.

**IMPLEMENTED:** Core UI/service integrations, LangGraph, PDF retrieval, artifacts, provider calls, persistence, deployment definitions.

**PARTIAL:** Security, credits, payments, sessions, memory, document lifecycle, reliability, observability.

**DOCUMENTED/INTENDED:** Network provisioning, some IAM/TLS settings, manual operational procedures.

**FUTURE/PROPOSED:** Atomic accounting, durable document mapping, evaluations, reliable jobs, immutable releases, tested resilience.

**UNVERIFIED:** Current deployment, real permissions, model availability, paid production use, performance, cost, capacity.

**NOT PRESENT:** Active Bedrock integration, autonomous planning loop, graph checkpointing, generated-code backend execution, comprehensive IaC/testing/MLOps.

**TOP STRENGTHS:** End-to-end integration, genuine retrieval, explicit workflows, multimodal outputs, deployment artifacts.

**TOP GAPS:** Authorization, credential exposure, accounting consistency, failure handling, missing verification.

**TOP PRODUCTION PRIORITIES:** Secure boundaries → correct accounting/sessions → regression tests → lifecycle/reliability → release gates and observability.

**PERSONAL OWNERSHIP MUST BE CONFIRMED BY THE USER.**