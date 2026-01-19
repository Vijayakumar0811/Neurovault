from django.urls import path
from .views import analyze_login

urlpatterns = [
    path("analyze/", analyze_login),
]