# Module 22 — Interview Q&A and Project Defense

> **FINAL NOVAMIND INTERVIEW DRILL BOOK**  
> This file is designed for repeated practice under pressure, not passive reading.

---

# Accuracy Contract

Use these facts consistently:

```text
5 backend services
8 specialist workflows inside Agent
bounded LangGraph routing
no autonomous planner
no reflection loop
no unrestricted tool loop
no LangGraph checkpointing
Redis context ≠ checkpointing
no active Bedrock inference verified
Express Gateway ≠ AWS API Gateway
application session = opaque Redis UUID
production-oriented ≠ fully production-ready
```

Never invent:

```text
ownership
incidents
metrics
cost
capacity
uptime
HA
live configuration
```

---

# How to Practice This File

For each question:

1. Hide the model answer.
2. Answer aloud.
3. Compare your answer.
4. Mark RED / YELLOW / GREEN / BLUE.
5. Record one mistake.
6. Repeat only the weak questions the next day.

---
# Mock Interview A — Beginner / Screening

## Q1. Tell me about NovaMind AI.

**Strong natural answer**

> NovaMind AI is a full-stack multi-workflow Generative AI application. React provides the frontend, the backend has five Express services—Gateway, Auth, Chat, Agent and Billing—and Agent uses LangGraph to route requests to eight predefined specialist workflows such as Chat, Search, Coding, PDF RAG and image/document generation.

**Follow-up**

> How is it different from a normal chatbot?

**Strong follow-up answer**

> A normal chatbot usually sends most requests to one conversation model. NovaMind routes different request types into specialized workflows and integrates retrieval, search, coding, document and image capabilities.

**Cross-question**

> How many microservices are there?

**Pressure variation**

> Are you sure the eight specialists are not separate services?

**What the interviewer is testing**

basic project clarity and service boundaries

**Common mistake**

Calling eight specialists eight microservices.

---

## Q2. What problem does the project solve?

**Strong natural answer**

> It gives users one interface for several AI tasks instead of separate tools for chat, current web search, coding, PDF question answering, document generation and image workflows.

**Follow-up**

> Who is the target user?

**Strong follow-up answer**

> A user who wants multiple AI capabilities through one unified application experience.

**Cross-question**

> What is the business differentiator?

**Pressure variation**

> Why not just connect everything to one LLM?

**What the interviewer is testing**

ability to explain problem before technology

**Common mistake**

Starting with a long technology list.

---

## Q3. Explain the high-level architecture.

**Strong natural answer**

> The user interacts with React, requests enter through an Express Gateway, then go to Auth, Chat, Agent or Billing. Agent contains LangGraph and eight specialist workflows. MongoDB, Redis, Qdrant and S3 handle different state/storage needs, while AI/search providers support specialist workflows.

**Follow-up**

> Where is LangGraph?

**Strong follow-up answer**

> Inside the Agent service.

**Cross-question**

> What is Gateway's job?

**Pressure variation**

> Is Gateway AWS API Gateway?

**What the interviewer is testing**

ability to draw the system correctly

**Common mistake**

Saying AWS API Gateway.

---

## Q4. What is LangGraph used for?

**Strong natural answer**

> It coordinates the bounded routing workflow inside Agent. The graph starts at a router, reads the current request state and routes to one of eight predefined specialists.

**Follow-up**

> Is it autonomous?

**Strong follow-up answer**

> No. It has agentic characteristics but no autonomous planner, reflection loop or unrestricted repeated tool loop.

**Cross-question**

> What is graph state?

**Pressure variation**

> Why use LangGraph instead of a switch?

**What the interviewer is testing**

agentic terminology accuracy

**Common mistake**

Calling bounded routing fully autonomous.

---

## Q5. Explain PDF RAG simply.

**Strong natural answer**

> The PDF is parsed, split into chunks, embedded with Gemini, stored in Qdrant, and the user's question is embedded and used to retrieve the top five relevant chunks. Those chunks are passed with the question to Groq to generate the answer.

**Follow-up**

> Does RAG prevent hallucination?

**Strong follow-up answer**

> No. It provides relevant evidence and can improve grounding, but it cannot guarantee correctness.

**Cross-question**

> Does it support scanned PDFs?

**Pressure variation**

> Can the user ask about the same PDF next week without uploading again?

**What the interviewer is testing**

RAG understanding and limitation awareness

**Common mistake**

Claiming persistent knowledge base behavior.

---

## Q6. What do Redis and MongoDB do?

**Strong natural answer**

> Redis handles the application session, fast conversation context and rate counters. MongoDB stores durable users, conversations, messages and payment records.

**Follow-up**

> Is Redis the LangGraph checkpoint?

**Strong follow-up answer**

> No. The graph has no verified LangGraph checkpointer.

**Cross-question**

> What survives an Agent restart?

**Pressure variation**

> If Redis goes down, can login continue safely?

**What the interviewer is testing**

state-layer distinction

**Common mistake**

Calling all state 'memory'.

---

## Q7. How is the backend deployed?

**Strong natural answer**

> The repository has separate Dockerized backend services with ECS/Fargate task definitions and ECR image publishing. The frontend deployment uses S3 and CloudFront. ALB/VPC/Cloud Map networking is substantially documented but current live topology is not fully verified.

**Follow-up**

> What is Fargate?

**Strong follow-up answer**

> Fargate is the serverless compute engine that runs ECS tasks without managing EC2 hosts.

**Cross-question**

> What is ECR?

**Pressure variation**

> Is the application definitely Multi-AZ today?

**What the interviewer is testing**

basic AWS architecture

**Common mistake**

Claiming live HA without evidence.

---

## Q8. Is the project production-ready?

**Strong natural answer**

> I would call it production-oriented rather than fully production-ready. Authorization, payment/credit consistency, automated testing and AI evaluation, observability, document/artifact lifecycle and HA still need hardening.

**Follow-up**

> What would you fix first?

**Strong follow-up answer**

> Authorization and any exposed credentials, followed by payment/credit idempotency and session correctness.

**Cross-question**

> Why security before scale?

**Pressure variation**

> But it's already deployed on AWS, isn't that production-ready?

**What the interviewer is testing**

production judgment

**Common mistake**

Equating deployment with production readiness.

---

# Mock Interview B — Intermediate

## Q9. Walk me through a normal Chat request.

**Strong natural answer**

> React sends the prompt to the Express Gateway. Gateway resolves the opaque Redis session and user identity. Agent receives the request, saves the user message through Chat, initializes LangGraph state, routes to Chat, calls the Groq-backed model, updates fast context in Redis, saves the assistant message and returns the response.

**Follow-up**

> Why does Agent call Chat?

**Strong follow-up answer**

> Chat owns conversation/message persistence while Agent owns AI orchestration. The trade-off is synchronous coupling.

**Cross-question**

> What if Chat is unavailable after the model generated an answer?

**Pressure variation**

> Would retrying the request be safe?

**What the interviewer is testing**

end-to-end request understanding

**Common mistake**

Skipping identity/persistence and saying only 'LLM returns answer'.

---

## Q10. Explain the routing priority.

**Strong natural answer**

> Explicit non-Auto selection wins. In Auto mode, a PDF routes to PDF RAG and an uploaded image routes to Image Analysis. Otherwise a model-based classifier selects a workflow. An unknown label can fall back to Chat.

**Follow-up**

> What happens if the classifier itself throws?

**Strong follow-up answer**

> There is no mature universal fallback for classifier exceptions.

**Cross-question**

> Why deterministic routing before classifier?

**Pressure variation**

> Would you call this an autonomous router?

**What the interviewer is testing**

router behavior precision

**Common mistake**

Inventing robust fallback that is not present.

---

## Q11. Explain Search end to end.

**Strong natural answer**

> The Search specialist calls Tavily for up to five web results and images, then passes the retrieved information into a Groq-backed synthesis step. The answer is persisted like other assistant responses.

**Follow-up**

> Is Search RAG?

**Strong follow-up answer**

> I would call it web retrieval plus LLM synthesis rather than automatically calling it the PDF RAG pipeline.

**Cross-question**

> What if Tavily is slow?

**Pressure variation**

> How do you validate that citations match claims?

**What the interviewer is testing**

retrieval distinction and failure analysis

**Common mistake**

Saying citations/fact checking are verified.

---

## Q12. Explain Coding end to end.

**Strong natural answer**

> A coding request goes through coding intent classification, then DeepSeek through OpenRouter generates structured files. The backend parses the structured output and the frontend displays files in Monaco with a basic browser preview.

**Follow-up**

> Does NovaMind run the code?

**Strong follow-up answer**

> It does not provide unrestricted server-side execution, package install, full compile/test or autonomous repair loops.

**Cross-question**

> What if the model returns malformed JSON?

**Pressure variation**

> Why not execute generated code automatically?

**What the interviewer is testing**

structured-output and security understanding

**Common mistake**

Claiming a full coding sandbox.

---

## Q13. Explain authentication.

**Strong natural answer**

> Google sign-in produces a Firebase ID token. Auth verifies it, finds or creates the MongoDB user, creates an opaque UUID session in Redis with a seven-day TTL and sends it in an HTTP-only cookie. Gateway later resolves the session.

**Follow-up**

> Why not JWT?

**Strong follow-up answer**

> Redis-backed sessions give centralized server state and revocation potential; JWT removes lookup but makes immediate revocation/stale claims more complex.

**Cross-question**

> What does SameSite=None imply?

**Pressure variation**

> Does CORS protect the application from CSRF?

**What the interviewer is testing**

session and security fundamentals

**Common mistake**

Calling the application session JWT.

---

## Q14. Explain the Razorpay flow.

**Strong natural answer**

> Billing creates a Razorpay order and a Payment record. After checkout, the callback signature is verified with HMAC, the payment becomes paid, and Billing calls Auth to update credits and plan.

**Follow-up**

> What is the current consistency issue?

**Strong follow-up answer**

> Payment can be marked paid before the credit update succeeds, so cross-service state can diverge.

**Cross-question**

> How do duplicate callbacks affect it?

**Pressure variation**

> Would a simple retry guarantee correctness?

**What the interviewer is testing**

distributed payment reasoning

**Common mistake**

Treating HMAC verification as idempotency.

---

## Q15. Explain the deployment pipeline.

**Strong natural answer**

> On push to main, GitHub Actions checks out the repository, authenticates to AWS, logs into ECR, builds and pushes five backend images, forces ECS service redeployments, builds the React frontend, syncs it to S3 and invalidates CloudFront.

**Follow-up**

> What is missing?

**Strong follow-up answer**

> Substantive test gates, immutable image versions, explicit task-definition registration, wait-for-stability/smoke gates and automated rollback are not maturely implemented.

**Cross-question**

> What if local task-definition JSON changes?

**Pressure variation**

> Why is latest a weak release tag?

**What the interviewer is testing**

CI/CD accuracy

**Common mistake**

Calling the current pipeline mature zero-downtime CI/CD.

---

## Q16. How would you troubleshoot a request that works locally but fails on ECS?

**Strong natural answer**

> I would first establish whether the failure is at container startup, service discovery, networking, secret/env configuration, external connectivity or application logic. Then I would inspect ECS events and CloudWatch logs, verify task environment/secrets and Cloud Map/DNS, and compare the runtime configuration against local.

**Follow-up**

> What if the task is healthy but provider calls fail?

**Strong follow-up answer**

> I would check outbound networking/NAT, DNS, provider credentials, quota and request errors.

**Cross-question**

> What if MongoDB works but Redis does not?

**Pressure variation**

> Would you restart all services first?

**What the interviewer is testing**

structured troubleshooting

**Common mistake**

Jumping straight to restart without evidence.

---

# Mock Interview C — Advanced GenAI Engineer

## Q17. Why do you call NovaMind agentic?

**Strong natural answer**

> Because it has stateful orchestration, intent-based routing, specialized workflows and tool/provider integration. But I qualify that it is bounded: there is no autonomous planner, reflection loop or unrestricted tool-use cycle.

**Follow-up**

> Is a router enough to call something agentic?

**Strong follow-up answer**

> The label is nuanced. I would describe it as LangGraph-orchestrated specialist workflows with agentic characteristics, not a fully autonomous agent platform.

**Cross-question**

> What would make it more autonomous?

**Pressure variation**

> Would adding loops automatically make it better?

**What the interviewer is testing**

nuanced agentic AI reasoning

**Common mistake**

Equating any LangGraph use with autonomy.

---

## Q18. What exactly is LangGraph state in NovaMind?

**Strong natural answer**

> It carries current execution data such as prompt, response, selected workflow, user/conversation IDs, optional file, search results, images and artifacts between graph nodes.

**Follow-up**

> Is that durable?

**Strong follow-up answer**

> No. No verified LangGraph checkpointer exists.

**Cross-question**

> How is this different from Redis conversation context?

**Pressure variation**

> What happens if Agent dies mid-graph?

**What the interviewer is testing**

state vs persistence

**Common mistake**

Calling Redis graph state persistence.

---

## Q19. Why use multiple model providers?

**Strong natural answer**

> The architecture maps different capabilities to different providers: Groq for general text, Gemini for embeddings/image analysis, DeepSeek through OpenRouter for coding, Stability for image generation and Tavily for search.

**Follow-up**

> What is the downside?

**Strong follow-up answer**

> More credentials, quotas, latency profiles, response formats, cost tracking and reliability dependencies.

**Cross-question**

> Does this provide failover?

**Pressure variation**

> How would you build controlled fallback?

**What the interviewer is testing**

provider architecture judgment

**Common mistake**

Saying multiple providers automatically provide resilience.

---

## Q20. How would you evaluate the router?

**Strong natural answer**

> I would create a labeled evaluation set covering clear and ambiguous intents, explicit selections, file-based routing, unknown labels and classifier failure cases. Then measure accuracy by class and review costly misroutes separately.

**Follow-up**

> What should be deterministic vs model-based?

**Strong follow-up answer**

> Explicit selections and file-type rules should remain deterministic; model classification is most useful when intent cannot be determined cheaply from request metadata.

**Cross-question**

> What if classifier accuracy is 92%?

**Pressure variation**

> Which errors matter most?

**What the interviewer is testing**

AI routing evaluation

**Common mistake**

Only quoting aggregate accuracy.

---

## Q21. How would you evaluate PDF RAG?

**Strong natural answer**

> I would separate retrieval from generation. Retrieval evaluation would test whether relevant evidence appears in top K using metrics such as hit rate, Recall@K, Precision@K or MRR where appropriate. Generation evaluation would measure groundedness, relevance, completeness and abstention behavior using a curated question/evidence set.

**Follow-up**

> Would you use only LLM-as-judge?

**Strong follow-up answer**

> No. I would combine deterministic checks, human-reviewed examples and judge models where useful, because judge models can also be biased or inconsistent.

**Cross-question**

> What if retrieval is good but answers are wrong?

**Pressure variation**

> What if answers sound good but retrieval is poor?

**What the interviewer is testing**

AI evaluation maturity

**Common mistake**

Treating one score as complete RAG quality.

---

## Q22. What are the main RAG weaknesses?

**Strong natural answer**

> No OCR for scanned PDFs, character-based chunks, request-oriented indexing, no durable user/document-to-index mapping, no mature page citations, reranking, threshold/no-answer policy, cleanup lifecycle or RAG evaluation.

**Follow-up**

> Which would you fix first?

**Strong follow-up answer**

> Persistent document identity/ownership and evaluation come before adding advanced retrieval tricks.

**Cross-question**

> Why not add hybrid search immediately?

**Pressure variation**

> Would larger chunks solve everything?

**What the interviewer is testing**

RAG trade-off awareness

**Common mistake**

Jumping to fashionable retrieval techniques without evaluation.

---

## Q23. How would you defend prompt injection?

**Strong natural answer**

> I would treat user, PDF and web content as untrusted data, keep system/tool authority separate, constrain tools by server-side authorization, validate outputs and include adversarial prompt-injection cases in evaluation.

**Follow-up**

> Can prompt text alone be dangerous?

**Strong follow-up answer**

> Yes, if the model is allowed to interpret untrusted data as privileged instructions or trigger powerful tools.

**Cross-question**

> Does RAG make injection safer?

**Pressure variation**

> What is the current project status?

**What the interviewer is testing**

LLM security reasoning

**Common mistake**

Claiming mature prompt-injection defense is current.

---

## Q24. Why no checkpointing?

**Strong natural answer**

> The current workflows are mostly bounded request-response flows, so durable graph checkpointing was not implemented. If V2 introduced long-running/resumable workflows or human approval, checkpointing would become much more valuable.

**Follow-up**

> Would Redis be enough?

**Strong follow-up answer**

> No. Redis application context is not the same as LangGraph execution checkpointing.

**Cross-question**

> When exactly would you introduce checkpointing?

**Pressure variation**

> Would every short chat request need it?

**What the interviewer is testing**

workflow design reasoning

**Common mistake**

Using checkpointing because it is fashionable.

---

# Mock Interview D — AWS / Production Engineering

## Q25. Explain ECS vs Fargate.

**Strong natural answer**

> ECS is the container orchestration service; Fargate is the serverless compute option that runs ECS tasks without managing EC2 hosts.

**Follow-up**

> What is an ECS task definition?

**Strong follow-up answer**

> The runtime specification for containers, including image, ports, CPU/memory, environment/secrets, roles and logging.

**Cross-question**

> Task vs service?

**Pressure variation**

> Why does Agent have more CPU/memory configured?

**What the interviewer is testing**

AWS container fundamentals

**Common mistake**

Calling Fargate the orchestrator.

---

## Q26. What is the execution role vs task role?

**Strong natural answer**

> The execution role is used by ECS for platform/startup operations such as pulling images, fetching secret references and writing logs. The task role is assumed by application code for AWS API calls.

**Follow-up**

> Which should allow S3 PutObject?

**Strong follow-up answer**

> If the application uploads artifacts to S3, that belongs in the application task role, scoped to required resources.

**Cross-question**

> Is least privilege verified today?

**Pressure variation**

> Would you use one shared role for all services?

**What the interviewer is testing**

IAM clarity

**Common mistake**

Mixing execution and application permissions.

---

## Q27. Explain ALB, Cloud Map and Express Gateway.

**Strong natural answer**

> ALB is the AWS load balancer at the network/application entry layer in the documented architecture. Express Gateway is the application-level backend gateway service. Cloud Map is internal DNS/service discovery for services.

**Follow-up**

> Does Cloud Map secure service-to-service traffic?

**Strong follow-up answer**

> No. Discovery is not authentication.

**Cross-question**

> Could you remove the Express Gateway and route directly from ALB?

**Pressure variation**

> Why not use AWS API Gateway?

**What the interviewer is testing**

network-layer distinctions

**Common mistake**

Conflating the three.

---

## Q28. How would private ECS tasks call Groq/Gemini/Tavily?

**Strong natural answer**

> If tasks are in private subnets without public IPs, they need an outbound path such as NAT for public internet providers. The exact live topology is not fully verified, so I would confirm the VPC route tables/subnets/NAT configuration.

**Follow-up**

> What is the cost implication?

**Strong follow-up answer**

> NAT can add baseline and data-processing cost.

**Cross-question**

> Can you assert a NAT gateway is live today?

**Pressure variation**

> Could VPC endpoints replace NAT for all providers?

**What the interviewer is testing**

network realism

**Common mistake**

Inventing live network state.

---

## Q29. How would you make Redis highly available?

**Strong natural answer**

> Production V2 would evaluate replication, Multi-AZ and automatic failover, then test failover behavior because Redis affects sessions, context and rate limiting.

**Follow-up**

> Is Redis HA now?

**Strong follow-up answer**

> A captured configuration showed a single nonredundant node with failover disabled; I would not claim that is the live current state without verification.

**Cross-question**

> What happens during failover?

**Pressure variation**

> Should auth fail open or closed?

**What the interviewer is testing**

stateful HA reasoning

**Common mistake**

Claiming current failover.

---

## Q30. How would you autoscale Agent?

**Strong natural answer**

> First load-test representative workflows and measure concurrency, p95/p99, CPU/memory and provider latency/quotas. Then choose a scaling signal such as ALB requests per target, active requests or queue depth if async jobs are introduced. CPU alone may be weak because AI calls are network-bound.

**Follow-up**

> Why not CPU target tracking only?

**Strong follow-up answer**

> Low CPU can coexist with high concurrency while requests wait on providers.

**Cross-question**

> What is the current autoscaling policy?

**Pressure variation**

> How many tasks are required?

**What the interviewer is testing**

measurement-driven scaling

**Common mistake**

Inventing capacity.

---

## Q31. How would you harden CI/CD?

**Strong natural answer**

> Use immutable Git-SHA image tags, automated tests/evals and image scanning before deploy, register explicit task-definition revisions, wait for service stability, run smoke tests, provide rollback, and use OIDC/least-privilege deployment identity.

**Follow-up**

> Is OIDC current?

**Strong follow-up answer**

> No, it is a Production V2 recommendation.

**Cross-question**

> Why not latest?

**Pressure variation**

> How do you roll back an immutable release?

**What the interviewer is testing**

release safety

**Common mistake**

Presenting V2 as current.

---

## Q32. What would you monitor?

**Strong natural answer**

> Per-service request/error rates, workflow latency and p95/p99, provider latency/429s, Redis/Mongo/Qdrant latency, ECS CPU/memory/restarts, payment consistency signals, RAG quality metrics and deployment health.

**Follow-up**

> Is this dashboard implemented today?

**Strong follow-up answer**

> No mature metrics/tracing/AI-quality dashboard is verified; current evidence is primarily CloudWatch logs.

**Cross-question**

> What are correlation IDs for?

**Pressure variation**

> Why are logs alone insufficient?

**What the interviewer is testing**

observability maturity

**Common mistake**

Claiming mature tracing.

---

# Mock Interview E — Senior Architecture Pressure Round

## Q33. Why five services for this project?

**Strong natural answer**

> The split creates separate responsibilities for entry, identity/account, conversation persistence, AI orchestration and billing. The trade-off is synchronous coupling and distributed operational complexity. A modular monolith could be a valid simpler design for a smaller team.

**Follow-up**

> So was microservices the wrong choice?

**Strong follow-up answer**

> Not necessarily. The right answer depends on independent scaling, ownership, deployment and reliability needs. The current project demonstrates those boundaries but does not have perfect service independence.

**Cross-question**

> What evidence shows service coupling?

**Pressure variation**

> Would you merge any services in V2?

**What the interviewer is testing**

architecture maturity

**Common mistake**

Defending microservices as inherently superior.

---

## Q34. Why LangGraph rather than normal JavaScript?

**Strong natural answer**

> LangGraph makes state, graph boundaries and conditional transitions explicit. The trade-off is framework overhead for a currently bounded router. If the graph stayed simple, plain JavaScript routing would be a legitimate alternative.

**Follow-up**

> Then why use LangGraph at all?

**Strong follow-up answer**

> It provides a structured orchestration model and room for more stateful workflows; the decision should be revisited if complexity does not justify it.

**Cross-question**

> What would force you to remove it?

**Pressure variation**

> What would justify more graph features?

**What the interviewer is testing**

framework trade-off reasoning

**Common mistake**

Saying LangGraph is required.

---

## Q35. Why MongoDB and not PostgreSQL?

**Strong natural answer**

> MongoDB fits flexible user/conversation/message/payment document models and integrates naturally with Mongoose. A relational database could provide stronger relational constraints and transaction patterns. I would choose based on query/consistency requirements rather than claiming MongoDB is universally better.

**Follow-up**

> Would PostgreSQL improve payments?

**Strong follow-up answer**

> A relational transactional ledger can be attractive for financial consistency, but distributed consistency with Billing/Auth still requires careful boundaries and idempotency.

**Cross-question**

> What current query problems exist?

**Pressure variation**

> Would you migrate the whole application?

**What the interviewer is testing**

data-store trade-offs

**Common mistake**

Technology tribalism.

---

## Q36. Why Qdrant instead of pgvector?

**Strong natural answer**

> Qdrant is a dedicated vector database and fits semantic retrieval. pgvector could simplify the stack by putting vectors with relational/application data. I would compare scale, filtering, operational ownership and team complexity before choosing.

**Follow-up**

> Which is better?

**Strong follow-up answer**

> There is no universal winner; requirements decide.

**Cross-question**

> Would you keep Qdrant if MongoDB vector search were available?

**Pressure variation**

> Why is current collection design weak?

**What the interviewer is testing**

vector architecture trade-offs

**Common mistake**

Declaring a winner without requirements.

---

## Q37. Why Fargate instead of Lambda?

**Strong natural answer**

> The backend consists of long-lived Express services and some potentially long-running/file-processing AI workflows, which fit containers. Lambda could fit short stateless event handlers but introduces runtime/time/package constraints. I would use it selectively where workload shape fits.

**Follow-up**

> Could Billing be Lambda?

**Strong follow-up answer**

> Potentially, if the workflow were refactored around stateless/event-driven operations; the current architecture is service-oriented.

**Cross-question**

> What about cold starts?

**Pressure variation**

> Is Fargate cheaper?

**What the interviewer is testing**

compute trade-offs

**Common mistake**

Claiming Fargate is always cheaper.

---

## Q38. Why no queue?

**Strong natural answer**

> The current user flows are primarily synchronous, which simplifies interaction but holds connections during long provider/file work. A queue becomes useful for large document ingestion or artifact generation when durability, burst absorption and retry isolation matter.

**Follow-up**

> Why not add SQS immediately?

**Strong follow-up answer**

> Because asynchronous infrastructure adds job state, duplicate handling and operational complexity. I would add it where measurements/user experience justify it.

**Cross-question**

> Which workflows would you move first?

**Pressure variation**

> How would users get results?

**What the interviewer is testing**

sync/async design judgment

**Common mistake**

Adding infrastructure without requirement.

---

## Q39. What is the biggest architectural risk?

**Strong natural answer**

> Authorization and money correctness are higher priority than performance. Resource ownership gaps, sensitive account mutation and payment/credit consistency can create security or financial impact, so I would fix those before scaling.

**Follow-up**

> Not Redis?

**Strong follow-up answer**

> Redis availability matters, but an authorization or accounting bug can create incorrect access or money state even when the system is fully available.

**Cross-question**

> Why not performance first?

**Pressure variation**

> How would you prioritize V2?

**What the interviewer is testing**

risk prioritization

**Common mistake**

Prioritizing fashionable scale work over correctness.

---

## Q40. Would you approve this architecture for production?

**Strong natural answer**

> Not as-is. I would approve it as a strong production-oriented prototype/portfolio implementation, but production approval would require authorization hardening, financial idempotency, tests/evals, structured observability, safer releases, persistent data lifecycle and verified HA/recovery.

**Follow-up**

> What minimum gates would you require?

**Strong follow-up answer**

> Security regression tests, payment idempotency/reconciliation, health/readiness, release verification, backups and key SLO/alerting baselines.

**Cross-question**

> How would you prove readiness?

**Pressure variation**

> What would you postpone?

**What the interviewer is testing**

production architecture judgment

**Common mistake**

Binary 'yes' without conditions.

---

# Mock Interview F — Resume Defense

## Q41. Which parts did you personally implement?

**Strong natural answer**

> I would list only my confirmed ownership: [FILL CONFIRMED COMPONENTS]. I can explain the exact files/functions, design decisions, debugging and verification for those parts. I understand the surrounding architecture, but I do not claim ownership of everything simply because it is in the repository.

**Follow-up**

> Which file should I open?

**Strong follow-up answer**

> For each claimed component I should provide a real file/module path that I personally worked on: [FILL].

**Cross-question**

> What code did AI tools generate?

**Pressure variation**

> What did a teammate or mentor contribute?

**What the interviewer is testing**

ownership integrity

**Common mistake**

Claiming the entire repository.

---

## Q42. Did you design the architecture?

**Strong natural answer**

> I would only claim architecture ownership if I personally made and can defend those decisions. Otherwise I would say I understand and can explain the architecture, and my confirmed contribution was [FILL].

**Follow-up**

> Who decided to use LangGraph?

**Strong follow-up answer**

> That historical decision must be answered from my actual experience, not inferred from the repository.

**Cross-question**

> What design decision was personally yours?

**Pressure variation**

> What alternative did you personally evaluate?

**What the interviewer is testing**

historical ownership honesty

**Common mistake**

Turning engineering reasoning into fabricated history.

---

## Q43. What was the hardest issue you personally solved?

**Strong natural answer**

> PERSONAL EXPERIENCE TEMPLATE — MUST BE FILLED BY ME. Situation: [REAL]. Task: [REAL]. Action: [REAL]. Result/verification: [REAL]. I should not convert a repository defect into a personal incident unless I actually handled it.

**Follow-up**

> What logs did you inspect?

**Strong follow-up answer**

> [FILL WITH REAL INCIDENT].

**Cross-question**

> How long did it take?

**Pressure variation**

> Who helped you?

**What the interviewer is testing**

behavioral evidence

**Common mistake**

Inventing a debugging story.

---

## Q44. Why are technologies on your resume if you did not implement all of them?

**Strong natural answer**

> A project can require architecture-level understanding beyond direct ownership, but my resume wording should reflect the level honestly. For technologies I claim as hands-on skills, I should be able to demonstrate actual use in projects or labs.

**Follow-up**

> Can you defend Qdrant?

**Strong follow-up answer**

> Yes at project architecture/implementation level; personal ownership wording depends on what I actually did.

**Cross-question**

> Can you write the implementation now?

**Pressure variation**

> Which technologies are strongest personally?

**What the interviewer is testing**

resume credibility

**Common mistake**

Equating exposure with deep ownership.

---

## Q45. How much of this was built with AI coding tools?

**Strong natural answer**

> I should answer from my actual process: [FILL]. Using tools does not remove responsibility to understand, test and defend the code. I should clearly explain what I reviewed, changed, verified and learned.

**Follow-up**

> Did AI design the architecture?

**Strong follow-up answer**

> [FILL ACTUAL HISTORY].

**Cross-question**

> Could you rebuild it without AI?

**Pressure variation**

> What part can you implement live?

**What the interviewer is testing**

tool-assisted development honesty

**Common mistake**

Hiding tool use or overstating independent work.

---

# Mock Interview G — Failure / Troubleshooting Round

## Q46. Chat works locally but fails on ECS. How do you troubleshoot?

**Strong natural answer**

> I would split the problem into container startup, service discovery/networking, runtime configuration/secrets, database/Redis connectivity and external provider access. I would inspect ECS events and CloudWatch logs, verify environment/secrets and Cloud Map resolution, then test dependencies one by one.

**Follow-up**

> What if Gateway is healthy but Agent returns 500?

**Strong follow-up answer**

> Trace Gateway → Agent logs, request payload, Agent startup/env, downstream Chat/provider calls and identify the first failing stage.

**Cross-question**

> Would you redeploy first?

**Pressure variation**

> What evidence proves a network problem?

**What the interviewer is testing**

systematic troubleshooting

**Common mistake**

Random changes before evidence.

---

## Q47. Redis connections fail in ECS. What do you inspect?

**Strong natural answer**

> Endpoint/port, security groups, subnet/routing, TLS configuration, environment value, DNS resolution, Redis availability and client error logs.

**Follow-up**

> What user features break?

**Strong follow-up answer**

> Authentication/session validation, fast conversation context and rate limiting can be affected.

**Cross-question**

> Should you fail open for auth?

**Pressure variation**

> How would HA change this?

**What the interviewer is testing**

dependency troubleshooting

**Common mistake**

Treating Redis as only a cache.

---

## Q48. PDF RAG returns unrelated answers. What do you inspect?

**Strong natural answer**

> First confirm routing went to PDF RAG. Then inspect PDF extraction, chunk content, embedding success, Qdrant insert/query, top-five retrieved chunks and finally the generation prompt. The goal is to determine whether retrieval or generation is failing.

**Follow-up**

> What if top-five chunks are irrelevant?

**Strong follow-up answer**

> Investigate chunking, embedding consistency, query wording, metadata and retrieval configuration; then evaluate changes on a labeled set.

**Cross-question**

> Would you increase top K immediately?

**Pressure variation**

> How do you measure improvement?

**What the interviewer is testing**

RAG troubleshooting

**Common mistake**

Changing the LLM before checking retrieval.

---

## Q49. Tavily works but Search is slow. What do you inspect?

**Strong natural answer**

> Measure Tavily duration, Groq synthesis duration, credit operation, Chat persistence and total request time. Search has multiple synchronous external stages, so the slowest stage must be identified.

**Follow-up**

> CPU is low. Does that mean capacity is fine?

**Strong follow-up answer**

> No. Network-bound waits can keep CPU low while concurrency/latency is high.

**Cross-question**

> Would more ECS tasks fix Tavily latency?

**Pressure variation**

> What timeout would you choose?

**What the interviewer is testing**

latency decomposition

**Common mistake**

Scaling before measurement.

---

## Q50. Razorpay payment is paid but credits are missing. What do you do?

**Strong natural answer**

> Confirm the verified payment record and whether the credit mutation executed. Do not blindly grant twice. Reconcile using payment identity and idempotent credit history, then repair the missing business effect exactly once.

**Follow-up**

> What if the previous credit call succeeded but response was lost?

**Strong follow-up answer**

> That is exactly why retry must be idempotent.

**Cross-question**

> How would you design the ledger?

**Pressure variation**

> Should payment remain 'paid'?

**What the interviewer is testing**

financial consistency

**Common mistake**

Manual duplicate credit without idempotency.

---

## Q51. Image is generated but S3 upload fails. What state exists?

**Strong natural answer**

> Provider work already happened and cost may already be incurred, but no deliverable exists. The system needs to return a real failure, clean local buffers/files, and decide whether a retry should regenerate or only retry the upload if the generated binary is still available.

**Follow-up**

> Would you charge credits?

**Strong follow-up answer**

> That depends on the product's accounting policy; current credits are not a precise provider-cost ledger. V2 should define reservation/commit/reversal semantics.

**Cross-question**

> Can you safely retry image generation?

**Pressure variation**

> Where would you persist job state?

**What the interviewer is testing**

partial failure reasoning

**Common mistake**

Ignoring provider cost or duplicate side effects.

---

## Q52. Frontend deploy succeeds but old version appears. What do you check?

**Strong natural answer**

> Check S3 sync result, CloudFront distribution/invalidation status, cache behavior, object keys and the actual build version. Verify from the delivered asset rather than assuming invalidation completed.

**Follow-up**

> Why invalidate CloudFront?

**Strong follow-up answer**

> To reduce stale cached frontend objects after deployment.

**Cross-question**

> Could immutable asset names help?

**Pressure variation**

> Is CloudFront used for the API?

**What the interviewer is testing**

frontend delivery troubleshooting

**Common mistake**

Confusing CloudFront with backend proxy.

---

## Q53. ECS deployment becomes unstable. What do you inspect?

**Strong natural answer**

> ECS service events, task exits, CloudWatch logs, target health, secrets/env, image digest/tag, ports, startup dependencies and whether the new task definition actually contains intended changes.

**Follow-up**

> What if workflow only forced redeploy of latest?

**Strong follow-up answer**

> The deployment may pick a new latest image but local task-definition changes are not automatically registered; that is a current release-safety gap.

**Cross-question**

> How do you roll back?

**Pressure variation**

> Why use Git SHA?

**What the interviewer is testing**

deployment troubleshooting

**Common mistake**

Assuming local JSON was deployed.

---

# Interviewer Trap Drill — 30 Questions

### Trap 1. So your Gateway is AWS API Gateway?

> **Correct response:** No. It is a custom Node.js/Express Gateway service.

---

### Trap 2. You have eight backend microservices?

> **Correct response:** No. Five backend services; eight specialist workflows inside Agent.

---

### Trap 3. Bedrock runs your chat model?

> **Correct response:** No active Bedrock inference is verified.

---

### Trap 4. Redis stores LangGraph checkpoints?

> **Correct response:** No. Redis stores application sessions/context; there is no LangGraph checkpointer.

---

### Trap 5. Your agents plan autonomously?

> **Correct response:** No. Routing is bounded to predefined workflows.

---

### Trap 6. Your agents reflect and retry tools automatically?

> **Correct response:** No reflection or unrestricted tool loop is implemented.

---

### Trap 7. RAG prevents hallucination?

> **Correct response:** No. It improves grounding but cannot guarantee correctness.

---

### Trap 8. You use OCR for PDFs?

> **Correct response:** No. Current PDF flow uses pdf-parse and does not support scanned/image-only PDFs reliably.

---

### Trap 9. Users can upload a PDF once and ask about it later anytime?

> **Correct response:** Not reliably. There is no durable document-to-Qdrant mapping for persistent reuse.

---

### Trap 10. Search citations are guaranteed accurate?

> **Correct response:** No mature citation alignment/fact checking is verified.

---

### Trap 11. Generated code is executed and tested on the server?

> **Correct response:** No.

---

### Trap 12. App session is JWT?

> **Correct response:** No. It is an opaque UUID stored in Redis.

---

### Trap 13. CORS means your API is authorized?

> **Correct response:** No. CORS is a browser cross-origin policy, not authorization.

---

### Trap 14. Cloud Map authenticates internal services?

> **Correct response:** No. It provides service discovery/DNS.

---

### Trap 15. Razorpay HMAC makes payment exactly-once?

> **Correct response:** No. It verifies authenticity, not idempotency.

---

### Trap 16. Credits represent exact provider cost?

> **Correct response:** No.

---

### Trap 17. Secrets Manager means no secrets were exposed?

> **Correct response:** No. A tracked credential/config issue was found.

---

### Trap 18. Presigned URL expiry deletes the S3 object?

> **Correct response:** No.

---

### Trap 19. ECS automatically means the app scales?

> **Correct response:** No. Dependencies/provider quotas can bottleneck.

---

### Trap 20. Low CPU means Agent has spare capacity?

> **Correct response:** Not necessarily. AI calls are network-bound.

---

### Trap 21. Configured task CPU proves throughput?

> **Correct response:** No.

---

### Trap 22. The project is currently Multi-AZ HA?

> **Correct response:** Not verified.

---

### Trap 23. Redis automatic failover is enabled?

> **Correct response:** A captured configuration showed it disabled; current live state is not verified.

---

### Trap 24. The pipeline is zero-downtime with automatic rollback?

> **Correct response:** No mature health/smoke/rollback gate is verified.

---

### Trap 25. Changing local task-definition JSON changes ECS on the next force redeploy?

> **Correct response:** Not automatically; a new task-definition revision must be registered.

---

### Trap 26. Latest is an immutable release tag?

> **Correct response:** No.

---

### Trap 27. CloudFront proxies the backend API?

> **Correct response:** Not in the verified architecture; it serves the frontend.

---

### Trap 28. All specialists use the same conversation memory?

> **Correct response:** No.

---

### Trap 29. MongoDB, Redis and LangGraph state are the same memory?

> **Correct response:** No, they have different lifetimes/responsibilities.

---

### Trap 30. Because the app is deployed, it is production-ready?

> **Correct response:** No. Deployment is only one part of production readiness.

---

# “I Don't Know / Not Verified” Drills

## Drill 1. What is the exact current ECS desired count?

> I don't want to invent the live value. The repository contains ECS service/task configuration, but I would verify the current desired count in ECS.

---

## Drill 2. What is your current p95 latency?

> It is not measured/verified in the project analysis, so I would not make up a number.

---

## Drill 3. What is the monthly AWS bill?

> No verified current monthly cost is available. I would break it down by ECS, ALB/NAT, Redis, storage/logs and external providers.

---

## Drill 4. What exact IAM permissions are attached to the Agent task role?

> The role reference is present, but the effective live policy was not fully inspected. I would verify the attached policies before claiming exact permissions.

---

## Drill 5. How many AZs are your tasks running across right now?

> The live placement is not fully verified, so I would not claim a specific Multi-AZ topology.

---

## Drill 6. What was your worst production outage?

> I would only answer with a real incident I personally experienced. I will not invent one from repository findings.

---

## Drill 7. Why was chunk size exactly 1000?

> The current implementation uses approximately 1000-character chunks with 200 overlap. I do not have evidence that this value came from formal benchmarking, so I would treat it as a current configuration to evaluate.

---

## Drill 8. Who personally chose Qdrant?

> That is historical ownership I should answer only from my real experience, not infer from the repository.

---

# Correction Drills

## Correction 1

**Wrong: 'Our JWT is stored in Redis.'**

> Correction: 'The app session is an opaque UUID stored in Redis. Firebase uses an ID token during login.'

---

## Correction 2

**Wrong: 'We use AWS API Gateway.'**

> Correction: 'We use a custom Express Gateway; the documented AWS ingress is an ALB.'

---

## Correction 3

**Wrong: 'Eight agents are separate ECS services.'**

> Correction: 'They are eight specialist workflows inside the Agent ECS service.'

---

## Correction 4

**Wrong: 'Redis is our LangGraph checkpoint store.'**

> Correction: 'There is no LangGraph checkpointer. Redis is application session/context state.'

---

## Correction 5

**Wrong: 'RAG prevents hallucination.'**

> Correction: 'RAG can improve grounding but does not guarantee correctness.'

---

## Correction 6

**Wrong: 'The app is highly available.'**

> Correction: 'Mature HA is not verified; it is a Production V2 concern.'

---

# Rapid-Fire Drill

**RF1. Backend services?** — 5

**RF2. Names?** — Gateway, Auth, Chat, Agent, Billing

**RF3. Gateway port?** — 8000

**RF4. Auth port?** — 8001

**RF5. Chat port?** — 8002

**RF6. Agent port?** — 8003

**RF7. Billing port?** — 8004

**RF8. Specialist workflows?** — 8 inside Agent

**RF9. LangGraph location?** — Agent service

**RF10. Autonomous planner?** — No

**RF11. Reflection loop?** — No

**RF12. Checkpointing?** — No

**RF13. Redis role?** — Sessions, fast context, rate counters

**RF14. Durable conversation store?** — MongoDB

**RF15. Vector DB?** — Qdrant

**RF16. Embedding model?** — gemini-embedding-001

**RF17. Image analysis?** — Gemini

**RF18. Coding model?** — DeepSeek via OpenRouter

**RF19. Search provider?** — Tavily

**RF20. Image generation?** — Stability AI

**RF21. General text generation?** — Groq-backed model

**RF22. RAG top K?** — 5

**RF23. Chunk size?** — ~1000 chars

**RF24. Chunk overlap?** — ~200 chars

**RF25. OCR?** — No

**RF26. App session?** — Opaque Redis UUID

**RF27. Session TTL?** — 7 days in verified login flow

**RF28. JWT app session?** — No

**RF29. Payment provider?** — Razorpay

**RF30. Payment verification?** — HMAC signature

**RF31. Credits = dollars?** — No

**RF32. Frontend?** — React/Vite

**RF33. Code editor?** — Monaco

**RF34. Containers?** — Docker

**RF35. Registry?** — ECR

**RF36. Orchestrator?** — ECS

**RF37. Compute?** — Fargate

**RF38. Frontend hosting?** — S3 + CloudFront

**RF39. Backend ingress?** — ALB documented/intended

**RF40. Service discovery?** — Cloud Map

**RF41. Logs?** — CloudWatch awslogs

**RF42. Secrets?** — Secrets Manager references

**RF43. Bedrock active?** — No verified active inference

**RF44. Kubernetes?** — No

**RF45. Production-ready?** — Production-oriented, not fully production-ready

**RF46. Autoscaling mature?** — Not verified

**RF47. Multi-AZ HA mature?** — Not verified

**RF48. RTO/RPO defined?** — Not verified

**RF49. Automated test suite mature?** — No

**RF50. RAG eval mature?** — No

**RF51. Prompt-injection defense mature?** — No


# Mock Interview Scoring Rubric

Score each answer 0–5.

| Category | 0 | 3 | 5 |
|---|---|---|---|
| Technical Correctness | wrong | mostly correct | fully correct |
| Project Accuracy | invents details | mostly project-specific | exact verified boundaries |
| Clarity | confusing | understandable | crisp |
| Structure | rambling | reasonable | strong logical flow |
| Depth | wrong depth | acceptable | exactly right depth |
| Trade-Off Awareness | none | one trade-off | balanced alternatives |
| Ownership Honesty | invents ownership | cautious | fully precise |
| Production Thinking | no distinction | some V2 thinking | clear current vs V2 |
| Communication | difficult to follow | acceptable | natural/confident |

**Total: 45**

Use the score only to guide practice.

---

# Red-Flag Tracker

```text
☐ Express Gateway called AWS API Gateway
☐ 8 specialists called 8 microservices
☐ Bedrock claimed active
☐ Redis called LangGraph checkpoint
☐ Autonomous AI overclaimed
☐ RAG said to eliminate hallucination
☐ Production-ready overclaimed
☐ Personal ownership invented
☐ Incident invented
☐ Performance/cost/capacity invented
☐ HA invented
☐ Current vs V2 mixed
☐ Answer too long
☐ No direct answer
☐ No project connection
☐ No limitation/trade-off when needed
```

---
# Final Full Mock Interview — 60-Minute NovaMind Round

## Final 1. Interviewer: Give me a 60-second overview of NovaMind.

> **Model answer:** NovaMind AI is a multi-workflow Generative AI application with a React frontend and five Node/Express backend services. Agent uses bounded LangGraph routing across eight specialist workflows. Different providers support text, coding, search, image and embedding workloads; MongoDB, Redis, Qdrant and S3 handle persistence/state/artifacts. Docker/ECS deployment and GitHub Actions automate AWS delivery. I call it production-oriented but not fully production-ready because authorization, financial consistency, testing, observability and HA need hardening.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 2. Interviewer: Draw the backend service boundaries.

> **Model answer:** Gateway → Auth / Chat / Agent / Billing. Gateway is the common entry; Agent contains all eight AI specialists.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 3. Interviewer: Why not just use one backend service?

> **Model answer:** One service would simplify deployment and transactions. The current separation clarifies responsibilities and potential scaling, but introduces distributed coupling. A modular monolith is a valid alternative.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 4. Interviewer: Where exactly is LangGraph used?

> **Model answer:** Inside Agent, as a bounded state graph for routing to predefined specialist workflows.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 5. Interviewer: Explain the routing priority.

> **Model answer:** Explicit selection first, Auto+PDF→PDF RAG, Auto+image→Image Analysis, otherwise model classifier; unknown label can fall back to Chat.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 6. Interviewer: Is it truly autonomous?

> **Model answer:** No. No autonomous planner, reflection loop, unrestricted tool loop or graph checkpointing.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 7. Interviewer: Trace a normal Chat request.

> **Model answer:** Frontend → Gateway session → Agent → persist user message → LangGraph Chat → Groq → Redis context → persist assistant → response.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 8. Interviewer: Trace Search.

> **Model answer:** Agent/Search → Tavily retrieval → Groq synthesis → persistence → response.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 9. Interviewer: Trace PDF RAG.

> **Model answer:** Temp PDF → pdf-parse → chunks ~1000/200 → Gemini embeddings → new Qdrant collection → query embedding → top-5 retrieval → Groq answer.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 10. Interviewer: What is the biggest current RAG limitation?

> **Model answer:** It is request-oriented, with no durable user/document-to-index mapping for reliable future reuse; OCR/citations/reranking/eval are also immature.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 11. Interviewer: Why Qdrant?

> **Model answer:** Dedicated semantic vector similarity search; trade-off is another stateful service and lifecycle/ownership complexity.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 12. Interviewer: Explain state vs memory.

> **Model answer:** LangGraph state = current execution; Redis = app sessions/fast context/counters; MongoDB = durable history; Redux = UI state.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 13. Interviewer: Explain login.

> **Model answer:** Google/Firebase ID token verification → Mongo user → opaque UUID Redis session → HTTP-only cookie → Gateway lookup.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 14. Interviewer: What is the biggest security concern?

> **Model answer:** Authorization/ownership boundaries, including sensitive account mutations and resource ownership.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 15. Interviewer: How would you stop User A reading User B's conversation?

> **Model answer:** Derive user identity from trusted session, load resource server-side, compare ownerId/permission, deny mismatch, add regression test.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 16. Interviewer: Explain payment consistency risk.

> **Model answer:** Payment can be marked paid before Auth credit update succeeds; duplicate callbacks also need idempotency.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 17. Interviewer: How would you redesign payments?

> **Model answer:** Verified event → idempotency check → auditable credit ledger/transaction → mark processed → reconciliation.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 18. Interviewer: Explain Docker/ECS deployment.

> **Model answer:** Five Docker images → ECR → ECS/Fargate task definitions/services; frontend → S3/CloudFront; ALB/Cloud Map support documented backend networking.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 19. Interviewer: What is execution role vs task role?

> **Model answer:** Execution role supports ECS platform startup/log/secret/image actions; task role is for application AWS API calls.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 20. Interviewer: Explain GitHub Actions deployment.

> **Model answer:** Push main → checkout/AWS auth/ECR login → build/push five images → force ECS redeploy → frontend build/S3 sync/CloudFront invalidation.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 21. Interviewer: What is unsafe about current release process?

> **Model answer:** Mutable latest, no substantive test gates, task-def changes not automatically registered, no mature stability/smoke/rollback gates.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 22. Interviewer: How did you test the application?

> **Model answer:** Current evidence is mainly frontend lint/build plus manual/deployment validation; a substantive automated backend/AI-eval suite was not found.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 23. Interviewer: How would you evaluate the router?

> **Model answer:** Labeled intent set including explicit/file/classifier/unknown/failure cases; per-class accuracy and misroute analysis.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 24. Interviewer: How would you evaluate RAG?

> **Model answer:** Separate retrieval metrics such as Recall@K/hit rate from generation groundedness/relevance/completeness on a curated dataset.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 25. Interviewer: How many users can it handle?

> **Model answer:** I cannot give a defensible number without load testing and provider-quota measurement.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 26. Interviewer: Why can CPU be low when Agent is overloaded?

> **Model answer:** Requests can be waiting on external providers; concurrency and latency can be high while CPU is low.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 27. Interviewer: What are the major cost drivers?

> **Model answer:** ECS/ALB/NAT/Redis/S3/CloudWatch plus Groq, Gemini, OpenRouter, Tavily, Stability, Qdrant and repeated embedding/index work.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 28. Interviewer: Is it highly available?

> **Model answer:** Mature HA is not verified; captured Redis configuration was nonredundant with failover disabled, and live Multi-AZ task topology is not fully verified.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 29. Interviewer: What would you improve first?

> **Model answer:** Authorization and credential exposure, then payments/credits/sessions, then tests/evals, persistent RAG/artifacts, observability/release safety, and finally scale/HA/cost.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---

## Final 30. Interviewer: What did YOU personally implement?

> **Model answer:** PERSONAL OWNERSHIP TEMPLATE — I personally implemented/configured [FILL CONFIRMED AREAS]. I can explain the exact files/functions, issues and verification for those components. I do not claim ownership of the rest simply because it exists in the repository.

**Follow-up challenge:**  
Explain one level deeper, then stop.

**Self-score:**  
Technical Correctness __/5  
Project Accuracy __/5  
Clarity __/5  
Structure __/5  
Depth __/5  
Trade-Off Awareness __/5  
Ownership Honesty __/5  
Production Thinking __/5  
Communication __/5

---


# Final Practice Workflow

After completing the file:

```text
Live Mock 1
↓
score + red flags
↓
revise only weak areas
↓
Live Mock 2
↓
score + pressure chains
↓
Senior Architecture Round
↓
Ownership Defense
↓
Final 60-minute Mock
```

Do not create Module 23.

The NovaMind learning curriculum ends here.

**Module 22 Interview Drill Book complete.**
