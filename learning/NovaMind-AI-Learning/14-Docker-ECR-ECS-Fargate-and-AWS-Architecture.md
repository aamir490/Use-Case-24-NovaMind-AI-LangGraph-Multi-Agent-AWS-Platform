# Module 14 — Docker, ECR, ECS Fargate and AWS Architecture

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Purpose:** Understand how NovaMind's five Node.js/Express backend services move from source code to Docker images, Amazon ECR, ECS task definitions, ECS services, AWS Fargate tasks, internal service communication, logging, secrets, networking, scaling, troubleshooting, cost, and Production V2 improvements.  
> **Accuracy rule:** This guide separates **PROJECT FACT**, **DOCUMENTED / INTENDED ARCHITECTURE**, **GENERAL CONCEPT**, and **PRODUCTION V2 RECOMMENDATION**. Do not present documented/intended networking or proposed improvements as live-proven current infrastructure.

---

## Module 14 Visual Architecture

![NovaMind AI — Docker, ECR, ECS Fargate and AWS Architecture](../images/14-docker-ecr-ecs-fargate-aws-architecture.png)

> Use the already-generated image at: `learning/images/14-docker-ecr-ecs-fargate-aws-architecture.png`

---

# 1. The Core Mental Model

The complete container lifecycle is:

```text
Source Code
   ↓
Docker Build
   ↓
Docker Image
   ↓
Amazon ECR
   ↓
ECS Task Definition
   ↓
ECS Service
   ↓
AWS Fargate Task
   ↓
Running Container
```

For NovaMind, the backend contains **five separately containerized Express services**:

```text
Gateway :8000
Auth    :8001
Chat    :8002
Agent   :8003
Billing :8004
```

Important:

```text
5 backend services
≠
8 AI specialists
```

The **eight specialist AI workflows live inside the Agent service**.

---

# 2. Container Fundamentals

## Concept 1 — What Is a Container?

**GENERAL CONCEPT**

A container is an isolated process environment that packages an application with its runtime and dependencies.

A container is lighter than a traditional VM because it shares the host operating-system kernel.

---

## Concept 2 — Why Containers Are Useful

Containers help make execution more consistent across:

- developer laptop
- CI/CD
- testing
- cloud runtime

The goal is:

```text
same image
→ same packaged application/runtime
```

---

## Concept 3 — Container vs Virtual Machine

A VM includes a full guest operating system.

A container normally packages:

- application
- runtime
- libraries
- dependencies

while sharing the host kernel.

---

# 3. Docker Image vs Container

## Concept 4 — Docker Image

A Docker image is an immutable packaged template.

Think:

```text
Image
= blueprint / packaged application
```

---

## Concept 5 — Docker Container

A container is a running instance of an image.

```text
Image
→ run
→ Container
```

---

## Concept 6 — NovaMind Mapping

For each backend service:

```text
Gateway source
→ Gateway Docker image
→ Gateway running container

Auth source
→ Auth Docker image
→ Auth running container
```

and so on for Chat, Agent and Billing.

---

# 4. Dockerfile

## Concept 7 — What Is a Dockerfile?

A Dockerfile is the set of instructions used to build a Docker image.

Typical instructions include:

```text
FROM
WORKDIR
COPY
RUN
EXPOSE
CMD
```

---

## Concept 8 — NovaMind Base Image

**PROJECT FACT**

NovaMind backend Dockerfiles use:

```text
node:22-alpine
```

---

## Concept 9 — Why Alpine Is Common

Alpine-based images are relatively small.

Benefits:

- smaller image
- faster transfer
- smaller storage footprint

Trade-offs:

- some native dependencies can be harder to compile/debug

---

# 5. Build Context

## Concept 10 — What Is Build Context?

The Docker build context is the set of files Docker can access during image build.

Example:

```bash
docker build .
```

The `.` is the build context.

---

## Concept 11 — Why Build Context Matters

Too-large build context can:

- slow builds
- accidentally include local files
- leak credentials into image layers
- increase image size

---

## Concept 12 — NovaMind Build Context Concern

**PROJECT FACT**

The verified review identified a `.dockerignore` / nested ignore concern.

A `.dockerignore` placed where Docker does not apply it to the selected build context may fail to exclude intended files.

---

# 6. `.dockerignore`

## Concept 13 — What `.dockerignore` Does

It prevents files from entering the Docker build context.

Common exclusions:

```text
node_modules
.git
.env
private keys
logs
temporary files
```

---

## Concept 14 — Why It Is a Security Control

If secrets enter build context:

```text
secret file
→ copied accidentally
→ image layer
→ registry
```

That is a serious leak.

---

## Concept 15 — Production V2

**PRODUCTION V2 RECOMMENDATION**

Use an effective root/build-context `.dockerignore` and verify it with build inspection.

---

# 7. Image Layers

## Concept 16 — What Is a Layer?

Docker builds images as layers.

Examples:

```text
base image layer
dependency layer
application-code layer
```

---

## Concept 17 — Why Layer Order Matters

If dependencies are copied/installed before rapidly changing source:

```text
package files
→ install
→ copy source
```

Docker can reuse cached dependency layers more effectively.

---

# 8. Dependency Installation

## Concept 18 — `npm install`

**PROJECT FACT**

Current Docker build logic uses `npm install`.

---

## Concept 19 — `npm ci`

**GENERAL CONCEPT**

For CI/container builds with a lockfile, `npm ci` is usually more deterministic.

It installs exactly from the lockfile and starts from a clean dependency tree.

---

## Concept 20 — Production V2

Use:

```text
npm ci
```

where lockfiles are valid and deterministic builds are desired.

---

# 9. Single-Stage vs Multi-Stage

## Concept 21 — Current Dockerfiles

**PROJECT FACT**

Current Dockerfiles are essentially single-stage builds.

---

## Concept 22 — Multi-Stage Build

A multi-stage Dockerfile can separate:

```text
build dependencies
from
runtime dependencies
```

---

## Concept 23 — Why Multi-Stage Helps

Potential benefits:

- smaller runtime image
- fewer build tools in production
- reduced attack surface

---

## Concept 24 — Is Multi-Stage Current?

No. It is a Production V2 recommendation.

---

# 10. Non-Root Runtime

## Concept 25 — Root in Container

Containers often run as root by default unless a `USER` is configured.

---

## Concept 26 — Why Non-Root Is Safer

If the application is compromised, a non-root process reduces privileges inside the container.

---

## Concept 27 — NovaMind Current Status

**PROJECT FACT**

A mature verified non-root runtime configuration is not present in the current backend Dockerfiles.

---

# 11. Ports and `EXPOSE`

## Concept 28 — Container Port

Each NovaMind service listens on its own application port:

```text
Gateway :8000
Auth    :8001
Chat    :8002
Agent   :8003
Billing :8004
```

---

## Concept 29 — `EXPOSE`

`EXPOSE` documents the intended container port.

It does not by itself publish the port to the internet.

---

## Concept 30 — Port Mapping in ECS

ECS task definitions/container definitions tell ECS which container port is used.

ALB/target groups and security groups determine actual network reachability.

---

# 12. CMD and Startup

## Concept 31 — Startup Command

**PROJECT FACT**

NovaMind containers start using the service's normal Node/npm start command.

---

## Concept 32 — Why Startup Command Matters

If the process exits, the container exits.

If the app never listens on the expected port, the task may be considered unhealthy/unreachable.

---

# 13. Container Filesystem

## Concept 33 — Ephemeral Runtime Files

Files written inside a running container are not a durable data store.

Task replacement can remove them.

---

## Concept 34 — NovaMind Impact

Temporary uploaded files may exist in container-local storage during request processing.

Do not treat them as persistent storage.

---

# 14. Docker Health Check

## Concept 35 — What Is a Health Check?

A health check asks whether the process/application is actually ready and functioning.

---

## Concept 36 — Current NovaMind Status

**PROJECT FACT**

The Dockerfiles do not define a mature Docker `HEALTHCHECK`.

---

## Concept 37 — Container Running ≠ Application Healthy

A Node process may be alive but:

- database unavailable
- Redis unavailable
- app not listening
- routes broken

A health endpoint can give better readiness/liveness signals.

---

# 15. Graceful Shutdown

## Concept 38 — SIGTERM

Container orchestrators typically send a termination signal before stopping a task.

Node.js should stop accepting new work and close resources gracefully.

---

## Concept 39 — Current Status

**PROJECT FACT**

A mature verified graceful shutdown strategy is not established.

---

## Concept 40 — Production V2

Handle SIGTERM:

```text
stop accepting traffic
→ finish/reject in-flight work
→ close Redis/MongoDB connections
→ exit
```

---

# 16. Immutable Images

## Concept 41 — Image Immutability

A release image should represent one exact build.

---

## Concept 42 — `latest`

**PROJECT FACT**

Current deployment uses mutable:

```text
latest
```

tags.

---

## Concept 43 — Why `latest` Is Weak

Two deployments can use the same tag name but different bytes.

This weakens:

- traceability
- rollback
- auditability
- reproducibility

---

## Concept 44 — Git SHA Tag

**PRODUCTION V2 RECOMMENDATION**

Example:

```text
gateway:4f82c8a
agent:4f82c8a
```

Now release identity points to a specific commit/build.

---

## Concept 45 — Digest Pinning

Image digest:

```text
sha256:...
```

identifies exact image content.

This is even more immutable than a mutable tag.

---

# 17. Amazon ECR

## Concept 46 — What Is ECR?

Amazon ECR is AWS's container image registry.

It stores Docker/OCI images.

---

## Concept 47 — ECR ≠ ECS

```text
ECR
= stores images

ECS
= runs/manages containers
```

---

## Concept 48 — Push Flow

```text
docker build
 ↓
tag image
 ↓
authenticate to ECR
 ↓
docker push
```

---

## Concept 49 — Pull Flow

When ECS/Fargate starts a task:

```text
task definition references image
 ↓
Fargate/ECS execution environment pulls from ECR
 ↓
container starts
```

---

# 18. ECS Fundamentals

## Concept 50 — What Is ECS?

Amazon ECS is AWS container orchestration.

It manages:

- task definitions
- tasks
- services
- deployments

---

## Concept 51 — ECS Cluster

An ECS cluster is a logical grouping for running ECS workloads.

---

## Concept 52 — ECS Is Not the Container Runtime

ECS orchestrates.

Fargate provides compute in this project.

---

# 19. Fargate

## Concept 53 — What Is Fargate?

AWS Fargate is serverless compute for containers.

AWS manages the underlying servers.

---

## Concept 54 — ECS vs Fargate

```text
ECS
= orchestration/control plane

Fargate
= compute where ECS tasks run
```

---

## Concept 55 — Why Fargate Is Convenient

Benefits:

- no EC2 host management
- task-level CPU/memory
- integrated ECS networking/logging/IAM

Trade-off:

- continuously running services have baseline cost
- less host-level control

---

# 20. Task Definition

## Concept 56 — What Is a Task Definition?

A task definition is the deployment blueprint for one or more containers.

It can define:

- image
- ports
- CPU/memory
- env variables
- secrets
- logging
- IAM roles
- networking compatibility

---

## Concept 57 — Task Definition ≠ Task

```text
Task Definition
= blueprint

Task
= running instance
```

---

## Concept 58 — Task Definition Revision

Every registered configuration change creates a new revision.

Example:

```text
novamind-agent:12
novamind-agent:13
```

---

# 21. ECS Task

## Concept 59 — What Is a Task?

A task is a running workload created from a task definition.

In NovaMind, a service task normally runs the corresponding backend container.

---

## Concept 60 — Task Stops

A task can stop because:

- process exits
- memory limit
- image pull failure
- config/secret problem
- application crash

---

# 22. ECS Service

## Concept 61 — What Is an ECS Service?

An ECS service keeps a desired number of tasks running.

---

## Concept 62 — Desired Count

Example:

```text
desiredCount = 2
```

means ECS attempts to maintain two tasks.

---

## Concept 63 — Service Recovery

If one task crashes:

```text
desired 2
actual 1
 ↓
ECS launches replacement
```

This helps availability, but only if dependencies/network/load balancing are also healthy.

---

# 23. NovaMind's Five Services

## Concept 64 — Five ECS Service Boundaries

**PROJECT FACT**

NovaMind deployment configuration maps to five backend services:

```text
Gateway
Auth
Chat
Agent
Billing
```

---

## Concept 65 — Eight Specialists Are Not ECS Services

**PROJECT FACT**

The eight specialist workflows are functions/workflows inside Agent.

Do not draw:

```text
8 ECS specialist services
```

That would be incorrect.

---

# 24. Task CPU and Memory

## Concept 66 — Verified Allocations

**PROJECT FACT**

```text
Gateway → 512 CPU / 1024 MiB
Auth    → 512 CPU / 1024 MiB
Chat    → 512 CPU / 1024 MiB
Billing → 512 CPU / 1024 MiB
Agent   → 1024 CPU / 2048 MiB
```

---

## Concept 67 — Allocation ≠ Benchmark

These values mean:

```text
configured resources
```

not:

```text
tested maximum throughput
```

---

## Concept 68 — Why Agent Has More Resources

**ENGINEERING REASONING**

Agent handles heavier orchestration, files and external-provider workflows.

It is reasonable for it to have more resources, but do not claim the original author's historical reason unless personally confirmed.

---

# 25. `awsvpc`

## Concept 69 — What Is `awsvpc`?

**PROJECT FACT**

The task definitions use:

```text
awsvpc
```

network mode.

---

## Concept 70 — What It Means

Each Fargate task receives its own elastic network interface and VPC networking identity.

---

## Concept 71 — Why Security Groups Matter

With `awsvpc`, tasks can have security-group-controlled traffic rules.

---

# 26. Security Groups

## Concept 72 — Security Group

A security group is a stateful network firewall attached to AWS resources such as ENIs/ALBs.

---

## Concept 73 — Desired Backend Pattern

**DOCUMENTED / INTENDED**

```text
ALB security group
→ allowed to Gateway

internal services
→ allowed only from required internal sources
```

Exact live rules are not verified.

---

# 27. ALB

## Concept 74 — What Is ALB?

Application Load Balancer distributes HTTP/HTTPS traffic to target groups.

---

## Concept 75 — NovaMind ALB Status

**DOCUMENTED / INTENDED**

Architecture documentation describes:

```text
React API
→ ALB
→ Gateway ECS
```

But current live ALB/network health is not verified from the repository alone.

---

## Concept 76 — ALB ≠ Express Gateway

```text
ALB
= AWS network/application load balancer

Express Gateway
= NovaMind Node.js application service
```

---

# 28. Target Groups

## Concept 77 — What Is a Target Group?

An ALB target group contains the backend targets that receive traffic.

For `awsvpc` Fargate tasks, IP target mode is commonly used.

---

## Concept 78 — Health Check Relationship

ALB can health-check targets.

A target may be removed from traffic if health checks fail.

Do not claim mature current health-gate behavior unless verified.

---

# 29. Cloud Map

## Concept 79 — What Is Cloud Map?

AWS Cloud Map provides service discovery.

---

## Concept 80 — NovaMind Namespace

**PROJECT FACT / DOCUMENTED**

Namespace:

```text
novamind.local
```

is intended for backend service discovery.

---

## Concept 81 — Cloud Map ≠ Authentication

Cloud Map helps answer:

> “Where is the service?”

It does not answer:

> “Is the caller authorized?”

---

# 30. Public and Private Subnets

## Concept 82 — Public Subnet

A public subnet has a route to an Internet Gateway.

---

## Concept 83 — Private Subnet

A private subnet does not directly route to an Internet Gateway.

---

## Concept 84 — NovaMind Placement

**DOCUMENTED / INTENDED**

The architecture describes:

- ALB/public-facing components in public networking
- ECS tasks in private subnets

Live placement is not fully verified.

---

# 31. NAT Gateway

## Concept 85 — Why Private Tasks Need NAT

Private ECS tasks may need outbound internet access to call:

- Groq
- Gemini
- OpenRouter
- Tavily
- Stability AI

A NAT Gateway is one common design.

---

## Concept 86 — NAT ≠ Inbound Public Access

NAT enables outbound connections from private networks.

It does not make the private task directly internet-reachable.

---

## Concept 87 — NAT Cost

NAT Gateway can create noticeable baseline and data-processing cost.

This matters for small workloads.

---

# 32. CloudFront + S3 Frontend

## Concept 88 — Frontend Hosting

**PROJECT FACT**

The deployment workflow uploads the React frontend build to S3 and invalidates CloudFront.

---

## Concept 89 — CloudFront Role

CloudFront delivers frontend/static content.

---

## Concept 90 — CloudFront Is Not API Proxy Here

**PROJECT FACT**

Do not describe CloudFront as NovaMind's backend API proxy.

---

# 33. Secrets Manager

## Concept 91 — What Is Secrets Manager?

AWS Secrets Manager stores sensitive values such as API/database credentials.

---

## Concept 92 — ECS Secret References

**PROJECT FACT**

ECS task configuration contains Secrets Manager references.

---

## Concept 93 — Startup Secret Injection

At task startup, ECS can retrieve configured secret values and inject them into the container environment.

---

## Concept 94 — Secret Reference ≠ Perfect Security

The repository also had a tracked MongoDB credential issue.

So do not say all secret handling is fully hardened.

---

# 34. Execution Role vs Task Role

## Concept 95 — Execution Role

General purpose:

```text
ECS startup operations
```

including:

- image pull
- logging setup
- startup secret retrieval

---

## Concept 96 — Task Role

General purpose:

```text
AWS permissions used by running application code
```

Example:

- S3 access from Agent

---

## Concept 97 — Critical Distinction

```text
Execution Role
≠
Task Role
```

---

## Concept 98 — Least Privilege Verification

**PROJECT FACT**

Effective IAM least privilege was not fully live-inspected.

Role existence/name is not proof.

---

# 35. CloudWatch Logs

## Concept 99 — `awslogs`

**PROJECT FACT**

The five services use CloudWatch `awslogs` configuration.

---

## Concept 100 — What It Gives

Container stdout/stderr can be sent to CloudWatch Logs.

This is the first place to inspect application failures in ECS.

---

## Concept 101 — Logs ≠ Full Observability

Current architecture does not have mature verified:

- tracing
- correlation
- alarms
- SLOs

CloudWatch logs are useful but not the complete observability stack.

---

# 36. Complete Runtime Flow

## Concept 102 — Frontend Path

```text
Browser
 ↓
CloudFront
 ↓
S3 frontend
```

---

## Concept 103 — Backend Path

**DOCUMENTED / INTENDED**

```text
React API request
 ↓
ALB
 ↓
Gateway ECS/Fargate
 ↓
Auth / Chat / Agent / Billing
```

---

## Concept 104 — Agent Dependencies

Agent calls external systems including:

- Groq
- Gemini
- OpenRouter
- Tavily
- Stability AI
- Qdrant
- S3

---

# 37. Docker → ECR → ECS Relationship

## Concept 105 — Build

Source is packaged into image.

---

## Concept 106 — Push

Image is pushed to ECR.

---

## Concept 107 — Task Definition References Image

ECS task definition contains image reference.

---

## Concept 108 — ECS Service Deploys It

The ECS service creates/replaces tasks using the task definition.

---

## Concept 109 — Fargate Runs It

Fargate supplies CPU/memory/network runtime.

---

# 38. Current Deployment Behavior

## Concept 110 — Five Images

**PROJECT FACT**

The deployment workflow builds/pushes five backend images.

---

## Concept 111 — Force New Deployment

**PROJECT FACT**

The workflow forces ECS service redeployment.

---

## Concept 112 — Frontend Deployment

**PROJECT FACT**

The same workflow builds the frontend, syncs it to S3, and invalidates CloudFront.

---

# 39. Critical Task-Definition Distinction

## Concept 113 — Image-Only Change

With mutable `latest`:

```text
push new latest
+
force service redeploy
→ new task may pull updated latest
```

---

## Concept 114 — Task Definition Change

If you change:

- CPU
- memory
- environment
- secrets
- IAM role
- container config

then:

```text
local JSON edit
≠
AWS ECS update
```

---

## Concept 115 — Register New Revision

You must register a new task-definition revision and update/deploy the service to use it.

---

## Concept 116 — Why This Matters in Interviews

A common weak answer is:

> “I changed task-definition JSON and force redeployed, so ECS used it.”

That is not guaranteed.

---

# 40. Mutable `latest`

## Concept 117 — Why Force Redeploy with `latest`

Since tag name stays the same, a new deployment forces replacement tasks to pull the tag again.

---

## Concept 118 — Why Rollback Is Harder

If both old and new releases were called `latest`, it is harder to know which bytes belonged to each release.

---

# 41. Rolling Deployment

## Concept 119 — What Is Rolling Deployment?

Replace old tasks gradually with new ones while maintaining desired service availability.

---

## Concept 120 — Current Deployment Maturity

Do not claim:

- zero downtime
- blue/green
- canary

Those are not verified current capabilities.

---

# 42. Health Checks

## Concept 121 — Container Health

Checks whether application inside container is functioning.

---

## Concept 122 — Load Balancer Health

Checks whether a target can serve expected network/application response.

---

## Concept 123 — Current Weakness

**PROJECT FACT**

No mature startup/readiness health gate is verified in the release process.

---

# 43. Container Crash Recovery

## Concept 124 — Process Exits

When the Node process exits, the container stops.

---

## Concept 125 — ECS Service Replacement

If service desired count requires a running task, ECS attempts to replace stopped tasks.

---

## Concept 126 — Crash Loop

If root cause remains:

```text
task starts
→ crashes
→ ECS replaces
→ crashes again
```

The service can enter repeated failure.

---

# 44. Troubleshooting Order

## Concept 127 — Start at ECS Service

Use this flow:

```text
ECS Service
 ↓
Deployment / Events
 ↓
Task
 ↓
Stopped Reason
 ↓
Container Exit Code
 ↓
CloudWatch Logs
 ↓
Task Definition
 ↓
Environment / Secrets
 ↓
Networking / SG / DNS / NAT
 ↓
External Dependencies
```

---

# 45. ECR Push Failure

## Concept 128 — Common Causes

- AWS auth
- ECR login
- wrong repository
- wrong region
- missing permission
- wrong account

---

# 46. ECS Cannot Pull Image

## Concept 129 — Check

- image URI
- tag/digest exists
- execution role permissions
- network path to ECR
- task execution setup
- region/account

---

# 47. Task Repeatedly Stops

## Concept 130 — Check

- stopped reason
- exit code
- CloudWatch logs
- missing env/secrets
- app startup exception
- memory limit
- connection failure

---

# 48. Node App Not Listening

## Concept 131 — Check Port

Verify:

```text
application listen port
=
container definition port
=
target group/route expectation
```

---

## Concept 132 — `localhost` Binding Concern

Applications in containers generally should listen on a reachable interface, not only an inaccessible loopback configuration.

Exact current binding should be verified from source.

---

# 49. ALB 502 / 503

## Concept 133 — 502

Possible causes:

- target connection errors
- invalid backend response
- app crash
- wrong port

---

## Concept 134 — 503

Often indicates:

- no healthy targets
- target group empty/unhealthy
- service deployment not ready

---

# 50. Cloud Map DNS Failure

## Concept 135 — Check

- namespace
- service registration
- DNS settings
- VPC resolver
- service name
- task registration

---

# 51. Outbound Provider Failure

## Concept 136 — Private Task Cannot Reach Provider

Check:

```text
route table
NAT Gateway
security group egress
DNS
provider endpoint
```

---

## Concept 137 — NAT Is Especially Important

Agent depends on several public external APIs.

If private tasks lack outbound internet path, those workflows fail.

---

# 52. Secrets Manager AccessDenied

## Concept 138 — Check

- execution role
- secret ARN
- region
- resource policy
- KMS permissions where relevant

---

# 53. CloudWatch Logs Missing

## Concept 139 — Check

- log configuration
- log group/region
- execution-role permissions
- task startup
- application stdout/stderr

---

# 54. MongoDB/Redis Connection Failure

## Concept 140 — Check

- secret/env values
- DNS
- security groups
- external DB allowlist/networking
- TLS/config
- endpoint

---

# 55. New CPU/Memory Not Applied

## Concept 141 — Main Suspect

The service may still run an older task-definition revision.

---

## Concept 142 — Correct Fix

Register the new revision and update service deployment to use it.

---

# 56. Fargate Memory Pressure

## Concept 143 — OOM Behavior

If a task exceeds its memory limit, it can be terminated.

---

## Concept 144 — Agent Risk

Agent handles:

- file buffers
- model/provider responses
- orchestration

So memory usage should be measured.

---

# 57. Scaling

## Concept 145 — Horizontal Scaling

Run multiple tasks for one ECS service.

Example:

```text
Agent task 1
Agent task 2
Agent task 3
```

---

## Concept 146 — Shared State Requirement

To scale horizontally, avoid relying on process-local state for important shared data.

NovaMind uses external:

- Redis
- MongoDB
- Qdrant
- S3

for many shared concerns.

---

## Concept 147 — Scaling Does Not Fix Provider Quotas

More Agent tasks can increase concurrent calls to:

- Groq
- Gemini
- Tavily
- Stability

Provider quotas can become the real bottleneck.

---

## Concept 148 — Scaling Does Not Fix Race Conditions

More tasks may worsen concurrent balance/memory races.

---

## Concept 149 — Scaling Does Not Fix Bad Queries

If MongoDB query is inefficient, adding more callers can increase load.

---

# 58. Autoscaling

## Concept 150 — What Is Autoscaling?

Automatically change task count based on measured demand/metrics.

---

## Concept 151 — Current Status

**PROJECT FACT**

Active mature autoscaling is not verified.

Do not claim it.

---

## Concept 152 — Production V2

Use measured signals such as:

- CPU
- memory
- request rate
- queue depth if async
- latency

rather than arbitrary scaling.

---

# 59. High Availability

## Concept 153 — What Is HA?

High availability means the system continues operating despite component failure.

---

## Concept 154 — Multiple Tasks Alone ≠ HA

Dependencies also matter:

- Redis
- MongoDB
- ALB
- NAT
- provider availability
- networking

---

## Concept 155 — Current HA Boundary

**PROJECT FACT**

Live multi-AZ HA/autoscaling is not verified.

Screenshots/documentation may show one task/service.

---

## Concept 156 — Redis Limitation

The captured Redis setup was previously seen as non-redundant/failover-disabled.

Do not claim Redis HA.

---

# 60. Cost

## Concept 157 — Fargate Cost

Fargate charges based on configured runtime resources/time.

Always-running services create baseline cost.

---

## Concept 158 — Five-Service Baseline

Even when traffic is low, continuously running five services can create ongoing compute cost.

---

## Concept 159 — ALB Cost

ALB has baseline and usage-related charges.

---

## Concept 160 — NAT Cost

NAT Gateway can be significant due to hourly/data processing charges.

---

## Concept 161 — ECR Cost

Image storage and data transfer can contribute cost.

---

## Concept 162 — CloudWatch Logs Cost

High log volume increases ingestion/storage cost.

---

## Concept 163 — External Provider Cost

AI/search/image APIs can dominate variable application cost.

---

# 61. ECS/Fargate vs Kubernetes

## Concept 164 — Kubernetes Not Used

**PROJECT FACT**

NovaMind does not use Kubernetes/EKS.

---

## Concept 165 — Why Fargate Is Reasonable

Engineering trade-off:

```text
Fargate
→ lower infrastructure-management overhead

Kubernetes
→ greater orchestration flexibility, but higher operational complexity
```

Do not claim historical decision reasoning unless confirmed.

---

# 62. Production V2 — Docker

## Concept 166 — Multi-Stage Build

Reduce runtime image size and build-time tools.

---

## Concept 167 — `npm ci`

Improve deterministic dependency installation.

---

## Concept 168 — Effective `.dockerignore`

Prevent unnecessary/sensitive build-context content.

---

## Concept 169 — Non-Root User

Reduce runtime privileges.

---

## Concept 170 — Image Scanning

Scan images/dependencies before deployment.

---

# 63. Production V2 — Release Identity

## Concept 171 — Immutable Tag

Use Git SHA or release version.

---

## Concept 172 — Optional Digest Pinning

Reference exact image digest.

---

## Concept 173 — Explicit Task Revision

Register updated ECS task definition on configuration change.

---

# 64. Production V2 — Health and Rollback

## Concept 174 — Health Endpoint

Provide readiness/liveness endpoint.

---

## Concept 175 — Service Stability Gate

CI/CD waits for ECS service to become stable.

---

## Concept 176 — Smoke Test

After deployment, call important endpoints.

---

## Concept 177 — Deployment Circuit Breaker

Could automatically fail/rollback unhealthy deployment.

This is proposed, not verified current behavior.

---

# 65. Production V2 — Graceful Shutdown

## Concept 178 — Handle SIGTERM

Stop new traffic and close resources cleanly.

---

# 66. Production V2 — Observability

## Concept 179 — Structured Logs

Include:

- request ID
- service
- route
- status
- latency
- error type

without leaking secrets.

---

## Concept 180 — Correlation ID

Trace one user request across:

```text
Gateway
→ Agent
→ Chat/Auth
→ provider
```

---

## Concept 181 — Metrics and Alarms

Track:

- CPU
- memory
- task count
- restart count
- 5xx
- latency
- provider failure

---

# 67. Production V2 — IaC

## Concept 182 — Why IaC?

Infrastructure as Code makes:

- networking
- services
- roles
- policies
- deployments

reproducible and reviewable.

---

## Concept 183 — Current IaC Boundary

**PROJECT FACT**

Comprehensive Terraform/CDK/CloudFormation for the whole platform is not present.

Do not claim full IaC.

---

# 68. Production V2 — HA

## Concept 184 — Multi-AZ Design

If availability requirement justifies it:

- ALB across AZs
- multiple ECS tasks
- resilient Redis
- durable database design
- redundant networking

But measure business need/cost.

---

# 69. Strong Interview Explanation

> NovaMind has five separately containerized Node.js/Express backend services: Gateway on 8000, Auth on 8001, Chat on 8002, Agent on 8003 and Billing on 8004. The eight AI specialists are not separate containers; they run inside the Agent service. Each service is packaged with Docker using a Node 22 Alpine base image, pushed to Amazon ECR, referenced by an ECS task definition, and run as an ECS service on AWS Fargate.
>
> I separate the AWS concepts clearly: ECR stores images, ECS orchestrates containers, and Fargate provides the serverless compute. A task definition is the deployment blueprint, a task is a running instance, and an ECS service keeps the desired number of tasks running. The verified task allocations are 512 CPU / 1024 MiB for Gateway, Auth, Chat and Billing, and 1024 CPU / 2048 MiB for Agent; those are configuration values, not performance guarantees.
>
> The current container/release design still has gaps: mostly single-stage Dockerfiles, no mature non-root runtime or Docker health check, mutable `latest` tags, no verified image-scanning gate, and no immutable release identity. A critical deployment detail is that pushing a new `latest` image and forcing a service redeploy can refresh image content, but editing a local ECS task-definition JSON does not update CPU, memory, environment, secrets or roles in AWS unless a new task-definition revision is registered and deployed.

---

# Quick Revision — Module 14

## Docker

```text
Dockerfile
→ docker build
→ image
→ container
```

## AWS

```text
ECR = image registry
ECS = orchestration
Fargate = compute
Task Definition = blueprint
Task = running workload
Service = maintains tasks
```

## NovaMind Services

```text
Gateway :8000
Auth    :8001
Chat    :8002
Agent   :8003
Billing :8004
```

Eight AI specialists remain inside Agent.

## Resource Allocations

```text
Gateway 512 / 1024
Auth    512 / 1024
Chat    512 / 1024
Billing 512 / 1024
Agent   1024 / 2048
```

Configured allocations only.

## Critical Deployment Rule

```text
New image + same task definition
→ force redeploy may pull updated `latest`

CPU / memory / env / secret / role change
→ register NEW task-definition revision
```

## Current Weaknesses

```text
single-stage Dockerfiles
npm install
possible ineffective .dockerignore
no mature non-root runtime
no Docker HEALTHCHECK
mutable latest tags
no verified image-scanning gate
no mature readiness gate
no immutable release ID
no verified graceful shutdown
task-definition file edits not automatically registered
```

## Production V2

```text
multi-stage
npm ci
effective .dockerignore
non-root
image scan
Git SHA/digest
register task revisions
health/readiness
SIGTERM handling
stability gate
smoke tests
rollback/circuit breaker
measured autoscaling
metrics/alarms
structured logs
least privilege
IaC
HA where justified
cost monitoring
```

## Best Interview Sentence

> **NovaMind uses Docker to package five backend services, ECR to store their images, ECS to orchestrate them, and Fargate to run them; the main production improvements are immutable releases, stronger container hardening, explicit task-definition revisioning, health gates, observability and measured scaling.**

**Module 14 Learning file complete.**
