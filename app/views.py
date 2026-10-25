from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("task-list")
    return render(request, "app/task_list.html", {"tasks": tasks, "form": form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("task-list")
    return render(
        request,
        "app/task_form.html",
        {"form": form, "task": task},
    )


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("task-list")
    return render(request, "app/task_confirm_delete.html", {"task": task})
