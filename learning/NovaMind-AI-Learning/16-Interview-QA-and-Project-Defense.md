# Module 16 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** GitHub Actions, CI/CD, Deployment and Release Safety  
> **Purpose:** Prepare for CI/CD, GitHub Actions, Docker/ECR/ECS, frontend deployment, release-safety, troubleshooting, design-defense and pressure interviews.

---

## Accuracy Rules

### CURRENT VERIFIED

```text
push to main triggers deployment automation
repository checkout
AWS credentials are configured
ECR login
five backend Docker images are built/tagged/pushed
Gateway/Auth/Chat/Agent/Billing are force-redeployed
React frontend is built
frontend is synced to S3
CloudFront invalidation is created
current backend image tag strategy uses latest
```

### CURRENT LIMITATIONS

```text
no substantive automated backend test gate
no mature AI evaluation gate
no verified image-scanning gate
no immutable release identity
no explicit task-definition registration step
no mature wait-for-service-stability gate
no mature post-deployment smoke test
no mature automated rollback
no mature deployment concurrency control
all five backend services are redeployed together
```

### PRODUCTION V2 — PROPOSED

```text
PR validation
unit/integration/E2E tests
AI evals
security scanning
Git SHA/image digest identity
task-definition registration
stability wait
smoke testing
rollback/circuit breaker
service-specific deployment
environment promotion
GitHub OIDC
structured release observability
```

### Do not claim

```text
current GitHub OIDC
blue/green
canary
zero-downtime guarantee
mature automated rollback
mature CI test suite
mature AI evaluation pipeline
immutable production releases
current environment promotion
production readiness
```

---

# CI/CD Fundamentals

## Q1. What is Continuous Integration?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Continuous Integration is the practice of frequently integrating code and automatically validating changes with checks such as linting, tests and builds.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q2. What is Continuous Delivery?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Continuous Delivery keeps validated software deployable, usually with a deliberate promotion or approval before production.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q3. What is Continuous Deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Continuous Deployment automatically releases every change that passes the required pipeline gates.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q4. CI vs CD?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> CI validates/integrates code; CD delivers or deploys validated artifacts.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q5. Continuous Delivery vs Continuous Deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Delivery keeps releases ready for production; Deployment automatically pushes successful changes to production.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q6. Does using GitHub Actions automatically mean you have mature CI/CD?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No. GitHub Actions is an automation platform; maturity depends on tests, gates, release identity, verification and rollback.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q7. What is a pipeline?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> An ordered automation flow that validates, builds and/or deploys software.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# GitHub Actions Basics

## Q8. What is a GitHub Actions workflow?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The complete automation definition, usually written in YAML under `.github/workflows`.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q9. What is a trigger?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> An event that starts the workflow.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q10. What is NovaMind's deployment trigger?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A push to `main`.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q11. What is a job?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A group of steps executed on a runner.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q12. What is a step?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> One action or shell command inside a job.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q13. What is a runner?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The machine/environment executing a workflow job.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q14. What is checkout?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The step that makes repository source available on the runner.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q15. What does workflow YAML define?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Triggers, jobs, steps, permissions, environment and workflow configuration.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# NovaMind Current Deployment

## Q16. Walk me through the verified deployment workflow.

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A push to main triggers GitHub Actions, which checks out the repo, configures AWS credentials, logs into ECR, builds/tags/pushes the five backend images, forces redeployment of the five ECS services, then builds React, syncs the frontend to S3 and invalidates CloudFront.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q17. How many backend services does the workflow deploy?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Five: Gateway, Auth, Chat, Agent and Billing.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q18. Are the eight AI specialists deployed independently?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No. They remain inside the Agent service.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q19. What is the backend release path?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Source → Docker build → image → ECR → ECS service redeployment → Fargate replacement task.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q20. What is the frontend release path?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> React source → frontend build → S3 sync → CloudFront invalidation.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q21. Is backend deployment the same as frontend deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# AWS Authentication

## Q22. Why does GitHub Actions need AWS credentials?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> To call AWS APIs such as ECR, ECS, S3 and CloudFront.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q23. Is GitHub OIDC verified as current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q24. How should you describe OIDC?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> As a Production V2 recommendation for short-lived role credentials.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q25. Why is OIDC better than long-lived CI keys?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It avoids storing persistent AWS access keys and supports short-lived, scoped role sessions.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q26. Should the CI deployment identity be AdministratorAccess?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No, it should follow least privilege.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# ECR and Docker Build

## Q27. What happens after checkout?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The workflow configures AWS credentials and logs into ECR before building/pushing images.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q28. What does ECR do?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Stores container images.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q29. Does ECR deploy the application?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q30. How many images are built?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Five backend images.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q31. What are the service names?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Gateway, Auth, Chat, Agent and Billing.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q32. What is the deployable backend artifact?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The Docker image.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q33. What is the current image tag strategy?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Mutable `latest` tags.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Mutable Latest

## Q34. Why is `latest` weak?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The same tag can point to different image bytes over time.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q35. What release-safety problems does that create?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Weak traceability, reproducibility, rollback and auditing.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q36. What is a better tag?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> An immutable Git SHA or release version.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q37. What is an image digest?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A content-addressed identity for exact image bytes.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q38. Git SHA vs digest?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Git SHA identifies source; image digest identifies the built container artifact.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q39. Are immutable tags/digests current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No, proposed.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# ECS Redeployment

## Q40. What does force ECS redeployment do?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It tells the ECS service to replace tasks using the currently registered task definition.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q41. Can force redeploy pull a newer `latest` image?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Yes, replacement tasks may pull the newer image referenced by the same mutable tag.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q42. Does force redeploy register a new task-definition revision?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q43. What is the critical limitation?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Local task-definition JSON changes are not applied just because the service is force-redeployed.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Task Definition Revisioning

## Q44. If CPU changes in local JSON, what must happen?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Register a new ECS task-definition revision and update the service to use it.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q45. What configuration changes need a new task revision?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> CPU, memory, environment variables, secret references, roles and other task/container settings.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q46. Why doesn't a repository JSON edit change ECS automatically?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> ECS runs registered task-definition revisions, not arbitrary files in Git.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q47. What is the correct V2 flow?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Render/validate task definition, register new revision, update service, wait for stability and smoke test.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q48. Why is this a major interview topic?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It shows you understand the difference between deploying application image content and deploying ECS runtime configuration.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Frontend Deployment

## Q49. How does NovaMind deploy the frontend?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It builds React, syncs the static output to S3, then creates a CloudFront invalidation.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q50. Why S3?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It stores the static frontend build files.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q51. Why invalidate CloudFront?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> CloudFront may still cache old assets after new files are uploaded.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q52. Does CloudFront invalidation deploy the backend?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q53. Is CloudFront the backend API proxy here?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# CI Quality Gates

## Q54. Does the current workflow have a substantive backend unit-test gate?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q55. Does it have a mature integration-test gate?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q56. Does it have a mature E2E gate?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q57. Does it have a mature AI evaluation gate?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q58. What frontend validation capability exists in the repository?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Frontend lint/build capability exists, but a strong deployment-blocking quality gate is not verified.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q59. Why is automated deployment without strong tests risky?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Bad code can move quickly into the deployed environment.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# AI Evaluation

## Q60. Why does GenAI need evaluation beyond normal unit tests?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Model outputs can be syntactically successful but semantically wrong, ungrounded or poorly routed.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q61. What NovaMind AI evals would matter?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Router accuracy, RAG retrieval/answer quality, structured-output validity and regression cases.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q62. Is a mature AI eval suite current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Security Scanning

## Q63. What is dependency scanning?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Checking dependencies for known vulnerabilities.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q64. What is image scanning?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Checking container images/base packages for vulnerabilities.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q65. Is a verified image scanning gate current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q66. Where should scanning happen?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Before production deployment, according to a defined severity policy.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Wait for Stability

## Q67. What does waiting for ECS service stability mean?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Confirming the service reaches the expected stable task/deployment state.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q68. Is a mature wait-for-stability gate current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q69. Does ECS stability prove the app works?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q70. Why not?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Tasks can run while important dependencies or business paths are broken.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Smoke Testing

## Q71. What is a smoke test?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A small set of post-deployment checks for critical user/application behavior.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q72. Give NovaMind examples.

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Health endpoint, login/session, basic chat, or another critical API path.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q73. Is a mature automated smoke-test gate current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q74. Health check vs smoke test?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Health check tests service readiness/aliveness; smoke test verifies important functional behavior.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Rollback

## Q75. What is rollback?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Restoring a previously known-good release.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q76. Why do immutable images make rollback safer?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> You can identify exactly which artifact/version to restore.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q77. Is mature automated rollback current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q78. Is ECS deployment circuit breaker verified current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q79. What is roll-forward?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Deploy a new corrected release instead of reverting.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q80. Which is always better?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Neither; it depends on failure/data compatibility.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Concurrency

## Q81. What deployment-concurrency problem can occur?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Two pushes can start overlapping production deployments.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q82. What can that cause?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Race conditions, mixed versions and confusing release state.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q83. Is mature concurrency control verified?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q84. How would you improve it?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Use GitHub Actions concurrency groups to serialize or supersede production deployments.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Service Deployment Independence

## Q85. Does NovaMind redeploy only changed services?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No; current workflow rebuilds/redeploys all five backends together.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q86. Why is that a limitation?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It increases deployment time/risk and weakens independent microservice release behavior.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q87. What could Production V2 do?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Detect changed paths/services and deploy only affected units when safe.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Partial Deployment

## Q88. What if three ECS services update and the fourth fails?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The environment can contain mixed backend versions.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q89. Why is that risky?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Cross-service API expectations may no longer match.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q90. Is deployment atomic across five services?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q91. What should you do about it?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Design backward-compatible contracts, explicit release order and verification/rollback.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Frontend Backend Skew

## Q92. What if frontend deploy succeeds but backend fails?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The frontend can expect an API that is not available yet.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q93. How can you reduce that risk?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Backward-compatible APIs, release ordering, versioned contracts and post-deploy checks.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Deployment Verification

## Q94. What should you verify after backend deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Correct task revision/image, target health, task stability, logs, error rate and smoke tests.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q95. What should you verify after frontend deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> CloudFront/S3 content, UI load and compatibility with backend.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q96. Workflow green vs release healthy?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Not the same.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Observability

## Q97. What should you watch during deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Task events, CloudWatch logs, 5xx/error metrics, provider errors and latency.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q98. Is mature release observability current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q99. What release metadata should be logged?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Git SHA, image digest, build/deployment ID and version.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Environment Promotion

## Q100. What is environment promotion?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Moving the same validated artifact through dev, staging and production.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q101. Why build once and promote?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It prevents environment-specific rebuild differences.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q102. Is mature dev→staging→prod promotion verified?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q103. What could GitHub Environments provide?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Approvals, environment-specific secrets and protection rules as a future design.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# CI Secrets

## Q104. Should backend secrets be compiled into React?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q105. Why?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Browser JavaScript is visible to users.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q106. Should CI print AWS/provider secrets?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q107. What is the difference between build-time and runtime secrets?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Build-time values influence artifact creation; runtime secrets are delivered only when the backend runs.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Troubleshooting — AWS Auth

## Q108. AWS steps fail immediately. What do you check?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Credential configuration, account, region, permissions and role trust if OIDC is later used.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q109. Could GitHub Actions be healthy while AWS auth fails?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Troubleshooting — ECR

## Q110. ECR login fails. What do you check?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> AWS auth, ECR account/region/repository and permissions.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q111. Docker build succeeds but push fails. What do you check?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> ECR login, repository existence, tag, permissions, region/account.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Troubleshooting — Docker Build

## Q112. Docker build fails. What do you inspect?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The failing Docker step, build context, dependencies, file paths, base image and logs.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q113. Why can a local build succeed while CI build fails?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Different environment, ignored/local files, architecture, cache or undeclared dependencies.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Troubleshooting — ECS

## Q114. Force deployment starts but tasks stop. What is your path?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> ECS service events → stopped task reason → exit code → CloudWatch logs → task definition → env/secrets/network.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q115. New CPU configuration isn't used. Why?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The service is probably still using the old registered task-definition revision.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q116. New image is not visible. What do you check?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> ECR tag/digest, service deployment, task image reference and whether new tasks actually replaced old ones.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Troubleshooting — Frontend

## Q117. Frontend build succeeds but website still looks old. What do you check?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> S3 sync target, CloudFront invalidation, cache behavior and browser cache.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q118. S3 sync fails. What do you check?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Bucket path, AWS credentials, IAM and build directory.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q119. Invalidation fails after upload. What happens?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> New files may exist in S3 while CloudFront continues serving cached content until cache expiry/another invalidation.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Release Safety

## Q120. What does release safety mean?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Controls that reduce the chance and impact of deploying bad changes.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q121. Name the biggest current NovaMind release-safety gaps.

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Limited test/eval gates, mutable tags, no task-definition registration, no stability/smoke gate, no mature rollback and no concurrency control.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q122. What is the first principle?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Validate before deploy and verify after deploy.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Production V2 Pipeline

## Q123. What should happen on pull request?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Lint, unit/integration tests, AI evals and security checks.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q124. What should happen after merge?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Build immutable images once, scan them and push them to ECR.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q125. How should task definitions be handled?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Render/pin immutable image, register a new revision and deploy that revision.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q126. What happens after ECS update?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Wait for stability, then execute health/smoke checks.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q127. What happens on failure?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Stop promotion and rollback or roll forward safely.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q128. How should frontend be handled?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Build a versioned artifact, deploy to S3/CloudFront and verify compatibility.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# OIDC and CI Security

## Q129. What is GitHub OIDC?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A federation mechanism where GitHub can obtain short-lived AWS role credentials using an identity token.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q130. Is it current NovaMind behavior?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q131. Why recommend it?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It reduces dependence on long-lived AWS access keys.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q132. What should the AWS deployment role permit?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Only the ECR/ECS/S3/CloudFront operations necessary for deployment.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Supply Chain

## Q133. What does pinning GitHub Actions mean?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Use a trusted explicit action version/commit instead of an uncontrolled reference.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q134. What is an SBOM?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A Software Bill of Materials listing software components/dependencies.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q135. Is an SBOM current?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q136. Why keep immutable images in ECR?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Traceability and rollback.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Cost

## Q137. What CI/CD cost drivers exist?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Runner time, repeated Docker builds, ECR storage and deployment-related AWS operations.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q138. Why can rebuilding all five services be inefficient?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Unchanged services consume build/push/redeployment time and compute.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q139. Does keeping immutable images mean never deleting any?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No; ECR lifecycle policies can retain appropriate history.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Design Defense

## Q140. Why use GitHub Actions?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It integrates repository events with automated build/deployment steps.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q141. Why separate backend and frontend pipelines conceptually?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> They produce different artifacts and deploy to different AWS services.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q142. Why not use `latest` in production?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It makes release identity ambiguous.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q143. Why explicitly register task definitions?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> ECS runtime configuration exists in registered revisions, not repository JSON alone.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q144. Why smoke test after deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A successful AWS deployment operation does not prove business functionality.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q145. Why not call this mature CI/CD today?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The deployment automation is real, but validation, release identity, verification and rollback controls are incomplete.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Pressure Questions

## Q146. Your workflow is green. Is production healthy?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Not necessarily; I still need service stability, health signals and smoke tests.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q147. You changed task memory and pushed main. Why did nothing change?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> The workflow did not register/deploy a new ECS task-definition revision.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q148. Haven't you solved traceability because Git stores every commit?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Not fully; the running `latest` image still needs an immutable mapping to the commit/build.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q149. Why do you need tests if Docker builds successfully?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> A successful build only proves packaging succeeded, not that behavior is correct.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q150. Why do you need AI evals if unit tests pass?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> AI behavior quality/routing/grounding can regress without normal code failures.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q151. Why not deploy all services together forever?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> It is simpler initially, but it weakens service independence and increases blast radius.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q152. Why is CloudFront invalidation needed if S3 already has new files?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> Edge caches may still serve older content.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q153. Can you claim blue/green deployment?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q154. Can you claim canary?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q155. Can you claim OIDC?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> No, it is proposed.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

## Q156. What is your strongest accurate CI/CD statement?

**What the interviewer is testing:** Whether you can distinguish deployment automation from mature CI/CD and reason about release identity, validation, ECS task configuration, partial failure, rollback and deployment safety.

**Word-for-word answer:**

> NovaMind has a real GitHub Actions deployment pipeline for five backend containers and the React frontend, but it still needs stronger CI validation, immutable release identity, explicit task-definition revisioning, deployment verification and rollback safety.

**Likely follow-up:** Be ready to explain **what the next pipeline step is, what happens if it fails, whether retry is safe, how you know which release is running, and which controls are current versus proposed**.

**Project-defense reminder:** A green workflow is not automatically a healthy release.

---

# Rapid-Fire Revision

**Q157. CI?**  
Continuous Integration.

**Q158. CD?**  
Continuous Delivery or Continuous Deployment.

**Q159. Trigger?**  
Push to main.

**Q160. Platform?**  
GitHub Actions.

**Q161. Backend services?**  
Five.

**Q162. Specialists separately deployed?**  
No.

**Q163. Registry?**  
ECR.

**Q164. Runtime deploy?**  
ECS/Fargate.

**Q165. Frontend deploy?**  
S3 + CloudFront.

**Q166. Current image tag?**  
latest.

**Q167. latest immutable?**  
No.

**Q168. Task JSON edit automatically registered?**  
No.

**Q169. Force redeploy registers task definition?**  
No.

**Q170. Backend unit-test gate mature?**  
No.

**Q171. AI eval gate mature?**  
No.

**Q172. Image scanning gate?**  
Not verified.

**Q173. Wait-for-stability gate?**  
Not maturely verified.

**Q174. Smoke tests?**  
Not maturely verified.

**Q175. Automated rollback?**  
Not maturely verified.

**Q176. Concurrency control?**  
Not maturely verified.

**Q177. OIDC current?**  
No.

**Q178. Blue/green current?**  
No.

**Q179. Canary current?**  
No.

**Q180. All five redeployed together?**  
Yes.

# Cross-Question Chain 1 — Current Pipeline

**Interviewer:** Walk me through your deployment.

> A push to `main` triggers GitHub Actions. The workflow checks out the repository, configures AWS credentials, logs into Amazon ECR, builds, tags and pushes five backend Docker images, then forces redeployment of the Gateway, Auth, Chat, Agent and Billing ECS services. After the backend steps, it builds the React frontend, syncs the build files to S3 and invalidates CloudFront so users receive updated static content.

**Interviewer:** So the eight agents are eight deployments?

> No. The eight specialist workflows are inside the Agent service. There are five backend deployment units.

---

# Cross-Question Chain 2 — CI/CD Maturity

**Interviewer:** Is this full CI/CD?

> It is real deployment automation, but I would not call it mature CI/CD yet. The verified workflow is missing substantive backend test/evaluation gates, immutable releases, explicit task-definition registration, mature stability/smoke checks, rollback and deployment concurrency controls.

---

# Cross-Question Chain 3 — `latest`

**Interviewer:** Why is `latest` risky?

> The same tag can represent different image bytes over time, so release traceability and rollback are weaker. I would use a Git SHA tag and optionally pin the image digest.

---

# Cross-Question Chain 4 — Task Definition

**Interviewer:** You changed Agent memory in the task JSON and pushed to main. Why didn't production change?

> Because the workflow's force redeployment uses the currently registered ECS task-definition revision. Editing the JSON in Git does not register a new AWS revision. I need to register the updated task definition and update the service to that revision.

---

# Cross-Question Chain 5 — Green Workflow

**Interviewer:** GitHub Actions finished successfully. Is the release good?

> Not necessarily. The workflow may have completed the AWS commands, but I still need ECS stability, target/application health and functional smoke tests. A green automation run is not the same as a verified healthy release.

---

# Cross-Question Chain 6 — Frontend Cache

**Interviewer:** S3 contains the new frontend but users see the old UI. Why?

> CloudFront can still have old objects cached at edge locations, which is why the deployment creates an invalidation.

---

# Cross-Question Chain 7 — OIDC

**Interviewer:** Do you use GitHub OIDC for AWS authentication?

> Not in the verified current implementation. I would recommend it for Production V2 so GitHub can assume a least-privilege AWS role with short-lived credentials.

---

# Cross-Question Chain 8 — Partial Deployment

**Interviewer:** Gateway and Auth deploy, Agent fails. What now?

> The environment may be in a mixed-version state. I would inspect the failed ECS deployment, avoid continuing blindly, verify compatibility and either roll forward or restore known-good immutable service versions. A stronger pipeline would add release gates and automated rollback logic.

---

# Troubleshooting Drill 1 — New Backend Not Running

```text
GitHub Actions
  ↓
Did Docker build?
  ↓
Did ECR push correct image?
  ↓
Which image tag/digest exists?
  ↓
Did ECS force deployment run?
  ↓
Did new tasks start?
  ↓
Task stopped reason?
  ↓
CloudWatch logs
```

---

# Troubleshooting Drill 2 — CPU/Memory Change Missing

```text
Local task-definition JSON changed
  ↓
Was new ECS revision registered?
  ├── No → old configuration remains
  └── Yes
       ↓
Did service update to new revision?
```

---

# Troubleshooting Drill 3 — Website Still Old

```text
Frontend build
  ↓
S3 sync successful?
  ↓
Correct bucket/path?
  ↓
CloudFront invalidation successful?
  ↓
Browser cache / edge cache?
```

---

# Troubleshooting Drill 4 — Workflow Green, App Broken

```text
ECS service stable?
  ↓
ALB/route health?
  ↓
CloudWatch 5xx/errors?
  ↓
Redis/MongoDB?
  ↓
Providers?
  ↓
Smoke test?
```

---

# 30-Second Interview Answer

> NovaMind uses GitHub Actions to automate deployment from `main`. It builds and pushes Docker images for Gateway, Auth, Chat, Agent and Billing to ECR, forces the corresponding ECS services to redeploy, then builds the React frontend, syncs it to S3 and invalidates CloudFront. The main limitations are mutable `latest` tags, limited automated testing/evaluation, no explicit task-definition registration step, and no mature stability, smoke-test or rollback gates.

---

# 60–90 Second Interview Answer

> NovaMind has a GitHub Actions deployment workflow triggered by a push to `main`. The runner checks out the code, configures AWS credentials, logs into ECR, builds/tag/pushes five backend images and forces ECS redeployment for Gateway, Auth, Chat, Agent and Billing. The eight specialist workflows remain inside Agent; they are not separately deployed services. The frontend is built separately and deployed as static files to S3, followed by a CloudFront invalidation.
>
> The important limitation is that deployment automation is ahead of CI/release safety. The backend images currently use mutable `latest` tags, and the workflow does not have a mature backend test or AI-evaluation gate, image-scanning gate, explicit ECS task-definition registration, wait-for-stability, smoke tests, automated rollback or concurrency control.
>
> For Production V2 I would use immutable Git SHA/image digest identity, run tests/evals/security scans before deployment, register new task-definition revisions explicitly, wait for ECS stability, run post-deployment smoke tests, serialize production releases and use GitHub OIDC with a least-privilege AWS role.

---

# 2–3 Minute CI/CD / Release-Safety Defense

> NovaMind's repository contains a real GitHub Actions deployment workflow. A push to `main` triggers the workflow. It checks out the source, configures AWS credentials, logs into ECR, builds Docker images for the five backend services, tags and pushes them to ECR, and then forces ECS service redeployments for Gateway, Auth, Chat, Agent and Billing. The frontend follows a separate release path: React is built into static files, those files are synced to S3, and CloudFront is invalidated so cached frontend assets are refreshed.
>
> I distinguish this deployment automation from mature CI/CD. The current release process has several important gaps. First, backend images use mutable `latest` tags, which weakens traceability and rollback. Second, the pipeline does not have substantive automated backend tests, AI evaluation, or a verified image-scanning gate before deployment. Third, force redeployment is not the same as registering a task-definition revision. If I change CPU, memory, environment variables, secret references or IAM roles in a local JSON file, ECS will continue using its currently registered revision until the new revision is explicitly registered and assigned to the service.
>
> Post-deployment release safety is also limited. A mature wait-for-service-stability gate, functional smoke tests, automated rollback and deployment concurrency control are not verified. All five backend services are also rebuilt and redeployed together, so deployment independence is incomplete.
>
> My Production V2 pipeline would validate pull requests with linting, tests, integration tests, AI evals and security scanning. On merge, it would build each changed service once, tag it with the Git SHA, optionally capture its digest, scan it, push it to ECR, render and register a new task-definition revision, deploy it, wait for ECS stability and run smoke tests. Production deployments would be serialized, failures would stop promotion or trigger a known rollback strategy, and GitHub would use OIDC to assume a narrowly scoped AWS deployment role. I would also log release metadata such as Git SHA and image digest so every runtime task can be traced to the exact source and artifact.

---

# Current vs Production V2

| Area | Current NovaMind | Production V2 Proposal |
|---|---|---|
| Trigger | Push to `main` | PR validation + controlled promotion |
| CI validation | Limited | Lint + unit + integration + E2E |
| AI eval | Not mature | Router/RAG/structured-output eval |
| Image tag | `latest` | Git SHA / digest |
| ECR | Implemented | Keep + scanning/lifecycle |
| ECS deploy | Force redeploy | New task revision + stability gate |
| Task-def registration | Missing from current workflow | Explicit registration |
| Backend scope | All five | Changed services where safe |
| Frontend | Build → S3 → invalidation | Versioned artifact + verification |
| Smoke test | Not mature | Automated post-deploy test |
| Rollback | Not mature | Known-good immutable rollback |
| Concurrency | Not mature | Serialize production |
| AWS auth | Credentials configured | OIDC + least privilege |
| Environments | Not maturely verified | dev → staging → prod |
| Observability | Basic logs | Release metadata + metrics/alarms |

---

# What Not to Say

Do not say:

- “GitHub Actions means our CI/CD is production-grade.”
- “All eight AI agents deploy independently.”
- “`latest` is immutable.”
- “Force ECS redeploy registers a new task definition.”
- “Editing task JSON in Git automatically changes ECS.”
- “We have comprehensive backend automated tests.”
- “We have AI evaluation gates.”
- “We have image scanning gates.”
- “We wait for ECS stability and smoke test every release.”
- “Rollback is fully automated.”
- “We use blue/green deployment.”
- “We use canary deployment.”
- “We currently use GitHub OIDC.”
- “CloudFront deploys our backend.”
- “A green workflow guarantees a healthy production release.”
- “The CI/CD process is production-ready.”

---

# Final Self-Test

Before Module 17, explain without notes:

- CI
- Continuous Delivery
- Continuous Deployment
- workflow
- trigger
- job
- step
- runner
- checkout
- AWS credentials
- ECR login
- Docker build/tag/push
- five backend services
- latest tag problem
- Git SHA
- image digest
- force ECS redeployment
- task definition revision
- local JSON vs registered revision
- frontend build
- S3 sync
- CloudFront invalidation
- backend vs frontend deploy
- lint/test gates
- integration/E2E
- AI eval
- image scanning
- stability wait
- health vs smoke test
- rollback
- concurrency
- partial deployment
- version skew
- environment promotion
- OIDC
- least-privilege CI role
- release metadata
- Production V2 pipeline

**Module 16 interview preparation complete.**
