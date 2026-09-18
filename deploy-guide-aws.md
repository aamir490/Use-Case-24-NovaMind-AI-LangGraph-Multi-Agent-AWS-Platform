# NovaMind AI — Complete AWS Deployment Guide

> **AWS Account:** `637423369471` | **IAM User:** `mlops-user` | **Region:** `us-east-1`
>
> **Guide type:** Beginner-friendly, project-specific, mentor-style
>
> **Rule:** This guide is read-only documentation. Do not execute commands unless you have completed every prerequisite and verification step.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Final AWS Architecture](#2-final-aws-architecture)
3. [Prerequisites](#3-prerequisites)
4. [AWS Account Verification](#4-aws-account-verification)
5. [Pre-Deployment Project Checks](#5-pre-deployment-project-checks)
6. [Local Application Verification](#6-local-application-verification)
7. [Docker Verification](#7-docker-verification)
8. [ECR — Container Registry](#8-ecr--container-registry)
9. [VPC and Networking](#9-vpc-and-networking)
10. [ElastiCache Redis](#10-elasticache-redis)
11. [S3 Buckets](#11-s3-buckets)
12. [Secrets Manager](#12-secrets-manager)
13. [IAM Roles and Permissions](#13-iam-roles-and-permissions)
14. [ECS Fargate Cluster](#14-ecs-fargate-cluster)
15. [ECS Task Definitions — All 5 Services](#15-ecs-task-definitions--all-5-services)
16. [ECS Services and Service Discovery](#16-ecs-services-and-service-discovery)
17. [Application Load Balancer](#17-application-load-balancer)
18. [Frontend Deployment — S3 + CloudFront](#18-frontend-deployment--s3--cloudfront)
19. [External Services Configuration](#19-external-services-configuration)
20. [GitHub Actions CI/CD](#20-github-actions-cicd)
21. [Complete First-Time Deployment Order](#21-complete-first-time-deployment-order)
22. [Verification After Deployment](#22-verification-after-deployment)
23. [Troubleshooting](#23-troubleshooting)
24. [Security Checklist](#24-security-checklist)
25. [AWS Cleanup — Avoid Unnecessary Charges](#25-aws-cleanup--avoid-unnecessary-charges)
26. [Final Deployment Checklist](#26-final-deployment-checklist)
27. [Interview Explanation](#27-interview-explanation)

---

## 1. Project Overview

### What This Project Is

NovaMind AI is a full-stack multi-agent AI platform with:
- A **React frontend** (Vite, port 5173 locally)
- **5 Node.js/Express backend services** — all Dockerized
- **Redis** for session storage, conversation memory, and rate limiting
- **MongoDB Atlas** as the cloud database (already external, stays external)
- **AWS S3** already used by the agent service for file storage
- **Qdrant Cloud** for PDF RAG vector search (already external)
- **Firebase Auth** for Google sign-in (already external)
- **LangGraph** for AI agent orchestration

### Backend Services and Ports

| Service | Port | Responsibility |
|---------|------|---------------|
| API Gateway | 8000 | Single entry point, CORS, session auth, proxy |
| Auth Service | 8001 | Firebase verification, sessions, credits, admin |
| Chat Service | 8002 | Conversation and message persistence |
| Agent Service | 8003 | LangGraph AI agents (8 agents) |
| Billing Service | 8004 | Razorpay payment processing |

### Local vs AWS — What Changes

| Component | Local | AWS |
|-----------|-------|-----|
| Frontend | `localhost:5173` (Vite dev server) | S3 + CloudFront (static build) |
| Backend services | `nodemon` on local ports | ECS Fargate containers |
| Redis | Docker container (`docker compose up`) | ElastiCache managed Redis |
| Inter-service URLs | `http://localhost:8001` etc. | AWS Cloud Map DNS |
| Secrets / API keys | `.env` files on disk | AWS Secrets Manager |
| Docker images | Built locally | Stored in Amazon ECR |
| `serviceAccountKey.json` | File on disk | Secrets Manager → injected at startup |
| HTTPS | Not present locally | ALB + CloudFront + ACM certificate |
| CI/CD | Manual `npm run dev` | GitHub Actions (`deploy.yml`) |

MongoDB Atlas, Qdrant Cloud, Firebase Auth, Groq, Gemini, OpenRouter, Tavily, Razorpay — **all stay external**. They are cloud services already. No migration needed.

---

## 2. Final AWS Architecture

### Text Architecture Diagram

```
════════════════════════════════════════════════════════════════
                        INTERNET USERS
════════════════════════════════════════════════════════════════
         │                              │
         │ (frontend requests)          │ (API requests /api/*)
         ▼                              ▼
┌─────────────────────┐    ┌──────────────────────────────────┐
│   AWS CloudFront    │    │   Application Load Balancer (ALB) │
│   (HTTPS CDN)       │    │   (HTTPS termination, public)     │
└────────┬────────────┘    └───────────────┬──────────────────┘
         │                                 │
         ▼                                 ▼
┌─────────────────────┐    ┌──────────────────────────────────┐
│   S3 Frontend       │    │         AWS VPC                   │
│   Bucket            │    │   ┌──────────────────────────┐   │
│   (React build)     │    │   │  PUBLIC SUBNETS           │   │
└─────────────────────┘    │   │  (ALB lives here)         │   │
                           │   └──────────────────────────┘   │
                           │                                   │
                           │   ┌──────────────────────────┐   │
                           │   │  PRIVATE SUBNETS          │   │
                           │   │                           │   │
                           │   │  ┌────────────────────┐  │   │
                           │   │  │ ECS Fargate Tasks   │  │   │
                           │   │  │                     │  │   │
                           │   │  │ :8000 Gateway       │  │   │
                           │   │  │ :8001 Auth          │  │   │
                           │   │  │ :8002 Chat          │  │   │
                           │   │  │ :8003 Agent         │  │   │
                           │   │  │ :8004 Billing       │  │   │
                           │   │  └─────────┬───────────┘  │   │
                           │   │            │               │   │
                           │   │  ┌─────────▼───────────┐  │   │
                           │   │  │ ElastiCache Redis    │  │   │
                           │   │  │ (sessions + memory)  │  │   │
                           │   │  └─────────────────────┘  │   │
                           │   │                           │   │
                           │   │  NAT Gateway ──► Internet │   │
                           │   └──────────────────────────┘   │
                           └───────────────────────────────────┘

ECS Tasks also connect to:
  ├── AWS S3          (Agent: upload PDFs, PPTs, images)
  ├── MongoDB Atlas   (all services: cloud database)
  ├── Qdrant Cloud    (Agent: PDF RAG vector search)
  ├── Firebase Auth   (Auth: token verification)
  ├── Groq API        (Agent: LLM inference)
  ├── Google Gemini   (Agent: image analysis + embeddings)
  ├── OpenRouter      (Agent: DeepSeek coding LLM)
  ├── Tavily          (Agent: web search)
  └── Razorpay        (Billing: payment processing)

Supporting AWS Services:
  ├── Amazon ECR         (stores 5 Docker images)
  ├── AWS Secrets Manager (stores all API keys + Firebase JSON)
  ├── AWS CloudWatch     (container logs from all 5 services)
  ├── AWS Cloud Map      (internal DNS for service-to-service calls)
  └── AWS IAM            (roles for ECS tasks)
```

### Component Explanations (Simple English)

| Component | What it does | Why this project needs it |
|-----------|-------------|--------------------------|
| **CloudFront** | Global CDN, delivers React app over HTTPS | Frontend needs HTTPS; S3 alone is HTTP |
| **S3 (frontend)** | Stores the compiled React build files | React app is just HTML/JS/CSS files after `npm run build` |
| **ALB** | Receives API traffic, terminates HTTPS, routes to Gateway | Gateway is the only public backend entry point |
| **ECS Fargate** | Runs Docker containers without managing servers | All 5 services have Dockerfiles; no EC2 to manage |
| **ElastiCache Redis** | Managed Redis for sessions, memory, rate limits | Replaces local Docker Redis; all services share it |
| **ECR** | Private Docker image registry | Stores built images; ECS pulls from here |
| **Secrets Manager** | Secure storage for all API keys and Firebase JSON | `.env` files cannot go into production containers |
| **Cloud Map** | Internal DNS so services find each other | Replaces `localhost:8001` with `novamind-auth.local:8001` |
| **CloudWatch** | Collects logs from all ECS containers | See what's happening inside containers |
| **IAM** | Permissions management | ECS tasks need permission to read secrets, write to S3 |
| **NAT Gateway** | Lets private ECS tasks reach the internet | Agent service calls Groq, Atlas, Firebase from private subnet |

---

## 3. Prerequisites

Before you start, you need everything in this list. Verify each one.

### 3.1 Software on Your Windows Machine

| Tool | Required Version | How to Check |
|------|-----------------|--------------|
| AWS CLI | v2.x | `aws --version` |
| Docker Desktop | Any recent | `docker --version` |
| Node.js | 22+ | `node --version` |
| npm | 9+ | `npm --version` |
| Git | Any | `git --version` |

### 3.2 AWS Requirements

- AWS account `637423369471` with IAM user `mlops-user`
- `mlops-user` must have these IAM policies attached (check in AWS Console → IAM → Users → mlops-user → Permissions):

| Policy | Why needed |
|--------|-----------|
| `AmazonECS_FullAccess` | Create ECS clusters, services, tasks |
| `AmazonEC2ContainerRegistryFullAccess` | Push images to ECR |
| `AmazonElastiCacheFullAccess` | Create Redis cluster |
| `AmazonS3FullAccess` | Create and manage S3 buckets |
| `CloudFrontFullAccess` | Create CDN distribution |
| `SecretsManagerReadWrite` | Store and retrieve secrets |
| `CloudWatchFullAccess` | Create log groups, view logs |
| `AmazonVPCFullAccess` | Create VPC, subnets, security groups |
| `ElasticLoadBalancingFullAccess` | Create ALB, target groups |
| `IAMFullAccess` | Create ECS task roles |
| `AWSCloudMapFullAccess` | Create service discovery namespace |

### 3.3 External Services (already configured locally)

- **MongoDB Atlas** — cluster running, connection strings known
- **Qdrant Cloud** — cluster URL and API key available
- **Firebase project** — `cortexnovamind`, service account key JSON downloaded
- **Groq API key** — available
- **Google Gemini API key** — available
- **OpenRouter API key** — available
- **Tavily API key** — available
- **Razorpay Key ID and Secret** — available
- **GitHub repository** — code pushed, Actions enabled

### 3.4 Verify Prerequisites

**Run in PowerShell — any folder:**

```powershell
# Check AWS CLI
aws --version
# Expected: aws-cli/2.x.x Python/3.x.x Windows/10

# Check Docker
docker --version
# Expected: Docker version 24.x.x

# Check Node.js
node --version
# Expected: v22.x.x

# Check npm
npm --version
# Expected: 10.x.x

# Check Git
git --version
# Expected: git version 2.x.x
```

If any of these fail, install the missing tool before continuing.

---

## 4. AWS Account Verification

> ⚠️ **STOP AND READ THIS SECTION CAREFULLY.**
> Before creating ANY AWS resource, verify you are in the correct account.
> Creating resources in the wrong account wastes money and causes confusion.

### Step 1 — Configure AWS CLI

**Run in PowerShell — any folder:**

```powershell
aws configure
```

Enter these values when prompted:

```
AWS Access Key ID:     [your mlops-user access key ID]
AWS Secret Access Key: [your mlops-user secret access key]
Default region name:   us-east-1
Default output format: json
```

> **Where to get the access key:** AWS Console → IAM → Users → mlops-user → Security credentials → Create access key → CLI use case.

### Step 2 — Verify Your Identity

**Run in PowerShell — any folder:**

```powershell
aws sts get-caller-identity
```

**Expected output:**

```json
{
    "UserId": "AIDAXXXXXXXXXXXXXXXXX",
    "Account": "637423369471",
    "Arn": "arn:aws:iam::637423369471:user/mlops-user"
}
```

**Check these three values:**

| Field | Expected Value | What to do if wrong |
|-------|---------------|---------------------|
| `Account` | `637423369471` | **STOP.** Run `aws configure` again with correct keys |
| `Arn` | contains `mlops-user` | **STOP.** You are using the wrong IAM user |
| Region (from configure) | `us-east-1` | Re-run `aws configure` and set `us-east-1` |

### Step 3 — Verify Region

**Run in PowerShell — any folder:**

```powershell
aws configure get region
```

**Expected output:**

```
us-east-1
```

> ⚠️ **If your account or region does not match exactly, STOP here. Do not proceed until both are correct. Creating resources in the wrong account is expensive to clean up.**

### Step 4 — Verify IAM Permissions

**Run in PowerShell — any folder:**

```powershell
# Test ECS access
aws ecs list-clusters --region us-east-1

# Test ECR access
aws ecr describe-repositories --region us-east-1

# Test S3 access
aws s3 ls
```

If any of these return `AccessDenied`, ask the account administrator to attach the required policies from Section 3.2.

---

## 5. Pre-Deployment Project Checks

Before touching AWS, verify the project is in the correct state. Think of this as a preflight checklist.

### 5.1 Verify Project Structure

**Run in PowerShell — project root:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI"
Get-ChildItem -Name
```

**You must see:**

```
.github/
backend/
frontend/
.gitignore
Architecture.md
README.md
```

### 5.2 Verify All 5 Dockerfiles Exist

**Run in PowerShell — project root:**

```powershell
Test-Path "backend\gateway\Dockerfile"
Test-Path "backend\services\auth\Dockerfile"
Test-Path "backend\services\chat\Dockerfile"
Test-Path "backend\services\agent\Dockerfile"
Test-Path "backend\services\billing\Dockerfile"
```

All 5 must return `True`.

### 5.3 Verify the CI/CD Pipeline File Exists

**Run in PowerShell — project root:**

```powershell
Test-Path ".github\workflows\deploy.yml"
```

Must return `True`. This file already contains the complete deployment pipeline.

### 5.4 Verify .env.example Files

**Run in PowerShell — project root:**

```powershell
Test-Path "backend\gateway\.env.example"
Test-Path "backend\services\auth\.env.example"
Test-Path "backend\services\chat\.env.example"
Test-Path "backend\services\agent\.env.example"
Test-Path "backend\services\billing\.env.example"
Test-Path "frontend\.env.example"
```

All 6 must return `True`. These are your reference for every environment variable.

### 5.5 Verify Docker Build Context

**Understand this before building:**

All 5 Dockerfiles use `backend/` as the build context, NOT the individual service folder. This is because every service needs `backend/shared/redis/redis.js`. Look at the gateway Dockerfile:

```dockerfile
COPY gateway ./gateway        # copies gateway/ folder
COPY shared ./shared          # copies shared/ folder — needs backend/ as context
```

This is why the CI/CD pipeline runs:
```bash
docker build -f backend/gateway/Dockerfile -t gateway backend
#                                                           ↑ build context = backend/
```

If you try to build from inside the service folder, it will fail with a `COPY shared` error.

### 5.6 Verify S3 Configuration in Agent Service

**Read this file to confirm S3 config:**

The file `backend/services/agent/config/s3.js` currently uses static credentials:

```javascript
export const s3 = new S3Client({
    region: process.env.AWS_REGION,
    credentials: {
        accessKeyId: process.env.AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.AWS_SECRET_KEY
    }
})
```

> **Note:** On AWS ECS with an IAM Task Role, the `credentials` block should be removed so the SDK uses the role automatically. This is a code change needed before production deployment. The S3 bucket `cretexainovamind` is in `ap-south-1` — this is already configured and working.

### 5.7 Verify Session Cookie Security Setting

**Read `backend/services/auth/controllers/auth.controller.js`:**

The login function sets a cookie with `secure: false`. On AWS with HTTPS, this must be `secure: true`. Before deploying to production:

- Change `secure: false` → `secure: process.env.NODE_ENV === "production"`
- Change `sameSite: "strict"` → `sameSite: process.env.NODE_ENV === "production" ? "none" : "strict"`

> **Why sameSite "none":** If your frontend CloudFront URL and API ALB URL are on different domains, the browser blocks `sameSite: "strict"` cookies on cross-domain requests. Setting `"none"` with `secure: true` allows it.

### 5.8 Files Summary — What Needs Changing for AWS

| File | Change needed | Why |
|------|--------------|-----|
| `backend/services/auth/controllers/auth.controller.js` | `secure: false` → `secure: process.env.NODE_ENV === "production"` | HTTPS cookies |
| All 5 Dockerfiles | `FROM node` → `FROM node:22-alpine` | Reproducible, smaller builds |
| `backend/services/agent/config/s3.js` | Remove `credentials` block | Use IAM Task Role instead of static keys |
| `frontend/.env` | `VITE_SERVER_URL` → ALB DNS URL | Points frontend to production API |

**Files that do NOT need changes:**

- `backend/gateway/index.js` — reads `FRONTEND_URL` from env, no code change
- `backend/gateway/middleware/auth.middleware.js` — reads `REDIS_URL` from env
- `shared/redis/redis.js` — reads `REDIS_URL` from env
- All 8 AI agent files — pure business logic, no infrastructure coupling
- All frontend components — pure UI, reads `VITE_SERVER_URL` from env
- `.github/workflows/deploy.yml` — already complete, no changes needed

---

## 6. Local Application Verification

Before deploying to AWS, make sure the application works perfectly locally. Never deploy broken code.

### 6.1 Start Redis

**Why:** All services need Redis. Start it first.

**Run in PowerShell — `backend/` folder:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend"
docker compose up -d
```

**Expected output:**

```
[+] Running 2/2
 ✔ Container backend-redis-1  Started
 ✔ Network backend_default    Created
```

**Verify Redis is running:**

```powershell
docker ps
```

You should see a container with image `redis` on port `6379`.

### 6.2 Start All Backend Services

Open **5 separate PowerShell terminals**. In each one:

**Terminal 1 — Auth Service:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend\services\auth"
npm run dev
```

Expected: `auth started at 8001` + `db connected`

**Terminal 2 — Chat Service:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend\services\chat"
npm run dev
```

Expected: `chat started at 8002` + `db connected`

**Terminal 3 — Agent Service:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend\services\agent"
npm run dev
```

Expected: `agent started at 8003` + `db connected`

**Terminal 4 — Billing Service:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend\services\billing"
npm run dev
```

Expected: `billing started at 8004` + `db connected`

**Terminal 5 — Gateway:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend\gateway"
npm run dev
```

Expected: `gateway started at 8000`

### 6.3 Start Frontend

**Terminal 6:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\frontend"
npm run dev
```

Expected:

```
VITE v8.x  ready in ~3s
➜  Local:   http://localhost:5173/
```

### 6.4 Test the Application

Open `http://localhost:5173` in your browser.

**Test checklist:**
- [ ] Login page loads with NovaMind AI logo
- [ ] Google sign-in works
- [ ] Dashboard appears after login
- [ ] Send a test chat message — AI responds
- [ ] Admin panel accessible at `/admin` (for admin email)

**Only proceed to AWS deployment if everything works locally.**

---

## 7. Docker Verification

Before pushing to ECR, verify that Docker can build all 5 images correctly.

### 7.1 Understand the Build Context

**Why this matters:** All 5 Dockerfiles copy the `shared/` folder. The `shared/` folder only exists at `backend/shared/`. So you must run all Docker builds from the `backend/` directory.

```
backend/                    ← BUILD CONTEXT (run docker build from here)
├── shared/
│   └── redis/redis.js      ← copied into every container
├── gateway/
│   └── Dockerfile          ← specifies -f path
└── services/
    ├── auth/Dockerfile
    ├── chat/Dockerfile
    ├── agent/Dockerfile
    └── billing/Dockerfile
```

### 7.2 Build All 5 Images Locally

**Run in PowerShell — `backend/` folder:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend"

# Build Gateway
docker build -f gateway/Dockerfile -t gateway .

# Build Auth
docker build -f services/auth/Dockerfile -t auth-service .

# Build Chat
docker build -f services/chat/Dockerfile -t chat-service .

# Build Agent
docker build -f services/agent/Dockerfile -t agent-service .

# Build Billing
docker build -f services/billing/Dockerfile -t billing-service .
```

**Expected output for each build (last few lines):**

```
Successfully built xxxxxxxx
Successfully tagged gateway:latest
```

### 7.3 Verify Images Were Built

**Run in PowerShell — any folder:**

```powershell
docker images
```

**Expected output (should see all 5):**

```
REPOSITORY      TAG     IMAGE ID       CREATED         SIZE
billing-service latest  xxxxxxxxxxxx   1 minute ago    ~500MB
agent-service   latest  xxxxxxxxxxxx   2 minutes ago   ~800MB
chat-service    latest  xxxxxxxxxxxx   3 minutes ago   ~400MB
auth-service    latest  xxxxxxxxxxxx   4 minutes ago   ~500MB
gateway         latest  xxxxxxxxxxxx   5 minutes ago   ~350MB
```

### 7.4 Test One Container Locally (Optional)

**Run the gateway container to verify it starts:**

```powershell
docker run --rm -p 8000:8000 `
  -e PORT=8000 `
  -e NODE_ENV=production `
  -e FRONTEND_URL=http://localhost:5173 `
  -e REDIS_URL=redis://host.docker.internal:6379 `
  gateway
```

**Expected:**

```
gateway started at 8000
```

Test it: open `http://localhost:8000` in browser — should return `{"message":"hello from gateway v5"}`

**Stop the container:**

Press `Ctrl+C` in the terminal.

### 7.5 Clean Up Local Test Images (Optional)

After verification, you can remove local images to free disk space (they'll be re-built by CI/CD):

```powershell
docker rmi gateway auth-service chat-service agent-service billing-service
```


---

## 8. ECR — Container Registry

### What is ECR and Why Do We Need It?

ECR (Elastic Container Registry) is AWS's private Docker image registry — think of it as a private Docker Hub that only your AWS account can access. ECS Fargate cannot pull images from your local machine. It needs images stored somewhere accessible. ECR is the right place because:

- It lives inside your AWS account — secure and private
- ECS Fargate pulls images from ECR automatically during task startup
- The CI/CD pipeline in `deploy.yml` already pushes to ECR — you just need the repositories to exist first

### 8.1 Create 5 ECR Repositories

You need one repository per service. The names match exactly what `deploy.yml` expects.

**Run in PowerShell — any folder:**

```powershell
# Gateway
aws ecr create-repository `
  --repository-name gateway `
  --region us-east-1

# Auth Service
aws ecr create-repository `
  --repository-name auth-service `
  --region us-east-1

# Chat Service
aws ecr create-repository `
  --repository-name chat-service `
  --region us-east-1

# Agent Service
aws ecr create-repository `
  --repository-name agent-service `
  --region us-east-1

# Billing Service
aws ecr create-repository `
  --repository-name billing-service `
  --region us-east-1
```

**Expected output for each (example for gateway):**

```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-1:637423369471:repository/gateway",
        "registryId": "637423369471",
        "repositoryName": "gateway",
        "repositoryUri": "637423369471.dkr.ecr.us-east-1.amazonaws.com/gateway",
        "createdAt": "2026-09-19T..."
    }
}
```

**Note the `repositoryUri`** — you will use it when tagging images.

### 8.2 Verify Repositories Were Created

**Run in PowerShell — any folder:**

```powershell
aws ecr describe-repositories `
  --region us-east-1 `
  --query "repositories[*].repositoryName" `
  --output table
```

**Expected output:**

```
------------------
|DescribeRepositories|
+------------------+
|  agent-service   |
|  auth-service    |
|  billing-service |
|  chat-service    |
|  gateway         |
+------------------+
```

### 8.3 Authenticate Docker to ECR

Before pushing images, Docker must log in to ECR. This login is valid for 12 hours.

**Run in PowerShell — any folder:**

```powershell
aws ecr get-login-password --region us-east-1 | `
  docker login `
  --username AWS `
  --password-stdin `
  637423369471.dkr.ecr.us-east-1.amazonaws.com
```

**Expected output:**

```
Login Succeeded
```

### 8.4 Build, Tag, and Push All 5 Images

**Run in PowerShell — `backend/` folder:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\backend"

# ── GATEWAY ────────────────────────────────────────────────────
docker build -f gateway/Dockerfile -t gateway .
docker tag gateway:latest 637423369471.dkr.ecr.us-east-1.amazonaws.com/gateway:latest
docker push 637423369471.dkr.ecr.us-east-1.amazonaws.com/gateway:latest

# ── AUTH ───────────────────────────────────────────────────────
docker build -f services/auth/Dockerfile -t auth-service .
docker tag auth-service:latest 637423369471.dkr.ecr.us-east-1.amazonaws.com/auth-service:latest
docker push 637423369471.dkr.ecr.us-east-1.amazonaws.com/auth-service:latest

# ── CHAT ───────────────────────────────────────────────────────
docker build -f services/chat/Dockerfile -t chat-service .
docker tag chat-service:latest 637423369471.dkr.ecr.us-east-1.amazonaws.com/chat-service:latest
docker push 637423369471.dkr.ecr.us-east-1.amazonaws.com/chat-service:latest

# ── AGENT ──────────────────────────────────────────────────────
docker build -f services/agent/Dockerfile -t agent-service .
docker tag agent-service:latest 637423369471.dkr.ecr.us-east-1.amazonaws.com/agent-service:latest
docker push 637423369471.dkr.ecr.us-east-1.amazonaws.com/agent-service:latest

# ── BILLING ────────────────────────────────────────────────────
docker build -f services/billing/Dockerfile -t billing-service .
docker tag billing-service:latest 637423369471.dkr.ecr.us-east-1.amazonaws.com/billing-service:latest
docker push 637423369471.dkr.ecr.us-east-1.amazonaws.com/billing-service:latest
```

**Expected output for each push:**

```
latest: digest: sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx size: xxxx
```

### 8.5 Verify Images in ECR

**Run in PowerShell — any folder:**

```powershell
aws ecr list-images `
  --repository-name gateway `
  --region us-east-1
```

**Expected:**

```json
{
    "imageIds": [
        {
            "imageDigest": "sha256:xxxxx",
            "imageTag": "latest"
        }
    ]
}
```

Repeat for each repository to confirm all 5 have a `latest` tag.

---

## 9. VPC and Networking

### What is a VPC and Why Does This Project Need One?

A VPC (Virtual Private Cloud) is your own private network inside AWS. Think of it as a walled-off section of the internet that only you control. This project needs a VPC because:

- ECS tasks should **not** be directly accessible from the internet (only the ALB should be)
- ElastiCache Redis must **only** be accessible from ECS tasks, not from the internet
- ECS tasks need to call **external services** (Groq, MongoDB Atlas, Firebase) — they need a path out via NAT Gateway

### Network Design for This Project

```
VPC: 10.0.0.0/16
│
├── PUBLIC SUBNETS (internet-accessible)
│   ├── 10.0.1.0/24  (us-east-1a) — ALB lives here
│   └── 10.0.2.0/24  (us-east-1b) — ALB lives here (multi-AZ)
│
└── PRIVATE SUBNETS (no direct internet access)
    ├── 10.0.3.0/24  (us-east-1a) — ECS tasks + ElastiCache
    └── 10.0.4.0/24  (us-east-1b) — ECS tasks + ElastiCache
```

**Why private subnets for ECS?** If someone found your task's IP address, they could try to call your services directly without going through the Gateway's auth. Private subnets prevent this.

**Why NAT Gateway?** Your ECS tasks are in private subnets with no internet access. But they need to call external APIs (Groq, Firebase, MongoDB Atlas, Tavily). The NAT Gateway sits in a public subnet and forwards their outbound traffic to the internet — while keeping them unreachable from outside.

### 9.1 Create the VPC

**AWS Console — recommended for beginners:**

1. Go to `https://console.aws.amazon.com/vpc/`
2. Click **Create VPC**
3. Select **VPC and more** (this creates everything automatically)
4. Configure:
   - Name: `novamind-vpc`
   - IPv4 CIDR: `10.0.0.0/16`
   - Number of Availability Zones: `2`
   - Number of public subnets: `2`
   - Number of private subnets: `2`
   - NAT gateways: `1 per AZ` → change to **In 1 AZ** (saves ~$32/month)
   - VPC endpoints: None
5. Click **Create VPC**

Wait 2–3 minutes. AWS creates: VPC, 4 subnets, Internet Gateway, NAT Gateway, and route tables automatically.

**Note the following IDs after creation (you'll need them later):**
- VPC ID (starts with `vpc-`)
- Public subnet IDs (2 of them, starts with `subnet-`)
- Private subnet IDs (2 of them, starts with `subnet-`)

**Verify via CLI:**

```powershell
aws ec2 describe-vpcs `
  --filters "Name=tag:Name,Values=novamind-vpc" `
  --region us-east-1 `
  --query "Vpcs[*].{ID:VpcId,CIDR:CidrBlock}" `
  --output table
```

### 9.2 Create Security Groups

Security groups are like firewall rules. You create 3 for this project.

#### Security Group 1: ALB Security Group (`novamind-alb-sg`)

This controls what traffic the ALB accepts from the internet.

**AWS Console:**
1. VPC → Security Groups → Create security group
2. Name: `novamind-alb-sg`
3. VPC: select `novamind-vpc`
4. Inbound rules:
   - HTTP (port 80) from `0.0.0.0/0` — so browsers can connect
   - HTTPS (port 443) from `0.0.0.0/0` — secure traffic
5. Outbound: leave default (allow all)
6. Click Create

#### Security Group 2: ECS Security Group (`novamind-ecs-sg`)

This controls what traffic ECS tasks accept. **Only the ALB should be allowed in.**

**AWS Console:**
1. Name: `novamind-ecs-sg`
2. VPC: `novamind-vpc`
3. Inbound rules:
   - Custom TCP, port range `8000-8004`, source: **select `novamind-alb-sg`**
   - (This means only the ALB can send requests to ECS tasks)
4. Outbound: leave default (allow all — tasks need to call external APIs)
5. Click Create

#### Security Group 3: Redis Security Group (`novamind-redis-sg`)

ElastiCache Redis should only accept connections from ECS tasks.

**AWS Console:**
1. Name: `novamind-redis-sg`
2. VPC: `novamind-vpc`
3. Inbound rules:
   - Custom TCP, port `6379`, source: **select `novamind-ecs-sg`**
4. Outbound: leave default
5. Click Create

### 9.3 Verify Security Groups

**Run in PowerShell — any folder:**

```powershell
aws ec2 describe-security-groups `
  --filters "Name=vpc-id,Values=YOUR_VPC_ID" `
  --region us-east-1 `
  --query "SecurityGroups[*].{Name:GroupName,ID:GroupId}" `
  --output table
```

Replace `YOUR_VPC_ID` with the actual VPC ID from Step 9.1. You should see `novamind-alb-sg`, `novamind-ecs-sg`, and `novamind-redis-sg`.

---

## 10. ElastiCache Redis

### What is ElastiCache and Why Does This Project Need It?

Locally, Redis runs as a Docker container via `docker compose up`. In AWS, you cannot use Docker Compose. ElastiCache is AWS's managed Redis service. You create it once and AWS handles:
- Redis process management
- Automatic restarts if Redis crashes
- Backups
- A stable DNS endpoint

**Why Redis is critical for this project:**

Reading `backend/gateway/middleware/auth.middleware.js`:
```javascript
const session = await redis.get(`session-${sessionId}`)
if (!session) return res.status(400).json({ message: "session expired" })
```

If Redis is down, every authenticated request returns 400. The entire application stops working. This is why managed ElastiCache is important in production.

The shared Redis client at `backend/shared/redis/redis.js` reads:
```javascript
const redis = new Redis(process.env.REDIS_URL)
```

All 5 services use this. On AWS, `REDIS_URL` becomes the ElastiCache endpoint.

### 10.1 Create ElastiCache Redis Cluster

**AWS Console:**

1. Go to `https://console.aws.amazon.com/elasticache/`
2. Click **Create cluster** → **Redis OSS**
3. Configure:
   - Cluster name: `novamind-redis`
   - Location: **AWS Cloud**
   - Cluster mode: **Disabled** (simpler, sufficient for this project)
   - Node type: `cache.t3.micro` (cheapest — ~$12/month)
   - Number of replicas: `0` (for development; use `1` for production reliability)
4. Subnet group:
   - Create new: name `novamind-redis-subnet-group`
   - Select your VPC: `novamind-vpc`
   - Select your **private subnets** (both of them)
5. Security group: select `novamind-redis-sg`
6. Leave all other settings as default
7. Click **Create**

**Wait 5–10 minutes** for status to change from `creating` to `available`.

### 10.2 Get the Redis Endpoint

**AWS Console:**
1. ElastiCache → Clusters → `novamind-redis`
2. Find **Primary endpoint** — it looks like:
   ```
   novamind-redis.xxxxxx.0001.use1.cache.amazonaws.com:6379
   ```

**Save this endpoint.** Your `REDIS_URL` environment variable for all ECS tasks will be:
```
redis://novamind-redis.xxxxxx.0001.use1.cache.amazonaws.com:6379
```

### 10.3 Verify Redis Creation

**Run in PowerShell — any folder:**

```powershell
aws elasticache describe-cache-clusters `
  --cache-cluster-id novamind-redis `
  --region us-east-1 `
  --query "CacheClusters[*].{ID:CacheClusterId,Status:CacheClusterStatus,Engine:Engine}" `
  --output table
```

**Expected:**

```
------------------------------------------
|       DescribeCacheClusters            |
+------------------+--------+-----------+
| ID               |Engine  | Status    |
+------------------+--------+-----------+
| novamind-redis   | redis  | available |
+------------------+--------+-----------+
```

---

## 11. S3 Buckets

### Two Different S3 Buckets for Two Different Purposes

This project uses S3 in **two completely different ways**. Do not confuse them.

| Bucket | Purpose | Who uses it | Region |
|--------|---------|-------------|--------|
| `novamind-frontend-prod` | Hosts the compiled React build | CloudFront serves it to users | `us-east-1` |
| `cretexainovamind` | Stores generated PDFs, PPTs, AI images | Agent service uploads files here | `ap-south-1` |

**The second bucket (`cretexainovamind`) already exists** — the agent service is already using it locally via `backend/services/agent/config/s3.js`. You only need to create the frontend bucket.

### 11.1 Create the Frontend S3 Bucket

**Run in PowerShell — any folder:**

```powershell
# Create the bucket
aws s3 mb s3://novamind-frontend-prod --region us-east-1

# Disable the "Block Public Access" setting (required for static hosting)
aws s3api put-public-access-block `
  --bucket novamind-frontend-prod `
  --public-access-block-configuration `
  "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false"

# Enable static website hosting
aws s3 website s3://novamind-frontend-prod `
  --index-document index.html `
  --error-document index.html
```

> **Why `--error-document index.html`?** React Router handles page routing in the browser. If a user refreshes the page at `/admin`, S3 would return a 404 because there's no actual `admin.html` file. Setting the error document to `index.html` returns the React app which then handles the route correctly. CloudFront also has custom error pages configured for this.

### 11.2 Apply a Bucket Policy for Public Read

The frontend files must be publicly readable (everyone's browser needs to download the CSS/JS).

**Run in PowerShell — any folder:**

```powershell
$policy = '{"Version":"2012-10-17","Statement":[{"Sid":"PublicReadGetObject","Effect":"Allow","Principal":"*","Action":"s3:GetObject","Resource":"arn:aws:s3:::novamind-frontend-prod/*"}]}'

aws s3api put-bucket-policy `
  --bucket novamind-frontend-prod `
  --policy $policy
```

### 11.3 Verify the App File Bucket Exists

**Run in PowerShell — any folder:**

```powershell
aws s3 ls s3://cretexainovamind --region ap-south-1
```

If this returns content or an empty result (not an error), the bucket exists and is accessible.

> **Important:** The `cretexainovamind` bucket is in `ap-south-1`, not `us-east-1`. This is fine — S3 is a global service and ECS can write to it from any region. The agent service uses `AWS_REGION=ap-south-1` in its config specifically for this.

### 11.4 Verify Frontend Bucket

**Run in PowerShell — any folder:**

```powershell
aws s3api get-bucket-website --bucket novamind-frontend-prod
```

**Expected:**

```json
{
    "IndexDocument": { "Suffix": "index.html" },
    "ErrorDocument": { "Key": "index.html" }
}
```

---

## 12. Secrets Manager

### Why Secrets Manager Instead of Environment Variables?

You might wonder — why not just put API keys directly as ECS environment variables? Three reasons:

1. **The `serviceAccountKey.json` problem:** Firebase Admin SDK needs a full JSON file on disk. You cannot put a multi-line JSON file in a plain environment variable cleanly. Secrets Manager stores it as a JSON value and you inject it at container startup.
2. **Security auditing:** Secrets Manager logs every access. You know exactly when and which task read which secret.
3. **Rotation:** Secrets Manager can auto-rotate database passwords. Plain env vars cannot.

### 12.1 Complete Secrets Checklist

Create all these secrets. Use the exact names — they are referenced in ECS task definitions.

**Run in PowerShell — any folder:**

> Replace every `YOUR_VALUE_HERE` with your actual value.

```powershell
# ── AUTH SERVICE SECRETS ───────────────────────────────────────

# MongoDB URI for Auth database
aws secretsmanager create-secret `
  --name "novamind/auth/mongodb-uri" `
  --secret-string "YOUR_MONGODB_AUTH_URI" `
  --region us-east-1

# ── CHAT SERVICE SECRETS ───────────────────────────────────────

aws secretsmanager create-secret `
  --name "novamind/chat/mongodb-uri" `
  --secret-string "YOUR_MONGODB_CHAT_URI" `
  --region us-east-1

# ── AGENT SERVICE SECRETS ──────────────────────────────────────

aws secretsmanager create-secret `
  --name "novamind/agent/mongodb-uri" `
  --secret-string "YOUR_MONGODB_AGENT_URI" `
  --region us-east-1

aws secretsmanager create-secret `
  --name "novamind/agent/groq-api-key" `
  --secret-string "YOUR_GROQ_API_KEY" `
  --region us-east-1

aws secretsmanager create-secret `
  --name "novamind/agent/google-api-key" `
  --secret-string "YOUR_GOOGLE_API_KEY" `
  --region us-east-1

aws secretsmanager create-secret `
  --name "novamind/agent/openrouter-api-key" `
  --secret-string "YOUR_OPENROUTER_KEY" `
  --region us-east-1

aws secretsmanager create-secret `
  --name "novamind/agent/tavily-api-key" `
  --secret-string "YOUR_TAVILY_KEY" `
  --region us-east-1

aws secretsmanager create-secret `
  --name "novamind/agent/qdrant-api-key" `
  --secret-string "YOUR_QDRANT_API_KEY" `
  --region us-east-1

# ── BILLING SERVICE SECRETS ────────────────────────────────────

aws secretsmanager create-secret `
  --name "novamind/billing/mongodb-uri" `
  --secret-string "YOUR_MONGODB_BILLING_URI" `
  --region us-east-1

aws secretsmanager create-secret `
  --name "novamind/billing/razorpay-secret" `
  --secret-string "YOUR_RAZORPAY_KEY_SECRET" `
  --region us-east-1
```

### 12.2 The Firebase serviceAccountKey.json — Special Handling

This is the most important secret. The auth service requires this file at:
`/app/services/auth/serviceAccountKey.json`

**Store the entire JSON file as one secret:**

```powershell
# Read the file content
$content = Get-Content `
  "E:\GenAi-Project-Cloudage\1.cortexAI\backend\services\auth\serviceAccountKey.json" `
  -Raw

# Store in Secrets Manager
aws secretsmanager create-secret `
  --name "novamind/auth/firebase-service-account" `
  --secret-string $content `
  --region us-east-1
```

**How it gets injected into the container:**

In the auth ECS task definition, the container `command` is overridden to:
1. Fetch the secret from Secrets Manager
2. Write it to the expected file path
3. Then run `npm start`

The command looks like this (set in task definition):
```json
["sh", "-c", "aws secretsmanager get-secret-value --secret-id novamind/auth/firebase-service-account --region us-east-1 --query SecretString --output text > /app/services/auth/serviceAccountKey.json && npm start"]
```

This runs every time the container starts. The file is never baked into the Docker image.

### 12.3 Verify All Secrets Were Created

**Run in PowerShell — any folder:**

```powershell
aws secretsmanager list-secrets `
  --region us-east-1 `
  --query "SecretList[*].Name" `
  --output table
```

**Expected output:**

```
---------------------------------------------
|             ListSecrets                   |
+-------------------------------------------+
|  novamind/agent/google-api-key            |
|  novamind/agent/groq-api-key              |
|  novamind/agent/mongodb-uri               |
|  novamind/agent/openrouter-api-key        |
|  novamind/agent/qdrant-api-key            |
|  novamind/agent/tavily-api-key            |
|  novamind/auth/firebase-service-account   |
|  novamind/auth/mongodb-uri                |
|  novamind/billing/mongodb-uri             |
|  novamind/billing/razorpay-secret         |
|  novamind/chat/mongodb-uri                |
+-------------------------------------------+
```

### 12.4 Secrets Reference Table

| Secret Name | Used By | What it contains | How ECS uses it |
|-------------|---------|-----------------|----------------|
| `novamind/auth/mongodb-uri` | Auth Service | MongoDB connection string | ECS secret → `MONGODB_URI` env var |
| `novamind/auth/firebase-service-account` | Auth Service | Full Firebase Admin JSON | Written to disk at startup via shell command |
| `novamind/chat/mongodb-uri` | Chat Service | MongoDB connection string | ECS secret → `MONGODB_URI` env var |
| `novamind/agent/mongodb-uri` | Agent Service | MongoDB connection string | ECS secret → `MONGODB_URI` env var |
| `novamind/agent/groq-api-key` | Agent Service | Groq API key | ECS secret → `GROQ_API_KEY` env var |
| `novamind/agent/google-api-key` | Agent Service | Google Gemini API key | ECS secret → `GOOGLE_API_KEY` env var |
| `novamind/agent/openrouter-api-key` | Agent Service | OpenRouter key | ECS secret → `OPENROUTER_API_KEY` env var |
| `novamind/agent/tavily-api-key` | Agent Service | Tavily search key | ECS secret → `TAVILY_API_KEY` env var |
| `novamind/agent/qdrant-api-key` | Agent Service | Qdrant Cloud key | ECS secret → `QDRANT_API_KEY` env var |
| `novamind/billing/mongodb-uri` | Billing Service | MongoDB connection string | ECS secret → `MONGODB_URI` env var |
| `novamind/billing/razorpay-secret` | Billing Service | Razorpay key secret | ECS secret → `RAZORPAY_KEY_SECRET` env var |

---

## 13. IAM Roles and Permissions

### Understanding the 3 Types of IAM Identities

Before creating roles, understand the difference:

| Identity | Who uses it | Example |
|----------|------------|---------|
| **IAM User** (`mlops-user`) | You (the developer) running CLI commands | `aws ecr create-repository` |
| **ECS Task Execution Role** | AWS infrastructure to START the task | Pulling Docker image from ECR, reading secrets from Secrets Manager |
| **ECS Task Role** | Your application CODE at runtime | Agent service writing a file to S3 |

Think of it this way:
- The **execution role** is like the crane that lifts the container onto the ship
- The **task role** is what the container can DO once it's running

### 13.1 Create the ECS Task Execution Role

This role is used by ECS itself to pull your image and inject secrets. It is shared by all 5 services.

**AWS Console:**
1. Go to `https://console.aws.amazon.com/iam/`
2. Roles → Create role
3. Trusted entity: **AWS service** → Use case: **Elastic Container Service Task**
4. Attach policies:
   - `AmazonECSTaskExecutionRolePolicy` (allows image pull from ECR + CloudWatch logs)
   - Create a custom inline policy for Secrets Manager (see below)
5. Role name: `novamindECSTaskExecutionRole`

**Custom inline policy for Secrets Manager (add to execution role):**

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": [
        "arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/*"
      ]
    }
  ]
}
```

This follows **least privilege** — only allows reading secrets that start with `novamind/`. Not all secrets in your account.

### 13.2 Create the Agent Task Role

The agent service writes files to S3 (`config/s3.js`). On ECS, instead of using static `AWS_ACCESS_KEY_ID` and `AWS_SECRET_KEY` in environment variables, the container should use an IAM Role. This is more secure because:
- No credentials stored anywhere
- The role is automatically rotated by AWS
- If the container is compromised, the keys cannot be extracted

**AWS Console:**
1. IAM → Roles → Create role
2. Trusted entity: **AWS service** → **Elastic Container Service Task**
3. Attach policy: create custom inline policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject"
      ],
      "Resource": "arn:aws:s3:::cretexainovamind/*"
    }
  ]
}
```

4. Role name: `novamindAgentTaskRole`

> **Why only `cretexainovamind/*`?** Least privilege. The agent only needs access to this one bucket. Not all S3 buckets in the account.

### 13.3 Create the Auth Task Role

The auth service runs a shell command to fetch the Firebase JSON from Secrets Manager at startup. The task role needs permission to call `secretsmanager:GetSecretValue`.

**AWS Console:**
1. IAM → Roles → Create role
2. Trusted entity: **AWS service** → **Elastic Container Service Task**
3. Custom inline policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/auth/firebase-service-account*"
    }
  ]
}
```

4. Role name: `novamindAuthTaskRole`

### 13.4 Verify Roles Were Created

**Run in PowerShell — any folder:**

```powershell
aws iam list-roles `
  --query "Roles[?contains(RoleName,'novamind')].RoleName" `
  --output table
```

**Expected:**

```
----------------------------------------
|             ListRoles                |
+--------------------------------------+
| novamindAgentTaskRole                |
| novamindAuthTaskRole                 |
| novamindECSTaskExecutionRole         |
+--------------------------------------+
```


---

## 14. ECS Fargate Cluster

### What is ECS Fargate?

ECS (Elastic Container Service) is AWS's container management service. **Fargate** is the launch type that means AWS manages the underlying servers — you never touch an EC2 instance. You just say "run this Docker image with 0.5 CPU and 1GB RAM" and AWS handles everything else.

A **cluster** is just a logical grouping of tasks and services. Think of it as the folder that holds all your running containers.

### 14.1 Create the ECS Cluster

**Run in PowerShell — any folder:**

```powershell
aws ecs create-cluster `
  --cluster-name novamind-cluster `
  --region us-east-1
```

**Expected output:**

```json
{
    "cluster": {
        "clusterArn": "arn:aws:ecs:us-east-1:637423369471:cluster/novamind-cluster",
        "clusterName": "novamind-cluster",
        "status": "ACTIVE"
    }
}
```

### 14.2 Create CloudWatch Log Groups

ECS writes container logs to CloudWatch. The log groups must exist before tasks start, otherwise logs are lost.

**Run in PowerShell — any folder:**

```powershell
aws logs create-log-group --log-group-name /ecs/novamind-gateway  --region us-east-1
aws logs create-log-group --log-group-name /ecs/novamind-auth     --region us-east-1
aws logs create-log-group --log-group-name /ecs/novamind-chat     --region us-east-1
aws logs create-log-group --log-group-name /ecs/novamind-agent    --region us-east-1
aws logs create-log-group --log-group-name /ecs/novamind-billing  --region us-east-1
```

**Verify:**

```powershell
aws logs describe-log-groups `
  --log-group-name-prefix /ecs/novamind `
  --region us-east-1 `
  --query "logGroups[*].logGroupName" `
  --output table
```

### 14.3 Create AWS Cloud Map Namespace (Service Discovery)

**Why service discovery?** Locally, the gateway connects to auth via `http://localhost:8001`. On AWS, each service runs as an independent container with its own IP address that changes every deployment. Cloud Map gives each service a stable DNS name inside the VPC.

After setup, service URLs become:
```
AUTH_SERVICE    = http://novamind-auth.novamind.local:8001
CHAT_SERVICE    = http://novamind-chat.novamind.local:8002
AGENT_SERVICE   = http://novamind-agent.novamind.local:8003
BILLING_SERVICE = http://novamind-billing.novamind.local:8004
```

**Create the private DNS namespace:**

**Run in PowerShell — any folder:**

```powershell
aws servicediscovery create-private-dns-namespace `
  --name novamind.local `
  --vpc YOUR_VPC_ID `
  --region us-east-1
```

Replace `YOUR_VPC_ID` with your actual VPC ID (e.g., `vpc-0abc123def456`).

**Expected output:**

```json
{
    "OperationId": "gv4g5meo6kjz-5zvgnng..."
}
```

Wait 1 minute then check the operation succeeded:

```powershell
aws servicediscovery list-namespaces `
  --region us-east-1 `
  --query "Namespaces[*].{Name:Name,ID:Id}" `
  --output table
```

Expected: `novamind.local` appears in the list. Note its **ID** (starts with `ns-`).

**Create a service discovery service for each backend service:**

```powershell
# Auth
aws servicediscovery create-service `
  --name novamind-auth `
  --dns-config "NamespaceId=YOUR_NAMESPACE_ID,DnsRecords=[{Type=A,TTL=10}]" `
  --region us-east-1

# Chat
aws servicediscovery create-service `
  --name novamind-chat `
  --dns-config "NamespaceId=YOUR_NAMESPACE_ID,DnsRecords=[{Type=A,TTL=10}]" `
  --region us-east-1

# Agent
aws servicediscovery create-service `
  --name novamind-agent `
  --dns-config "NamespaceId=YOUR_NAMESPACE_ID,DnsRecords=[{Type=A,TTL=10}]" `
  --region us-east-1

# Billing
aws servicediscovery create-service `
  --name novamind-billing `
  --dns-config "NamespaceId=YOUR_NAMESPACE_ID,DnsRecords=[{Type=A,TTL=10}]" `
  --region us-east-1
```

Replace `YOUR_NAMESPACE_ID` with the `ns-xxxxx` ID from the step above. Note each service's **ARN** — you need them when creating ECS services in Section 16.

### 14.4 Verify Cluster

**Run in PowerShell — any folder:**

```powershell
aws ecs describe-clusters `
  --clusters novamind-cluster `
  --region us-east-1 `
  --query "clusters[*].{Name:clusterName,Status:status}" `
  --output table
```

**Expected:**

```
------------------------------------------
|          DescribeClusters              |
+-----------------------+----------------+
|  Name                 |  Status        |
+-----------------------+----------------+
|  novamind-cluster     |  ACTIVE        |
+-----------------------+----------------+
```

---

## 15. ECS Task Definitions — All 5 Services

### What is a Task Definition?

A task definition is a blueprint that tells ECS how to run a container. It specifies:
- Which Docker image to use (from ECR)
- How much CPU and memory to give it
- Which environment variables to set
- Which secrets to inject from Secrets Manager
- Which IAM roles to use
- Where to send logs

You create one task definition per service. Think of it as the recipe; the ECS service is the chef who follows the recipe repeatedly.

### How Environment Variables Work in ECS

There are two types in a task definition:

```json
"environment": [
    {"name": "PORT", "value": "8001"}
]
```
These are plain text — fine for non-sensitive values like port numbers and service URLs.

```json
"secrets": [
    {
        "name": "MONGODB_URI",
        "valueFrom": "arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/auth/mongodb-uri"
    }
]
```
These are pulled from Secrets Manager at task startup — for sensitive values like API keys.

---

### 15.1 Task Definition: Gateway Service

**AWS Console — ECS → Task Definitions → Create new task definition**

| Setting | Value |
|---------|-------|
| Family name | `novamind-gateway` |
| Launch type | AWS Fargate |
| CPU | 0.5 vCPU |
| Memory | 1 GB |
| Task execution role | `novamindECSTaskExecutionRole` |
| Task role | (none needed) |

**Container definition:**

| Setting | Value |
|---------|-------|
| Container name | `gateway` |
| Image URI | `637423369471.dkr.ecr.us-east-1.amazonaws.com/gateway:latest` |
| Port | `8000` (TCP) |

**Environment variables (plain):**

| Name | Value |
|------|-------|
| `PORT` | `8000` |
| `NODE_ENV` | `production` |
| `FRONTEND_URL` | `https://YOUR_CLOUDFRONT_DOMAIN` ← update after CloudFront is created |
| `AUTH_SERVICE` | `http://novamind-auth.novamind.local:8001` |
| `CHAT_SERVICE` | `http://novamind-chat.novamind.local:8002` |
| `AGENT_SERVICE` | `http://novamind-agent.novamind.local:8003` |
| `BILLING_SERVICE` | `http://novamind-billing.novamind.local:8004` |
| `REDIS_URL` | `redis://YOUR_ELASTICACHE_ENDPOINT:6379` |

**Log configuration:**

| Setting | Value |
|---------|-------|
| Log driver | `awslogs` |
| Log group | `/ecs/novamind-gateway` |
| Region | `us-east-1` |
| Stream prefix | `gateway` |

---

### 15.2 Task Definition: Auth Service

| Setting | Value |
|---------|-------|
| Family name | `novamind-auth` |
| CPU | 0.5 vCPU |
| Memory | 1 GB |
| Task execution role | `novamindECSTaskExecutionRole` |
| Task role | `novamindAuthTaskRole` |

**Container definition:**

| Setting | Value |
|---------|-------|
| Container name | `auth` |
| Image URI | `637423369471.dkr.ecr.us-east-1.amazonaws.com/auth-service:latest` |
| Port | `8001` |

**Container command (override — critical for Firebase JSON):**

```json
["sh", "-c", "aws secretsmanager get-secret-value --secret-id novamind/auth/firebase-service-account --region us-east-1 --query SecretString --output text > /app/services/auth/serviceAccountKey.json && npm start"]
```

This command runs on every container start. It fetches the Firebase service account JSON from Secrets Manager and writes it to disk before `npm start` runs.

> **Why is this needed?** The auth service reads `serviceAccountKey.json` at startup via `config/firebase.js`. The file is gitignored and never in the Docker image. This startup command injects it fresh from Secrets Manager every time.

**Environment variables (plain):**

| Name | Value |
|------|-------|
| `PORT` | `8001` |
| `NODE_ENV` | `production` |
| `REDIS_URL` | `redis://YOUR_ELASTICACHE_ENDPOINT:6379` |
| `ADMIN_EMAIL` | `aamirimran49000@gmail.com` |
| `BILLING_MONGODB_URI` | (set as secret — see below) |
| `CHAT_MONGODB_URI` | (set as secret — see below) |

**Secrets (from Secrets Manager):**

| Env var name | Secret ARN |
|-------------|-----------|
| `MONGODB_URI` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/auth/mongodb-uri` |
| `BILLING_MONGODB_URI` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/billing/mongodb-uri` |
| `CHAT_MONGODB_URI` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/chat/mongodb-uri` |

**Log configuration:**

| Setting | Value |
|---------|-------|
| Log group | `/ecs/novamind-auth` |
| Stream prefix | `auth` |

---

### 15.3 Task Definition: Chat Service

| Setting | Value |
|---------|-------|
| Family name | `novamind-chat` |
| CPU | 0.5 vCPU |
| Memory | 1 GB |
| Task execution role | `novamindECSTaskExecutionRole` |
| Task role | (none needed) |

**Container definition:**

| Setting | Value |
|---------|-------|
| Container name | `chat` |
| Image URI | `637423369471.dkr.ecr.us-east-1.amazonaws.com/chat-service:latest` |
| Port | `8002` |

**Environment variables (plain):**

| Name | Value |
|------|-------|
| `PORT` | `8002` |
| `NODE_ENV` | `production` |

**Secrets:**

| Env var name | Secret ARN |
|-------------|-----------|
| `MONGODB_URI` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/chat/mongodb-uri` |

**Log configuration:**

| Setting | Value |
|---------|-------|
| Log group | `/ecs/novamind-chat` |
| Stream prefix | `chat` |

---

### 15.4 Task Definition: Agent Service

The agent service is the most resource-intensive — it handles LLM calls, PDF processing, PPT generation, and S3 uploads. Give it more CPU and memory.

| Setting | Value |
|---------|-------|
| Family name | `novamind-agent` |
| CPU | **1 vCPU** |
| Memory | **2 GB** |
| Task execution role | `novamindECSTaskExecutionRole` |
| Task role | `novamindAgentTaskRole` ← S3 access |

**Container definition:**

| Setting | Value |
|---------|-------|
| Container name | `agent` |
| Image URI | `637423369471.dkr.ecr.us-east-1.amazonaws.com/agent-service:latest` |
| Port | `8003` |

**Environment variables (plain):**

| Name | Value |
|------|-------|
| `PORT` | `8003` |
| `NODE_ENV` | `production` |
| `REDIS_URL` | `redis://YOUR_ELASTICACHE_ENDPOINT:6379` |
| `CHAT_SERVICE` | `http://novamind-chat.novamind.local:8002` |
| `AUTH_SERVICE` | `http://novamind-auth.novamind.local:8001` |
| `AWS_REGION` | `ap-south-1` |
| `AWS_BUCKET_NAME` | `cretexainovamind` |
| `QDRANT_URL` | `https://YOUR_QDRANT_CLUSTER_URL` |

> **Note on AWS credentials in agent service:** Because the agent task has `novamindAgentTaskRole` attached, the AWS SDK automatically uses the role credentials. **Do NOT set `AWS_ACCESS_KEY_ID` or `AWS_SECRET_KEY` in the task definition.** Remove them. The SDK's credential chain finds the IAM role automatically via ECS metadata. This is the correct production approach.

**Secrets (from Secrets Manager):**

| Env var name | Secret ARN |
|-------------|-----------|
| `MONGODB_URI` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/agent/mongodb-uri` |
| `GROQ_API_KEY` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/agent/groq-api-key` |
| `GOOGLE_API_KEY` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/agent/google-api-key` |
| `OPENROUTER_API_KEY` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/agent/openrouter-api-key` |
| `TAVILY_API_KEY` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/agent/tavily-api-key` |
| `QDRANT_API_KEY` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/agent/qdrant-api-key` |

**Log configuration:**

| Setting | Value |
|---------|-------|
| Log group | `/ecs/novamind-agent` |
| Stream prefix | `agent` |

---

### 15.5 Task Definition: Billing Service

| Setting | Value |
|---------|-------|
| Family name | `novamind-billing` |
| CPU | 0.5 vCPU |
| Memory | 1 GB |
| Task execution role | `novamindECSTaskExecutionRole` |
| Task role | (none needed) |

**Container definition:**

| Setting | Value |
|---------|-------|
| Container name | `billing` |
| Image URI | `637423369471.dkr.ecr.us-east-1.amazonaws.com/billing-service:latest` |
| Port | `8004` |

**Environment variables (plain):**

| Name | Value |
|------|-------|
| `PORT` | `8004` |
| `NODE_ENV` | `production` |
| `AUTH_SERVICE` | `http://novamind-auth.novamind.local:8001` |
| `RAZORPAY_KEY_ID` | `rzp_test_Tce3KzaAQlK513` ← your key ID (not secret) |

**Secrets:**

| Env var name | Secret ARN |
|-------------|-----------|
| `MONGODB_URI` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/billing/mongodb-uri` |
| `RAZORPAY_KEY_SECRET` | `arn:aws:secretsmanager:us-east-1:637423369471:secret:novamind/billing/razorpay-secret` |

**Log configuration:**

| Setting | Value |
|---------|-------|
| Log group | `/ecs/novamind-billing` |
| Stream prefix | `billing` |

---

## 16. ECS Services and Internal Service Communication

### What is an ECS Service?

A task definition is the blueprint. An **ECS service** is what keeps that blueprint running. You tell the service: "always keep 1 copy of this task running." If the task crashes, the service automatically starts a new one.

### 16.1 Create ECS Service: Gateway

The gateway is the only service that connects to the ALB. We create it last among the 5 to reference the ALB target group.

**AWS Console — ECS → Clusters → novamind-cluster → Services → Create:**

| Setting | Value |
|---------|-------|
| Launch type | Fargate |
| Task definition | `novamind-gateway` (latest revision) |
| Service name | `novamind-gateway-service` |
| Desired tasks | `1` |
| VPC | `novamind-vpc` |
| Subnets | Both **private** subnets |
| Security group | `novamind-ecs-sg` |
| Public IP | **Disabled** (private subnet) |
| Load balancer | Application Load Balancer (see Section 17) |
| Service discovery | (optional, not strictly needed for gateway) |

### 16.2 Create ECS Services: Auth, Chat, Agent, Billing

Each of these services should be registered with Cloud Map for internal DNS.

**For each service (repeat this pattern):**

**AWS Console:**

| Setting | Auth | Chat | Agent | Billing |
|---------|------|------|-------|---------|
| Task definition | `novamind-auth` | `novamind-chat` | `novamind-agent` | `novamind-billing` |
| Service name | `novamind-auth-service` | `novamind-chat-service` | `novamind-agent-service` | `novamind-billing-service` |
| Desired tasks | `1` | `1` | `1` | `1` |
| Subnets | private | private | private | private |
| Security group | `novamind-ecs-sg` | `novamind-ecs-sg` | `novamind-ecs-sg` | `novamind-ecs-sg` |
| Public IP | Disabled | Disabled | Disabled | Disabled |

**Service Discovery (Cloud Map) — enable for each:**
- Namespace: `novamind.local`
- Service: select the matching one created in Section 14.3 (`novamind-auth`, `novamind-chat`, etc.)

### 16.3 Inter-Service Communication — Local vs AWS

This is one of the most important concepts to understand.

**Locally** (your `.env` files):
```
AUTH_SERVICE=http://localhost:8001
CHAT_SERVICE=http://localhost:8002
AGENT_SERVICE=http://localhost:8003
BILLING_SERVICE=http://localhost:8004
```

**On AWS** (ECS task definition environment variables):
```
AUTH_SERVICE=http://novamind-auth.novamind.local:8001
CHAT_SERVICE=http://novamind-chat.novamind.local:8002
AGENT_SERVICE=http://novamind-agent.novamind.local:8003
BILLING_SERVICE=http://novamind-billing.novamind.local:8004
```

**How Cloud Map DNS works:**
When the agent service calls `http://novamind-auth.novamind.local:8001/deduct-credits`, AWS Cloud Map resolves `novamind-auth.novamind.local` to the private IP of the running auth task. If the task restarts with a new IP, Cloud Map automatically updates. Your services always find each other by name, not IP.

**No code changes needed** — only environment variable values change. The gateway's `index.js` already reads from `process.env.AUTH_SERVICE`, `process.env.CHAT_SERVICE` etc.

---

## 17. Application Load Balancer

### What is an ALB and Why Does This Project Need One?

The ALB receives all HTTPS traffic from the internet and forwards it to the gateway ECS service. It handles:
- **HTTPS termination** — decrypts TLS so ECS tasks don't need to handle it
- **Health checks** — removes unhealthy tasks from rotation automatically
- **SSL certificate** — manages the TLS certificate via AWS ACM

Only the **gateway** connects to the ALB. The other 4 services are internal only.

### 17.1 Request an SSL Certificate (ACM)

Before creating the HTTPS listener, you need a certificate.

**AWS Console:**
1. Go to `https://console.aws.amazon.com/acm/`
2. Click **Request a certificate**
3. Request a public certificate
4. Domain name: enter your domain (e.g., `api.yourdomain.com`)
   - If you don't have a domain yet: skip to Step 17.2a (HTTP only)
5. Validation method: **DNS validation**
6. Click Request — then add the CNAME record to your DNS provider
7. Wait for status: **Issued** (can take up to 30 minutes)

Note the Certificate ARN — you need it for the ALB HTTPS listener.

> **No custom domain?** Use HTTP for now (Section 17.2a). You can add HTTPS later. The application works over HTTP during testing.

### 17.2 Create the Application Load Balancer

**AWS Console — EC2 → Load Balancers → Create load balancer → Application Load Balancer:**

| Setting | Value |
|---------|-------|
| Name | `novamind-alb` |
| Scheme | **Internet-facing** |
| IP address type | IPv4 |
| VPC | `novamind-vpc` |
| Subnets | Both **public** subnets |
| Security group | `novamind-alb-sg` |

**Create Target Group first:**

1. EC2 → Target Groups → Create target group
2. Target type: **IP** (required for Fargate)
3. Name: `novamind-gateway-tg`
4. Protocol: HTTP
5. Port: `8000`
6. VPC: `novamind-vpc`
7. Health check:
   - Protocol: HTTP
   - Path: `/` (gateway returns `{"message":"hello from gateway v5"}`)
   - Healthy threshold: 2
   - Unhealthy threshold: 3
   - Interval: 30 seconds
8. Click Create

**Back to ALB — add listeners:**

**17.2a (HTTP only — for testing without domain):**
- Listener: HTTP:80 → Forward to `novamind-gateway-tg`

**17.2b (HTTPS with domain):**
- Listener: HTTP:80 → Redirect to HTTPS:443
- Listener: HTTPS:443 → Forward to `novamind-gateway-tg`
  - SSL certificate: select the ACM certificate from Step 17.1

Click **Create load balancer**.

**Note the ALB DNS name** — it looks like:
```
novamind-alb-1234567890.us-east-1.elb.amazonaws.com
```

This becomes your `VITE_SERVER_URL` for the frontend and the `FRONTEND_URL` for the gateway (after wrapping in CloudFront).

### 17.3 Update Gateway Task Definition with FRONTEND_URL

After CloudFront is created (Section 18), go back to the gateway task definition and update:

```
FRONTEND_URL = https://dxxxxxxxxxxxx.cloudfront.net
```

This is the CORS allowed origin. It must match exactly — no trailing slash.

### 17.4 Verify ALB

**Run in PowerShell — any folder:**

```powershell
aws elbv2 describe-load-balancers `
  --names novamind-alb `
  --region us-east-1 `
  --query "LoadBalancers[*].{Name:LoadBalancerName,DNS:DNSName,State:State.Code}" `
  --output table
```

**Expected:**

```
-----------------------------------------------------------------------
|             DescribeLoadBalancers                                   |
+-------------------+---------------------------------+---------------+
|  Name             |  DNS                            |  State        |
+-------------------+---------------------------------+---------------+
|  novamind-alb     |  novamind-alb-xxxx.elb.amazonaws.com | active   |
+-------------------+---------------------------------+---------------+
```

---

## 18. Frontend Deployment — S3 + CloudFront

### How Frontend Deployment Works

The React app is not a server — after `npm run build`, it becomes a folder of static HTML, CSS, and JavaScript files. These files go into S3. CloudFront sits in front of S3 and delivers them over HTTPS globally.

**Critical concept — Vite build-time variables:**

The `frontend/.env.example` documents this clearly:
```
# API Gateway URL
# AWS production: https://your-alb-dns.us-east-1.elb.amazonaws.com
VITE_SERVER_URL=http://localhost:8000
```

`VITE_SERVER_URL` is read by Vite during `npm run build` and **baked into the JavaScript bundle**. It is NOT a runtime variable. This means:
- You must set the correct production URL **before** running `npm run build`
- The built JS files will contain the hardcoded ALB/CloudFront URL
- If you change the URL later, you must rebuild and redeploy

### 18.1 Update Frontend Environment for Production

**Edit `frontend/.env`** (or set as GitHub Secret for CI/CD):

```
VITE_FIREBASE_API_KEY=AIzaSyDjTlZRCkMOqmpbuAhgEzsOg8_f4XjVLxM
VITE_RAZORPAY_KEY_ID=rzp_test_Tce3KzaAQlK513
VITE_SERVER_URL=https://novamind-alb-xxxx.us-east-1.elb.amazonaws.com
VITE_ADMIN_EMAIL=aamirimran49000@gmail.com
```

Replace `VITE_SERVER_URL` with your actual ALB DNS name (or CloudFront API URL if you set up a custom domain).

### 18.2 Build the Frontend

**Run in PowerShell — `frontend/` folder:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI\frontend"
npm install
npm run build
```

**Expected output:**

```
vite v8.x.x building for production...
✓ 150 modules transformed.
dist/index.html                   1.23 kB
dist/assets/index-xxxxxxxx.js   420.50 kB
dist/assets/index-xxxxxxxx.css   48.30 kB
✓ built in 8.50s
```

Verify the `dist/` folder was created:

```powershell
Get-ChildItem "E:\GenAi-Project-Cloudage\1.cortexAI\frontend\dist"
```

You should see `index.html` and an `assets/` folder.

### 18.3 Upload to S3

**Run in PowerShell — project root:**

```powershell
aws s3 sync `
  frontend/dist `
  s3://novamind-frontend-prod `
  --delete `
  --region us-east-1
```

The `--delete` flag removes old files that no longer exist in the build. This ensures stale JS bundles don't remain in S3 after a rebuild.

**Expected output:**

```
upload: frontend\dist\index.html to s3://novamind-frontend-prod/index.html
upload: frontend\dist\assets\index-xxxx.js to s3://...
upload: frontend\dist\assets\index-xxxx.css to s3://...
```

### 18.4 Create CloudFront Distribution

**AWS Console — CloudFront → Create distribution:**

| Setting | Value |
|---------|-------|
| Origin domain | `novamind-frontend-prod.s3-website-us-east-1.amazonaws.com` ← S3 **website** endpoint, NOT REST endpoint |
| Origin protocol | HTTP only |
| Viewer protocol policy | **Redirect HTTP to HTTPS** |
| Cache policy | `CachingOptimized` |
| Default root object | `index.html` |

**Custom error pages (critical for React Router):**
1. HTTP error code: `403` → Response page path: `/index.html` → HTTP response code: `200`
2. HTTP error code: `404` → Response page path: `/index.html` → HTTP response code: `200`

These ensure that when a user refreshes the page at `/admin`, CloudFront returns `index.html` (the React app) instead of a 404.

Click **Create distribution**. Wait 5–15 minutes for status to change to **Enabled**.

**Note the CloudFront domain name:**
```
dxxxxxxxxxxxx.cloudfront.net
```

This is your production frontend URL. Share this with users.

### 18.5 Invalidate CloudFront Cache After Updates

After every frontend redeployment, CloudFront caches the old files. Force a cache refresh:

**Run in PowerShell — any folder:**

```powershell
aws cloudfront create-invalidation `
  --distribution-id YOUR_DISTRIBUTION_ID `
  --paths "/*" `
  --region us-east-1
```

Replace `YOUR_DISTRIBUTION_ID` with your actual distribution ID (starts with `E`). The CI/CD pipeline (`deploy.yml`) does this automatically.

### 18.6 Verify Frontend Works

Open in browser:
```
https://dxxxxxxxxxxxx.cloudfront.net
```

**Expected:** NovaMind AI login page loads with the logo.

**If you see a blank page or error:** Open browser DevTools (F12) → Console tab. If you see `http://localhost:8000` in failed requests, the `VITE_SERVER_URL` was not set correctly before building. Rebuild with the correct URL.

---

## 19. External Services Configuration

### 19.1 MongoDB Atlas — Whitelist NAT Gateway IP

MongoDB Atlas uses an IP whitelist. Your ECS tasks are in private subnets and reach the internet through the NAT Gateway. You must add the NAT Gateway's public IP to Atlas.

**Find NAT Gateway IP:**

**Run in PowerShell — any folder:**

```powershell
aws ec2 describe-nat-gateways `
  --region us-east-1 `
  --query "NatGateways[*].NatGatewayAddresses[*].PublicIp" `
  --output table
```

Note the public IP (e.g., `3.123.456.789`).

**In MongoDB Atlas:**
1. Go to `https://cloud.mongodb.com/`
2. Your project → Network Access → IP Access List
3. Click **Add IP Address**
4. Enter the NAT Gateway public IP
5. Description: `AWS ECS NAT Gateway`
6. Click Confirm

> **Why not whitelist `0.0.0.0/0`?** That would allow anyone on the internet to try to connect to your database. Use the specific NAT Gateway IP.

### 19.2 Firebase — Authorize Production Domain

Firebase only allows sign-in from domains you explicitly whitelist. Your CloudFront domain is new and must be added.

**In Firebase Console:**
1. Go to `https://console.firebase.google.com/`
2. Select project: **cortexnovamind**
3. Authentication → Settings → Authorized domains
4. Click **Add domain**
5. Add: `dxxxxxxxxxxxx.cloudfront.net` (your CloudFront URL without `https://`)
6. If you have a custom domain, add that too
7. Click Save

> **What happens if you skip this?** When a user clicks "Continue With Google", Firebase will reject the authentication with an "unauthorized domain" error. Login will completely fail in production.

### 19.3 Qdrant Cloud — Verify Connectivity

Qdrant Cloud is accessible via HTTPS from anywhere. Your ECS tasks in private subnets route through NAT Gateway to reach it. No special configuration needed. Verify the credentials are correct in Secrets Manager:

```powershell
aws secretsmanager get-secret-value `
  --secret-id "novamind/agent/qdrant-api-key" `
  --region us-east-1 `
  --query "SecretString" `
  --output text
```

If this returns your Qdrant API key, the secret is correctly stored.

### 19.4 Summary — What External Services Need

| Service | Change needed | Where |
|---------|-------------|-------|
| MongoDB Atlas | Add NAT Gateway IP to IP whitelist | Atlas Console → Network Access |
| Firebase Auth | Add CloudFront domain to Authorized domains | Firebase Console → Auth → Settings |
| Qdrant Cloud | No change needed | Already accessible via HTTPS |
| Groq API | No change needed | Key stored in Secrets Manager |
| Google Gemini | No change needed | Key stored in Secrets Manager |
| OpenRouter | No change needed | Key stored in Secrets Manager |
| Tavily | No change needed | Key stored in Secrets Manager |
| Razorpay | No change needed for test keys | Use live keys for production |


---

## 20. GitHub Actions CI/CD

### What the Existing Pipeline Already Does

The file `.github/workflows/deploy.yml` already contains a **complete, working deployment pipeline**. You do not need to rewrite it. You only need to create the GitHub Secrets it reads from.

Here is exactly what the pipeline does when you push to `main`:

```
git push origin main
        │
        ▼
GitHub Actions triggers automatically
        │
        ▼
Job 1: deploy-backend (runs on ubuntu-latest)
  │
  ├── 1. Checkout your code
  ├── 2. Configure AWS credentials (from GitHub Secrets)
  ├── 3. Login to ECR
  │
  ├── For EACH of 5 services (gateway, auth, chat, agent, billing):
  │     4a. docker build -f backend/{service}/Dockerfile -t {name} backend/
  │     4b. docker tag {name}:latest {ECR_URI}/{name}:latest
  │     4c. docker push {ECR_URI}/{name}:latest
  │
  └── For EACH of 5 services:
        5. aws ecs update-service --cluster {CLUSTER} --service {SERVICE} --force-new-deployment
           (ECS pulls new image, starts new task, drains old task — rolling update)

Job 2: deploy-frontend (runs AFTER backend job succeeds)
  │
  ├── 1. Checkout code
  ├── 2. cd frontend && npm install && npm run build
  │      (Vite reads VITE_* variables from GitHub Actions environment)
  ├── 3. Configure AWS credentials
  ├── 4. aws s3 sync frontend/dist s3://{S3_BUCKET} --delete
  └── 5. aws cloudfront create-invalidation --paths "/*"
```

### 20.1 Create All Required GitHub Secrets

**In your GitHub repository:**
1. Go to your repo on GitHub
2. Settings → Secrets and variables → Actions → New repository secret
3. Create each secret below

| Secret Name | Value | Used in pipeline |
|-------------|-------|-----------------|
| `AWS_REGION` | `us-east-1` | All AWS CLI commands |
| `AWS_ACCOUNT_ID` | `637423369471` | Docker image tagging |
| `AWS_ACCESS_KEY` | Your mlops-user access key ID | `configure-aws-credentials` action |
| `AWS_SECRET_ACCESS_KEY` | Your mlops-user secret key | `configure-aws-credentials` action |
| `ECS_CLUSTER` | `novamind-cluster` | `ecs update-service` |
| `GATEWAY_SERVICE` | `novamind-gateway-service` | `ecs update-service` |
| `AUTH_SERVICE` | `novamind-auth-service` | `ecs update-service` |
| `CHAT_SERVICE` | `novamind-chat-service` | `ecs update-service` |
| `AGENT_SERVICE` | `novamind-agent-service` | `ecs update-service` |
| `BILLING_SERVICE` | `novamind-billing-service` | `ecs update-service` |
| `S3_BUCKET` | `novamind-frontend-prod` | `aws s3 sync` |
| `CLOUDFRONT_DISTRIBUTION_ID` | Your CloudFront distribution ID (starts with `E`) | `aws cloudfront create-invalidation` |
| `VITE_FIREBASE_API_KEY` | `AIzaSyDjTlZRCkMOqmpbuAhgEzsOg8_f4XjVLxM` | Frontend build |
| `VITE_RAZORPAY_KEY_ID` | `rzp_test_Tce3KzaAQlK513` | Frontend build |
| `VITE_SERVER_URL` | `https://novamind-alb-xxxx.us-east-1.elb.amazonaws.com` | Frontend build |
| `VITE_ADMIN_EMAIL` | `aamirimran49000@gmail.com` | Frontend build |

> **Why are VITE_* variables GitHub Secrets?** Vite reads them during `npm run build` which runs inside GitHub Actions. They are injected as environment variables in the Actions runner, not into containers. They get baked into the JavaScript bundle at build time.

### 20.2 Update deploy.yml to Pass VITE Variables

The existing `deploy.yml` runs `npm run build` but does not explicitly set the `VITE_*` environment variables. Add an `env:` block to the frontend build step:

```yaml
- name: build frontend
  env:
    VITE_FIREBASE_API_KEY: ${{ secrets.VITE_FIREBASE_API_KEY }}
    VITE_RAZORPAY_KEY_ID: ${{ secrets.VITE_RAZORPAY_KEY_ID }}
    VITE_SERVER_URL: ${{ secrets.VITE_SERVER_URL }}
    VITE_ADMIN_EMAIL: ${{ secrets.VITE_ADMIN_EMAIL }}
  run: |
    cd frontend
    npm install
    npm run build
```

### 20.3 Test the Pipeline

After setting all GitHub Secrets, trigger the pipeline by pushing any change:

**Run in PowerShell — project root:**

```powershell
cd "E:\GenAi-Project-Cloudage\1.cortexAI"
git add .
git commit -m "trigger deployment"
git push origin main
```

**Monitor the pipeline:**
1. Go to your GitHub repo
2. Actions tab
3. Click the running workflow
4. Watch both jobs: `deploy-backend` and `deploy-frontend`

Each job shows individual step logs. If a step fails, the error is shown inline.

---

## 21. Complete First-Time Deployment Order

Follow this numbered checklist from top to bottom. Do not skip steps — each depends on the previous.

```
PRE-DEPLOYMENT (do locally)
─────────────────────────────────────────────────────────
[ ] 1.  Verify local app works (Section 6)
[ ] 2.  Verify all 5 Docker images build successfully (Section 7)
[ ] 3.  Make required code changes:
        - auth.controller.js: cookie.secure and sameSite
        - All Dockerfiles: FROM node:22-alpine
        - agent/config/s3.js: remove static credentials block
[ ] 4.  Push all code changes to GitHub (git add . && git commit && git push)

AWS INFRASTRUCTURE (one-time setup)
─────────────────────────────────────────────────────────
[ ] 5.  Verify AWS identity (Section 4) — MUST MATCH 637423369471 / mlops-user
[ ] 6.  Create 5 ECR repositories (Section 8.1)
[ ] 7.  Build and push all 5 Docker images to ECR (Section 8.4)
[ ] 8.  Create VPC with public+private subnets (Section 9.1)
[ ] 9.  Create 3 security groups: ALB, ECS, Redis (Section 9.2)
[ ] 10. Create ElastiCache Redis cluster (Section 10.1)
        → Note Redis endpoint URL
[ ] 11. Create frontend S3 bucket with static hosting (Section 11.1)
[ ] 12. Verify app file S3 bucket exists: cretexainovamind (Section 11.3)
[ ] 13. Create all Secrets Manager secrets (Section 12.1)
[ ] 14. Store Firebase serviceAccountKey.json in Secrets Manager (Section 12.2)
[ ] 15. Create IAM roles: execution role, agent task role, auth task role (Section 13)
[ ] 16. Create ECS cluster: novamind-cluster (Section 14.1)
[ ] 17. Create CloudWatch log groups (5) (Section 14.2)
[ ] 18. Create Cloud Map namespace and 4 service discovery services (Section 14.3)
[ ] 19. Create ALB target group: novamind-gateway-tg (Section 17.2)
[ ] 20. Create ALB: novamind-alb (Section 17.2)
        → Note ALB DNS name
[ ] 21. Create 5 ECS task definitions (Section 15)
        → Use Redis endpoint, service discovery DNS, Secrets Manager ARNs
[ ] 22. Create 4 internal ECS services: auth, chat, agent, billing (Section 16.2)
        → Enable Cloud Map for each
[ ] 23. Create gateway ECS service + attach to ALB target group (Section 16.1)

EXTERNAL SERVICES CONFIGURATION
─────────────────────────────────────────────────────────
[ ] 24. Get NAT Gateway public IP and whitelist in MongoDB Atlas (Section 19.1)

FRONTEND DEPLOYMENT
─────────────────────────────────────────────────────────
[ ] 25. Update frontend/.env: set VITE_SERVER_URL to ALB DNS (Section 18.1)
[ ] 26. Build frontend: npm run build (Section 18.2)
[ ] 27. Upload to S3: aws s3 sync (Section 18.3)
[ ] 28. Create CloudFront distribution (Section 18.4)
        → Note CloudFront domain (dxxxx.cloudfront.net)

POST-SETUP UPDATES
─────────────────────────────────────────────────────────
[ ] 29. Update gateway ECS task definition:
        FRONTEND_URL = https://dxxxx.cloudfront.net (exact CloudFront URL)
        Force new deployment of gateway service
[ ] 30. Add CloudFront domain to Firebase Authorized domains (Section 19.2)

CI/CD SETUP
─────────────────────────────────────────────────────────
[ ] 31. Create all GitHub Secrets (Section 20.1)
[ ] 32. Update deploy.yml to pass VITE_* variables at build time (Section 20.2)
[ ] 33. Push to main → watch Actions pipeline run successfully

VERIFICATION
─────────────────────────────────────────────────────────
[ ] 34. Open https://dxxxx.cloudfront.net in browser
[ ] 35. Login with Google works
[ ] 36. Send a test message — AI responds
[ ] 37. File upload and PDF/PPT generation works
[ ] 38. Admin panel accessible at /admin
[ ] 39. Check CloudWatch logs show requests
```

---

## 22. Verification After Deployment

After every major step and after the full deployment, run these checks.

### 22.1 Verify ECS Services Are Running

**Run in PowerShell — any folder:**

```powershell
aws ecs list-services `
  --cluster novamind-cluster `
  --region us-east-1 `
  --output table
```

Then check each service has running tasks:

```powershell
aws ecs describe-services `
  --cluster novamind-cluster `
  --services novamind-gateway-service novamind-auth-service novamind-chat-service novamind-agent-service novamind-billing-service `
  --region us-east-1 `
  --query "services[*].{Name:serviceName,Running:runningCount,Desired:desiredCount,Status:status}" `
  --output table
```

**Expected:**

```
------------------------------------------------------------------------
|                       DescribeServices                               |
+--------------------------+----------+---------+---------+-----------+
|  Name                    | Desired  | Running | Status  |           |
+--------------------------+----------+---------+---------+-----------+
|  novamind-agent-service  |    1     |    1    | ACTIVE  |           |
|  novamind-auth-service   |    1     |    1    | ACTIVE  |           |
|  novamind-billing-service|    1     |    1    | ACTIVE  |           |
|  novamind-chat-service   |    1     |    1    | ACTIVE  |           |
|  novamind-gateway-service|    1     |    1    | ACTIVE  |           |
+--------------------------+----------+---------+---------+-----------+
```

If `Running` is `0`, a task is failing. Check CloudWatch logs immediately.

### 22.2 Check CloudWatch Logs for Errors

**Run in PowerShell — any folder:**

```powershell
# Check the last 20 log events for the gateway
aws logs get-log-events `
  --log-group-name /ecs/novamind-gateway `
  --log-stream-name gateway/gateway/TASK_ID `
  --limit 20 `
  --region us-east-1
```

Or use the AWS Console:
- CloudWatch → Log groups → `/ecs/novamind-gateway` → Select the latest log stream

**What to look for:**
- `gateway started at 8000` → gateway is running
- `auth started at 8001` → auth is running
- `db connected` → MongoDB Atlas connection successful
- Any `Error` or `ECONNREFUSED` messages → something is failing

### 22.3 Verify ALB Health Check

**Run in PowerShell — any folder:**

```powershell
aws elbv2 describe-target-health `
  --target-group-arn YOUR_TARGET_GROUP_ARN `
  --region us-east-1 `
  --query "TargetHealthDescriptions[*].{ID:Target.Id,Port:Target.Port,Health:TargetHealth.State}" `
  --output table
```

**Expected:**

```
------------------------------------
|  DescribeTargetHealth            |
+------------+-------+----------+--+
|  Health    | ID    | Port     |  |
+------------+-------+----------+--+
|  healthy   | 10.0.3.x | 8000  |  |
+------------+-------+----------+--+
```

If health is `unhealthy`, the gateway container is either not running or failing the health check at `GET /`.

### 22.4 Test the API Gateway Directly

**Run in PowerShell — any folder:**

```powershell
Invoke-WebRequest `
  -Uri "http://novamind-alb-xxxx.us-east-1.elb.amazonaws.com/" `
  -UseBasicParsing
```

**Expected response:**

```json
{"message":"hello from gateway v5"}
```

### 22.5 Test Frontend in Browser

1. Open `https://dxxxxxxxxxxxx.cloudfront.net`
2. NovaMind AI login page should load
3. Open DevTools (F12) → Network tab
4. Click "Continue With Google"
5. After login, the `POST /api/auth/login` request should return `200`
6. Dashboard should appear

### 22.6 Verify S3 Frontend Files

**Run in PowerShell — any folder:**

```powershell
aws s3 ls s3://novamind-frontend-prod --region us-east-1
```

**Expected:** `index.html` and `assets/` folder visible.

### 22.7 Verify ElastiCache Is Reachable

You cannot test Redis directly from your local machine (it's in a private subnet). Instead, check that services are working — if login works, Redis sessions are working.

Alternatively, look at auth service CloudWatch logs. If you see `session expired` errors for all requests, Redis is unreachable.

---

## 23. Troubleshooting

### Problem 1: ECS Task Stops Immediately

**Why it happens:** The container starts, then crashes due to a startup error.

**How to check:**
```powershell
aws ecs describe-tasks `
  --cluster novamind-cluster `
  --tasks TASK_ID `
  --region us-east-1 `
  --query "tasks[*].{Status:lastStatus,StoppedReason:stoppedReason}" `
  --output table
```

Also check CloudWatch logs for the stopped task.

**Common causes and fixes:**

| Cause | Fix |
|-------|-----|
| Missing environment variable | Check task definition — add the missing env var |
| MongoDB connection fails | Add NAT Gateway IP to Atlas whitelist |
| Redis connection fails | Verify `REDIS_URL` uses ElastiCache endpoint, not `localhost` |
| `serviceAccountKey.json` not found | Verify Secrets Manager secret exists and startup command is correct in auth task definition |
| Wrong ECR image URI | Verify image was pushed with correct tag to correct region |

---

### Problem 2: ALB Returns 502 Bad Gateway

**Why it happens:** ALB reaches the gateway, but the gateway cannot respond — usually because the ECS task isn't running.

**How to check:**
- Check ECS service: is `runningCount` = 1?
- Check target group health — is target healthy?
- Check CloudWatch logs for gateway errors

**Fix:** Find the task crash reason in CloudWatch logs and resolve it.

---

### Problem 3: ALB Returns 503 Service Unavailable

**Why it happens:** ALB has no healthy targets in the target group.

**How to check:**
```powershell
aws elbv2 describe-target-health `
  --target-group-arn YOUR_TG_ARN `
  --region us-east-1
```

**Fix:** ECS task is not starting or health check path `/` is returning an error. Check CloudWatch logs.

---

### Problem 4: Redis Connection Refused

**Why it happens:** `REDIS_URL` points to wrong endpoint, or security group blocks Redis.

**How to check:** Look for `ECONNREFUSED` in auth or gateway CloudWatch logs.

**Fix:**
1. Verify `REDIS_URL` in ECS task definition uses the exact ElastiCache endpoint
2. Verify `novamind-redis-sg` allows inbound port 6379 from `novamind-ecs-sg`
3. Verify Redis subnet group uses the same private subnets as ECS tasks

---

### Problem 5: MongoDB Atlas Connection Fails

**Why it happens:** NAT Gateway IP not whitelisted in Atlas.

**How to check:** Look for `MongoNetworkError` or `connection timed out` in CloudWatch logs.

**Fix:**
1. Get NAT Gateway IP: `aws ec2 describe-nat-gateways --region us-east-1`
2. Add that IP to MongoDB Atlas → Network Access → IP Access List

---

### Problem 6: CORS Error in Browser

**Why it happens:** `FRONTEND_URL` in the gateway task definition does not exactly match the CloudFront URL the browser is using.

**How to check:** Browser DevTools → Console → look for `Access-Control-Allow-Origin` errors

**Fix:**
1. Note the exact URL in the browser address bar (e.g., `https://dxxxx.cloudfront.net`)
2. Update gateway ECS task definition: `FRONTEND_URL=https://dxxxx.cloudfront.net` (no trailing slash)
3. Force new deployment of gateway service

---

### Problem 7: Login Fails — "Unauthorized Domain"

**Why it happens:** Firebase rejects sign-in because the CloudFront domain is not in the authorized domains list.

**How to check:** Browser DevTools → Console → Firebase error about unauthorized domain

**Fix:** Firebase Console → Authentication → Settings → Authorized domains → Add `dxxxx.cloudfront.net`

---

### Problem 8: Cookie/Session Not Working — All Requests Return 401

**Why it happens:** `cookie.secure = false` prevents the browser from sending the cookie over HTTPS.

**How to check:** Browser DevTools → Application → Cookies → check if `session` cookie is present

**Fix:** In `auth.controller.js`, change:
```javascript
secure: false  →  secure: process.env.NODE_ENV === "production"
sameSite: "strict"  →  sameSite: process.env.NODE_ENV === "production" ? "none" : "strict"
```
Rebuild Docker image, push to ECR, force new ECS deployment.

---

### Problem 9: Frontend Calls localhost:8000

**Why it happens:** `VITE_SERVER_URL` was not set correctly before `npm run build`.

**How to check:** Browser DevTools → Network tab → look at the URL of failed API requests

**Fix:**
1. Update `frontend/.env`: `VITE_SERVER_URL=https://your-alb-dns.elb.amazonaws.com`
2. Rebuild: `npm run build`
3. Re-upload to S3: `aws s3 sync frontend/dist s3://novamind-frontend-prod --delete`
4. Invalidate CloudFront: `aws cloudfront create-invalidation --distribution-id ID --paths "/*"`

---

### Problem 10: ECS Cannot Reach Internet (Cannot Call Groq, Firebase, Atlas)

**Why it happens:** ECS tasks are in private subnets but NAT Gateway is missing or route table is wrong.

**How to check:** Check CloudWatch logs for connection timeout errors to external services.

**Fix:**
1. Verify NAT Gateway exists in a **public** subnet (not private)
2. Verify the private subnet route table has a route: `0.0.0.0/0 → nat-xxxxxxxx`
3. Verify NAT Gateway status is `available`

---

### Problem 11: Docker Build Fails — "COPY failed: file not found"

**Why it happens:** Building from wrong directory. All builds must use `backend/` as context.

**Correct command:**

```powershell
# CORRECT — context is backend/
docker build -f backend/services/auth/Dockerfile -t auth-service backend/

# WRONG — context is the service folder
docker build -f Dockerfile -t auth-service backend/services/auth/
```

---

### Problem 12: GitHub Actions Fails — "ECR login failed"

**Why it happens:** GitHub Secret `AWS_ACCESS_KEY` or `AWS_SECRET_ACCESS_KEY` is wrong or expired.

**Fix:**
1. Go to AWS Console → IAM → Users → mlops-user → Security credentials
2. Create a new access key
3. Update GitHub Secrets with new values

---

### Problem 13: Secrets Manager Permission Denied

**Why it happens:** ECS task execution role does not have permission to read secrets.

**How to check:** CloudWatch logs show `AccessDeniedException: User is not authorized to perform: secretsmanager:GetSecretValue`

**Fix:** Add the inline policy from Section 13.1 to `novamindECSTaskExecutionRole`.

---

### Problem 14: S3 AccessDenied When Agent Uploads Files

**Why it happens:** Agent task role does not have S3 write permission, or static credentials were removed but IAM role was not attached.

**Fix:**
1. Verify `novamindAgentTaskRole` is attached to the agent task definition as the **task role** (not execution role)
2. Verify the inline policy allows `s3:PutObject` on `arn:aws:s3:::cretexainovamind/*`
3. Verify `AWS_ACCESS_KEY_ID` and `AWS_SECRET_KEY` are **not** set in the agent task definition (they would override the IAM role)

---

### Problem 15: CloudFront Serving Old Files After Deployment

**Why it happens:** CloudFront caches files for up to 24 hours by default.

**Fix:**

```powershell
aws cloudfront create-invalidation `
  --distribution-id YOUR_DISTRIBUTION_ID `
  --paths "/*" `
  --region us-east-1
```

The CI/CD pipeline does this automatically. If you deployed manually, run this command.

---

## 24. Security Checklist

Go through this checklist before declaring the deployment production-ready.

### Secrets and Credentials

- [ ] No API keys in any `.env` file that gets committed to git (check `.gitignore` includes `.env`)
- [ ] No `serviceAccountKey.json` in git (check `.gitignore`)
- [ ] No static `AWS_ACCESS_KEY_ID` or `AWS_SECRET_KEY` in agent ECS task definition — using IAM Task Role instead
- [ ] All secrets stored in Secrets Manager under `novamind/*` prefix
- [ ] Firebase service account JSON stored in Secrets Manager, not in Docker image

### Cookies and Authentication

- [ ] `cookie.secure = true` (or `process.env.NODE_ENV === "production"`) in `auth.controller.js`
- [ ] `cookie.sameSite = "none"` in production with `secure: true`
- [ ] `cookie.httpOnly = true` — already set, do not change

### Network Security

- [ ] ECS tasks in **private subnets** — no public IPs assigned
- [ ] ElastiCache Redis in private subnets — only accessible from `novamind-ecs-sg`
- [ ] ALB security group allows only ports 80 and 443 from internet
- [ ] ECS security group allows only traffic from ALB security group on ports 8000–8004
- [ ] Redis security group allows only port 6379 from ECS security group
- [ ] MongoDB Atlas IP whitelist contains only the NAT Gateway IP (not 0.0.0.0/0)

### IAM Least Privilege

- [ ] `novamindECSTaskExecutionRole` has only `AmazonECSTaskExecutionRolePolicy` + Secrets Manager read for `novamind/*`
- [ ] `novamindAgentTaskRole` has only S3 access to `cretexainovamind/*`
- [ ] `novamindAuthTaskRole` has only Secrets Manager read for the Firebase secret
- [ ] `mlops-user` does not have `AdministratorAccess`

### HTTPS

- [ ] CloudFront enforces HTTPS (`Redirect HTTP to HTTPS`)
- [ ] ALB listener redirects HTTP:80 → HTTPS:443 (if custom domain + ACM certificate)
- [ ] No hardcoded `http://` URLs in production environment variables

### S3 Security

- [ ] Frontend bucket: only `s3:GetObject` is public — no `s3:PutObject` or `s3:DeleteObject`
- [ ] App file bucket (`cretexainovamind`): not publicly accessible — files served via presigned URLs only

---

## 25. AWS Cleanup — Avoid Unnecessary Charges

> ⚠️ **WARNING: The commands in this section are DESTRUCTIVE and IRREVERSIBLE.**
> Only run these if you want to permanently remove all AWS resources.
> Some resources generate charges every hour even when idle — especially NAT Gateway (~$0.045/hr) and ElastiCache.

### Cost Impact of Doing Nothing

If you leave everything running after testing:
- NAT Gateway: ~$33/month (charged by hour + data transfer)
- ALB: ~$17/month (charged by hour)
- ElastiCache cache.t3.micro: ~$12/month
- ECS Fargate (5 tasks): ~$75/month
- **Total: ~$137+/month** while idle

### 25.1 Scale Down ECS to Zero (Cheapest Option — Keeps Resources)

This stops the Fargate compute charges but keeps everything else in place for quick restart.

**Run in PowerShell — any folder:**

```powershell
# Scale all services to 0 tasks
$services = @("novamind-gateway-service","novamind-auth-service","novamind-chat-service","novamind-agent-service","novamind-billing-service")

foreach ($svc in $services) {
    aws ecs update-service `
      --cluster novamind-cluster `
      --service $svc `
      --desired-count 0 `
      --region us-east-1
    Write-Host "Scaled $svc to 0"
}
```

To restart later, set `--desired-count 1` for each service.

### 25.2 Full Cleanup — Delete Everything

Delete in this order (dependencies matter — you cannot delete a VPC that has resources in it).

#### Step 1 — Delete ECS Services

```powershell
$services = @("novamind-gateway-service","novamind-auth-service","novamind-chat-service","novamind-agent-service","novamind-billing-service")

foreach ($svc in $services) {
    # Scale to 0 first
    aws ecs update-service --cluster novamind-cluster --service $svc --desired-count 0 --region us-east-1
}

Start-Sleep -Seconds 30  # Wait for tasks to drain

foreach ($svc in $services) {
    aws ecs delete-service --cluster novamind-cluster --service $svc --region us-east-1
    Write-Host "Deleted $svc"
}
```

#### Step 2 — Delete ECS Cluster

```powershell
aws ecs delete-cluster --cluster novamind-cluster --region us-east-1
```

#### Step 3 — Delete ECR Repositories (⚠️ deletes all Docker images)

```powershell
$repos = @("gateway","auth-service","chat-service","agent-service","billing-service")

foreach ($repo in $repos) {
    aws ecr delete-repository --repository-name $repo --force --region us-east-1
    Write-Host "Deleted ECR repo: $repo"
}
```

#### Step 4 — Delete CloudFront Distribution

```powershell
# First disable it (required before deletion)
# AWS Console: CloudFront → Distributions → select → Disable → wait for Deployed status → Delete
# OR via CLI:
aws cloudfront get-distribution-config --id YOUR_DIST_ID --region us-east-1
# Note ETag from output, then:
# aws cloudfront update-distribution --id YOUR_DIST_ID --if-match ETAG --distribution-config '{...with Enabled:false}'
# Wait ~5 minutes, then delete
```

> **Easiest:** Use AWS Console for CloudFront. CLI requires ETag handling.

#### Step 5 — Empty and Delete S3 Frontend Bucket (⚠️ deletes all frontend files)

```powershell
# Empty the bucket first
aws s3 rm s3://novamind-frontend-prod --recursive --region us-east-1

# Delete the bucket
aws s3 rb s3://novamind-frontend-prod --region us-east-1
```

#### Step 6 — Delete ElastiCache Redis (⚠️ deletes all session data)

```powershell
aws elasticache delete-cache-cluster `
  --cache-cluster-id novamind-redis `
  --region us-east-1
```

Wait ~5 minutes for deletion.

#### Step 7 — Delete ALB and Target Group

```powershell
# Get ALB ARN
aws elbv2 describe-load-balancers --names novamind-alb --region us-east-1 --query "LoadBalancers[*].LoadBalancerArn" --output text

# Delete ALB
aws elbv2 delete-load-balancer --load-balancer-arn YOUR_ALB_ARN --region us-east-1

# Wait 2 minutes, then delete target group
aws elbv2 describe-target-groups --names novamind-gateway-tg --region us-east-1 --query "TargetGroups[*].TargetGroupArn" --output text
aws elbv2 delete-target-group --target-group-arn YOUR_TG_ARN --region us-east-1
```

#### Step 8 — Delete Secrets Manager Secrets

```powershell
$secrets = @(
    "novamind/auth/mongodb-uri",
    "novamind/auth/firebase-service-account",
    "novamind/chat/mongodb-uri",
    "novamind/agent/mongodb-uri",
    "novamind/agent/groq-api-key",
    "novamind/agent/google-api-key",
    "novamind/agent/openrouter-api-key",
    "novamind/agent/tavily-api-key",
    "novamind/agent/qdrant-api-key",
    "novamind/billing/mongodb-uri",
    "novamind/billing/razorpay-secret"
)

foreach ($secret in $secrets) {
    aws secretsmanager delete-secret `
      --secret-id $secret `
      --force-delete-without-recovery `
      --region us-east-1
    Write-Host "Deleted secret: $secret"
}
```

#### Step 9 — Delete Cloud Map Services and Namespace

```powershell
# AWS Console: Route 53 → Cloud Map → Namespaces → novamind.local
# Delete all services first, then delete namespace
# CLI requires service IDs which vary — easiest via Console
```

#### Step 10 — Delete VPC and Networking (⚠️ deletes NAT Gateway which takes ~5 minutes)

> **Do this LAST.** VPC deletion fails if any resources are still using it.

**AWS Console (recommended):**
1. VPC → Your VPCs → select `novamind-vpc`
2. Actions → Delete VPC
3. AWS will list everything inside the VPC that will be deleted (subnets, route tables, internet gateway, NAT Gateway, security groups)
4. Type `delete` to confirm
5. Click Delete

**Note:** NAT Gateway deletion releases the associated Elastic IP. If you had a static IP attached, it stops generating charges.

#### Step 11 — Delete CloudWatch Log Groups

```powershell
$groups = @("/ecs/novamind-gateway","/ecs/novamind-auth","/ecs/novamind-chat","/ecs/novamind-agent","/ecs/novamind-billing")

foreach ($group in $groups) {
    aws logs delete-log-group --log-group-name $group --region us-east-1
    Write-Host "Deleted log group: $group"
}
```

#### Step 12 — Delete IAM Roles

```powershell
# Remove inline policies first, then delete roles
aws iam delete-role --role-name novamindECSTaskExecutionRole
aws iam delete-role --role-name novamindAgentTaskRole
aws iam delete-role --role-name novamindAuthTaskRole
```

### 25.3 Verify Cleanup — Check for Remaining Charges

After cleanup, verify nothing billable is still running:

```powershell
# Check ECS
aws ecs list-clusters --region us-east-1

# Check ECR
aws ecr describe-repositories --region us-east-1

# Check ElastiCache
aws elasticache describe-cache-clusters --region us-east-1

# Check ALB
aws elbv2 describe-load-balancers --region us-east-1

# Check NAT Gateways
aws ec2 describe-nat-gateways --region us-east-1
```

All should return empty results if cleanup was successful.

---

## 26. Final Deployment Checklist

```
PREPARATION
[ ] AWS account verified: 637423369471
[ ] Region verified: us-east-1
[ ] IAM user mlops-user confirmed
[ ] Docker Desktop installed and running
[ ] Local application works at localhost:5173
[ ] All 5 Docker images build successfully

CODE CHANGES FOR AWS
[ ] auth.controller.js: cookie.secure → production conditional
[ ] All 5 Dockerfiles: FROM node:22-alpine
[ ] agent/config/s3.js: static credentials removed

AWS INFRASTRUCTURE
[ ] 5 ECR repositories created
[ ] All 5 Docker images pushed to ECR with :latest tag
[ ] VPC created with public + private subnets
[ ] 3 security groups created: ALB, ECS, Redis
[ ] ElastiCache Redis cluster running (status: available)
[ ] Redis endpoint noted for REDIS_URL
[ ] S3 frontend bucket created with static hosting
[ ] App file S3 bucket (cretexainovamind) accessible
[ ] All 11 secrets created in Secrets Manager
[ ] Firebase JSON stored in Secrets Manager
[ ] 3 IAM roles created: execution, agent task, auth task
[ ] ECS cluster novamind-cluster created
[ ] 5 CloudWatch log groups created
[ ] Cloud Map namespace novamind.local created
[ ] 4 service discovery services created
[ ] ALB target group created
[ ] ALB created and noted DNS name
[ ] 5 ECS task definitions created with correct env vars and secrets
[ ] 4 internal ECS services created with Cloud Map enabled
[ ] Gateway ECS service created and attached to ALB target group
[ ] All 5 services show runningCount = 1

EXTERNAL SERVICES
[ ] MongoDB Atlas whitelist: NAT Gateway IP added
[ ] Firebase authorized domains: CloudFront domain added

FRONTEND
[ ] VITE_SERVER_URL set to ALB DNS
[ ] npm run build completed
[ ] Frontend dist/ synced to S3
[ ] CloudFront distribution created
[ ] CloudFront domain noted
[ ] Gateway FRONTEND_URL updated to CloudFront domain

CI/CD
[ ] All 16 GitHub Secrets created
[ ] deploy.yml updated with VITE_* env block
[ ] Pipeline triggered and all steps green

APPLICATION TESTING
[ ] Frontend loads at CloudFront URL
[ ] Google login works
[ ] Chat AI response works
[ ] File upload and PDF generation works
[ ] Billing drawer opens
[ ] Admin panel accessible
[ ] CloudWatch logs showing requests
[ ] No CORS errors in browser console
[ ] No localhost:8000 in network requests
```

---

## 27. Interview Explanation

### "How I Deployed NovaMind AI on AWS" — 4–5 Minute Answer

Here is exactly how to explain this in an interview. Speak naturally and confidently.

---

*"NovaMind AI is a microservices application with 5 Node.js backend services, a React frontend, Redis for session management, and MongoDB Atlas as the database. Let me walk you through how I deployed it on AWS.*

*The first thing I noticed is that all 5 backend services already had Dockerfiles and a complete GitHub Actions pipeline was already written in `.github/workflows/deploy.yml`. So the infrastructure I needed to build just had to work with that existing CI/CD setup.*

*For the frontend, I used S3 plus CloudFront. Vite compiles the React app into static HTML, CSS, and JavaScript files. These go into an S3 bucket, and CloudFront sits in front of it for HTTPS and global caching. One important detail — Vite bakes environment variables into the JavaScript bundle at build time, not at runtime. So the API URL has to be set as a GitHub Secret before the CI/CD pipeline runs `npm run build`.*

*For the backend, I used ECS Fargate with ECR. Fargate is the right choice because the services are already containerized and some operations like PPT generation take 30–60 seconds, which rules out Lambda. ECR stores the Docker images. The CI/CD pipeline builds all 5 images, pushes them to ECR, then runs `aws ecs update-service --force-new-deployment` for each service.*

*The most important infrastructure change was Redis. Locally it runs as a Docker container. On AWS I replaced it with ElastiCache. All 5 services connect to Redis via a `REDIS_URL` environment variable, so the only change was pointing that variable to the ElastiCache endpoint in each ECS task definition.*

*For secrets I used AWS Secrets Manager. The agent service needs 6 API keys — Groq, Gemini, OpenRouter, Tavily, Qdrant, and MongoDB. But the trickiest one was the Firebase service account — it's a full JSON file, not just a string. I stored it as a JSON secret in Secrets Manager, then in the auth service ECS task definition, I overrode the container startup command to fetch the JSON from Secrets Manager and write it to disk before `npm start` runs.*

*For networking, all ECS tasks run in private subnets. Only the Application Load Balancer is public. A NAT Gateway allows the private tasks to call external APIs like Groq and MongoDB Atlas. I also had to add the NAT Gateway's public IP to MongoDB Atlas's IP whitelist — that was a non-obvious step that would break the database connection if missed.*

*For internal service communication — locally everything uses localhost. On AWS, I set up AWS Cloud Map service discovery so services find each other by DNS name like `novamind-auth.novamind.local:8001` instead of `localhost:8001`. This is set as an environment variable in each task definition — no code change needed.*

*One code change I did have to make was in the auth service cookie configuration. The session cookie had `secure: false` which prevents the browser from sending it over HTTPS. I changed it to `secure: process.env.NODE_ENV === 'production'` so it works in both environments."*

---

### 20 Likely Interviewer Follow-Up Questions

**Q1: Why ECS Fargate instead of EC2?**
"The services are already containerized. Fargate means I don't manage EC2 instances, OS patches, or auto-scaling groups. I just define CPU and memory per task and AWS handles the rest. Some AI operations take 30–60 seconds — Lambda's execution model and cold starts aren't suited for that."

---

**Q2: Why not Kubernetes/EKS?**
"EKS is significantly more complex — you manage control planes, node groups, ingress controllers. For 5 services with predictable load, ECS is simpler and cheaper. The CI/CD pipeline already uses `aws ecs update-service` which is one command. EKS would require kubectl, Helm, and much more operational overhead that isn't justified at this scale."

---

**Q3: Why ElastiCache instead of running Redis on EC2?**
"ElastiCache is managed — automatic failover, backups, and a stable endpoint. If I ran Redis on EC2, I'd need to handle restarts, patches, and disk management myself. Redis is critical for this project: if it goes down, every authenticated request fails because the gateway validates sessions by reading from Redis."

---

**Q4: How does service-to-service communication work on AWS?**
"Locally services use `localhost:8001`. On AWS I set up AWS Cloud Map — each service registers a DNS name in a private namespace `novamind.local`. The gateway's `AUTH_SERVICE` env var changes from `localhost:8001` to `novamind-auth.novamind.local:8001`. When the task restarts with a new IP, Cloud Map updates automatically. No code change needed — just environment variable values."

---

**Q5: How do you handle secrets in production?**
"Everything goes to AWS Secrets Manager. Non-sensitive values like port numbers and service URLs go as plain ECS environment variables. Sensitive values — MongoDB URIs, API keys, Razorpay secret — are stored in Secrets Manager and referenced by ARN in the task definition. ECS injects them as environment variables at startup. The task execution role has a least-privilege policy to only read secrets under the `novamind/` prefix."

---

**Q6: How does the Firebase service account key work in production?**
"The `serviceAccountKey.json` file is gitignored — it never goes into the Docker image. I store the full JSON content in Secrets Manager. In the auth ECS task definition, I override the container start command with a shell script that fetches the JSON, writes it to the expected file path, then runs `npm start`. This runs fresh on every container start."

---

**Q7: Why does the frontend need to be rebuilt for production?**
"Vite bakes `VITE_*` environment variables into the JavaScript bundle at compile time. `VITE_SERVER_URL=http://localhost:8000` in development becomes `VITE_SERVER_URL=https://alb-dns.elb.amazonaws.com` in production. If you don't rebuild with the correct URL, the browser's API calls go to localhost and fail. In CI/CD, I inject the production URL as a GitHub Secret during the build step."

---

**Q8: Why does the ALB health check use `/`?**
"The gateway returns `{"message":"hello from gateway v5"}` at `GET /`. That's a reliable health check endpoint — it confirms the Express server is running and can respond. If the health check fails, ALB removes the task from rotation and ECS starts a new one."

---

**Q9: Why are ECS tasks in private subnets?**
"If someone found a task's IP address, they could call the auth, agent, or billing services directly — bypassing the gateway's session validation and `protect` middleware entirely. Private subnets prevent direct internet access. Only the ALB is public, and it only forwards to the gateway."

---

**Q10: How does the CI/CD pipeline work?**
"The existing `deploy.yml` triggers on every push to main. It builds all 5 Docker images using `backend/` as the build context — important because all Dockerfiles need the shared Redis client in `backend/shared/`. It pushes to ECR, then calls `ecs update-service --force-new-deployment` for each service, which triggers a rolling update. A second job builds the React frontend and syncs it to S3, then invalidates CloudFront cache."

---

**Q11: What is the build context and why does it matter for Docker?**
"The build context is the folder Docker sends to the daemon. All 5 Dockerfiles need `backend/shared/redis/redis.js` — the shared Redis client used by every service. That file only exists at the `backend/` level. If you build from inside a service folder, `COPY shared ./shared` fails because `shared/` isn't there. The CI/CD pipeline always runs `docker build -f backend/services/auth/Dockerfile backend/` — the last argument is the context."

---

**Q12: How do you handle the MongoDB Atlas connection from AWS?**
"MongoDB Atlas uses an IP whitelist. ECS tasks in private subnets reach the internet through a NAT Gateway which has a fixed public IP. I whitelist that specific NAT Gateway IP in Atlas. If I whitelisted `0.0.0.0/0`, anyone could try to connect to the database."

---

**Q13: What AWS services generate charges even when idle?**
"NAT Gateway charges by the hour plus data transfer — about $33/month just to exist. ALB charges by the hour — about $17/month. ElastiCache charges by the hour — about $12/month. Fargate only charges while tasks are running. To minimize costs during testing, I scale ECS tasks to desired count 0 — this stops Fargate compute charges while keeping the infrastructure in place."

---

**Q14: How do you update the application after deployment?**
"Just push to main. GitHub Actions automatically builds new Docker images, pushes to ECR, and calls `ecs update-service --force-new-deployment`. ECS pulls the latest image, starts a new task, waits for it to pass health checks, then drains and stops the old task. Zero downtime rolling update. For frontend changes, the pipeline rebuilds with Vite and syncs to S3, then invalidates CloudFront so users get fresh files immediately."

---

**Q15: What code changes were required specifically for AWS?**
"Three changes: First, `auth.controller.js` — session cookie `secure: false` must be `true` in production for HTTPS to work. Second, all Dockerfiles — `FROM node` is unpinned and non-reproducible, changed to `FROM node:22-alpine` for consistency and smaller images. Third, `agent/config/s3.js` — removed static `AWS_ACCESS_KEY_ID` and `AWS_SECRET_KEY` to use the IAM Task Role instead, which is more secure since no credentials need to be stored."

---

**Q16: Why CloudFront and not just S3 directly?**
"S3 static website hosting is HTTP only. CloudFront provides HTTPS which is required for the session cookie to work — browsers refuse to send `Secure` cookies over HTTP. CloudFront also provides global edge caching for faster load times and handles the React Router issue by serving `index.html` for unknown paths."

---

**Q17: What monitoring do you have?**
"CloudWatch Logs collects all container stdout/stderr — the gateway uses Morgan for HTTP access logs, all services use console.log for errors. I can query logs by log group per service. For production I'd add CloudWatch metric alarms on ECS task failure count, ALB 5xx error rate, and ElastiCache memory utilization."

---

**Q18: How do you handle the agent service's long-running AI operations on AWS?**
"The agent service makes synchronous LLM calls that can take 30–60 seconds for PPT or PDF generation. ECS Fargate handles this fine — there's no timeout at the container level. The ALB has a default idle timeout of 60 seconds which I'd increase to 300 seconds for the agent service. In the future, I'd move long-running operations to an SQS queue with background workers, but for the current scale, synchronous works."

---

**Q19: What's the difference between the task execution role and the task role?**
"The execution role is used by AWS infrastructure to start the container — pulling the Docker image from ECR, injecting secrets from Secrets Manager into environment variables, writing logs to CloudWatch. The task role is used by the application code at runtime — the agent service uses it to upload files to S3. If I accidentally removed the task role but kept the execution role, the container would start fine but S3 uploads would fail with AccessDenied."

---

**Q20: What would you improve in a production deployment?**
"Several things: First, streaming responses instead of waiting for the full LLM output — reduces perceived latency. Second, moving PPT/PDF generation to an async job queue with SQS so a slow AI operation doesn't block the HTTP thread. Third, adding distributed tracing with AWS X-Ray to trace requests across all 5 services. Fourth, adding CloudWatch alarms that page on-call engineers when error rates spike. Fifth, using multi-AZ ElastiCache with a replica for Redis high availability. The current architecture is solid for a side project but these additions would make it production-grade."

---

*End of NovaMind AI AWS Deployment Guide*

---

> **Built by Aamir** · [GitHub](https://github.com/aamir490) · [LinkedIn](https://www.linkedin.com/in/aamir-imran)
>
> *AWS Account: 637423369471 | IAM User: mlops-user | Region: us-east-1*
