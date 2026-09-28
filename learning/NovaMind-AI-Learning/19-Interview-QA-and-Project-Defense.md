# Module 19 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Scalability, Performance, Cost and High Availability  
> **Purpose:** Prepare for architecture scaling, bottleneck, capacity, latency, unit-cost, HA, DR and pressure questions without overclaiming unmeasured production behavior.

---

## Accuracy Rules

### CURRENT VERIFIED

```text
Five separately containerized backend services:
Gateway, Auth, Chat, Agent, Billing

Eight specialist workflows inside Agent

Approx task definitions:
Gateway/Auth/Chat/Billing = 512 CPU / 1024 MiB
Agent = 1024 CPU / 2048 MiB

Synchronous AI/provider request paths
Redis / MongoDB / Qdrant / S3 dependencies
Groq / Gemini / OpenRouter / Tavily / Stability AI dependencies

Captured Redis configuration:
single-node / nonredundant / failover disabled

ECS task definitions in us-east-1
Qdrant endpoint configured in eu-west-1
```

### CURRENT GAPS

```text
No measured RPS/capacity benchmark
No verified p95/p99 baseline
No mature autoscaling evidence
No durable async queue/worker architecture
No mature backpressure/admission control
No verified current Multi-AZ HA
No verified redundant ECS desired count
No verified Redis failover
No verified MongoDB/Qdrant HA topology
No tested RTO/RPO
No tested DR
No exact cost-per-workflow ledger
No verified total monthly cost
No universal provider failover
```

### PRODUCTION V2 — PROPOSED

```text
Measurement-driven scaling
Workflow-specific metrics
ECS autoscaling
Async long-running jobs
Backpressure
Persistent PDF indexes
Cost-per-workflow telemetry
Right-sizing
Pagination/indexing
Redis correctness + failover
Multi-AZ service redundancy
Stateful HA verification
Backups / restore testing
RTO / RPO
Provider degradation/fallback
Failure testing
```

---

# Scalability Fundamentals

## Q1. What is scalability?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Scalability is the ability of a system to handle increasing workload without unacceptable degradation.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q2. What is vertical scaling?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Increasing CPU or memory of one task or instance.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q3. What is horizontal scaling?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Running more replicas of the service.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q4. What is elasticity?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Adjusting capacity up and down as demand changes.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q5. What is capacity?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> The amount of workload the system can handle while meeting acceptable performance/reliability.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q6. What is throughput?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> How much work completes per unit time.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q7. What is concurrency?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> How many operations are in progress at the same time.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q8. What is a bottleneck?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> The component or dependency that limits system performance.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q9. What is saturation?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> A resource approaching or exceeding its useful capacity.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# NovaMind Service Scaling

## Q10. How many separately containerized backend services exist?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Five: Gateway, Auth, Chat, Agent and Billing.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q11. Are the eight AI specialists eight ECS services?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No. They are inside the single Agent service.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q12. Which service has the largest configured CPU/memory?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Agent, at approximately 1024 CPU and 2048 MiB in the repository task definition.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q13. Does that prove Agent capacity?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No. Configuration is not a benchmark.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q14. Can you say one Agent task handles a specific number of users?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No, not without load testing.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Vertical vs Horizontal

## Q15. When would you scale vertically?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> When one task needs more CPU/memory and simplicity is valuable.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q16. What is vertical scaling's limitation?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Finite size ceiling and no redundancy by itself.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q17. When would you scale horizontally?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> When workload can be handled by multiple replicas and shared dependencies support it.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q18. Why might horizontal scaling fail to help?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> A shared dependency or provider quota may remain the bottleneck.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# ECS Scaling

## Q19. What is desired count?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> The number of ECS tasks the service tries to keep running.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q20. Is NovaMind's current desired count verified?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q21. What is ECS autoscaling?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Automatically adjusting desired count based on metrics/policies.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q22. Is mature autoscaling currently verified?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q23. What metrics can drive autoscaling?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> CPU, memory, ALB request count, queue depth or custom concurrency/latency metrics.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q24. Why can CPU be a poor Agent scaling metric?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Agent may be waiting on external providers with low CPU but high open-request concurrency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Statelessness

## Q25. Why are stateless services easier to scale?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Any replica can handle a request because durable state is external.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q26. Is NovaMind fully stateless?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q27. Why not?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> In-flight LangGraph state, local temp files and in-memory buffers exist, and no LangGraph checkpointing is implemented.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q28. Does MongoDB/Redis external state make workflow execution durable?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Agent Hot Spot

## Q29. Why is Agent a potential scaling hot spot?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> All eight AI workflows share the same service.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q30. Why not split all eight immediately?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> That adds operational complexity and should be justified by measured traffic, isolation and ownership needs.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q31. What is a noisy-neighbor risk?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> A heavy workflow can consume shared Agent resources and slow other workflows.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q32. What is a bulkhead?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Isolation that prevents one workload from exhausting all shared resources.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Synchronous vs Async

## Q33. What is the current pattern for many AI workflows?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Synchronous request-response.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q34. What is the downside?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Long provider work keeps HTTP requests open and consumes concurrency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q35. What is an async job model?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> API creates job → queue → worker → stored result/status.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q36. Which workflows could benefit?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Large PDF ingestion, PDF/PPT generation or image generation if requirements justify it.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q37. Are queues/workers current?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Backpressure

## Q38. What is backpressure?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Controlling incoming work when demand exceeds processing capacity.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q39. What can happen without backpressure?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Latency, timeouts, memory and connection pressure can cascade.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q40. How can you implement it?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Concurrency limits, queues, rate limits, admission control or load shedding.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q41. Is mature backpressure current?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Performance Fundamentals

## Q42. What is latency?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Time for one request to complete.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q43. What is throughput?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Work completed per unit time.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q44. What is response time?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Usually end-to-end user-visible latency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q45. What is queue time?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Time waiting before work starts.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q46. What is service time?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Time actually processing the operation.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q47. What is tail latency?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Latency experienced by the slowest part of the request distribution.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Percentiles

## Q48. What is p50?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Median latency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q49. What is p95?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> 95% of requests finish at or below that value.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q50. What is p99?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> 99% of requests finish at or below that value.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q51. Why not use average only?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Average can hide very slow tail requests.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q52. Does NovaMind have verified p95/p99 today?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Chat Performance

## Q53. What stages affect Chat latency?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Gateway, Redis session lookup, Agent/router, history, Groq, Redis update and Chat/MongoDB persistence.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q54. Why not automatically blame Groq?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Other stages may dominate latency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Search Performance

## Q55. Why can Search be slower than Chat?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> It adds Tavily retrieval before Groq synthesis plus other internal operations.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q56. What do you measure?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Tavily latency, Groq latency, persistence, credit operations and total latency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# PDF RAG Performance

## Q57. Why is current PDF RAG relatively expensive?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> It parses, chunks, embeds and creates a Qdrant collection in the request-oriented flow.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q58. What repeated work happens for the same PDF?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Parsing, chunking, embeddings and vector insertion can repeat.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q59. How would V2 improve it?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Persistent document identity/index mapping and embed-once reuse.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Provider Limits

## Q60. Why doesn't adding Agent tasks guarantee higher throughput?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Provider quotas and latency can remain the limiting factor.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q61. What can provider limits include?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Requests/minute, tokens/minute, concurrency and account quotas.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q62. What happens if provider quota is hit?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> 429/rate-limit failures or throttling.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Redis Scaling

## Q63. What does Redis support?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Sessions, conversation context/cache and rate counters.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q64. Why can Redis become a bottleneck?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> More app replicas can increase Redis concurrency and memory/connection pressure.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q65. Does scale-out fix Redis read-modify-write races?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q66. What current HA concern was captured?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> A single-node/nonredundant Redis setup with failover disabled in captured configuration.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# MongoDB Scaling

## Q67. What MongoDB scaling concerns matter?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Indexes, pagination, query shape, connection pools, aggregation and write contention.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q68. Why is missing pagination a problem?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Large result sets increase DB, memory and network work.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Qdrant Scaling

## Q69. What Qdrant concerns matter?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Collection growth, query latency, metadata filters, storage and lifecycle.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q70. What is a current lifecycle concern?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Request-oriented collections have no mature automatic cleanup lifecycle.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q71. What regional configuration is notable?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> ECS task defs point to us-east-1 while Qdrant endpoint is eu-west-1.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q72. Can you claim cross-region latency is currently a measured problem?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# S3 Performance

## Q73. Does S3 scale?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Yes, but application-side generation, buffering, upload and presigning can still be bottlenecks.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q74. Why can artifact flow be slow?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Rendering/provider work plus network upload and delivery.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Connection Pooling

## Q75. Why use connection pooling?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Reuse connections and avoid expensive connection setup per request.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q76. Which dependencies may benefit?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> MongoDB, Redis and outbound HTTP clients where supported.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q77. Do you know current exact pool sizes?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Caching

## Q78. What is caching?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Storing reusable data/results for faster future access.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q79. Can you blindly cache AI responses?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No, because context, freshness, privacy and nondeterminism matter.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q80. Is all Redis usage a cache?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Pagination

## Q81. What is pagination?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Returning data in bounded pages instead of all records.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q82. Why does it help?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Reduces DB, memory, network and UI latency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Performance Testing

## Q83. What is load testing?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Testing expected workload.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q84. What is stress testing?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Pushing beyond expected capacity.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q85. What is spike testing?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Sudden large traffic burst.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q86. What is soak testing?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Long sustained load.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q87. Does NovaMind have a mature load benchmark?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q88. What should be measured?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> RPS, concurrency, p50/p95/p99, errors, CPU/memory and dependency/provider latency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Capacity Planning

## Q89. How do you capacity-plan Agent?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Load-test representative workflows, measure concurrency/latency/resource usage and provider quotas, then add safety margin.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q90. Why not infer capacity from CPU/memory config?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Resource configuration alone does not show workload behavior.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q91. Should capacity be measured per workflow?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Yes, because workflows have very different cost/latency profiles.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Cost Fundamentals

## Q92. What is fixed/baseline cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Cost that exists even at low traffic.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q93. What is variable cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Cost that increases with usage.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q94. What is unit economics?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Cost per meaningful product unit such as one workflow request.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q95. Does NovaMind have a verified monthly total cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# AWS Cost Drivers

## Q96. What AWS cost drivers matter?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> ECS/Fargate, ALB, NAT, Redis, S3, CloudFront, CloudWatch and network transfer.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q97. Why can NAT be meaningful?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Hourly baseline plus data processing for outbound provider calls.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q98. Why can CloudWatch become costly?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> High log ingestion and retention.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q99. What is ECR cost trade-off with immutable releases?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> More images improve rollback but increase storage; lifecycle policies balance it.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Provider Cost Drivers

## Q100. What external cost drivers exist?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Groq, Gemini, OpenRouter, Tavily, Stability AI, Qdrant and embeddings/search/image usage.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q101. Why can one user request generate several costs?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Some workflows call multiple providers/tools.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q102. Give a Search example.

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Tavily retrieval plus Groq synthesis.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q103. Give a PDF RAG example.

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Gemini embeddings + Qdrant + Groq.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Credits vs Cost

## Q104. Are NovaMind credits equal to dollar cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q105. What are credits?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> An application usage/business mechanism.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q106. What is missing today?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> A verified per-request/provider/infrastructure dollar-cost ledger.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Routing Cost

## Q107. Can Auto routing add cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Yes, model-based classification can add another provider call.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q108. Can Coding add extra model calls?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Yes, it includes a coding-intent classification stage plus generation.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Cost Optimization

## Q109. What are the highest-value cost ideas?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Measure cost per workflow, avoid repeated PDF indexing, right-size tasks, tune logging/retention, optimize provider calls and evaluate NAT/region choices.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q110. Should you optimize purely for cheapest model?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No, quality/latency/reliability matter.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# High Availability Fundamentals

## Q111. What is high availability?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Designing the system to remain usable despite component failures.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q112. Scalability vs HA?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Scalability handles more load; HA survives failures.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q113. What is redundancy?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Having more than one component capable of serving.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q114. What is a single point of failure?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> A component whose failure can make the service unavailable.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q115. What is an Availability Zone?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> An isolated location inside an AWS Region.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q116. What is Multi-AZ?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Deploying redundant components across multiple AZs.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Current HA Boundary

## Q117. Can you claim NovaMind is currently Multi-AZ HA?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q118. Can you claim redundant desired counts?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q119. Can you claim Redis automatic failover?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q120. What captured Redis evidence exists?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Single-node/nonredundant with failover disabled.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q121. Can you claim zero downtime?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q122. Can you claim tested DR?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# ALB and ECS HA

## Q123. Does an ALB automatically make the app highly available?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q124. What else is needed?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Multiple healthy targets, appropriate placement and resilient dependencies.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q125. What could ECS do if one task fails?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Maintain desired count by starting replacement tasks, depending on service configuration.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q126. Is NovaMind's exact redundant task count verified?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Stateful HA

## Q127. Why is Redis important for HA?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> It affects sessions, context and rate limiting.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q128. What would Production V2 evaluate for Redis?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Replication, Multi-AZ and failover.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q129. Is MongoDB HA verified?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q130. Is Qdrant HA verified?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# External Provider HA

## Q131. Can AWS be healthy while NovaMind features fail?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Yes, if external providers fail.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q132. Does using multiple providers mean automatic failover?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q133. What would provider fallback require?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Compatible prompts/outputs, quality/cost testing, quota and explicit fallback logic.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Backup and DR

## Q134. Backup vs HA?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> HA keeps service available; backup helps recover lost/corrupted data.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q135. What is restore testing?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Proving a backup can actually be restored.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q136. What is RTO?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Target recovery time.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q137. What is RPO?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Acceptable data-loss window.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q138. Does NovaMind have verified RTO/RPO?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q139. Is tested disaster recovery verified?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Performance vs Cost Tradeoffs

## Q140. More tasks: benefit and cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> More parallel capacity/redundancy but higher compute cost.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q141. More redundancy: benefit and cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Better availability but higher infrastructure cost.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q142. More retrieved chunks: benefit and cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Potentially more evidence but more prompt size/noise/cost.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q143. Larger model: benefit and cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Potential quality improvement but possibly higher latency/cost.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario Traffic Doubles

## Q144. Traffic doubles. What do you do first?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Measure Gateway/Agent latency, concurrency, CPU/memory, Redis/Mongo/Qdrant and provider quotas.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q145. Do you scale everything immediately?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No, find the bottleneck first.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario Low CPU High Latency

## Q146. CPU is low but latency is high. What can cause it?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Waiting on providers, DB/vector/network/S3 or quota/throttling.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q147. What key lesson?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Low CPU does not mean spare end-to-end capacity.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario High CPU

## Q148. CPU is high. What do you inspect?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Parsing, rendering, serialization, request volume and inefficient code.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q149. Do you immediately increase CPU?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Not before profiling/measurement.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario High Memory

## Q150. Memory is high. What do you inspect?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Large file/image buffers, history, concurrency and leaks.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q151. Is more memory always the solution?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario Search Slow

## Q152. How do you debug slow Search?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Measure Tavily, Groq, persistence and credit-operation latency separately.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario RAG Slow

## Q153. How do you debug slow PDF RAG?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Measure parsing, chunk count, embeddings, Qdrant insert/retrieval, query embedding and Groq.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q154. What V2 improvement helps repeated use?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Persistent index reuse.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario Scale-Out No Gain

## Q155. You add Agent tasks but latency is unchanged. Why?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> A shared dependency/provider quota may be the real bottleneck.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q156. What phrase summarizes it?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Scaling the caller does not scale the dependency.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario Provider 429

## Q157. How do you handle provider 429s?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Respect limits/retry guidance, back off, control concurrency, queue suitable work and plan quota.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario AZ Failure

## Q158. Can you say NovaMind survives an AZ failure?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q159. What would you verify?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Task placement, ALB targets, Redis/database/Qdrant topology, NAT and external dependencies.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Scenario Cost Spike

## Q160. Cost suddenly increases. How do you investigate?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Break down compute, network, storage, logs and provider costs, then attribute by workflow.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q161. Why not blame ECS immediately?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Provider calls or repeated embeddings may dominate.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Production V2 Scaling

## Q162. What scaling improvements would you propose?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Measure first, then ECS autoscaling, workflow isolation where justified, async jobs, backpressure, DB pagination/indexing and persistent RAG indexing.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q163. What should be fixed before scaling Redis concurrency?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Race conditions/atomicity and TTL/memory behavior.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Production V2 Cost

## Q164. What cost telemetry would you add?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Workflow/provider/model/call counts/tokens where available and estimated cost per request.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q165. Why track cost per workflow?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> To understand unit economics and which features need optimization.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Production V2 HA

## Q166. What HA improvements would you propose?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Multiple tasks across AZs where justified, Redis failover, verified stateful HA, health/readiness, backups/restore and defined RTO/RPO.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q167. Would you implement multi-region immediately?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No, only if requirements and risk justify the complexity/cost.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Design Defense

## Q168. Why not call ECS automatically scalable?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> ECS can run replicas, but application/dependency capacity and concurrency correctness still determine scalability.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q169. Why not call AWS automatically highly available?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> AWS provides building blocks, but redundancy and failover must be configured and verified.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q170. Why not split every specialist service?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Operational complexity may outweigh benefit without measured need.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q171. Why not optimize only for cost?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Performance, reliability and quality trade-offs matter.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q172. Why not optimize only for latency?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> It may increase cost or reduce quality.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Pressure Questions

## Q173. How many users can NovaMind support?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> I cannot give a defensible number without load tests; I would measure workflow-specific concurrency, p95/p99 latency and dependency quotas.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q174. What is your current p95 latency?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Not measured/verified in the repository analysis.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q175. Is NovaMind autoscaling today?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Mature autoscaling is not verified.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q176. Is NovaMind highly available today?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> I would not claim mature HA; current evidence is insufficient and captured Redis configuration showed no redundancy/failover.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q177. Why is Agent the likely scaling focus?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> All eight AI workflows concentrate there, but the real bottleneck still must be measured.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q178. If Agent CPU is only 30%, can you cut tasks?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> Not based on CPU alone; concurrency/provider waits and tail latency may still require capacity.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q179. If Groq has a quota, can 20 Agent tasks bypass it?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q180. If Redis is single-node, what does that mean?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> It can be a single point of failure for sessions/context/rate limits.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q181. Can you claim current zero-downtime deployment/HA?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

## Q182. What is the strongest accurate scalability statement?

**What the interviewer is testing:** Whether you understand real scaling limits, dependency bottlenecks, measurement, cost and HA rather than assuming AWS automatically solves them.

**Word-for-word answer:**

> NovaMind has independently deployable backend services and externalized state, but measured capacity, autoscaling and dependency scaling remain Production V2 work.

**Likely follow-up:** I would explain **what I would measure, which dependency could become the bottleneck, whether the statement is verified, and what trade-off the proposed improvement introduces**.

**Project-defense reminder:** Configuration, scalability, performance and high availability are four different things.

---

# Rapid-Fire Revision

**Q183. Backend services?**  
Five.

**Q184. AI specialist services?**  
Eight workflows inside Agent, not eight ECS services.

**Q185. Agent configured resources?**  
Approx 1024 CPU / 2048 MiB.

**Q186. Config = capacity?**  
No.

**Q187. Vertical scale?**  
Bigger task.

**Q188. Horizontal scale?**  
More task replicas.

**Q189. Elasticity?**  
Adjust capacity with load.

**Q190. Throughput?**  
Work per time.

**Q191. Concurrency?**  
Work in progress simultaneously.

**Q192. Low CPU = low latency?**  
No.

**Q193. Autoscaling verified?**  
No.

**Q194. p95/p99 verified?**  
No.

**Q195. Queue architecture current?**  
No.

**Q196. Main provider quota rule?**  
More ECS tasks do not increase provider quota.

**Q197. RAG top-k?**  
Top 5.

**Q198. Persistent document index current?**  
No.

**Q199. Credits = dollar cost?**  
No.

**Q200. Total monthly cost verified?**  
No.

**Q201. Multi-AZ HA verified?**  
No.

**Q202. Redis failover verified?**  
No.

**Q203. Captured Redis topology?**  
Single-node/nonredundant, failover disabled.

**Q204. RTO/RPO verified?**  
No.

**Q205. DR tested?**  
No.

**Q206. Universal provider fallback?**  
No.

**Q207. Qdrant configured region?**  
eu-west-1.

**Q208. ECS task-def region?**  
us-east-1.

# Cross-Question Chain 1 — How Many Users?

**Interviewer:** How many concurrent users can NovaMind support?

> I cannot give a defensible number from the repository alone. The task CPU/memory settings show configuration, not measured capacity. I would load-test each major workflow, measure p50/p95/p99 latency, concurrency, resource utilization and provider quotas, then define capacity with a safety margin.

**Interviewer:** Why can't you estimate from ECS task size?

> Because AI requests are often network-bound and provider-bound. Two tasks with the same CPU can have very different throughput depending on Groq/Tavily/Qdrant latency and quotas.

---

# Cross-Question Chain 2 — Add More Agent Tasks

**Interviewer:** Why not simply scale Agent from 1 to 10 tasks?

> That may increase parallel request handling, but it does not scale Groq/Gemini/Tavily quotas, Redis, MongoDB or Qdrant. It can also increase concurrency against existing race conditions. I would identify the real bottleneck first.

---

# Cross-Question Chain 3 — Low CPU

**Interviewer:** Agent CPU is low, so can you scale in?

> Not based on CPU alone. Agent can be waiting on external providers with many concurrent open requests, so CPU can look low while latency and concurrency are high. I would also inspect active requests, p95 latency and provider wait time.

---

# Cross-Question Chain 4 — PDF RAG

**Interviewer:** Why is PDF RAG expensive?

> The current request-oriented implementation parses the PDF, chunks it, creates Gemini embeddings, creates a new Qdrant collection, stores vectors, embeds the question, retrieves top five chunks and then calls Groq. Re-uploading the same document can repeat much of that work.

**Interviewer:** How would you improve it?

> Give the document a durable identity, embed it once, persist owner/document-to-index mapping and reuse the index for later authorized questions.

---

# Cross-Question Chain 5 — Cost

**Interviewer:** Your app charges credits, so do you know your margin?

> Not from the current credit implementation alone. Credits are an application usage mechanism, not a verified dollar-cost ledger. I would track provider and infrastructure cost per workflow before making unit-economics claims.

---

# Cross-Question Chain 6 — HA

**Interviewer:** Is NovaMind highly available?

> I would not claim mature HA from the current evidence. The repository does not verify redundant task counts or Multi-AZ deployment, and a captured Redis configuration showed a single nonredundant node with failover disabled. I treat multi-AZ service redundancy and stateful failover as Production V2 work.

---

# Cross-Question Chain 7 — Provider Availability

**Interviewer:** You use several AI providers, so do you already have failover?

> No. Multiple integrations do not automatically create failover. Controlled failover requires explicit routing, compatible prompts/output contracts, quality testing, quota planning and cost analysis.

---

# Cross-Question Chain 8 — Cross Region

**Interviewer:** Qdrant is in eu-west-1 while ECS task definitions are us-east-1. Is that bad?

> It creates a potential cross-region latency and data-transfer dependency, but I would not call it a proven performance problem without measurement. I would compare measured retrieval latency and cost before changing regions.

---

# Bottleneck Walkthrough 1 — Traffic Doubles

```text
1. Check total RPS/concurrency.
2. Compare p50/p95/p99.
3. Check Gateway/Agent CPU and memory.
4. Measure provider latency and 429s.
5. Measure Redis/Mongo/Qdrant latency.
6. Check S3/file operations.
7. Identify saturation point.
8. Scale or optimize the bottleneck, not everything.
```

---

# Bottleneck Walkthrough 2 — CPU Low, Latency High

```text
CPU low
↓
Check active requests
↓
provider wait
↓
DB/vector latency
↓
network/NAT
↓
connection pool
↓
provider throttling
```

---

# Bottleneck Walkthrough 3 — PDF RAG Slow

```text
Upload
↓
pdf-parse time
↓
chunk count
↓
embedding time
↓
Qdrant insertion
↓
query embedding
↓
retrieval
↓
Groq answer

If repeated same document:
consider persistent indexing.
```

---

# Cost Analysis Walkthrough

```text
1. Choose workflow.
2. Count provider calls.
3. Measure tokens/embeddings where available.
4. Attribute ECS/NAT/storage/log usage.
5. Add vector/search/image provider cost.
6. Calculate cost per successful request.
7. Compare to NovaMind credit consumption.
8. Optimize highest-cost stage without harming quality.
```

---

# HA Walkthrough — One AZ Fails

```text
1. Are multiple ECS tasks deployed?
2. Are they across AZs?
3. Does ALB still have healthy targets?
4. Is Redis redundant?
5. What is MongoDB topology?
6. What is Qdrant topology?
7. Does NAT remain available?
8. What external providers remain dependencies?
9. What is expected RTO/RPO?
```

Current NovaMind cannot claim this scenario is tested.

---

# 30-Second Interview Answer

> NovaMind has five containerized backend services, with all eight AI workflows concentrated inside Agent. The repository defines task CPU/memory, but it has no measured capacity, p95/p99 baseline or mature autoscaling evidence. I would scale based on measured bottlenecks because more ECS tasks do not increase provider quotas and can increase pressure on Redis, MongoDB and Qdrant. Cost also needs workflow-level measurement because NovaMind credits are not an actual dollar-cost ledger. For HA, I would not claim mature Multi-AZ resilience today; that is Production V2 work.

---

# 60–90 Second Interview Answer

> My approach to NovaMind scalability is measurement-driven. The five backend services can theoretically scale independently, but Agent concentrates all eight AI workflows. I would not assume adding more Agent tasks solves everything because requests are often waiting on Groq, Gemini, Tavily, Qdrant, MongoDB or S3, and provider quotas can become the real bottleneck.
>
> Performance should be measured by workflow using concurrency and p50/p95/p99 latency. Search has Tavily plus Groq, while PDF RAG also performs parsing, embedding, vector storage and retrieval, so their latency/cost profiles differ from Chat. The current RAG implementation also repeats indexing work for each uploaded PDF, so persistent document indexing is a strong V2 improvement.
>
> Cost should be attributed per workflow across infrastructure, network and provider calls. Credits are not a verified dollar-cost ledger. For high availability, the current repository does not prove redundant Multi-AZ tasks, and captured Redis configuration was nonredundant with failover disabled. V2 should add measured autoscaling, async/backpressure where justified, Redis/stateful failover, backups/restore and explicit RTO/RPO.

---

# 2–3 Minute Scalability / Cost / HA Defense

> NovaMind has five separately containerized backend services: Gateway, Auth, Chat, Agent and Billing. The task definitions allocate approximately 512 CPU and 1 GiB to Gateway/Auth/Chat/Billing and 1024 CPU with 2 GiB to Agent. I treat those as configuration values only, not proof of capacity.
>
> Scalability has two dimensions. Vertically, I can give one task more CPU or memory. Horizontally, I can run more task replicas. Horizontal scaling is usually more useful for redundancy and parallel traffic, but it only works if shared dependencies and business logic support it. NovaMind's Agent handles eight different AI workflows, and all of them can call shared stores or external providers. So ten Agent tasks do not create ten times the capacity if Groq, Gemini, Redis, MongoDB or Qdrant becomes the bottleneck. CPU can also stay low while latency is high because the service is waiting on network-bound AI providers.
>
> Performance should therefore be decomposed. For Chat I would measure Gateway, Redis session lookup, routing, history load, Groq and persistence. For Search I would measure Tavily and Groq separately. For PDF RAG I would measure parse, chunking, embeddings, Qdrant insertion/retrieval and Groq. I would build p50, p95 and p99 baselines per workflow rather than one global average.
>
> Cost has the same workflow-specific nature. Baseline AWS costs can include ECS/Fargate, ALB, NAT and Redis, while request-driven costs include model inference, embeddings, search, images, storage and logs. NovaMind's internal credits are not an actual dollar-cost ledger. A Production V2 cost layer should attribute provider and infrastructure usage to each workflow and measure unit economics.
>
> High availability is different from scalability. I would not claim mature HA today because redundant desired counts and Multi-AZ deployment are not fully verified, and a captured Redis configuration showed a single nonredundant node with failover disabled. Production V2 should use multiple ECS tasks across AZs where the availability target requires it, Redis replication/failover, verified MongoDB/Qdrant resilience, health/readiness checks, backups, restore testing, and defined RTO/RPO. For external providers, I would design graceful degradation or controlled fallback only after testing model compatibility, quality, cost and quota behavior.

---

# Current vs Production V2

| Area | Current / Evidence | Production V2 |
|---|---|---|
| Service decomposition | 5 backend services | Keep; split only if evidence |
| Agent | 8 workflows together | isolate heavy workloads if justified |
| Capacity benchmark | none verified | load/capacity testing |
| Latency baseline | none verified | p50/p95/p99 per workflow |
| Autoscaling | not maturely verified | metric-driven ECS scaling |
| Async jobs | not current | queue/workers for long work |
| Backpressure | not mature | concurrency/admission controls |
| PDF indexing | request-oriented | persistent/reusable index |
| Redis correctness | race/TTL issues | atomic bounded operations |
| Cost ledger | credits only | workflow unit-cost telemetry |
| NAT/log optimization | not measured | measure and tune |
| Multi-AZ | not verified | deploy redundant tasks where needed |
| Redis HA | captured single node | replication/failover |
| DB/vector HA | unverified | verify/configure resilience |
| RTO/RPO | not defined/tested | define and test |
| DR | not tested | backups + restore + runbooks |
| Provider fallback | no universal failover | controlled, evaluated fallback |

---

# What Not to Say

Do not say:

- “ECS automatically makes the app scalable.”
- “Agent can support 10,000 users.”
- “The current p95 is X seconds.”
- “CPU is the only scaling metric.”
- “More ECS tasks always improve performance.”
- “The eight AI workflows are eight ECS services.”
- “Redis scales automatically with the app.”
- “NovaMind credits equal actual dollar cost.”
- “We know exact cost per workflow.”
- “The app is Multi-AZ highly available.”
- “Redis has automatic failover.”
- “MongoDB/Qdrant HA is verified.”
- “The application has zero downtime.”
- “Provider failover is automatic.”
- “RTO/RPO are defined and tested.”
- “Disaster recovery has been tested.”
- “The system is production-ready.”

---

# Final Self-Test

Before Module 20, explain without notes:

- scalability
- vertical/horizontal scaling
- elasticity
- capacity
- throughput
- concurrency
- bottleneck
- saturation
- CPU vs network-bound work
- statelessness
- desired count
- autoscaling
- target tracking
- cooldown
- Agent hot spot
- noisy neighbor
- bulkhead
- synchronous vs async
- queue/worker
- backpressure
- admission control
- latency
- p50/p95/p99
- Chat/Search/PDF RAG latency stages
- Redis/Mongo/Qdrant scaling
- provider quotas
- cross-region Qdrant consideration
- connection pooling
- caching
- pagination
- load/stress/spike/soak
- capacity planning
- fixed vs variable cost
- credits vs dollar cost
- NAT/CloudWatch/ECR/S3 cost
- cost per workflow
- HA
- redundancy
- SPOF
- AZ/Multi-AZ
- Redis HA
- provider HA
- backups
- RTO/RPO
- DR
- Production V2

**Module 19 interview preparation complete.**
