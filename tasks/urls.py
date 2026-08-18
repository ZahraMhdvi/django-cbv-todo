from django.urls import path

from .views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDoneView,
    TaskListView,
    TaskUpdateView,
)


app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/edit/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/done/", TaskDoneView.as_view(), name="task-done"),
]