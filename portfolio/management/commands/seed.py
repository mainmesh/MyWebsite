from portfolio.models import Project, SiteMeta
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed SiteMeta + featured projects."
    help = "Seed SiteMeta + AI Engineer & Full-Stack projects."

    def handle(self, *args, **kwargs):
        SiteMeta.objects.all().delete()
        SiteMeta.objects.create(
            name="Meshack Mbithi",
            headline="Full-Stack Engineer · AI Quality Specialist",
            headline="AI Engineer · Full-Stack Developer",
            location="Nairobi, KE · GMT+3",
            status="Open to contract & full-time remote roles",
            status="Open to AI Engineering & Full-Stack Remote Roles",
            email="meshackmbithi01@gmail.com",
            phone="0794913356",
            bio_short=(
                "Full-stack engineer building production web apps — and the "
                "human feedback loops that make AI systems worth trusting."
                "AI Engineer specializing in LLM evaluation frameworks, AI agent architectures, "
                "and production full-stack web applications."
            ),
        )

        Project.objects.all().delete()

        # Project 1: AI Evaluation Engine
        Project.objects.create(
            slug="llm-eval-benchmark",
            title="LLM Evaluation & Benchmarking Suite",
            tagline="Automated feedback loops and evaluation pipeline for AI model reasoning & code synthesis.",
            problem=(
                "Generative AI models require continuous benchmarking against complex prompt criteria, "
                "factual verification rules, and safety metrics before deployment into production workflows."
            ),
            features=[
                "Automated reasoning & code synthesis evaluation harness",
                "Human-in-the-loop annotation and RLHF feedback scoring",
                "Factual consistency and instruction-following metrics",
                "Custom evaluation dashboards for model quality tracking",
            ],
            metrics=[
                {"value": 98, "suffix": "%", "label": "Eval accuracy"},
                {"value": 15, "suffix": "k+", "label": "Prompts benchmarked"},
                {"value": 40, "suffix": "%", "label": "Faster error triage"},
            ],
            stack="Python · LLM Eval · PyTorch · RAG · JSON",
            role="Lead AI Engineer",
            year=2025,
            github_url="https://github.com/",
            category=Project.CATEGORY_AI,
            featured=True,
            order=1,
        )

        # Project 2: RAG AI Agent Architecture
        Project.objects.create(
            slug="autonomous-rag-agent",
            title="Autonomous RAG & AI Agent Pipeline",
            tagline="Enterprise knowledge retrieval agent with dynamic vector search and structured reasoning.",
            problem=(
                "Domain-specific enterprise knowledge is locked in unstructured documentation, requiring "
                "high-accuracy vector retrieval and multi-step reasoning agents that prevent hallucinations."
            ),
            features=[
                "Multi-stage RAG document chunking and vector embeddings",
                "LangChain & Python agent tools for live document queries",
                "FastAPI REST endpoints with semantic similarity scoring",
                "Hallucination detection and confidence thresholding",
            ],
            metrics=[
                {"value": 94, "suffix": "%", "label": "Retrieval precision"},
                {"value": 120, "suffix": "ms", "label": "Mean search latency"},
                {"value": 10, "suffix": "k", "label": "Docs indexed"},
            ],
            stack="Python · LangChain · Vector DB · FastAPI · RAG",
            role="AI Systems Developer",
            year=2025,
            github_url="https://github.com/",
            category=Project.CATEGORY_AI,
            featured=True,
            order=2,
        )

        # Project 3: Kimeta Capital Full-Stack Platform
        Project.objects.create(
            slug="kimeta-capital",
            title="Kimeta Capital",
            tagline="A database-driven investment platform for a real-world financial workflow.",
            tagline="Database-driven investment platform with role-based access and realtime dashboards.",
            problem=(
                "Informal investment groups in Kenya track contributions, returns, and "
                "member equity using WhatsApp threads and spreadsheets. The result: "
                "disputes, lost records, zero transparency."
                "member equity manually, causing disputes and lack of transparency."
            ),
            features=[
                "Auth + role-based access (admin / investor / member)",
                "Role-based authentication (admin / investor / member)",
                "Transaction engine: deposits, withdrawals, dividends",
                "Live dashboard showing portfolio value per user",
                "Live HTMX dashboard showing portfolio value per user",
                "Admin panel for KYC, approvals, and audit log",
                "HTMX-powered partial updates — no full page reloads",
            ],
            metrics=[
                {"value": 3, "suffix": "", "label": "Roles of access"},
                {"value": 3, "suffix": "", "label": "Access roles"},
                {"value": 12, "suffix": "", "label": "Core models"},
                {"value": 0, "suffix": "ms", "label": "Reload flash"},
                {"value": 0, "suffix": "ms", "label": "Page reload flash"},
            ],
            stack="Django · PostgreSQL · HTMX",
            role="Solo full-stack build",
            stack="Django · PostgreSQL · HTMX · Alpine.js",
            role="Full-Stack Developer",
            year=2025,
            github_url="https://github.com/",
            category=Project.CATEGORY_FULLSTACK,
            featured=True,
            order=1,
            order=3,
        )

        self.stdout.write(self.style.SUCCESS(
            f"Seeded: 1 SiteMeta, {Project.objects.count()} Project(s)"
        ))
