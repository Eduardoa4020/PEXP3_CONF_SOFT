from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "completed"]
        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "Escribe una tarea", "required": True}
            ),
        }
