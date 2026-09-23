"""Render the README architecture as PNG and self-contained SVG.

Run: python scripts/render_architecture.py (requires Pillow).
The checked-in AWS icons are from the official July 2026 asset package.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import base64
import html
import math

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'new-project-pic'
ICONS = OUT / 'aws-icons'
W, H = 1800, 1640
im = Image.new('RGB', (W, H), 'white')
d = ImageDraw.Draw(im)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
       '<title id="title">NovaMind AI numbered AWS architecture</title>',
       '<desc id="desc">Browser, CloudFront and S3 frontend, ALB, five ECS Fargate services, Redis, LangGraph specialists, external providers, artifact storage, security and deployment.</desc>',
       '<rect width="100%" height="100%" fill="white"/>']
INK, MUTED, BLUE, BORDER = '#17263c', '#526278', '#1765ad', '#cbd5e1'

def font(size, bold=False):
    candidates = [Path('C:/Windows/Fonts') / ('arialbd.ttf' if bold else 'arial.ttf'),
                  Path('/usr/share/fonts/truetype/dejavu') / ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')]
    return ImageFont.truetype(str(next(p for p in candidates if p.exists())), size)

def text(x, y, s, size=20, fill=INK, bold=False):
    d.text((x,y), s, font=font(size,bold), fill=fill)
    svg.append(f'<text x="{x}" y="{y+size*.92}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{fill}">{html.escape(s)}</text>')

def box(x,y,w,h,fill='white',stroke=BORDER,r=10):
    d.rounded_rectangle((x,y,x+w,y+h), radius=r, fill=fill, outline=stroke, width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

def icon(x,y,name,size=52):
    p = ICONS / (name+'.png')
    asset = Image.open(p).convert('RGBA').resize((size,size),Image.Resampling.LANCZOS)
    im.paste(asset,(x,y),asset)
    enc=base64.b64encode(p.read_bytes()).decode()
    svg.append(f'<image x="{x}" y="{y}" width="{size}" height="{size}" href="data:image/png;base64,{enc}"/>')

def badge(x,y,n):
    d.ellipse((x,y,x+32,y+32),fill=BLUE)
    svg.append(f'<circle cx="{x+16}" cy="{y+16}" r="16" fill="{BLUE}"/>')
    s=str(n); text(x+(10 if n<10 else 5),y+5,s,18,'white',True)

def card(x,y,w,h,title,lines=(),ico=None,n=None):
    box(x,y,w,h)
    tx=x+18
    if ico: icon(x+18,y+18,ico); tx=x+84
    size=21
    while d.textlength(title,font=font(size,True)) > x+w-14-tx: size-=1
    text(tx,y+18,title,size,bold=True)
    for i,s in enumerate(lines):
        size=18
        while d.textlength(s,font=font(size)) > x+w-14-tx: size-=1
        text(tx,y+49+i*25,s,size,MUTED)
    if n: badge(x+w-39,y-15,n)

def arrow(points,label=None,lx=None,ly=None,dashed=False,color=BLUE):
    for a,b in zip(points,points[1:]):
        if dashed:
            length=math.dist(a,b)
            for t in range(0,int(length),14):
                q=min(t+7,length)
                d.line((a[0]+(b[0]-a[0])*t/length,a[1]+(b[1]-a[1])*t/length,a[0]+(b[0]-a[0])*q/length,a[1]+(b[1]-a[1])*q/length),fill=color,width=2)
        else: d.line((a,b),fill=color,width=3)
    a,b=points[-2:]; angle=math.atan2(b[1]-a[1],b[0]-a[0]);
    head=[b,(b[0]-11*math.cos(angle-.45),b[1]-11*math.sin(angle-.45)),(b[0]-11*math.cos(angle+.45),b[1]-11*math.sin(angle+.45))]
    d.polygon(head,fill=color)
    dash=' stroke-dasharray="7 7"' if dashed else ''
    svg.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{color}" stroke-width="{2 if dashed else 3}"{dash}/>')
    svg.append(f'<polygon points="{" ".join(f"{x},{y}" for x,y in head)}" fill="{color}"/>')
    if label: text(lx,ly,label,17,color)

text(48,30,'NovaMind AI',42,bold=True)
text(48,84,'AWS deployment architecture  /  numbered request and delivery flow',25,MUTED)
text(48,124,'React + Node.js microservices + LangGraph  •  AWS region: us-east-1',19,MUTED)

# Static delivery is separate from the configured API endpoint.
card(48,193,290,120,'User browser',['React 19 + Vite SPA','Firebase Auth SDK'],n=1)
card(460,193,330,120,'Amazon CloudFront',['HTTPS static delivery'],ico='cloudfront',n=2)
card(920,193,360,120,'Amazon S3 / frontend',['novamind-frontend-prod','Compiled HTML, JS, CSS'],ico='s3')
arrow([(338,250),(460,250)],'load SPA',354,219)
arrow([(790,250),(920,250)],'origin fetch',804,219)
card(1390,193,360,120,'Firebase / Google',['Browser sign-in; Auth service','verifies Firebase ID tokens'])
arrow([(190,193),(190,169),(1570,169),(1570,193)],'Google sign-in',1380,142)

# AWS network topology from the deployment runbook.
box(48,370,1232,780,'#f8fafc','#7c9a76')
icon(65,385,'vpc',38)
text(115,389,'Amazon VPC  •  novamind-vpc',23,bold=True)
text(680,393,'Subnet layout follows the deployment guide',18,MUTED)
box(70,438,1188,145,'#f3f8ef','#a9c39b')
text(87,449,'PUBLIC SUBNETS',16,'#466638',True)
card(95,481,400,82,'Application Load Balancer',['API entry → Gateway :8000'],ico='alb',n=3)
card(910,481,325,82,'NAT Gateway',['Outbound internet access'],ico='nat')
arrow([(190,313),(190,350),(560,350),(560,522),(495,522)],'API + session cookie',305,325)

box(70,607,1188,519,'#f6f9ff','#9bb5d3')
text(87,622,'PRIVATE SUBNETS  /  ECS CLUSTER: novamind-cluster  /  AWS Fargate',18,BLUE,True)
card(95,677,295,117,'Express Gateway :8000',['Redis session validation','Proxy + x-user-id'],ico='fargate',n=4)
arrow([(290,563),(290,594),(80,594),(80,652),(240,652),(240,677)])
for x,title,port,lines in [
    (460,'Auth',8001,['Login, credits, admin']),
    (720,'Chat',8002,['History + messages']),
    (980,'Billing',8004,['Orders + verification'])]:
    card(x,677,245,117,f'{title} :{port}',lines,ico='fargate')
arrow([(390,725),(424,725),(424,661),(1098,661),(1098,677)])
arrow([(579,661),(579,677)])
arrow([(839,661),(839,677)])
text(470,804,'Internal HTTP via Cloud Map DNS: novamind.local',17,MUTED)
icon(1194,805,'cloudmap',28)
badge(1230,615,5)

card(95,873,295,136,'ElastiCache / Redis',['Gateway + Auth: sessions','Agent: memory + limits'],ico='redis',n=6)
arrow([(230,794),(230,873)])
card(460,855,765,230,'Agent service :8003',['LangGraph StateGraph • eight nodes inside this service'],ico='fargate',n=7)
arrow([(390,764),(424,764),(424,900),(460,900)])
arrow([(460,960),(390,960)])
text(482,945,'Router: explicit selection → PDF → image → Groq classifier',18,INK,True)
text(482,980,'chat    •    search → chat    •    coding    •    pdf    •    ppt',20)
text(482,1016,'vision (image generation)    •    pdfRag    •    imageAnalyzer',20)
text(95,1030,'Agent → Chat: save messages',17,MUTED)
text(95,1057,'Agent → Auth: deduct credits',17,MUTED)
text(482,1093,'Billing → Auth: update plan / credits after payment verification',17,MUTED)

# External systems: logical dependencies share outbound NAT.
box(1360,370,390,780,'#fafafa',BORDER)
badge(1711,355,8)
text(1380,390,'EXTERNAL SERVICES',20,bold=True)
text(1380,422,'Backend connections via NAT + internet',17,MUTED)
card(1380,472,350,116,'MongoDB Atlas',['Auth / Chat / Billing persistence','Agent also connects at startup'])
card(1380,608,350,160,'AI inference + tools',['Groq: router, chat, documents','OpenRouter / DeepSeek: coding','Gemini: images + embeddings','Tavily: search; Stability: images'])
card(1380,788,350,110,'Qdrant Cloud',['PDF chunks + vector search','Agent service RAG pipeline'])
card(1380,918,350,90,'Razorpay',['Billing orders + client checkout'])
text(1380,1030,'Auth also uses Firebase Admin.',18,MUTED)
text(1380,1060,'Providers are external services,',18,MUTED)
text(1380,1088,'not separate AWS agent tasks.',18,MUTED)
arrow([(1235,522),(1360,522)])
arrow([(1225,920),(1248,920),(1248,594),(1065,594),(1065,563)],dashed=True)

# Regional services sit outside the VPC boundary.
card(48,1200,410,141,'Amazon S3 / artifacts',['cretexainovamind','PDF, PPTX and generated images','Agent uploads; signed download URLs'],ico='s3',n=9)
arrow([(1225,1055),(1268,1055),(1268,1173),(260,1173),(260,1200)],'upload artifacts',875,1151)
card(490,1200,390,141,'Secrets Manager + IAM',['ECS startup secret injection','Execution roles: pull, secrets, logs','Agent task role: S3 access'],ico='secrets',n=10)
icon(515,1289,'iam',35)
card(912,1200,368,141,'Amazon CloudWatch',['awslogs from all five services','/ecs/novamind-*'],ico='cloudwatch',n=11)
arrow([(1100,1126),(1100,1200)],dashed=True)

box(48,1390,1702,143,'#f8fafc',BORDER)
badge(64,1375,12)
text(88,1406,'GitHub Actions  /  push to main',23,bold=True)
icon(515,1420,'ecr',52)
text(583,1409,'Amazon ECR',21,bold=True)
text(583,1440,'Build + push 5 images',18,MUTED)
text(952,1409,'ECS Fargate',21,bold=True)
text(952,1440,'Force redeploy 5 services',18,MUTED)
text(1337,1409,'Frontend delivery',21,bold=True)
text(1337,1440,'Build → S3 sync → invalidate CDN',18,MUTED)
arrow([(426,1437),(500,1437)],dashed=True)
arrow([(813,1437),(930,1437)],dashed=True)
arrow([(1190,1437),(1312,1437)],dashed=True)
text(88,1492,'Deployment lane: frontend job starts after backend deployment commands complete.',18,MUTED)

text(48,1560,'Solid arrows: requests / data dependencies     Dashed arrows: shared egress, logging or deployment',18,MUTED)
text(48,1590,'Source: application code, task-defs/*.json, deploy guide and deploy.yml. Network topology is documented, not live-verified.',17,MUTED)
text(48,1615,'Official AWS Architecture Icons • July 2026 • aws.amazon.com/architecture/icons/  |  Numbers identify stages, not a strict execution sequence.',16,MUTED)
svg.append('</svg>')
OUT.mkdir(exist_ok=True)
im.save(OUT/'novamind-aws-architecture.png',optimize=True)
(OUT/'novamind-aws-architecture.svg').write_text('\n'.join(svg),encoding='utf-8')
print('Rendered numbered architecture PNG and SVG.')
