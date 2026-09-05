from django.db import models


class Project(models.Model):
    CATEGORY_FULLSTACK = "fullstack"
    CATEGORY_AI = "ai"
    CATEGORY_WRITING = "writing"
    CATEGORY_CHOICES = [
        (CATEGORY_FULLSTACK, "Full-Stack"),
        (CATEGORY_AI, "AI"),
        (CATEGORY_WRITING, "Writing"),
    ]

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    tagline = models.CharField(max_length=200)
    problem = models.TextField()
    features = models.JSONField(default=list)
    metrics = models.JSONField(default=list)
    stack = models.CharField(max_length=200)
    role = models.CharField(max_length=80)
    year = models.PositiveIntegerField()
    screenshot = models.ImageField(upload_to="projects/", blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=CATEGORY_FULLSTACK)
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-year"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("case_study_detail", args=[self.slug])


class SiteMeta(models.Model):
    """Singleton row for global site configuration."""
    name = models.CharField(max_length=80, default="Meshack Mbithi")
    headline = models.CharField(max_length=200, default="Full-Stack Engineer · AI Quality Specialist")
    location = models.CharField(max_length=80, default="Nairobi, KE · GMT+3")
    status = models.CharField(max_length=200, default="Open to contract & full-time remote roles")
    email = models.EmailField(default="meshackmbithi01@gmail.com")
    phone = models.CharField(max_length=40, default="0794913356")
    bio_short = models.TextField(blank=True)
    cv = models.FileField(upload_to="cv/", blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    whatsapp_url = models.URLField(blank=True)
    skills = models.JSONField(default=list, blank=True)

    class Meta:
        verbose_name = "Site Meta"

    def __str__(self):
        return f"SiteMeta({self.name})"
