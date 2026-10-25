from django.test import TestCase
from django.urls import reverse

from .models import Task


class TaskModelTests(TestCase):
    def test_create_task(self):
        task = Task.objects.create(title="Preparar proyecto")

        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(task.title, "Preparar proyecto")
        self.assertFalse(task.completed)


class TaskViewTests(TestCase):
    def test_task_list_returns_success(self):
        response = self.client.get(reverse("task-list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/task_list.html")

    def test_task_list_creates_task(self):
        response = self.client.post(
            reverse("task-list"),
            {"title": "Ejecutar pruebas", "completed": ""},
        )

        self.assertRedirects(response, reverse("task-list"))
        self.assertTrue(Task.objects.filter(title="Ejecutar pruebas").exists())
