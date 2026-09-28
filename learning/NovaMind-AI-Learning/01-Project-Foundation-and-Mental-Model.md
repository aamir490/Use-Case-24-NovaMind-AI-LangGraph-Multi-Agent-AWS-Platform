# Module 01 — Project Foundation and Mental Model

**Project:** NovaMind AI  
**Learning File:** `01-Project-Foundation-and-Mental-Model.md`  
**Purpose:** Build a correct beginner-to-interview mental model of the project before studying the architecture and code in depth.

---

## Learning Objectives

By the end of this module, I should be able to:

- Explain what NovaMind AI is in simple English.
- Explain why it is a full-stack Generative AI application.
- Explain why the project uses multiple specialized AI workflows.
- Identify the five backend services and their high-level responsibilities.
- Distinguish AI models, providers, tools, workflows, agents, RAG, embeddings, vector databases, APIs, microservices, state, memory, and sessions.
- Explain the roles of MongoDB, Redis, Qdrant, and S3.
- Separate core AI capabilities from supporting application features.
- Distinguish what is implemented, partial, documented/intended, future/proposed, unverified, and not present.
- Discuss the project’s strengths, limitations, and engineering trade-offs.
- Explain NovaMind AI in 30 seconds and 1 minute without overclaiming.

---

## 1. What Is NovaMind AI?

NovaMind AI is a **full-stack Generative AI application** that provides multiple specialized AI capabilities through one user interface.

At a high level, users can:

- ask normal AI questions,
- search the web and receive AI-synthesized answers,
- generate or work with code,
- upload a PDF and ask questions about it,
- generate PDFs,
- generate PowerPoint presentations,
- generate images,
- upload images for AI analysis,
- view conversation history,
- sign in,
- use credits,
- make payments,
- and use administration features.

The important idea is that NovaMind is **not just one LLM call**. It combines normal application engineering with several AI workflows.

---

## 2. Project Foundation & Mental Model Diagram

The diagram below gives a high-level mental model of NovaMind AI before studying each component in depth.

![NovaMind-AI-Project-Foundation-&-Mental-Model](images\01-project-foundation-mental-model.png.png)


### How to Read This Diagram

Read it from top to bottom:

1. The user interacts with the React frontend.
2. The frontend sends requests to the backend.
3. The backend is split into Gateway, Auth, Chat, Agent, and Billing services.
4. The Agent service contains LangGraph-based orchestration and specialized AI workflows.
5. Different workflows use different AI models, providers, tools, and retrieval components.
6. MongoDB, Redis, Qdrant, and S3 handle different types of data and state.
7. AWS services support deployment, storage, secrets, logging, and delivery.

This is a **mental-model diagram**, not the final detailed architecture diagram. The detailed request-flow and architecture diagram belongs in Module 02.

---

## 3. What Does “Full-Stack” Mean?

A full-stack application contains both:

- a **frontend**, which the user sees and interacts with, and
- a **backend**, where server-side logic, APIs, authentication, data access, and other processing happen.

### NovaMind Project Connection

NovaMind has:

- a **React + Redux frontend**, and
- a backend with **five Node.js/Express services**.

Therefore, NovaMind can correctly be described as a full-stack application.

### Important Interview Correction

Do not say:

- “Full-stack means frontend + AWS.”
- “Full-stack means React + AI.”

A better definition is:

> Full-stack means the application includes both user-facing frontend code and server-side/backend application logic.

---

## 4. Why Is NovaMind a Generative AI Application?

Generative AI is AI that can generate new content based on a user’s input or instructions.

Examples include:

- text,
- code,
- images,
- documents,
- audio,
- or video.

NovaMind uses Generative AI in several workflows, including:

- conversational responses,
- code generation,
- document content generation,
- image generation,
- search-result synthesis,
- and document question answering.

### Important Distinction

NovaMind **integrates pretrained AI models and services**.

It does **not** mean that the project trained the underlying foundation models.

A correct way to explain this is:

> “NovaMind is a full-stack application that integrates multiple Generative AI capabilities. The project uses pretrained models for inference rather than training those foundation models from scratch.”

---

## 5. What Does “Multiple Specialized AI Workflows” Mean?

Different user requests require different processing.

For example:

- A normal chat question can use a conversational LLM workflow.
- A web-search request needs search results before the LLM synthesizes an answer.
- A PDF question requires document extraction, chunking, embeddings, vector retrieval, and then generation.
- An image-generation request needs an image-generation provider.
- A coding request uses a coding-specific workflow.

So NovaMind does not treat every request exactly the same.

### High-Level Specialist Workflows

The Agent service contains eight specialist workflows plus routing logic:

1. General Chat
2. Web Search
3. Coding
4. PDF RAG
5. PDF Generation
6. PPT Generation
7. Image Generation
8. Image Analysis

### Important Distinction

A “specialized workflow” does not automatically mean “fully autonomous agent.”

A safer description is:

> NovaMind uses LangGraph to orchestrate and route requests across multiple specialized AI workflows.

---

## 6. High-Level System Mental Model

Think of NovaMind in six layers.

### Layer 1 — User Interface

**React + Redux**

The user interacts with:

- chat,
- sign-in,
- conversation history,
- file upload,
- billing,
- and administration interfaces.

### Layer 2 — Application Services

The backend contains five services:

- **Gateway** — main backend entry point and request routing
- **Auth** — users, authentication, sessions, account-related operations
- **Chat** — conversations and messages
- **Agent** — Generative AI orchestration and specialist workflows
- **Billing** — payment-related workflows

### Layer 3 — AI Orchestration

The Agent service contains:

- LangGraph
- router logic
- specialized workflows

### Layer 4 — AI Models, Providers, and Tools

Examples include:

- Groq
- Gemini
- OpenRouter / DeepSeek
- Tavily
- Stability AI
- Qdrant

These do different jobs and should not all be called “AI models.”

### Layer 5 — Data and State

- MongoDB
- Redis
- Qdrant
- S3

### Layer 6 — Cloud and Operations

The repository includes deployment-related configuration for services such as:

- ECR
- ECS / Fargate
- S3
- CloudFront
- Secrets Manager
- CloudWatch

Some networking components are documented or intended rather than fully verified from live infrastructure.

---

## 7. The Five Backend Services

### Gateway Service

The Gateway is an **Express service** and is the main backend entry point.

Important:

> Express Gateway is **not AWS API Gateway**.

### Auth Service

Responsible for areas such as:

- users,
- authentication,
- sessions,
- account-related operations,
- credits or plan-related operations,
- and some administration functionality.

### Chat Service

Responsible for:

- conversations,
- messages,
- and conversation history.

### Agent Service

The main AI orchestration service.

It contains:

- LangGraph,
- routing,
- specialist workflows,
- model/tool integrations,
- RAG-related processing,
- and artifact-related AI flows.

### Billing Service

Responsible for:

- payment order creation,
- Razorpay integration,
- payment verification,
- and payment-related application flow.

---

## 8. Core AI Capabilities vs Supporting Features

### Core AI Capabilities

These define the AI experience of NovaMind:

- General Chat
- Web Search
- Coding
- PDF RAG
- PDF Generation
- PPT Generation
- Image Generation
- Image Analysis

### Supporting Application Features

These make the AI system usable as a real application:

- authentication,
- sessions,
- conversation persistence,
- credits,
- rate limiting,
- payments,
- generated-file storage,
- logging,
- deployment,
- and security controls.

### Why This Separation Matters

A project feature is not the same thing as a technology.

For example:

- **Feature:** Ask questions about a PDF
- **Architecture:** RAG
- **Technologies:** PDF parsing, Gemini embeddings, Qdrant, Groq

---

## 9. Important Terminology

### Artificial Intelligence

AI is the broad field of building systems that perform tasks associated with human-like intelligence.

### Generative AI

Generative AI creates new content from input or instructions.

### LLM

A Large Language Model is a type of Generative AI model designed to understand and generate language.

### Model

The AI model performs inference for a task.

Examples configured in the project include models such as:

- `openai/gpt-oss-120b`
- `gemini-2.0-flash`
- `gemini-embedding-001`
- `deepseek/deepseek-chat`

### Provider

A provider gives application access to a model or AI capability.

Example:

- OpenRouter = provider/access layer
- DeepSeek = model

Important: a model name that contains `openai/` does not automatically mean the OpenAI API is being used. In this project, `openai/gpt-oss-120b` is called through the Groq client.

### Tool

A tool provides an external capability to a workflow.

Example:

- Tavily = web search tool/service

### Workflow

A workflow is a sequence of steps used to complete a task.

### Agent

An AI agent is a system that can use reasoning, state, tools, and actions toward a goal.

Do not automatically label every LLM function as a fully autonomous agent.

### Agentic AI

Agentic AI describes systems that can use actions, tools, state, or multi-step decisions toward a goal.

NovaMind has bounded agentic orchestration, not open-ended autonomous planning and reflection.

### Router

The router decides which workflow should handle a request.

### Orchestration

Orchestration means coordinating multiple steps or components.

### LangGraph

LangGraph is used to structure and coordinate stateful AI workflow execution.

It is **not the LLM**.

### API

An API is an interface that allows software components to communicate.

### Microservice

A microservice is a separately running service focused on a specific responsibility.

NovaMind’s five backend services can reasonably be described as microservices, although their independence is not perfect.

### RAG

Retrieval-Augmented Generation means:

1. retrieve relevant information,
2. provide it to the language model,
3. generate an answer using that context.

### Embedding

An embedding is a numerical representation of semantic meaning.

### Vector

A vector is an ordered list of numbers.

### Vector Database

A vector database stores vectors and supports similarity search.

In NovaMind, Qdrant is used for this purpose.

### Retrieval

Retrieval means finding the most relevant information before generation.

### Prompt

A prompt is the instruction/context sent to an AI model.

### Inference

Inference means using an already-trained model to produce an output.

### State

State is information the workflow/application needs while processing.

### Memory

Memory refers to information from previous interactions that is reintroduced into the model or workflow.

Stored history is not automatically the same thing as model memory.

### Session

A session is application state used to identify and track a logged-in user across requests.

A login session is not the same thing as LLM memory.

---

## 10. PDF RAG Mental Model

The project’s PDF workflow is a real example of Retrieval-Augmented Generation.

At a high level:

```text
PDF upload
   ↓
Text extraction
   ↓
Chunking
   ↓
Gemini embeddings
   ↓
Vectors
   ↓
Qdrant
   ↓
Similarity retrieval
   ↓
Relevant chunks
   ↓
Groq-backed LLM generation
   ↓
Answer
```

### Current Strength

The project performs real semantic retrieval rather than simply sending the complete document to an LLM.

### Current Limitation

The current document lifecycle is limited. The project does not provide a strong persistent user/document/index mapping for long-term document reuse and text-only follow-up questions.

---

## 11. Data and State Responsibilities

### MongoDB

Used for durable application records such as:

- users,
- conversations,
- messages,
- payments.

### Redis

Used for areas such as:

- sessions,
- conversation-related context/cache,
- rate counters.

### Qdrant

Used for:

- vector storage,
- similarity retrieval,
- PDF RAG.

### S3

Used for:

- generated files,
- generated artifacts,
- and frontend/static delivery-related storage in the deployment setup.

### Important Distinction

Do not call all four “databases” without explaining their different purposes.

---

## 12. External Services and Their Roles

### Firebase / Google Identity

Used for Google sign-in and Firebase ID token verification.

### Groq

Used for LLM inference.

### Google Gemini

Used for:

- image analysis,
- and PDF RAG embeddings.

### OpenRouter / DeepSeek

OpenRouter is the access layer/provider used for the DeepSeek coding model.

### Tavily

Used for web search.

### Stability AI

Used for image generation.

### Qdrant

Used as the vector database for PDF RAG.

### Razorpay

Used for payment/order/checkout flow and signature verification.

### Important Corrections

- LangGraph and LangChain are libraries/frameworks, not hosted model providers.
- Express Gateway is not AWS API Gateway.
- Amazon Bedrock is not actively used for runtime inference in the current verified project.
- Stripe is not part of this project.

---

## 13. What Problem Is NovaMind Designed to Address?

A defensible project-purpose statement is:

> NovaMind AI is designed to provide users with multiple specialized Generative AI capabilities through one application instead of treating every task as one generic chatbot workflow.

The important idea is:

```text
Different user needs
        ↓
Different AI workflows
        ↓
One unified application
```

### Potential Target Users

Based on the functionality, possible target users could include:

- developers,
- students,
- researchers,
- knowledge workers,
- and general users.

These are **possible target users based on functionality**, not verified production customer demographics.

---

## 14. Project Status Classification

Use these six labels:

1. **IMPLEMENTED**
2. **PARTIAL**
3. **DOCUMENTED / INTENDED**
4. **FUTURE / PROPOSED**
5. **UNVERIFIED**
6. **NOT PRESENT**

### Implemented

Examples include:

- React frontend
- five Express services
- LangGraph routing
- eight specialist workflows
- PDF RAG
- Qdrant retrieval
- Firebase authentication
- Redis-backed sessions
- MongoDB persistence
- Razorpay integration
- Dockerfiles
- ECS task definitions
- GitHub Actions deployment workflow

### Partial

Examples include:

- authorization and tenant isolation
- credit enforcement
- payment consistency
- session revocation
- conversation memory limits
- persistent document lifecycle
- structured model-output validation
- upload cleanup
- operational monitoring
- release verification

### Documented / Intended

Examples include parts of the desired AWS networking architecture such as:

- ALB
- private ECS tasks
- VPC/subnets
- security groups
- NAT
- Cloud Map
- HTTPS API design

### Future / Proposed

Examples include:

- persistent document indexes
- atomic credit ledger
- idempotent payment handling
- durable async jobs
- broader automated testing
- AI evaluation
- tracing
- alarms
- immutable deployments
- broader Infrastructure as Code

### Unverified

Examples include:

- current live AWS service health
- current provider availability
- effective IAM permissions
- current S3 bucket policies
- actual live capacity
- latency
- uptime
- disaster-recovery behavior
- real cloud cost

### Not Present

Examples include:

- active Amazon Bedrock inference
- Bedrock Agents
- Bedrock Knowledge Bases
- fully autonomous planner
- reflection loop
- LangGraph checkpointing
- server-side execution/testing of generated code
- model training/fine-tuning
- MLflow
- DVC
- model registry
- drift monitoring
- Kubernetes
- comprehensive Terraform/CDK/CloudFormation
- substantive automated test/evaluation suite

---

## 15. Deployed vs Production-Ready

A deployed project is not automatically production-ready.

A system can be deployed and still have:

- authorization gaps,
- weak testing,
- poor observability,
- unsafe release behavior,
- payment consistency problems,
- race conditions,
- missing rollback,
- or incomplete disaster recovery.

A good description of NovaMind is:

> **production-oriented portfolio application**

rather than:

> **fully production-ready system**

---

## 16. Major Strengths

### Separation of Responsibilities

The five backend services separate major responsibilities.

### Specialized AI Workflows

Different task types use different workflows instead of one generic path.

### Real PDF RAG

The project performs document extraction, chunking, embeddings, vector retrieval, and answer generation.

### Multi-Provider Integration

Different providers are used for different capabilities.

### Full Application Engineering

The project includes:

- authentication,
- sessions,
- persistence,
- billing,
- credits,
- file storage,
- and cloud deployment.

### Containerized AWS Deployment Path

The project includes Docker and ECS/Fargate-oriented deployment configuration.

---

## 17. Major Limitations

### Authorization

Authentication exists, but authorization and resource-ownership enforcement need strengthening.

### Payment and Credit Consistency

Payment verification and credit updates happen across separate services, creating distributed-state consistency risks.

### PDF Document Lifecycle

The current design does not provide a robust persistent document identity/index mapping for long-term reuse.

### Structured AI Output Validation

LLM-produced structured output is not fully protected by strong schema validation and recovery logic.

### Error Handling

Some AI failures may be converted into normal-looking responses, making real technical failures harder to identify.

### Automated Testing

The repository does not contain a strong automated testing/evaluation suite.

### Observability

CloudWatch logging exists, but mature tracing, metrics, alerting, SLOs, and AI-quality observability are limited.

### Release Safety

Deployment is automated, but strong release gates, immutable promotion, smoke checks, and rollback controls are incomplete.

---

## 18. Engineering Trade-Offs

| Decision | Benefit | Cost |
|---|---|---|
| Multiple backend services | Clear responsibilities | More distributed-system complexity |
| Multiple AI providers | Task-specific flexibility | More integration and operational complexity |
| LangGraph orchestration | Explicit workflow structure | Additional framework complexity |
| Redis-backed sessions | Centralized shared session state | Extra infrastructure dependency |
| Specialized workflows | Better task-specific behavior | More prompts, errors, tests, and maintenance |

---

## 19. High-Level Project Story

A strong explanation follows this order:

```text
1. Problem
2. User capabilities
3. High-level architecture
4. Backend services
5. AI orchestration
6. Data and storage
7. External providers and tools
8. AWS deployment
9. Strengths
10. Limitations and improvements
```

This is better than giving a technology list.

---

## 20. 30-Second Explanation

> “NovaMind AI is a full-stack Generative AI application that provides multiple specialized AI capabilities through one interface. It supports general chat, web search, coding, PDF RAG, document generation, image generation, and image analysis. The frontend is built with React, and the backend contains five Node.js/Express services. The Agent service uses LangGraph to route each request to the appropriate specialized workflow.”

---

## 21. 1-Minute Explanation

> “NovaMind AI is a full-stack Generative AI application designed to provide multiple specialized AI capabilities through one interface. The frontend is built with React, while the backend contains five Node.js/Express services for gateway, authentication, chat, AI orchestration, and billing. The Agent service uses LangGraph to route requests across workflows such as general chat, web search, coding, PDF RAG, document generation, image generation, and image analysis. The workflows integrate with services such as Groq, Gemini, OpenRouter/DeepSeek, Tavily, Stability AI, and Qdrant. MongoDB, Redis, Qdrant, and S3 handle different types of data and state, and the repository includes Docker and AWS ECS/Fargate deployment configuration.”

---

## 22. Beginner-Friendly Explanation

> “NovaMind AI is an application where users can access different AI features from one place. They can ask questions, search the web, generate code, ask questions about a PDF, create documents or presentations, and work with images. Behind the interface, the application decides which AI workflow should handle each request and then connects to the appropriate model, tool, or storage system.”

---

## 23. Common Mistakes to Avoid

Do not say:

- “I trained all the AI models.”
- “All eight agents are fully autonomous.”
- “LangGraph is the LLM.”
- “Qdrant is an AI agent.”
- “Redis is the vector database.”
- “The project uses AWS API Gateway.”
- “The project actively uses Bedrock inference.”
- “The project is fully production-ready.”
- “Every AWS resource is currently live and verified.”
- “All backend services are perfectly independent.”
- “The PDF RAG supports permanent reusable document memory.”
- “The project has production-grade automated testing.”

---

## 24. Final Mental Model

```text
User
  ↓
React Frontend
  ↓
Express Gateway
  ↓
Auth / Chat / Agent / Billing
              ↓
           LangGraph
              ↓
            Router
              ↓
   Specialized AI Workflows
              ↓
Models / Providers / Tools / RAG
              ↓
MongoDB / Redis / Qdrant / S3
              ↓
Docker + AWS Deployment
```

Remember:

> NovaMind is not “just an LLM.”  
> It is a full application that combines frontend, backend services, AI orchestration, data/state systems, external providers, billing, and AWS deployment.

---

## 25. Final Module Revision Checklist

Before moving to Module 02, I should be able to answer:

- What is NovaMind AI?
- Why is it full-stack?
- Why is it Generative AI?
- Why are there specialized workflows?
- What are the five backend services?
- Which service contains LangGraph?
- What is the difference between an LLM, provider, tool, workflow, and agent?
- What is RAG?
- What is an embedding?
- What is Qdrant?
- What are the roles of MongoDB, Redis, Qdrant, and S3?
- What is implemented?
- What is partial?
- What is not present?
- Why is deployed not the same as production-ready?
- What are the project’s biggest strengths?
- What are the biggest limitations?
- What are the major trade-offs?
- Can I explain the project in 30 seconds?
- Can I explain it in one minute?
