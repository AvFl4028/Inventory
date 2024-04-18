from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("reactpy/", include("reactpy_django.http.urls")),
]
