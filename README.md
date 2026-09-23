<div align="center">

# NovaMind AI

### A multi-agent AI workspace powered by LangGraph and AWS

Chat, search, write code, create documents and images, and ask questions about your files — from one Google-authenticated workspace.

[![Node.js](https://img.shields.io/badge/Node.js-22-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![React](https://img.shields.io/badge/React-19-149ECA?logo=react&logoColor=white)](https://react.dev/)
[![AWS](https://img.shields.io/badge/AWS-ECS_Fargate-FF9900)](https://aws.amazon.com/)
[![Deployment](https://github.com/aamir490/Use-Case-24-NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform/actions/workflows/deploy.yml/badge.svg)](https://github.com/aamir490/Use-Case-24-NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform/actions/workflows/deploy.yml)

**[Live demo](https://d8au5xi32kvkz.cloudfront.net) · [Architecture](#architecture) · [Local setup](#local-development) · [Screenshots](#screenshots)**

</div>

## Overview

NovaMind AI combines **eight specialist agents** with **five Node.js microservices**. A LangGraph router selects a workflow from the user's prompt, chosen agent or uploaded file. The platform includes conversation history, credit-based usage, Razorpay payments and an admin dashboard.

- **Create and research:** general chat, web search, coding, PDF/PPTX generation and image generation.
- **Work with files:** PDF question answering and Gemini image analysis; PDF and image uploads up to 20 MiB.
- **Manage an account:** Google sign-in, Redis-backed sessions, conversation history, credit plans and administration.
- **Deploy on AWS:** ECS Fargate services, S3/CloudFront frontend delivery and GitHub Actions deployment.

To try the demo, sign in with Google, choose an agent or use automatic routing, and send a prompt. For document questions, attach a PDF and ask about its contents.

## Contents

- [Architecture](#architecture)
- [Agents and request flow](#agents-and-request-flow)
- [Technology stack](#technology-stack)
- [Local development](#local-development)
- [AWS deployment](#aws-deployment)
- [Credits and usage limits](#credits-and-usage-limits)
- [Screenshots](#screenshots)
- [Project structure](#project-structure)
- [Documentation](#documentation)

## Architecture

[![NovaMind AI — AWS architecture poster](new-project-pic/novamind-aws-architecture-poster.png)](new-project-pic/novamind-aws-architecture-poster.png)

[View full-size architecture poster](new-project-pic/novamind-aws-architecture-poster.png)

**Numbered architecture walkthrough:**

1. **User access** — React 19 + Vite frontend served by CloudFront and S3. API calls originate from the browser and use the configured API endpoint.
2. **AWS infrastructure** — ALB forwards to Gateway :8000, which independently proxies Auth :8001, Chat :8002, Agent :8003 and Billing :8004. The deployment guide places ECS Fargate tasks in private subnets and ALB/NAT in public subnets. Cloud Map provides internal service discovery.
3. **Shared AWS services** — ElastiCache stores sessions, agent memory and rate limits; CloudWatch collects container logs; IAM grants task permissions; S3 stores generated artifacts.
4. **LangGraph agents** — Eight specialist nodes run inside the Agent service. Routing priority: explicit choice → PDF → image → Groq classifier. Search chains into Chat; Vision generates images with Stability AI, while Image Analyzer uses Gemini.
5. **External providers** — Groq, Gemini, OpenRouter/DeepSeek, Tavily, Stability AI, Qdrant Cloud, MongoDB Atlas, Firebase and Razorpay supply AI, data, identity and payment services.
6. **PDF RAG** — Parse uploaded PDF → split text → Gemini embeddings → Qdrant vectors → top-five similarity retrieval → context and prompt → Groq answer.
7. **Security and observability** — Secrets Manager injects startup secrets; IAM execution/task roles govern access; CloudWatch receives logs from all five services; Redis supports session validation.
8. **Backend deployment** — Push to `main` → GitHub Actions builds and pushes five images to ECR → ECS force redeployments.
9. **Frontend deployment** — After the backend job commands complete, build React → sync to S3 → invalidate CloudFront.
10. **User results** — Return answers, images and documents, with presigned S3 URLs for generated artifacts.

**Scope:** Architecture is based on application source, `task-defs/*.json`, `.github/workflows/deploy.yml` and the AWS deployment guides; network topology is not live-verified. The poster is an AI-generated illustration styled after the supplied reference. AWS and provider marks in it are illustrative; the [technical SVG](new-project-pic/novamind-aws-architecture.svg) uses original [official AWS icon assets](new-project-pic/aws-icons/README.md).


## Agents and request flow

The graph combines conditional routing with specialized workflows. All eight nodes execute inside the **Agent service**, using shared state for the prompt, file, selected agent and results.

| Agent | Trigger | Tools Used |
|-------|---------|-----------|
| 🗨️ **Chat** | General conversation, Q&A | Groq LLM |
| 🔍 **Search** | Current events, latest news | Tavily API → Groq synthesis |
| 💻 **Coding** | Code generation, debugging | DeepSeek via OpenRouter |
| 📄 **PDF** | Generate document | Groq + PDFKit + S3 |
| 📊 **PPT** | Generate presentation | Groq + PptxGenJS + S3 |
| 🎨 **Vision** | Generate image | Groq prompt refinement + Stability AI |
| 📚 **PDF RAG** | Q&A over uploaded PDF | pdf-parse + Gemini embeddings + Qdrant |
| 🖼️ **Image Analyzer** | Analyze uploaded image | Gemini Vision multimodal |


**Routing priority:** explicit agent selection → PDF upload → image upload → Groq classifier. The Search node hands its results to Chat for synthesis; the other specialists return their results directly to the controller.

```mermaid
sequenceDiagram
    participant U as Browser
    participant G as Gateway :8000
    participant R as Redis
    participant A as Agent :8003
    participant C as Chat :8002
    participant M as MongoDB Atlas
    U->>G: POST /api/agent/chat + session cookie
    G->>R: Validate session
    G->>A: Proxy /chat + x-user-id
    A->>C: Save user message
    C->>M: Persist message
    A->>A: Route and run specialist workflow
    Note over A: Call providers, generate artifacts and deduct credits as needed
    A->>R: Update conversation memory
    A->>C: Save assistant message and artifact metadata
    C->>M: Persist message
    A-->>G: Answer, images, artifacts
    G-->>U: JSON response
```

### PDF question answering

The PDF RAG workflow extracts text with `pdf-parse`, splits it into 1,000-character chunks with 200-character overlap, embeds them with Gemini, and creates a Qdrant collection for the upload. It retrieves the five most similar chunks and asks Groq to answer using that context. The temporary PDF is removed after processing.

### Services

| Service | Port | Responsibility |
|---|---|---|
| Gateway | 8000 | CORS, Redis session validation and reverse proxy |
| Auth | 8001 | Firebase token verification, sessions, credits and admin APIs |
| Chat | 8002 | Conversations and messages in MongoDB |
| Agent | 8003 | LangGraph routing, provider calls, RAG and artifact generation |
| Billing | 8004 | Razorpay orders, payment verification and plan updates |

Gateway forwards authenticated user identity to the private services. Agent calls Chat to save messages and Auth to deduct credits; Billing calls Auth after payment verification to update the user's plan.

## Technology stack

| Layer | Technologies |
|-------|-------------|
| **Frontend** | React 19, Vite 8, React Router 7, Redux Toolkit, Tailwind CSS 4, Axios, Monaco Editor, React Markdown |
| **Backend** | Node.js 22 (ES Modules), Express 5, Mongoose 9, ioredis, Multer, Morgan |
| **AI / Agents** | LangGraph, LangChain, Groq, Google Gemini, OpenRouter (DeepSeek), Tavily, Stability AI, Qdrant |
| **Auth** | Firebase Auth (client) + Firebase Admin (server) + Redis sessions |
| **Documents** | pdf-parse, PDFKit, PptxGenJS |
| **Storage** | AWS S3 (artifacts), MongoDB Atlas (data), Qdrant Cloud (vectors), Redis (sessions + memory) |
| **Infrastructure** | AWS ECS Fargate, ECR, ElastiCache, ALB, CloudFront, S3, Secrets Manager, Cloud Map, IAM, CloudWatch |
| **CI/CD** | GitHub Actions — build 5 Docker images → push ECR → redeploy ECS → build frontend → S3 sync → CloudFront invalidation |


Dependency versions are maintained in [frontend/package.json](frontend/package.json) and the backend service manifests. Model choices are configured in [llmModels.js](backend/services/agent/config/llmModels.js) and [embeddings.js](backend/services/agent/config/embeddings.js).

## Local development

### 1. Prerequisites

- Node.js 22 and npm.
- Docker Desktop with Docker Compose for local Redis.
- MongoDB connection strings and a Firebase project with Google sign-in enabled.
- Provider credentials for the features you intend to use: Groq, Gemini, OpenRouter, Tavily, Stability AI and Qdrant.
- An S3 bucket and AWS credentials for generated files; Razorpay keys for billing.

### 2. Configure environment files

Create a `.env` beside each `.env.example`: `frontend/`, `backend/gateway/`, and each of `backend/services/auth/`, `chat/`, `agent/`, `billing/`. Keep existing `.env` files if already configured.

| Location | Configuration |
|---|---|
| Frontend | `VITE_SERVER_URL=http://localhost:8000`, Firebase API key, Razorpay public key and admin email |
| Gateway | Port 8000, `FRONTEND_URL=http://localhost:5173`, Redis URL and four service URLs |
| Auth | Port 8001, MongoDB URI, Redis URL, admin email and Firebase service account |
| Chat | Port 8002 and MongoDB URI |
| Agent | Port 8003, MongoDB/Redis URLs, Auth/Chat URLs, AI keys, Qdrant URL/key and S3 configuration |
| Billing | Port 8004, MongoDB URI, Auth URL and Razorpay key ID/secret |

Use `NODE_ENV=development`, `REDIS_URL=redis://localhost:6379`, and these local service endpoints wherever required:

```dotenv
AUTH_SERVICE=http://localhost:8001
CHAT_SERVICE=http://localhost:8002
AGENT_SERVICE=http://localhost:8003
BILLING_SERVICE=http://localhost:8004
```

Additional setup beyond the example files:

- **Firebase:** place the service account at `backend/services/auth/serviceAccountKey.json`, or supply its JSON through `FIREBASE_SERVICE_ACCOUNT`. Match the browser Firebase project configuration in [frontend/utils/firebase.js](frontend/utils/firebase.js) to your project.
- **Image generation:** add `STABILITY_API_KEY` to the Agent environment; it is not included in the current example file.
- **Admin data:** add `BILLING_MONGODB_URI` and `CHAT_MONGODB_URI` to Auth for the cross-service admin views.
- **S3:** configure `AWS_REGION` and `AWS_BUCKET_NAME`. The explicit local credential path expects `AWS_ACCESS_KEY_ID` and `AWS_SECRET_KEY`; when omitted, the SDK uses its default credential chain.

`VITE_*` values are included in the browser build. Use them for public client configuration, and keep server API secrets in backend environments.

### 3. Install dependencies

Run these commands from the repository root. The shared backend package is required by the Redis client.

```sh
npm --prefix backend ci
npm --prefix backend/gateway ci
npm --prefix backend/services/auth ci
npm --prefix backend/services/chat ci
npm --prefix backend/services/agent ci
npm --prefix backend/services/billing ci
npm --prefix frontend ci
```

### 4. Start Redis and the application

From the repository root:

```sh
docker compose -f backend/docker-compose.yml up -d
```

Start each process below in a **separate terminal**, with every terminal initially at the repository root. Running within each service directory ensures `.env` and upload paths resolve correctly.

```sh
# Terminal 1
cd backend/services/auth
npm run dev

# Terminal 2
cd backend/services/chat
npm run dev

# Terminal 3
cd backend/services/agent
npm run dev

# Terminal 4
cd backend/services/billing
npm run dev

# Terminal 5
cd backend/gateway
npm run dev

# Terminal 6
cd frontend
npm run dev
```

Open **[localhost:5173](http://localhost:5173)**. The gateway root at [localhost:8000](http://localhost:8000) returns a basic response; it does not check every downstream dependency. Sign in and send a Chat message to exercise the complete request path.

### Checks and common setup issues

```sh
npm --prefix frontend run lint
npm --prefix frontend run build
```

These are frontend checks. The repository does not currently provide a backend automated test suite.

- **Redis connection fails:** confirm Docker is running and the local Redis port is 6379.
- **Login succeeds but API calls fail:** confirm `VITE_SERVER_URL`, Gateway `FRONTEND_URL`, and local `NODE_ENV` settings agree. Restart Vite after changing frontend environment values.
- **Provider or artifact calls fail:** check the relevant API key, provider access, S3 bucket region and AWS permissions.
- **Admin data fails to load:** check both admin database connection strings in Auth.

## AWS deployment

Follow the [AWS deployment guide](deploy-guide-aws-original.md) to provision infrastructure, configure service discovery, register task definitions and create ECS services. Adapt the checked-in task definitions to your account and resources before use.

The [GitHub Actions workflow](.github/workflows/deploy.yml) runs on pushes to `main`:

```text
Push to main
  └─ deploy-backend
       ├─ Authenticate to AWS and ECR
       ├─ Build and push five service images
       └─ Force new ECS deployments
            └─ deploy-frontend
                 ├─ Build React with VITE_* configuration
                 ├─ Sync frontend/dist to S3
                 └─ Invalidate CloudFront
```

The frontend job waits for the backend job's commands to finish. The workflow does not wait for ECS service stability or run an automated test suite.

<details>
<summary>GitHub Actions configuration</summary>

Set the repository secrets referenced by the workflow:

- **AWS:** `AWS_REGION`, `AWS_ACCOUNT_ID`, `AWS_ACCESS_KEY`, `AWS_SECRET_ACCESS_KEY`.
- **ECS:** `ECS_CLUSTER`, `GATEWAY_SERVICE`, `AUTH_SERVICE`, `CHAT_SERVICE`, `AGENT_SERVICE`, `BILLING_SERVICE`.
- **Frontend delivery:** `S3_BUCKET`, `CLOUDFRONT_DISTRIBUTION_ID`.
- **Client build:** `VITE_FIREBASE_API_KEY`, `VITE_RAZORPAY_KEY_ID`, `VITE_SERVER_URL`, `VITE_ADMIN_EMAIL`.

Backend runtime credentials are configured separately through ECS task definitions and Secrets Manager. `S3_BUCKET` is the frontend deployment bucket; the Agent's `AWS_BUCKET_NAME` identifies artifact storage.

</details>

## Credits and usage limits

The [billing configuration](backend/services/billing/config/Plans.js) defines these plans:

| Plan | Price | Credits |
|---|---|---|
| Free | ₹0 | 100 |
| Starter | ₹199 | 500 |
| Pro | ₹499 | 1,000 |

Plan configuration declares a 30-day validity. Credit deductions are implemented by Auth, while rate counters are maintained by the Agent service in Redis.

| Workflow | Credit deductions on successful path | Rate-limit bucket |
|---|---|---|
| Chat | 1 | `chat`: 20 requests / 60 seconds |
| Search → Chat | 5 for Search + 1 for Chat | Both `search` (5) and `chat` (20) |
| Coding | 10 | `coding`: 5 / 60 seconds |
| PDF generation / PDF RAG | 10 | Shared `pdf`: 5 / 60 seconds |
| PPT generation | 10 | `ppt`: 5 / 60 seconds |
| Image generation / image analysis | 10 | Shared `image`: 5 / 60 seconds |

The limits apply per user and bucket. See [agentLimit.js](backend/services/agent/config/agentLimit.js), the [specialist implementations](backend/services/agent/agents/) and [Auth credit handling](backend/services/auth/controllers/auth.controller.js) for the implementation.

<details>
<summary>Implementation details that affect usage</summary>

- PDF and generated-image download links currently request **1,440 seconds (24 minutes)**; PPTX links request **86,400 seconds (24 hours)**.
- Each PDF upload creates a new Qdrant collection. The current RAG flow does not delete that collection after answering.
- Chat memory is cached in Redis; message history is persisted through the Chat service. Memory writes do not preserve the initial cache expiry consistently.
- Downstream services trust the Gateway's user header and internal service calls; the deployment design keeps them private.

</details>

## Screenshots

Expand a gallery to view the application and deployment screenshots.

<details>
<summary>Login & Authentication</summary>

| Login Page | Google Authentication |
|---|---|
| ![Login Page](new-project-pic/NovaMind-Ai-MultiAgent-platform-loginpage-1.png) | ![Google Auth](new-project-pic/NovaMind-Ai-MultiAgent-platform-login-aunthentication-1.png) |

</details>

<details>
<summary>Dashboard & Chat Interface</summary>

| Dashboard Overview | Chat — General AI |
|---|---|
| ![Dashboard 1](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-1.png) | ![Dashboard 2](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-2.png) |

| Chat — Coding Agent | Chat — Search Agent |
|---|---|
| ![Dashboard 3](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-3.png) | ![Dashboard 4](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-4.png) |

| Chat — Image Generation | Chat — PDF/PPT Generation |
|---|---|
| ![Dashboard 5](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-5.png) | ![Dashboard 6](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-6.png) |

| Dashboard — Full View | Conversation History |
|---|---|
| ![Dashboard 6 New](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-6-new.png) | ![Dashboard 7](new-project-pic/NovaMind-Ai-MultiAgent-Platform-Dashboard-7.png) |

</details>

<details>
<summary>PDF RAG (Document Q&A)</summary>

| Upload PDF & Ask Questions | Follow-up Questions |
|---|---|
| ![RAG 1](new-project-pic/Novamind-ai-multiagent-platform-rag-capabiliti-1%20.png) | ![RAG 2](new-project-pic/Novamind-ai-multiagent-platform-rag-capabiliti-2.png) |

</details>

<details>
<summary>Admin Panel</summary>

| Admin Dashboard — Stats | Admin — Users Management |
|---|---|
| ![Admin 1](new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-1.png) | ![Admin 2](new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-2.png) |

| Admin — Payments | Admin — All Users |
|---|---|
| ![Admin 3](new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-3.png) | ![Admin 4](new-project-pic/NovaMind-Ai-MultiAgent-Platform-admin-panel-4-users.png) |

| Admin — Full Overview |
|---|
| ![Admin Full](new-project-pic/screencapture-d8au5xi32kvkz-cloudfront-net-admin-2026-09-19-06_49_34.png) |

</details>

<details>
<summary>CI/CD — GitHub Actions Pipeline</summary>

| Pipeline Triggered | Jobs Running | Deployment Complete |
|---|---|---|
| ![GitHub Actions 1](new-project-pic/Novamind-ai-multiagent-github-action-1.png) | ![GitHub Actions 2](new-project-pic/Novamind-ai-multiagent-github-action-2.png) | ![GitHub Actions 3](new-project-pic/Novamind-ai-multiagent-github-action-3.png) |

</details>

<details>
<summary>AWS Infrastructure</summary>

| ECR — Container Registry | ECS — Fargate Services |
|---|---|
| ![ECR](new-project-pic/aws-ecr.png) | ![ECS](new-project-pic/aws-ecs.png) |

| ElastiCache Redis | S3 Buckets |
|---|---|
| ![ElastiCache](new-project-pic/aws-elastic-cache.png) | ![S3](new-project-pic/aws-s3-bucket.png) |

| CloudFront CDN | IAM Roles |
|---|---|
| ![CloudFront](new-project-pic/aws-cloudfront.png) | ![IAM](new-project-pic/aws-iam-role.png) |

| CloudWatch Logs |
|---|
| ![CloudWatch](new-project-pic/aws-cloudwatch-logs.png) |

</details>

## Project structure

```text
1.cortexAI/
├── frontend/                    # React UI, Redux state and API calls
├── backend/
│   ├── gateway/                 # Session checks and reverse proxy
│   ├── shared/redis/            # Shared Redis client
│   ├── docker-compose.yml       # Local Redis container
│   └── services/
│       ├── auth/                # Identity, credits and admin APIs
│       ├── chat/                # Conversation and message storage
│       ├── agent/
│       │   ├── agents/          # Eight specialist implementations
│       │   ├── graph/           # State, router and graph definition
│       │   ├── config/          # Models, retrieval, memory and storage
│       │   └── utils/           # Document generation and service calls
│       └── billing/             # Razorpay and plan updates
├── task-defs/                   # Five ECS Fargate task definitions
├── .github/workflows/           # Deployment workflow
├── new-project-pic/             # Architecture artwork and screenshots
└── scripts/                    # Technical architecture renderer
```

## Documentation

- [Local deployment runbook](steps_to_do_deploy_localhost.md) — development setup notes.
- [AWS deployment guide](deploy-guide-aws-original.md) — infrastructure and deployment instructions.
- [Architecture details](Architecture.md) — deeper component and integration notes.
- [Interview guide](interview.md) — project walkthrough and discussion prompts.
- [Technical diagram assets](new-project-pic/aws-icons/README.md) — original AWS icons and renderer instructions.
- [Poster notes](new-project-pic/architecture-poster-notes.md) — poster design and generation details.

## Author

**Aamir Imran** · [GitHub](https://github.com/aamir490)

Built with LangGraph, React, Node.js and AWS.
