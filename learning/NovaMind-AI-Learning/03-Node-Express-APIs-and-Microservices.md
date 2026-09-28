# Module 03 — Node, Express, APIs and Microservices

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Purpose:** Understand the backend foundations of NovaMind: Node.js, Express, APIs, middleware, service boundaries, service-to-service communication, request/response flow, data access, error handling, and the microservice trade-offs used in this project.  
> **Accuracy rule:** Project-specific statements below are based on the verified repository analysis. General backend concepts are explained separately and should not be confused with claims about features that are not implemented.

---

## Module 03 Architecture Image

![NovaMind AI — Node/Express APIs and Microservices Architecture](images\03-node-express-microservices-architecture.png)

> Place the image at: `learning/images/node-express-microservices-architecture.png`

---

# Module 03 Mental Model

Think about the NovaMind backend like this:

```text
React Frontend
      ↓
Express Gateway :8000
      ↓
 ┌────┼─────┬─────┐
 ↓    ↓     ↓     ↓
Auth Chat  Agent Billing
:8001 :8002 :8003 :8004
 ↓     ↓     ↓     ↓
Mongo Redis Qdrant S3 Razorpay
        + External AI Providers
```

The important idea is:

> **Node.js runs the backend JavaScript, Express defines the HTTP APIs, and the five services divide backend responsibilities.**

---

# Concept 1 — What Is Node.js?

## 1. Simple definition

Node.js is a JavaScript runtime that allows JavaScript to run outside the browser.

Normally JavaScript runs inside a browser:

```text
Browser
 ↓
JavaScript
```

With Node.js:

```text
Server
 ↓
Node.js
 ↓
JavaScript Backend
```

NovaMind uses Node.js for its backend services.

## 2. Why Node.js matters in NovaMind

The backend needs to:

- receive HTTP requests
- verify users
- call AI APIs
- read/write MongoDB
- read/write Redis
- upload files to S3
- call Razorpay
- coordinate LangGraph workflows

Node.js is the runtime executing that server-side JavaScript.

## 3. Node.js is not Express

This distinction is important:

```text
Node.js
= JavaScript runtime

Express
= web framework running on Node.js
```

Node.js gives the environment.

Express makes HTTP API development easier.

## 4. Project fact

The verified backend uses:

- Node.js
- Express
- JavaScript ES modules

It is not a TypeScript backend.

---

# Concept 2 — What Is Express?

## 1. Simple definition

Express is a lightweight web framework for Node.js.

It helps developers create APIs such as:

```text
GET /api/conversations
POST /api/auth/login
POST /api/agent/chat
POST /api/billing/order
```

## 2. Basic Express idea

A simplified example:

```js
app.post("/api/login", async (req, res) => {
  // read request
  // verify user
  // return response
});
```

The important concepts are:

```text
HTTP Method
+
Route
+
Handler
=
API Endpoint
```

## 3. Why Express is useful

Without a framework, you would manually handle more low-level HTTP behavior.

Express provides:

- routing
- middleware
- request parsing
- response helpers
- modular routers
- error-handling patterns

## 4. NovaMind project fact

All five backend services are separate Express applications/processes.

---

# Concept 3 — What Is an API?

## 1. Simple definition

An API is a defined way for one software component to communicate with another.

Example:

```text
React
 ↓
POST /api/agent/chat
 ↓
Backend
```

The frontend does not directly call backend JavaScript functions.

It sends an HTTP request.

## 2. API request contains

A request can contain:

- HTTP method
- path
- headers
- cookies
- body
- query parameters
- uploaded file

## 3. API response contains

A response can contain:

- status code
- headers
- JSON
- error information
- URLs
- generated content

## 4. NovaMind API relationships

```text
Frontend → Gateway

Gateway → Auth
Gateway → Chat
Gateway → Agent
Gateway → Billing

Agent → Chat
Agent → Auth
Billing → Auth
```

This means APIs are used both:

- from frontend to backend
- between backend services

---

# Concept 4 — HTTP Methods and REST Basics

Common HTTP methods:

```text
GET
→ read

POST
→ create / submit / execute

PUT or PATCH
→ update

DELETE
→ delete
```

Examples conceptually:

```text
GET /conversations
POST /login
POST /chat
PATCH /conversation-title
DELETE /conversation
```

A good API should communicate intent clearly.

## Status codes

Common status codes:

```text
200 OK
201 Created
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
429 Too Many Requests
500 Internal Server Error
```

NovaMind has some error-handling paths where specialist failures can be converted into normal assistant text, so HTTP success can sometimes hide underlying AI/provider failure. This is a current reliability limitation.

---

# Concept 5 — Request and Response Lifecycle

A normal backend request follows this pattern:

```text
Client Request
 ↓
Express App
 ↓
Middleware
 ↓
Route Matching
 ↓
Route Handler
 ↓
Business Logic
 ↓
Database / Service / Provider
 ↓
Response
```

For NovaMind:

```text
React
 ↓
Gateway Middleware
 ↓
Gateway Route
 ↓
Agent Service
 ↓
Agent Middleware
 ↓
LangGraph / Workflow
 ↓
AI Provider
 ↓
JSON Response
```

This is the basic pattern you should remember for troubleshooting.

---

# Concept 6 — Express Middleware

## 1. What is middleware?

Middleware is code that runs between the incoming request and the final route handler.

Conceptually:

```text
Request
 ↓
Middleware 1
 ↓
Middleware 2
 ↓
Route Handler
```

Middleware can:

- inspect requests
- authenticate users
- parse JSON
- parse cookies
- log requests
- handle CORS
- process uploaded files
- reject invalid input

## 2. NovaMind examples

The project uses tools/patterns including:

- request logging with Morgan
- file upload handling with Multer
- session/authentication middleware in the Gateway
- CORS configuration
- Express routers

## 3. Why middleware order matters

Express runs middleware in registration order.

A simplified example:

```text
Session middleware
 ↓
Authentication middleware
 ↓
Protected route
```

If authentication middleware runs after the protected route, the route may execute before the user is verified.

---

# Concept 7 — Express Router vs Express Application

A service may use:

```text
Express App
 ↓
Router
 ↓
Specific route handlers
```

For example:

```text
Auth App
 ↓
authRouter
 ↓
/login
/logout
/user
```

Routers help organize related endpoints.

They do not create new microservices.

A router is only an internal code-organization mechanism inside a service.

---

# Concept 8 — The Five NovaMind Backend Services

The project has five backend services.

## Gateway — Port 8000

Responsibilities:

- main backend API entry point
- session resolution
- identity propagation
- request proxying

## Auth — Port 8001

Responsibilities:

- Firebase token verification
- user creation/lookup
- Redis-backed application session creation
- user/account operations
- credits/plan handling

## Chat — Port 8002

Responsibilities:

- conversations
- messages
- history persistence
- MongoDB-backed chat data

## Agent — Port 8003

Responsibilities:

- LangGraph orchestration
- workflow routing
- AI provider integrations
- PDF RAG
- code generation
- document generation
- image workflows

## Billing — Port 8004

Responsibilities:

- Razorpay order creation
- payment verification
- payment persistence
- credit/plan update coordination

---

# Concept 9 — Why Use a Gateway?

Without a Gateway:

```text
React
 ├── Auth
 ├── Chat
 ├── Agent
 └── Billing
```

The frontend would need to understand multiple backend service addresses and potentially repeat authentication behavior.

With Gateway:

```text
React
 ↓
Gateway
 ├── Auth
 ├── Chat
 ├── Agent
 └── Billing
```

Benefits:

- one backend entry point
- centralized session checking
- routing/proxying
- less service-location knowledge in frontend

Trade-off:

> The Gateway can become a critical dependency and potential bottleneck.

Important:

> NovaMind's Express Gateway is not AWS API Gateway.

---

# Concept 10 — Gateway Authentication and Identity Propagation

A protected request conceptually flows like:

```text
Browser
 ↓
Session Cookie
 ↓
Gateway
 ↓
Redis Session Lookup
 ↓
Authenticated userId
 ↓
Downstream Service
```

The Gateway derives the authenticated identity from the server-side session.

It should not trust a client-provided user ID as the source of truth.

## Identity propagation

The Gateway can forward trusted identity information to downstream services.

For example:

```text
x-user-id
```

This creates an important trust boundary:

> Downstream services must trust that the identity header actually came from the Gateway.

That is why internal network exposure and service-to-service authentication matter.

---

# Concept 11 — Service-to-Service Communication

NovaMind services do not operate independently.

Important synchronous calls include:

```text
Agent → Chat
Agent → Auth
Billing → Auth
```

## Agent → Chat

Used for conversation/message persistence.

## Agent → Auth

Used for credit-related account operations.

## Billing → Auth

Used to update credits/plan after payment verification.

## Why this matters

Every synchronous network call adds:

- latency
- failure risk
- retry complexity
- dependency coupling

Example:

```text
Agent works
 ↓
Chat is down
 ↓
Request can still fail
```

This is one reason microservices are operationally more complex than a single-process application.

---

# Concept 12 — Microservices: What They Actually Mean

A microservice architecture usually has independently running services with clear responsibilities.

NovaMind has separate:

- processes
- ports
- Dockerfiles
- task definitions
- service names

So calling it a microservice-style architecture is defensible.

However, independence is incomplete.

## Why?

Because the services still share several forms of coupling:

```text
Agent → Chat
Billing → Auth
Auth admin → other service data
Shared identity/header conventions
All services rebuilt/redeployed together
```

Therefore, the best wording is:

> **NovaMind uses a microservice-style backend with five separately containerized Express services, but some service boundaries remain tightly coupled.**

---

# Concept 13 — Microservices vs Modular Monolith

## Microservices model

```text
Gateway process
Auth process
Chat process
Agent process
Billing process
```

Benefits:

- independent runtime boundaries
- potential independent scaling
- fault isolation possibilities
- clearer domain separation

Costs:

- network calls
- deployment complexity
- distributed debugging
- consistency problems
- more infrastructure

## Modular monolith alternative

```text
One backend process
 ├── auth module
 ├── chat module
 ├── agent module
 └── billing module
```

Benefits:

- simpler deployment
- easier transactions
- fewer network calls
- easier local debugging

Trade-off:

- one deployment unit
- less independent scaling

Neither architecture is automatically better.

---

# Concept 14 — File Uploads with Multer

NovaMind accepts optional uploaded files for workflows such as:

- PDF RAG
- image analysis

Multer is used to process multipart uploads.

Conceptual flow:

```text
Browser
 ↓
multipart/form-data
 ↓
Multer
 ↓
Temporary file
 ↓
Workflow
 ↓
Cleanup
```

## Why multipart?

Because a request may contain:

```text
prompt
conversationId
selectedAgent
file
```

in the same HTTP request.

## Current limitations

Upload validation is partial.

MIME metadata alone is not a full security guarantee.

A stronger production system should validate:

- size
- extension
- content signature
- parser safety
- ownership
- cleanup
- potentially malware scanning

---

# Concept 15 — MongoDB and Mongoose in the Services

Mongoose is the Node.js library used to work with MongoDB.

Think:

```text
Node.js
 ↓
Mongoose
 ↓
MongoDB
```

Models include application entities such as:

- User
- Conversation
- Message
- Payment

## Example concept

```text
User Model
 ↓
MongoDB users collection
```

## Why models matter

Models define application structure and operations around stored data.

## Service ownership issue

A clean microservice architecture normally prefers each service to own its data access boundary.

The repository review found that some Auth admin functionality accesses data associated with Chat/Billing directly, weakening strict service ownership.

---

# Concept 16 — Redis and ioredis

The backend uses Redis through a Node.js Redis client.

Redis supports:

- sessions
- conversation context/cache
- rate counters

Conceptually:

```text
Node.js Service
 ↓
Redis Client
 ↓
Redis / ElastiCache
```

## Why Redis is useful

Redis is fast and shared across service instances.

That makes it useful for server-side session state.

## Why Redis is risky

Redis becomes a shared critical dependency.

If Redis is unavailable:

- session lookup can fail
- protected APIs may fail
- context behavior may degrade
- counters may fail

This is why availability and failover matter.

---

# Concept 17 — Error Handling in Express and Microservices

A backend should distinguish:

```text
Client error
Server error
Dependency error
Business-rule error
```

Examples:

```text
Bad input → 400
No authentication → 401
No permission → 403
Missing resource → 404
Conflict/idempotency issue → 409
Rate limit → 429
Unexpected failure → 500
```

## Current NovaMind weakness

Some AI specialist code catches provider exceptions and converts them into assistant-response text.

That can create:

```text
Provider failed ❌
HTTP response still looks successful ✅
```

This makes:

- monitoring harder
- retry logic harder
- user messaging ambiguous

A stronger design should use structured error types and consistent HTTP/API semantics.

---

# Concept 18 — API Security Fundamentals

This module does not replace the dedicated security module, but API fundamentals include:

## Never trust the browser

The browser can modify:

- request body
- headers
- IDs
- URLs

## Authentication

Who is the caller?

## Authorization

Can this caller perform this action?

## Ownership

Does this conversation/artifact belong to this caller?

## Input validation

Is the supplied data valid?

## Internal trust

Is a service-to-service request really coming from the expected internal caller?

Important:

```text
CORS ≠ Authentication
Private network ≠ Authorization
x-user-id header ≠ proof by itself
```

---

# Concept 19 — API Design Problems in the Current Project

The repository review identified several architecture/API concerns.

## 1. Sensitive account mutation

Routes related to:

- credit deduction
- plan updates

must not trust client-supplied identity/account data.

## 2. Missing ownership checks

Some conversation/message operations do not consistently enforce resource ownership.

## 3. Admin route exposure

Admin boundaries need stronger, centralized authorization.

## 4. Payment consistency

Billing verifies payment, but payment status and credit updates are separate distributed operations.

## 5. Error semantics

Some technical failures are returned as normal AI response text.

## 6. Internal service trust

Internal HTTP calls do not have a strongly verified service-identity layer.

These are not reasons to reject the architecture. They are areas where Production V2 should harden the API layer.

---

# Concept 20 — Backend Troubleshooting by Request Path

When an API is failing, do not randomly check everything.

Trace the request.

Example:

```text
React request
 ↓
Gateway received?
 ↓
Session valid?
 ↓
Correct route?
 ↓
Correct downstream service?
 ↓
Service healthy?
 ↓
Database/provider reachable?
 ↓
Response generated?
 ↓
Response returned?
```

## Example: `/api/agent/chat` fails

Check:

1. frontend request body
2. Gateway logs
3. Redis session
4. Gateway proxy target
5. Agent logs
6. Multer/file handling
7. LangGraph routing
8. provider call
9. Chat persistence
10. returned status/body

## Example: login fails

Check:

1. Firebase token exists
2. Auth receives request
3. Firebase verification succeeds
4. MongoDB reachable
5. user lookup/create
6. Redis reachable
7. session stored
8. cookie returned
9. browser sends cookie later

This path-based approach is much stronger than guessing.

---

# Concept 21 — Backend Deployment Boundaries

Each service has its own runtime/container definition.

That means conceptually:

```text
Gateway image
Auth image
Chat image
Agent image
Billing image
```

These images are stored in ECR and used by ECS/Fargate.

This is one reason the project can reasonably be described as microservice-style.

However, the current deployment pipeline rebuilds/redeploys all five services together.

So:

```text
Separate runtime services ✅
Fully independent deployment lifecycle ❌
```

This is an important interview distinction.

---

# Concept 22 — Final Module 03 Mental Model

Remember:

```text
Node.js
= JavaScript runtime

Express
= HTTP web framework

API
= communication contract

Middleware
= request-processing steps

Gateway
= single backend entry point

Service
= separate runtime responsibility

Microservice architecture
= multiple independently running services

MongoDB
= durable application data

Redis
= fast shared state

Mongoose
= Node.js ↔ MongoDB mapping layer

Multer
= file upload middleware

Service-to-service HTTP
= useful but adds coupling/failure risk
```

And for NovaMind:

```text
React
 ↓
Gateway :8000
 ├── Auth :8001
 ├── Chat :8002
 ├── Agent :8003
 └── Billing :8004
```

The strongest way to explain Module 03 is:

> **Node.js runs the backend JavaScript, Express exposes the APIs, the Gateway centralizes backend entry and session resolution, and four domain services separate authentication, chat persistence, AI orchestration and billing. The system gains clearer responsibility boundaries, but it also introduces network dependencies, distributed consistency issues, and more complex error handling.**

---

# Quick Revision — Module 03

```text
Node.js
→ runtime

Express
→ web/API framework

Five Services
→ Gateway 8000
→ Auth 8001
→ Chat 8002
→ Agent 8003
→ Billing 8004

Gateway
→ session lookup
→ identity propagation
→ request proxying

Auth
→ Firebase verification
→ Redis session
→ account / credits

Chat
→ conversations/messages
→ MongoDB

Agent
→ LangGraph
→ AI workflows
→ providers / Qdrant / S3

Billing
→ Razorpay
→ payment verification
→ Auth credit update

Key Libraries
→ Mongoose = MongoDB
→ ioredis = Redis
→ Multer = uploads
→ Morgan = request logging
→ Axios = HTTP calls

Microservice Strength
→ clear responsibility boundaries

Microservice Weakness
→ network coupling
→ partial failures
→ distributed consistency
→ harder debugging

Important Limitations
→ authorization gaps
→ internal trust assumptions
→ payment/credit consistency
→ inconsistent error semantics
→ deployment independence incomplete
```

**Module 03 learning file complete.**
