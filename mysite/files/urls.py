from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="file-home"),
    path("upload/", views.upload, name="file-upload"),
]
