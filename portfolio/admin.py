from django.contrib import admin
from .models import Project, SiteMeta


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "year", "featured", "order")
    list_filter = ("category", "featured", "year")
    search_fields = ("title", "tagline")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(SiteMeta)
class SiteMetaAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
