from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

def home(request):
    return render(request, "tasks/index.html")

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
