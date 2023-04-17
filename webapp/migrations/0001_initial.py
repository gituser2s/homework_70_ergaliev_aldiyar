# Generated by Django 3.2 on 2023-04-17 15:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import webapp.models.tasks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Начало')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Конец')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Тип')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='Слишком короткое описание!'), webapp.models.tasks.CustomDescriptionValidator()], verbose_name='Описание')),
                ('detailed_description', models.TextField(blank=True, max_length=2000, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=5, message='Необходимо ввести больше 5 символов!'), webapp.models.tasks.CustomDetailedValidator()], verbose_name='Детально')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время и дата обновления')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Время и дата удаления')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='webapp.project', verbose_name='Проект')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.status')),
                ('type', models.ManyToManyField(to='webapp.Type')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задание',
            },
        ),
    ]
