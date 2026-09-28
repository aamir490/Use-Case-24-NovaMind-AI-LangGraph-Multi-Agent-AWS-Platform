# Module 21 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Roles, Responsibilities, Project Storytelling and Interview Q&A  
> **Critical rule:** Never convert repository evidence into personal ownership unless personally confirmed.

---

## Ownership Rule

```text
PROJECT FACT
≠
POSSIBLE ROLE RESPONSIBILITY
≠
MY CONFIRMED PERSONAL OWNERSHIP
```

Use project-level wording until ownership is confirmed.

---

# 1 — Tell Me About Your Project

## Q1. Tell me about NovaMind AI.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> NovaMind AI is a full-stack multi-workflow Generative AI application that combines chat, search, coding, PDF RAG, document generation and image workflows. React is the frontend, the backend has Gateway, Auth, Chat, Agent and Billing services, and Agent uses bounded LangGraph routing to eight predefined specialist workflows.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q2. Give me a 15-second introduction.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> NovaMind is a full-stack GenAI platform that combines chat, search, coding, PDF RAG, document generation and image workflows using React, Node/Express, LangGraph and AWS container deployment.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q3. Give me a 30-second introduction.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> NovaMind is a React and Node/Express multi-workflow GenAI platform. Five backend services separate request entry, identity, conversations, AI orchestration and billing, while Agent uses LangGraph to route requests to eight specialist workflows. The platform integrates multiple AI providers and has Docker/ECS deployment configuration on AWS.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q4. Give me a one-minute introduction.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I explain the problem first, then the five-service architecture, bounded LangGraph routing, provider map, MongoDB/Redis/Qdrant/S3 state, AWS deployment, and one important production-hardening limitation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q5. What makes NovaMind different from a normal chatbot?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It does not send every request to one generic model. It routes different request types into specialized workflows for web search, PDF RAG, coding, document generation and image tasks, while also supporting sessions, persistence, payments and cloud deployment.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q6. What is the strongest one-line description?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A full-stack, LangGraph-orchestrated multi-workflow Generative AI application deployed with an AWS container architecture.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 2 — Problem / Business Context

## Q7. What problem does the project solve?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It reduces tool fragmentation by giving users one interface for several AI workflows instead of requiring separate applications for chat, search, code, documents and images.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q8. Who is the target user?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A user who needs multiple AI capabilities in one product experience, such as general Q&A, current web information, document Q&A, coding help or generated artifacts.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q9. Why not just use one LLM for everything?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Different workflows have different requirements, such as live web retrieval, vector search, image generation or coding output. Specialized providers and workflows can fit those requirements better, although they add operational complexity.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q10. What is the product value beyond model access?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The value is orchestration, workflow routing, persistent state, files/artifacts, identity, payments and deployment around the model calls.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q11. What is the main architectural idea?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> One frontend and backend entry point route the request into the correct domain service and, for AI tasks, into the appropriate specialist workflow inside Agent.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 3 — Roles & Responsibilities

## Q12. What was your role?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I separate repository implementation from personal ownership. My confirmed role areas are [FILL CONFIRMED AREAS], and I would only claim components I personally implemented, configured, debugged or deployed.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q13. What were your responsibilities?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I would structure my answer around three to five confirmed areas: my primary technical responsibility, one or two supporting areas, deployment/operations work if I personally did it, and one real troubleshooting contribution.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q14. What did you personally implement?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I would list only confirmed components: [FILL]. I would not claim every component simply because it exists in the repository.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q15. Did you build the whole project yourself?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I would not claim that unless it is literally true and defensible. I separate what the project contains from what I personally owned.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q16. How do you prove a responsibility claim?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I should be able to explain the exact files or configuration, inputs and outputs, design choice, a problem I observed, how I changed it and how I verified it.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q17. What should your final role answer contain?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> My confirmed primary area, supporting area, cloud/deployment work if true, one real debugging story, and an explicit boundary around components I did not personally own.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q18. How do you answer if ownership is uncertain?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I use project-level language such as 'the project implements' until I have confirmed what I personally did.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 4 — Ownership and Credibility

## Q19. What is the difference between project fact and personal ownership?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Project fact means the implementation exists. Personal ownership means I personally designed, implemented, configured, debugged or operated it. Those are different claims.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q20. Why is ownership accuracy important?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Because interviewers can quickly test ownership by asking about exact code paths, failures, alternatives and verification.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q21. What wording is safe if you did not design a component?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I say 'the architecture uses' or 'the project implements' instead of 'I designed'.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q22. Can repository commits alone prove your role?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Not necessarily. They show repository activity but do not automatically prove the full scope of personal design or ownership.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q23. Can you discuss a component you did not personally own?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Yes. I can explain how it works and its trade-offs while being clear that I am describing project architecture rather than claiming direct ownership.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q24. What should you never invent?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Personal incidents, outages, design history, customer impact or ownership that I cannot verify.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 5 — Architecture

## Q25. Explain the architecture at a high level.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> User → React → Express Gateway → Auth/Chat/Agent/Billing. Agent contains LangGraph and eight specialist workflows. Providers/tools and MongoDB/Redis/Qdrant/S3 support those workflows, and the deployment configuration uses AWS container services and S3/CloudFront.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q26. How many backend services are there?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Five: Gateway, Auth, Chat, Agent and Billing.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q27. How many AI specialist workflows are there?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Eight predefined specialist workflows inside Agent.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q28. Are the eight specialists eight ECS services?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. They are JavaScript workflows inside the single Agent service.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q29. Where is LangGraph used?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Inside Agent.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q30. What is the frontend layer?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> React/Vite with Redux, Firebase login, chat/file UI, artifact rendering and Monaco code display.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q31. What is the data layer?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> MongoDB for durable application records, Redis for sessions/fast context/counters, Qdrant for PDF vectors and S3 for files/artifacts.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q32. What is the AWS runtime layer?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> S3/CloudFront for frontend delivery and ECS/Fargate/ECR plus Secrets Manager, CloudWatch and documented ALB/Cloud Map/VPC networking for the backend.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 6 — Frontend / Gateway / Services

## Q33. What does React do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It provides the user interface for chat, file/image upload, response rendering, artifacts and coding preview.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q34. What does Redux do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It stores in-memory frontend application/UI state such as optimistic messages and current user-facing state.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q35. What does Firebase do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It handles Google sign-in and produces the Firebase ID token that Auth verifies during login.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q36. What does the Express Gateway do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It is the main backend entry/proxy service. On protected paths it checks the Redis-backed app session, derives trusted user identity and forwards the request to the correct service.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q37. Is the Express Gateway AWS API Gateway?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. It is a Node.js/Express service.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q38. What does Auth own?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> User/account/session-related behavior.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q39. What does Chat own?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Conversation and message persistence.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q40. What does Agent own?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> AI orchestration, LangGraph and specialist workflows.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q41. What does Billing own?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Razorpay order/payment-related behavior.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q42. Are the service boundaries perfectly independent?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. There is synchronous coupling and some data-boundary leakage, so I would call it microservice-style rather than perfectly isolated microservices.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 7 — LangGraph / Agentic AI

## Q43. What is LangGraph?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A graph-oriented orchestration framework for stateful workflow nodes and transitions.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q44. How is LangGraph used in NovaMind?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> START → router → conditional route → one of eight predefined specialist workflows → END.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q45. What is graph state?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Current request execution data including prompt, response, selected workflow, user/conversation IDs, optional file, search results, images and artifacts.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q46. What is a node?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A work unit that reads or updates graph state.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q47. What is an edge?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A transition from one node to another.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q48. What is a conditional edge?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A transition selected based on the current state or router result.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q49. What is routing priority?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Explicit non-auto selection first; Auto+PDF goes to PDF RAG; Auto+image goes to Image Analysis; otherwise model classification; unknown label falls back to Chat.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q50. What happens if the classifier throws?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> There is no mature universal fallback for classifier exceptions.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q51. Is NovaMind Agentic AI?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It has agentic characteristics through stateful routing, specialist workflows and tool/provider integration, but it is bounded rather than fully autonomous.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q52. Is it fully autonomous?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q53. Does it have an autonomous planner?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q54. Does it have reflection?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No reflection loop is verified.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q55. Does it repeatedly choose unrestricted tools?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q56. Does it have LangGraph checkpointing?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q57. Is Redis conversation state the same as checkpointing?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q58. Is it a true autonomous multi-agent collaboration system?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. A more accurate description is LangGraph-orchestrated specialist workflows inside one Agent service.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 8 — Normal Chat Flow

## Q59. Trace a normal chat request.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> React sends the prompt → Gateway validates the Redis session → Agent saves the user message through Chat → initializes LangGraph state → routes to Chat → Groq generates → Redis context is updated → assistant message is persisted → response returns.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q60. Where is user message persistence handled?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Agent calls the Chat service to save messages.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q61. Does Chat itself run LangGraph?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. LangGraph is inside Agent.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q62. Does every specialist use full conversation history?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. Chat explicitly uses conversation context; other specialists do not necessarily share the same memory behavior.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q63. Is the response token-streamed?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The verified main flow is synchronous rather than token streaming.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 9 — PDF RAG

## Q64. Explain PDF RAG end to end.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Upload PDF → temporary file → pdf-parse text extraction → ~1000-character chunks with ~200 overlap → Gemini embeddings → new Qdrant collection → question embedding → top-five similarity search → retrieved context + question → Groq answer.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q65. Is PDF RAG genuinely implemented?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Yes.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q66. Which embedding model?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> gemini-embedding-001.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q67. Which vector DB?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Qdrant.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q68. Which model/provider generates the final answer?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Groq-backed generation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q69. What is top-k?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The number of nearest chunks retrieved; current verified value is five.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q70. Why chunk the document?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> To retrieve smaller relevant passages rather than send an entire large PDF for every question.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q71. Why overlap chunks?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> To reduce context loss around chunk boundaries.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q72. Does it support OCR?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q73. Can it reliably answer scanned PDFs?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Not if text is only present as images, because no OCR is implemented.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q74. Does it keep a durable document ID-to-collection mapping?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No mature mapping is implemented.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q75. Can the user upload once and reliably ask a text-only follow-up next week?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Not in the current design.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q76. Does it show mature page citations?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q77. Does it rerank retrieved chunks?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No mature reranking stage.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q78. Does it use a mature similarity threshold?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q79. Does RAG eliminate hallucination?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. It improves grounding but does not guarantee correctness.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q80. What is the strongest V2 RAG improvement?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Persistent document identity, ownership, S3 source storage, durable Qdrant mapping, source metadata/citations, lifecycle and evaluation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 10 — Search

## Q81. Explain Search end to end.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The Search specialist calls Tavily for up to five results/images, then passes retrieved information into Groq-backed synthesis and returns the answer.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q82. Is Search the same as PDF RAG?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q83. Why not call Search RAG?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It is web retrieval plus synthesis, while PDF RAG uses embeddings and Qdrant over an uploaded document.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q84. Are source citations guaranteed?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No mature citation alignment/fact-checking is verified.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q85. What makes Search more expensive than basic Chat?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It adds a search provider call before generation, plus additional internal operations.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 11 — Coding

## Q86. Explain Coding end to end.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Coding request → coding-intent classification → OpenRouter → DeepSeek → structured files[] output → backend parsing → Monaco editor → basic browser preview.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q87. Why OpenRouter?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It acts as the access layer for the DeepSeek coding model in this implementation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q88. Does NovaMind execute generated code server-side?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q89. Does it install npm packages?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No full arbitrary package installation flow is implemented.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q90. Does it compile every generated project?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q91. Does it automatically test code?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No full test runner is implemented for generated code.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q92. Does it have an autonomous repair loop?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q93. Why structured files[]?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It gives the backend/frontend a parseable multi-file artifact format.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q94. What is a current risk?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> LLM JSON can be malformed because mature schema-enforced output validation is not implemented.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 12 — Images / PDF / PPT

## Q95. Explain Image Generation.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Prompt preparation → Stability AI → image bytes → S3 → presigned URL → frontend.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q96. Explain Image Analysis.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Uploaded image → Gemini multimodal → text analysis → response.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q97. Generation vs analysis?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Generation is text-to-image; analysis is image-to-text.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q98. Explain PDF generation.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Groq structured content → parse → PDFKit → S3 → presigned URL.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q99. Explain PPT generation.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Groq structured content → parse → PptxGenJS → S3 → presigned URL.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q100. What is the verified PPT pattern?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Cover + six content slides + closing = eight slides.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q101. Does URL expiry delete the S3 object?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q102. What artifact lifecycle gap exists?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No mature artifact ownership metadata and fresh-link renewal model.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 13 — State / Memory

## Q103. Explain LangGraph state vs Redis vs MongoDB.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> LangGraph state is current request execution; Redis is fast shared app state for sessions/context/counters; MongoDB is durable users/conversations/messages/payments.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q104. What does Redux store?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Frontend in-memory UI state.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q105. Does Redis equal LangGraph checkpointing?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q106. What current Redis memory issues exist?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Unbounded hydration, possible duplicate current message, read-modify-write races, weak cap enforcement, TTL-loss risk and no token-aware summarization.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q107. What survives Agent restart?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> External stores may survive, but local temp state and in-flight graph execution do not have a durable resume protocol.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 14 — Authentication / Security

## Q108. Explain login end to end.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Google sign-in → Firebase ID token → Auth verifies → user lookup/create → opaque UUID session in Redis → HTTP-only cookie → later Gateway session lookup.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q109. Is the application session a JWT?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q110. What is authentication?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Proving who the user is.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q111. What is authorization?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Deciding what resources/actions that user is allowed to access.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q112. Is authorization fully mature?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. Tenant/resource ownership is partial.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q113. What security controls exist?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Firebase verification, Redis sessions, HTTP-only cookies, Razorpay HMAC, file MIME/size limits, presigned S3 links, sandboxed iframe and Secrets Manager references.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q114. What are the main verified security gaps?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Sensitive account/credit mutation paths, alternate admin route concern, ownership gaps, tracked credential exposure, partial session revocation, no mature CSRF strategy and prompt-injection risk.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q115. Does CORS provide authorization?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q116. Does Cloud Map authenticate services?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q117. What should happen if Redis session lookup fails?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> For protected operations, failing closed is safer than trusting unverified client identity.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 15 — Payments

## Q118. Explain the payment flow.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Billing creates a Razorpay order and Payment(created) record; checkout completes; Billing verifies HMAC; Payment is marked paid; Billing calls Auth to grant credits.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q119. What does HMAC verification prove?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The callback/signature is authentic according to the shared secret; it does not solve replay or cross-service consistency.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q120. What is the main payment consistency problem?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Payment can be marked paid before the credit grant succeeds.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q121. What is replay risk?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The same callback/event can be processed multiple times and repeat a business effect if processing is not idempotent.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q122. How would you fix it?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Use a stable payment/event ID, idempotent processing, an auditable credit ledger and reconciliation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q123. What happens if credit deduction helper fails?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Provider work may continue even though deduction was not confirmed, creating a business-cost gap.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q124. Are credits actual provider-dollar cost?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 16 — Docker / ECS / AWS

## Q125. How is the backend containerized?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Five separate Dockerized Express services.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q126. What is a Docker image?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> An immutable package/template containing application filesystem and runtime setup.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q127. What is a container?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A running instance of an image.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q128. What is ECR?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> AWS container image registry.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q129. What is ECS?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> AWS container orchestration service.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q130. What is Fargate?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A serverless compute engine for ECS tasks.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q131. What is an ECS task definition?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The runtime blueprint for containers, resources, roles, secrets and logging.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q132. What are verified task resources?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Gateway/Auth/Chat/Billing are approximately 512 CPU/1024 MiB; Agent is 1024 CPU/2048 MiB.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q133. Does that tell you capacity?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q134. What does ALB do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Routes backend traffic to healthy targets in the documented/intended architecture.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q135. What does CloudFront do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Delivers the S3-hosted frontend.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q136. What does Cloud Map do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Provides internal DNS/service discovery.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q137. What do Secrets Manager refs do?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Inject/reference runtime secrets for tasks.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q138. What does CloudWatch provide today?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Centralized container logs through awslogs.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q139. Is the full live network topology verified?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. Much of the ALB/VPC/private-task topology is documented/intended rather than comprehensively live-verified.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 17 — CI/CD

## Q140. Explain the deployment workflow.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Push main → GitHub Actions → configure AWS credentials → ECR login → build/tag/push five backend images → force ECS redeploy → build frontend → S3 sync → CloudFront invalidation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q141. Why is it automated deployment rather than mature CI/CD?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It lacks substantive automated test/eval gates, immutable release identifiers, explicit task-definition registration, stability/smoke verification and automated rollback.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q142. What is wrong with mutable latest?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It makes release identity and rollback less deterministic than immutable Git-SHA/image-digest releases.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q143. What happens to local task-definition JSON changes?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The current workflow does not explicitly register a new task-definition revision, so force redeploy alone may not apply those local definition changes.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q144. What should V2 add?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Git SHA tags, tests/evals, image scanning, OIDC, explicit task-def registration, wait for stability, smoke tests and rollback.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 18 — Reliability / Troubleshooting

## Q145. What is a major error-handling weakness?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Some specialist exceptions are turned into error text returned as a normal AI response, often with HTTP 200.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q146. Why is HTTP 200 for failure bad?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Clients and monitoring may treat failure as success and the failure text can be persisted as an assistant message.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q147. What is a partial failure?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Some side effects complete before a downstream operation fails.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q148. Give a payment partial-failure example.

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Payment becomes paid but the credit update fails.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q149. How would you troubleshoot a generic 500?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Identify request stage, inspect Gateway and target-service logs, check provider/data dependencies, identify already-completed side effects, then reproduce and verify the fix.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q150. How would you troubleshoot slow AI?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Break total latency into Gateway/session, routing, provider/tool, persistence and network stages instead of blaming the model immediately.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q151. What is your troubleshooting framework?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Symptom → hypothesis → evidence → root cause → fix → verification → prevention.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q152. Should you invent a troubleshooting story?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No. Use only a personally confirmed incident for behavioral questions.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 19 — Testing / AI Evaluation

## Q153. How did you test the project?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Current evidence includes frontend lint/build and manual deployment verification, but no substantive backend unit/integration/E2E or mature AI-evaluation suite was found.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q154. What would you test first?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Authorization/resource ownership, payment replay/idempotency, credit consistency and HTTP error semantics.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q155. What router tests would you add?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Explicit selection priority, Auto+PDF, Auto+image, classifier labels, unknown-label fallback and exception behavior.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q156. How would you evaluate router quality?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Build a representative dataset and measure accuracy, confusion patterns and per-workflow precision/recall.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q157. How would you evaluate RAG?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Separate retrieval quality from generation quality.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q158. What is Recall@K?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> How much relevant evidence appears in the top K retrieved chunks.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q159. What is Precision@K?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> How much of the top K retrieved set is relevant.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q160. What is faithfulness?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Whether the answer stays supported by retrieved context instead of inventing unsupported claims.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q161. Does HTTP 200 prove AI quality?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q162. What observability is verified?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> CloudWatch container logs.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q163. What is not maturely verified?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Correlation IDs, distributed tracing, app metrics and AI quality dashboards.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 20 — Scalability / Performance / Cost / HA

## Q164. Is NovaMind scalable?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The containerized services can scale horizontally in principle, but measured capacity and mature autoscaling are not verified.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q165. Why doesn't adding Agent tasks solve everything?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Provider quotas, Redis, MongoDB, Qdrant, network and race conditions can remain bottlenecks.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q166. Why can CPU be low while latency is high?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Agent can be waiting on external providers with many open requests.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q167. What are important performance metrics?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Workflow-specific concurrency, throughput and p50/p95/p99 latency plus error rate and dependency latency.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q168. What is a likely Agent bottleneck?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> All eight AI workflows share the same Agent service.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q169. Why can PDF RAG be expensive?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It repeats parsing, chunking, embeddings and Qdrant indexing for each request-oriented upload.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q170. How would V2 improve RAG performance?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Persist documents and indexes so the document is embedded once and reused for authorized follow-ups.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q171. How do you control cost?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Current credits control application usage, but V2 should measure provider and infrastructure cost per workflow.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q172. What are major cost drivers?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> ECS/Fargate, ALB/NAT/Redis/S3/CloudWatch plus Groq/Gemini/OpenRouter/Tavily/Stability/Qdrant and embeddings.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q173. Is current HA mature?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q174. What captured HA risk exists?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Redis was captured as single-node/nonredundant with failover disabled.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q175. What should V2 add for HA?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Redundant ECS tasks across AZs where required, Redis failover, verified stateful HA, backups/restore and defined RTO/RPO.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 21 — Design Decisions

## Q176. Why five services?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Clear responsibility boundaries; trade-off is distributed complexity and synchronous coupling. A modular monolith is a valid alternative.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q177. Why LangGraph?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Explicit state and conditional routing; trade-off is framework overhead for the current bounded graph. Plain JavaScript routing is an alternative.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q178. Why Redis?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Shared low-latency server-side sessions/context; trade-off is critical dependency, atomicity, TTL and HA complexity. JWT is an alternative with different revocation trade-offs.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q179. Why MongoDB?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Flexible document persistence with Node/Mongoose; trade-off is indexing/pagination and ownership design.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q180. Why Qdrant?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Semantic vector search for PDF RAG; trade-off is another service and index lifecycle.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q181. Why multiple providers?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Specialized capabilities; trade-off is more credentials, quotas, cost and response variability.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q182. Why Fargate?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Managed container compute without EC2 host management; trade-off is baseline cost and networking/IAM/deployment complexity.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q183. Why S3 artifacts?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Scalable object storage and presigned access; trade-off is ownership, lifecycle and expired links.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q184. Why synchronous AI calls?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Simple UX; trade-off is long-held connections and timeout/concurrency pressure. Async jobs are a future option for long work.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 22 — Limitations

## Q185. What are the main limitations?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Authorization, payment/credit consistency, request-oriented RAG and artifact lifecycle, Redis memory issues, testing/eval gaps, basic observability, release-safety gaps and unverified mature HA.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q186. Which limitation is highest risk?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Authorization/resource ownership and credential/security issues should be fixed first.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q187. Why is admitting limitations good in an interview?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It shows engineering judgment if I explain impact, trade-off and a realistic improvement.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q188. What should you never say about limitations?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I should not claim there are no major limitations or pretend proposed fixes are already implemented.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q189. What is the best limitation answer structure?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> State the limitation → impact → current reason → V2 fix → trade-off.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 23 — Production V2

## Q190. What would you improve first?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Authorization and credential rotation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q191. What comes after security?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Payment/credit idempotency and complete session revocation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q192. Then what?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Automated tests and AI evaluation, persistent RAG/artifact lifecycle, observability/release safety, then scale/HA/cost.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q193. Why security before scale?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Scaling a broken authorization or accounting path increases blast radius.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q194. How would persistent RAG work?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Document ID + owner + S3 source + metadata + durable Qdrant mapping + authorized retrieval + retention.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q195. How would artifact lifecycle work?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Persist artifact metadata/owner/object key and issue fresh presigned URLs only after authorization.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q196. How would release safety improve?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Immutable Git-SHA images, explicit task-definition revisions, tests, scans, stability checks, smoke tests and rollback.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q197. How would observability improve?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Structured logs, correlation IDs, metrics, traces and AI-specific quality signals.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 24 — Pressure / Challenge Questions

## Q198. You call it multi-agent, but where are the agents?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The eight task-specific specialists are inside Agent. I would not describe them as autonomous independently deployed agents; 'LangGraph-orchestrated specialist workflows' is more precise.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q199. Why not just use one model?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Some tasks require capabilities beyond text generation, such as vector embeddings, web search or image generation. Specialized providers fit those needs, at the cost of more operational complexity.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q200. Why not Bedrock?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Active Bedrock inference is not verified in this project, so I do not claim it.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q201. Why not AWS API Gateway?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> The project uses an Express Gateway, with ALB documented/intended for AWS ingress.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q202. Why not JWT?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Redis sessions provide centralized server-side state and revocation potential; JWT reduces lookup but makes immediate revocation/stale claims harder.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q203. Why not a monolith?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> A modular monolith could be simpler. The current service split is useful only where responsibility/scaling/ownership benefits justify distributed complexity.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q204. Is LangGraph over-engineering?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> It may be more framework than strictly necessary for the current bounded router, but it provides explicit graph/state structure and controlled extensibility.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q205. How many users can it support?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I cannot give a defensible number without load tests and dependency-quota measurements.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q206. What is your current p95?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Not verified.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q207. What was the worst production outage you fixed?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I would only answer with a personally confirmed incident. I will not invent one.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q208. Did you personally design the architecture?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> I would claim that only if personally confirmed; otherwise I explain the architecture and state my confirmed contribution separately.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q209. Why should I believe you understand this project?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Because I can trace concrete request flows, explain state and provider boundaries, defend trade-offs, identify verified limitations and explain what I would improve without relying on unsupported claims.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q210. Is this production-ready?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Production-oriented, not fully production-ready.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# 25 — Rapid Fire

## Q211. Gateway port?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> 8000.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q212. Auth port?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> 8001.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q213. Chat port?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> 8002.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q214. Agent port?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> 8003.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q215. Billing port?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> 8004.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q216. Backend services?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Five.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q217. Specialists?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Eight inside Agent.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q218. RAG embedding model?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> gemini-embedding-001.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q219. Vector DB?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Qdrant.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q220. RAG top K?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> 5.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q221. Search provider?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Tavily.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q222. Coding model?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> DeepSeek through OpenRouter.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q223. Image generation?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Stability AI.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q224. Image analysis?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Gemini.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q225. Text generation?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Groq is a major provider for general generation.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q226. Application session JWT?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q227. Session store?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Redis.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q228. Durable conversations?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> MongoDB.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q229. Artifacts?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> S3.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q230. Frontend delivery?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> S3 + CloudFront.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q231. Backend runtime?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> ECS/Fargate.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q232. Container registry?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> ECR.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q233. LangGraph checkpointer?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q234. Autonomous planner?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q235. Reflection loop?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q236. Bedrock active?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> No.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

## Q237. Production-ready?

**What the interviewer is testing:** Whether you understand the project well enough to explain the real implementation, defend the engineering trade-off, and avoid unsupported ownership or production claims.

**Word-for-word answer:**

> Production-oriented, not fully production-ready.

**Likely follow-up:**

> “Can you show where that happens in the request flow and explain the trade-off?”

**Follow-up answer:**

> I would trace the relevant request from the frontend through Gateway, the owning service, Agent/LangGraph if AI is involved, the provider/data store, and then explain the limitation or alternative. I would clearly separate current implementation from Production V2.

**Cross-question:**

> “Did you personally implement that?”

**Ownership-safe answer:**

> I separate project implementation from my own contribution. I would only say I personally implemented it if I can defend the exact code or configuration, debugging and verification. My confirmed ownership here is: **[FILL IF TRUE]**.

**Pressure variation:**

> “What is wrong with the current approach?”

**Defense:**

> I would state the current limitation directly, explain its impact, then describe a Production V2 improvement without pretending it is already implemented.

**What not to say:** Do not claim full autonomy, Bedrock, eight ECS specialist services, mature production readiness, or personal ownership unless verified.

**Key technical point:** Project behavior, design trade-off, production maturity and personal ownership are separate dimensions.

---

# Master Story Scripts\n\n## 15-Second Project Answer\n\n> NovaMind AI is a full-stack Generative AI platform that combines chat, search, coding, PDF RAG, document generation and image workflows. It uses React, Node/Express, bounded LangGraph routing and AWS container deployment.\n\n## 30-Second Project Answer\n\n> NovaMind AI is a full-stack multi-workflow Generative AI application. React is the frontend, and five Express services separate Gateway, Auth, Chat, Agent and Billing responsibilities. Agent uses LangGraph to route requests to eight predefined specialist workflows, and the platform integrates multiple AI providers with MongoDB, Redis, Qdrant and S3. The backend is containerized for ECS/Fargate on AWS.\n\n## 60–90 Second Project Answer\n\n> NovaMind AI is designed to combine several AI capabilities in one application. The React frontend sends requests through an Express Gateway to Auth, Chat, Agent and Billing services. Agent contains a bounded LangGraph router that selects one of eight specialist workflows such as Chat, Search, Coding, PDF RAG, document generation and image workflows. Groq handles much of the text generation, Gemini handles embeddings and image analysis, DeepSeek through OpenRouter handles coding, Tavily provides web search and Stability generates images. MongoDB stores durable data, Redis provides sessions and fast context, Qdrant stores vectors and S3 stores artifacts. Docker/ECS/Fargate configuration and GitHub Actions automate deployment. I call the project production-oriented rather than fully production-ready because authorization, payment consistency, testing, observability and HA still need hardening.\n\n## 2–3 Minute Project Answer\n\n> The problem NovaMind addresses is tool fragmentation: users may need general chat, current web information, coding, document Q&A, document generation and image capabilities, but those normally live in separate tools. NovaMind brings them together in one product.\n>\n> The frontend is React and the backend has five separately containerized Express services: Gateway, Auth, Chat, Agent and Billing. Gateway is the entry point, Auth handles identity/account/session concerns, Chat owns conversation persistence, Billing handles Razorpay, and Agent contains AI orchestration.\n>\n> Inside Agent, LangGraph is genuinely implemented as a bounded graph. Explicit workflow selection has highest priority, Auto plus PDF routes to PDF RAG, Auto plus image routes to image analysis, and otherwise a model classifier chooses a predefined specialist. The eight specialists are workflows inside Agent, not eight ECS services.\n>\n> Different workflows use different providers: Groq for general generation, Gemini for embeddings and image analysis, DeepSeek through OpenRouter for coding, Tavily for search and Stability for image generation. MongoDB stores durable application data, Redis stores sessions and fast conversation context, Qdrant supports PDF vector retrieval and S3 stores generated artifacts.\n>\n> The backend is containerized with ECS/Fargate task definitions and ECR images, while S3/CloudFront deliver the frontend. GitHub Actions automates image builds/pushes, ECS redeployment and frontend deployment. The current version is production-oriented, but Production V2 should harden authorization, payment idempotency, persistent RAG/artifact lifecycle, testing/evaluation, observability, release safety and HA.\n\n## 5-Minute Whiteboard Script\n\n> I’ll draw it in layers. User traffic starts at React. API calls go to a custom Express Gateway—not AWS API Gateway. Behind Gateway are Auth, Chat, Agent and Billing, so with Gateway there are five backend services. Auth owns identity/account/session concerns, Chat owns conversations/messages, Billing owns payments, and Agent owns AI orchestration.\n>\n> Inside Agent is LangGraph. It uses a bounded router to choose one of eight specialist workflows: Chat, Search, Coding, PDF RAG, PDF Generation, PPT Generation, Image Generation and Image Analysis. Those specialists are inside Agent, not separately deployed microservices.\n>\n> The provider depends on the workflow: Groq for much of the text generation, Gemini for embeddings and image analysis, DeepSeek through OpenRouter for coding, Tavily for search and Stability for image generation. PDF RAG also uses Qdrant for similarity retrieval.\n>\n> MongoDB stores durable users/conversations/messages/payments, Redis stores opaque app sessions and fast context, Qdrant stores vectors, and S3 stores artifacts. The AWS deployment uses S3/CloudFront for the frontend and ECS/Fargate/ECR plus Secrets Manager, CloudWatch and documented ALB/Cloud Map networking for the backend.\n>\n> I would not call the current version fully production-ready. Authorization, payment consistency, persistent document/artifact lifecycle, tests/evals, observability, release safety and HA require more hardening. I can now trace any workflow end to end if you want.\n\n---\n\n# Role & Responsibility Answer Templates\n\n## 30 Seconds\n\n> My main responsibility was **[CONFIRMED AREA]**, where I personally **[ACTION]**. I also worked on **[CONFIRMED SECONDARY AREA]**. I can go deeper into the exact implementation, debugging and verification for those areas.\n\n## 60–90 Seconds\n\n> My primary responsibility was **[CONFIRMED AREA 1]**, where I personally **[ACTION]**. I also worked on **[CONFIRMED AREA 2]**, especially **[DETAIL]**. On deployment/operations I personally **[CONFIRMED ACTION]**. One issue I directly handled was **[REAL INCIDENT]**, where I diagnosed **[ROOT CAUSE]**, applied **[FIX]**, and verified it using **[EVIDENCE]**. I understand the full architecture, but I separate that understanding from components I did not directly own.\n\n## 2 Minutes\n\n> My role focused primarily on **[CONFIRMED AREA 1]** and **[CONFIRMED AREA 2]**. In the first area I personally implemented/configured **[DETAIL]**. In the second I worked on **[DETAIL]**. I also contributed to **[DEPLOYMENT/OPERATIONS]** by **[ACTION]**. One issue I directly debugged was **[REAL INCIDENT]**; the symptom was **[SYMPTOM]**, I checked **[EVIDENCE]**, identified **[ROOT CAUSE]**, implemented **[FIX]**, and verified it with **[TEST/LOG/RESULT]**. The broader project also contains other components that I understand architecturally but do not claim as personal ownership unless I directly worked on them.\n\n---\n\n# STAR Template — Personal Incident Must Be Real\n\n```text\nSituation:\n________________________\n\nTask:\n________________________\n\nAction:\n________________________\n\nResult:\n________________________\n\nVerification / Learning:\n________________________\n```\n\nNever invent an outage, production incident, customer impact or personal implementation story.\n\n---\n\n# Troubleshooting Story Template\n\n```text\nSymptom\n→ Hypothesis\n→ Evidence\n→ Root Cause\n→ Fix\n→ Verification\n→ Prevention\n```\n\n---\n\n# Design-Decision Defense Template\n\n```text\nRequirement\n→ Current Design\n→ Why It Fits\n→ Benefit\n→ Trade-Off\n→ Alternative\n→ When I Would Change It\n```\n\n---\n\n# Ten Critical Follow-Up Chains\n\n## Chain 1 — Redis\n\n```text\nWhy Redis?\n→ Why not JWT?\n→ What if Redis fails?\n→ How do sessions expire?\n→ How do you revoke?\n→ How would Redis become HA?\n→ What is wrong with current memory updates?\n```\n\n## Chain 2 — LangGraph\n\n```text\nWhy LangGraph?\n→ What is state?\n→ What is a conditional edge?\n→ Is it autonomous?\n→ Does it have loops?\n→ Does it checkpoint?\n→ Why not plain JS routing?\n```\n\n## Chain 3 — PDF RAG\n\n```text\nWhy chunk?\n→ Why overlap?\n→ Why embeddings?\n→ Why Qdrant?\n→ Why top 5?\n→ What if retrieval is wrong?\n→ Where are citations?\n→ Can I reuse the document next week?\n```\n\n## Chain 4 — Microservices\n\n```text\nWhy five services?\n→ Are they independently deployable?\n→ Why does Agent call Chat?\n→ Why does Auth touch other DB areas?\n→ Why not a modular monolith?\n```\n\n## Chain 5 — Payments\n\n```text\nWhy HMAC?\n→ What about replay?\n→ What if Auth fails after paid?\n→ How would idempotency work?\n→ Why use a ledger?\n→ How do you reconcile?\n```\n\n## Chain 6 — Docker / ECS\n\n```text\nWhat is Docker image?\n→ ECR?\n→ ECS task?\n→ task definition?\n→ Fargate?\n→ ALB?\n→ desired count?\n→ autoscaling?\n```\n\n## Chain 7 — CI/CD\n\n```text\nWhat triggers deployment?\n→ How are images tagged?\n→ What is wrong with latest?\n→ Are task-definition changes registered?\n→ Do you wait for stability?\n→ Smoke test?\n→ Rollback?\n```\n\n## Chain 8 — Security\n\n```text\nAuthentication?\n→ Authorization?\n→ ownership?\n→ admin?\n→ client x-user-id?\n→ CSRF?\n→ service-to-service auth?\n```\n\n## Chain 9 — Testing\n\n```text\nWhat tests exist?\n→ Why not enough?\n→ router test vs eval?\n→ RAG retrieval vs generation eval?\n→ payment replay test?\n→ deployment smoke gate?\n```\n\n## Chain 10 — Scalability\n\n```text\nCan Agent scale?\n→ What is the bottleneck?\n→ CPU low but latency high?\n→ provider quota?\n→ Redis?\n→ p95/p99?\n→ how many users?\n```\n\n---\n\n# Interview Trap Sheet\n\n| Trap | Accurate Response |\n|---|---|\n| “AWS API Gateway?” | Custom Express Gateway; no main AWS API Gateway |\n| “Eight microservices?” | Five backend services; eight specialists inside Agent |\n| “Bedrock?” | No active Bedrock inference verified |\n| “Redis checkpointing?” | No LangGraph checkpointer |\n| “Fully autonomous?” | No, bounded routing |\n| “RAG prevents hallucination?” | No |\n| “Production ready?” | Production-oriented, not fully production-ready |\n| “Credits = cost?” | No |\n| “You built all of it?” | Claim only confirmed ownership |\n\n---\n\n# What Not to Say\n\nDo not say:\n\n- “I designed the complete platform,” unless true.\n- “There are eight microservices.”\n- “Express Gateway is AWS API Gateway.”\n- “Bedrock powers the models.”\n- “Redis is LangGraph checkpointing.”\n- “The system is fully autonomous.”\n- “RAG eliminates hallucinations.”\n- “The system is production-ready.”\n- “Credits are exact dollar cost.”\n- “I fixed a production outage,” unless it actually happened.\n- “We chose X because…,” if historical decision ownership is unknown.\n\n---\n\n# Final Self-Test Before Module 22\n\nYou should answer without notes:\n\n1. Tell me about NovaMind in 15 seconds.\n2. Tell me about it in 30 seconds.\n3. Tell me about it in one minute.\n4. Explain the architecture in 2–3 minutes.\n5. Draw the architecture.\n6. Explain your confirmed role.\n7. Explain one real personal challenge.\n8. Trace Chat.\n9. Trace Search.\n10. Trace PDF RAG.\n11. Trace Coding.\n12. Trace image generation/analysis.\n13. Explain state vs memory.\n14. Explain authentication vs authorization.\n15. Explain payment consistency.\n16. Explain AWS deployment.\n17. Explain CI/CD.\n18. Explain security limitations.\n19. Explain testing/evaluation.\n20. Explain scalability/cost/HA.\n21. Defend LangGraph, Redis, Qdrant, Fargate and multiple providers.\n22. State top five limitations.\n23. Explain Production V2.\n24. Correct the common interview traps.\n25. Separate project fact from personal ownership.\n\n**Module 21 Interview preparation complete.**\n