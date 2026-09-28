"""
NovaMind AI — AWS Architecture Diagram
Style inspired by CortexAI layered architecture diagram.
Run: python generate_architecture.py
Output: novamind-aws-architecture.png
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import ECS, Fargate, ECR
from diagrams.aws.network import CloudFront, ElbApplicationLoadBalancer as ALB, NATGateway
from diagrams.aws.storage import S3
from diagrams.aws.database import ElastiCache
from diagrams.aws.security import SecretsManager, IAM
from diagrams.aws.management import Cloudwatch
from diagrams.onprem.client import Users
from diagrams.onprem.network import Internet

graph_attr = {
    "fontsize": "26",
    "bgcolor": "white",
    "pad": "1.0",
    "splines": "ortho",
    "nodesep": "0.6",
    "ranksep": "1.0",
    "fontname": "Arial",
    "labeljust": "c",
    "labelloc": "t",
}

node_attr = {
    "fontsize": "10",
    "fontname": "Arial",
}

with Diagram(
    "NovaMind AI — AWS Cloud Architecture\nBuilt by Aamir",
    filename="novamind-aws-architecture",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
):

    # ── 1. Client Layer ──
    with Cluster("1. Client Layer"):
        user = Users("User Browser\nReact 19 + Vite\nFirebase Auth SDK")

    # ── 2. AWS Infrastructure ──
    with Cluster("2. AWS Infrastructure"):
        cf    = CloudFront("Amazon CloudFront\nHTTPS CDN\nd8au5xi32kvkz.cloudfront.net")
        s3f   = S3("S3 Frontend\nnovamind-frontend-prod\nReact build HTML/JS/CSS")
        alb   = ALB("Application Load Balancer\nnovamind-alb\nHTTPS termination → :8000")

        with Cluster("Amazon VPC  (novamind-vpc  10.0.0.0/16)"):
            with Cluster("Public Subnets"):
                nat = NATGateway("NAT Gateway\nOutbound to\nexternal APIs")

            with Cluster("Private Subnets — Amazon ECS Cluster (novamind-cluster · AWS Fargate)"):
                gw      = ECS("Express API Gateway\n:8000\nCORS · Session validation\nx-user-id injection\nReverse proxy")
                auth    = ECS("Auth Service\n:8001\nFirebase Admin verify\nCredits · Sessions\nAdmin APIs")
                chat    = ECS("Chat Service\n:8002\nConversations\nMessages\nMongoDB Atlas only")
                agent   = ECS("Agent Service ★\n:8003  CORE AI\nLangGraph orchestration\n8 specialist agents\nRedis memory + rate limits")
                billing = ECS("Billing Service\n:8004\nRazorpay orders\nHMAC verify\nMongoDB Atlas")

            with Cluster("Data & Secrets (Private)"):
                redis = ElastiCache("ElastiCache Redis\nSessions · Agent memory\nRate limits\nGateway · Auth · Agent only")
                s3a   = S3("S3 Artifacts\ncretexainovamind\nPDF · PPTX · PNG\nPresigned URLs 24hr")
                sm    = SecretsManager("Secrets Manager\nAPI Keys · MongoDB URIs\nFirebase JSON\nInjected at ECS startup")
                iam   = IAM("AWS IAM\nTask Execution Role\nAgent Task Role → S3\nAuth Task Role → Secrets")

    # ── 3. AI / Agent Layer ──
    with Cluster("3. AI / LangGraph Agent Layer"):
        with Cluster("LangGraph StateGraph\n(Deterministic routing — NOT autonomous planning)"):
            router  = ECS("router node\nPriority: explicit→PDF→image→LLM")
            n_chat  = Fargate("chat\nGroq LLM")
            n_srch  = Fargate("search\nTavily → Groq")
            n_code  = Fargate("coding\nDeepSeek/OpenRouter")
            n_pdf   = Fargate("pdf\nGroq + PDFKit + S3")
            n_ppt   = Fargate("ppt\nGroq + PptxGenJS + S3")
            n_vis   = Fargate("vision\nGroq + Stability AI + S3")
            n_rag   = Fargate("pdfRag\nGemini embeddings\n+ Qdrant + Groq")
            n_img   = Fargate("imageAnalyzer\nGemini Vision\nmultimodal")

    # ── 4. Observability & CI/CD ──
    with Cluster("4. Observability & CI/CD"):
        ecr = ECR("Amazon ECR\n5 repositories\ngateway · auth · chat\nagent · billing")
        cw  = Cloudwatch("Amazon CloudWatch Logs\n/ecs/novamind-gateway\n/ecs/novamind-auth\n/ecs/novamind-chat\n/ecs/novamind-agent\n/ecs/novamind-billing")

    # ── 5. External / Third-Party ──
    with Cluster("5. External Services  (via NAT Gateway)"):
        mongo      = Internet("MongoDB Atlas\nUsers · Conversations\nMessages · Payments")
        firebase   = Internet("Firebase Auth\nGoogle OAuth\nToken verification")
        groq_api   = Internet("Groq API\nChat · Router\nPDF · PPT · Vision")
        gemini_api = Internet("Google Gemini\nEmbeddings (RAG)\nImage analysis")
        or_api     = Internet("OpenRouter\nDeepSeek Coder\nCoding agent")
        tavily_api = Internet("Tavily API\nWeb search\nSearch agent")
        qdrant_api = Internet("Qdrant Cloud\nVector store\nPDF RAG")
        stab_api   = Internet("Stability AI\nImage generation\nVision agent")
        rp_api     = Internet("Razorpay\nPayment orders\nHMAC verify")

    # ════════════════════════════════
    # ARROWS — Main request flow
    # ════════════════════════════════
    user >> Edge(label="① Load SPA", color="#2E86C1", style="bold") >> cf
    cf   >> Edge(label="origin fetch", color="#FF9900", style="dashed") >> s3f
    user >> Edge(label="② HTTPS API + cookie", color="#1E8449", style="bold") >> alb
    alb  >> Edge(label="③ forward :8000", color="#1E8449", style="bold") >> gw

    gw >> Edge(label="④ session lookup", color="#C0392B", style="bold") >> redis
    gw >> Edge(label="⑤ Cloud Map DNS", color="#7D3C98") >> auth
    gw >> Edge(label="Cloud Map DNS", color="#7D3C98") >> chat
    gw >> Edge(label="⑥ x-user-id header", color="#E67E22", style="bold") >> agent
    gw >> Edge(label="Cloud Map DNS", color="#7D3C98") >> billing

    agent >> Edge(label="⑦ save-message", color="#2E86C1") >> chat
    agent >> Edge(label="⑧ /deduct-credits", color="#AD1457") >> auth
    agent >> Edge(label="memory + rate limits", color="#C0392B") >> redis
    agent >> Edge(label="⑨ PutObject (IAM role)", color="#FF9900") >> s3a
    auth  >> Edge(label="session write/read", color="#C0392B") >> redis
    billing >> Edge(label="/update-plan", color="#AD1457") >> auth

    # LangGraph flow
    agent  >> Edge(color="#E67E22", style="bold") >> router
    router >> n_chat
    router >> n_srch
    router >> n_code
    router >> n_pdf
    router >> n_ppt
    router >> n_vis
    router >> n_rag
    router >> n_img
    n_srch >> Edge(label="search→chat\ngrounded answer", color="#E67E22", style="dashed") >> n_chat

    # CI/CD (dashed)
    ecr >> Edge(label="pull :latest", color="#1E8449", style="dashed") >> gw
    sm  >> Edge(label="inject secrets", color="#AD1457", style="dashed") >> agent
    agent >> Edge(label="awslogs", color="#2E7D32", style="dashed") >> cw
    auth  >> Edge(label="awslogs", color="#2E7D32", style="dashed") >> cw

    # External services
    auth    >> Edge(color="#1E8449") >> mongo
    chat    >> Edge(color="#1E8449") >> mongo
    billing >> Edge(color="#1E8449") >> mongo
    auth    >> Edge(color="#FF9900") >> firebase
    agent   >> Edge(color="#2E86C1") >> groq_api
    agent   >> Edge(color="#1B4F72") >> gemini_api
    agent   >> Edge(color="#7D3C98") >> or_api
    agent   >> Edge(color="#00838F") >> tavily_api
    agent   >> Edge(color="#C0392B") >> qdrant_api
    agent   >> Edge(color="#F39C12") >> stab_api
    billing >> Edge(color="#1E8449") >> rp_api

print("✅ Saved: novamind-aws-architecture.png")
