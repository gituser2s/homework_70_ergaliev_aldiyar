from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание",
        null=False,
        blank=False
    )
    start_date = models.DateField(
        verbose_name="Начало",
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name="Конец",
        null=True,
        blank=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False,
    )

    def __str__(self):
        return self.title
