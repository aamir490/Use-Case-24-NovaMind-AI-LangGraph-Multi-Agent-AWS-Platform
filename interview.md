# NovaMind AI — Interview Preparation

Grounded in the checked-in codebase, `task-defs/`, CI workflow, and `deploy-guide-aws-original.md`. Separates **what runs today** from **what the AWS guide describes** you must provision manually.

---

## Project story (Problem → Production)

**Problem.** Users bounce between chat apps, search tabs, IDEs, slide tools, and PDF viewers. Nothing ties identity, billing, and history together.

**Architecture choice.** I split the backend into five services so identity, persistence, AI orchestration, and payments can evolve independently. The **gateway** is the only browser-facing API: it validates a Redis-backed session cookie and forwards `x-user-id` so downstream services stay simple.

**Development.** The frontend is React with Redux for conversations and messages. Firebase handles Google OAuth in the browser; the auth service verifies ID tokens and mints server sessions. The chat service owns MongoDB models for conversations and messages. The agent service owns LangGraph and all third-party AI integrations.

**Agentic AI.** I used LangGraph not for autonomous planning, but to make routing explicit: a router node, eight specialists, and one important chain (`search → chat`) so web answers are synthesised from Tavily results instead of hallucinated from the model alone.

**AWS.** Containers are Node 22 Alpine. Task definitions target ECS Fargate, Cloud Map for internal DNS, ElastiCache for Redis, ECR for images, Secrets Manager for keys, S3 + CloudFront for the static UI, and an ALB in front of the gateway. GitHub Actions on `main` rebuilds images, redeploys ECS services, syncs the Vite build to S3, and invalidates CloudFront.

**Testing.** There is no real automated test suite yet—only a placeholder npm test script. I relied on manual flows: login, each agent type, billing, admin.

**Production honesty.** The repo is **deployment-ready configuration**, not proof every AWS resource is healthy. I would verify ALB target health, Redis connectivity, secret injection, and cross-origin cookies before calling it production-grade. I also documented known gaps: chat ownership checks, exposed auth mutation routes, and secrets that must be rotated out of task definitions.

---

## 4–5 minute explanation (speak naturally)

Use this as a script outline—not word-for-word documentation.

> I built NovaMind AI as a credit-based multi-agent workspace—think one authenticated UI where you can chat, run web research, generate code projects, create PDFs and PowerPoints, generate images, ask questions over an uploaded PDF, or analyse an uploaded image.
>
> On the frontend I used React with Vite and Redux. Users sign in with Google through Firebase; the client sends the Firebase ID token to my API gateway, which proxies to the auth service. Auth verifies the token with Firebase Admin, upserts the user in MongoDB, and stores a seven-day session in Redis behind an HTTP-only cookie. Every protected API call goes through the gateway, which loads that session and forwards the user id to microservices in a header—so chat, agent, and billing never parse cookies themselves.
>
> The interesting part is the agent service. I modelled workflows with LangGraph: a router node first. If the user picked an agent in the UI, I honour that. If they attached a PDF or image, I route to PDF RAG or image analysis regardless. Otherwise a Groq model classifies the prompt into chat, search, coding, PDF, PPT, or vision. Each node is a focused pipeline—search calls Tavily and then hands results to the chat node so the final answer is grounded in retrieved text. Coding uses DeepSeek via OpenRouter and can return a JSON file tree rendered in Monaco. PDF and PPT agents ask the LLM for structured JSON, render binaries with PDFKit and PptxGenJS, upload to S3, and return presigned links. Vision refines the prompt with Groq, calls Stability’s API, and stores PNGs in S3. PDF RAG chunks the document, embeds with Gemini, writes a fresh Qdrant collection per upload, retrieves top chunks, and answers with strict context-only prompting.
>
> Persistence is MongoDB Atlas—users, messages, payments. Redis holds sessions, a rolling window of the last twenty messages per conversation for prompt context, and per-minute rate limits. Credits are enforced in the auth service; agents call deduct-credits after successful work. Billing integrates Razorpay with HMAC verification and then updates plan and credits internally.
>
> For AWS I containerised all five backend services. The intended layout is ECS Fargate behind an ALB for the gateway, Cloud Map DNS between services, ElastiCache for Redis, ECR for images, Secrets Manager for sensitive env vars, and S3 plus CloudFront for the static frontend. CI is GitHub Actions: build and push five images, force ECS redeployments, build the frontend with Vite env vars baked in, sync to S3, invalidate CloudFront.
>
> Trade-offs I’m transparent about: routing is deterministic, not a self-correcting agent loop; generation is synchronous; and I’d harden internal auth routes, add conversation ownership checks, and move long-running jobs to a queue before calling it enterprise-ready. That’s the system I designed, built, deployed, and debugged end to end.

---

## Agentic AI — how to explain it in interviews

### Why this counts as “agentic”

- **Specialised behaviours** selected by rules + LLM classification.
- **Tool invocation** (Tavily, Stability, Qdrant, S3, local PDF/PPT builders).
- **Shared state** carried through LangGraph (`searchResults`, `artifacts`, `file`, etc.).
- **Multi-step workflow** where search retrieval is separated from answer generation.

### Why it is not “full autonomy”

- No open-ended tool loop or planner that revisits goals.
- No reflection/retry agent or human approval gate.
- Single request/response HTTP path—no background workers or streaming tokens.

### Decision flow (memorise order)

1. Explicit agent from UI (unless `auto`).
2. PDF MIME → `pdfRag`.
3. Image MIME → `imageAnalyzer`.
4. Groq router → one of six labels.
5. Execute node → rate limit → work → deduct credits → persist.

### Context and state

- **Short memory:** Redis list, max 20 messages; hydrated from chat DB on cache miss.
- **Long memory:** MongoDB messages per conversation.
- **Uploads:** temp disk on agent container; deleted in `finally`.

### Error handling

- Rate limits throw structured 429 from agent middleware.
- Many agents catch errors and return friendly `aiResponse` strings instead of failing the HTTP request.
- Credit deduction failures are logged but **not** propagated from `deductCredits.js` util.

### Limitations to admit confidently

- Router LLM can return invalid labels; graph defaults toward chat via switch default.
- PDF RAG creates a new Qdrant collection every time—no cleanup.
- Chat APIs don’t verify the conversation belongs to the caller.
- No streaming; long PDF/PPT/image jobs risk gateway timeouts.

---

## Interview Q&A

### Architecture

**Q: Why microservices instead of a monolith?**  
A: Identity, chat CRUD, AI orchestration, and payments have different scaling and failure profiles. The agent service pulls heavy dependencies (LangChain, PDF libs, S3). Isolating it limits blast radius and lets me redeploy AI changes without touching billing. Cost is operational complexity—Cloud Map URLs, five containers, shared Redis.

**Q: Why an API gateway?**  
A: Single CORS origin and cookie domain, one place for session validation, and consistent injection of `x-user-id`. The browser never talks to internal service ports directly.

**Q: How do services find each other locally vs AWS?**  
A: Environment variables. Localhost URLs in `.env`; ECS task definitions use Cloud Map hostnames like `novamind-chat.novamind.local:8002`.

**Follow-up:** What happens if Redis is down?  
Session validation fails at gateway → users cannot call protected APIs. Agent memory and rate limits also break.

**Difficult:** How would you secure service-to-service calls?  
Today they’re trust-on-LAN HTTP. I’d add an internal HMAC or mTLS on a private subnet, and never expose auth mutation routes on the public auth prefix.

---

### Agentic AI and LangGraph

**Q: Why LangGraph instead of a single prompt with function calling?**  
A: The product has distinct pipelines with different tools and post-processing. The graph makes branching explicit and gives a clean `search → chat` composition without nesting callbacks in one handler.

**Q: How many agents?**  
A: Eight graph nodes: router plus seven specialists (chat, search, coding, pdf, ppt, vision, pdfRag, imageAnalyzer)—router is not a user-facing “agent” but a node.

**Why LangGraph vs plain Express switch?**  
LangGraph gives a maintainable state object and conditional edges; for this scale a switch would work, but the graph documents workflow structure for future async nodes.

---

### LLMs and prompt engineering

**Q: Which model for what?**  
A: Groq `openai/gpt-oss-120b` for chat, routing, search synthesis, and vision prompt refinement. Gemini `gemini-2.0-flash` for multimodal image Q&A. Gemini embeddings for RAG. OpenRouter DeepSeek for coding.

**Q: How do you reduce hallucination in search?**  
A: Tavily results are injected into the chat system prompt with instructions to use only that context. It’s prompt grounding—not citation verification or reranking.

**Q: PDF RAG prompts?**  
A: System message restricts answers to uploaded context with a fixed fallback sentence if missing.

**Follow-up:** Do you use Bedrock?  
No—Bedrock SDK is in package.json but unused; all inference is via Groq, Google, OpenRouter, Stability, Tavily, Qdrant.

---

### Tool calling

**Q: Is Tavily “tool calling”?**  
A: It’s invoked imperatively via LangChain’s Tavily tool in the search node—not dynamic OpenAI-style tool selection. Same for Stability `fetch` and Qdrant vector store helpers.

---

### RAG

**Q: Walk through PDF RAG.**  
A: Multer saves PDF → pdf-parse text → 1000-char chunks, 200 overlap → embed with Gemini → new Qdrant collection → similarity search top 5 → Groq answers with context-only system prompt → temp file deleted.

**Q: Do you reuse vectors across sessions?**  
A: Not in current code—each upload creates `pdf-{timestamp}` collection without deletion logic.

---

### APIs and backend

**Q: Main agent endpoint?**  
A: `POST /api/agent/chat` multipart: `prompt`, `conversationId`, `agent`, optional `file`.

**Q: How are messages stored?**  
A: Agent calls chat service `save-message` before and after graph execution; chat writes MongoDB `Message` documents.

**Q: Credit costs?**  
A: chat 1, search 5, coding/pdf/ppt/vision 10 (auth service map). Rate limits separate in Redis.

---

### Frontend

**Q: How is auth persisted in the UI?**  
A: Redux `userSlice` hydrated from `GET /api/me` on load; login updates from auth response.

**Q: Coding output UX?**  
A: Artifacts array with files rendered in Monaco side panel (`Artifact.jsx`).

**Q: Admin security?**  
A: Route guard checks email client-side; real enforcement is `adminProtect` on auth service comparing `ADMIN_EMAIL`.

---

### Docker

**Q: Why is Docker build context `backend/`?**  
A: Dockerfiles copy `shared/redis` alongside each service. Building from the service folder alone breaks `COPY shared`.

**Q: Local Redis?**  
A: Only Redis runs in Compose; app processes run on host with nodemon.

---

### AWS, ECS, ECR

**Q: CI/CD flow?**  
A: On push to `main`, build five images, tag/push to ECR, force ECS service deployment per secret names, then frontend build → S3 sync → CloudFront invalidation.

**Q: Fargate sizing?**  
A: Gateway/auth/chat/billing 512 CPU / 1 GB; agent 1024 CPU / 2 GB for heavier workloads.

**Q: Why force new deployment?**  
A: Same `:latest` tag—ECS needs forced rollout to pull fresh digest.

---

### CloudFront

**Q: What does CloudFront serve?**  
A: Static React assets from S3—not the API. `VITE_SERVER_URL` must point to the gateway ALB.

**Follow-up:** Why invalidate `/*`?  
Ensures users get new JS bundles after deploy; API unaffected.

---

### Cloud Map

**Q: Purpose?**  
A: Stable internal DNS for service mesh–less microservices in private subnets—replaces localhost in task env vars.

---

### IAM

**Q: Task role vs execution role?**  
A: Execution role pulls ECR images and writes logs; agent task role grants S3 access for artifact upload; auth has task role for secret access pattern in guide.

---

### Networking

**Q: How do private tasks reach MongoDB and Groq?**  
A: NAT gateway outbound (described in guide)—private subnets without public IPs.

**Q: Where is HTTPS terminated?**  
A: ALB for API; CloudFront for static site (guide)—certificates not in repo.

---

### Authentication and security

**Q: Cookie settings in production?**  
A: `httpOnly`, `secure`, `SameSite=None` for cross-site frontend on CloudFront calling API on another domain.

**Q: Biggest auth vulnerability?**  
A: `/api/auth` proxy without gateway `protect` exposes `/deduct-credits` and `/update-plan` to anyone who can reach the auth service URL.

---

### Monitoring, scalability, cost

**Q: Observability today?**  
A: CloudWatch container logs and Morgan on gateway—no custom metrics or tracing in code.

**Q: Scale agent service?**  
A: Horizontally scale ECS tasks behind internal load balancing; shared Redis and Mongo become contention points; rate limits help abuse.

**Q: Cost optimisations?**  
A: Right-size Fargate tasks, ElastiCache node type, CloudFront caching for static assets, presigned S3 instead of proxying files, Qdrant collection cleanup to avoid storage creep.

---

### Deployment and debugging

**Q: Vite env mistake symptom?**  
A: Frontend built with wrong `VITE_SERVER_URL` → API calls go to localhost or wrong host from users’ browsers.

**Q: CORS/cookie symptom?**  
A: `FRONTEND_URL` mismatch → browser blocks credentials or session not sent.

**Q: ECS task fails to start?**  
A: Check CloudWatch log group, secret ARN, Redis security group, and image pull permissions on execution role.

---

### Design decisions — “Why X instead of Y?”

| Question | Answer |
| --- | --- |
| Redis + MongoDB vs Mongo only? | Sessions and rate counters need fast TTL semantics; chat history stays durable in Mongo. |
| Groq for router vs rules only? | Natural language intent needs flexibility; rules handle files and explicit UI selection first. |
| Razorpay vs Stripe? | Implemented Razorpay with INR plan table in code. |
| Presigned S3 vs streaming through gateway? | Offloads bandwidth; keeps bucket private. |
| LangGraph vs Temporal/Step Functions? | LangGraph fits in-process Node orchestration; no external workflow engine in scope. |
| Monorepo microservices vs separate repos? | Single repo simplifies portfolio delivery and shared Redis module. |

---

### Troubleshooting scenarios (practice aloud)

1. **User logged in but 400 unauthorized on chat.** Session cookie missing or Redis key expired; check `FRONTEND_URL`, `SameSite`, HTTPS, and ElastiCache connectivity from gateway.

2. **Search works but ignores current events.** Tavily failure returns empty results; chat may answer generically—check Tavily key and agent logs.

3. **Payment verified but credits unchanged.** Billing calls auth `/update-plan` over internal URL; if auth unreachable or route abused/blocking, credits won’t update—trace billing → auth HTTP status.

4. **PDF RAG slow/timeouts.** Large PDF embedding + Qdrant insert synchronously in request path—candidate for async job queue.

5. **Generated PDF link expired.** Presigned URL TTL vs message text mismatch—pdf agent passes `24*60` seconds while UI text says ten minutes.

---

### Difficult interviewer questions

- **Is this production-ready?** Configuration and CI exist; I would not claim production-ready until secrets are scrubbed, auth routes locked down, ownership checks added, tests and alarms exist, and live AWS verified.

- **How do you prevent prompt injection in RAG?** Context-only prompting reduces but does not eliminate injection; would add input sanitisation, chunk scoring thresholds, and logging.

- **Why no streaming?** Not implemented—would add SSE from agent through gateway and adjust load balancer idle timeout.

- **Single point of failure?** Gateway and Redis are critical; would add Redis replication and multi-AZ ECS for gateway.

---

## Questions to ask the interviewer

- What SLO do you target for interactive agent latency vs document generation?
- Is cross-origin cookie auth acceptable long term, or should we move to BFF-only same-site hosting?
- What compliance requirements apply to user-uploaded PDFs/images?
- Do you standardise on one observability stack (OpenTelemetry, Datadog)?

---

## Claims to avoid

- Autonomous multi-agent collaboration or self-healing tool loops.
- All five services using Redis (only gateway, auth, agent).
- AWS Bedrock in the inference path.
- Live AWS deployment verified solely from screenshots or task defs.
- IaC, autoscaling, WAF, or Razorpay webhooks in the current codebase.
- `deploy-guide-aws.md` in git (gitignored)—reference `deploy-guide-aws-original.md` or your local copy.

---

## Quick reference tables

**Ports:** 8000 gateway · 8001 auth · 8002 chat · 8003 agent · 8004 billing · 6379 Redis (local)

**Plans (INR):** free 100 credits · starter ₹199 / 500 · pro ₹499 / 1000

**Rate limits (per user / minute):** chat 20 · others 5

**Graph edge:** `search → chat` only multi-node chain

---

## Stability AI — Image Generation (updated)

### What changed and why

Originally the vision agent used **Amazon Nova Canvas** via Bedrock. After deployment it returned a `LEGACY` model error — Nova Canvas was retired and marked inaccessible for accounts that hadn't used it in 30 days. It was replaced with the **Stability AI REST API** (`stable-image/generate/core` endpoint).

**Q: Why Stability AI over Bedrock for image generation?**  
A: Nova Canvas was the only text-to-image model available on Bedrock in `us-east-1` and it became legacy. Stability AI's direct API is actively maintained, has a free tier (25 credits), and the integration is a simple `fetch` call — no SDK dependency change needed.

**Q: How does the vision agent work now?**  
A:
1. Groq refines the user's raw prompt into a detailed cinematic image prompt.
2. A `fetch` POST to `https://api.stability.ai/v2beta/stable-image/generate/core` with `Authorization: Bearer` header.
3. Response is raw binary PNG data (`Accept: image/*`).
4. Buffer uploaded to S3 via `PutObjectCommand`.
5. `GetObjectCommand` presigned URL returned to user (expires 24 hours).

**Q: How is the API key handled in production?**  
A: Stored in AWS Secrets Manager as `novamind/agent/stability-api-key`, injected as `STABILITY_API_KEY` env var into the ECS agent task at startup. Never hardcoded.

**Q: What happens if Stability AI is down?**  
A: The `fetch` throws or returns a non-200 status; the agent catches it and returns a friendly error string as `aiResponse` — same error boundary pattern as all other agents.

---

## GitHub Actions CI/CD — Deep Dive

### Setup steps completed

1. Installed GitHub CLI: `winget install --id GitHub.cli`
2. Authenticated: `gh auth login` → browser OAuth → logged in as `aamir490`
3. Fixed `deploy.yml` to pass `VITE_*` env vars to the frontend build step
4. Created all 16 GitHub Secrets via `gh secret set` CLI

### 16 secrets and their purpose

| Secret | Purpose |
|--------|---------|
| `AWS_REGION` | Region for all AWS CLI commands |
| `AWS_ACCOUNT_ID` | ECR image tagging (`{account}.dkr.ecr...`) |
| `AWS_ACCESS_KEY` | mlops-user credentials for ECR login |
| `AWS_SECRET_ACCESS_KEY` | mlops-user credentials for ECR login |
| `ECS_CLUSTER` | `novamind-cluster` — target cluster for deployments |
| `GATEWAY_SERVICE` | ECS service name for gateway |
| `AUTH_SERVICE` | ECS service name for auth |
| `CHAT_SERVICE` | ECS service name for chat |
| `AGENT_SERVICE` | ECS service name for agent |
| `BILLING_SERVICE` | ECS service name for billing |
| `S3_BUCKET` | `novamind-frontend-prod` — frontend sync target |
| `CLOUDFRONT_DISTRIBUTION_ID` | `EBG0WA07U0GG8` — cache invalidation target |
| `VITE_FIREBASE_API_KEY` | Baked into frontend JS bundle at build time |
| `VITE_RAZORPAY_KEY_ID` | Baked into frontend JS bundle at build time |
| `VITE_SERVER_URL` | API base URL baked into frontend at build time |
| `VITE_ADMIN_EMAIL` | Admin email baked into frontend at build time |

### Common CI/CD interview questions

**Q: Why are VITE_* variables GitHub Secrets and not env vars in the container?**  
A: Vite bakes them into the JS bundle at `npm run build` time — they are not runtime env vars. The build runs inside GitHub Actions, so they must be available as environment variables on the Actions runner, not in the Docker container.

**Q: What happens if you change VITE_SERVER_URL?**  
A: You must push to `main` to trigger a rebuild. The old JS bundles in CloudFront must also be invalidated — the pipeline does this automatically with `aws cloudfront create-invalidation --paths "/*"`.

**Q: Why `--force-new-deployment` on ECS?**  
A: All images are tagged `:latest`. ECS won't pull a new image unless forced — it caches the previous digest. Force deployment triggers a rolling replacement: new task starts, old task drains, health check passes, then old task stops.

**Q: How long does the full pipeline take?**  
A: ~8–12 minutes total. Docker builds (5 images in parallel): ~3–4 min. ECR pushes: ~2–3 min. ECS redeployments: ~2–3 min. Frontend build + S3 sync + CloudFront invalidation: ~1–2 min.

**Q: What if one ECS service deployment fails?**  
A: The `aws ecs update-service` call itself rarely fails — it just queues the deployment. The real failure shows up as the new task not reaching `RUNNING` state in ECS. CloudWatch logs for that service show why (bad secret ARN, missing env var, crash on startup).

**Q: How would you add rollback?**  
A: Tag images with the git SHA (`git rev-parse --short HEAD`) in addition to `:latest`. On failure, re-run `ecs update-service` pointing to the previous SHA tag. Currently not implemented — relies on `:latest` only.

---

## System Design — Extended Questions

**Q: How would you add streaming (SSE) to the agent responses?**  
A: Replace the synchronous `graph.invoke()` with `graph.stream()` in LangGraph. The agent route handler writes chunked SSE events. Gateway must not buffer — set `X-Accel-Buffering: no`. ALB idle timeout must be extended (default 60s). Frontend uses `EventSource` or `fetch` with `ReadableStream`. Session and credit deduction stay at the end of stream.

**Q: How would you handle concurrent users hitting the same conversation?**  
A: Currently no locking — two parallel requests to the same `conversationId` could both read the same last-20 messages from Redis and write duplicate responses. Fix: Redis distributed lock on `conversationId` for the duration of graph execution, or optimistic concurrency in MongoDB messages.

**Q: How would you make PDF RAG production-grade?**  
A: 
- Move embedding + Qdrant insert to a background job queue (BullMQ + Redis).
- Store collection name in MongoDB against the conversation.
- Add cleanup job to delete Qdrant collections older than N days.
- Add chunk count limit for very large PDFs.
- Cache embeddings for the same PDF hash.

**Q: How would you scale the agent service under high load?**  
A: ECS service auto-scaling on CPU/memory. Agent is stateless (Redis + Mongo are external). Rate limits per user already in Redis. Bottleneck is LLM API latency — add a request queue with BullMQ, set concurrency limit per LLM provider, and return a job ID to the client for polling.

**Q: What database would you use if MongoDB becomes a bottleneck?**  
A: For user sessions and credits — Redis already handles it. For conversation history — MongoDB works well for document-style messages. For analytics/reporting — push events to a time-series store (DynamoDB or ClickHouse). No change needed at current scale.

**Q: How would you add multi-tenancy (organizations)?**  
A: Add `orgId` to User model. Credit pools at org level in auth service. Conversations scoped to `orgId`. Admin APIs filtered by org. Rate limits keyed by `orgId` instead of `userId` for shared pools.

---

## Behavioral / HR Questions

**Q: Walk me through the biggest technical challenge you faced.**  
A: The S3 `PermanentRedirect` error in production. The bucket `cretexainovamind` is in `us-east-1` but the agent task definition had `AWS_REGION=ap-south-1` hardcoded — so the S3 client was hitting the wrong regional endpoint. Locally it worked because `.env` had the right region. I debugged it by checking `aws s3api get-bucket-location` which returned `null` (AWS's way of saying `us-east-1`), traced the env var through the task definition, and fixed it by correcting the region and redeploying via ECS.

**Q: How did you decide on the microservice boundaries?**  
A: I separated by domain ownership and failure isolation. Auth owns identity, sessions, credits — high security sensitivity. Chat owns conversation persistence — pure CRUD. Agent owns all AI logic and third-party integrations — most likely to change and fail. Billing owns payment flows — compliance boundary. Gateway owns the public interface — single CORS/cookie domain.

**Q: What would you do differently if you started over?**  
A: Add a message queue (BullMQ) from day one for agent jobs so long-running tasks don't block HTTP. Add conversation ownership checks to the chat service. Use infrastructure-as-code (CDK or Terraform) instead of a manual deploy guide. Set up basic integration tests before deployment.

**Q: How do you keep up with AI tooling changes?**  
A: The Nova Canvas retirement is a real example — AWS deprecated it without much warning. I monitor provider changelogs, pin SDK versions in `package.json`, and design provider integrations behind a thin abstraction so swapping (Nova Canvas → Stability AI) is a single file change.

**Q: Describe a time you made a mistake and fixed it.**  
A: Committed real API keys inside `deploy-guide-aws.md` and tried to push to GitHub. GitHub's secret scanning blocked the push. I used `git reset --soft` to squash all commits containing the file into one clean commit without the secrets, then gitignored the file going forward. Lesson: sensitive documentation should be gitignored from the start.

---

## One-liner answers (quick fire round)

| Question | Answer |
|----------|--------|
| What is LangGraph? | A library for building stateful, graph-based AI workflows with nodes and edges |
| What is a StateGraph? | A directed graph where each node reads and writes a shared state object |
| What is Cloud Map? | AWS service discovery — gives containers stable DNS names inside a VPC |
| What is a presigned URL? | A time-limited S3 URL that grants temporary GET/PUT access without AWS credentials |
| What is ElastiCache? | AWS managed Redis — replaces Docker Redis in production |
| What is ECS Fargate? | Serverless container runtime — run Docker containers without managing EC2 |
| What is ECR? | AWS private Docker image registry |
| What is Secrets Manager? | AWS service to store and inject sensitive env vars securely |
| What is a task definition? | ECS blueprint: image, CPU, memory, env vars, secrets, IAM roles, log config |
| What is `force-new-deployment`? | Tells ECS to pull the latest image even if the tag hasn't changed |
| What is `SameSite=None`? | Cookie policy allowing cross-site requests — required when frontend and API are on different domains |
| What is RAG? | Retrieval-Augmented Generation — answer questions using retrieved document chunks as context |
| What is Qdrant? | Vector database for storing and searching embeddings |
| What is a vector embedding? | A numerical representation of text that captures semantic meaning |
| What is Tavily? | A search API optimised for LLM-friendly results |

---

## Architecture decisions — one-line justifications

| Decision | Justification |
|----------|--------------|
| HTTP-only session cookie | Prevents XSS token theft vs localStorage JWT |
| Gateway injects `x-user-id` | Downstream services stay simple; no repeated token parsing |
| LangGraph over plain switch | Explicit state machine; clean `search→chat` composition; extensible |
| Groq for router | Fast inference; cheap; prompt-based routing handles natural language |
| Gemini for embeddings | Best quality embeddings for RAG; same provider as image analysis |
| DeepSeek for coding | Specialised code model; cost-effective via OpenRouter |
| Stability AI for images | Only active text-to-image API available after Nova Canvas retired |
| Per-upload Qdrant collection | Simplest isolation; no cross-user data leak risk |
| `:latest` ECR tag | Simple for a portfolio project; production should use SHA tags |
| 7-day Redis session | Balance between UX (infrequent re-login) and security |
