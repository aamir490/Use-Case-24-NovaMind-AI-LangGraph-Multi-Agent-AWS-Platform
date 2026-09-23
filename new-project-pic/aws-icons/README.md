# Architecture diagram assets

The README diagram uses original PNG icons from the [official AWS Architecture Icons](https://aws.amazon.com/architecture/icons/) July 2026 release. Icons are embedded in the SVG, so neither output needs network access to render.

Package: [Icon-package_07312026.zip](https://d1.awsstatic.com/onedam/marketing-channels/website/public/shared/architecture-icon-release/Icon-package_07312026.5846e92413caa21490223536cc97f1269e44fa92.zip).

The twelve PNGs in this directory are unmodified assets extracted from the package, renamed for the renderer. Service icons use the 64@5x variants; ALB and NAT use the corresponding 48-pixel resource icons. AWS permits these assets in architecture diagrams; see the source page for usage information.

## Regenerate

From the repository root, with Python and Pillow installed:

```sh
python scripts/render_architecture.py
```

Outputs: `new-project-pic/novamind-aws-architecture.png` and `.svg`. The renderer uses Arial on Windows or DejaVu Sans on Linux. It requires no Graphviz, AWS credentials or network access.

## Evidence and interpretation

- `backend/gateway/index.js` and `middleware/auth.middleware.js`: public auth proxy, protected routes, Redis sessions.
- `backend/services/agent/graph/{graph,router}.js`: eight specialist nodes in one process, routing precedence and search-to-chat edge.
- `backend/services/agent/controllers/agent.controller.js`: Chat persistence calls and Redis memory updates.
- `backend/services/agent/config/` and `agents/`: provider clients, vector retrieval, memory, rate limits and S3 configuration.
- `backend/services/agent/index.js`: MongoDB connection on startup; persistent messages are saved through Chat.
- `backend/services/billing/controllers/billing.controller.js`: Razorpay verification and Auth plan update.
- `task-defs/*.json`: five Fargate tasks, ports, Cloud Map URLs, secret injection, roles and CloudWatch logging.
- `.github/workflows/deploy.yml`: ECR pushes, ECS deployment commands, dependent frontend build/sync/invalidation job. There is no service-stability wait in this workflow.
- `deploy-guide-aws.md` and `deploy-guide-aws-original.md`: documented VPC, public/private subnets, ALB and NAT topology. No live infrastructure inspection was performed.

The API endpoint is a frontend build setting. The diagram does not infer a CloudFront API origin or an active HTTPS ALB listener from that setting. AWS regional managed services are outside the VPC boundary. External providers are labeled explicitly instead of using AWS icons. Numbered markers identify architecture stages; requests do not execute every stage in numerical order. Solid arrows show selected request/data dependencies, while dashed arrows show shared egress, logging or deployment; annotations cover service calls omitted to keep the diagram legible.
