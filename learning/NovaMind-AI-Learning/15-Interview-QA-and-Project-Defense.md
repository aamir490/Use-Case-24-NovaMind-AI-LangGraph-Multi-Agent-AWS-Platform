# Module 15 — Interview Q&A and Project Defense

> **Project:** NovaMind-AI-LangGraph-Multi-Agent-AWS-Platform  
> **Module:** AWS Networking, IAM, Secrets Manager and CloudWatch  
> **Purpose:** Prepare for deep AWS networking, IAM, secrets, logging, observability, troubleshooting and architecture-defense interviews while keeping current, documented and proposed claims separate.

---

## Accuracy Rules

### CURRENT VERIFIED

```text
Frontend deployment uses S3 + CloudFront.
ECS/Fargate task definitions use awsvpc.
All five backend services use CloudWatch awslogs.
Secrets Manager references exist in ECS configuration.
Cloud Map namespace novamind.local is part of the documented service-discovery design.
A tracked MongoDB credential was found in source/task-definition context.
A local Firebase key existed but was ignored from source control.
Effective IAM least privilege was not fully live-inspected.
```

### DOCUMENTED / INTENDED

```text
ALB fronting Gateway
private ECS task placement
public/private subnet topology
NAT outbound internet path
some SG relationships
Cloud Map internal service discovery
```

### PRODUCTION V2 — PROPOSED

```text
IaC networking
least-privilege SGs
service-to-service authentication
separate least-privilege task roles
secret rotation
VPC endpoint evaluation
structured logs
correlation IDs
metrics
alarms
dashboards
distributed tracing
multi-AZ networking where justified
```

### Do not claim

```text
exact live subnet topology
exact live security-group rules
verified NAT health
active VPC endpoints
mTLS
zero-trust networking
fully verified least privilege
mature secret rotation
comprehensive alarms
AWS X-Ray
verified multi-AZ HA
production readiness
```

---

# Networking Fundamentals

## Q1. What is a VPC?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A VPC is a logically isolated virtual network in AWS where resources such as ALBs, ECS tasks, subnets and ENIs can run.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q2. What is CIDR?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> CIDR defines an IP address range, such as `10.0.0.0/16`.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q3. What is a subnet?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A smaller IP range inside a VPC.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q4. What is a public subnet?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A subnet whose route table has a route to an Internet Gateway; that alone does not automatically make every resource public.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q5. What is a private subnet?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A subnet without direct public internet routing through an Internet Gateway.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q6. What is a route table?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A set of rules deciding where network traffic is sent.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q7. Does a route table act as a firewall?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q8. What is an Internet Gateway?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> The VPC component that connects public routing to the internet.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q9. What is a NAT Gateway?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A managed service that lets private resources initiate outbound internet connections.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q10. NAT Gateway vs Internet Gateway?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> NAT provides outbound internet access for private resources; the Internet Gateway connects the VPC to the public internet.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# NovaMind Network Architecture

## Q11. How is the frontend delivered?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> CloudFront serves the React frontend from S3.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q12. What is the documented backend request path?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> React API request → ALB → Gateway ECS/Fargate → Auth/Chat/Agent/Billing.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q13. Is that entire live topology fully verified?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No; the ALB/private-subnet/NAT topology is documented/intended rather than fully live-proven.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q14. What is the intended backend placement?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Public-facing entry through ALB, with backend ECS/Fargate tasks privately placed.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q15. Why do private Agent tasks need outbound internet?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Agent calls public providers such as Groq, Gemini, OpenRouter, Tavily and Stability AI.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q16. What is the intended outbound path?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Private task → route table → NAT Gateway → Internet Gateway → external provider.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# North-South and East-West

## Q17. What is north-south traffic?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Traffic entering or leaving the application boundary.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q18. Give a NovaMind north-south example.

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Browser → ALB or Agent → external AI provider.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q19. What is east-west traffic?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Service-to-service traffic inside the application/network.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q20. Give NovaMind east-west examples.

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Gateway→Agent, Agent→Chat and Billing→Auth.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q21. Does east-west traffic automatically become trusted?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Security Groups

## Q22. What is a security group?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A stateful virtual firewall controlling inbound and outbound traffic for AWS network interfaces/resources.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q23. What does stateful mean?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Return traffic for an allowed connection is automatically allowed.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q24. Security group vs application authorization?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Security group controls network reachability; application authorization controls whether an identity may perform an action.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q25. What is the intended ALB-to-Gateway pattern?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> ALB security group should be allowed to reach Gateway's security group on the application port.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q26. Are the exact live NovaMind SG rules verified?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q27. Should internal services accept traffic from anywhere in the VPC?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Ideally no; allow only required trusted sources.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# awsvpc and ENI

## Q28. What ECS network mode is verified?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> `awsvpc`.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q29. What does awsvpc give a Fargate task?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Its own ENI, VPC IP and security-group-controlled network identity.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q30. What is an ENI?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> An Elastic Network Interface, a virtual network interface in AWS.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q31. Why is awsvpc important?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Tasks become first-class VPC network endpoints that can be targeted and secured independently.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q32. Does awsvpc mean the task is public?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# ALB and Target Groups

## Q33. What is ALB?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> AWS Application Load Balancer for HTTP/HTTPS traffic.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q34. What is a target group?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A set of backend targets that receive ALB traffic.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q35. What is a health check?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A probe used to determine whether a target should receive traffic.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q36. ALB vs Express Gateway?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> ALB is AWS load balancing; Express Gateway is NovaMind's Node.js application service.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q37. Express Gateway vs AWS API Gateway?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> They are different; NovaMind uses an Express Gateway service, not AWS API Gateway for this architecture.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q38. What can ALB 503 mean?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No healthy targets or service unavailable.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q39. What can ALB 502 mean?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Backend connection, port, protocol or invalid-response issues.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# DNS and Cloud Map

## Q40. What is DNS?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Name-to-address resolution.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q41. What is AWS Cloud Map?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> AWS service discovery.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q42. What namespace is used in NovaMind's documented design?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> `novamind.local`.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q43. What does Cloud Map solve?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Finding internal service endpoints by name.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q44. Does Cloud Map authenticate callers?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q45. Does Cloud Map authorize callers?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q46. Is Cloud Map a load balancer?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q47. Give a possible NovaMind service-discovery path.

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Gateway resolves Agent or Agent resolves Chat through internal DNS/service discovery.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# IAM Fundamentals

## Q48. What is IAM?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> AWS Identity and Access Management, used to control access to AWS APIs/resources.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q49. IAM user vs IAM role?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> User is a long-lived identity; role is an assumed identity with temporary credentials.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q50. Why should ECS workloads use roles?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> To avoid embedding long-lived AWS credentials inside containers.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q51. What are the four basic IAM policy elements?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Effect, Action, Resource and optional Condition.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q52. What is least privilege?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Grant only the permissions actually required.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q53. Does having an IAM role prove least privilege?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q54. Were NovaMind effective IAM permissions fully live-inspected?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Execution Role vs Task Role

## Q55. What is the ECS execution role?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> The role used for ECS/Fargate startup operations such as image pull, log delivery and startup secret retrieval.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q56. What is the ECS task role?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> The role used by application code inside the running container for AWS API calls.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q57. Execution role vs task role?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Startup/control-plane permissions versus application-runtime permissions.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q58. Which role would Agent use for S3 API calls?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> The task role.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q59. Which role is involved in pulling the ECR image?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> The execution role.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q60. Can one broad task role be shared by every service safely?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> It can work technically, but separate least-privilege roles are safer when services have different needs.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Least Privilege

## Q61. Why is `Action:* Resource:*` risky?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> It grants extremely broad access and increases blast radius.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q62. What S3 permission might Agent need?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Only the specific artifact bucket/prefix actions required, such as PutObject/GetObject-related access.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q63. Should Chat automatically have S3 admin permissions?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q64. Should Billing have unrelated IAM/S3 permissions?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q65. How would you verify least privilege?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Inspect effective role policies and compare them with actual service API usage.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Secrets Manager

## Q66. What is Secrets Manager?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A managed AWS service for storing sensitive runtime values.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q67. Are Secrets Manager references present in NovaMind?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q68. What kinds of secrets are relevant?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Database/provider/Firebase-type credentials/configuration.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q69. Does using Secrets Manager prove no secrets exist elsewhere?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q70. What credential exposure was found?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A MongoDB credential was tracked in task-definition/source context.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q71. What local secret was present?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A local Firebase key existed but was ignored from source control.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q72. What should happen after secret exposure?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Rotate/revoke, remove the hard-coded value, use managed secret delivery and audit use.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q73. Can you claim the exposed secret was already rotated?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No, not without verification.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Secret Injection

## Q74. How can ECS inject a secret?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> At task startup, configured secret references are resolved and provided to the container runtime environment.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q75. Which IAM role is normally involved in startup secret retrieval?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> The execution role.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q76. Should secrets be embedded into the Docker image?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q77. Should secrets be printed into logs?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q78. Should backend secrets be returned to frontend code?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Secret Rotation

## Q79. What is secret rotation?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Replacing an old secret with a new one and safely updating dependent applications.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q80. Is mature automatic secret rotation verified in NovaMind?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q81. What must a safe rotation plan include?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> New secret creation/versioning, deployment/update, validation, old-secret retirement and monitoring.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# CloudWatch Logs

## Q82. What logging integration is verified?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> All five backend ECS services use the CloudWatch `awslogs` driver.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q83. What is the log flow?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Container stdout/stderr → awslogs → CloudWatch Logs.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q84. What is a log group?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A logical collection of related logs.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q85. What is a log stream?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A sequence of log events from a particular source/task/container.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q86. Does CloudWatch Logs equal full observability?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Observability Fundamentals

## Q87. What are the three observability pillars?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Logs, metrics and traces.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q88. What are logs good for?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Detailed event/error records.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q89. What are metrics good for?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Numerical trends such as latency, CPU, memory and error rate.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q90. What are traces good for?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Following one request across multiple services and operations.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q91. What is a span?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> One operation within a trace.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q92. Why does NovaMind benefit from tracing?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A request can cross Gateway, Agent, Chat/Auth and external providers.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q93. Are mature distributed traces verified?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Correlation IDs

## Q94. What is a correlation ID?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A request identifier propagated across services so related logs can be connected.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q95. Why is it useful in NovaMind?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> One user request can cross several services and providers.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q96. Is mature cross-service correlation currently verified?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q97. Where should correlation ID begin?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> At the edge/Gateway and then be forwarded to internal services.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Metrics and Alarms

## Q98. What infrastructure metrics matter?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> CPU, memory, running tasks, target health, ALB request/5xx metrics.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q99. What application metrics matter?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Workflow latency, provider errors, Redis/MongoDB failures, payment/artifact failures.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q100. What is an alarm?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A rule that reacts to a metric threshold/condition.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q101. Are comprehensive alarms current?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q102. What would an example alarm be?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> High Agent 5xx rate or no healthy ALB targets.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Dashboards

## Q103. What is a dashboard?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A visual view of metrics and health indicators.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q104. Does a dashboard fix failures automatically?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q105. Is a mature NovaMind dashboard suite verified?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Tracing

## Q106. Should you claim AWS X-Ray?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No, not unless implemented and verified.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q107. What would tracing help diagnose?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Which service/provider caused latency or failure.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Network Troubleshooting Model

## Q108. What troubleshooting order do you use for connectivity?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Source → DNS → Route → Security Group → Target → Port → Application Health.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q109. Why start with DNS?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> If the name does not resolve, later network layers are irrelevant.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q110. Why check route tables?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Correct DNS does not guarantee a route exists.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q111. Why check SG after route?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Traffic can be routed but still blocked.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q112. Why check port/application last?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Network can be healthy while the app listens on the wrong port or is unhealthy.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Provider Connectivity

## Q113. Agent task is running but Groq calls fail. What do you check?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> DNS, SG egress, route table, NAT, provider endpoint, API key, quota/status and logs.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q114. If all public providers fail from private ECS, what common suspect exists?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Outbound routing/NAT/DNS.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q115. If only one provider fails, what else do you check?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Provider-specific key, endpoint, quota or outage.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q116. Does running ECS task prove internet connectivity?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# NAT Troubleshooting

## Q117. What indicates NAT trouble?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Private tasks cannot reach multiple public internet endpoints.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q118. What do you inspect?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Private route table, NAT Gateway, NAT subnet route to IGW, SG egress and DNS.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q119. Does NAT provide inbound public access?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Cloud Map Troubleshooting

## Q120. What if `novamind.local` service does not resolve?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Check namespace, service registration, VPC DNS and service name.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q121. If name resolves but connection fails?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Check target port, SG, task health and application listener.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# MongoDB Troubleshooting

## Q122. MongoDB connection fails. What do you check?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> URI secret, DNS, network allowlist/security, TLS/configuration and credentials.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q123. Can CloudWatch logs help?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Yes, application startup/runtime logs can show connection errors.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Redis Troubleshooting

## Q124. What does Redis failure affect?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Sessions, fast conversation memory/context and rate limiting.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q125. What do you check?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Endpoint, DNS, SG, credentials/config, node health and connectivity.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Qdrant Troubleshooting

## Q126. What does Qdrant failure affect?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> PDF RAG retrieval.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q127. Should NovaMind silently answer ungrounded if Qdrant fails?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No; it should expose retrieval failure rather than pretend grounding occurred.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q128. What do you check?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Endpoint, DNS, API key, collection, region/latency and service health.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# S3 AccessDenied

## Q129. What is your S3 AccessDenied debugging path?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Agent task → task role → IAM action → resource ARN/prefix → bucket policy → region/key.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q130. Which role matters for app S3 calls?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Task role.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q131. Can execution role permissions replace task role permissions?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Secrets AccessDenied

## Q132. What is the startup-secret debug path?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Task startup → execution role → secret ARN → Secrets Manager permissions → KMS permissions if applicable.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q133. Why can a task fail before application logs appear?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Startup secret/image pull errors can happen before the app starts.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# CloudWatch Missing Logs

## Q134. What do you check when logs are missing?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> awslogs configuration, log group/region, execution-role permissions, whether the task started, and stdout/stderr.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q135. Could the app be crashing before logging?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Yes.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Public vs Private Tasks

## Q136. What is the advantage of public ECS tasks?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Simpler outbound internet connectivity.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q137. What is the downside?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Greater exposure and stricter security requirements.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q138. What is the benefit of private ECS tasks + NAT?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Reduced direct inbound exposure.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q139. What is the downside?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> NAT cost and network complexity.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q140. Which is universally better?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Neither; it depends on requirements/threat/cost.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# VPC Endpoints

## Q141. What is a VPC endpoint?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Private connectivity to supported AWS services without traversing public internet/NAT.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q142. Are VPC endpoints verified current for NovaMind?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q143. Why evaluate them?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Potential security and NAT-cost benefits for AWS-service traffic.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Cost

## Q144. What networking component can create meaningful baseline cost?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> NAT Gateway.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q145. Why?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Hourly and data-processing charges.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q146. What CloudWatch cost factors matter?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Log ingestion, retention and queries.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q147. Why can verbose logging be expensive?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> More bytes ingested/stored.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q148. Why can verbose logging be risky?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Sensitive data may be recorded.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Security Trade-offs

## Q149. Does private subnet solve authorization?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q150. Does SG solve IAM?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q151. Does IAM solve app-level ownership?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q152. What does each layer protect?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> SG controls network reachability, IAM controls AWS API permissions, application authorization controls business/resource access.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Production V2 Networking

## Q153. What would you codify with IaC?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> VPC, subnets, route tables, NAT, SGs, ALB, target groups and Cloud Map.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q154. Why IaC?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Reproducibility, reviewability and drift reduction.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q155. What SG improvement would you make?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Allow only required service-to-service paths.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q156. Would you verify private placement?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Yes, through IaC/runtime inspection rather than documentation alone.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q157. Would you automatically add VPC endpoints?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No; evaluate security/cost benefits first.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Production V2 IAM

## Q158. What IAM improvement would you make?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Separate least-privilege task roles by service.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q159. What should be audited?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Wildcards, unused actions/resources and unnecessary cross-service access.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q160. Would you claim least privilege today?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Production V2 Secrets

## Q161. What is the first secret-hygiene priority?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Rotate any known exposed credential.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q162. What should be removed from Git/task JSON?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Plaintext secrets.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q163. What should runtime use?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Managed secret references with restricted IAM.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q164. Would you add rotation?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Yes where operationally appropriate, but it is proposed.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Production V2 Observability

## Q165. What log improvement would you make?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Structured logs with service, request ID, route, latency, status and error type.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q166. What correlation improvement?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Generate at Gateway and propagate across internal calls.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q167. What metric improvement?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Add application/provider/business metrics in addition to infrastructure metrics.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q168. What alarm improvement?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Alert on task failures, ALB 5xx/no healthy targets, Redis/MongoDB/provider errors.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q169. What trace improvement?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Add distributed tracing where debugging/latency value justifies cost.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q170. What retention improvement?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Define log retention by log type.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Design Defense

## Q171. Why use private ECS tasks?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> It can reduce direct inbound exposure while still allowing controlled outbound access through NAT.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q172. Why use Cloud Map?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> To discover internal services by DNS name instead of hard-coded task IPs.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q173. Why not call Cloud Map authentication?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> It only helps locate a service.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q174. Why separate execution role and task role?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> ECS startup needs different permissions from application runtime AWS API calls.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q175. Why use Secrets Manager if env vars are still used?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> The secret can be injected at runtime rather than stored in source/image.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q176. Why isn't CloudWatch Logs enough?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Logs do not provide complete metrics/tracing/correlation by themselves.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q177. Why not make every internal service public?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> It increases attack surface and bypass risk.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Pressure Questions

## Q178. If the task is in a public subnet, is it public?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Not automatically; it also needs appropriate routing, public addressing and security configuration.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q179. If the security group allows traffic, why can the call still fail?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> DNS, routing, port, target health or application issues can still fail.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q180. If DNS resolves, why can connection fail?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> A route, SG, target or port can still block it.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q181. If Secrets Manager is used, why did a credential leak?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Using Secrets Manager in some places does not guarantee secrets were removed everywhere.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q182. If CloudWatch logs exist, why can't you trace one request end to end?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> Without correlation IDs/distributed tracing, related log events across services are difficult to connect.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q183. If tasks are private, are they zero trust?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q184. If Cloud Map resolves Agent, is Agent authenticated?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q185. If the task role has S3 permission, can User A access User B's artifact?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> IAM only allows the service to call S3; application ownership checks still decide user access.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q186. Can you claim live NAT health?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q187. Can you claim exact live SG rules?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> No.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

## Q188. What is the strongest accurate networking claim?

**What the interviewer is testing:** Whether you understand the networking/security/observability layer and can clearly separate live-verified facts from intended architecture and future hardening.

**Word-for-word answer:**

> NovaMind has verified ECS `awsvpc`, CloudWatch logging and Secrets Manager references, with a documented ALB/private-task/NAT/Cloud Map architecture whose exact live state was not fully verified.

**Likely follow-up:** Be ready to explain **the packet/request path, which IAM role is involved, what the failure would look like, and whether the claim is current, documented/intended, or proposed**.

**Defense reminder:** Network reachability, AWS IAM permission, and application authorization are three different layers.

---

# Rapid-Fire Revision

**Q189. Frontend delivery?**  
CloudFront → S3.

**Q190. Backend ALB topology status?**  
Documented/intended, not fully live-verified.

**Q191. ECS network mode?**  
awsvpc.

**Q192. Task gets?**  
ENI + private IP + SG.

**Q193. Public subnet = public resource?**  
No.

**Q194. NAT = IGW?**  
No.

**Q195. NAT purpose?**  
Outbound internet for private resources.

**Q196. SG type?**  
Stateful firewall.

**Q197. SG = authorization?**  
No.

**Q198. Cloud Map namespace?**  
novamind.local.

**Q199. Cloud Map = authentication?**  
No.

**Q200. Execution role?**  
ECS startup permissions.

**Q201. Task role?**  
Application runtime AWS API permissions.

**Q202. Least privilege fully verified?**  
No.

**Q203. Secrets Manager refs?**  
Yes.

**Q204. Tracked MongoDB credential?**  
Yes.

**Q205. Mature secret rotation?**  
No.

**Q206. Backend logging?**  
CloudWatch awslogs.

**Q207. CloudWatch Logs = full observability?**  
No.

**Q208. Metrics mature?**  
Not fully verified.

**Q209. Alarms mature?**  
Not fully verified.

**Q210. Tracing mature?**  
No.

**Q211. X-Ray verified?**  
No.

**Q212. NAT health verified?**  
No.

**Q213. VPC endpoints verified?**  
No.

**Q214. Multi-AZ HA verified?**  
No.

# Cross-Question Chain 1 — VPC and Subnets

**Interviewer:** What is the difference between public and private subnet?

> A public subnet has a route to an Internet Gateway. A private subnet does not directly route to the Internet Gateway. But a resource in a public subnet is not automatically public; public addressing and security configuration also matter.

**Interviewer:** How can a private Agent call Groq?

> The documented design uses an outbound NAT path: the private subnet routes internet-bound traffic to a NAT Gateway, which reaches the internet through the VPC's Internet Gateway.

---

# Cross-Question Chain 2 — Security Groups

**Interviewer:** If Gateway's security group allows Agent traffic, is the request authorized?

> No. The security group only permits network reachability. Application authentication and authorization still need to validate the caller and resource permission.

---

# Cross-Question Chain 3 — Cloud Map

**Interviewer:** What does `novamind.local` do?

> It is the documented Cloud Map namespace used for internal service discovery so services can resolve each other by name.

**Interviewer:** Does that secure the service?

> No. Cloud Map is discovery, not authentication or authorization.

---

# Cross-Question Chain 4 — Execution Role vs Task Role

**Interviewer:** Which role does ECS use to pull the ECR image?

> The ECS execution role supports startup operations such as image pull, log delivery and startup secret retrieval.

**Interviewer:** Which role does Agent use to write an artifact to S3?

> The task role used by the running application.

---

# Cross-Question Chain 5 — Secrets

**Interviewer:** You use Secrets Manager, so are all secrets secure?

> Not automatically. The deployment does use Secrets Manager references, but the review also found a tracked MongoDB credential in source/task-definition context, so I would not claim full secret hygiene.

**Interviewer:** What would you do?

> Rotate the exposed credential, remove hard-coded values, use managed secret injection and audit the old credential's use.

---

# Cross-Question Chain 6 — Observability

**Interviewer:** What monitoring do you have?

> All five backend services send container stdout/stderr to CloudWatch Logs through awslogs. That gives centralized logging, but I would not claim mature metrics, alarms, dashboards or distributed tracing today.

---

# Cross-Question Chain 7 — Provider Connectivity

**Interviewer:** Agent task is running but every public provider fails. What do you check?

> I check DNS first, then the private subnet route, NAT Gateway path, security-group egress, provider endpoint connectivity, API keys, quota/status and CloudWatch logs.

---

# Cross-Question Chain 8 — S3 AccessDenied

**Interviewer:** Agent gets S3 AccessDenied. Which role do you inspect?

> The task role because application code is making the S3 request. Then I inspect the IAM action/resource, bucket policy, key/prefix and region.

---

# 30-Second Interview Answer

> NovaMind's verified frontend is served from S3 through CloudFront. The backend architecture is documented as an ALB fronting the Gateway ECS/Fargate service, with backend services intended to run privately. ECS tasks use `awsvpc`, so each task has an ENI, private IP and security-group-controlled network identity. The deployment also uses Secrets Manager references and CloudWatch `awslogs`. I clearly separate the execution role from the task role, and I do not claim that the documented subnet/NAT/SG topology or least-privilege IAM has been fully live-verified.

---

# 60–90 Second Interview Answer

> NovaMind's networking design separates frontend delivery from backend service traffic. The React frontend is deployed to S3 and served through CloudFront. The documented backend architecture has an ALB routing API traffic to the Gateway ECS/Fargate service, with Auth, Chat, Agent and Billing behind it. The ECS task definitions use `awsvpc`, so every Fargate task receives its own ENI, private IP and security-group-controlled network identity.
>
> The documented design places backend tasks privately. Agent still needs outbound internet access because it calls Groq, Gemini, OpenRouter, Tavily and Stability AI, so NAT is part of the intended architecture. I do not present the exact live subnet, SG and NAT state as verified because the repository analysis did not inspect all live resources.
>
> For IAM, the execution role handles ECS startup operations like image pulls, logs and startup secrets, while the task role is used by the application for AWS APIs such as S3. Secrets Manager references exist, but a tracked MongoDB credential was also identified. CloudWatch `awslogs` is configured for all five backend services, giving centralized logs, but full observability such as mature metrics, alarms, correlation IDs and tracing is not yet verified.

---

# 2–3 Minute AWS Networking / Security / Observability Defense

> NovaMind has a layered AWS network and security design. On the frontend side, the React build is stored in S3 and delivered through CloudFront. On the backend side, the repository documents an Application Load Balancer as the public API entry point, routing requests to the Gateway ECS/Fargate service. The other backend services are intended to communicate internally behind that entry point.
>
> The ECS task definitions use `awsvpc`, which means each Fargate task gets its own elastic network interface, private IP and security-group-controlled network identity. The documented design places backend tasks in private subnets. Because the Agent service calls external public APIs such as Groq, Gemini, OpenRouter, Tavily and Stability AI, those private tasks need outbound internet access, typically through a NAT Gateway. I describe the ALB, subnet and NAT topology as documented/intended because the exact live AWS state was not fully inspected.
>
> For service discovery, the design uses Cloud Map with the `novamind.local` namespace. I make a clear distinction that Cloud Map only provides DNS/service discovery; it does not authenticate or authorize the calling service.
>
> IAM is split between the ECS execution role and task role. The execution role supports startup activities such as pulling from ECR, writing logs and retrieving startup secrets. The task role gives running application code AWS API permissions, for example Agent accessing S3. The presence of roles does not prove least privilege, and effective IAM policies were not fully live-inspected.
>
> Secrets Manager references are present in the ECS configuration, but the review also found a MongoDB credential tracked in source/task-definition context, so the secret lifecycle still needs hardening. I would rotate exposed credentials and remove plaintext secrets rather than claiming current secret management is perfect.
>
> All five backend services use the `awslogs` driver to send stdout/stderr to CloudWatch Logs. That gives basic centralized logging, but logs are only one observability pillar. Mature metrics, alarms, correlation IDs and distributed tracing are not fully verified today.
>
> For Production V2 I would codify the networking with IaC, audit security groups and IAM for least privilege, authenticate service-to-service calls, rotate exposed credentials, evaluate VPC endpoints/NAT cost, add structured logs with request IDs, create actionable metrics/alarms, add tracing where justified, and define log-retention and multi-AZ strategies based on actual availability requirements.

---

# Troubleshooting Drill 1 — ALB 503

```text
ALB 503
  ↓
Check target group
  ↓
Any registered targets?
  ↓
Any healthy targets?
  ↓
Task running?
  ↓
Port correct?
  ↓
SG allows ALB → task?
  ↓
Health endpoint responding?
```

---

# Troubleshooting Drill 2 — ALB 502

```text
ALB 502
  ↓
Backend connection?
  ↓
Correct target port?
  ↓
App listening?
  ↓
Protocol mismatch?
  ↓
Container crash/reset?
  ↓
CloudWatch logs
```

---

# Troubleshooting Drill 3 — Provider Timeout

```text
Agent healthy
  ↓
DNS
  ↓
Private route table
  ↓
NAT
  ↓
SG egress
  ↓
TLS/provider endpoint
  ↓
API key
  ↓
Quota/status
  ↓
CloudWatch logs
```

---

# Troubleshooting Drill 4 — Secrets Manager AccessDenied

```text
Task startup
  ↓
Execution role
  ↓
Secret ARN
  ↓
secretsmanager permission
  ↓
KMS permission if required
  ↓
region/resource policy
```

---

# Troubleshooting Drill 5 — S3 AccessDenied

```text
Agent application
  ↓
Task Role
  ↓
s3 Action
  ↓
Resource ARN/prefix
  ↓
Bucket Policy
  ↓
Key / Region
```

---

# Current vs Production V2

| Area | Current / Documented | Production V2 Proposal |
|---|---|---|
| Frontend | CloudFront + S3 | Keep/harden |
| ECS networking | `awsvpc` verified | Keep |
| ALB | documented/intended | IaC + health validation |
| Private ECS | documented/intended | IaC + verified placement |
| NAT | documented/intended | Validate + cost optimize |
| Cloud Map | `novamind.local` documented | Keep + service auth |
| SGs | not fully live-verified | Least-privilege flows |
| IAM roles | present | Separate/audit least privilege |
| Secrets | Secrets Manager refs + exposure gap | Rotation + no plaintext |
| Logs | CloudWatch awslogs | Structured logging |
| Metrics | basic AWS metrics possible | Custom/application metrics |
| Alarms | not maturely verified | Actionable alarms |
| Tracing | not verified | Add where justified |
| IaC | not comprehensive | Full reproducible networking |
| HA | not verified | Multi-AZ where justified |

---

# What Not to Say

Do not say:

- “The exact VPC/subnet topology is live verified.”
- “Every ECS task definitely runs in a private subnet today.”
- “NAT health is verified.”
- “Cloud Map authenticates microservices.”
- “Security groups authorize users.”
- “IAM replaces application authorization.”
- “Execution role and task role are the same.”
- “Least privilege is fully verified.”
- “All secrets are securely managed.”
- “Secret rotation is fully automated.”
- “CloudWatch Logs means we have full observability.”
- “We have comprehensive alarms and dashboards.”
- “We use X-Ray.”
- “We use mTLS.”
- “We have zero-trust networking.”
- “Multi-AZ HA is verified.”
- “The platform is production-ready.”

---

# Final Self-Test

Before Module 16, explain without notes:

- VPC
- CIDR
- subnet
- public vs private subnet
- route table
- IGW
- NAT
- SG
- stateful behavior
- north-south vs east-west
- ALB
- target group
- 502 vs 503
- awsvpc
- ENI
- DNS
- Cloud Map
- novamind.local
- IAM
- user vs role
- policy elements
- least privilege
- execution role
- task role
- S3 AccessDenied path
- Secrets Manager
- secret injection
- secret exposure
- rotation
- awslogs
- log groups/streams
- logs vs metrics vs traces
- correlation IDs
- alarms
- provider-connectivity debugging
- NAT troubleshooting
- Cloud Map troubleshooting
- Redis/MongoDB/Qdrant failures
- CloudWatch missing logs
- public vs private ECS trade-off
- VPC endpoints
- NAT cost
- CloudWatch cost
- Production V2

**Module 15 interview preparation complete.**
