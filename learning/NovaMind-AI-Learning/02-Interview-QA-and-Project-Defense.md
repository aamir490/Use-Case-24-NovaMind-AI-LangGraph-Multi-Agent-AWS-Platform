# Module 02 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Scope:** Architecture, request flows, LangGraph routing, data/state, AWS, deployment, security, reliability, scalability, troubleshooting, trade-offs and pressure defense.  
> **Accuracy rule:** Do not turn documented/intended architecture into verified live-state claims.

---

## Practice Method

For every question:

1. Understand what is being tested.
2. Say the answer naturally without reading.
3. Expect a follow-up.
4. Be ready to discuss one limitation or trade-off.
5. Never add an unsupported ownership, HA, scale, security or production-readiness claim.

---

# Foundations & Architecture

## Q1. What is NovaMind AI from an architecture perspective?

**Word-for-word answer:**

> NovaMind is a full-stack Generative AI platform with a React frontend and five Node.js/Express backend services: Gateway, Auth, Chat, Agent and Billing. The Agent service contains LangGraph and routes AI requests to predefined specialist workflows. MongoDB, Redis, Qdrant and S3 support persistence, state, retrieval and generated artifacts.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q2. How many backend services are there?

**Word-for-word answer:**

> There are five backend services: Gateway, Auth, Chat, Agent and Billing. The eight AI specialists are inside the Agent service; they are not eight independent services.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q3. What does the Express Gateway do?

**Word-for-word answer:**

> It is the application backend entry point. It receives requests, resolves protected Redis-backed sessions, derives the authenticated user identity and proxies requests to the correct backend service.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q4. Is your Gateway AWS API Gateway?

**Word-for-word answer:**

> No. It is an Express application service. AWS API Gateway is not part of the verified implementation.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q5. What is the role of the Auth service?

**Word-for-word answer:**

> Auth verifies Firebase login identity, manages the Redis-backed application session, and owns user/account-related state such as plan and credits in the current design.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q6. What is the role of the Chat service?

**Word-for-word answer:**

> Chat handles durable conversation and message persistence in MongoDB. Agent handles AI orchestration while Chat owns conversation storage.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q7. What is the role of the Agent service?

**Word-for-word answer:**

> Agent is the AI orchestration layer. It contains LangGraph, the router, the specialist workflows and integrations with model providers, search, Qdrant and S3.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q8. What is the role of Billing?

**Word-for-word answer:**

> Billing creates Razorpay orders, stores payment records, verifies payment signatures and triggers credit/plan updates through Auth.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q9. What are the eight specialist workflows?

**Word-for-word answer:**

> Chat, Search, Coding, PDF RAG, PDF Generation, PPT Generation, Image Generation and Image Analysis.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q10. Where does LangGraph sit?

**Word-for-word answer:**

> LangGraph sits inside the Agent service. It carries current workflow state and routes execution to the selected specialist workflow.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# End-to-End Flows

## Q11. Walk me through a normal chat request.

**Word-for-word answer:**

> The user sends a prompt from React. The Gateway resolves the Redis-backed session and forwards the request to Agent. Agent persists the user message through Chat, starts LangGraph, routes to the Chat workflow, calls the Groq-backed language-model path, performs credit/context handling, persists the assistant response through Chat and returns the result to React.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q12. Walk me through login.

**Word-for-word answer:**

> The user signs in with Google through Firebase. The frontend sends the Firebase ID token to Auth. Auth verifies it, finds or creates the user in MongoDB, creates an opaque UUID session in Redis and returns an HTTP-only cookie. Later protected requests use that Redis-backed application session.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q13. Is the NovaMind session a JWT?

**Word-for-word answer:**

> No. The application session is an opaque Redis-backed session identifier. The Firebase ID token is separate and is used during login verification.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q14. How does Auto routing work?

**Word-for-word answer:**

> An explicit workflow selection wins first. Otherwise an uploaded PDF routes to PDF RAG and an uploaded image routes to Image Analysis. If neither applies, the system uses model-based classification. Unknown labels can fall back to Chat.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q15. How does web search work?

**Word-for-word answer:**

> The Search workflow calls Tavily for current web results and images, then passes those results with the user's question to the Groq-backed generation path for synthesis.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q16. Does the LLM itself search the web?

**Word-for-word answer:**

> No. Tavily performs the retrieval. The language model synthesizes the retrieved content.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q17. How does PDF RAG work?

**Word-for-word answer:**

> The PDF is parsed to text, split into overlapping chunks, embedded with Gemini embeddings and stored in Qdrant. The question is embedded, Qdrant returns the top relevant chunks, and those chunks are given to the Groq-backed LLM to generate the answer.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q18. What are the key PDF RAG implementation values?

**Word-for-word answer:**

> The current implementation uses roughly 1000-character chunks, about 200-character overlap and top-5 similarity retrieval.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q19. How does Coding work?

**Word-for-word answer:**

> After routing to Coding, the workflow determines the coding intent, calls DeepSeek through OpenRouter, expects structured file output, parses that into a files array and returns a code artifact that the frontend can show in Monaco and preview for compatible frontend code.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q20. Does the coding workflow execute arbitrary server-side code?

**Word-for-word answer:**

> No. It does not provide a complete secure backend execution, package-installation, compile, test and repair environment.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q21. How does PDF generation work?

**Word-for-word answer:**

> The language model creates structured document content, PDFKit renders the actual PDF, the file is uploaded to S3 and the backend returns a presigned URL.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q22. How does PPT generation work?

**Word-for-word answer:**

> The language model creates structured slide content, PptxGenJS creates the PPTX file, the file is uploaded to S3 and a presigned URL is returned.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q23. How does image generation work?

**Word-for-word answer:**

> The workflow prepares the text prompt, calls Stability AI, receives generated image bytes, uploads the image to S3 and returns an access URL.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q24. How does image analysis work?

**Word-for-word answer:**

> The user uploads an image with a question. The backend prepares the image for Gemini multimodal analysis, receives a text response, persists it and cleans up the temporary upload.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q25. Walk me through the payment flow.

**Word-for-word answer:**

> The user chooses a plan, Billing creates a Razorpay order and stores a payment record. After checkout, Billing verifies the Razorpay HMAC signature, marks the payment paid and then calls Auth to update credits and plan.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# Data, State & Memory

## Q26. What is MongoDB used for?

**Word-for-word answer:**

> MongoDB stores durable application data such as users, conversations, messages and payments.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q27. What is Redis used for?

**Word-for-word answer:**

> Redis is used for server-side sessions, conversation-related context/cache and rate counters.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q28. What is Qdrant used for?

**Word-for-word answer:**

> Qdrant stores PDF chunk embeddings and performs semantic similarity retrieval for the PDF RAG workflow.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q29. What is S3 used for?

**Word-for-word answer:**

> S3 stores the built frontend in the hosting path and also stores generated artifacts such as PDFs, PPTX files and images.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q30. What is the difference between MongoDB history, Redis context and LangGraph state?

**Word-for-word answer:**

> MongoDB is durable history, Redis is fast shared runtime state, and LangGraph state is current workflow execution data.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q31. Is stored history automatically LLM memory?

**Word-for-word answer:**

> No. The application must explicitly load and pass relevant history into the model context.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q32. Does Redis mean LangGraph checkpointing is implemented?

**Word-for-word answer:**

> No. Redis application state is separate from LangGraph checkpointing, and durable LangGraph checkpoints are not implemented.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q33. What are current memory weaknesses?

**Word-for-word answer:**

> The review found potentially large history hydration, duplicate-current-message behavior, read-modify-write race conditions, weak size enforcement, TTL preservation issues and no mature token-aware summarization policy.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q34. Can a user upload a PDF once and reliably query it next week?

**Word-for-word answer:**

> Not as a mature persistent knowledge-base feature. The current design lacks a strong durable mapping from user to document to reusable vector index.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q35. What is the artifact-lifecycle limitation?

**Word-for-word answer:**

> Presigned URLs expire. A stronger design would store artifact metadata and the S3 object key, then reauthorize the user and generate a fresh URL when needed.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# AWS Runtime

## Q36. How is the frontend hosted?

**Word-for-word answer:**

> The React build is stored in S3 and delivered through CloudFront in the documented deployment.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q37. What is the documented backend request path?

**Word-for-word answer:**

> React sends API requests through the documented Application Load Balancer to the Express Gateway running as an ECS/Fargate service.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q38. What is the difference between ECS and Fargate?

**Word-for-word answer:**

> ECS orchestrates container tasks and services. Fargate provides the managed compute for those ECS tasks without requiring EC2 host management.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q39. What does ECR do?

**Word-for-word answer:**

> ECR stores the Docker images that ECS tasks pull.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q40. What does Cloud Map do?

**Word-for-word answer:**

> Cloud Map provides internal service discovery so services can resolve logical service names instead of hard-coded task IPs.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q41. Does Cloud Map provide authorization?

**Word-for-word answer:**

> No. Service discovery and service authentication/authorization are different concerns.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q42. Why might private ECS tasks need NAT?

**Word-for-word answer:**

> Because Agent must reach public external APIs such as Groq, Gemini, OpenRouter, Tavily and Stability AI. Private tasks need a controlled outbound path.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q43. What does Secrets Manager do here?

**Word-for-word answer:**

> ECS task definitions reference Secrets Manager for sensitive runtime configuration.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q44. What does CloudWatch provide?

**Word-for-word answer:**

> Container logs are sent to CloudWatch for centralized logging. Mature metrics, tracing and correlation are still limited.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q45. Is high availability verified?

**Word-for-word answer:**

> No. The architecture can support HA patterns, but live desired counts, Redis redundancy, failover and multi-AZ behavior require direct verification.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# Deployment & CI/CD

## Q46. Explain the deployment pipeline.

**Word-for-word answer:**

> A Git push triggers GitHub Actions. The workflow checks out code, authenticates to AWS, logs in to ECR, builds and pushes the five backend images and forces ECS redeployment. The frontend is built, synced to S3 and followed by a CloudFront invalidation.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q47. Why is using `latest` a weakness?

**Word-for-word answer:**

> `latest` is mutable, so it weakens traceability and rollback. Immutable tags based on a commit SHA are safer.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q48. If I edit CPU in the task-definition JSON, will force redeploy apply it?

**Word-for-word answer:**

> Not necessarily. The JSON must be registered as a new ECS task-definition revision and the service updated to use that revision.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q49. How do you know deployment succeeded?

**Word-for-word answer:**

> A successful GitHub Actions run proves the scripted steps completed, not that the application is healthy. Stronger verification would wait for ECS stability, ALB health and smoke tests.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q50. Is this mature CI/CD?

**Word-for-word answer:**

> It is working automated deployment, but strong test gates, immutable promotion, smoke tests, rollback and release verification are incomplete.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q51. Why invalidate CloudFront?

**Word-for-word answer:**

> Because CloudFront may still serve cached frontend files even after a new React build is synced to S3.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q52. Why is rebuilding all services a trade-off?

**Word-for-word answer:**

> It is simple, but it means one small service change can rebuild and redeploy every backend service, increasing release time and risk.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# Security & Trust

## Q53. What is the difference between authentication and authorization?

**Word-for-word answer:**

> Authentication proves who the user is. Authorization determines what that authenticated user is allowed to access or change.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q54. How is identity propagated?

**Word-for-word answer:**

> The Gateway resolves the Redis-backed session and derives the authenticated user identity, then forwards trusted identity information to downstream services.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q55. Why are ownership checks required after login?

**Word-for-word answer:**

> Because login only proves identity. A user must still be prevented from reading or changing another user's conversation, message, artifact or account data.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q56. What is the main tenant-isolation risk?

**Word-for-word answer:**

> Inconsistent object-level authorization. A logged-in user should not be able to change an object ID and access another user's resource.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q57. Why is a private VPC not enough?

**Word-for-word answer:**

> Private networking reduces exposure but does not prove the identity or authorization of an internal caller.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q58. Does CORS secure the API?

**Word-for-word answer:**

> No. CORS is a browser-origin policy, not authentication or authorization.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q59. Why are public credit mutation routes dangerous?

**Word-for-word answer:**

> Credits and plans should be changed only by trusted server-side business logic. The browser must not be allowed to choose the target user or credit amount and have the server trust it.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q60. How would you secure artifact access?

**Word-for-word answer:**

> Store artifact ownership metadata, authenticate the user, verify ownership and only then generate a short-lived presigned URL.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q61. What is prompt injection in this project?

**Word-for-word answer:**

> Web results and uploaded documents are untrusted text. They may contain instructions that try to manipulate the model, so retrieved content must be treated as data rather than trusted system instructions.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q62. What security areas would you prioritize first?

**Word-for-word answer:**

> Object-level authorization, sensitive account mutation paths, credential rotation/hygiene, session revocation and regression tests for cross-user access.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# Reliability & Troubleshooting

## Q63. What is failure propagation?

**Word-for-word answer:**

> It means a failure in one dependency causes the user-facing request or a downstream operation to fail.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q64. Give a partial-success example.

**Word-for-word answer:**

> The LLM may generate a response successfully while saving the assistant message through Chat fails. Provider work succeeded but durable state did not.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q65. Why not retry the whole request blindly?

**Word-for-word answer:**

> Because side effects may already have happened: provider cost, credit deduction, payment processing, message writes or artifact creation.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q66. What if Qdrant fails during PDF RAG?

**Word-for-word answer:**

> I would not silently fall back to normal chat because that removes document grounding. I would return a clear retrieval failure or use a verified alternate retrieval path.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q67. What if PDF rendering succeeds but S3 upload fails?

**Word-for-word answer:**

> The artifact-generation stage succeeded but delivery failed. I would record that stage and retry the upload where safe instead of rerunning the LLM automatically.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q68. Why are timeouts important?

**Word-for-word answer:**

> Without deadlines, slow providers can hold requests open and consume resources for too long.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q69. What is a correlation ID?

**Word-for-word answer:**

> A request identifier propagated across services so logs from one user request can be connected.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q70. What is the current error-handling weakness?

**Word-for-word answer:**

> Some specialist exceptions can be converted into normal response text, which can make failures look like successful HTTP responses.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q71. Chat is not working. How do you troubleshoot?

**Word-for-word answer:**

> I trace the path: frontend request, ALB/Gateway, Redis session, Agent, LangGraph route, provider call, Chat persistence, MongoDB and response path.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q72. PDF answers are wrong. What do you troubleshoot?

**Word-for-word answer:**

> I check extraction, chunking, embeddings, the correct Qdrant collection, retrieved chunks, prompt construction and then final generation.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q73. User paid but has no credits. What do you troubleshoot?

**Word-for-word answer:**

> I check the Razorpay order, payment verification, Payment status, Billing-to-Auth credit call and final user balance.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q74. GitHub Actions succeeded but the app is down. What do you troubleshoot?

**Word-for-word answer:**

> I verify the image push, ECS redeploy, new task startup, logs, secrets, Redis/MongoDB connectivity, ALB target health and a smoke test.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# Scalability & Design Defense

## Q75. What are the likely bottlenecks?

**Word-for-word answer:**

> Potential bottlenecks include Agent, Redis, MongoDB, external provider latency/quotas, synchronous long-running workflows, repeated PDF embedding work, growing context and artifact generation/upload.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q76. Which service would you scale first?

**Word-for-word answer:**

> I would measure first. Agent is a candidate, but the actual bottleneck may be an external provider, Redis or MongoDB.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q77. Does adding more Agent tasks solve everything?

**Word-for-word answer:**

> No. It does not fix provider quotas, shared-state races, payment consistency, duplicate work or external-call latency.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q78. When would you introduce a queue?

**Word-for-word answer:**

> When long-running or retryable operations should not hold an HTTP request open, for example heavy document or image jobs.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q79. Would you split every specialist into its own service?

**Word-for-word answer:**

> No. I would split only when scaling, runtime, security, deployment or ownership requirements justify the operational cost.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q80. Why use LangGraph instead of if/else?

**Word-for-word answer:**

> A simple router could handle basic conditions. LangGraph provides an explicit state/graph model and clearer conditional workflow structure as paths grow, at the cost of framework complexity.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q81. Why use multiple model providers?

**Word-for-word answer:**

> Different providers are used for different capabilities. The benefit is flexibility and task fit; the cost is more credentials, quotas, monitoring, latency profiles and failure modes.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q82. Why Redis sessions?

**Word-for-word answer:**

> Redis gives shared server-side sessions and supports centralized revocation logic, but it becomes a critical runtime dependency.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q83. Why Qdrant?

**Word-for-word answer:**

> Because the PDF RAG workflow needs semantic vector similarity search. The trade-off is another external dependency and lifecycle/latency/cost complexity.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q84. Why S3 for artifacts?

**Word-for-word answer:**

> S3 is a better fit for durable object storage and temporary signed delivery than keeping files on application containers.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q85. Why Fargate?

**Word-for-word answer:**

> It allows containerized workloads without managing EC2 hosts. The trade-off is baseline cost and less host-level control.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q86. Why five services instead of one backend?

**Word-for-word answer:**

> The split separates authentication/account logic, conversation persistence, AI orchestration and billing, but the system still has synchronous coupling. A modular monolith would also be a valid alternative if independent deployment/scaling were not justified.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q87. Where are the weakest boundaries?

**Word-for-word answer:**

> Agent depends on Chat, Billing depends on Auth, some Auth admin functionality reaches other service data, and services share identity/header conventions.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q88. What would you simplify in a rebuild?

**Word-for-word answer:**

> I would keep clear domain boundaries but reconsider whether every boundary needs a separate deployable service, while strengthening authorization, accounting consistency, document lifecycle, observability and release safety.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# Pressure Questions

## Q89. Is NovaMind production-ready?

**Word-for-word answer:**

> I would call it production-oriented, not production-ready. It has meaningful production elements but still needs stronger authorization, payment consistency, tests/evals, observability, release verification, durable lifecycle handling and validated HA.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q90. Is it a fully autonomous multi-agent system?

**Word-for-word answer:**

> No. It is bounded LangGraph orchestration across predefined specialist workflows, not unrestricted autonomous planning, reflection or repeated self-directed tool use.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q91. Does it use Amazon Bedrock?

**Word-for-word answer:**

> Not for active inference in the verified implementation. A dependency or documentation reference does not prove runtime Bedrock usage.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q92. Does RAG eliminate hallucinations?

**Word-for-word answer:**

> No. It improves grounding but still depends on extraction, retrieval quality and model behavior.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q93. How do you know generated code works?

**Word-for-word answer:**

> The current project does not guarantee it. There is no complete secure compile/test/repair loop.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q94. How do you know payment grants credits exactly once?

**Word-for-word answer:**

> The current design does not provide a fully verified exactly-once guarantee. It needs stronger idempotency, transaction keys, ledgering and reconciliation.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q95. How do you know User A cannot access User B's conversation?

**Word-for-word answer:**

> The current project needs stronger object-level authorization, so I would not claim perfect tenant isolation.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q96. Why not make the S3 bucket public?

**Word-for-word answer:**

> Generated artifacts can be user-specific or sensitive. Private S3 objects with short-lived presigned access reduce exposure.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q97. Why not fall back to Chat if Qdrant is down?

**Word-for-word answer:**

> Because that would silently remove document grounding while making the answer appear valid.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q98. The deployment workflow passed. Is production healthy?

**Word-for-word answer:**

> Not necessarily. I still need runtime health checks, ECS stability, ALB target health and smoke tests.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q99. What is the biggest architectural risk?

**Word-for-word answer:**

> The highest-risk areas are authorization/account mutation, payment-to-credit consistency and reliability across synchronous service calls.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

## Q100. What would you improve first in Production V2?

**Word-for-word answer:**

> First fix authorization and sensitive account mutation, rotate exposed credentials, make payments/credits idempotent and auditable, improve session revocation and error semantics, and add regression tests. Then improve observability, release safety, document lifecycle and async processing.

**Likely follow-up direction:** Expect the interviewer to ask **why**, **what can fail**, **what the trade-off is**, or **what you would change in Production V2**.

**What not to say:** Do not overclaim live AWS state, autonomous behavior, production readiness, tenant isolation, exactly-once billing, HA, or performance benchmarks.

---

# Rapid-Fire Revision

**Q101. What provider handles web search?**  
Tavily.

**Q102. What provider handles image generation?**  
Stability AI.

**Q103. What model handles image analysis?**  
Gemini `gemini-2.0-flash`.

**Q104. What model creates PDF embeddings?**  
Gemini `gemini-embedding-001`.

**Q105. What provider/model handles coding?**  
DeepSeek `deepseek/deepseek-chat` through OpenRouter.

**Q106. What is the configured Groq model?**  
`openai/gpt-oss-120b` through the Groq client.

**Q107. Does the `openai/` prefix mean OpenAI API?**  
No.

**Q108. What is the payment provider?**  
Razorpay.

**Q109. Is Stripe used?**  
No.

**Q110. Is AWS API Gateway used?**  
No.

**Q111. Are the eight specialists separate ECS services?**  
No.

**Q112. Is LangGraph checkpointing implemented?**  
No.

**Q113. Is OCR implemented for scanned PDFs?**  
No.

**Q114. Is reranking implemented in PDF RAG?**  
No.

**Q115. Are page citations mature?**  
No.

**Q116. How many chunks are retrieved?**  
Top five.

**Q117. What is the approximate chunk size?**  
1000 characters.

**Q118. What is the approximate chunk overlap?**  
200 characters.

**Q119. Is generated code automatically tested?**  
No.

**Q120. Are generated artifacts stored in S3?**  
PDF/PPT/image artifacts are.

**Q121. Does presigned URL expiry delete the object?**  
No.

**Q122. Does Redis replace MongoDB?**  
No.

**Q123. Does Qdrant equal RAG?**  
No.

**Q124. Does Cloud Map equal service authentication?**  
No.

**Q125. Does CORS equal authorization?**  
No.

**Q126. Is current live AWS health verified?**  
No.

**Q127. Are task-definition CPU/memory values benchmarks?**  
No.

**Q128. Is GitHub OIDC verified as current?**  
No; it is a recommendation.

**Q129. Are immutable release tags used?**  
Not in the current mature form; `latest` is used.

**Q130. Are smoke tests a strong current release gate?**  
No.

**Q131. Is automatic rollback mature?**  
No.

**Q132. Is the system token-streaming?**  
Not in the verified request path.

**Q133. Is the system fully autonomous?**  
No.

**Q134. Is the project production-ready?**  
No; production-oriented is the accurate description.

**Q135. What is the key Search distinction?**  
Tavily retrieves; the LLM synthesizes.

**Q136. What is the key RAG distinction?**  
Retrieval + augmentation + generation.

**Q137. What is the key image distinction?**  
Stability generates images; Gemini analyzes uploaded images.

**Q138. What is the key state distinction?**  
MongoDB = durable history, Redis = fast shared state, LangGraph = current workflow state.

**Q139. What is the key security distinction?**  
Authentication identifies the user; authorization controls access.

**Q140. What is the key deployment distinction?**  
A successful pipeline run does not prove runtime health.

# Whiteboard Interview Script

Draw in this order:

```text
User / Browser
 ↓
CloudFront + S3
 ↓
React
 ↓
ALB (documented)
 ↓
Express Gateway
 ↓
Auth / Chat / Agent / Billing
 ↓
LangGraph inside Agent
 ↓
8 Specialist Workflows
 ↓
Providers / Tools
 ↓
MongoDB / Redis / Qdrant / S3
```

Then add ECS/Fargate, ECR, Secrets Manager, CloudWatch, Cloud Map and the deployment path.

---

# 30-Second Architecture Answer

> NovaMind has a React frontend and five Node.js/Express backend services: Gateway, Auth, Chat, Agent and Billing. The Agent service contains LangGraph and routes AI requests to eight predefined specialist workflows. MongoDB stores durable application data, Redis supports sessions and temporary context, Qdrant provides vector retrieval for PDF RAG, and S3 stores generated artifacts. The backend is containerized for ECS/Fargate, with ECR for images, Secrets Manager for runtime secrets and CloudWatch for logs.

---

# 60–90 Second Architecture Answer

> NovaMind is a full-stack Generative AI platform. The frontend is built with React and Redux and is delivered through S3 and CloudFront. Backend requests enter through an Express Gateway and are routed to Auth, Chat, Agent or Billing. Auth handles login and sessions, Chat handles conversation persistence, Agent handles AI orchestration and Billing handles Razorpay payments.
>
> Inside Agent, LangGraph carries workflow state and routes requests to eight predefined specialist workflows. General chat uses a Groq-backed model path, Search uses Tavily followed by LLM synthesis, Coding uses DeepSeek through OpenRouter, PDF RAG uses PDF extraction, Gemini embeddings, Qdrant retrieval and Groq generation, Image Generation uses Stability AI, and Image Analysis uses Gemini.
>
> MongoDB stores durable application data, Redis supports sessions and temporary context, Qdrant stores vectors, and S3 stores generated artifacts. The repository also includes ECS/Fargate deployment configuration, ECR, Secrets Manager references and CloudWatch logging. I separate that repository-defined architecture from current live AWS state, which needs direct verification.

---

# 2–3 Minute End-to-End Answer

> The user loads the React frontend through the S3 and CloudFront frontend path. During login, Firebase verifies the Google identity and Auth creates NovaMind's own Redis-backed application session using an HTTP-only cookie.
>
> When the user sends an AI request, it reaches the Express Gateway through the backend entry path. The Gateway resolves the session from Redis, derives the authenticated user identity and forwards the request to Agent. Agent coordinates persistence of the user message through Chat and then starts the LangGraph workflow.
>
> LangGraph selects one of the predefined specialist workflows. Chat uses the Groq-backed model path. Search uses Tavily and then LLM synthesis. PDF RAG parses and chunks the document, creates Gemini embeddings, uses Qdrant for similarity retrieval and passes the retrieved context to the language model. Coding uses DeepSeek through OpenRouter. PDF and PPT generation use structured LLM content followed by PDFKit or PptxGenJS and S3 artifact storage. Image generation uses Stability AI, while uploaded-image analysis uses Gemini.
>
> After processing, the assistant response is persisted through Chat. Generated files are stored in S3 and exposed through temporary presigned URLs. The response returns through the Gateway to React. I describe the project as production-oriented rather than production-ready because authorization, payment consistency, testing, observability, release verification, durable lifecycle handling and validated high availability still need hardening.

---

# Final Defense Rules

Always distinguish:

```text
Express Gateway ≠ AWS API Gateway
ALB ≠ Express Gateway
ECS ≠ Fargate
ECR ≠ ECS
LangGraph ≠ LLM
Router ≠ Specialist
MongoDB ≠ Redis
Redis ≠ Qdrant
Qdrant ≠ RAG
PDF RAG ≠ PDF Generation
Image Analysis ≠ Image Generation
Firebase ID Token ≠ NovaMind Session
Automated deployment ≠ mature CI/CD
Production-oriented ≠ production-ready
```

Never claim:

- Bedrock inference is active.
- all eight specialists are separate ECS services.
- autonomous planning/reflection is implemented.
- RAG guarantees correctness.
- generated code is fully executed/tested/repaired.
- payment/credits are exactly-once.
- tenant isolation is fully hardened.
- HA/zero downtime is proven.
- current AWS health is verified from repository evidence.
- capacity/latency has been benchmarked.

---

# Self-Test Checklist

Before moving to Module 03, you should be able to explain without notes:

- all five backend services
- all eight workflows
- login/session flow
- normal chat flow
- Search flow
- PDF RAG flow
- Coding flow
- PDF/PPT generation
- image workflows
- payment and credit flow
- MongoDB vs Redis vs Qdrant vs S3
- AWS runtime path
- deployment path
- three coupling points
- three partial-failure scenarios
- authentication vs authorization
- why LangGraph is used
- why the project is production-oriented rather than production-ready

**Module 02 interview preparation complete.**
