# Module 14 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** Docker, ECR, ECS Fargate and AWS Architecture  
> **Purpose:** Prepare for Docker/container, AWS ECS/Fargate, deployment, troubleshooting, scaling, cost and architecture-defense interviews.

---

## Accuracy Rules

### Confident current claims

```text
Five separately containerized Express services:
Gateway 8000
Auth 8001
Chat 8002
Agent 8003
Billing 8004

Eight specialist AI workflows are inside Agent.
Docker base image: node:22-alpine.
Dockerfiles are mostly single-stage.
Deployment uses five ECR image paths/repositories.
Image tags use mutable latest.
ECS task definitions exist for the five services.
Launch/runtime uses ECS + Fargate + awsvpc.
CloudWatch awslogs is configured.
Secrets Manager references exist.
Task allocations:
Gateway/Auth/Chat/Billing = 512 CPU / 1024 MiB
Agent = 1024 CPU / 2048 MiB
```

### Documented / intended but not live-proven

```text
ALB frontend/API entry
private ECS tasks
public/private subnet pattern
NAT outbound connectivity
Cloud Map service discovery
```

### Do not claim

```text
Kubernetes / EKS
active autoscaling
verified multi-AZ HA
zero downtime
blue/green
canary
Docker HEALTHCHECK
mature non-root hardening
immutable release identity
complete IaC
full Terraform/CDK/CloudFormation
production readiness
```

---

# Docker Fundamentals

## Q1. What is a container?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A container is an isolated process environment that packages the application, runtime and dependencies while sharing the host kernel.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q2. What is a Docker image?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> An immutable packaged template used to create containers.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q3. What is a Docker container?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A running instance of a Docker image.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q4. Image vs container?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Image is the packaged blueprint; container is the running process created from it.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q5. What is a Dockerfile?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A declarative build file that defines how the image is created.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q6. What is build context?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The set of files available to Docker during image build.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q7. Why does build context matter?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Large or poorly filtered contexts slow builds and can accidentally include sensitive files.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q8. What is an image layer?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A filesystem/build layer produced by image instructions.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q9. Why does layer order matter?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It affects cache reuse and build speed.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# NovaMind Dockerfiles

## Q10. What base image does NovaMind use?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> `node:22-alpine`.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q11. Are the Dockerfiles multi-stage?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No, they are essentially single-stage.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q12. Do they use a mature non-root runtime?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No verified mature non-root configuration.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q13. Do they define Docker HEALTHCHECK?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q14. What dependency command is used?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> `npm install`.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q15. What stronger deterministic install would you prefer?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> `npm ci` when using valid lockfiles.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q16. What .dockerignore concern exists?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Nested/ineffective ignore placement can allow unnecessary local files into the build context.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q17. Why is that a security concern?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Sensitive files or local dependencies could enter the build/image context.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q18. How do containers start?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Using each service's normal Node/npm start command.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# NovaMind Service Layout

## Q19. How many backend services are containerized?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Five.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q20. Name them with ports.

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Gateway 8000, Auth 8001, Chat 8002, Agent 8003 and Billing 8004.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q21. Are the eight AI specialists separate containers?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q22. Where do the eight specialists live?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Inside the Agent service.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q23. Why is this distinction important?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The deployment has five backend service boundaries, not thirteen or eight AI-service containers.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# ECR

## Q24. What is Amazon ECR?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> AWS's container image registry.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q25. What does ECR store?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Container images.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q26. Does ECR run containers?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q27. ECR vs ECS?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> ECR stores images; ECS orchestrates running containers.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q28. What happens before ECR push?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Build and tag the Docker image.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q29. What happens when ECS launches a task?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The execution environment pulls the configured image from ECR.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q30. How many backend image paths exist conceptually?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Five, corresponding to the five backend services.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# ECS Fundamentals

## Q31. What is ECS?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Amazon Elastic Container Service, AWS container orchestration.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q32. What is an ECS cluster?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A logical grouping for ECS workloads.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q33. What is a task definition?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The deployment blueprint describing image, ports, CPU/memory, env, secrets, logs and roles.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q34. What is a task?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A running instance of a task definition.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q35. What is an ECS service?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A controller that keeps a desired number of tasks running and manages deployments.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q36. Task definition vs task?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Blueprint versus running workload.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q37. Task vs service?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Task is one running workload; service manages desired running tasks.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q38. Does ECS equal Fargate?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Fargate

## Q39. What is Fargate?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Serverless compute for containers used by ECS in this project.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q40. ECS vs Fargate?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> ECS is orchestration; Fargate is compute.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q41. Why use Fargate?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It avoids managing EC2 container hosts and provides task-level CPU/memory/networking.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q42. What is the trade-off?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Baseline runtime cost and less host-level control.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q43. Does NovaMind use Kubernetes?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q44. Does NovaMind use EKS?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Task CPU Memory

## Q45. What are the Gateway resources?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> 512 CPU / 1024 MiB.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q46. Auth?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> 512 CPU / 1024 MiB.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q47. Chat?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> 512 CPU / 1024 MiB.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q48. Billing?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> 512 CPU / 1024 MiB.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q49. Agent?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> 1024 CPU / 2048 MiB.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q50. Do these numbers prove throughput?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q51. What do they represent?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Configured allocations.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q52. Why might Agent need more?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It performs heavier AI orchestration, file handling and external-provider workflows; that is engineering reasoning, not a verified historical decision.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# awsvpc and Networking

## Q53. What network mode is used?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> `awsvpc`.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q54. What does awsvpc mean?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Each task gets VPC networking through its own ENI.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q55. Why do security groups matter?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> They control allowed network traffic to/from task ENIs.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q56. Are exact live network rules verified?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q57. What is a public subnet?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A subnet with a route to an Internet Gateway.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q58. What is a private subnet?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A subnet without direct public-internet routing.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q59. What placement is documented/intended?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> ALB/public components in public subnets and ECS tasks in private subnets.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q60. Is that live-proven from repo analysis?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# ALB and Target Groups

## Q61. What is ALB?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Application Load Balancer for HTTP/HTTPS traffic distribution.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q62. What is NovaMind's documented API path?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> React API request → ALB → Gateway ECS service.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q63. Is ALB live health fully verified?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q64. ALB vs Express Gateway?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> ALB is AWS load balancing; Express Gateway is the NovaMind Node.js application entry service.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q65. What is a target group?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A collection of backend targets receiving ALB traffic.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q66. What can cause ALB 503?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No healthy targets or unavailable target group/service.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q67. What can cause 502?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Backend connection/response errors, wrong port or app failures.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Cloud Map

## Q68. What is Cloud Map?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> AWS service discovery.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q69. What namespace is documented?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> `novamind.local`.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q70. What problem does Cloud Map solve?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Finding internal service endpoints by service name.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q71. Does Cloud Map authenticate services?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q72. Cloud Map vs ALB?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Cloud Map is service discovery; ALB distributes application traffic.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# NAT and Outbound Access

## Q73. Why might private Agent tasks need NAT?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> To call public providers like Groq, Gemini, OpenRouter, Tavily and Stability AI.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q74. Does NAT make tasks public inbound?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q75. What happens if NAT/outbound path is broken?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> External provider calls can fail even if the containers themselves are healthy.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q76. Why is NAT a cost concern?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It can add baseline and data-processing charges.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Secrets Manager

## Q77. What is Secrets Manager used for?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Managed storage/delivery of sensitive runtime values.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q78. Are secret references present?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q79. Does that prove all secrets are handled perfectly?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q80. Why not?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The review also found tracked MongoDB credentials in source/task-definition context.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q81. How do ECS tasks receive startup secrets?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Configured secret references can be resolved at task startup.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Execution Role vs Task Role

## Q82. What is the ECS execution role?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The role used for ECS startup operations such as pulling images, logs and startup secrets.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q83. What is the task role?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The role used by application code inside the running container for AWS API calls.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q84. Execution role vs task role?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Startup/control-plane permissions versus application runtime permissions.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q85. Does a role name prove least privilege?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q86. Was least privilege fully live-inspected?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# CloudWatch

## Q87. What logging driver is configured?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> CloudWatch `awslogs`.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q88. What does it capture?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Container stdout/stderr.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q89. Why is CloudWatch the first place to inspect app failures?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It captures the running service's application logs.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q90. Does CloudWatch logs mean mature observability?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q91. What is missing from mature observability?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Tracing, correlation IDs, alarms, metrics and SLOs.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Runtime Architecture

## Q92. How is the frontend delivered?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> CloudFront serves the frontend from S3.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q93. How do backend requests enter the documented architecture?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> React request → ALB → Gateway ECS/Fargate.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q94. What happens after Gateway?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It routes to Auth, Chat, Agent or Billing depending on the request.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q95. What external systems does Agent call?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Groq, Gemini, OpenRouter, Tavily, Stability AI, Qdrant and S3.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q96. Is CloudFront the API proxy?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q97. Is Express Gateway AWS API Gateway?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Deployment Flow

## Q98. What is the deployment relationship?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Source → Docker build → image → ECR → task definition → ECS service → Fargate task → running container.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q99. How many backend images are built?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Five.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q100. What tag is currently used?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> `latest`.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q101. What is force new deployment?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Tell ECS service to replace tasks using the current task definition.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q102. What happens to frontend deployment?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Frontend is built, synced to S3 and CloudFront is invalidated.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q103. Does force redeploy register a new task definition?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Task Definition Revisioning

## Q104. If I only push a new `latest` image, can force redeploy pick it up?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Yes, replacement tasks may pull the updated image behind the same tag.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q105. If I change CPU in local task JSON, will force redeploy apply it?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q106. Why not?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The service still references the existing registered task-definition revision.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q107. What must you do?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Register a new task-definition revision and update the service to use it.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q108. Which changes require a new task definition revision?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> CPU, memory, environment, secret refs, IAM roles, container settings and similar task config.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q109. Why is this a critical interview concept?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It distinguishes image deployment from infrastructure/task configuration deployment.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Mutable latest

## Q110. Why is `latest` weak?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It is mutable, so the tag name does not uniquely identify release bytes.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q111. What problem does that create?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Poor traceability and rollback reproducibility.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q112. What is a better tag?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Git SHA or immutable release version.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q113. What is an image digest?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A content-addressed SHA256 identity for an exact image.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q114. Are immutable SHA/digest releases current?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No, proposed.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Container Security

## Q115. What are current hardening gaps?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Single-stage builds, no mature non-root user, no HEALTHCHECK and potential build-context issues.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q116. Why run as non-root?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Reduce privileges if compromised.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q117. Why scan images?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Detect vulnerable dependencies/base layers.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q118. Is image scanning a verified deployment gate?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q119. Why is .dockerignore security-relevant?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It can keep secrets/local files out of the image build context.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Health and Shutdown

## Q120. Does NovaMind define Docker HEALTHCHECK?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q121. Why is process running not enough?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The app can be alive but unable to serve requests or reach dependencies.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q122. What is readiness?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Whether the app is ready to receive traffic.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q123. What is liveness?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Whether the process should be considered alive/restartable.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q124. Is mature graceful shutdown verified?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q125. What should SIGTERM handling do?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Stop new work, finish/abort in-flight work safely, close resources and exit.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Rolling Deployment

## Q126. What is rolling deployment?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Gradually replacing old tasks with new ones.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q127. Can you claim zero downtime today?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q128. Can you claim blue/green?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q129. Can you claim canary?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q130. Why are health gates important during rolling deployment?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> To avoid routing traffic to broken new tasks.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Troubleshooting ECS

## Q131. What is your first ECS debugging path?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Service events → deployment → task → stopped reason → exit code → CloudWatch logs → task definition → env/secrets → networking/dependencies.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q132. Why check service events?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> They often show scheduling, target health, pull or deployment errors.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q133. Why check stopped reason?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It tells why ECS/Fargate terminated the task.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q134. Why check exit code?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It distinguishes application/process failure from some infrastructure issues.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q135. Why check task definition revision?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The service may be running old config.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# ECR Failures

## Q136. What can cause ECR push failure?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Wrong AWS auth, account/region/repository or missing permissions.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q137. What can cause ECS image pull failure?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Bad image URI/tag, missing image, execution-role permissions or network access.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q138. Should you debug app code before image-pull failure?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No, the application has not started yet.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Port and ALB Failures

## Q139. Container starts but ALB returns 503. What do you check?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Target health, target group, container port, service task status and app readiness.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q140. What if Node app listens on wrong port?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Traffic cannot reach the expected endpoint.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q141. What if target group expects a different port?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Health checks and requests fail.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q142. Why check interface binding?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Binding only to an inaccessible local interface can prevent external container traffic.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# DNS and Cloud Map Failures

## Q143. What do you check if `novamind.local` does not resolve?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Namespace/service registration, VPC DNS/resolver and service naming.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q144. Does a DNS resolution success prove service authorization?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Provider Connectivity

## Q145. Agent works locally but not in private ECS. What do you check?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> NAT/route table, DNS, security-group egress and provider endpoints.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q146. Why can all internal services be healthy while AI calls fail?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Outbound internet/provider connectivity can be broken independently.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Secrets and Environment

## Q147. What if a task starts with wrong env variable?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The app may connect to wrong endpoints or fail startup/runtime behavior.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q148. What if Secrets Manager returns AccessDenied?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Check execution role, secret ARN, region and related policies.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q149. Why not print secrets to logs for debugging?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> That leaks credentials.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# MongoDB Redis Failures

## Q150. What if Redis connection fails?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Sessions, fast memory and rate-limit behavior can fail.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q151. What if MongoDB connection fails?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Durable users/conversations/messages/payments fail.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q152. What do you check?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Endpoint, env/secret values, DNS, security groups/allowlist and TLS/configuration.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# CPU Memory Problems

## Q153. Why might Agent need more memory?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> File buffers, orchestration and provider payloads can use more resources.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q154. What happens if task exceeds memory?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It can be terminated.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q155. Do configured allocations prove they are sufficient?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q156. How should you tune?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Measure actual CPU/memory/latency under realistic load.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q157. New memory value doesn't appear after deploy. What do you check?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Whether a new task-definition revision was registered and the service uses it.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Scaling

## Q158. What is horizontal scaling?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Running multiple tasks for a service.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q159. What does desired count control?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> How many service tasks ECS attempts to keep running.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q160. Why can NovaMind scale services horizontally in principle?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Important shared state is externalized to services such as Redis/MongoDB/Qdrant/S3.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q161. Does more Agent tasks fix provider quotas?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q162. Does scaling fix Redis race conditions?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q163. Does scaling fix inefficient DB queries?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q164. Can scaling worsen concurrency bugs?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# High Availability

## Q165. Can you claim NovaMind is highly available?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No, live HA is not verified.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q166. Why not?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Task counts, multi-AZ behavior and dependency redundancy are not fully verified.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q167. What Redis HA limitation was observed?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> A captured Redis setup showed non-redundant/failover-disabled state.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q168. Does one ECS service with one task provide HA?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q169. What would HA require?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Redundant tasks/AZs plus resilient data stores/networking and health-based traffic routing.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Cost

## Q170. What are major container-platform cost drivers?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Fargate CPU/memory runtime, ALB, NAT, CloudWatch logs, ECR storage and data transfer.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q171. Why can five microservices cost money even at low traffic?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Always-on Fargate tasks create baseline runtime cost.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q172. Why is NAT noteworthy?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It has hourly/data processing cost.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q173. Can external AI providers exceed AWS container cost?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Yes, depending on workload.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q174. What should Production V2 add?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Cost monitoring and measurement by service/workflow.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Production V2

## Q175. What Docker improvements do you recommend?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Multi-stage builds, npm ci, effective .dockerignore, non-root runtime and image scanning.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q176. What release improvements?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Immutable Git SHA tags or digest pinning and explicit task-definition revision registration.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q177. What health improvements?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Readiness/health endpoints and deployment stability gates.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q178. What shutdown improvement?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Graceful SIGTERM handling.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q179. What deployment improvements?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Wait for stability, smoke tests and rollback/circuit-breaker strategy.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q180. What scaling improvement?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Measured autoscaling based on real demand.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q181. What observability improvement?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Structured logs, correlation IDs, metrics and alarms.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q182. What infrastructure improvement?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Least-privilege IAM and broader Infrastructure as Code.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q183. What HA improvement?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Multi-AZ/redundant components only where justified by availability requirements.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Design Defense

## Q184. Why Docker?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It packages each service with a consistent Node runtime and dependencies.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q185. Why ECR?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Native AWS registry integrated with ECS.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q186. Why ECS Fargate instead of Kubernetes?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Fargate reduces infrastructure-management overhead; Kubernetes offers more flexibility but adds operational complexity.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q187. Why five services rather than one container?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The repository already separates Gateway/Auth/Chat/Agent/Billing responsibilities, though it increases distributed-system complexity.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q188. Why not split eight specialists into eight services?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> They are bounded workflows inside Agent; separate services would add complexity without a verified requirement.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q189. Why is Agent larger?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> It has heavier orchestration/file/provider work, though the exact historical reason is not verified.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q190. Why not make all services public?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> The documented architecture intends controlled public entry and internal/private backend communication.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q191. Why use Cloud Map?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Service discovery between internal services.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q192. Why use Fargate?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Run containers without managing EC2 hosts.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Pressure Questions

## Q193. If you changed CPU locally and forced redeploy, why didn't it change?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Because ECS still used the previously registered task-definition revision; local JSON edits do not update ECS.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q194. If you push `latest`, how do you know which release is running?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> That is exactly the weakness of mutable tags; immutable SHA/digest releases improve traceability.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q195. Why not say Docker HEALTHCHECK is configured?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Because the verified Dockerfiles do not include a mature one.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q196. If ECS replaces crashed tasks automatically, are you highly available?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Not necessarily; repeated crash loops and dependency failures can still take the service down.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q197. If Agent scales from 1 to 10 tasks, will Groq latency disappear?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No. Provider quotas/latency are external bottlenecks.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q198. If all services are in private subnets, can they call Tavily?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> Only if outbound routing such as NAT is correctly configured.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q199. Is Cloud Map security?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No, discovery is not authentication.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q200. Can you say your deployment is zero downtime?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No, not without verified health/stability behavior and evidence.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q201. Can you say the whole infrastructure is IaC?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

## Q202. What is the strongest accurate deployment claim?

**What the interviewer is testing:** Whether you understand container packaging, AWS container orchestration, deployment identity, task configuration, networking, troubleshooting and production trade-offs.

**Word-for-word answer:**

> NovaMind has real containerized deployment configuration for five services using Docker, ECR, ECS task definitions and Fargate, with CloudWatch logging and Secrets Manager references, but release immutability, health gates, HA and full IaC still need hardening.

**Likely follow-up:** Be ready to explain **where the image lives, which task-definition revision is running, what Fargate actually does, what happens when the task fails, and whether the claim is current, documented or proposed**.

**Defense reminder:** Do not turn documented/intended AWS networking or Production V2 ideas into live-verified current facts.

---

# Rapid-Fire Revision

**Q203. Backend services?**  
Gateway, Auth, Chat, Agent, Billing.

**Q204. Ports?**  
8000, 8001, 8002, 8003, 8004.

**Q205. AI specialists separate ECS services?**  
No.

**Q206. Docker base?**  
node:22-alpine.

**Q207. Multi-stage current?**  
No.

**Q208. Non-root mature?**  
No.

**Q209. Docker HEALTHCHECK?**  
No.

**Q210. Install command?**  
npm install.

**Q211. Registry?**  
ECR.

**Q212. Orchestrator?**  
ECS.

**Q213. Compute?**  
Fargate.

**Q214. Network mode?**  
awsvpc.

**Q215. ECR = ECS?**  
No.

**Q216. ECS = Fargate?**  
No.

**Q217. Task definition?**  
Blueprint.

**Q218. Task?**  
Running workload.

**Q219. Service?**  
Maintains desired tasks.

**Q220. Gateway resources?**  
512 / 1024 MiB.

**Q221. Agent resources?**  
1024 / 2048 MiB.

**Q222. latest immutable?**  
No.

**Q223. Cloud Map namespace?**  
novamind.local.

**Q224. Cloud Map = auth?**  
No.

**Q225. CloudWatch logs?**  
awslogs.

**Q226. Kubernetes?**  
No.

**Q227. Autoscaling verified?**  
No.

**Q228. HA verified?**  
No.

**Q229. Zero downtime verified?**  
No.

**Q230. Full IaC?**  
No.

**Q231. New CPU via local JSON + force redeploy?**  
No.

**Q232. Need new task definition revision?**  
Yes.

# Cross-Question Chain 1 — Docker to AWS

**Interviewer:** How does your source become a running AWS service?

> Source code is packaged into a Docker image, the image is pushed to Amazon ECR, the ECS task definition references that image and runtime configuration, the ECS service deploys the task definition, and AWS Fargate provides the compute that runs the task/container.

**Interviewer:** So ECR runs the container?

> No. ECR stores the image; ECS/Fargate runs it.

---

# Cross-Question Chain 2 — Five Services vs Eight Specialists

**Interviewer:** How many backend containers do you run?

> The project defines five backend service containers: Gateway, Auth, Chat, Agent and Billing.

**Interviewer:** What about eight agents?

> The eight specialist AI workflows are inside the Agent service. They are not eight separate ECS services.

---

# Cross-Question Chain 3 — Task Definition

**Interviewer:** What is the difference between task definition, task and service?

> The task definition is the blueprint, a task is one running instance of that blueprint, and an ECS service maintains the desired number of tasks and manages replacement/deployment.

---

# Cross-Question Chain 4 — Image vs Task Configuration

**Interviewer:** You changed Agent memory in the JSON file and forced redeploy. Why didn't memory change?

> Because the service still used the old registered task-definition revision. Force redeploy replaces tasks using the current registered revision; local JSON changes require registering a new revision and updating the service.

---

# Cross-Question Chain 5 — `latest`

**Interviewer:** Why is `latest` a problem?

> It is mutable, so the same tag can represent different image bytes over time. That weakens traceability and rollback. I would use Git SHA tags or digests for immutable release identity.

---

# Cross-Question Chain 6 — Networking

**Interviewer:** Why does Agent need NAT?

> The documented architecture places backend tasks privately, while Agent calls public external providers such as Groq, Gemini, OpenRouter, Tavily and Stability. Private tasks need a valid outbound path, commonly NAT.

**Interviewer:** Does NAT make Agent public?

> No. It supports outbound access; it does not directly expose the task to inbound internet traffic.

---

# Cross-Question Chain 7 — ECS Failure

**Interviewer:** An Agent task keeps stopping. What do you do?

> I start with ECS service events and the stopped task reason, inspect the container exit code and CloudWatch logs, then verify task-definition revision, environment/secrets, memory, DNS/network/NAT and external dependencies.

---

# Cross-Question Chain 8 — HA

**Interviewer:** Is the application highly available?

> I would not claim that. Fargate/ECS can run multiple tasks, but the current live task counts, multi-AZ behavior and dependency redundancy are not fully verified, and the captured Redis setup was not redundant.

---

# 30-Second Interview Answer

> NovaMind has five containerized Node.js/Express backend services: Gateway, Auth, Chat, Agent and Billing. Docker packages each service, ECR stores the images, ECS orchestrates the workloads and Fargate runs the tasks. The eight AI specialists remain inside Agent. The project has ECS task definitions, CloudWatch logging and Secrets Manager references, but current releases still use mutable `latest` tags and do not have mature Docker health checks, immutable release identity or fully verified HA.

---

# 60–90 Second Interview Answer

> NovaMind's backend is split into five separately containerized Express services: Gateway on port 8000, Auth on 8001, Chat on 8002, Agent on 8003 and Billing on 8004. The Dockerfiles use Node 22 Alpine. The images are pushed to Amazon ECR, ECS task definitions describe image, ports, CPU/memory, secrets, logging and roles, ECS services maintain tasks, and AWS Fargate provides the compute.
>
> I distinguish the AWS services carefully: ECR stores images, ECS orchestrates them and Fargate runs the tasks. A task definition is the blueprint, a task is a running instance, and a service maintains desired tasks. Gateway, Auth, Chat and Billing are configured at 512 CPU and 1024 MiB, while Agent is 1024 CPU and 2048 MiB; those are allocations, not benchmarked capacity.
>
> The main current deployment limitations are single-stage Dockerfiles, no mature non-root runtime or Docker health check, mutable `latest` tags, and no immutable release identity. Also, changing local task-definition JSON does not change ECS until a new revision is registered and deployed.

---

# 2–3 Minute Architecture Defense

> NovaMind's backend is implemented as five Node.js/Express services: Gateway, Auth, Chat, Agent and Billing. Each service has its own container deployment configuration and port. The important clarification is that the eight AI specialists are workflows inside the Agent service; they are not eight separate ECS services.
>
> At build time, Docker packages each backend service using a Node 22 Alpine base image. The resulting images are pushed to Amazon ECR. ECR is only the registry; it does not run containers. ECS provides orchestration, and the project uses AWS Fargate as the compute platform. Each service has an ECS task definition describing its image, port, CPU/memory, environment/secrets, logging and IAM roles. An ECS service then keeps the configured number of tasks running.
>
> The task definitions use Fargate and `awsvpc`. Gateway, Auth, Chat and Billing are configured for 512 CPU and 1024 MiB, while Agent is configured for 1024 CPU and 2048 MiB. I treat those values as configured allocations, not tested throughput.
>
> The documented runtime architecture has CloudFront serving the React frontend from S3, and API traffic entering through an ALB into the Gateway service, with the other services available internally. Cloud Map with the `novamind.local` namespace is intended for service discovery. I do not claim the exact ALB/subnet/NAT/Cloud Map live state is currently verified from the repository.
>
> The deployment has several maturity gaps. It uses mutable `latest` tags, mostly single-stage Dockerfiles, no mature non-root runtime, no Docker health check and no verified image-scanning gate. A particularly important operational detail is the distinction between changing an image and changing a task definition. Pushing a new `latest` image and forcing a service deployment can replace containers with the new image, but changing CPU, memory, environment, secrets or IAM in a local task-definition JSON does nothing until a new ECS task-definition revision is registered and the service uses it.
>
> For Production V2 I would use multi-stage builds, `npm ci`, an effective `.dockerignore`, non-root containers, image scanning, Git SHA or digest-based image identity, explicit task-definition registration, readiness/health checks, graceful SIGTERM handling, deployment stability/smoke-test gates, structured metrics/alarms, measured autoscaling, least-privilege IAM and broader Infrastructure as Code.

---

# Current vs Production V2

| Area | Current NovaMind | Production V2 Proposal |
|---|---|---|
| Base image | `node:22-alpine` | Keep/evaluate pinned version |
| Build | Mostly single-stage | Multi-stage |
| Install | `npm install` | `npm ci` |
| Runtime user | Not maturely non-root | Non-root |
| Docker health | Not defined | Health/readiness endpoint/check |
| Image tag | `latest` | Git SHA / digest |
| Registry | ECR | ECR + scan/sign policy |
| Orchestration | ECS | Keep |
| Compute | Fargate | Keep/evaluate |
| Task config | Existing registered revisions | Explicit revision registration |
| Networking | Documented/intended ALB/private/NAT/Cloud Map | IaC + verified rules |
| Logs | CloudWatch awslogs | Structured logs + metrics + alarms |
| Deploy gate | Force redeploy | Stability + smoke tests + rollback |
| Scaling | Not verified mature autoscaling | Measured autoscaling |
| HA | Not verified | Multi-AZ/redundancy where justified |
| IaC | Not comprehensive | Broader Terraform/CDK/CloudFormation |

---

# What Not to Say

Do not say:

- “We run eight AI agents as eight ECS services.”
- “ECR runs my containers.”
- “ECS and Fargate are the same thing.”
- “Express Gateway is AWS API Gateway.”
- “Cloud Map authenticates services.”
- “The project uses Kubernetes/EKS.”
- “Autoscaling is fully configured.”
- “We have verified multi-AZ HA.”
- “Deployments are zero downtime.”
- “We use blue/green/canary.”
- “Docker HEALTHCHECK is configured.”
- “All containers run as non-root.”
- “Image tags are immutable.”
- “Changing local task JSON automatically changes ECS.”
- “The entire infrastructure is IaC.”
- “The deployment is production-ready.”

---

# Final Self-Test

Before Module 15, explain without notes:

- image vs container
- Dockerfile
- build context
- layers
- `.dockerignore`
- single-stage vs multi-stage
- npm install vs npm ci
- root vs non-root
- health check
- graceful shutdown
- `latest` vs SHA/digest
- ECR
- ECS
- Fargate
- ECS cluster
- task definition
- task
- service
- desired count
- CPU/memory allocations
- `awsvpc`
- security groups
- ALB
- target groups
- Cloud Map
- NAT
- execution role
- task role
- Secrets Manager
- CloudWatch
- deployment flow
- task-definition revisioning
- rolling deployment
- troubleshooting
- scaling
- HA limitations
- cost
- Production V2 improvements

**Module 14 interview preparation complete.**
