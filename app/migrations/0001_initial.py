from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="título")),
                ("completed", models.BooleanField(default=False, verbose_name="completada")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name="fecha de creación",
                    ),
                ),
            ],
            options={
                "verbose_name": "tarea",
                "verbose_name_plural": "tareas",
                "ordering": ["completed", "-created_at"],
            },
        ),
    ]
