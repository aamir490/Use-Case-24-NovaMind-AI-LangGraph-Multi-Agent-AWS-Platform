# Module 17 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Error Handling, Reliability and Troubleshooting  
> **Purpose:** Prepare for reliability, distributed failure, debugging, retry, idempotency, timeout, recovery and pressure questions using only defensible NovaMind claims.

---

## Accuracy Rules

### CURRENT VERIFIED

```text
NovaMind has synchronous multi-service request paths.
CloudWatch awslogs is configured for backend services.
Some specialist/provider failures are caught and converted into aiResponse text.
HTTP 200 can therefore hide workflow failure.
Failure text can be persisted as assistant output.
Partial side effects can occur before error return.
The repo contains specific error-handling defects including:
- error vs err variable mismatch
- PDF rejection/error handling bug
- Date.now usage bug
- cleanup/finally weaknesses
- frontend artifact/null handling weakness
- MongoDB startup failure can be logged while process may continue
```

### CURRENT LIMITATIONS

```text
no uniform structured error contract
no mature timeout/deadline strategy
no mature circuit breakers
no universal provider failover
no mature global retry policy
incomplete idempotency
no mature distributed tracing
no mature cross-service correlation IDs
no verified SLO/SLA/RTO/RPO
no general async queue/DLQ architecture
```

### PRODUCTION V2 — PROPOSED

```text
structured error classes/codes
correct HTTP statuses
safe user messages
request IDs
per-dependency timeouts
total deadlines
cancellation
bounded retries
backoff + jitter
idempotency
circuit breakers where justified
graceful degradation
health/readiness
metrics
tracing
alerts
reconciliation
async jobs/DLQ where justified
failure testing
```

---

# Foundations

## Q1. What is an error?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> An error is a condition showing that the requested operation cannot proceed normally or did not produce the expected result.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q2. What is an exception?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> An exception is a runtime/programming mechanism used to signal an abnormal condition.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q3. What is a failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A failure is when the system does not deliver the expected behavior to the caller.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q4. What is a fault?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A fault is the underlying condition that can cause a failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q5. What is a bug?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A bug is a defect in code or logic.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q6. Error vs exception?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Error describes the problem condition; exception is one mechanism for representing/propagating that problem in code.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q7. Failure vs bug?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A bug is a defect; a failure is an observed incorrect behavior. A bug can cause a failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Failure Types

## Q8. What is a transient failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A temporary failure that may succeed on a later attempt, such as a brief provider 503.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q9. What is a permanent failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A failure that retrying unchanged will not fix, such as an invalid API key or unsupported input.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q10. What is partial failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Some stages succeed and create state, but the full business operation fails.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q11. What is cascading failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> One failing component causes failures or overload in dependent components.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q12. What is failure propagation?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A failure crossing service/dependency boundaries and affecting downstream behavior.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q13. What is synchronous failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The request is waiting directly on the failing operation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q14. What is asynchronous failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A background job/event fails outside the original request-response cycle.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# NovaMind Reliability Mental Model

## Q15. What troubleshooting questions do you ask first?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> What failed, what state already changed, can I retry safely, can retry create duplicate side effects, and how do I recover.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q16. Why is 'what state already changed' important?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Because a retry after partial success can duplicate messages, credits, files or payments.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q17. Why isn't try/catch enough?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Distributed reliability also needs correct status semantics, timeouts, retry safety, idempotency, logging and recovery.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# HTTP 200 Business Failure

## Q18. What is the most important current error-handling weakness?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Some specialist/provider errors are caught, converted into an aiResponse error string, and may still return HTTP 200.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q19. Why is that dangerous?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The frontend and monitoring may treat the request as successful even though the AI workflow failed.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q20. Can the failure text be stored?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Yes, it can be persisted as an assistant message in some flows.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q21. What key distinction do you use?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> HTTP 200 or transport success is not the same as business/workflow success.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q22. How would you improve it?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Return structured errors with correct HTTP status, safe message, machine-readable code and request ID.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Verified Defects

## Q23. What generic error-handler defect exists?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A verified variable mismatch involving `error` versus `err`.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q24. What Date.now defect exists?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A `${Date.now}` versus `Date.now()` mistake exists in one path.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q25. What PDF reliability issue exists?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The review found a PDF rejection/error-handling defect and a finally/cleanup path that can interfere with the original error.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q26. What image cleanup weakness exists?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Rate/cleanup ordering can create cleanup reliability issues.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q27. Can incompatible route/file combinations leak temp files?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Yes, some paths can leave uploaded temporary files.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q28. What frontend error weakness exists?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Frontend code can assume artifact fields exist and fail on null/unexpected data.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q29. What database startup weakness exists?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> MongoDB connection failure may be logged while the process can continue listening.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# HTTP Status Codes

## Q30. What does 200 mean?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The HTTP request succeeded according to the API semantics; it should not be used to hide a failed business operation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q31. What does 201 mean?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A resource was successfully created.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q32. What does 400 usually mean?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Invalid request.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q33. 401?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Not authenticated or invalid authentication.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q34. 403?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Authenticated but forbidden.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q35. 404?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Resource not found.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q36. 409?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Conflict or duplicate/state conflict.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q37. 422?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Semantically invalid request.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q38. 429?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Too many requests/rate limited.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q39. 500?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Internal server error.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q40. 502?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Bad gateway/upstream failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q41. 503?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Service unavailable.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q42. 504?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Gateway/upstream timeout.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Structured Errors

## Q43. What is a structured error?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A consistent error object with fields such as code, safe message and request ID.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q44. Why use machine-readable error codes?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Clients and metrics can distinguish timeout, auth, provider, validation and business failures reliably.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q45. What should user-facing errors avoid?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Secrets, stack traces and unnecessary infrastructure details.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q46. What belongs in internal logs instead?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Technical cause, dependency, stack/context where safe, latency and request ID.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q47. Is a centralized error model current?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No, it is a Production V2 recommendation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Gateway Failure

## Q48. What happens if Gateway fails?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Backend APIs are unavailable even if downstream services are healthy.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q49. Why is Gateway a critical boundary?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> It is the common application entry point for backend requests.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Redis Failure

## Q50. What does Redis support in NovaMind?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Sessions, fast conversation context/cache and rate counters.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q51. How can Redis failure affect authentication?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Session lookup can fail, blocking protected requests.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q52. How can Redis failure affect memory?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Recent conversation context/cache may be unavailable.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q53. How can Redis failure affect rate limiting?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Rate-limit enforcement can fail or become ambiguous.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q54. Fail open or fail closed for authentication?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Fail closed is generally safer.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q55. Fail open or fail closed for rate limiting?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> It is a trade-off between availability and abuse/cost protection.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# MongoDB Failure

## Q56. What durable data does MongoDB hold?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Users, conversations, messages and payments.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q57. What if Groq succeeds but assistant message save fails?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The user may receive an answer that is not durably recorded, which is a partial failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q58. Why is retrying message creation dangerous?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> It can create duplicate messages without idempotency.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q59. Why is process listening not enough?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The app may be alive while its required database is unavailable.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Chat Service Failure

## Q60. What does Agent depend on Chat for?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Conversation/message persistence and related history operations.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q61. What happens if Chat fails after provider response?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> AI generation may succeed while persistence fails.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Auth Service Failure

## Q62. What can Auth failure affect?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Account/session operations, credit deduction, credit grant and plan updates.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q63. Give a key partial-failure example.

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Payment is marked paid but Auth credit update fails.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Agent Failure

## Q64. What happens if Agent fails?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> AI workflows become unavailable even if Auth, Chat and Billing remain healthy.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Provider Mapping

## Q65. Which provider serves normal Chat?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Groq.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q66. Search?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Tavily retrieval plus Groq synthesis.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q67. PDF RAG?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Gemini embeddings, Qdrant retrieval and Groq answer generation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q68. Coding?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> OpenRouter with DeepSeek.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q69. Image generation?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Stability AI.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q70. Image analysis?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Gemini.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q71. Does having multiple providers mean automatic failover?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Qdrant Failure

## Q72. What does Qdrant failure mean for PDF RAG?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Document retrieval failed, so the application should not pretend grounded RAG succeeded.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q73. Should it silently switch to normal chat?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Not unless the product explicitly designs and communicates that fallback.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# S3 Failure

## Q74. What if PDF rendering succeeds but S3 upload fails?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The artifact was created but durable delivery failed.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q75. What if S3 upload succeeds but presigning fails?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The object exists but the user lacks the expected access URL.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q76. Why are retries tricky?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Regeneration or random object keys can create duplicate artifacts and extra provider cost.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Timeouts

## Q77. What is a timeout?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A maximum wait duration for an operation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q78. Why are timeouts necessary?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Without them, slow dependencies can hold resources indefinitely.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q79. What timeout layers exist?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Frontend, Gateway, service-to-service, provider, database and storage.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q80. Should every workflow use the same timeout?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q81. Are mature NovaMind timeout values verified?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Deadlines and Cancellation

## Q82. Timeout vs deadline?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Timeout limits one operation; deadline limits the total request.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q83. Why propagate deadlines?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Downstream calls should know how much total request time remains.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q84. What is cancellation?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Stopping work when the request is no longer useful, such as after deadline/disconnect.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q85. Is mature cancellation current?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Retries

## Q86. What is a retry?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Trying a failed operation again.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q87. When is retry appropriate?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Transient failures where the operation is safe to repeat.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q88. Why is retrying every error bad?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Permanent failures won't recover and retries add load, latency and cost.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q89. Retryable vs safe to retry?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A failure may be transient, but the operation may have side effects that make repetition unsafe.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Backoff and Jitter

## Q90. What is exponential backoff?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Increasing the wait between retry attempts.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q91. Why use backoff?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> To give the dependency time to recover and avoid hammering it.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q92. What is jitter?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Random variation added to retry delay.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q93. Why jitter?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> To avoid many clients retrying simultaneously.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q94. What is the thundering herd problem?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Many clients retry together and overload the recovering dependency.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Idempotency

## Q95. What is idempotency?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Repeating the same logical operation produces one business effect.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q96. Why is it important for payment callbacks?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The same valid callback can arrive multiple times.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q97. Why is it important for credit deduction?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Retries can double debit.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q98. Why is it important for message creation?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Retries can create duplicate messages.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q99. Why is it useful for S3 artifacts?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Stable artifact/object identity avoids duplicate objects on retry.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q100. Is global idempotency mature today?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Circuit Breaker

## Q101. What is a circuit breaker?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A pattern that temporarily stops calls to a repeatedly failing dependency.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q102. What are its common states?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Closed, open and half-open.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q103. Why use it?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Fail fast and reduce cascading pressure on a failing dependency.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q104. Is a mature circuit breaker implemented?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q105. Should you add one everywhere?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No, only where reliability measurements justify it.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Fallback

## Q106. What is fallback?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Alternative behavior when the primary path fails.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q107. Does NovaMind automatically fail over from Groq to Gemini?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No verified universal failover exists.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q108. Why is silent fallback risky?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> It can change feature semantics without the user realizing it.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Graceful Degradation

## Q109. What is graceful degradation?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Keeping unaffected features available when one feature/dependency fails.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q110. Give a NovaMind example.

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Image generation can be unavailable while normal chat continues, if failure isolation is designed.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q111. Is every workflow isolated that way today?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No mature universal guarantee.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Bulkhead

## Q112. What is the bulkhead pattern?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Isolating resources so one overloaded workflow cannot consume all shared capacity.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q113. Give a NovaMind example.

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Image generation spikes should not consume all capacity needed for chat.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q114. Is a mature bulkhead design current?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Fail Open vs Fail Closed

## Q115. What is fail closed?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Deny/block the operation when the control dependency fails.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q116. What is fail open?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Allow the operation even though the control failed.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q117. Where is fail closed safer?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Authentication and sensitive authorization.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q118. What is the rate-limit trade-off?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Fail open protects availability but risks abuse/cost; fail closed protects cost/security but blocks legitimate users.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Health Liveness Readiness

## Q119. What is a health check?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A probe indicating component/service condition.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q120. What is liveness?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Whether the process should be restarted.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q121. What is readiness?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Whether the process should receive traffic.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q122. Can a process be live but not ready?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Yes, for example Node is running but MongoDB is unavailable.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q123. Is mature NovaMind readiness verified?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Correlation IDs

## Q124. What is a correlation ID?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A shared identifier used to connect log events for one request across services.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q125. Where should it start?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> At the edge/Gateway.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q126. Where should it propagate?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Agent, Chat/Auth/Billing and provider-related logs.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q127. Is mature propagation current?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Logs Metrics Traces

## Q128. What are logs?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Detailed event records.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q129. What are metrics?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Numerical measurements over time.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q130. What are traces?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> End-to-end request journeys across components.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q131. What current observability is verified?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Centralized CloudWatch container logs.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q132. Is mature distributed tracing verified?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Reliability Availability Resilience

## Q133. What is reliability?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> How consistently the system performs correctly over time.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q134. What is availability?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> How often the system is usable when needed.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q135. What is resilience?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> How well the system handles and recovers from failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q136. Does NovaMind have measured reliability percentages?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No verified SLO/SLA measurements.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# SLI SLO SLA

## Q137. What is an SLI?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A measured reliability indicator.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q138. What is an SLO?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> An internal reliability target.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q139. What is an SLA?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A contractual reliability commitment.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q140. Does NovaMind have a verified formal SLA?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# RTO RPO

## Q141. What is RTO?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Maximum desired recovery time after disruption.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q142. What is RPO?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Maximum acceptable data-loss window.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q143. Are tested NovaMind RTO/RPO values verified?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Troubleshooting Method

## Q144. What is your full troubleshooting method?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Define the symptom, identify the workflow, find the first failing boundary, inspect health/logs/dependency/network/auth, check state already written, decide safe recovery, verify the fix and add prevention.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q145. Why find the first failing boundary?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Later errors may only be consequences of an earlier root failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q146. Why inspect state before retry?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> To avoid duplicating side effects.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario HTTP 500

## Q147. Frontend sees HTTP 500. What do you do?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Trace from Gateway to the downstream service/provider, inspect logs, determine the first failure and what state changed before retrying.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario HTTP 200 Failure Text

## Q148. Frontend gets 200 but answer says error. What do you suspect?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A specialist catch block may have converted a provider/tool exception into aiResponse text.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q149. Why is this especially dangerous?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Monitoring and frontend logic can classify a failed workflow as successful.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Local vs AWS

## Q150. Works locally but fails on AWS. What do you check?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> ECS task state, CloudWatch logs, env/secrets, Cloud Map/DNS, SG/NAT, Redis/MongoDB and external providers.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q151. Why not immediately change code?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The failure may be deployment/config/network-specific rather than application logic.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Slow Request

## Q152. How do you troubleshoot slow AI requests?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Measure Gateway, routing, memory/history load, provider/tool call, retrieval, persistence and artifact stages separately.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q153. Why not just blame the LLM?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The delay may be retrieval, network, persistence or another provider.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario PDF RAG

## Q154. PDF RAG gives wrong answer. What do you inspect first?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Routing and PDF extraction, then chunking, embeddings, Qdrant indexing/query, top-5 retrieval and finally generation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q155. Why not jump directly to hallucination?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The retrieved context itself may be wrong.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Search

## Q156. Search fails. What boundaries do you inspect?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Routing, Tavily, search results, Groq synthesis, credit operations and persistence.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Coding

## Q157. Coding fails. What stages do you inspect?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Router, coding classifier, OpenRouter, DeepSeek, structured JSON parse, artifact creation and frontend.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q158. Can provider success still lead to failure?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Yes, malformed structured output can fail parsing.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Image Analysis

## Q159. Image analysis fails. What do you inspect?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Upload/temp file, read/base64 conversion, Gemini call, response and cleanup.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Image Generation

## Q160. Image generation fails. What do you inspect?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Prompt preparation, Stability AI, returned bytes, S3 upload and presigned URL.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Paid No Credits

## Q161. User paid but no credits. What is the troubleshooting path?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Razorpay status, callback, HMAC, Payment record, Billing→Auth call, credit state and reconciliation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q162. Why not just call Auth again blindly?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The first call may have succeeded and only the response was lost, so a blind retry can double grant.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario Artifact Missing

## Q163. Generated PDF/PPT is missing. What do you trace?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> LLM structured output, parse, renderer, file/buffer, S3 upload, presign and frontend delivery.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Scenario ECS Failure

## Q164. ECS task stops. What do you check?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Service events, stopped reason, exit code, CloudWatch logs, env/secrets, memory and dependencies.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Retry Matrix

## Q165. Is LLM inference retryable?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Often for transient failures, but retries add cost and can produce different output.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q166. Is Tavily search retryable?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Often for transient failure, but it adds quota/cost.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q167. Is Qdrant read retryable?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Generally yes for transient read failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q168. Is MongoDB read retryable?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Generally yes according to database retry policy.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q169. Is message creation safe to retry blindly?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No, it can duplicate messages.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q170. Is S3 upload safe to retry?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Safer with a stable object key/artifact ID; random keys can duplicate objects.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q171. Is credit deduction safe to retry blindly?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q172. Is payment credit grant safe to retry blindly?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q173. Can Razorpay callbacks repeat?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Yes, so processing must be idempotent.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q174. Is a frontend GET usually safe to retry?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Usually yes if it is truly read-only.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q175. Can deployment retries overlap dangerously?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Yes, so immutable releases and concurrency control matter.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Recovery and Reconciliation

## Q176. What is recovery?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Restoring correct service after a failure.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q177. What is reconciliation?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Comparing distributed states and repairing mismatches safely.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q178. Give a reconciliation example.

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Payment says paid but user credits were not granted.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Production V2 Error Model

## Q179. What error-model improvement would you add first?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Central structured error classes/codes mapped to correct HTTP statuses.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q180. What should every error response include?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Safe message and request/correlation ID.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q181. What should stay internal?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Stack traces, secrets and raw provider internals.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Production V2 Timeouts and Retries

## Q182. What timeout improvement would you make?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Explicit per-dependency timeouts plus total request deadline.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q183. What retry improvement?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Retry only transient failures with bounded attempts, backoff, jitter and idempotency.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q184. What should retries respect?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> The overall deadline and business side effects.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Production V2 Resilience

## Q185. Would you add circuit breakers?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Where repeated provider failure and measurements justify them.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q186. Would you add fallback?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Only explicit feature-aware fallback, not silent semantic changes.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q187. Would you add async jobs?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> For suitable long-running operations such as large document/artifact processing if required.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q188. What is a DLQ?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A dead-letter queue holding repeatedly failed async jobs for inspection/recovery.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q189. Is DLQ current?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Production V2 Observability

## Q190. What observability improvements matter?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Structured logs, correlation IDs, reliability metrics, distributed tracing, dashboards and alerts.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q191. What provider metrics would you track?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Latency, timeout count, failure rate and rate-limit errors by provider/workflow.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Design Defense

## Q192. Why not retry every provider error?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Some failures are permanent, retries add cost, and side effects may duplicate.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q193. Why not always fail over to another LLM?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Models differ in capability/output and automatic failover can change semantics, cost and quality.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q194. Why not return HTTP 200 with an error message?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> It breaks API semantics and hides failures from clients/monitoring.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q195. Why not expose the real stack trace to users?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> It leaks implementation details and potentially sensitive information.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q196. Why not make every dependency part of readiness?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> A strict readiness check can take the whole service out for optional dependency failures; readiness should reflect required dependencies.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Pressure Questions

## Q197. If Groq times out, why not retry five times immediately?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> That can amplify an outage and increase latency/cost; use bounded backoff with jitter and deadline awareness.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q198. If the provider succeeded but the response was lost, what does retry risk?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Duplicate cost or side effects, depending on the operation.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q199. If Redis is down, should you let users through?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> For authentication I would fail closed; for other uses the policy depends on security/cost/product requirements.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q200. If MongoDB is down but Node is listening, is the service healthy?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> It may be live but not ready for required business operations.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q201. If Qdrant fails, can you just answer from the LLM?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Only if the product explicitly says grounding is unavailable; otherwise that would misrepresent RAG success.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q202. If HTTP status is 200, can your monitoring mark it successful?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> Not safely in the current project because some business failures can be encoded as response text.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

## Q203. What is the strongest accurate reliability claim?

**What the interviewer is testing:** Whether you can reason about real distributed failures instead of only repeating try/catch theory.

**Word-for-word answer:**

> NovaMind has real error handling and centralized logs, but failure semantics, retry/idempotency, timeout/deadline controls, correlation and recovery still need production hardening.

**Likely follow-up:** I would explain **what state already changed, whether retry is safe, whether the operation is idempotent, what the user should see, and how I would detect/recover from the failure**.

**Project-defense reminder:** HTTP transport success, provider success, persistence success and business success are separate things.

---

# Rapid-Fire Revision

**Q204. HTTP 200 = workflow success?**  
No.

**Q205. Main current error weakness?**  
Some failures become aiResponse text and may still return 200.

**Q206. Centralized structured errors current?**  
No.

**Q207. Per-dependency timeout strategy mature?**  
No.

**Q208. Circuit breaker current?**  
No.

**Q209. Universal provider failover current?**  
No.

**Q210. Distributed tracing current?**  
No.

**Q211. Correlation IDs mature?**  
No.

**Q212. Chat provider?**  
Groq.

**Q213. Search providers?**  
Tavily + Groq.

**Q214. PDF RAG providers?**  
Gemini embeddings + Qdrant + Groq.

**Q215. Coding?**  
OpenRouter + DeepSeek.

**Q216. Image generation?**  
Stability AI.

**Q217. Image analysis?**  
Gemini.

**Q218. Redis roles?**  
Sessions, context/cache, rate counters.

**Q219. MongoDB durable data?**  
Users, conversations, messages, payments.

**Q220. Fail closed for auth store failure?**  
Generally yes.

**Q221. Retry every error?**  
No.

**Q222. Backoff?**  
Increase wait between retries.

**Q223. Jitter?**  
Randomize retry timing.

**Q224. Idempotency?**  
One business effect for repeated logical request.

**Q225. Liveness?**  
Should process be restarted?

**Q226. Readiness?**  
Should traffic be sent?

**Q227. SLI?**  
Measured indicator.

**Q228. SLO?**  
Internal target.

**Q229. SLA?**  
Contractual promise.

**Q230. RTO?**  
Recovery time objective.

**Q231. RPO?**  
Recovery point objective.

# Cross-Question Chain 1 — HTTP 200 with Error Text

**Interviewer:** Your endpoint returned 200. Was the AI request successful?

> Not necessarily in the current NovaMind implementation. Some specialist catch blocks convert provider errors into `aiResponse` text, so the transport can return HTTP 200 even though the workflow failed.

**Interviewer:** Why is that bad?

> It confuses the frontend and monitoring, can persist failure text as an assistant message, and makes retry/business metrics unreliable.

**Interviewer:** How would you fix it?

> I would classify the failure, return a structured error with the correct status, log the technical cause with a request ID, and keep the user-facing message safe.

---

# Cross-Question Chain 2 — Retry Safety

**Interviewer:** A provider timed out. Do you retry?

> First I classify the failure as transient or permanent, then I check whether the operation is safe to repeat. For side-effecting operations I need idempotency before retrying.

**Interviewer:** What retry policy would you use?

> Bounded attempts with exponential backoff, jitter and respect for the total request deadline.

---

# Cross-Question Chain 3 — MongoDB Failure

**Interviewer:** Groq generated the answer but MongoDB save failed. What now?

> That is a partial failure. I need to decide whether to return the answer with a clear persistence warning or fail the request, but I must record the failure and avoid blindly creating duplicate messages on retry. A stable message/request ID would make retry safer.

---

# Cross-Question Chain 4 — Redis Failure

**Interviewer:** Redis is unavailable. Should you fail open?

> It depends on the concern. For authentication/session validation I would fail closed because security is more important. For a non-security cache, graceful degradation may be possible. Rate limiting is a policy trade-off because fail-open protects availability but increases abuse and cost risk.

---

# Cross-Question Chain 5 — RAG Failure

**Interviewer:** Qdrant is down. Can you just ask Groq without retrieval?

> I would not silently present that as PDF RAG because the answer would no longer be grounded in the uploaded document. If the product supports a fallback, I would disclose that retrieval is unavailable.

---

# Cross-Question Chain 6 — Paid but No Credits

**Interviewer:** The user paid but didn't get credits. Is retrying Auth enough?

> Not safely by itself. The original Auth call may have succeeded and only the response was lost, so a blind retry could double grant. I need idempotency and reconciliation around the payment/credit operation.

---

# Cross-Question Chain 7 — Slow Request

**Interviewer:** Users say AI is slow. What do you do?

> I decompose the request into Gateway, routing, history load, tool/retrieval, provider generation, persistence and artifact stages, then measure latency at each boundary. I don't assume the LLM is the bottleneck without evidence.

---

# Cross-Question Chain 8 — Circuit Breaker

**Interviewer:** Why add a circuit breaker?

> If a provider repeatedly fails, continuing to call it wastes time and resources and can amplify failures. A circuit breaker can fail fast temporarily, but I would only introduce it where measurements justify the complexity.

---

# Incident Walkthrough 1 — Provider Error Hidden as 200

```text
Symptom:
Frontend shows assistant error text.

1. Check HTTP status.
2. Confirm 200 was returned.
3. Trace specialist catch block.
4. Identify original provider/tool exception.
5. Check whether failure text was persisted.
6. Correct response semantics.
7. Add failure metric.
8. Add regression test.
```

---

# Incident Walkthrough 2 — Works Locally, Fails on ECS

```text
1. ECS task running?
2. Service events?
3. CloudWatch logs?
4. Correct environment variables?
5. Secrets available?
6. Internal DNS / Cloud Map?
7. Security groups?
8. NAT/outbound route?
9. Redis/MongoDB?
10. Provider reachability?
11. Verify fix from ECS, not only locally.
```

---

# Incident Walkthrough 3 — PDF RAG Wrong Answer

```text
1. Was PDF RAG actually selected?
2. Did pdf-parse extract useful text?
3. Did chunking produce expected chunks?
4. Did Gemini create embeddings?
5. Were vectors inserted into Qdrant?
6. Was question embedding generated?
7. What top-5 chunks were retrieved?
8. Were the relevant facts present?
9. What context was sent to Groq?
10. Only then inspect generation behavior.
```

---

# Incident Walkthrough 4 — Paid but No Credits

```text
1. Razorpay status
2. callback received
3. HMAC verified
4. Payment MongoDB status
5. Billing log
6. Billing → Auth request
7. current user balance
8. duplicate/idempotency state
9. reconciliation/recovery
```

---

# 30-Second Reliability Answer

> NovaMind is a synchronous distributed application, so failures can propagate across Gateway, Redis, internal services, providers and data stores. My main troubleshooting rule is to identify what failed, what state already changed and whether retry is safe. One current weakness is that some specialist failures can become `aiResponse` text and still return HTTP 200, so transport success does not always equal workflow success. Production V2 should add structured errors, correct statuses, timeouts, safe retry/idempotency and better observability.

---

# 60–90 Second Reliability Answer

> NovaMind's AI request path crosses multiple synchronous boundaries, so reliability is mainly about controlling failure propagation and partial success. For example, a user message may already be saved before a provider fails, or an LLM answer may be generated before MongoDB persistence fails. Payments have another distributed case where a Payment can be marked paid before credits are successfully granted.
>
> One verified error-handling weakness is that some specialist catch blocks convert provider failures into an `aiResponse` error sentence. That means HTTP 200 can be returned even when the workflow failed, and the failure text may be stored as an assistant message.
>
> I would improve this with structured error codes, correct HTTP statuses, safe user messages, correlation IDs, per-dependency timeouts, total deadlines, bounded retries with backoff and jitter, and idempotency for side-effecting operations. I would add circuit breakers only where provider-failure data justifies them, and use reconciliation for distributed partial failures.

---

# 2–3 Minute Reliability / Troubleshooting Defense

> NovaMind is a distributed synchronous AI system. A request can enter through the Express Gateway, depend on Redis for the application session, move into Agent and LangGraph, call Chat or Auth, then use an external provider such as Groq, Gemini, Tavily, OpenRouter/DeepSeek or Stability AI, and finally persist results in MongoDB, Qdrant or S3. Because there are many boundaries, a failure can happen after earlier state changes have already succeeded.
>
> My reliability model is always: what failed, what state already changed, can I retry safely, can retry duplicate a side effect, and how do I recover. This is especially important for messages, credits, payments and artifacts.
>
> A major verified weakness in the current implementation is that some specialist workflows catch provider errors and convert them into an `aiResponse` string. So the HTTP layer may still return 200 even though the workflow failed, and the error text can be persisted as an assistant message. That breaks the distinction between transport success and business success and makes monitoring and retries harder.
>
> There are also several concrete reliability defects in the repository, including an `error` versus `err` variable mismatch, PDF error/cleanup issues, a `Date.now` usage bug, cleanup leakage paths and frontend null/artifact handling weaknesses. MongoDB connection failure can also be logged while the service may continue listening, which shows why liveness and readiness should be separated.
>
> For Production V2, I would standardize errors across services, map them to correct HTTP statuses, generate a request ID at the Gateway, and propagate it through internal calls. I would set explicit per-dependency timeouts plus a total request deadline, retry only transient failures with bounded exponential backoff and jitter, and make side-effecting operations idempotent. I would consider circuit breakers for repeatedly failing providers, add readiness/health checks, and improve observability with structured logs, metrics and tracing.
>
> For troubleshooting I never jump directly to the LLM. For example, if PDF RAG returns the wrong answer, I first verify routing, text extraction, chunking, embedding, Qdrant indexing and top-k retrieval, then inspect the context sent to Groq. Similarly, if something works locally but fails on AWS, I inspect ECS state, CloudWatch logs, environment/secrets, service discovery, security groups, NAT and external dependencies before changing code.

---

# Current vs Production V2

| Area | Current NovaMind | Production V2 Proposal |
|---|---|---|
| Error representation | inconsistent; some failures become response text | centralized structured errors |
| HTTP semantics | some business failures can return 200 | correct 4xx/5xx |
| User errors | inconsistent | safe standardized messages |
| Correlation IDs | not mature | end-to-end propagation |
| Timeouts | not maturely verified | per-dependency timeouts |
| Deadlines | not mature | total request budget |
| Retry | inconsistent | bounded retry + backoff + jitter |
| Idempotency | partial | stable IDs for side effects |
| Circuit breaker | not mature | add where justified |
| Provider failover | no universal failover | explicit fallback if designed |
| Health/readiness | limited | meaningful liveness/readiness |
| Logging | CloudWatch logs | structured logs |
| Metrics | not mature | reliability/provider metrics |
| Tracing | not verified | distributed tracing |
| Recovery | manual/ad hoc in areas | reconciliation/runbooks |
| Async jobs | not general current design | optional for long-running work |

---

# What Not to Say

Do not say:

- “HTTP 200 means every AI request succeeded.”
- “All errors are returned with correct status codes.”
- “We have standardized error classes everywhere.”
- “We have automatic provider failover.”
- “Groq automatically falls back to Gemini.”
- “Every dependency has retries.”
- “Retries are always safe.”
- “We use circuit breakers everywhere.”
- “We have distributed tracing.”
- “We have mature correlation IDs.”
- “We have a tested 99.9% SLO.”
- “We have tested RTO/RPO.”
- “We use async queues/DLQs for all long tasks.”
- “The system is fault tolerant / production-ready.”

---

# Final Self-Test

Before Module 18, explain without notes:

- error
- exception
- fault
- bug
- failure
- transient vs permanent
- partial failure
- cascading failure
- HTTP 200 vs business success
- verified NovaMind error defects
- 2xx / 4xx / 5xx
- structured errors
- safe user vs internal error
- Redis failure
- MongoDB failure
- Chat/Auth/Agent failure
- provider map
- Qdrant failure
- S3 partial failure
- timeout
- deadline
- cancellation
- retry
- backoff
- jitter
- idempotency
- circuit breaker
- fallback
- graceful degradation
- bulkhead
- fail-open / fail-closed
- liveness / readiness
- correlation IDs
- logs / metrics / traces
- reliability / availability / resilience
- SLI / SLO / SLA
- RTO / RPO
- troubleshooting methodology
- PDF RAG troubleshooting
- paid/no credits troubleshooting
- retry matrix
- Production V2

**Module 17 interview preparation complete.**
