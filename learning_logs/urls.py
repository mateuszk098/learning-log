"""Defines url adress patterns for the learning_logs."""

from django.urls import path

from . import views

app_name = "learning_logs"
urlpatterns = [
    # Main website.
    path("", views.index, name="index"),
    # Display all topis.
    path("topis/", views.topics, name="topics"),
    # Detail view of the individual topic.
    path("topic/(<int:topic_id>)", views.topic, name="topic")
]
