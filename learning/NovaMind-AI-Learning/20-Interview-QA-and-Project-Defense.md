# Module 20 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Security, Limitations, Design Decisions and Production V2  
> **Purpose:** Prepare for security, design-defense, limitation, trade-off, production-readiness and pressure interview questions with accurate NovaMind claims.

---

## Accuracy Rules

### CURRENT VERIFIED

```text
Firebase ID-token verification
opaque Redis UUID application session
HTTP-only cookie
Secure + SameSite=None in production
Gateway session lookup / identity propagation
Razorpay HMAC verification
Multer MIME + 20 MiB limit
S3 presigned URLs
sandboxed iframe preview
Secrets Manager references
CloudWatch logging
```

### CURRENT LIMITATIONS

```text
authorization / ownership gaps
sensitive public plan/credit mutation paths
alternate admin-route exposure
tracked credential exposure
partial session revocation
no mature CSRF strategy
internal service identity not mature
prompt-injection defense not mature
payment replay / non-atomic credits
HTTP 200 can hide workflow failure
limited tests/evals/observability
no verified mature HA
```

### PRODUCTION V2 — PROPOSED

```text
centralized authorization
server-derived identity
credential rotation
idempotent credit ledger
session revocation/rotation
CSRF controls
structured errors
persistent document/artifact ownership
prompt-injection testing
correlation IDs / metrics / tracing
immutable releases
HA / backups / RTO/RPO
```

### NOT PRESENT / DO NOT CLAIM

```text
Bedrock inference
Bedrock Agents / Knowledge Bases
autonomous planning
reflection loop
LangGraph checkpointing
Kubernetes
model training/fine-tuning
MLflow/DVC/model registry
drift detection
comprehensive IaC
mature security certification
production readiness
```

---

# Security Foundations

## Q1. What is information security?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Protecting data, identities, operations and systems from unauthorized access, change, disclosure or disruption.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q2. What is the CIA triad?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Confidentiality, Integrity and Availability.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q3. What is confidentiality?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Only authorized users/systems can access protected data.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q4. What is integrity?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Data/actions cannot be changed incorrectly or without authorization.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q5. What is availability?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> The service remains usable when required.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Authentication and Sessions

## Q6. How does NovaMind authenticate users?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Google sign-in produces a Firebase ID token, Auth verifies it, finds/creates the user, then creates an opaque UUID app session in Redis and returns it in an HTTP-only cookie.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q7. Is the NovaMind application session a JWT?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q8. Firebase token vs app session?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Firebase ID token is used during login verification; the app session is a separate opaque Redis UUID.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q9. What is the verified session TTL?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Seven days in the login flow.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q10. What does HTTP-only protect against?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> It prevents normal browser JavaScript from directly reading the cookie.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q11. What does Secure mean?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Cookie is sent over HTTPS.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q12. What does SameSite control?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Whether cookies are sent in cross-site requests.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q13. Is session revocation mature?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No, it is partial.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q14. Why is Redis a security dependency?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Protected requests depend on Redis session validation.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Authorization

## Q15. Authentication vs authorization?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Authentication proves identity; authorization decides allowed actions/resources.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q16. What is NovaMind's biggest security gap?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Authorization/ownership boundaries are incomplete.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q17. What is resource ownership?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Checking that the authenticated user owns or is allowed to access the requested resource.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q18. What is IDOR?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Accessing another user's object by manipulating an identifier without a proper authorization check.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q19. What resource areas have verified gaps?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Message retrieval, conversation title/update and message creation.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q20. What should authorize a resource?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Trusted authenticated user ID compared with server-side resource ownership.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Sensitive Mutation Routes

## Q21. What sensitive route concern exists?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Public `/api/auth` proxy paths expose account/credit mutation operations such as update-plan and deduct-credits.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q22. Why is client-supplied user ID dangerous?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> A client must not be able to choose which account receives a sensitive mutation.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q23. How should V2 handle it?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Derive user ID from validated session and enforce server-side authorization.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Admin Security

## Q24. What admin-route concern was verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> An alternate public path can reach admin handlers, weakening the intended authorization boundary.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q25. Is hiding admin UI sufficient?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q26. What should protect admin routes?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Authenticated identity plus server-side role/permission checks.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# CSRF and CORS

## Q27. What is CSRF?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Tricking a browser into sending an authenticated state-changing request.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q28. Why is cookie auth relevant to CSRF?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Browsers automatically attach cookies.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q29. Does CORS stop CSRF?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q30. What is CORS?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> A browser cross-origin access policy.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q31. Is a mature explicit CSRF strategy verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q32. What V2 controls could be added?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> CSRF token, Origin/Referer validation, SameSite review and re-authentication for sensitive operations.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Credential Exposure

## Q33. What credential issue was found?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> MongoDB connection credentials/information appeared in tracked ECS task-definition configuration.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q34. Why isn't deleting the secret enough?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Git history may still contain it.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q35. What is the correct response?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Rotate/revoke it, remove exposure, inspect history, scan the repo, move runtime secret to a secret store and prevent recurrence.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q36. What local Firebase credential fact is relevant?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> A local Firebase key/file existed but was ignored from Git.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Secrets and IAM

## Q37. Does NovaMind use Secrets Manager references?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Yes, task definitions contain Secrets Manager references.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q38. Does that prove every secret is safe?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q39. Execution role vs task role?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Execution role is used by ECS startup/platform operations; task role is used by application code for AWS API calls.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q40. What is least privilege?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Only required actions on required resources.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q41. Are effective IAM policies fully verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Network and Service Security

## Q42. What is Cloud Map used for?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Service discovery.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q43. Does Cloud Map authenticate services?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q44. Is mature service-to-service authentication verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q45. What is zero trust?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Do not automatically trust requests just because they are internal.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q46. Is the full private/multi-AZ topology verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No, it is substantially documented/intended rather than comprehensively live-verified.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# File Security

## Q47. What upload controls are verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Multer MIME checks and a 20 MiB limit.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q48. Why isn't MIME check enough?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Metadata can be spoofed.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q49. What temp-file risk exists?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Some error paths can leave temporary files.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q50. What V2 controls could help?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Magic-byte validation, stricter cleanup, lifecycle, optional malware scanning where required.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# S3 and Artifacts

## Q51. What is a presigned URL?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> A temporary bearer link granting access to a specific S3 object.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q52. Does URL expiry delete the object?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q53. What artifact lifecycle gap exists?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No mature artifact ownership/metadata/renewal lifecycle.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q54. How would V2 improve it?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Persist artifactId/owner/objectKey metadata and authorize before issuing a fresh URL.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Generated Code Security

## Q55. How is code preview constrained?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> A sandboxed browser iframe.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q56. Does NovaMind execute arbitrary backend code?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q57. Does iframe sandbox equal secure server code execution?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q58. Why is not executing arbitrary backend code safer?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> It avoids a major remote-code execution surface.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Prompt Injection

## Q59. What is prompt injection?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Untrusted content tries to manipulate model instructions.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q60. What NovaMind sources can contain it?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> User prompts, PDFs and web-search results.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q61. How should retrieved text be treated?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> As untrusted data, not privileged instructions.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q62. Is mature prompt-injection defense verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# RAG and Search Security

## Q63. What are RAG security concerns?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Document ownership, vector ownership, retention, cross-tenant access and prompt injection.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q64. Does current request-oriented RAG provide persistent tenant isolation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q65. Are Tavily results trusted instructions?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q66. What must persistent V2 RAG add?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Document identity, ownership, S3/Qdrant mapping, authorization and retention.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Model Output Security

## Q67. Should LLM output be trusted?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q68. What failures can model output contain?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Malformed JSON, unsafe code/HTML, bad commands and malicious links.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q69. What should privileged actions require?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Validation and explicit authorization.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Payments and Credits

## Q70. What payment security control is verified?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Razorpay HMAC signature verification.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q71. Does signature verification solve replay?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q72. What partial failure exists?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Payment can be marked paid before Auth successfully grants credits.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q73. What is idempotency?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Repeated logical operation causes one business effect.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q74. What does exactly-once business effect mean?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Use idempotency so repeated deliveries do not repeat the business mutation.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q75. What credit-helper weakness exists?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Provider work may continue even when credit deduction helper fails/returns null.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Session Security

## Q76. What is session fixation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Forcing a victim to use an attacker-known session identifier.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q77. What is session hijacking?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Stealing/reusing a valid session.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q78. What does session rotation help with?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Reducing fixation and stale-security-context risks.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q79. Is revoke-all-sessions current?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Logging and Privacy

## Q80. Why can logs be a security risk?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> They can contain prompts, documents, identifiers, tokens or secrets.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q81. What should be redacted?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Secrets, tokens, DB URIs and sensitive content.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q82. What privacy lifecycle is incomplete?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Retention/deletion for artifacts, vector collections, uploads and logs.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Compliance

## Q83. Security vs compliance?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Security controls do not automatically equal certification/compliance.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q84. Can you claim SOC2/ISO/HIPAA/PCI/GDPR?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No, not from current evidence.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q85. Does Razorpay make the platform PCI compliant?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Threat Modeling

## Q86. What is threat modeling?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Systematically identifying assets, attackers, attack paths, impact and mitigations.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q87. What assets exist?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Accounts, sessions, conversations, uploads, artifacts, credits, payments and credentials.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q88. What is STRIDE?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service and Elevation of Privilege.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q89. Give a broken-access example.

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> User B reads User A's conversation.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Defense in Depth

## Q90. What is defense in depth?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Multiple independent controls reduce risk if one fails.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q91. Give a NovaMind example.

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Session auth + resource ownership + network restrictions + least-privilege IAM + logging.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — Services

## Q92. Why five services?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> They separate Gateway, Auth, Chat, Agent and Billing responsibilities.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q93. What is the trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Synchronous coupling, distributed failures and operational complexity.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q94. What is a simpler alternative?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> A modular monolith.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q95. When might modular monolith be better?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Small team, low independent scaling needs, simpler transactions/operations.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — LangGraph

## Q96. Why use LangGraph?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Explicit state, nodes, conditional routing and extensibility.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q97. Trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Framework overhead for a currently bounded graph.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q98. Alternative?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Plain JavaScript routing/functions.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q99. Is LangGraph autonomous here?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — Redis

## Q100. Why Redis sessions?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Centralized server-side session state with opaque IDs.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q101. Trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Critical dependency, HA and TTL/revocation complexity.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q102. Alternative?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Signed token/JWT-based session.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q103. Is JWT automatically better?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — Multiple Providers

## Q104. Why multiple providers?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Different providers support different task capabilities.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q105. Trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> More credentials, quotas, cost and output variability.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q106. Does multiple providers equal automatic failover?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — Qdrant

## Q107. Why Qdrant?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Semantic vector retrieval for PDF RAG.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q108. Trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Extra service, lifecycle, embedding cost and region considerations.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q109. Alternative?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Another vector DB, DB vector extension or direct context for small documents.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — S3

## Q110. Why S3 for artifacts?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Scalable object storage and presigned delivery.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q111. Trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Ownership, retention, expiration and storage lifecycle.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — Fargate

## Q112. Why Fargate?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Container deployment without managing EC2 hosts.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q113. Trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Baseline cost and networking/IAM/deployment complexity.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q114. Is Fargate always cheaper?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Design Decisions — Sync vs Async

## Q115. Why synchronous AI calls?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Simple request-response user experience.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q116. Trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Long-held connections and timeout/concurrency limits.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q117. What future alternative exists?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Async job/queue/worker pattern for long tasks.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Production Readiness

## Q118. Is NovaMind production-ready?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> I would describe it as production-oriented but not fully production-ready.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q119. Why not?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Authorization, financial consistency, testing/eval, observability, release safety, lifecycle and HA need hardening.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q120. Does deployed mean production-ready?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Limitations

## Q121. Top security limitation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Authorization/ownership boundaries.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q122. Top money limitation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Payment/credit idempotency and partial consistency.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q123. Top RAG limitation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Request-oriented document lifecycle with no durable ownership/index mapping.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q124. Top testing limitation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No substantive backend/AI-eval suite.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q125. Top observability limitation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Basic logs but no mature correlation/tracing/AI quality telemetry.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q126. Top HA limitation?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No verified Multi-AZ or stateful failover.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Production V2 Priorities

## Q127. What is P0?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Credential rotation and authorization fixes.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q128. What is P1?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Payments/credits/sessions correctness.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q129. What is P2?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Tests/evals/reliability controls.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q130. What is P3?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Persistent RAG/artifact lifecycle.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q131. What is P4?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Observability/release safety.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q132. What is P5?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Scaling/HA/cost/DR.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q133. Why security before scaling?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Scaling a security or accounting bug increases blast radius.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Incident Scenarios

## Q134. User A reads User B conversation. Root issue?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Authorization/ownership failure, not authentication.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q135. Credential found in Git. First action?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Rotate/revoke the credential.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q136. Duplicate Razorpay callback arrives. What prevents double credit?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Idempotent processing keyed by payment/event identity.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q137. Redis session store is down. Protected request behavior?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Fail closed is generally safer.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q138. PDF contains malicious instructions. What do you do?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Treat document text as untrusted data and keep tool/system authority separate.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q139. Presigned URL is shared. Risk?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Anyone with the bearer URL may use it until expiration.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q140. Normal user reaches admin route. Fix?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Server-side role/permission authorization.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Security Tradeoffs

## Q141. Shorter session TTL trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> More security, more login friction.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q142. Shorter presigned URL trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Smaller exposure window, more renewal requests.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q143. Strict validation trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Safer but may reject unusual valid content.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q144. Fail closed trade-off?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Stronger security but lower availability during auth-store outage.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Ownership Safety

## Q145. Does repository evidence prove you personally built everything?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q146. How should you phrase uncertain ownership?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> The project implements / the architecture uses / the current implementation.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Pressure Questions

## Q147. If authentication is implemented, why is authorization still a problem?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Knowing who the user is does not prove they can access a specific resource.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q148. Why not trust x-user-id from internal requests?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Headers can be forged unless identity is derived and protected by trusted server-side boundaries.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q149. Why not use JWT and remove Redis?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> JWT reduces session lookup but complicates revocation/stale claims; requirements decide.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q150. Why not split all services further for security?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> More services do not automatically improve security and can expand operational attack surface.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q151. Why isn't Secrets Manager enough?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> It does not undo previously exposed credentials or prove every secret/IAM policy is safe.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q152. Why isn't HMAC verification enough for payments?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Authenticity does not solve replay or cross-service consistency.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q153. If prompt injection is only text, why is it dangerous?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> The model may treat malicious data as instructions, especially when tools/actions are available.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q154. Why not call the app production-ready if it runs on ECS?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Runtime deployment does not prove security, testing, observability, HA or recovery maturity.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

## Q155. What should be fixed first?

**What the interviewer is testing:** Whether you understand the difference between authentication, authorization, secure design, production readiness and architectural trade-offs.

**Word-for-word answer:**

> Credential exposure and authorization, then money/session correctness.

**Likely follow-up:** I would explain **the trust boundary, the current verified control, the remaining limitation, the attack/failure impact, and the Production V2 mitigation without claiming it is already implemented**.

**Project-defense reminder:** Security and production readiness must be demonstrated by controls and evidence, not by the fact that the system is deployed.

---

# Rapid-Fire Revision

**Q156. App session JWT?**  
No.

**Q157. App session type?**  
Opaque UUID in Redis.

**Q158. Login token?**  
Firebase ID token.

**Q159. Session TTL?**  
7 days in verified login flow.

**Q160. Auth implemented?**  
Yes.

**Q161. Authorization mature?**  
No, partial.

**Q162. Main security gap?**  
Broken/partial access control and ownership.

**Q163. CSRF strategy mature?**  
No.

**Q164. CORS = auth?**  
No.

**Q165. Cloud Map = service auth?**  
No.

**Q166. Presigned URL expiry deletes S3 object?**  
No.

**Q167. Razorpay HMAC current?**  
Yes.

**Q168. Payment idempotency mature?**  
No.

**Q169. Prompt injection defense mature?**  
No.

**Q170. Secrets Manager refs current?**  
Yes.

**Q171. Perfect least privilege verified?**  
No.

**Q172. Server-side arbitrary code execution?**  
No.

**Q173. Bedrock active?**  
No.

**Q174. LangGraph checkpointing?**  
No.

**Q175. Production-ready?**  
Not fully.

**Q176. Top P0?**  
Credential rotation + authorization fixes.

# Cross-Question Chain 1 — Authentication vs Authorization

**Interviewer:** You already verify users with Firebase. Why do you say security is incomplete?

> Firebase verification solves identity at login, but authorization is a separate question. A logged-in user still must be prevented from accessing or mutating another user's resources. The repository review found ownership and sensitive account-mutation gaps, so authentication is stronger than authorization in the current version.

---

# Cross-Question Chain 2 — Sessions

**Interviewer:** Why not use JWT instead of Redis?

> The Redis-backed opaque session gives centralized server-side state and makes revocation conceptually easier. JWT removes the session lookup but makes revocation and stale claims harder. The right choice depends on requirements; JWT is not automatically more secure or scalable.

---

# Cross-Question Chain 3 — Payment Security

**Interviewer:** You verify Razorpay HMAC, so why is payment still risky?

> HMAC proves the callback is authentic. It does not make the business operation idempotent or atomic across Billing and Auth. The current flow can mark a payment paid before credits are successfully granted, and repeated callbacks can create repeated effects unless processing is idempotent.

---

# Cross-Question Chain 4 — Secrets

**Interviewer:** You use Secrets Manager. Why was credential exposure still a problem?

> Secrets Manager references exist, but one tracked task-definition configuration included MongoDB credential information. Secret management must cover the full lifecycle: preventing commits, rotating exposed values, minimizing IAM permissions and scanning history.

---

# Cross-Question Chain 5 — Prompt Injection

**Interviewer:** How can a PDF attack an LLM?

> The PDF can contain text that looks like instructions. If the model treats retrieved document text as trusted authority rather than untrusted data, it can be manipulated. The defense is strong instruction/data separation, constrained tools, output validation and adversarial evaluation.

---

# Cross-Question Chain 6 — Microservices

**Interviewer:** Why not combine everything into one service?

> A modular monolith could absolutely be a valid simpler architecture. The current five-service design gives clearer runtime responsibilities, but adds synchronous coupling and operational complexity. I would keep or split boundaries only where scaling, ownership or reliability needs justify them.

---

# Cross-Question Chain 7 — LangGraph

**Interviewer:** Isn't LangGraph overkill for simple routing?

> It may be more framework than strictly required for the current bounded graph. The benefit is explicit state, nodes and conditional edges plus room for controlled workflow growth. If the graph stays simple, plain JavaScript routing is a valid alternative.

---

# Cross-Question Chain 8 — Production Readiness

**Interviewer:** It's deployed to ECS, so why isn't it production-ready?

> Deployment proves the software can run in AWS. Production readiness also requires strong authorization, idempotent financial operations, test/evaluation coverage, observability, release safety, data lifecycle, backup/recovery and verified HA. Several of those remain incomplete.

---

# Security Incident Walkthrough 1 — Cross-User Data Access

```text
Symptom:
User B accesses User A's conversation.

1. Authentication may be valid.
2. Identify missing ownership check.
3. Block request server-side.
4. Add resource.ownerId comparison.
5. Audit other object routes.
6. Add regression test.
7. Add security log/alert if needed.
```

---

# Security Incident Walkthrough 2 — Secret in Git

```text
1. Rotate credential immediately.
2. Revoke old value.
3. Replace with Secrets Manager reference.
4. Inspect repository history.
5. Run secret scanning.
6. Review IAM/database permissions.
7. Add CI secret-scanning prevention.
```

---

# Security Incident Walkthrough 3 — Duplicate Payment Callback

```text
1. Verify HMAC.
2. Identify payment/event ID.
3. Check processed-event store.
4. If already processed: return safely.
5. If new: apply idempotent credit ledger mutation.
6. Mark processed.
7. Reconcile balance/payment state.
```

---

# Security Incident Walkthrough 4 — Redis Outage

```text
Protected request
↓
session cannot be verified
↓
fail closed
↓
return safe temporary error
↓
alert / recover Redis
```

Do not trust client identity just because Redis is unavailable.

---

# Security Incident Walkthrough 5 — Malicious PDF

```text
PDF contains:
"Ignore system instructions..."

Treat as untrusted data.
Do not grant new tool permissions.
Do not expose system prompt.
Validate model output.
Run prompt-injection evaluation.
```

---

# 30-Second Security Answer

> NovaMind has real security controls including Firebase verification, Redis-backed HTTP-only sessions, Razorpay signature verification, upload limits, S3 presigned access and Secrets Manager references. The biggest current gap is authorization rather than authentication: resource ownership and some sensitive account/admin mutation boundaries are incomplete. I would fix authorization and any exposed credentials first, then payment idempotency and session revocation before scaling further.

---

# 60–90 Second Security / Limitations Answer

> NovaMind's authentication flow is real: Firebase verifies Google identity, then the application creates a separate opaque UUID session in Redis and uses an HTTP-only cookie. The limitation is that authorization and tenant isolation are only partial. The code review found sensitive account/credit mutation paths, an alternate admin route and missing ownership checks for some conversation/message operations.
>
> There is also a credential-management issue from tracked DB configuration, and payment consistency is not fully idempotent because payment can be marked paid before credit grant completes. AI security matters too because PDFs and web search results are untrusted content and can contain prompt-injection text.
>
> Production V2 should start with credential rotation and centralized ownership/role authorization, then idempotent payment/credit accounting and complete session revocation. After that I would strengthen tests, persistent document/artifact ownership, observability, immutable deployments and HA.

---

# 2–3 Minute Production-Readiness Defense

> NovaMind has meaningful production-oriented engineering, but I would not call the current version fully production-ready. On security, the platform has real controls: Firebase token verification, opaque server-side Redis sessions, HTTP-only cookies, Razorpay HMAC verification, upload size/MIME validation, S3 presigned URLs, a sandboxed browser preview and Secrets Manager references.
>
> The main gap is authorization. Authentication confirms identity, but several operations do not consistently verify resource ownership or privileged access. The review found sensitive plan/credit mutation routes, an alternate admin path and ownership gaps around conversation/message operations. I would make all security-sensitive user identity server-derived from the validated session and perform ownership or role checks inside the service handling the resource.
>
> Payment consistency is another production-readiness issue. Authenticating the Razorpay callback is not enough; the system needs idempotent processing and reconciliation because a payment may be marked paid before credits are granted. I would use a stable payment/event ID and an auditable credit ledger so repeated callbacks produce one business effect.
>
> AI security adds another trust boundary. Uploaded PDFs and Tavily results are external/untrusted data, not trusted instructions. Model output is also untrusted and needs structured validation before privileged use.
>
> Architecturally, the five services improve separation but introduce synchronous coupling. LangGraph gives explicit state and routing but the current graph is bounded, so plain control flow would be a valid alternative if complexity stayed low. Redis sessions give centralized revocation potential but create a critical HA dependency. Multiple AI providers specialize workloads but add operational and cost complexity.
>
> My V2 roadmap is risk-first: P0 credentials and authorization; P1 payments, credits and sessions; P2 tests/evals/reliability; P3 persistent RAG and artifact lifecycle; P4 observability and release safety; P5 scaling, HA, DR and cost optimization. The principle is to fix security and correctness before increasing scale.

---

# Top 5 Limitations — Word-for-Word

> My top five limitations are, first, authorization and ownership checks are incomplete. Second, payment and credit accounting need idempotency and reconciliation. Third, automated software testing and AI evaluation are still limited. Fourth, PDF RAG and generated artifacts do not yet have a mature persistent ownership and lifecycle model. Fifth, observability, deployment safety and high availability are not maturely verified. I would address them in that order based on security and business risk.

---

# What Would You Improve First? — Word-for-Word

> I would first rotate any exposed credentials and close authorization gaps around account mutation, admin functions and resource ownership. Those are higher risk than performance optimization. After that I would make payment and credit changes idempotent and auditable, then improve session revocation, testing and observability.

---

# Why Not Production Ready Yet? — Word-for-Word

> Because production readiness includes more than successful deployment. The project still needs stronger authorization, financial consistency, session revocation, automated tests and AI evaluations, observability, release safety, persistent document/artifact lifecycle and verified HA and recovery.

---

# What Security Issue Worries You Most? — Word-for-Word

> Broken or incomplete authorization concerns me most because the user can be correctly authenticated and still access or mutate something they do not own. I would enforce ownership and role checks server-side using the trusted session identity, never a client-supplied user ID.

---

# Why Microservices? — Word-for-Word

> From an engineering perspective, the five-service structure separates Gateway, Auth, Chat, AI orchestration and Billing responsibilities. The benefit is clearer boundaries and potential independent scaling, but the trade-off is distributed complexity and synchronous coupling. If the team or scale did not require those boundaries, a modular monolith would be a reasonable simpler alternative.

---

# Is LangGraph Over-Engineering? — Word-for-Word

> It can be argued that LangGraph is more framework than strictly required for the current bounded router. Its value is that state, nodes and conditional routing are explicit and extensible. If the workflow remained simple, I would consider plain JavaScript routing; if it became more stateful or cyclic, LangGraph's structure becomes more valuable.

---

# Why Not JWT? — Word-for-Word

> Redis-backed opaque sessions give the application centralized session state and make revocation conceptually easier. JWTs remove the session lookup but make immediate revocation and stale claims more difficult. I would choose based on the security and scaling requirements rather than assuming one is always better.

---

# Why Multiple Providers? — Word-for-Word

> NovaMind uses specialized providers for different jobs: Groq for text generation, Gemini for embeddings and image analysis, OpenRouter/DeepSeek for coding, Stability for image generation and Tavily for search. The advantage is capability specialization; the trade-off is more credentials, quotas, latency and cost complexity.

---

# Why Qdrant? — Word-for-Word

> Qdrant gives the PDF RAG workflow semantic vector storage and similarity search. The trade-off is another infrastructure dependency plus index lifecycle, embedding cost and ownership requirements. A database vector extension could be a simpler alternative for some architectures.

---

# Why Fargate? — Word-for-Word

> Fargate lets the application run containerized services without managing EC2 hosts. That simplifies host operations, but it still requires careful IAM, networking, deployment and observability, and it can have baseline cost. It is not automatically the cheapest option.

---

# How Would You Redesign Production V2? — Word-for-Word

> I would redesign V2 in phases. First, rotate exposed credentials and centralize authorization so user and admin actions are based on trusted server-side identity. Second, make payment and credit operations idempotent and auditable and improve session revocation. Third, add unit, integration, authorization, payment, router and RAG evaluation gates plus structured errors and timeouts. Fourth, create persistent document and artifact ownership/lifecycle. Fifth, add correlation IDs, metrics, traces, immutable deployments, smoke tests and rollback. Only after those correctness controls would I add measured autoscaling, async workers for long operations, stateful HA, backups, RTO/RPO and cost-per-workflow telemetry.

---

# What Not to Say

Do not say:

- “Our app session is JWT.”
- “Authentication means authorization is solved.”
- “CORS protects us from CSRF.”
- “Cloud Map authenticates internal services.”
- “All resources have tenant isolation.”
- “All secrets are safe because we use Secrets Manager.”
- “Razorpay signature verification makes payments idempotent.”
- “Presigned URL expiry deletes the S3 object.”
- “Multiple providers give automatic failover.”
- “The iframe is a secure backend code sandbox.”
- “Prompt injection is impossible because we use RAG.”
- “The project is PCI/SOC2/ISO/HIPAA/GDPR compliant.”
- “AWS deployment means production-ready.”
- “We have zero trust.”
- “We have mature HA.”
- “I personally implemented every component,” unless true and confirmable.

---

# Final Self-Test

Before Module 21, explain without notes:

- CIA triad
- authentication vs authorization
- Firebase token vs Redis session
- HTTP-only / Secure / SameSite
- session TTL / rotation / revocation
- CSRF vs CORS
- trust boundaries
- IDOR / resource ownership
- sensitive credit/plan routes
- admin authorization
- credential exposure/rotation
- Secrets Manager
- execution role vs task role
- least privilege
- Cloud Map vs service auth
- file validation
- temp-file security
- presigned URLs
- artifact ownership
- prompt injection
- RAG/search trust
- model output validation
- payment HMAC vs idempotency
- credit consistency
- logging/privacy
- compliance vs certification
- threat modeling / STRIDE
- defense in depth
- zero-trust concept
- five-service trade-offs
- LangGraph trade-offs
- Redis sessions trade-offs
- multiple providers trade-offs
- Qdrant trade-offs
- S3 trade-offs
- Fargate trade-offs
- sync vs async
- production readiness
- current limitations
- P0–P5 roadmap

**Module 20 interview preparation complete.**
