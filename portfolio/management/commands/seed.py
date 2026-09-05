from portfolio.models import Project, SiteMeta
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed SiteMeta + featured projects."

    def handle(self, *args, **kwargs):
        SiteMeta.objects.all().delete()
        SiteMeta.objects.create(
            name="Meshack Mbithi",
            headline="Full-Stack Engineer · AI Quality Specialist",
            location="Nairobi, KE · GMT+3",
            status="Open to contract & full-time remote roles",
            email="meshackmbithi01@gmail.com",
            phone="0794913356",
            bio_short=(
                "Full-stack engineer building production web apps — and the "
                "human feedback loops that make AI systems worth trusting."
            ),
        )

        Project.objects.all().delete()

        Project.objects.create(
            slug="kimeta-capital",
            title="Kimeta Capital",
            tagline="A database-driven investment platform for a real-world financial workflow.",
            problem=(
                "Informal investment groups in Kenya track contributions, returns, and "
                "member equity using WhatsApp threads and spreadsheets. The result: "
                "disputes, lost records, zero transparency."
            ),
            features=[
                "Auth + role-based access (admin / investor / member)",
                "Transaction engine: deposits, withdrawals, dividends",
                "Live dashboard showing portfolio value per user",
                "Admin panel for KYC, approvals, and audit log",
                "HTMX-powered partial updates — no full page reloads",
            ],
            metrics=[
                {"value": 3, "suffix": "", "label": "Roles of access"},
                {"value": 12, "suffix": "", "label": "Core models"},
                {"value": 0, "suffix": "ms", "label": "Reload flash"},
            ],
            stack="Django · PostgreSQL · HTMX",
            role="Solo full-stack build",
            year=2025,
            github_url="https://github.com/",
            category=Project.CATEGORY_FULLSTACK,
            featured=True,
            order=1,
        )

        self.stdout.write(self.style.SUCCESS(
            f"Seeded: 1 SiteMeta, {Project.objects.count()} Project(s)"
        ))
