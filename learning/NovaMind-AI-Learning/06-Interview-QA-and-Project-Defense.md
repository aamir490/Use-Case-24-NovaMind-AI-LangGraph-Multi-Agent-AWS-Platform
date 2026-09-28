# Module 06 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** LangGraph State, Nodes, Edges and Routing  
> **Purpose:** Prepare for detailed LangGraph interviews while defending only what the verified NovaMind implementation supports.

---

## Accuracy Rules

Confidently say:

```text
LangGraph is genuinely implemented.
It is inside the Agent service.
The graph routes to 8 predefined specialist workflows.
Explicit non-Auto selection has highest priority.
PDF in Auto → PDF RAG.
Image in Auto → Image Analysis.
Otherwise model-based classification is used.
Unknown classifier labels can fall back to Chat.
Graph state carries prompt/response/user/conversation/file/search/image/artifact data.
```

Do not claim:

```text
LangGraph checkpointing
Autonomous planner
Reflection/self-critique loop
Unrestricted repeated tool-selection loop
Eight separate ECS agent services
Fully autonomous multi-agent collaboration
```

Important nuance:

```text
Unknown classifier label → Chat fallback
Classifier exception → no mature universal fallback
```

---

## Practice Method

For every question:

1. Define the LangGraph concept.
2. Map it to NovaMind.
3. Explain the exact request flow.
4. Mention one limitation or trade-off.
5. Be ready for a debugging or pressure follow-up.

---

# Foundations

## Q1. What is LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> LangGraph is a framework for building stateful workflows as graphs made of nodes, edges and shared state.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q2. Why would you use LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It makes state, routing and conditional workflow structure explicit, which becomes useful as workflows grow beyond simple sequential functions.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q3. What is a graph in LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A graph is the workflow definition that connects nodes through edges and controls how execution moves from START to END.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q4. What is a node?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A node is a unit of work that reads graph state, performs some logic, and can return state updates.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q5. What is an edge?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> An edge defines which node should execute next.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q6. What is a conditional edge?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A conditional edge chooses the next node based on state or routing logic.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q7. What are START and END?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> START represents graph entry and END represents completion of graph execution.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q8. What is state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> State is the structured data carried through one graph execution and shared between nodes.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q9. Does LangGraph itself generate text?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. LangGraph orchestrates workflow execution; external models/providers generate model output.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q10. Is LangGraph itself an agent?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. It is a framework that can be used to build workflows and agents.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q11. Does using LangGraph automatically make a system autonomous?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Autonomy depends on graph design, planning, loops, tools and control logic.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q12. Can a simple if/else replace LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> For simple routing, yes. LangGraph becomes more useful when stateful conditional workflows grow in complexity.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# NovaMind Graph Architecture

## Q13. Where is LangGraph implemented in NovaMind?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Inside the Agent service.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q14. What is the main role of LangGraph in NovaMind?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It carries request state and routes execution to one of eight predefined specialist workflows.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q15. How many specialist workflows are there?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Eight.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q16. Name the eight specialists.

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Chat, Search, Coding, PDF RAG, PDF Generation, PPT Generation, Image Generation and Image Analysis.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q17. Are these eight separate microservices?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. They are workflows inside the Agent service.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q18. Are these eight separate ECS services?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q19. What is the simplified graph shape?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> START → Router → one specialist workflow → END.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q20. Is the graph bounded?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes. Routes are constrained to predefined workflow options.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q21. Does the graph dynamically create new agents?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q22. Does it have a general planner?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q23. Does it have a reflection loop?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q24. Does it have unrestricted repeated tool selection?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q25. Does it use LangGraph checkpointing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q26. Can you still call it agentic?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes, in a bounded sense because it uses state, routing and multi-step specialist workflows.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q27. What is the best description?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A bounded LangGraph-orchestrated multi-specialist AI system.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# State

## Q28. What state fields are verified in NovaMind?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Prompt, response, selected workflow/agent, conversation ID, user ID, search results, images, artifacts and file.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q29. Why keep prompt in state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because downstream nodes need access to the user's request.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q30. Why keep conversationId in state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> So specialist workflows can associate work with the correct conversation.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q31. Why keep userId in state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> So downstream logic can associate the request with the authenticated user, while authorization must still be enforced by application logic.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q32. Why keep searchResults in state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> So the Search workflow can pass retrieved web information into the synthesis step.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q33. Why keep artifacts in state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> So document/code/image workflows can return generated artifact metadata to later handling or the final response.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q34. Why keep file in state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because file-aware workflows such as PDF RAG and Image Analysis need access to uploaded input.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q35. Can state be updated by nodes?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes. Nodes can read existing fields and return new or modified fields.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q36. Is state long-term memory?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q37. Is state automatically durable?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q38. Does state survive Agent service crashes?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Not through verified LangGraph checkpointing.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q39. Could large state be a problem?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes. Large files or intermediate results can increase memory, serialization and logging risk.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q40. Should full state be logged?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Sensitive or large content should be avoided; use safe metadata and correlation IDs.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q41. Can state contain untrusted values?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes, which is why identity and authorization cannot rely solely on arbitrary state fields.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q42. What would state schema validation improve?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It would reduce invalid route labels, malformed fields and inconsistent node assumptions.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# State vs Memory

## Q43. How is LangGraph state different from Redis?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> LangGraph state is current graph execution data. Redis stores application sessions, conversation context and counters.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q44. How is LangGraph state different from MongoDB?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> MongoDB stores durable application data such as conversations/messages, while LangGraph state coordinates the current request.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q45. Is Redis a LangGraph checkpointer in this project?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q46. Is MongoDB used as a LangGraph checkpointer?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q47. What is checkpointing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Persisting graph execution state so an interrupted workflow can resume later.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q48. Why is checkpointing useful?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> For long-running workflows, human approval, crash recovery and resumability.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q49. Why might checkpointing add complexity?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It introduces storage lifecycle, state versioning, cleanup, security and replay concerns.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q50. Does NovaMind have durable graph resume?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No, not through a verified LangGraph checkpointer.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q51. Does conversation history persistence equal graph persistence?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Conversation history can survive while an in-flight graph execution is lost.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q52. Could Redis still survive a process restart?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Potentially, because it is external application storage, but that does not make graph execution resumable.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q53. What would Production V2 add for durable workflows?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A supported LangGraph checkpointer plus durable job IDs, retryable stages and clear state lifecycle.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Routing Priority

## Q54. What is NovaMind's first routing priority?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> An explicit non-Auto workflow selection.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q55. Why does explicit selection win?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because the user's intent is already known, so classification is unnecessary.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q56. What happens with a PDF in Auto mode?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It routes to PDF RAG.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q57. What happens with an image in Auto mode?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It routes to Image Analysis.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q58. What happens when no explicit/file rule applies?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The system uses model-based classification.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q59. What happens with an unknown classifier label?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It can fall back to Chat.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q60. What happens if the classifier throws an exception?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> There is no mature universal fallback for every classifier exception.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q61. Why is deterministic routing used before classification?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It reduces latency, cost and classification error when a reliable signal already exists.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q62. What is the difference between unknown label and classifier exception?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Unknown label means classification returned a value the router did not recognize; exception means the classification call itself failed.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q63. Why is that distinction important?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because the project handles unknown labels more gracefully than classifier exceptions.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q64. Could a user override Auto routing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes, explicit workflow selection takes priority.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q65. Does PDF upload always mean PDF Generation?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. In Auto mode, uploaded PDF means PDF RAG.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q66. Does image upload always mean Image Generation?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. In Auto mode, uploaded image means Image Analysis.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q67. How would you improve routing reliability?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Add structured route labels, validation, evaluation datasets, route metrics and explicit fallback/error handling.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q68. How would you test route priority?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Create cases for explicit selection, PDF Auto, image Auto, classifier route, unknown label and classifier failure.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Router and Conditional Edges

## Q69. What does the Router node do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It inspects state and returns the route that determines the specialist workflow.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q70. Does the Router generate the final answer?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q71. What does a conditional edge do after Router?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It maps the route label to the corresponding specialist node.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q72. What happens if a route label is mapped incorrectly?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A valid classifier result can still execute the wrong specialist.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q73. How would you test conditional edges?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Feed known route labels and assert they transition to the expected nodes.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q74. Why separate router and specialist logic?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It isolates intent selection from task execution and keeps specialist workflows focused.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q75. Could the Router itself call tools?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It could in a general design, but NovaMind's key verified role is workflow selection.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q76. Is model-based routing the same as planning?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Routing selects among predefined paths; planning can create or revise multi-step plans.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q77. Is routing the same as tool selection?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Routing selects a workflow; tools are generally used inside the selected specialist.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q78. Could a deterministic router be safer than an LLM router?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes, when rules are reliable because behavior is more predictable and testable.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q79. When is a model router useful?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> When intent is ambiguous and cannot be reliably inferred from explicit metadata or file type.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Specialist Nodes

## Q80. What does Chat do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It handles general conversation and language generation through the Groq-backed model path.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q81. What does Search do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It calls Tavily for web retrieval and then uses language-model synthesis.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q82. What does Coding do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It uses coding-intent logic and calls DeepSeek through OpenRouter for structured files output.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q83. What does PDF RAG do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It extracts/chunks PDF text, creates Gemini embeddings, retrieves from Qdrant and generates an answer through the Groq-backed path.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q84. What does PDF Generation do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It generates structured content, renders a PDF with PDFKit and stores the artifact in S3.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q85. What does PPT Generation do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It generates structured slide content, renders with PptxGenJS and stores the artifact in S3.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q86. What does Image Generation do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It calls Stability AI, stores the generated image and returns access information.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q87. What does Image Analysis do?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It sends the uploaded image and question to Gemini and returns a text analysis.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q88. Does every specialist use the same provider?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q89. Does every specialist use conversation history in the same way?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q90. Does every specialist generate text?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Some produce files or images.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q91. Does every specialist persist artifacts in S3?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. S3 artifact behavior is mainly for generated files/images, while code artifacts are handled differently.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q92. Why are specialists useful?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> They allow task-specific prompts, providers, tools and output handling.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q93. What is the trade-off of specialists?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> More routing complexity, more code paths and more failure modes.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# LangGraph vs Plain Code

## Q94. Could you implement NovaMind's routing without LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes. A switch/if-else router could handle basic branches.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q95. Then why use LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It gives explicit state, graph structure and conditional transitions that become useful as workflows grow.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q96. What is the main benefit for maintainability?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The workflow topology is easier to reason about than scattered nested control logic.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q97. What is the main cost?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Framework abstraction and graph-specific debugging complexity.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q98. When is LangGraph overkill?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> When the application has only a few simple deterministic steps and no meaningful stateful branching.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q99. When does LangGraph become more valuable?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> When there are multiple conditional branches, shared state, loops, human approval or durable execution needs.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q100. Does using LangGraph guarantee good architecture?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Poorly designed nodes, state and error handling can still create a bad system.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q101. Would you remove LangGraph if workflows stayed simple?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> I would evaluate whether its state/graph benefits still justify the complexity.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q102. Does LangGraph replace Express?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Express handles HTTP/service APIs; LangGraph handles internal AI workflow orchestration.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q103. Does LangGraph replace MongoDB/Redis?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Loops and Cycles

## Q104. Can LangGraph support cycles?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q105. What is a cycle?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A graph path that returns execution to an earlier node.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q106. Give a general reflection-loop example.

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Generate → Critic → if weak, revise → Critic again → END when acceptable.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q107. Does NovaMind implement that?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q108. Why are loops risky?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> They can increase cost, latency and the risk of infinite or repeated execution.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q109. What controls should an open-ended loop have?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Maximum steps, maximum tool calls, timeouts, token/cost budgets and explicit stopping conditions.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q110. Does NovaMind have unrestricted agent loops?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q111. Is Search-to-Chat a loop?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. It is a bounded chain/handoff-like sequence.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q112. Is PDF RAG a loop?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. It is a multi-step workflow but not an open-ended cycle.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q113. Would adding reflection automatically improve quality?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. The critic can be wrong and adds cost/latency.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Tools

## Q114. What is a tool node in general?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A graph node designed to execute external tools or tool calls.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q115. Does NovaMind have a generic unrestricted tool node loop?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q116. How are tools used instead?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> They are mostly bound to specialist workflows.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q117. What tool does Search use?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Tavily.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q118. What data/tool service does PDF RAG use?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Qdrant plus Gemini embeddings.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q119. What provider does Image Generation use?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Stability AI.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q120. Why is bounded tool access useful?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It improves predictability, least privilege and cost control.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q121. Could a tool result be malicious?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes. Web and document content should be treated as untrusted data.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q122. Should a model decide authorization for tools?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Authorization should be deterministic server-side logic.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q123. What is tool argument validation?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Validating tool inputs against schema, permissions and safe bounds before execution.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Errors and Failure Propagation

## Q124. What can fail before the graph starts?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Gateway/session/request validation or Agent-service reachability.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q125. What can fail in Router?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> State assumptions, classifier request, invalid route label or mapping.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q126. What can fail in Search?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Tavily retrieval, response parsing or later Groq synthesis.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q127. What can fail in PDF RAG?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> PDF parsing, embeddings, Qdrant retrieval or answer generation.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q128. What can fail in Coding?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Intent classification, OpenRouter/DeepSeek call or structured-output parsing.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q129. What can fail in document generation?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> LLM content generation, JSON parsing, renderer or S3 upload.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q130. What is partial success?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> An earlier stage succeeds but a later stage fails.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q131. Give a Search partial-success example.

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Tavily succeeds but Groq synthesis fails.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q132. Give an artifact partial-success example.

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> PDF rendering succeeds but S3 upload fails.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q133. Does LangGraph automatically make multi-step operations atomic?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q134. Why can blind retries be dangerous?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Earlier steps may already have caused side effects or provider cost.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q135. What is safe retry?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Retrying only when the operation is idempotent or side effects are known and controlled.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q136. What is idempotency?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Repeating the same logical request does not duplicate its side effect.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q137. Does LangGraph itself guarantee idempotency?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q138. What is wrong with converting exceptions into normal assistant text?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Monitoring and callers may treat technical failure as successful execution.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q139. What should Production V2 improve?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Structured errors, explicit timeouts, safe retries, idempotency and stage-aware recovery.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Debugging

## Q140. How do you debug a LangGraph request?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Inspect input state, router decision, selected node, dependency calls, state updates, final response and errors.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q141. How do you debug wrong routing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Check explicit selection, Auto mode, file metadata, classifier input/output and route mapping.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q142. How do you debug a graph that stops unexpectedly?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Find the last node that started/completed and inspect its error/dependency logs.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q143. How do you debug a slow graph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Measure router time, specialist stages, provider latency, persistence and serialization separately.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q144. Why is end-to-end latency alone insufficient?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It does not identify which node or dependency is slow.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q145. What is a correlation ID?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A request identifier propagated through services and logs.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q146. Why is it useful?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It lets you reconstruct one request across Gateway, Agent, Chat and provider calls.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q147. Is mature distributed tracing verified?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q148. What should be logged at graph level?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Route, node start/end, stage duration, safe identifiers, provider status and sanitized error data.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q149. What should not be logged blindly?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Full prompts, files, secrets, tokens or sensitive full state.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q150. How do you debug classifier fallback?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Test the classifier result separately, then verify unknown-label mapping and exception behavior.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Observability

## Q151. What graph metrics would you track?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Route counts, route accuracy, node latency, error rate, fallback rate, provider latency and workflow success.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q152. Why track route distribution?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It reveals usage patterns and unexpected routing shifts.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q153. Why track fallback rate?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A rising fallback rate can indicate classifier or prompt issues.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q154. Why track per-node latency?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It identifies the slow stage in a multi-step workflow.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q155. Why track provider-specific errors?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Different providers have independent reliability and quota behavior.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q156. Why track workflow-level cost?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A graph can create several model/tool calls from one user request.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q157. Does CloudWatch logging equal full observability?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q158. What is tracing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Following one request across multiple nodes/services with timing and causality.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q159. What is an SLO?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A measurable reliability target such as success rate or latency percentile.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q160. Are graph SLOs verified in NovaMind?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Testing and Evaluation

## Q161. What should a Router unit test verify?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Given known state, the router returns the expected route label.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q162. What should an edge test verify?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Each route label maps to the intended specialist node.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q163. What should a state test verify?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Nodes read/write expected fields without corrupting unrelated state.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q164. What should an unknown-label test verify?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It falls back to Chat.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q165. What should a classifier-exception test verify?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The system returns a controlled failure or explicit fallback according to the intended Production V2 policy.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q166. How would you test PDF Auto routing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Provide Auto + PDF and assert the classifier is bypassed and PDF RAG is selected.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q167. How would you test Image Auto routing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Provide Auto + image and assert Image Analysis is selected.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q168. How would you test explicit selection priority?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Set a non-Auto selection and verify it wins even if a file is present, according to the project's routing rules.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q169. How would you evaluate routing quality?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Use a labeled dataset of prompts/files and compare actual vs expected specialist.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q170. Does NovaMind have a mature routing evaluation suite?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q171. How do you test failure handling?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Inject provider/data-store failures and verify errors, cleanup and safe retry behavior.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q172. How do you regression-test graph changes?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Run the same labeled routing and workflow cases after state/node/edge changes.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q173. Why test graph topology?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> A small route-map change can silently send requests to the wrong specialist.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Scaling and Performance

## Q174. Does LangGraph itself scale the application?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q175. What scales the Agent service?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Its runtime/container deployment, such as ECS task count, subject to dependencies and quotas.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q176. Can more Agent tasks solve provider quotas?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q177. Can more Agent tasks solve Redis races?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q178. Can more Agent tasks solve payment consistency?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q179. What happens to an in-flight graph if its task crashes?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Without checkpointing, that execution is lost.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q180. Can external state survive the crash?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> MongoDB/Redis/S3 data already written may survive, depending on the external service.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q181. Why can state size hurt performance?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Large state increases memory use and data movement between nodes.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q182. How can deterministic routing improve performance?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It avoids an unnecessary classifier call.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q183. How can persistent RAG indexes improve performance?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> They avoid repeated document extraction/embedding for the same document.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q184. Could some graph work be parallelized?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes if branches are independent and side effects are controlled, but this is not a major verified current pattern.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q185. Does NovaMind currently have a general parallel-merge graph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Security

## Q186. Can LangGraph replace authorization?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q187. Why not trust state.userId blindly?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because authorization depends on trusted authenticated identity and resource ownership, not merely a value in a state object.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q188. What is prompt injection risk in routing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Untrusted text could influence model-based classification or downstream model behavior.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q189. How does deterministic routing reduce some risk?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It limits model control when the route can be decided from trusted application metadata.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q190. What is least privilege for specialist nodes?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Each specialist should have only the tools/data permissions it needs.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q191. Should Search have billing-admin permissions?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q192. Should PDF RAG have unrestricted account mutation permissions?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q193. Can untrusted documents contain malicious instructions?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q194. Should those instructions override system/application rules?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q195. What protects secrets?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Server-side secret management and permission boundaries, not prompt instructions alone.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q196. Why avoid logging full state?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It can expose user content, files, identifiers and secrets.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q197. What security tests would you add?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Cross-user authorization tests, prompt-injection tests, tool-argument validation and malicious file/search-content tests.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Production V2

## Q198. What would you improve first in routing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Structured labels, validation, evaluation data, route metrics and a clear classifier-error policy.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q199. What would you improve first in state handling?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Typed/schema-validated state and clearer ownership of large/sensitive fields.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q200. When would you add checkpointing?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> For long-running, resumable or human-approved workflows.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q201. When would you add human-in-the-loop?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> For high-impact, expensive or sensitive actions where approval is useful.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q202. When would you add reflection?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Only when evaluation shows a measurable quality benefit.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q203. When would you add planning?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> When user goals require dynamic multi-step decomposition beyond predefined workflows.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q204. When would you add a supervisor?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> When one user goal needs several specialists dynamically coordinated.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q205. What reliability improvements matter?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Timeouts, idempotent retries, structured errors, circuit breakers where justified and correlation/tracing.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q206. What evaluation improvements matter?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Routing, retrieval, answer-groundedness, structured-output and failure-recovery evaluations.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q207. What deployment concern appears with durable checkpoints?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Graph/state versioning across application releases.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q208. What cost controls matter for more autonomous graphs?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Maximum steps, tool calls, time, tokens and workflow cost budgets.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q209. Why not add all of these immediately?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because each adds complexity and should be justified by real use cases and measured benefits.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Design Defense

## Q210. Why use deterministic routing before model classification?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It is cheaper, faster and more predictable when the route is already known from user selection or file type.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q211. Why use model classification at all?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It handles ambiguous requests that cannot be resolved deterministically.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q212. Why fall back unknown labels to Chat?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Chat is the most general text workflow and provides a safe generic route for unrecognized classifier labels.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q213. Why isn't classifier exception handled the same way?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The current implementation does not have a mature universal exception fallback, which is a known reliability gap.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q214. Why keep eight specialists in one Agent service?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It avoids unnecessary network boundaries while still allowing task-specific workflow separation.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q215. Why not make each specialist a microservice?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> There is no demonstrated need for separate runtime scaling/deployment for every specialist, and doing so would add operational complexity.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q216. Why use LangGraph if the graph is bounded?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Bounded graphs still benefit from explicit shared state and conditional workflow structure.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q217. Why not let the model choose every tool and step?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Deterministic control is safer, cheaper and more testable for known workflows.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q218. What is the strongest advantage of the current graph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Predictable routing across real specialist workflows with explicit state.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q219. What is the biggest current graph weakness?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Lack of mature checkpointing, routing evaluation, graph-level observability and standardized error semantics.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q220. Would you call the graph production-ready?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. It is production-oriented but still needs stronger reliability, evaluation, security and observability.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q221. What is the key design principle?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Use model decisions only where they add value, and keep known application rules deterministic.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Pressure Questions

## Q222. Isn't this just a switch statement wrapped in LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The current router could partly be expressed with a switch, but LangGraph also gives explicit shared state and graph structure for multiple specialist workflows. I would not claim the framework is necessary for trivial routing; its value increases as the workflow grows.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q223. Why should an interviewer care that you used LangGraph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The important point is not the library name. It is that I understand stateful orchestration, routing, specialist boundaries, failure handling and the trade-off versus simpler control flow.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q224. If there is no checkpointing, what happens on crash?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The in-flight graph execution is not resumable through LangGraph. External writes that already completed may remain, so recovery must consider partial state.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q225. If Redis survives, why can't you resume the graph?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because application Redis context is not integrated as a LangGraph execution checkpointer.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q226. If an unknown label falls back to Chat, why not catch every classifier error and do the same?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> That is a reasonable Production V2 improvement, but fallback policy must be explicit because silently degrading may hide classifier/provider failures.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q227. Why not always route to Chat when anything fails?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Because some workflows have semantic guarantees. For example, falling back from PDF RAG to plain Chat would remove document grounding.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q228. Can LangGraph prevent hallucinations?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. It controls workflow execution; model correctness still depends on context, retrieval and model behavior.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q229. Can LangGraph prevent unauthorized access?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No. Authorization must be enforced in application services.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q230. Can LangGraph make payments atomic?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q231. Can LangGraph automatically retry safely?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It can be designed with retries, but safe retry still requires idempotent application logic.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q232. Why not add reflection now?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It adds model calls, latency and cost, and must be justified by evaluation.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q233. Why not add a planner now?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> The current tasks are largely known workflows. Open-ended planning would add complexity without clear need.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q234. Why not add checkpointing now?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It is useful for long-running workflows, but it adds persistence/versioning complexity. It should be introduced when resume semantics are needed.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q235. Does LangGraph make NovaMind multi-agent?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> It enables multi-workflow orchestration, but I describe NovaMind carefully as multi-specialist bounded orchestration rather than independent autonomous agents.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q236. What is one routing bug that could be expensive?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Misrouting a simple chat request into a more expensive specialist workflow can add unnecessary provider calls and cost.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q237. What is one routing bug that could be semantically dangerous?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Routing a PDF question to plain Chat could produce an answer that appears document-grounded when it is not.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q238. What is one state bug that could be security-sensitive?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Using an untrusted or wrong user/conversation identifier without ownership validation could expose another user's data.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q239. What would you show on a whiteboard?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> START, Router, routing priority, conditional edges to the eight specialists, state fields, END, and a separate box showing Redis/MongoDB are application persistence rather than LangGraph checkpointing.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q240. What would you improve before adding more graph complexity?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> Routing tests, typed state, standardized error handling, observability, security boundaries and AI evaluation.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

## Q241. What is your final one-line defense?

**What the interviewer is testing:** Whether you understand LangGraph as an orchestration framework and can connect the concept accurately to NovaMind's real graph.

**Word-for-word answer:**

> NovaMind uses LangGraph where it adds value—stateful bounded routing across specialist workflows—without pretending that framework usage alone makes the system autonomous.

**Likely follow-up:** Expect **why**, **what can fail**, **how would you test it**, **how is it different from memory/planning**, or **what would Production V2 improve**.

**Defense reminder:** Do not turn general LangGraph capabilities into claims that NovaMind currently implements them.

---

# Rapid-Fire Revision

**Q242. LangGraph?**  
Stateful graph/workflow orchestration framework.

**Q243. Node?**  
Unit of work.

**Q244. Edge?**  
Transition between nodes.

**Q245. Conditional edge?**  
Next-node choice based on state/route logic.

**Q246. START?**  
Graph entry.

**Q247. END?**  
Graph completion.

**Q248. State?**  
Current execution data shared across nodes.

**Q249. Router?**  
Node that selects specialist workflow.

**Q250. Specialists?**  
Eight predefined workflows inside Agent.

**Q251. Chat?**  
General text workflow.

**Q252. Search?**  
Tavily retrieval + LLM synthesis.

**Q253. Coding?**  
DeepSeek through OpenRouter.

**Q254. PDF RAG?**  
Extract → chunk → Gemini embeddings → Qdrant → Groq answer.

**Q255. PDF Generation?**  
LLM content → PDFKit → S3.

**Q256. PPT Generation?**  
LLM slides → PptxGenJS → S3.

**Q257. Image Generation?**  
Stability AI.

**Q258. Image Analysis?**  
Gemini.

**Q259. Explicit non-Auto selection?**  
Highest routing priority.

**Q260. PDF in Auto?**  
PDF RAG.

**Q261. Image in Auto?**  
Image Analysis.

**Q262. No deterministic signal?**  
Model-based classifier.

**Q263. Unknown classifier label?**  
Chat fallback.

**Q264. Classifier exception?**  
No mature universal fallback.

**Q265. LangGraph checkpointing?**  
Not implemented.

**Q266. Redis = checkpointing?**  
No.

**Q267. MongoDB = graph state?**  
No.

**Q268. Autonomous planner?**  
No.

**Q269. Reflection loop?**  
No.

**Q270. Unrestricted tool loop?**  
No.

**Q271. Eight ECS agent services?**  
No.

**Q272. Can normal JavaScript replace simple routing?**  
Yes.

**Q273. Why LangGraph then?**  
Explicit state and graph/conditional structure.

**Q274. Does LangGraph generate text?**  
No.

**Q275. Does LangGraph provide authorization?**  
No.

**Q276. Does LangGraph guarantee idempotency?**  
No.

**Q277. Does LangGraph guarantee correct answers?**  
No.

**Q278. Can graphs have cycles?**  
Yes generally.

**Q279. Does NovaMind have a general cycle/reflection loop?**  
No.

**Q280. Can more Agent tasks fix provider quotas?**  
No.

**Q281. What survives without checkpointing?**  
Only external writes already persisted; in-flight graph execution is not resumable.

**Q282. Best description?**  
Bounded stateful LangGraph routing to eight specialist workflows.

**Q283. Best routing principle?**  
Use deterministic rules first; use model decisions only when needed.

**Q284. Main graph maturity gaps?**  
Checkpointing, routing evaluation, graph observability and standardized failure semantics.

# Cross-Question Chain 1 — Explain the Graph

**Interviewer:** What does your LangGraph actually do?

> It carries request state and routes the request from a Router node to one of eight predefined specialist workflows.

**Interviewer:** How is the route selected?

> Explicit non-Auto selection wins first. In Auto mode, PDF routes to PDF RAG and image routes to Image Analysis. Otherwise the system uses model-based classification.

**Interviewer:** What if the classifier returns something unexpected?

> An unknown returned label can fall back to Chat. A classifier exception does not currently have a mature universal fallback.

**Interviewer:** What happens after the specialist?

> The workflow updates response, image, search-result or artifact state and the graph completes.

---

# Cross-Question Chain 2 — State vs Memory

**Interviewer:** What is LangGraph state?

> It is the structured data carried through the current graph execution, including prompt, response, user/conversation IDs, selected workflow, file, search results, images and artifacts.

**Interviewer:** Is Redis your LangGraph memory?

> No. Redis stores application sessions and fast context. It is not a verified LangGraph checkpointer.

**Interviewer:** Is MongoDB graph persistence?

> No. MongoDB stores durable application entities such as conversations and messages.

**Interviewer:** Can the graph resume after a crash?

> Not through a verified LangGraph checkpointing mechanism in the current implementation.

---

# Cross-Question Chain 3 — Why LangGraph?

**Interviewer:** Couldn't you implement this with if/else?

> Yes, basic routing could be written with ordinary JavaScript.

**Interviewer:** Then why LangGraph?

> It gives explicit state, nodes, edges and conditional routing, which becomes more valuable as workflows become stateful and multi-step.

**Interviewer:** Is it over-engineering?

> It would be if the workflow stayed trivial. The right question is whether the graph/state abstraction makes the current and expected workflow complexity easier to maintain.

---

# Cross-Question Chain 4 — Reliability

**Interviewer:** What happens if Tavily succeeds but Groq fails?

> Search retrieval succeeds but synthesis fails. That is partial success.

**Interviewer:** Can LangGraph automatically fix that?

> No. The application needs explicit timeout, retry and error behavior.

**Interviewer:** Why not retry the whole graph?

> Earlier steps may already have created side effects or provider cost. Safe recovery should retry only the failed idempotent stage where possible.

---

# Cross-Question Chain 5 — Autonomy

**Interviewer:** LangGraph is an agent framework, so is your graph autonomous?

> No. Framework capability and application behavior are different. NovaMind uses bounded routing to predefined workflows.

**Interviewer:** Do you have planning?

> No general autonomous planner.

**Interviewer:** Reflection?

> No verified reflection loop.

**Interviewer:** Repeated tool selection?

> No unrestricted open-ended tool loop.

---

# 30-Second Interview Answer

> NovaMind uses LangGraph inside the Agent service as a bounded stateful router. The graph carries request state and routes to one of eight predefined specialist workflows. Explicit user selection is checked first, then PDF/image file rules in Auto mode, and model-based classification is used only when those deterministic signals do not apply. Unknown classifier labels can fall back to Chat. The project does not use LangGraph checkpointing, autonomous planning, reflection or unrestricted repeated tool loops.

---

# 60–90 Second Interview Answer

> In NovaMind, LangGraph sits inside the Agent service. A request enters the graph with state containing values such as the prompt, user ID, conversation ID, selected workflow, optional file, and output fields such as response, search results, images and artifacts. The Router reads that state and applies an ordered routing policy.
>
> Explicit non-Auto workflow selection has the highest priority. In Auto mode, an uploaded PDF routes directly to PDF RAG and an uploaded image routes to Image Analysis. If there is no deterministic signal, the project uses model-based classification. The resulting label is mapped through conditional routing to one of eight specialist workflows. Unknown labels can fall back to Chat, while classifier exceptions still need a stronger universal fallback policy.
>
> I use LangGraph because it gives explicit state and graph structure for the specialist workflows, but I do not claim it is a fully autonomous graph. There is no verified planner, reflection loop, unrestricted tool loop or LangGraph checkpointing.

---

# 2–3 Minute Whiteboard / Project Defense

Draw:

```text
START
  ↓
Router
  ↓
Routing Priority
  ├── Explicit selection
  ├── PDF in Auto
  ├── Image in Auto
  └── Classifier
  ↓
Conditional Edges
  ├── Chat
  ├── Search
  ├── Coding
  ├── PDF RAG
  ├── PDF Generation
  ├── PPT Generation
  ├── Image Generation
  └── Image Analysis
  ↓
END
```

Then draw a separate State box:

```text
prompt
response
selected workflow
conversationId
userId
file
searchResults
images
artifacts
```

Then draw separately:

```text
Redis
→ sessions / fast context

MongoDB
→ durable conversations/messages

NOT LangGraph checkpointing
```

Say:

> The key point is that LangGraph state coordinates the current execution, while Redis and MongoDB are application storage layers. The graph itself is not durably checkpointed in the verified implementation.

---

# What Not to Say

Do not say:

- “Redis is our LangGraph checkpointer.”
- “The graph resumes automatically after a crash.”
- “All eight agents run as separate ECS services.”
- “LangGraph automatically chooses unlimited tools.”
- “The router creates new agents dynamically.”
- “The graph has autonomous planning.”
- “The graph reflects on every answer.”
- “LangGraph prevents hallucinations.”
- “LangGraph handles authorization.”
- “LangGraph makes retries automatically safe.”
- “Using LangGraph makes the system production-ready.”

Use:

> **bounded stateful routing**

> **eight predefined specialist workflows**

> **conditional edges**

> **application Redis/MongoDB persistence separate from graph state**

> **no verified LangGraph checkpointing**

---

# Final Self-Test

Before Module 07, you should be able to explain without notes:

- LangGraph
- graph
- node
- edge
- conditional edge
- START/END
- state
- state updates
- Router node
- routing priority
- explicit selection behavior
- PDF Auto routing
- image Auto routing
- model classification
- unknown-label fallback
- classifier-exception limitation
- all eight specialists
- LangGraph vs JavaScript if/else
- LangGraph vs LLM
- LangGraph vs agent
- state vs Redis
- state vs MongoDB
- checkpointing
- why Redis is not checkpointing
- cycles/loops
- tool nodes
- partial failure
- retry/idempotency
- debugging
- observability
- testing
- scaling
- security
- Production V2 improvements

**Module 06 interview preparation complete.**
