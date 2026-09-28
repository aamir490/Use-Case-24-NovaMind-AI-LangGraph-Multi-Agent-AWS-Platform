# Module 07 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Specialist AI Workflows and Tool Integration  
> **Purpose:** Practice explaining every specialist workflow, its providers/tools, its data flow, its limitations, and the trade-offs behind the design.

---

## Accuracy Rules

Confidently say:

```text
8 predefined specialist workflows exist inside the Agent service.
Chat → Groq-backed generation.
Search → Tavily → Groq-backed synthesis.
Coding → coding-intent step → OpenRouter → DeepSeek → structured files[].
PDF RAG → pdf-parse → chunks → Gemini embeddings → Qdrant top-5 → Groq-backed answer.
PDF Generation → LLM structured content → PDFKit → S3 → presigned URL.
PPT Generation → LLM structured content → PptxGenJS → S3 → presigned URL.
Image Generation → Stability AI → S3.
Image Analysis → Gemini 2.0 Flash → text.
```

Do not claim:

```text
8 separate ECS agent services
Autonomous collaboration among specialists
Full code execution/test/repair
OCR for scanned PDFs
Persistent reusable PDF knowledge base
Guaranteed search citations/fact checking
Uniform conversation memory across all specialists
Mature async job processing
Mature AI evaluation suite
```

---

# Foundations

## Q1. What is a specialist workflow?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> A specialist workflow is a task-focused execution path with its own prompt, tools, provider integrations, parsing logic and output handling.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q2. Why does NovaMind use specialists?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Because different tasks need different models, tools and output formats. Specialization keeps each workflow focused instead of forcing every request through one giant general-purpose prompt.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q3. How many specialist workflows are there?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Eight.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q4. Name the eight workflows.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Chat, Search, Coding, PDF RAG, PDF Generation, PPT Generation, Image Generation and Image Analysis.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q5. Are the eight specialists eight microservices?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. They are workflows inside the Agent service.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q6. Are the eight specialists eight ECS services?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. The Agent service is the container/service boundary.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q7. What is the common specialist lifecycle?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Read state, validate inputs, call the required model/tool, parse the result, update state, persist where necessary, and return the response or artifact.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q8. What is the difference between a specialist and a provider?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The specialist is NovaMind application logic. The provider is an external platform or API used by that workflow.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q9. What is the difference between a specialist and a tool?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The specialist owns the task flow; the tool is one capability used inside that flow.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q10. What is the difference between a specialist and a model?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The specialist coordinates the task. The model performs inference for one step.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q11. Why is one giant agent not always better?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> A giant agent can require one large prompt and broad tool access, making behavior harder to control, secure, test and optimize.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q12. What is the main trade-off of specialists?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> More routing and orchestration complexity.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Chat Workflow

## Q13. Walk me through the Chat workflow.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The Chat specialist receives the user prompt, loads relevant conversation context, calls the Groq-backed language model, updates the response in state, and persists the assistant message through the Chat service.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q14. Which provider is used for general Chat?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Groq.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q15. What configured model ID is used through Groq?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `openai/gpt-oss-120b`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q16. Does that mean NovaMind uses the OpenAI API?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. The configured model ID contains `openai/`, but the verified client/provider is Groq.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q17. Does Chat use conversation context?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Yes. Chat is the specialist that explicitly uses conversation history/context.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q18. Does every specialist use the same history?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q19. What can fail in Chat?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Context loading, Groq inference, credit handling, Chat persistence or Redis/MongoDB dependencies.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q20. Give a Chat partial-success example.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The model can generate an answer successfully while saving the assistant message through Chat fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q21. How would you improve Chat memory?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Use token-aware recent-history windows, summarization, atomic updates and consistent TTL handling.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q22. Is Chat a separate microservice from Agent?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The Chat service is a separate backend service for conversation persistence; the Chat specialist itself is inside Agent.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q23. Why does Agent call Chat rather than writing messages directly?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It preserves a clearer conversation-persistence boundary, although it adds a synchronous dependency.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q24. What is the main Chat cost driver?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Language-model input/output usage, especially as conversation context grows.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Search Workflow

## Q25. Walk me through Search.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The router selects Search, Tavily retrieves current web results and images, the results are passed into the language-generation path, and the Groq-backed model synthesizes the final answer.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q26. Is Tavily an LLM?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. Tavily is the web-search/retrieval tool.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q27. Who generates the final Search answer?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The Groq-backed language-model path.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q28. How many Tavily results are configured?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Up to about five results, with images also requested.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q29. Why is Search more expensive than Chat?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It includes retrieval plus language-model synthesis and additional application credit handling.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q30. How many application credits can a Search-to-Chat request request?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The verified flow can request 5 credits in Search plus 1 credit in Chat, effectively 6 credits for a successful chain.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q31. Are those credits the real provider cost?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. They are application-level credits, not a verified dollar-cost ledger.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q32. Does Search guarantee accurate citations?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. Mature citation alignment and fact checking are not verified.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q33. Can web results contain prompt injection?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Yes. Retrieved web text must be treated as untrusted data.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q34. What happens if Tavily succeeds but Groq fails?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Retrieval succeeds but synthesis fails, which is partial success.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q35. What happens if Groq is healthy but Tavily fails?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The current-search capability cannot retrieve the latest information.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q36. Why not silently answer from the LLM if Tavily fails?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Because that would no longer provide the same current-web-search guarantee and should be explicit.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q37. What would you monitor for Search?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Tavily latency/error rate, Groq latency/error rate, result counts, final success, fallback behavior and per-request cost.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q38. How would you test Search?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Test routing, normal results, empty results, malformed results, Tavily timeout, Groq failure and malicious retrieved content.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Coding Workflow

## Q39. Walk me through Coding.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The request routes to Coding, a coding-intent step determines the task type, the workflow calls DeepSeek through OpenRouter, expects structured files, parses them into an artifact, and the frontend displays them in Monaco with a basic browser preview where compatible.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q40. What is OpenRouter?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The model-access layer.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q41. What is DeepSeek?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The configured coding model.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q42. What model ID is used?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `deepseek/deepseek-chat`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q43. What temperature is configured?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> 0.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q44. What approximate max output is configured?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> About 2500 tokens.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q45. Why structured files instead of one code block?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The frontend needs file names and contents to create a multi-file code artifact.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q46. What does the expected structure contain?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> A `files` array with items such as file name and content.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q47. What can make structured parsing fail?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Malformed JSON, Markdown fences, missing fields, extra commentary, escaping problems or truncated output.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q48. Does the project execute generated backend code?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q49. Does it install dependencies automatically?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q50. Does it compile and test generated code server-side?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q51. Does it have an autonomous repair loop?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q52. What is Monaco used for?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Displaying/editing generated code in the frontend.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q53. What is the browser preview limitation?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It is a basic preview suitable for compatible frontend HTML/CSS/JS, not a complete application runtime.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q54. How would you improve Coding in Production V2?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Schema validation, safe sandboxing, dependency controls, compile/test stages and optional repair loops only where justified.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# PDF RAG

## Q55. Walk me through PDF RAG.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The uploaded PDF is temporarily stored, parsed to text, split into overlapping chunks, embedded with Gemini, stored/searched in Qdrant, the question is embedded, the top relevant chunks are retrieved, and the Groq-backed model generates the final answer.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q56. What extracts PDF text?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `pdf-parse`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q57. What is the chunk size?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> About 1000 characters.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q58. What is the overlap?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> About 200 characters.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q59. What embedding model is used?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `gemini-embedding-001`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q60. What vector database is used?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Qdrant.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q61. How many chunks are retrieved?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Top five.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q62. Who generates the answer?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The Groq-backed language-model path.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q63. Is Qdrant the RAG model?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. Qdrant stores/retrieves vectors.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q64. Is Gemini the final answer model in this flow?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. Gemini is used for embeddings; Groq-backed generation produces the answer.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q65. Does RAG eliminate hallucinations?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. It improves grounding but retrieval and generation can still fail.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q66. Is OCR implemented?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q67. Does it support scanned PDFs reliably?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Not without OCR, so scanned/image-only PDFs are a limitation.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q68. Is reranking implemented?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q69. Are mature page citations implemented?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q70. Is a retrieval threshold mature?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q71. Can users upload once and reliably query the same document next week?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Not as a mature persistent document-index feature.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q72. Why not silently fall back to Chat if Qdrant fails?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Because that removes document grounding while the user may think the answer still came from the PDF.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q73. How would you improve RAG?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Persistent document metadata, page/chunk metadata, retrieval evaluation, thresholds/reranking where justified, citations, cleanup and authorized reuse.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q74. How would you test RAG?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Use representative documents/questions and inspect extraction, retrieved chunks, groundedness and failure behavior.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# PDF Generation

## Q75. Walk me through PDF Generation.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The workflow generates structured document content with an LLM, parses it, renders the binary PDF using PDFKit, uploads it to S3 and returns a presigned URL.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q76. Is PDF Generation the same as PDF RAG?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. Generation creates a new document; RAG answers questions about an uploaded document.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q77. What does PDFKit do?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It renders the actual PDF binary.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q78. Does the LLM directly create the PDF binary?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. It creates content; PDFKit creates the file.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q79. Where is the generated PDF stored?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> S3.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q80. How is it delivered?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Through a presigned URL.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q81. What can fail before rendering?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> LLM generation or structured-content parsing.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q82. What can fail after rendering?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> S3 upload or URL generation.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q83. Give a partial-success example.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The PDF is rendered successfully but the S3 upload fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q84. How would you retry safely?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Retry only the failed upload stage if the rendered file is still available and the operation is idempotent.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q85. What should Production V2 persist?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Artifact ID, owner, conversation, S3 key, type, status and retention metadata.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# PPT Generation

## Q86. Walk me through PPT Generation.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The workflow generates structured slide content, parses it, uses PptxGenJS to build the PPTX, uploads it to S3 and returns a presigned URL.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q87. What renderer is used?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> PptxGenJS.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q88. Does the LLM create the PPTX binary?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. It generates slide content; PptxGenJS renders the file.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q89. What is the current slide pattern?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Approximately a cover, six content slides and a closing slide.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q90. Where is the PPT stored?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> S3.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q91. What can break the workflow?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Malformed structured content, renderer errors, S3 upload failures or expired access URLs.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q92. How is PPT Generation different from Coding?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> PPT Generation creates a binary presentation artifact, while Coding returns structured source files for frontend display/preview.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q93. What would you validate before rendering?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Slide titles, body fields, length limits and required schema.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q94. How would you test PPT Generation?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Check valid content, malformed content, renderer failure, S3 failure and output-file integrity.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Image Generation

## Q95. Walk me through Image Generation.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The workflow prepares/expands the prompt, calls Stability AI, receives image bytes, uploads the generated image to S3 and returns access information.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q96. Which provider is used?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Stability AI.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q97. What endpoint family is verified?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `stable-image/generate/core`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q98. Does Gemini generate images in the current project?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q99. What can fail?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Prompt/provider rejection, timeout, invalid bytes, S3 upload or presigned URL generation.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q100. Why upload to S3?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> To separate generated artifacts from container-local storage and provide durable object storage.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q101. Does a successful Stability call guarantee the user gets the image?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. S3 upload or URL generation can still fail.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q102. Would Image Generation be a candidate for async jobs?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Potentially yes for long-running workloads, but async workers are not currently verified.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q103. How would you monitor it?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Provider latency, generation error rate, S3 upload success, artifact size and workflow cost.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Image Analysis

## Q104. Walk me through Image Analysis.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The user uploads an image and asks a question, the backend prepares the image for Gemini multimodal analysis, Gemini returns a text response, the result is persisted/returned and the temporary upload is cleaned up.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q105. What model is used?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `gemini-2.0-flash`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q106. Is Image Analysis image-to-image?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. It is image plus prompt to text.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q107. Is Image Analysis the same as Image Generation?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q108. What can fail?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Upload handling, image preparation, provider call, response handling or cleanup.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q109. Can Gemini image analysis hallucinate?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q110. Why is cleanup important?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Temporary files can consume disk or retain sensitive user data.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q111. How would you test cleanup?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Force both success and failure paths and verify the temporary file is removed.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q112. What security concern exists with image content?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Images can contain misleading or prompt-injection-like text, and model output should remain bounded by application authorization.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# State and Persistence

## Q113. How do specialists use LangGraph state?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> They read common inputs such as prompt, user, conversation, file and selected workflow and write task-specific outputs such as response, search results, images or artifacts.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q114. Which fields are commonly written by Search?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `searchResults` and `response`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q115. Which field is central for Chat?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `response`, with conversation context loaded outside the graph state as needed.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q116. Which field is common for Coding/PDF/PPT outputs?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `artifacts`.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q117. Which field can Image Generation update?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> `images` and/or artifact-related output.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q118. Is graph state durable memory?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q119. Where is durable conversation history stored?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> MongoDB.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q120. What does Redis store?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Sessions, fast conversation context and counters.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q121. Is Redis LangGraph checkpointing?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q122. Does every specialist use the same memory behavior?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q123. Why can large state be a problem?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Memory, serialization and logging overhead.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q124. Should full file content be placed into logs?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Service-to-Service Integration

## Q125. Why does Agent call Chat?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> To persist and retrieve conversation/message data through the Chat service boundary.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q126. Why does Agent call Auth?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> For account/credit-related operations.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q127. Why does Billing call Auth?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> To update credits/plan after payment verification.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q128. What is the downside of Agent → Chat synchronous calls?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Latency and partial-failure coupling.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q129. What is the downside of Agent → Auth credit calls?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> AI execution can become inconsistent with account state if one side fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q130. What credit weakness was identified?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> In some paths, failure of the credit helper can allow provider work to continue.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q131. Why is that a cost-control risk?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Provider usage can occur even when the account operation failed.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q132. Would queues automatically solve this?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. They can improve delivery/retry patterns, but business consistency and idempotency still need explicit design.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q133. What should an internal service call carry?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Trusted authenticated identity/context, correlation ID and validated operation data.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q134. Is Cloud Map service discovery the same as internal authorization?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Artifacts and Files

## Q135. What is the difference between an uploaded file and a generated artifact?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Uploaded PDF/image is user input processed temporarily; generated PDF/PPT/image is application output stored as an artifact.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q136. Are uploaded PDFs stored in S3 as the primary RAG input lifecycle?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Not in the verified current RAG flow; temporary local processing is the supported claim.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q137. Which generated artifacts are stored in S3?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Generated PDFs, PPTs and images.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q138. What is a presigned URL?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> A temporary signed URL granting access to a private S3 object.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q139. Does URL expiry delete the object?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q140. What is wrong with storing only the URL forever?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The URL can expire while the object remains, breaking old conversation links.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q141. What should be stored instead?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Artifact metadata and the S3 object key, with a fresh URL generated after authorization.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q142. Are code artifacts handled identically to PDF/PPT/image artifacts?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q143. What lifecycle controls are missing?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Mature ownership metadata, retention, renewal and cleanup policies.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Failures and Reliability

## Q144. What is partial success?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> One stage succeeds but a later stage fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q145. Give a Search partial success.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Tavily succeeds but Groq fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q146. Give a RAG partial success.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Embeddings and retrieval succeed but final generation fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q147. Give a PDF partial success.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Rendering succeeds but S3 upload fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q148. Give an Image partial success.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Stability succeeds but S3 upload fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q149. Give a Chat partial success.

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> LLM succeeds but assistant persistence fails.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q150. Why not blindly retry the whole workflow?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It can repeat provider cost, credits, messages or artifacts.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q151. What is safe retry?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Retrying only when the failed stage is idempotent or its side effects are controlled.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q152. What is idempotency?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Repeated processing has the same effect as processing once.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q153. Which specialist operations especially need idempotency?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Credits, artifacts, messages and any future async jobs.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q154. What is a timeout?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> A maximum wait for an external dependency.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q155. Why do specialists need different timeout policies?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Search, embeddings, image generation and storage have different latency characteristics.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q156. What is a circuit breaker?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> A pattern that temporarily stops calls to a repeatedly failing dependency.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q157. Is it verified in the project?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q158. What is the current error-semantic weakness?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Some specialist exceptions can become normal assistant text, hiding technical failures.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Security

## Q159. Why should specialist tools be least-privileged?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> To reduce the blast radius if a prompt, model or workflow behaves incorrectly.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q160. Should Search have account-administration permissions?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q161. Should Image Generation have broad database permissions?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q162. What is prompt injection?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Untrusted input tries to manipulate model behavior or tool usage.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q163. Which workflows are exposed to prompt injection?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> At minimum user prompts, Search web content, PDF RAG document content and image-analysis content.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q164. Can CORS prevent prompt injection?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q165. Can a system prompt fully solve prompt injection?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q166. What must enforce authorization?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Deterministic server-side application logic.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q167. Can the LLM decide whether User A owns Conversation B?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q168. What is the main Coding security principle?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Generated code is untrusted and should not run directly in a trusted environment.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q169. What would a safe code sandbox need?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Isolation, resource limits, network controls, time limits and dependency restrictions.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Testing and Evaluation

## Q170. Why does each specialist need separate tests?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> They have different providers, inputs, outputs and failure modes.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q171. What should Chat tests cover?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Context, provider response, persistence and failure paths.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q172. What should Search tests cover?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Tavily, synthesis, empty/malicious results and partial failure.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q173. What should Coding tests cover?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Intent classification, schema validity, malformed model output and preview behavior.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q174. What should RAG tests cover?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Extraction, chunking, embeddings, retrieval relevance, groundedness and failure handling.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q175. What should PDF/PPT tests cover?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Structured content parsing, renderer success and S3 delivery.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q176. What should Image Generation tests cover?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Provider response, image bytes, S3 upload and access URL.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q177. What should Image Analysis tests cover?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Valid/corrupt images, model accuracy and cleanup.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q178. What is AI evaluation?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Measuring model/workflow quality on representative labeled examples, not only whether the API returned 200.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q179. Does NovaMind have a mature AI evaluation suite?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q180. How would you evaluate Search?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Retrieval usefulness, answer quality and source consistency.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q181. How would you evaluate RAG?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Retrieval relevance and answer groundedness/faithfulness.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q182. How would you evaluate Coding?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Schema validity and, in a future safe sandbox, compile/test success.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Performance Cost Scaling

## Q183. Why do workflows have different latency?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> They execute different numbers and types of external calls.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q184. Which is usually simpler, Chat or PDF RAG?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Chat is simpler because PDF RAG adds extraction, embeddings and vector retrieval.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q185. Why can Search be slower than Chat?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It adds web retrieval before synthesis.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q186. Why can PDF RAG be expensive?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It can embed many chunks and then call a language model.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q187. Why can repeated PDF uploads be wasteful?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The same document may be parsed and embedded repeatedly.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q188. How would persistent document indexes help?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Reuse prior embeddings instead of rebuilding them every time.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q189. Why can Image Generation be costly?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Image providers have separate usage pricing and can be slower than text generation.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q190. Can horizontal Agent scaling fix provider quota limits?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q191. Can horizontal scaling fix duplicate credit operations?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q192. When would you split a specialist into its own service?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> When it has clearly different scaling, runtime, security or deployment needs.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q193. When would you use an async worker?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> For long-running/retryable tasks where synchronous HTTP becomes unreliable.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q194. Is async processing implemented now?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q195. What should cost metrics capture?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Provider calls, tokens, embeddings, search calls, image generations, latency and workflow-level estimated cost.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Design Defense

## Q196. Why use multiple specialist workflows?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Because the project has genuinely different task types with different providers, tools and outputs.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q197. Why not use one LLM for everything?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It would simplify integration but may be a poor fit for embeddings, vision, image generation and coding-specific behavior.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q198. Why not make each specialist a service?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It would add network and deployment complexity without evidence that each needs an independent runtime boundary.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q199. Why keep specialists inside Agent?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> They share orchestration/state concerns and can remain application-level workflow branches.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q200. Why use different providers?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Task-specific capability fit.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q201. What is the cost of multi-provider design?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> More credentials, quotas, APIs, monitoring and failure modes.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q202. Why use S3 for generated files?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Durable object storage and controlled delivery via presigned URLs.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q203. Why use Qdrant for PDF RAG?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Semantic vector retrieval over embedded chunks.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q204. Why does Search chain retrieval and generation?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Tavily is good at current retrieval; the language model synthesizes a readable answer.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q205. Why not call Search RAG in every interview?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Web search + synthesis is the clearer description for this project; PDF RAG is the explicit vector-retrieval pipeline.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q206. What would you improve before adding more specialists?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Testing/evaluation, structured validation, authorization, observability, cost metrics and failure semantics.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q207. What is the strongest current specialist design choice?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Task-specific tools/providers behind bounded routing.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q208. What is the biggest specialist-layer weakness?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Operational maturity around validation, evaluation, failure handling and lifecycle consistency.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Pressure Questions

## Q209. Aren't your eight agents just functions?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> They are specialist workflows/functions inside one Agent service. I avoid pretending they are independent autonomous services; the value is task-specific orchestration, not the label.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q210. Why call them agents at all?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Because they sit inside a stateful routed AI workflow and use task-specific models/tools, but I prefer the more precise term specialist workflows.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q211. If Search is Tavily plus Groq, what's special about it?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The application coordinates retrieval, result handling, context construction, synthesis, credit behavior and persistence as one controlled workflow.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q212. If PDF RAG is predefined, is it agentic?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It is a bounded multi-step AI workflow. The agentic part of NovaMind is the stateful routing/tool orchestration, not autonomous planning.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q213. Why not use Gemini for everything?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> One-provider architecture could be simpler, but the current project uses different providers for different capabilities. The trade-off should be evaluated using quality, cost and reliability.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q214. Why not store every generated artifact in MongoDB?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Binary/object artifacts are a better fit for S3; MongoDB can store metadata if needed.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q215. Why not store every upload permanently?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Retention, privacy, cost and ownership should be designed explicitly; temporary processing is appropriate for current one-request workflows.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q216. If the model returns invalid JSON, isn't the system broken?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> That is a known structured-output risk. Production V2 should validate against schemas and repair/retry safely.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q217. If credits fail but the model still runs, isn't that a serious bug?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Yes, it is a cost/control weakness and should be fixed with stronger preauthorization/reservation or atomic ledger-style accounting.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q218. If Chat persistence fails after the answer, what does the user see?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> That depends on the current error path, but architecturally it is partial success and should be represented explicitly rather than silently treated as full success.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q219. Why not retry every provider failure three times?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Retries can amplify latency/cost and duplicate side effects. Retry policy must depend on failure type and idempotency.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q220. Why not always use a fallback provider?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> A fallback must preserve the workflow semantics, output format, safety and quality. Blind provider substitution can silently change behavior.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q221. Is the Search answer grounded in citations?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> The workflow uses search results as context, but mature citation alignment and fact checking are not verified.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q222. Is PDF RAG production-ready?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It is a real RAG implementation, but document lifecycle, OCR, citations, retrieval evaluation, reranking and persistent index management still need improvement.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q223. Is Coding production-ready?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> It demonstrates structured code generation, but lacks secure execution, full testing, repair loops and mature schema validation.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q224. Does Image Analysis guarantee correct interpretation?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q225. Does S3 make artifacts secure automatically?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> No. Ownership, bucket policy, presigned URL handling and lifecycle controls still matter.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q226. What workflow would you optimize first?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> I would measure latency, cost, usage and failure rate before deciding. PDF RAG and Search are natural candidates because they have multiple external stages.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q227. What would you build first in Production V2?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> Structured output validation, per-workflow tests/evals, timeouts/error semantics, stronger credit/accounting controls, artifact/document metadata and provider observability.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

## Q228. What is your one-line project defense?

**What the interviewer is testing:** Whether you can explain the actual specialist implementation, not just name a provider.

**Word-for-word answer:**

> NovaMind's Agent service uses bounded LangGraph routing to select one of eight specialist workflows, and each workflow integrates only the models, tools and data handling required for that task.

**Likely follow-up:** Be ready to explain **what data enters, which tool/model is called, what state changes, what can fail, what the trade-off is, and what you would improve in Production V2**.

**Defense reminder:** Keep workflow, model, provider, tool, service, data store and artifact responsibilities separate.

---

# Rapid-Fire Revision

**Q229. Number of specialists?**  
Eight.

**Q230. Chat provider?**  
Groq.

**Q231. Groq model ID?**  
`openai/gpt-oss-120b`.

**Q232. OpenAI API?**  
Not in the verified Groq path.

**Q233. Search tool?**  
Tavily.

**Q234. Search final synthesis?**  
Groq-backed language-model path.

**Q235. Tavily an LLM?**  
No.

**Q236. Coding access layer?**  
OpenRouter.

**Q237. Coding model?**  
`deepseek/deepseek-chat`.

**Q238. Coding temperature?**  
0.

**Q239. Coding max output?**  
About 2500 tokens.

**Q240. Coding output?**  
Structured `files[]`.

**Q241. Backend code execution?**  
No.

**Q242. PDF parser?**  
`pdf-parse`.

**Q243. RAG chunk size?**  
About 1000 characters.

**Q244. RAG overlap?**  
About 200 characters.

**Q245. Embedding model?**  
`gemini-embedding-001`.

**Q246. Vector DB?**  
Qdrant.

**Q247. Retrieved chunks?**  
Top five.

**Q248. RAG answer generation?**  
Groq-backed path.

**Q249. OCR?**  
No.

**Q250. Reranking?**  
No.

**Q251. Mature page citations?**  
No.

**Q252. PDF renderer?**  
PDFKit.

**Q253. PPT renderer?**  
PptxGenJS.

**Q254. Image-generation provider?**  
Stability AI.

**Q255. Image-analysis model?**  
`gemini-2.0-flash`.

**Q256. Generated PDF/PPT/image storage?**  
S3.

**Q257. Presigned URL permanent?**  
No.

**Q258. URL expiry deletes object?**  
No.

**Q259. Uploaded PDF/image primary path?**  
Temporary processing.

**Q260. Agent → Chat?**  
Conversation/message persistence.

**Q261. Agent → Auth?**  
Credit/account operations.

**Q262. All specialists same memory?**  
No.

**Q263. Search citations guaranteed?**  
No.

**Q264. Application credits equal dollar cost?**  
No.

**Q265. Specialists separate microservices?**  
No.

**Q266. Specialists inside Agent?**  
Yes.

**Q267. Async workers implemented?**  
No.

**Q268. Mature AI eval suite?**  
No.

**Q269. Best maturity phrase?**  
Production-oriented, not production-ready.

# Cross-Question Chain — Search

**Interviewer:** What does Search do?

> It retrieves current web results through Tavily and then uses the Groq-backed language-model path to synthesize the final answer.

**Interviewer:** Is Tavily the model?

> No. Tavily is the search tool.

**Interviewer:** Do you guarantee citations?

> No. The project uses search context, but mature citation alignment and fact checking are not verified.

**Interviewer:** What if Tavily succeeds and Groq fails?

> That is partial success: retrieval succeeded but synthesis failed.

---

# Cross-Question Chain — Coding

**Interviewer:** What model generates code?

> DeepSeek `deepseek/deepseek-chat` through OpenRouter.

**Interviewer:** Why structured output?

> The frontend needs a machine-readable files array for Monaco and browser preview.

**Interviewer:** What if JSON is invalid?

> Parsing can fail. Production V2 should add schema validation and safe repair/retry.

**Interviewer:** Does it compile and test the code?

> No, not through a complete secure backend compile/test/repair system.

---

# Cross-Question Chain — PDF RAG

**Interviewer:** Which model creates embeddings?

> Gemini `gemini-embedding-001`.

**Interviewer:** What does Qdrant do?

> Stores vectors and retrieves the top relevant chunks.

**Interviewer:** Who generates the answer?

> The Groq-backed language-model path.

**Interviewer:** Does RAG eliminate hallucination?

> No.

**Interviewer:** Can I upload a PDF once and ask questions next week?

> Not as a mature persistent knowledge-base feature in the current implementation.

---

# Cross-Question Chain — Artifacts

**Interviewer:** How do users receive generated PDFs?

> The content is rendered with PDFKit, uploaded to S3 and exposed through a temporary presigned URL.

**Interviewer:** What happens when the URL expires?

> The URL stops working; the S3 object may still exist.

**Interviewer:** How would you fix old broken links?

> Persist artifact ownership metadata and the S3 key, then reauthorize and generate a new presigned URL.

---

# 30-Second Interview Answer

> NovaMind has eight specialist workflows inside one Agent service. LangGraph routes each request to the appropriate specialist. Chat uses Groq, Search uses Tavily followed by Groq synthesis, Coding uses DeepSeek through OpenRouter, PDF RAG uses Gemini embeddings with Qdrant retrieval and Groq generation, PDF/PPT generation use PDFKit or PptxGenJS with S3, Image Generation uses Stability AI, and Image Analysis uses Gemini. Each workflow updates task-specific LangGraph state and persists messages or artifacts where required.

---

# 60–90 Second Interview Answer

> The Agent service does not use one general model path for every request. LangGraph routes the request to one of eight predefined specialists, and each specialist has task-specific integrations. Chat uses conversation context with a Groq-backed model. Search calls Tavily for current web information and then passes those results to Groq-backed synthesis. Coding first determines coding intent and then calls DeepSeek through OpenRouter, expecting a structured files array. PDF RAG extracts and chunks the uploaded PDF, creates Gemini embeddings, retrieves the top five chunks from Qdrant and uses Groq to generate the answer. PDF and PPT generation use LLM-generated structured content followed by PDFKit or PptxGenJS and S3 delivery. Image Generation uses Stability AI, while Image Analysis uses Gemini.
>
> The benefit is specialization and clearer tool boundaries. The trade-off is more routing, provider dependencies, partial-failure cases, different cost/latency profiles and more testing/observability work.

---

# Final Defense Rules

Always distinguish:

```text
Specialist Workflow ≠ Microservice
Provider ≠ Model
Tool ≠ Model
Qdrant ≠ RAG
Tavily ≠ LLM
PDF RAG ≠ PDF Generation
Image Analysis ≠ Image Generation
S3 Object ≠ Presigned URL
Application Credit ≠ Provider Dollar Cost
```

Do not say:

- “Every specialist has its own ECS service.”
- “All agents share the same long-term memory.”
- “Search gives verified citations.”
- “RAG completely prevents hallucinations.”
- “Coding runs and fixes the project automatically.”
- “Uploaded PDFs are a persistent knowledge base.”
- “Presigned URL expiry deletes the artifact.”
- “Every provider failure automatically falls back safely.”
- “The project has mature per-agent evaluation.”
- “The agent layer is production-ready.”

---

# Final Self-Test

Before Module 08, explain without notes:

- all eight specialists
- exact provider/tool for each
- Chat memory behavior
- Search-to-Groq chain
- Coding intent + OpenRouter/DeepSeek
- structured files output
- PDF extraction/chunking/embeddings/Qdrant/generation
- PDF/PPT renderers
- image generation vs analysis
- Agent → Chat
- Agent → Auth
- credit weakness
- state updates
- artifact storage
- presigned URL lifecycle
- temporary upload handling
- partial failure
- safe retry/idempotency
- specialist-specific testing
- security risks
- latency/cost differences
- scaling limits
- Production V2 priorities

**Module 07 interview preparation complete.**
