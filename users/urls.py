"""Defines urls patterns for the users application."""

from django.urls import path, include

from . import views

app_name = "users"
urlpatterns = [
    # Default addresses.
    path("", include("django.contrib.auth.urls")),
    # Sign up website.
    path("register/", views.register, name="register"),
]
