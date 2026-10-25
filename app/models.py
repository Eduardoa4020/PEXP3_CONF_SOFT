from django.db import models


class Task(models.Model):
    title = models.CharField("título", max_length=200)
    completed = models.BooleanField("completada", default=False)
    created_at = models.DateTimeField("fecha de creación", auto_now_add=True)

    class Meta:
        ordering = ["completed", "-created_at"]
        verbose_name = "tarea"
        verbose_name_plural = "tareas"

    def __str__(self):
        return self.title
