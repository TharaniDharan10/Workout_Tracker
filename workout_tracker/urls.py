"""workout_tracker URL Configuration

Points our project to our workout application.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.workout.urls")),
]

