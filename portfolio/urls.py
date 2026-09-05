from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("work/<slug:slug>/", views.case_study_detail, name="case_study_detail"),
    path("cv/", views.cv_page, name="cv_page"),
    path("cv/download/", views.cv_download, name="cv_download"),
]
