# Module 18 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Testing, AI Evaluation and Observability  
> **Purpose:** Prepare for software-testing, AI-evaluation, RAG-quality, routing, observability, performance, failure-testing, and production-readiness interview questions.

---

## Accuracy Rules

### CURRENT VERIFIED

```text
Frontend ESLint/lint capability
Frontend build capability
Dependency lockfiles
Manual deployment documentation/screenshots
CloudWatch awslogs for Gateway/Auth/Chat/Agent/Billing
```

### CURRENT GAPS

```text
No substantive backend unit-test suite
No mature API/integration/E2E suite
No mature authorization regression suite
No payment replay/idempotency suite
No router evaluation benchmark
No RAG evaluation benchmark
No structured-output evaluation suite
No prompt/model regression suite
No load/performance/failure suite
No mature deployment smoke-test gate
No mature distributed tracing
No mature correlation IDs
No mature AI quality dashboard
```

### PRODUCTION V2 — PROPOSED

```text
Layered automated tests
Golden/evaluation datasets
Router evaluation
RAG retrieval + generation evaluation
Structured-output schema validation
Authorization/payment regression tests
Performance and failure testing
CI quality gates
Structured logs
Metrics
Correlation IDs
Distributed tracing
AI quality monitoring
```

---

# Testing Fundamentals

## Q1. What is software testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Software testing is the systematic process of checking whether software behaves as expected.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q2. What is a test case?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> One specific input/action and expected result.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q3. What is a test scenario?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A broader user or system flow containing multiple checks.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q4. What is an assertion?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A check that compares actual behavior with expected behavior.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q5. What is a test fixture?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Predefined data or setup used to run a repeatable test.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q6. What is a mock?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A test double that replaces a dependency and can verify expected interactions.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q7. What is a stub?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A test double that returns predetermined values.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q8. What is a fake?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A lightweight working implementation used in place of a real dependency.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q9. What is a test double?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A general term for mocks, stubs, fakes and similar replacements.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q10. What is deterministic testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A test that should produce the same result when relevant conditions do not change.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Test Types

## Q11. What is positive testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing valid expected usage.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q12. What is negative testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing invalid or failure conditions.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q13. What is boundary testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing at and around system limits.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q14. What is regression testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Keeping a test for a previously found bug so it does not return.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q15. What is unit testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing a small piece of logic in isolation.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q16. What is integration testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing multiple components together.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q17. What is API testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing request/response behavior, auth, status, schema and side effects.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q18. What is component testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing a larger service/module while replacing some external dependencies.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q19. What is E2E testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing a real user journey through multiple layers.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q20. What is contract testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing that two services agree on request/response contracts.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Test Pyramid

## Q21. What is the test pyramid?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A strategy with many fast unit tests, fewer integration tests and fewer expensive E2E tests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q22. Why not only use E2E tests?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> They are slower, more brittle and harder to debug.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q23. Why not only use unit tests?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> They cannot prove real service integration or user workflows.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q24. Should I follow exact percentage ratios?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No; choose proportions based on risk and system architecture.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Coverage

## Q25. What is code coverage?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A measure of how much code is executed by tests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q26. Does 100% coverage prove correctness?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q27. What is behavior coverage?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Whether important real behaviors and risks are tested.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q28. Which matters more for NovaMind?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Risk-based behavior coverage is more important than a vanity percentage.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Current NovaMind Testing State

## Q29. What current testing evidence exists?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Frontend ESLint/lint capability, frontend build capability, lockfiles, manual deployment docs/screenshots and CloudWatch logging.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q30. Is there a substantive backend unit-test suite?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q31. Is there a mature integration-test suite?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q32. Is there a mature E2E suite?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q33. Was the backend test script substantive?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No, it was effectively a placeholder/error.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q34. Can you claim the full application was run and tested during repo analysis?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Unit Tests for NovaMind

## Q35. What should be unit tested first?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Router helpers, validation, parsers, signature verification, credit/payment utilities, rate-limit helpers and error classification.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q36. Should unit tests call real Groq?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Usually no; mock provider behavior for deterministic unit tests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q37. What is the benefit?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Fast and focused failure diagnosis.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Router Logic Tests

## Q38. What is router priority #1?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Explicit non-auto selection wins.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q39. Auto + PDF routes where?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> PDF RAG.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q40. Auto + image routes where?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Image Analysis.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q41. What happens otherwise?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Model-based classifier is used.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q42. What happens on unknown classifier label?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Chat fallback.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q43. Is classifier exception handled by a mature universal fallback?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q44. Coding selected + PDF attached should route where?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Coding, because explicit non-auto selection has priority.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Routing Quality Evaluation

## Q45. Router logic test vs router quality evaluation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Logic tests deterministic branch rules; quality evaluation measures whether model classification is correct across realistic prompts.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q46. What metrics can evaluate routing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Accuracy, confusion matrix, per-workflow precision/recall, misrouting rate and fallback rate.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q47. Why can overall accuracy mislead?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> One workflow can perform badly while dominant workflows make overall accuracy look high.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q48. Does NovaMind currently have a mature router benchmark?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# AI Evaluation Basics

## Q49. What is AI evaluation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Systematic measurement of whether AI behavior meets quality expectations.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q50. Why isn't normal testing enough?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Software can run correctly while the model output is poor or wrong.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q51. Operational success vs AI quality?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A request can be technically successful but semantically wrong.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q52. What dimensions matter?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Correctness, relevance, grounding, completeness, format, latency, cost and consistency.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Deterministic vs Semantic Eval

## Q53. What is deterministic evaluation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Checking exact properties such as JSON validity, required fields or allowed route labels.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q54. What is semantic evaluation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Judging meaning, correctness, relevance or grounding.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q55. Why do we need both?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> AI systems must satisfy both machine-readable contracts and qualitative behavior.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Golden Dataset

## Q56. What is a golden/evaluation dataset?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A fixed representative set of inputs with expected behavior or evidence.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q57. Why use one?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> To compare prompt/model/config changes on the same cases.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q58. Does NovaMind currently have a mature golden dataset?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q59. What router record might look like?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Prompt plus expected workflow label.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q60. What RAG record might contain?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Question, expected evidence and expected answer points.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# RAG Evaluation Basics

## Q61. What are the two parts of RAG evaluation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Retrieval evaluation and generation evaluation.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q62. Why separate them?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A bad final answer can come from bad retrieval or bad generation.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q63. What is NovaMind's current retrieval K?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Top 5.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q64. What embedding model is verified?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> `gemini-embedding-001`.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q65. What vector DB?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Qdrant.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q66. What answer model/provider?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Groq-backed answer generation.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Retrieval Metrics

## Q67. What is Recall@K?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> How much relevant evidence appears within the top K retrieved items.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q68. What is Precision@K?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> How many of the top K retrieved items are relevant.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q69. What is hit rate?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Whether at least one expected relevant item appears in the top K.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q70. What is MRR conceptually?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A metric rewarding relevant evidence appearing closer to the top.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q71. What is a retrieval threshold?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A minimum relevance score below which weak matches may be rejected.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q72. Is mature thresholding implemented?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q73. Is reranking currently mature?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# RAG Generation Quality

## Q74. What is groundedness?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Whether answer claims are supported by retrieved evidence.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q75. What is faithfulness?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Whether the model stays faithful to provided context without unsupported invention.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q76. What is answer relevance?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Whether the answer addresses the question.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q77. What is completeness?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Whether it includes the important required answer points.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q78. Does RAG eliminate hallucinations?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q79. Does NovaMind have mature page/source citations?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# No-Answer Testing

## Q80. Why test questions whose answers are absent?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> To measure whether the system abstains instead of hallucinating.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q81. What is abstention quality?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> How appropriately the system says it cannot find/support an answer.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q82. Is mature abstention-threshold eval implemented?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Scanned PDF Testing

## Q83. Why are scanned PDFs important test cases?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Current `pdf-parse` is text extraction, not OCR.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q84. What should a scanned-PDF test reveal?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> The current OCR limitation rather than falsely claiming successful extraction.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Search Evaluation

## Q85. What is NovaMind Search flow?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Tavily retrieves up to five results/images, then Groq synthesizes the answer.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q86. What should Search evaluation measure?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Freshness, result relevance, answer correctness/grounding, latency and cost.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q87. Are search citations/fact checking maturely verified?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Chat Evaluation

## Q88. What should Chat evaluation measure?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Correctness, relevance, instruction following, context use, coherence, latency and cost.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q89. Does NovaMind have a mature chat benchmark?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Coding Workflow Evaluation

## Q90. What is the coding path?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Coding classifier → OpenRouter → DeepSeek → structured files[] → parse → Monaco/preview.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q91. What deterministic checks matter?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Valid JSON, files array, required fields/types and parser validity.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q92. What quality checks could be added?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Syntax, lint, compile/build, unit tests and browser smoke tests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q93. Does NovaMind run generated code server-side?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q94. Does it have a full compile/test/repair loop?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Structured Output

## Q95. Does asking an LLM for JSON guarantee valid JSON?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q96. What failures occur?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Markdown fences, malformed/truncated JSON, wrong types and missing fields.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q97. What should Production V2 add?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Schema validation plus controlled repair/retry/error handling.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Artifact Testing

## Q98. What should PDF/PPT testing cover?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Content parse, renderer, file creation/opening, S3 upload and presigned URL.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q99. What PPT pattern is verified?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Cover + six content slides + closing = eight slides.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q100. Should artifact tests verify only HTTP 200?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Image Workflow Testing

## Q101. What should image-generation tests cover?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Prompt prep, Stability response, valid bytes, S3 upload and URL.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q102. What should image-analysis tests cover?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Upload, MIME handling, base64/read, Gemini call, response and cleanup.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Authentication Testing

## Q103. What is the verified login flow?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Google/Firebase ID token verification → user lookup/create → Redis opaque UUID app session → HTTP-only cookie.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q104. Is the NovaMind application session a JWT?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q105. What auth tests matter?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Valid/invalid token, missing/expired session, Redis unavailable, logout/revocation and cookie behavior.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Authorization Testing

## Q106. Why is authorization testing high priority?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Ownership/tenant isolation is only partial in the current project.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q107. What should be tested?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> User A cannot access User B conversations/messages/artifacts; admin and credit mutation routes are protected.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q108. Authentication vs authorization?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Authentication proves identity; authorization decides permitted actions/resources.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Payment Testing

## Q109. What payment cases matter beyond happy path?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Invalid signature, duplicate callback, replay, paid-but-credit-failed, concurrency and retry.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q110. Why is duplicate callback testing critical?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Repeated events must not grant credits twice.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q111. Is current payment consistency fully idempotent?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Redis Memory Testing

## Q112. What verified memory bugs should become tests?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Unbounded hydration, duplicated current user message, read-modify-write races, weak 20-message cap, TTL loss and no token-aware summarization.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q113. Why is concurrency testing needed?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Sequential tests will not expose read-modify-write races.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Performance Testing

## Q114. What is load testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing expected traffic levels.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q115. What is stress testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Pushing beyond normal capacity to find limits.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q116. What is spike testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing sudden bursts.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q117. What is soak testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Sustained load over a long period.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q118. Does NovaMind have a mature load suite?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q119. What should be measured?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Latency, error rate, CPU/memory, Redis/Mongo/Qdrant behavior and provider quotas.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Failure and Recovery Testing

## Q120. What is failure testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Intentionally making dependencies fail to verify behavior.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q121. What should be injected?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Redis/Mongo/Qdrant outages, provider timeout, S3 denial and missing secrets.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q122. What is recovery testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Verifying correct recovery after the dependency comes back.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q123. Does NovaMind have a mature chaos program?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Observability Fundamentals

## Q124. Monitoring vs observability?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Monitoring watches known signals; observability helps infer internal system state from telemetry.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q125. What are the three main observability pillars?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Logs, metrics and traces.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q126. What current telemetry is verified?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> CloudWatch container logs via awslogs.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q127. Does that equal full observability?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Logging

## Q128. What is structured logging?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Logging consistent machine-readable fields such as service, requestId, workflow, provider, latency and status.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q129. What should never be logged blindly?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Secrets, tokens, DB URIs and sensitive prompt/document data.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q130. Why are logs useful?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> They preserve event/error detail for troubleshooting.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Metrics

## Q131. What is a counter?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A metric that increases, such as total provider errors.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q132. What is a gauge?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A current value such as active requests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q133. What is a histogram/distribution used for?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Latency/value distributions and percentiles.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q134. What AI-specific metrics would you add?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Routing errors, retrieval hits, structured-output failures, provider latency/errors and quality scores.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Latency Percentiles

## Q135. What is p50?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Median latency.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q136. What is p95?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> 95% of requests are at or below that latency.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q137. What is p99?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> 99% of requests are at or below that latency.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q138. Why not only use average?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Average can hide slow tail requests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Tracing

## Q139. What is a trace?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> The end-to-end request journey.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q140. What is a span?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> One operation within a trace.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q141. Give a NovaMind trace example.

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Gateway → Agent → Router → Tavily → Groq → Chat persistence.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q142. Is mature distributed tracing current?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Correlation IDs

## Q143. What is a correlation ID?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> An identifier propagated across services so logs for one request can be joined.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q144. Why is it useful before full tracing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> It enables cross-service log search with less infrastructure.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q145. Is mature correlation-ID propagation current?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# AI Observability

## Q146. What extra telemetry does AI need?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Workflow/model/provider, prompt version, token/cost signals, latency, retrieval stats, structured-output failures and quality feedback.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q147. Should you log every full prompt?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No, privacy/sensitivity must be considered.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Prompt Versioning

## Q148. Why version prompts?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Prompt changes can change behavior and create regressions.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q149. Is a mature prompt registry current?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q150. What metadata would you record?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Prompt version, model, workflow and relevant parameters.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Offline vs Online Evaluation

## Q151. What is offline evaluation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Running a fixed dataset before release.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q152. What is online evaluation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Measuring real production behavior/feedback.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q153. Why use both?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Offline catches regressions before release; online detects real-world issues.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Human Evaluation

## Q154. Why use human evaluators?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> They can judge nuanced usefulness/correctness that automated metrics miss.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q155. What are drawbacks?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Cost, speed and subjectivity.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q156. How reduce subjectivity?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Use clear rubrics.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# LLM-as-a-Judge

## Q157. What is LLM-as-a-judge?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> A model scores another model's answer using a rubric.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q158. What are benefits?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Scalable semantic evaluation.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q159. What are limitations?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Bias, preference, inconsistency, correlated errors and cost.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q160. Is a mature judge system current?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Cost Evaluation

## Q161. Why evaluate cost?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> An AI system can be high quality but financially inefficient.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q162. What should be tracked?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Provider calls, tokens where available, embeddings, search/image operations and infrastructure.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q163. Are NovaMind credits equal to dollar cost?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Prompt and Model Regression

## Q164. How do you evaluate a new prompt?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Run old and new prompts on the same dataset and compare quality/cost.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q165. Should a newer model automatically replace the old one?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q166. What if embedding model changes?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Existing vectors may need re-embedding because vector spaces can differ.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Experiment Tracking

## Q167. What could an eval run store?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Run ID, model, prompt/dataset version, metrics, latency and cost.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q168. Does NovaMind use MLflow or DVC for this project?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No verified usage.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Security Testing

## Q169. What high-risk areas need tests?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Ownership, public credit/plan mutation routes, admin routes, secret leakage, session behavior, prompt injection and file uploads.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q170. What is prompt-injection testing?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Testing whether untrusted retrieved content can manipulate model behavior.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q171. Is mature prompt-injection evaluation current?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# File Upload Testing

## Q172. What file cases should be tested?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Valid, scanned, corrupt, oversized, MIME mismatch, wrong type and cleanup on success/failure.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q173. Is MIME metadata perfect proof of file contents?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Alerting

## Q174. What makes an alert useful?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> It is actionable and tied to meaningful user/system impact.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q175. Give good alert examples.

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No healthy Agent tasks, rising 5xx, Redis failures, provider timeout spike, payment consistency errors.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q176. Should thresholds be invented?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No, establish them from baselines/SLOs.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Error Budget

## Q177. What is an error budget?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> The amount of failure allowed by an SLO.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q178. Does NovaMind have a verified error-budget practice?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Quality Gates

## Q179. What can AI quality gates block?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Router/RAG/structured-output regressions before deployment.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q180. Should thresholds be arbitrary?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q181. How choose thresholds?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> From product requirements and measured baselines.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# CI/CD Integration

## Q182. How should tests/evals fit Module 16 pipeline?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> PR lint/tests/security/router/RAG/structured-output eval before build/deploy, followed by smoke tests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q183. Is that current?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No, proposed.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Mock vs Real Providers

## Q184. Why mock providers?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Fast, cheap and deterministic software tests.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q185. Why use real providers too?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Mocks cannot test actual model behavior, latency, quota or API differences.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q186. What is the strongest strategy?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Use both at different test layers.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Design Defense

## Q187. Why test router separately from RAG?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Routing correctness and retrieval/generation quality are different failure domains.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q188. Why evaluate retrieval separately from generation?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Bad retrieval can make a good model answer badly.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q189. Why not rely only on logs?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Logs show events but do not measure AI quality or provide full metrics/tracing.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q190. Why not chase 100% coverage?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Risk-based tests catch important failures better than vanity coverage.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q191. Why isn't a successful deployment enough?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> The software may run while important features or AI quality are broken.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Pressure Questions

## Q192. Your API returns 200 and latency is good. Is AI quality good?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Not necessarily.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q193. Your RAG answer is wrong. Is Groq at fault?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Not necessarily; I first inspect retrieval.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q194. Why not test LLM answers by exact string?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Semantic outputs can vary; exact-string checks are brittle.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q195. Why use mocks if production uses real providers?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Mocks test deterministic application logic cheaply; controlled real-provider evals test actual model behavior.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q196. If router accuracy is 95%, are you done?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No; I inspect per-workflow errors, especially high-risk workflows.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q197. If RAG has high Recall@5 but poor answers, where do you look?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> Generation quality, context noise, prompt/instruction and answer evaluation.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q198. If RAG answer is good but retrieval metric is poor, is that okay?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> It may be accidental/model prior knowledge; I still need reliable evidence retrieval for grounding.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q199. Can you claim CloudWatch gives full observability?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q200. Can you claim the project has been fully tested?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

## Q201. What is your strongest accurate statement?

**What the interviewer is testing:** Whether you can distinguish software correctness, AI quality and runtime observability, and whether you can design realistic tests for NovaMind rather than giving generic QA answers.

**Word-for-word answer:**

> NovaMind has basic lint/build and centralized logging, but testing and AI-evaluation maturity is a major identified gap with a concrete Production V2 strategy.

**Likely follow-up:** I would explain **what I would test, what I would mock, what must use a real integration/provider, what metric proves success, and whether the capability is current or proposed**.

**Project-defense reminder:** A request can be operationally healthy and still produce a bad AI answer.

---

# Rapid-Fire Revision

**Q202. Testing answers?**  
Does the software behave correctly?

**Q203. Evaluation answers?**  
Is the AI output good?

**Q204. Monitoring answers?**  
Are known runtime signals healthy?

**Q205. Observability answers?**  
What is happening internally and why?

**Q206. Backend unit suite current?**  
No substantive suite.

**Q207. E2E suite current?**  
No.

**Q208. Router eval current?**  
No.

**Q209. RAG eval current?**  
No.

**Q210. CloudWatch logs current?**  
Yes.

**Q211. Distributed tracing current?**  
No.

**Q212. Correlation IDs mature?**  
No.

**Q213. RAG retrieval K?**  
Top 5.

**Q214. Embedding model?**  
gemini-embedding-001.

**Q215. Vector DB?**  
Qdrant.

**Q216. RAG answer provider?**  
Groq.

**Q217. Scanned PDF OCR?**  
No.

**Q218. Coding server-side execution?**  
No.

**Q219. Application session JWT?**  
No.

**Q220. Test pyramid?**  
Many unit, fewer integration, few E2E.

**Q221. Recall@K?**  
Relevant evidence found in top K.

**Q222. Precision@K?**  
Fraction of top K that is relevant.

**Q223. p50?**  
Median.

**Q224. p95?**  
95th percentile.

**Q225. p99?**  
99th percentile.

**Q226. LLM judge absolute truth?**  
No.

**Q227. NovaMind credits = dollar cost?**  
No.

# Cross-Question Chain 1 — Testing vs Evaluation

**Interviewer:** If your unit tests pass, is the AI system correct?

> Not necessarily. Unit tests can prove deterministic application behavior, but they do not prove semantic AI quality. I also need AI evaluation for routing, RAG, search, chat and structured outputs.

**Interviewer:** Give me a NovaMind example.

> I can unit-test that Auto plus a PDF routes to the PDF RAG node. But whether an ambiguous natural-language prompt is classified into the correct workflow requires a router evaluation dataset.

---

# Cross-Question Chain 2 — RAG Evaluation

**Interviewer:** Your PDF answer is wrong. What do you evaluate?

> I separate retrieval from generation. First I check whether top-5 Qdrant retrieval included the expected evidence. Only after confirming retrieval do I score the generated answer for correctness, grounding and relevance.

**Interviewer:** Why?

> Because if relevant evidence never entered the prompt, the LLM cannot reliably produce a grounded answer from it.

---

# Cross-Question Chain 3 — CloudWatch

**Interviewer:** Do you already have observability?

> We have basic centralized container logging through CloudWatch `awslogs` for all five backend services. I would not call that complete observability because mature application metrics, correlation IDs and distributed tracing are not verified.

---

# Cross-Question Chain 4 — Payment Testing

**Interviewer:** What is the most important payment test?

> Beyond signature verification, I would send the same valid callback repeatedly and verify credits are granted exactly once. That directly tests idempotency and replay safety.

---

# Cross-Question Chain 5 — Authorization Testing

**Interviewer:** How would you test tenant isolation?

> I would create two users, create a conversation/artifact for User A, then attempt to retrieve or modify it as User B and assert that access is denied.

---

# Cross-Question Chain 6 — LLM-as-a-Judge

**Interviewer:** Why not let another LLM grade everything?

> It can scale semantic evaluation, but the judge can be biased or inconsistent and may share the same blind spots. I would combine judge scoring with deterministic checks, human-reviewed calibration and representative datasets.

---

# Cross-Question Chain 7 — Performance

**Interviewer:** Why not just add more ECS tasks if latency is high?

> Because the bottleneck may be Groq, Gemini, Qdrant, Redis, MongoDB or provider quotas. I would load-test and measure each stage before scaling.

---

# Cross-Question Chain 8 — Embedding Model Change

**Interviewer:** Can you change the embedding model without touching Qdrant data?

> Not safely by assumption. Different embedding models can produce incompatible vector spaces or dimensions, so I would validate compatibility and normally re-embed documents for a clean migration.

---

# Test Plan Walkthrough 1 — Router

```text
Dataset:
- clear Chat prompts
- clear Search prompts
- Coding prompts
- PDF/Image auto cases
- explicit manual selections
- ambiguous prompts
- unknown labels

Deterministic checks:
- routing priority
- valid branch
- fallback behavior

Quality metrics:
- accuracy
- confusion matrix
- per-workflow precision/recall
- misrouting rate
```

---

# Test Plan Walkthrough 2 — PDF RAG

```text
1. Create representative PDFs.
2. Create questions with expected evidence.
3. Run extraction/chunking.
4. Index with Gemini embeddings in Qdrant.
5. Retrieve top 5.
6. Score retrieval hit/Recall@5/Precision@5.
7. Generate answer with Groq.
8. Score correctness, faithfulness, relevance, completeness.
9. Include no-answer and scanned-PDF cases.
10. Compare candidate changes against baseline.
```

---

# Test Plan Walkthrough 3 — Payment

```text
1. Valid signature
2. Invalid signature
3. Duplicate callback
4. Replay after success
5. Auth credit update failure
6. Retry
7. Concurrent callbacks
8. Verify payment state
9. Verify credits exactly once
10. Verify reconciliation path
```

---

# Test Plan Walkthrough 4 — Redis Memory

```text
1. Empty conversation
2. Hydrate from MongoDB
3. Append current user message
4. Verify no duplicate
5. Concurrent writes
6. Verify cap behavior
7. Verify TTL remains
8. Large history
9. Redis restart/failure
```

---

# AI Evaluation Walkthrough — Candidate Model/Prompt

```text
Baseline:
model A + prompt v1

Candidate:
model B + prompt v2

Same evaluation dataset

Compare:
router quality
RAG quality
chat quality
structured-output validity
latency
cost
failure rate

Decision:
deploy only if trade-off is acceptable
```

---

# 30-Second Interview Answer

> NovaMind currently has frontend lint/build capability and centralized CloudWatch logs, but not a substantive automated test or AI-evaluation suite. I separate software testing from AI evaluation: tests verify deterministic behavior such as routing rules, authentication, payment idempotency and API contracts, while AI evaluation measures router quality, RAG retrieval, grounding and structured outputs. Production V2 should combine layered tests with evaluation datasets and observability through logs, metrics, correlation IDs and tracing.

---

# 60–90 Second Interview Answer

> Testing, AI evaluation and observability solve different problems. Software tests verify deterministic behavior, for example explicit routing priority, API status codes, authentication, authorization and payment idempotency. AI evaluation measures semantic quality, such as whether the classifier routes realistic prompts correctly, whether Qdrant retrieves the right PDF chunks and whether the Groq answer is grounded and relevant.
>
> NovaMind currently has frontend lint/build capability, lockfiles and CloudWatch `awslogs` for the five backend services, but it does not have a mature backend unit/integration/E2E suite, router/RAG benchmark, structured-output quality gate, correlation layer or distributed tracing.
>
> My Production V2 strategy would start with risk-heavy regression tests for authorization, payment replay, credits and HTTP error semantics, then add router/RAG eval datasets, structured-output validation, Redis memory regression tests, performance/failure testing and deployment smoke tests. In production I would add structured logs, metrics, correlation IDs, traces and AI-quality signals.

---

# 2–3 Minute Testing / AI Evaluation / Observability Defense

> NovaMind needs a layered quality strategy because it combines normal deterministic software with probabilistic AI behavior. I use software tests to verify things that should have exact behavior. For example, explicit non-auto workflow selection must have higher priority than file-based routing, Auto plus a PDF should route to PDF RAG, invalid sessions should be rejected, and a duplicate Razorpay callback should not grant credits twice.
>
> AI behavior needs evaluation rather than only exact assertions. For the router, I would build a representative evaluation dataset covering all eight specialist workflows, ambiguous prompts and fallback cases, then measure overall and per-workflow accuracy, precision, recall and confusion patterns. For PDF RAG, I separate retrieval from generation. I verify whether the top five Qdrant results include the expected evidence, then independently score the generated answer for correctness, relevance and faithfulness. That separation matters because a bad answer may be caused by poor retrieval rather than the LLM itself.
>
> The current project has limited testing maturity. It has frontend lint/build capability, lockfiles and centralized CloudWatch container logs, but no substantive backend unit/integration/E2E suite, no mature router/RAG evaluation suite, no payment replay regression suite, no load/failure suite and no distributed tracing.
>
> My Production V2 approach would prioritize the highest risks first: authorization ownership, payment replay/idempotency, credit consistency and error semantics. Then I would add router and RAG evaluation datasets, structured JSON validation, Redis memory regressions, artifact/S3 failure tests and deployment smoke tests. These would become CI quality gates.
>
> For runtime observability I would keep CloudWatch logs but make them structured, add a Gateway-generated correlation ID, collect application/provider metrics such as p95 latency, provider errors, routing failures and RAG retrieval quality, and add distributed tracing where the debugging value justifies it. Operational telemetry and AI quality would be monitored separately because a technically healthy request can still produce a poor answer.

---

# Current vs Production V2

| Area | Current | Production V2 |
|---|---|---|
| Frontend lint/build | Present | Gate in CI |
| Backend unit tests | Not substantive | Add |
| API/integration | Not mature | Add contracts/integration |
| E2E | Not mature | Critical journeys |
| Router tests | Not mature | Deterministic + eval dataset |
| RAG eval | Not mature | Retrieval + generation eval |
| Coding validation | Basic parsing only | Schema + build/test |
| Authorization tests | Not mature | Ownership regression |
| Payment replay tests | Not mature | Idempotency/concurrency |
| Performance tests | Not mature | load/stress/spike/soak |
| Failure tests | Not mature | dependency/fault testing |
| Logs | CloudWatch awslogs | Structured logs |
| Metrics | Limited/basic AWS | Application + AI metrics |
| Correlation IDs | Not mature | End-to-end |
| Tracing | Not verified | Distributed tracing |
| AI quality dashboard | Not present | Proposed |

---

# What Not to Say

Do not say:

- “NovaMind has complete automated test coverage.”
- “The backend has a mature unit-test suite.”
- “We have full E2E automation.”
- “RAG quality is fully benchmarked.”
- “The router has verified 95%+ accuracy.”
- “Search answers are always cited correctly.”
- “Generated code is automatically compiled and tested.”
- “CloudWatch Logs means full observability.”
- “We use distributed tracing.”
- “We use MLflow/DVC in this project.”
- “LLM-as-a-judge gives objective truth.”
- “RAG eliminates hallucination.”
- “100% code coverage means production-ready.”
- “The project has been fully tested in live production.”

---

# Final Self-Test

Before Module 19, explain without notes:

- testing vs evaluation
- monitoring vs observability
- unit/integration/API/E2E
- test pyramid
- mock/stub/fake
- regression testing
- contract testing
- router logic testing
- router quality evaluation
- golden dataset
- confusion matrix
- precision/recall
- RAG retrieval vs generation evaluation
- Recall@K / Precision@K
- hit rate
- MRR concept
- groundedness
- faithfulness
- no-answer evaluation
- search/chat/coding evaluation
- structured-output validation
- auth/authz tests
- payment/idempotency tests
- Redis memory tests
- performance/load/stress/spike/soak
- failure/recovery testing
- logs/metrics/traces
- structured logging
- p50/p95/p99
- correlation IDs
- AI observability
- prompt versioning
- offline/online eval
- human evaluation
- LLM-as-judge
- prompt/model regression
- cost evaluation
- security/prompt-injection testing
- CI quality gates
- Production V2

**Module 18 interview preparation complete.**
