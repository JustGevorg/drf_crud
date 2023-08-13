from django.urls import path, include
from rest_framework import routers
from facilities_area.views import MasterProfilesAPIView, EventAPIView, TaskModelViewSet

masters_patterns = [
    path("", MasterProfilesAPIView.as_view(), name="list_masters"),
]

events_patterns = [
    path("", EventAPIView.as_view(), name="events"),
    path("<int:pk>", EventAPIView.as_view()),
]

task_router = routers.SimpleRouter()
task_router.register(r"tasks", TaskModelViewSet)

tasks_patterns = [
    path("", include(task_router.urls)),
]
