from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('user/register', views.register),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('dashboard', views.dashboard),
    path('workout', views.new_workout),
    path('workout/<int:id>', views.workout),
    path('workout/<int:id>/exercise', views.exercise),
    path('workout/<int:id>/complete', views.complete_workout),
    path('workout/<int:id>/edit', views.edit_workout),
    path('workout/<int:id>/delete', views.delete_workout),
    path('workouts', views.all_workouts),
    path('legal/tos', views.tos),
]
