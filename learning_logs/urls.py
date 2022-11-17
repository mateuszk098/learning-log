"""Defines url adress patterns for the learning_logs."""

from django.urls import path

from . import views

app_name = "learning_logs"
urlpatterns = [
    # Main website.
    path("", views.index, name="index"),
    # Display all topis.
    path("topic/", views.topics, name="topics"),
    # Detail view of the individual topic.
    path("topic/(<int:topic_id>)", views.topic, name="topic"),
    # Site for adding a new topic.
    path("new_topic/", views.new_topic, name="new_topic"),
    # Site for adding a new entry.
    path("new_entry/(<int:topic_id>)", views.new_entry, name="new_entry"),
    # Site for edditing the existing entry.
    path("edit_entry/(<int:entry_id>)/", views.edit_entry, name="edit_entry")
]
