from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("tasks.urls")),     # homepage
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")), # REST API
]
