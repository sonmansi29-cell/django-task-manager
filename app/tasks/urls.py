from django.urls import path
from .views import TaskList, TaskDetail, home

urlpatterns = [
    path("", home, name="home"),                # frontend
    path("api/tasks/", TaskList.as_view()),
    path("api/tasks/<int:pk>/", TaskDetail.as_view()),
]
