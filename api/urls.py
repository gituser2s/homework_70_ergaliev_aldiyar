from django.urls import path
from api.views import TasksView, TaskDetailView, TaskUpdateView, TaskDeleteView, ProjectsView, ProjectDetailView, ProjectUpdateView, ProjectDeleteView


urlpatterns = [
    path("tasks/", TasksView.as_view()),
    path("tasks/<int:pk>", TaskDetailView.as_view()),
    path("tasks/update/<int:pk>", TaskUpdateView.as_view()),
    path("tasks/delete/<int:pk>", TaskDeleteView.as_view()),
    path("projects/", ProjectsView.as_view()),
    path("projects/<int:pk>", ProjectDetailView.as_view()),
    path("projects/update/<int:pk>", ProjectUpdateView.as_view()),
    path("projects/delete/<int:pk>", ProjectDeleteView.as_view()),
]