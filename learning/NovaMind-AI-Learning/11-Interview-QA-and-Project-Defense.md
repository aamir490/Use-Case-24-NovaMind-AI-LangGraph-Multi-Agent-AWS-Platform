# Module 11 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Authentication, Authorization and Session Security  
> **Purpose:** Prepare for deep authentication/security interviews while defending only the verified NovaMind implementation.

---

## Accuracy Rules

### Confident current claims

```text
Google sign-in uses Firebase.
Firebase ID token is verified at login.
NovaMind then creates its own opaque UUID server-side session.
Session state is stored in Redis.
The application session is NOT a JWT.
Verified TTL is about 7 days.
The browser receives an HTTP-only cookie.
Production cookie settings include Secure and SameSite=None.
Gateway resolves Redis session and forwards trusted identity.
MongoDB stores the durable user record.
```

### Current gaps

```text
public /api/auth account/credit mutation exposure
alternate/public admin path
incomplete resource ownership checks
tracked MongoDB credential exposure
incomplete logout/session revocation
stale sessions after account changes
no mature explicit CSRF strategy
no verified strong internal service identity
partial file validation
prompt injection risk
credit-helper failure
payment replay/non-atomic account state
```

### Do not claim

```text
JWT app sessions
complete RBAC
complete tenant isolation
mTLS
zero-trust networking
Cognito
AWS API Gateway authentication
Bedrock Agents authentication
mature CSRF protection
production readiness
```

---
# Authentication Fundamentals

## Q1. What is authentication?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authentication proves who the user is.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q2. What is authorization?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authorization decides what an authenticated user is allowed to access or change.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q3. What is the difference between authentication and authorization?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authentication establishes identity; authorization checks permission on a specific action or resource.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q4. Can secure login coexist with insecure data access?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes. A valid login does not prevent cross-user access if ownership checks are missing.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q5. What is identity?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The server-side representation of the authenticated user.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q6. What is a session?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Application state that remembers an authenticated user across multiple requests.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q7. What is resource ownership?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> A rule linking a specific resource to the user or tenant allowed to access it.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q8. What is tenant isolation?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Preventing User A from accessing User B's data.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q9. Can an LLM enforce authorization?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No. Authorization must be deterministic backend logic.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# NovaMind Login Flow

## Q10. How does NovaMind login work?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The user signs in with Google through Firebase, the frontend sends the Firebase ID token to the backend, Auth verifies it, finds or creates the MongoDB user, creates an opaque UUID session in Redis, and returns the session credential in an HTTP-only cookie.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q11. What is Firebase used for?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Initial Google identity verification.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q12. What is the Firebase ID token used for?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> It proves the Firebase/Google identity during login.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q13. What happens after token verification?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> NovaMind resolves the application user and creates its own server-side session.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q14. Where is the user stored?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> MongoDB.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q15. Where is the app session stored?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Redis.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q16. Is the app session a JWT?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q17. What is the session TTL?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Approximately seven days.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q18. What cookie properties are verified?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> HTTP-only, and in production Secure plus SameSite=None.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q19. Does Firebase replace NovaMind sessions?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q20. What is the user-session pointer?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> A verified Redis-side association used alongside the session snapshot; I would not overstate it beyond that.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Firebase vs Session

## Q21. What is the difference between Firebase ID token and NovaMind session?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The Firebase token proves identity at login; the Redis session maintains ongoing app authentication.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q22. Why use an opaque session?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> It keeps session state server-side and allows application-controlled validation/revocation.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q23. What is the main trade-off?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Redis becomes a critical dependency.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q24. Does the browser need to decode the session ID?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q25. Where does full session state live?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Server-side in Redis.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Authenticated Request Flow

## Q26. What happens on a later protected request?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The browser sends the cookie, Gateway looks up the Redis session, resolves the trusted user, and forwards that identity to the target service.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q27. What happens if the cookie is missing?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The protected request should fail authentication.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q28. What happens if the Redis session expired?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The cookie no longer represents a valid app session and the user must re-establish one.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q29. What happens if Redis is unavailable?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authenticated requests can fail because Gateway cannot validate the server-side session.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q30. Should the backend accept a body userId if Redis is down?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q31. What is x-user-id used for?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Internal propagation of the trusted server-resolved user identity.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q32. Can a client choose x-user-id?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Authorization and Ownership

## Q33. After authentication, what must happen before reading a conversation?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Verify the authenticated user is authorized for that conversation.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q34. Why is conversationId not authorization?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The client can change IDs; an ID does not prove ownership.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q35. What ownership gaps were found?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Incomplete checks around message retrieval, title operations and message creation.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q36. What is an IDOR-style issue conceptually?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> A user changes a resource identifier and accesses another user's object because ownership was not enforced.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q37. How do you fix ownership?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Scope resource lookup to the authenticated owner or run an explicit authorization policy.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q38. What should happen when User A requests User B's conversation?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Deny with an authorization failure, typically 403.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q39. Is frontend hiding enough?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No. Backend enforcement is mandatory.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Public Account Mutation

## Q40. What serious route issue was identified?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Public `/api/auth` routing exposes account/credit mutation routes such as `/update-plan` and `/deduct-credits`, with identity potentially taken from request data.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q41. Why is that severe?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> A client may attempt to mutate another user's account or credits.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q42. What is the correct identity source?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The authenticated server-side session identity.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q43. Does CORS make these endpoints secure?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q44. Would renaming the endpoint solve it?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No. Authorization logic must change.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Admin Security

## Q45. How is admin access represented today?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The project includes admin logic based on an email comparison.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q46. Is that mature RBAC?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q47. What admin routing weakness exists?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> An alternate/public route can reach admin handlers.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q48. Why is alternate routing dangerous?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Security can be bypassed even if the primary route is protected.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q49. How should admin routes be tested?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Unauthenticated, normal-user and authorized-admin cases for every route mount.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q50. What is RBAC?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Role-Based Access Control.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q51. Is complete RBAC verified?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Cookies and Browser Security

## Q52. What does HTTP-only do?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Reduces direct JavaScript access to the session cookie.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q53. What does Secure do?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Limits sending the cookie to HTTPS.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q54. What does SameSite control?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Cross-site cookie behavior.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q55. What SameSite value is verified in production?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> None.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q56. Does HTTP-only prevent CSRF?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q57. Does HTTP-only eliminate XSS?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q58. Does Secure fix authorization bugs?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# CSRF

## Q59. What is CSRF?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Cross-Site Request Forgery: another site tries to trigger authenticated state-changing requests using the victim's cookies.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q60. Why does SameSite=None matter?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Cross-site cookie sending makes an explicit CSRF strategy especially important.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q61. Is CORS the same as CSRF protection?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q62. Is a mature explicit CSRF strategy verified?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q63. What are future CSRF options?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> CSRF tokens, origin/referer validation and appropriate SameSite policy.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# XSS

## Q64. What is XSS?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Cross-Site Scripting: malicious JavaScript runs in the trusted application origin.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q65. Can XSS still act as the user with HTTP-only cookies?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes, even if it cannot directly read the cookie.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q66. Does the coding iframe create a complete secure sandbox?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No. It provides some browser isolation but is not a full secure arbitrary-code execution environment.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# CORS

## Q67. What is CORS?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> A browser cross-origin response-sharing policy.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q68. Is CORS authentication?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q69. Is CORS authorization?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q70. Can direct API clients ignore browser CORS?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Internal Service Security

## Q71. How do internal NovaMind services communicate?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Through internal HTTP/service-discovery patterns such as Agent→Chat, Agent→Auth and Billing→Auth.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q72. Does private networking authenticate the caller?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q73. Does Cloud Map authenticate the caller?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q74. Is mTLS verified?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q75. Is strong service identity verified?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q76. What should Production V2 consider?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authenticated service-to-service calls using a mechanism appropriate to the deployment.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Sessions and Revocation

## Q77. What is session revocation?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Server-side invalidation of an existing app session.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q78. Does clearing the browser cookie guarantee revocation?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q79. Is current revocation mature?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q80. What is a stale session snapshot?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Redis session state that no longer matches the latest user/account state.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q81. Do admin changes automatically invalidate old sessions?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No mature universal mechanism is verified.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q82. What would session versioning do?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Allow sensitive changes to invalidate older sessions.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q83. What should logout ideally do?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Revoke/delete the Redis session, clear the cookie and update session pointers where appropriate.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# 401 vs 403

## Q84. What does 401 mean?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authentication is missing or invalid.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q85. What does 403 mean?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The user is authenticated but forbidden from the requested action/resource.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q86. Expired session: 401 or 403?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Typically 401.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q87. Other user's conversation: 401 or 403?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Typically 403 after valid authentication.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Secrets

## Q88. How should secrets be managed in AWS?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Prefer managed secret delivery such as Secrets Manager with scoped IAM.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q89. Are Secrets Manager references present?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q90. What credential problem was found?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> MongoDB credentials were tracked in task-definition/source context.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q91. What should happen after exposure?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Rotate/revoke the credential and replace hard-coded values with managed secrets.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q92. Can you claim rotation already happened?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No, not without verification.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q93. What about the local Firebase key?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> It exists locally but is ignored from source control; secure local handling is still required.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# IAM

## Q94. What is least privilege?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Grant only the minimum permissions required.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q95. Execution role vs task role?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Execution role supports ECS startup operations; task role is used by app code for AWS APIs.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q96. Does a role name prove least privilege?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q97. Were all effective policies live-inspected?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# File Upload Security

## Q98. What upload controls are verified?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Multer MIME checks and an approximately 20 MiB size limit.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q99. Why is MIME validation partial?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Client-provided MIME data can be spoofed.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q100. Why limit upload size?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> To reduce memory/disk abuse and denial-of-service risk.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q101. Why is cleanup security-relevant?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Sensitive temporary files may remain if cleanup fails.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q102. Can a valid PDF still be malicious?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes, including prompt injection or malformed content.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Prompt Injection vs Authorization

## Q103. What is prompt injection?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Untrusted content attempts to manipulate model behavior.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q104. Can a logged-in user still send prompt injection?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q105. Can PDFs contain prompt injection?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q106. Can web results contain prompt injection?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q107. Does authentication make the content trusted?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q108. Can prompt injection grant access to another user's data?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> It must not; deterministic authorization should prevent that.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Credit and Account Security

## Q109. Why are credits security-sensitive?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> They affect account entitlement and provider-cost control.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q110. What Agent credit weakness exists?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Provider work can continue when the credit helper fails in some paths.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q111. Why is that important?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The application can incur provider usage without enforcing the intended account rule.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q112. What payment issue is relevant?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Replay/idempotency and non-atomic credit granting risks.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Threat Scenarios

## Q113. A user sends another user's ID in the body. What should happen?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Ignore it for identity and use the session-resolved user.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q114. A user changes conversationId. What should happen?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Verify resource ownership and deny if it belongs to another user.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q115. A normal user calls an admin route. What should happen?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Deny authorization.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q116. A browser sends x-user-id=victim. What should happen?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Gateway should ignore/overwrite it with the authenticated session identity.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q117. Redis is unavailable. Should the API trust the client userId?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q118. Firebase verification fails. Should a session be created?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q119. Cookie exists but session expired. What happens?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authentication fails until a new valid session is created.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q120. Admin disables user but old session remains. What risk exists?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The stale session may continue operating until invalidated or refreshed.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q121. Logout clears UI but Redis session remains. What risk exists?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> The credential may still be valid server-side.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q122. Downstream service receives no trusted identity. What should it do?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Reject protected operations.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Security Testing

## Q123. What authentication tests would you write?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Valid/invalid Firebase token, missing token, session creation, missing cookie, expired session, invalid session and Redis outage.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q124. What authorization tests would you write?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Owner allow, different-user deny, unauthenticated deny, admin/non-admin cases.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q125. What is a cross-tenant test?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> User A tries User B's resource and must be denied.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q126. Why test every router mount?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> An alternate path can bypass correct middleware.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q127. How do you test x-user-id spoofing?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Send a forged header and verify the server still uses the session-resolved user.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q128. How do you test logout?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Reuse the old cookie after logout and verify the server session is invalid.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q129. How do you test stale sessions?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Change sensitive account state and verify old sessions are invalidated/refreshed according to policy.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q130. How do you test CSRF?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Attempt cross-site mutation requests without the required CSRF proof.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q131. How do you test prompt injection?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Use malicious PDF/web content and verify tool/data authorization cannot be overridden.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Troubleshooting

## Q132. Google sign-in works but backend login fails. What do you check?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Firebase token generation, backend verification configuration, Auth secrets and logs.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q133. Login succeeds but later request is 401. What do you check?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Cookie set/sent, Secure/SameSite/domain/path, Redis key, TTL and Gateway lookup.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q134. Works locally but not production. What do you check?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> HTTPS, cross-origin cookie behavior, credentialed CORS and Redis connectivity.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q135. All authenticated requests fail. What dependency do you check?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Redis session store.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q136. One user sees another user's conversation. What do you inspect?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Ownership query, identity propagation, alternate routes and client-controlled IDs.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q137. Admin route exposed. What do you inspect?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Every router mount and middleware order.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q138. Logout succeeds visually but old cookie still works. What do you inspect?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Server-side Redis revocation.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Production V2

## Q139. What is the first V2 priority?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Centralized deterministic authorization and ownership checks.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q140. How should account mutation be protected?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Use server-resolved authenticated identity and explicit permissions.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q141. How should client identity headers be handled?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Ignore/reject them and set trusted identity at the Gateway.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q142. How should admin authorization improve?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Use one consistent protected route/role policy.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q143. How should logout improve?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Revoke Redis session server-side and clear the cookie.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q144. How should sensitive account changes affect sessions?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Invalidate or refresh affected sessions.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q145. What should happen with CSRF?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Adopt an explicit documented strategy.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q146. What should happen with internal calls?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Authenticate service-to-service requests.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q147. What should happen with exposed credentials?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Rotate them and use managed runtime secrets.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q148. What should happen with regression tests?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Automate cross-tenant and authorization tests across all sensitive routes.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q149. What should be monitored?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> 401/403 rates, failed session lookups, ownership denials, admin activity and abnormal account mutations.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Design Defense

## Q150. Why Firebase plus Redis session?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Firebase verifies identity, while Redis gives the application server-side session control.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q151. Why not call the Firebase token the app session?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Because NovaMind creates a separate opaque server-side session after verification.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q152. Why use HTTP-only cookies?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> To reduce direct JavaScript access to the session credential.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q153. Why not trust client x-user-id?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Clients can forge headers.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q154. Why isn't private networking enough?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Reachability is not caller identity or authorization.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q155. Why isn't CORS enough?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> CORS is a browser policy, not server-side authorization.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q156. Why fix ownership before adding advanced AI security?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Deterministic access-control bugs can directly expose or mutate real user data.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q157. Is the current security model production-ready?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No. Authentication is real, but authorization, revocation, CSRF, service identity and secret-management gaps remain.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Pressure Questions

## Q158. If Firebase already verifies the user, why do you need Redis?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Firebase proves identity at login; Redis stores the ongoing application session used by Gateway later.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q159. If the cookie is HTTP-only, are you safe from XSS?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q160. If CORS allows only your frontend, can attackers still call the API?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Yes, direct clients are not constrained by browser CORS.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q161. If services are private, why authenticate internal calls?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Private network location does not prove service identity.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q162. Why is email-based admin authorization weak?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> It is simple and brittle and does not provide a complete role/permission system.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q163. If a user knows another conversation ID, what stops access?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Only a correct ownership check.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q164. Is Redis session safer than JWT?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Neither is universally safer; Redis gives central revocation but adds a stateful dependency.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q165. What is the most serious current security theme?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> Deterministic authorization/trust-boundary problems such as account mutation and incomplete ownership checks.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q166. Would you claim zero trust?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q167. Would you claim complete tenant isolation?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q168. Would you claim secrets are fully hardened?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> No.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

## Q169. What is the strongest accurate statement?

**What the interviewer is testing:** Whether you understand the trust boundary and can separate authentication, sessions, authorization, ownership and security controls.

**Word-for-word answer:**

> NovaMind has a real Firebase-plus-Redis authentication foundation, but authorization boundaries still need significant hardening.

**Likely follow-up:** Expect a question about **failure behavior, spoofing, ownership, session lifecycle, CSRF/XSS, internal service trust, or how you would improve the current design**.

**Project-defense reminder:** Keep current implementation and Production V2 recommendations separate.

---

# Rapid-Fire Revision

**Q170. Authentication?**  
Who are you?

**Q171. Authorization?**  
What are you allowed to do?

**Q172. Ownership?**  
Can this user access this resource?

**Q173. Tenant isolation?**  
User A must not access User B data.

**Q174. Login provider?**  
Google through Firebase.

**Q175. Login proof?**  
Firebase ID token.

**Q176. App session?**  
Opaque UUID server-side session.

**Q177. Session store?**  
Redis.

**Q178. JWT app session?**  
No.

**Q179. Session TTL?**  
About 7 days.

**Q180. Cookie?**  
HTTP-only.

**Q181. Production cookie flags?**  
Secure + SameSite=None.

**Q182. Later auth boundary?**  
Gateway + Redis lookup.

**Q183. Trusted identity?**  
Server-resolved user ID.

**Q184. Trust browser x-user-id?**  
No.

**Q185. 401?**  
Missing/invalid auth.

**Q186. 403?**  
Authenticated but forbidden.

**Q187. CORS = auth?**  
No.

**Q188. Cloud Map = auth?**  
No.

**Q189. Private subnet = service identity?**  
No.

**Q190. mTLS verified?**  
No.

**Q191. RBAC mature?**  
No.

**Q192. Ownership complete?**  
No.

**Q193. CSRF mature?**  
No.

**Q194. Revocation mature?**  
No.

**Q195. Admin fully hardened?**  
No.

**Q196. MIME checks?**  
Yes, partial.

**Q197. Upload limit?**  
About 20 MiB.

**Q198. Prompt injection possible?**  
Yes.

**Q199. Secrets Manager refs?**  
Yes.

**Q200. Tracked MongoDB credentials found?**  
Yes.

**Q201. Production-ready?**  
No.

# Cross-Question Chain 1 — Login

**Interviewer:** Walk me through login.

> The user signs in with Google through Firebase. The frontend gets a Firebase ID token and sends it to the backend. Auth verifies it, finds or creates the user in MongoDB, creates a fresh opaque UUID application session in Redis with about a seven-day TTL, and returns the session credential in an HTTP-only cookie.

**Interviewer:** So you use JWT sessions?

> No. Firebase provides an ID token during login, but the ongoing NovaMind application session is an opaque Redis-backed server-side session.

---

# Cross-Question Chain 2 — Authorization

**Interviewer:** If the user has a valid session, can they read any conversation ID?

> No. Authentication only proves identity. The backend still has to verify resource ownership.

**Interviewer:** Is that fully enforced today?

> Not yet. The verified review found incomplete ownership checks on some conversation/message operations.

---

# Cross-Question Chain 3 — x-user-id

**Interviewer:** Can't I just send another user's x-user-id?

> A client-supplied identity header must not be trusted. The Gateway should resolve identity from the Redis session and overwrite the internal header with that trusted value.

---

# Cross-Question Chain 4 — Cookie Security

**Interviewer:** Why HTTP-only?

> It reduces direct JavaScript access to the session credential.

**Interviewer:** Does that stop XSS?

> No.

**Interviewer:** SameSite=None — what about CSRF?

> That is why an explicit CSRF strategy is important. A mature CSRF control is not verified in the current project.

---

# Cross-Question Chain 5 — Logout

**Interviewer:** What should logout do?

> Revoke/delete the Redis session server-side and clear the browser cookie.

**Interviewer:** Is that fully mature today?

> No. Session revocation is partial.

---

# Cross-Question Chain 6 — Admin

**Interviewer:** How do you authorize admins?

> The current project includes an email-based admin check, but that is not mature RBAC, and the review found an alternate/public path to admin handlers.

---

# Cross-Question Chain 7 — Secrets

**Interviewer:** Are secrets fully managed?

> The deployment uses Secrets Manager references, but the review also found MongoDB credentials tracked in source/task-definition context, so I would not claim the posture is fully hardened.

---

# Cross-Question Chain 8 — Account Mutation

**Interviewer:** What is one of the highest-risk API problems?

> Public `/api/auth` routing exposes sensitive account/credit mutation routes and can rely on request-provided identity. That should be replaced with server-resolved authenticated identity plus explicit authorization.

---

# 30-Second Interview Answer

> NovaMind uses Google sign-in through Firebase for initial identity verification, then creates its own opaque UUID server-side session in Redis. The session is returned in an HTTP-only cookie with Secure and SameSite=None in production. On later requests, the Express Gateway looks up the Redis session, resolves the trusted user identity and forwards it to downstream services. The main limitation is that authentication is stronger than authorization today: account-mutation, admin-route, resource-ownership and session-revocation gaps still need hardening.

---

# 60–90 Second Interview Answer

> NovaMind separates identity verification from application session management. The user signs in with Google through Firebase and the frontend sends the Firebase ID token to the backend. Auth verifies it, finds or creates the MongoDB user and creates an opaque UUID application session in Redis with roughly a seven-day TTL. The browser receives that session credential in an HTTP-only cookie, with Secure and SameSite=None in production.
>
> On later protected requests, the Express Gateway resolves the session in Redis and obtains the trusted user identity. Client-provided identity such as userId or x-user-id must not be trusted.
>
> Authentication is real, but authorization is only partially hardened. The verified review found public account/credit mutation routes, an alternate admin path, incomplete resource-ownership checks, partial session revocation, no mature explicit CSRF strategy and no verified strong service-to-service identity. Those are the areas I would fix before calling the platform production-ready.

---

# 2–3 Minute Project Defense

> NovaMind's authentication flow begins with Google sign-in through Firebase. The browser receives a Firebase ID token and sends it to the backend login endpoint. Auth verifies the token and resolves the application user in MongoDB. After that, NovaMind creates its own opaque UUID server-side session in Redis. That distinction is important: the Firebase token proves identity during login, while the Redis session maintains authenticated application state after login.
>
> The server returns the session credential in an HTTP-only cookie. In production the cookie is also Secure and uses SameSite=None. Later requests send the cookie to the Express Gateway. Gateway resolves the Redis session, obtains the trusted user identity and forwards that identity to downstream services. A browser-supplied user ID or x-user-id must not become the source of truth.
>
> Authentication is only the first layer. Every conversation, message, artifact, admin action or account mutation still needs authorization. This is where the current project has significant gaps. The review found incomplete conversation ownership checks, public account/credit mutation routes, an alternate path to admin handlers, incomplete session revocation and stale-session behavior. It also found no mature explicit CSRF strategy and no verified strong internal service identity. Cloud Map and private networking help discovery/reachability but do not authenticate callers.
>
> The project uses Secrets Manager references, but the review also found tracked MongoDB credentials, so I would rotate those credentials and remove hard-coded values before claiming strong secret hygiene.
>
> For Production V2, I would first centralize deterministic authorization: enforce resource ownership, protect account mutation, reject client-controlled identity and add cross-tenant regression tests. Then I would improve session revocation, invalidate sessions after sensitive account changes, add an explicit CSRF strategy, authenticate internal service calls, rotate exposed credentials and add security/audit observability.

---

# What Not to Say

Do not say:

- “NovaMind uses JWT application sessions.”
- “Firebase ID token is the same as the Redis session.”
- “HTTP-only means CSRF is impossible.”
- “CORS protects the API.”
- “Cloud Map authenticates services.”
- “Private subnet means internal traffic is trusted.”
- “RBAC is fully implemented.”
- “Tenant isolation is complete.”
- “Logout fully revokes every session.”
- “Admin changes always invalidate sessions.”
- “All secrets are fully hardened.”
- “We use mTLS.”
- “We use Cognito.”
- “AWS API Gateway handles authentication.”
- “The project is production-ready.”

---

# Final Self-Test

Before Module 12, explain without notes:

- authentication vs authorization
- identity vs session
- Firebase login
- Firebase ID token
- opaque UUID app session
- Redis session
- 7-day TTL
- HTTP-only / Secure / SameSite=None
- later session lookup
- trusted identity propagation
- x-user-id spoofing
- resource ownership
- tenant isolation
- 401 vs 403
- public account-mutation issue
- admin-route issue
- session revocation
- stale sessions
- CORS
- CSRF
- XSS
- internal service identity
- Cloud Map vs authentication
- Secrets Manager
- credential exposure
- IAM least privilege
- file security
- prompt injection vs authorization
- security testing
- Production V2 priorities

**Module 11 interview preparation complete.**
