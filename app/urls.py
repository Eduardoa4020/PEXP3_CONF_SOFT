from django.urls import path

from . import views


urlpatterns = [
    path("", views.task_list, name="task-list"),
    path("tasks/<int:pk>/edit/", views.task_update, name="task-update"),
    path("tasks/<int:pk>/delete/", views.task_delete, name="task-delete"),
]
