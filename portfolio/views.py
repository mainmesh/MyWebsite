from django.http import FileResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db import ProgrammingError
from .models import Project, SiteMeta


def _meta():
    try:
        return SiteMeta.objects.first()
    except ProgrammingError:
        return None


def _projects():
    try:
        return list(Project.objects.filter(featured=True))
    except ProgrammingError:
        return []


def home(request):
    meta = _meta()
    projects = _projects()
    return render(request, "portfolio/home.html", {
        "meta": meta,
        "projects": projects,
    })


def case_study_detail(request, slug):
    try:
        project = Project.objects.get(slug=slug)
    except (Project.DoesNotExist, ProgrammingError):
        from django.http import Http404
        raise Http404("Project not found")
    return render(request, "portfolio/case_study.html", {
        "meta": _meta(),
        "project": project,
    })


def cv_download(request):
    meta = _meta()
    if not meta or not meta.cv:
        raise Http404("CV not available")
    file_path = meta.cv.path
    filename = meta.cv.name.split("/")[-1]
    response = FileResponse(open(file_path, "rb"), as_attachment=True, filename=filename)
    if filename.lower().endswith(".docx"):
        response["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    return response


def cv_page(request):
    return render(request, "portfolio/cv.html", {"meta": _meta()})
