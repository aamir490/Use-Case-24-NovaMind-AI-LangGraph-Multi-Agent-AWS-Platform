# Module 03 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Node, Express, APIs and Microservices  
> **Purpose:** Practice explaining and defending the backend architecture without overclaiming implementation maturity.

---

## How to Practice

For each question:

1. Read the question.
2. Understand what the interviewer is testing.
3. Say the answer without reading.
4. Add one project example.
5. Be ready for a follow-up about failure, trade-off, security, or alternative design.

---

# Foundations

## Q1. What is Node.js?

**Word-for-word answer:**

> Node.js is the JavaScript runtime used to execute NovaMind's backend code outside the browser. It provides the runtime environment for the Express services, database clients, API calls and backend business logic.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q2. What is Express?

**Word-for-word answer:**

> Express is the web framework running on Node.js that defines NovaMind's HTTP APIs, middleware, routes and request/response behavior.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q3. What is the difference between Node.js and Express?

**Word-for-word answer:**

> Node.js is the runtime. Express is the web framework that runs on top of Node.js.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q4. Is the NovaMind backend written in TypeScript?

**Word-for-word answer:**

> No. The verified backend is JavaScript using ES modules.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q5. What is an API?

**Word-for-word answer:**

> An API is a defined communication contract between software components. In NovaMind, React calls backend APIs and backend services also call each other through APIs.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q6. What is an endpoint?

**Word-for-word answer:**

> An endpoint is a specific API method and path, such as POST /api/agent/chat.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q7. What is middleware?

**Word-for-word answer:**

> Middleware is code that runs during the request lifecycle before or around the final route handler, for example authentication, logging, CORS or file upload handling.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q8. What is a router in Express?

**Word-for-word answer:**

> A router groups related endpoints inside an Express service. A router is not a separate microservice.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Service Architecture

## Q9. How many backend services does NovaMind have?

**Word-for-word answer:**

> Five: Gateway, Auth, Chat, Agent and Billing.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q10. What is the Gateway service responsible for?

**Word-for-word answer:**

> It is the main backend entry point. It resolves protected Redis-backed sessions, derives authenticated identity and proxies requests to the correct downstream service.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q11. What is the Auth service responsible for?

**Word-for-word answer:**

> Firebase token verification, user/account handling, Redis-backed session creation, and current account state such as credits and plan.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q12. What is the Chat service responsible for?

**Word-for-word answer:**

> Conversation and message persistence in MongoDB.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q13. What is the Agent service responsible for?

**Word-for-word answer:**

> LangGraph orchestration, workflow routing, AI provider integration, PDF RAG, code generation, document generation and image workflows.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q14. What is the Billing service responsible for?

**Word-for-word answer:**

> Razorpay order creation, payment record handling, signature verification and coordination of credit/plan updates.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q15. Why are the eight AI specialists not microservices?

**Word-for-word answer:**

> Because they are workflows/functions inside the Agent service rather than independently deployed processes with their own ports and runtime boundaries.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q16. Why is it fair to call the backend microservice-style?

**Word-for-word answer:**

> Because the project has separately running Express services with separate ports, Dockerfiles and ECS task definitions. However, independence is incomplete because several services depend synchronously on each other.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q17. What is the biggest difference between a service and a router?

**Word-for-word answer:**

> A service is a separately running application/process. A router is only a code-organization mechanism inside one Express application.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# HTTP and APIs

## Q18. What is the role of GET?

**Word-for-word answer:**

> GET is generally used to retrieve data without creating a new resource.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q19. What is the role of POST?

**Word-for-word answer:**

> POST is generally used to submit data, create a resource or trigger an operation.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q20. What is the role of PATCH or PUT?

**Word-for-word answer:**

> They are generally used to update an existing resource.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q21. What is the role of DELETE?

**Word-for-word answer:**

> DELETE is generally used to remove a resource.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q22. What does HTTP 200 mean?

**Word-for-word answer:**

> The request was successfully processed.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q23. What does 400 mean?

**Word-for-word answer:**

> The client sent invalid or malformed input.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q24. What does 401 mean?

**Word-for-word answer:**

> Authentication is missing or invalid.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q25. What does 403 mean?

**Word-for-word answer:**

> The user is authenticated but does not have permission for the operation.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q26. What does 404 mean?

**Word-for-word answer:**

> The requested resource was not found.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q27. What does 409 mean?

**Word-for-word answer:**

> There is a conflict, for example a duplicate or idempotency-related state conflict.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q28. What does 429 mean?

**Word-for-word answer:**

> The caller exceeded a rate limit.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q29. What does 500 mean?

**Word-for-word answer:**

> The server encountered an unexpected internal error.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q30. Why are HTTP status codes important?

**Word-for-word answer:**

> They make API behavior machine-readable and allow frontend, monitoring and retry logic to distinguish success from different types of failure.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q31. What is wrong with returning provider failures as normal assistant text?

**Word-for-word answer:**

> The API may look successful even though the underlying operation failed, which makes monitoring, retry logic and user experience ambiguous.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Gateway and Identity

## Q32. Why does NovaMind use a Gateway?

**Word-for-word answer:**

> It gives the frontend a single backend entry point and centralizes session resolution, identity propagation and request proxying.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q33. Is the Express Gateway AWS API Gateway?

**Word-for-word answer:**

> No. It is a custom Express service. AWS API Gateway is not used in the verified implementation.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q34. How does a protected request reach a downstream service?

**Word-for-word answer:**

> The browser sends the session cookie to the Gateway, the Gateway looks up the Redis session, derives the authenticated user identity and forwards the request to the required downstream service.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q35. Why should the backend not trust a userId sent by the browser?

**Word-for-word answer:**

> Because the browser is untrusted and a user can modify request data. Identity should come from the authenticated server-side session.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q36. What is identity propagation?

**Word-for-word answer:**

> It is the process of carrying the authenticated user's identity from the Gateway to downstream services, for example through a trusted internal header.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q37. What is the risk of x-user-id style headers?

**Word-for-word answer:**

> A downstream service must be sure the header came from the trusted Gateway and cannot be forged by an external client.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q38. Does private networking solve identity trust?

**Word-for-word answer:**

> No. Private networking reduces exposure but does not itself authenticate or authorize service calls.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q39. What is the Gateway trade-off?

**Word-for-word answer:**

> It simplifies client routing and centralizes common concerns, but it also becomes a critical dependency and potential bottleneck.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Service-to-Service Communication

## Q40. Which important service-to-service calls exist?

**Word-for-word answer:**

> Agent calls Chat for message persistence, Agent calls Auth for credit-related operations, and Billing calls Auth for credit/plan updates.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q41. Why does Agent call Chat instead of writing messages directly?

**Word-for-word answer:**

> It preserves a clearer responsibility boundary where Chat owns conversation persistence, although it introduces a synchronous network dependency.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q42. What happens if Chat is down while Agent is healthy?

**Word-for-word answer:**

> The AI workflow may still be able to generate, but persistence can fail and the overall request may fail or become partially successful.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q43. Why does Billing call Auth?

**Word-for-word answer:**

> Because Auth currently owns user/account state such as credits and plan, so Billing verifies the payment and then asks Auth to update that account state.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q44. What is the downside of synchronous service-to-service calls?

**Word-for-word answer:**

> They add network latency, dependency coupling, timeout risk, retry complexity and partial-failure scenarios.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q45. When would async communication be better?

**Word-for-word answer:**

> For long-running or retryable work where the caller should not block, or where durable delivery is more important than immediate synchronous completion.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q46. Is an async queue currently implemented?

**Word-for-word answer:**

> No. Queue/worker processing is a Production V2 idea, not a verified current feature.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Middleware and Uploads

## Q47. What does Morgan do?

**Word-for-word answer:**

> Morgan is used for HTTP request logging.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q48. What does Multer do?

**Word-for-word answer:**

> Multer processes multipart/form-data uploads such as uploaded PDFs and images.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q49. Why is multipart/form-data needed?

**Word-for-word answer:**

> Because a request may include both text fields such as prompt/conversation ID and an uploaded file.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q50. What file types use upload handling in NovaMind?

**Word-for-word answer:**

> Uploaded PDFs for PDF RAG and uploaded images for image analysis.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q51. Is checking MIME type enough to secure file uploads?

**Word-for-word answer:**

> No. MIME metadata can be misleading. Stronger validation should also inspect file signature, size, allowed extensions, parser safety and potentially malware.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q52. Why is temporary-file cleanup important?

**Word-for-word answer:**

> Otherwise abandoned uploads can accumulate on disk, consume space and potentially expose sensitive data.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q53. Can cleanup itself fail?

**Word-for-word answer:**

> Yes. Error paths can skip or mishandle cleanup, which is why finally-style cleanup and monitoring matter.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# MongoDB and Mongoose

## Q54. What does Mongoose do?

**Word-for-word answer:**

> Mongoose is the Node.js object-modeling library used to interact with MongoDB.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q55. What major models exist in NovaMind?

**Word-for-word answer:**

> User, Conversation, Message and Payment.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q56. What does MongoDB store?

**Word-for-word answer:**

> Durable application data such as users, conversations, messages and payments.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q57. Why not use Redis for all persistent data?

**Word-for-word answer:**

> Redis serves fast shared runtime state. MongoDB is used for durable application records and queryable history.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q58. What is a service data-ownership boundary?

**Word-for-word answer:**

> It means a service should ideally own the rules and access path for its domain data rather than allowing other services to reach directly into its storage.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q59. Where is that boundary weak in NovaMind?

**Word-for-word answer:**

> Some Auth admin functionality opens additional database connections to data associated with Chat/Billing, which weakens strict service ownership.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q60. What would improve this?

**Word-for-word answer:**

> Use explicit service APIs or a clearly designed reporting boundary instead of direct cross-service database access.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Redis

## Q61. What is Redis used for?

**Word-for-word answer:**

> Sessions, conversation-related context/cache and rate counters.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q62. Why is Redis appropriate for sessions?

**Word-for-word answer:**

> It is fast and shared across service instances, so any Gateway instance can resolve the same server-side session.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q63. What happens if Redis is unavailable?

**Word-for-word answer:**

> Protected requests may fail because session lookup depends on Redis, and context/rate-limit behavior may also degrade.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q64. Why is Redis a critical shared dependency?

**Word-for-word answer:**

> Multiple concerns depend on the same store, so one failure can affect authentication, context and counters.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q65. Is Redis the durable conversation database?

**Word-for-word answer:**

> No. MongoDB is the durable conversation store.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q66. Is Redis LangGraph checkpointing?

**Word-for-word answer:**

> No. Redis application state is separate from LangGraph durable graph checkpoints.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Microservice Design

## Q67. What are the benefits of the five-service split?

**Word-for-word answer:**

> Clearer responsibility boundaries, separate runtime units, potential independent scaling and separation of authentication, persistence, AI orchestration and billing concerns.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q68. What are the costs of the five-service split?

**Word-for-word answer:**

> More network calls, more deployment complexity, more failure modes, distributed debugging and consistency problems.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q69. Would a modular monolith be a valid alternative?

**Word-for-word answer:**

> Yes. For a smaller system, a single backend with clear auth, chat, agent and billing modules could simplify deployment and transactions.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q70. Is microservices always better?

**Word-for-word answer:**

> No. It is valuable only when independent scaling, deployment, ownership, reliability or security needs justify the operational complexity.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q71. Where is NovaMind tightly coupled?

**Word-for-word answer:**

> Agent depends on Chat, Billing depends on Auth, some admin data access crosses service boundaries, and all backend services are rebuilt/redeployed together.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q72. Does separate Dockerization guarantee independent microservices?

**Word-for-word answer:**

> No. Runtime separation helps, but independence also depends on data ownership, deployment, communication patterns and failure isolation.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q73. Why not split all eight AI specialists into services?

**Word-for-word answer:**

> That would add network and operational complexity without a proven need. They should become separate services only if scaling, runtime, security or ownership requirements justify it.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Error Handling and Reliability

## Q74. How should an Express service handle unexpected errors?

**Word-for-word answer:**

> It should capture the error, log useful context, return a consistent structured error response and avoid leaking sensitive implementation details.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q75. What is a dependency error?

**Word-for-word answer:**

> A failure from something the service depends on, such as MongoDB, Redis, Qdrant, S3 or an external AI provider.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q76. Why are timeouts important?

**Word-for-word answer:**

> Without deadlines, slow dependencies can hold Node.js requests open too long and consume server resources.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q77. Why can retries be dangerous?

**Word-for-word answer:**

> The original request may already have produced side effects such as credit deduction, payment processing, message creation or provider cost.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q78. What is idempotency?

**Word-for-word answer:**

> It means retrying the same logical operation does not apply the side effect more than once.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q79. Where is idempotency particularly important?

**Word-for-word answer:**

> Payments, credit updates, artifact jobs and other state-changing operations.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q80. What is partial success?

**Word-for-word answer:**

> Some steps succeed while a later step fails, such as model generation succeeding while database persistence fails.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q81. How should you troubleshoot partial success?

**Word-for-word answer:**

> Identify which stages completed, what state changed, which step failed and whether only the failed step can be safely retried.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Security and API Boundaries

## Q82. What is authentication?

**Word-for-word answer:**

> Proving who the caller is.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q83. What is authorization?

**Word-for-word answer:**

> Checking whether that authenticated caller can perform a specific action.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q84. What is an ownership check?

**Word-for-word answer:**

> Verifying that a user-scoped resource such as a conversation belongs to the authenticated user before reading or modifying it.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q85. Why is CORS not authorization?

**Word-for-word answer:**

> CORS is a browser-origin policy. Non-browser callers are not controlled by CORS, so the backend still needs authentication and authorization.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q86. What is object-level authorization?

**Word-for-word answer:**

> Permission enforcement for a specific resource instance, such as ensuring User A cannot request User B's conversation by changing the conversation ID.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q87. Why are credit and plan mutation APIs sensitive?

**Word-for-word answer:**

> They modify financial/account state and should only be callable through trusted, authorized server-side workflows.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q88. What does service-to-service authentication mean?

**Word-for-word answer:**

> A downstream service verifies that an internal call came from an authorized service rather than simply trusting network location or headers.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q89. Is strong service identity verified in the current project?

**Word-for-word answer:**

> No. Internal HTTP trust is an area that needs hardening.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Deployment Boundaries

## Q90. How are backend services packaged?

**Word-for-word answer:**

> Each service has its own Docker image/runtime definition.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q91. Where are images stored?

**Word-for-word answer:**

> In Amazon ECR.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q92. Where do the containers run?

**Word-for-word answer:**

> The repository includes ECS Fargate task definitions for the five backend services.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q93. Does the deployment pipeline redeploy services independently?

**Word-for-word answer:**

> Not fully. The current workflow rebuilds and redeploys all five backend services together.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q94. Why does that matter?

**Word-for-word answer:**

> A small change in one service can trigger unnecessary rebuild/redeployment of other services, reducing deployment independence.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q95. What is the relationship between local ports and ECS services?

**Word-for-word answer:**

> Locally the services listen on ports 8000 through 8004. In ECS they remain separate containerized services with their own task definitions and networking.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Troubleshooting

## Q96. How do you troubleshoot an API request that returns 500?

**Word-for-word answer:**

> Trace the request from frontend to Gateway, authentication/session, downstream route, business logic, database/provider call and response generation, using logs and a correlation ID where available.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q97. How do you troubleshoot login failure?

**Word-for-word answer:**

> Verify Firebase token creation, Auth receipt, Firebase verification, MongoDB user lookup/create, Redis connectivity, session write, cookie response and whether the browser sends the cookie later.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q98. How do you troubleshoot /api/agent/chat failure?

**Word-for-word answer:**

> Check the frontend payload, Gateway route, Redis session, proxy target, Agent logs, upload parsing, LangGraph route, provider call, Chat persistence and returned response.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q99. How do you troubleshoot service-to-service connection failure?

**Word-for-word answer:**

> Verify service name/address, port, DNS/service discovery, security groups/network path, target service health and application logs.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q100. How do you know whether the bug is in Gateway or downstream service?

**Word-for-word answer:**

> Call or inspect the downstream service path directly in the controlled environment and compare logs. If Gateway receives and proxies correctly but downstream rejects/fails, the problem is downstream.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q101. What should you log for distributed troubleshooting?

**Word-for-word answer:**

> Request/correlation ID, route, service, user-safe identifiers, duration, dependency stage, status and sanitized error details.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Design Defense

## Q102. Why use Express instead of a heavier framework?

**Word-for-word answer:**

> Express is simple, widely understood and gives direct control over routing and middleware. The trade-off is that the team must define more conventions for validation, errors, structure and dependency management.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q103. Why use Node.js for an AI orchestration backend?

**Word-for-word answer:**

> The workload is largely I/O-heavy: HTTP APIs, database calls, Redis and external AI providers. Node.js handles asynchronous I/O well and keeps one language across frontend and backend, though CPU-heavy work may need different execution strategies.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q104. Would Node.js be ideal for heavy CPU processing?

**Word-for-word answer:**

> Not necessarily. CPU-intensive work can block the event loop and may be better moved to worker processes or another runtime depending on workload.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q105. Why use a Gateway rather than exposing every service?

**Word-for-word answer:**

> It centralizes the public backend entry point, session checking and service routing, reducing client knowledge of internal services.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q106. Why not let Agent write directly to MongoDB?

**Word-for-word answer:**

> Using Chat preserves a service boundary for conversation persistence, but the trade-off is another synchronous call. Whether that boundary is worth it depends on scale, ownership and reliability needs.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q107. What would you change first in the backend architecture?

**Word-for-word answer:**

> I would first harden authorization and account-mutation APIs, standardize structured errors, add safe idempotency for state-changing operations, strengthen internal service trust and add integration tests before increasing service count.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Pressure Questions

## Q108. Your project has microservices, so is it automatically scalable?

**Word-for-word answer:**

> No. Microservices create separate runtime boundaries, but real scalability still depends on data stores, provider quotas, state consistency, request patterns and measured bottlenecks.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q109. Your services are separate, so are they loosely coupled?

**Word-for-word answer:**

> Not completely. Agent depends synchronously on Chat, Billing depends on Auth, some data access crosses boundaries and deployment is coordinated across all services.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q110. Why call this microservices if Auth reads other service data?

**Word-for-word answer:**

> The system still has separate runtime services, ports, containers and responsibilities, so microservice-style is accurate. But strict data ownership is incomplete, and I would explicitly describe that as a boundary weakness.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q111. Why not merge everything into one service?

**Word-for-word answer:**

> A single service could simplify development and transactions. The current split provides clearer runtime/domain boundaries, but I would keep only boundaries that are justified by scaling, ownership, security or deployment needs.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q112. What happens if Gateway goes down?

**Word-for-word answer:**

> Because it is the main backend entry point, protected frontend API access is disrupted even if downstream services are still healthy.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q113. What happens if Auth goes down?

**Word-for-word answer:**

> Login/account operations fail, and services that synchronously depend on Auth for credit/account operations can also be affected.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q114. What happens if Chat goes down?

**Word-for-word answer:**

> Conversation/history persistence can fail, and Agent requests that depend on Chat can become partially successful or fail.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q115. What happens if Agent goes down?

**Word-for-word answer:**

> Core AI workflows become unavailable even if Auth, Chat and Billing remain healthy.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q116. What happens if Billing goes down?

**Word-for-word answer:**

> Payment/order flows fail, while non-billing AI/chat features may still work.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

## Q117. Would you call the backend production-ready?

**Word-for-word answer:**

> No. It is production-oriented, but authorization, payment/account consistency, error semantics, automated tests, internal service trust, observability and deployment safety need further hardening.

**Likely follow-up:** The interviewer may ask **why**, **what can fail**, **what the trade-off is**, **how you would troubleshoot it**, or **what you would improve in Production V2**.

**What not to say:** Avoid claiming perfect service independence, production readiness, full authorization, exactly-once operations, or verified live AWS health unless you have direct evidence.

---

# Rapid-Fire Revision

**Q118. Which service listens on port 8000?**  
Gateway.

**Q119. Which service listens on 8001?**  
Auth.

**Q120. Which service listens on 8002?**  
Chat.

**Q121. Which service listens on 8003?**  
Agent.

**Q122. Which service listens on 8004?**  
Billing.

**Q123. What library handles MongoDB?**  
Mongoose.

**Q124. What library handles Redis?**  
ioredis.

**Q125. What middleware handles uploads?**  
Multer.

**Q126. What library logs HTTP requests?**  
Morgan.

**Q127. What library is commonly used for service HTTP calls?**  
Axios.

**Q128. What does Gateway do first on a protected request?**  
Resolve/validate the Redis-backed session and derive the user identity.

**Q129. Where are sessions stored?**  
Redis.

**Q130. Where are conversations/messages stored?**  
MongoDB.

**Q131. Where are AI workflows located?**  
Inside Agent.

**Q132. Are specialists separate microservices?**  
No.

**Q133. Is Express Gateway AWS API Gateway?**  
No.

**Q134. What does 401 mean?**  
Unauthenticated.

**Q135. What does 403 mean?**  
Authenticated but not authorized.

**Q136. What does 429 mean?**  
Rate limit exceeded.

**Q137. What does 500 mean?**  
Unexpected server failure.

**Q138. What is synchronous coupling?**  
One service waits directly for another service to respond before it can continue.

**Q139. Give one synchronous dependency.**  
Agent → Chat.

**Q140. Give another synchronous dependency.**  
Billing → Auth.

**Q141. What is partial success?**  
Earlier stages succeed but a later stage fails.

**Q142. What is idempotency?**  
Repeating the same logical request does not duplicate its side effect.

**Q143. Does CORS provide authorization?**  
No.

**Q144. Does a private VPC authenticate services?**  
No.

**Q145. Does an internal header automatically prove identity?**  
No.

**Q146. What is a modular monolith?**  
One deployable backend with clear internal modules instead of separate network services.

**Q147. Is microservices always better?**  
No.

**Q148. Does separate Dockerization guarantee loose coupling?**  
No.

**Q149. Is the backend TypeScript?**  
No, JavaScript ES modules.

**Q150. What is the best description of maturity?**  
Production-oriented, not production-ready.

# Whiteboard Answer — Module 03

Draw:

```text
User / React
    ↓
Express Gateway :8000
    ↓
 ┌────────┬────────┬────────┐
 ↓        ↓        ↓        ↓
Auth     Chat     Agent    Billing
:8001    :8002    :8003    :8004
 ↓        ↓        ↓        ↓
Redis   MongoDB   AI/DB    Razorpay
```

Then explain the important service-to-service calls:

```text
Agent → Chat
Agent → Auth
Billing → Auth
```

Then explain the trade-off:

> Clearer service responsibilities, but more network dependencies, more partial-failure cases, and more complex distributed consistency.

---

# 30-Second Interview Answer

> NovaMind's backend is built with Node.js and Express and is split into five services: Gateway, Auth, Chat, Agent and Billing. The Gateway is the main backend entry point and handles session resolution and routing. Auth manages login and account state, Chat owns conversation persistence, Agent contains LangGraph and AI workflows, and Billing handles Razorpay payments. The services communicate through HTTP APIs, which gives clear responsibility boundaries but also introduces network coupling and distributed failure scenarios.

---

# 60–90 Second Interview Answer

> The NovaMind backend runs on Node.js with five separate Express services. The Gateway on port 8000 is the public application entry point. It resolves the Redis-backed session, derives authenticated identity and proxies requests to Auth, Chat, Agent or Billing. Auth handles Firebase identity verification, server-side sessions and account state. Chat handles durable conversation/message persistence in MongoDB. Agent contains LangGraph and the AI workflows, and Billing handles Razorpay orders and payment verification.
>
> The services also communicate internally. Agent calls Chat to persist messages and calls Auth for credit-related operations, while Billing calls Auth after payment verification. That separation gives cleaner responsibilities, but it also introduces synchronous dependencies, network latency, partial failures and distributed consistency problems. So I describe the system as microservice-style rather than pretending the services are perfectly independent.

---

# Project-Defense Rules

Always distinguish:

```text
Node.js ≠ Express
Express Router ≠ Microservice
Express Gateway ≠ AWS API Gateway
Authentication ≠ Authorization
Private Network ≠ Service Authentication
Redis ≠ MongoDB
Separate Container ≠ Loose Coupling
Automated Deployment ≠ Production Readiness
```

Do not claim:

- the services are fully independent
- service-to-service authentication is fully hardened
- account/credit operations are fully atomic
- every route has perfect object-level authorization
- current live AWS networking is verified from source alone
- the backend has a mature automated test suite
- the system has proven high availability

---

# Final Self-Test

Before moving to Module 04, you should be able to answer without notes:

- What is Node.js?
- What is Express?
- What is an API?
- What is middleware?
- What is a router?
- What are all five services?
- Why is Gateway used?
- How does identity reach downstream services?
- How does Agent communicate with Chat?
- Why does Billing call Auth?
- What does Multer do?
- What does Mongoose do?
- What does Redis do?
- What are the benefits and costs of microservices?
- What is the modular-monolith alternative?
- What is partial success?
- Why is idempotency important?
- Why are error semantics important?
- What backend security boundaries are currently weak?
- How would you troubleshoot a failing API?
- Why is the project microservice-style but not perfectly decoupled?

**Module 03 interview preparation complete.**
