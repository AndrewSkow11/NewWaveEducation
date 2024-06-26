# Generated by Django 5.0.6 on 2024-06-12 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Section",
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
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="заголовок"),
                ),
            ],
            options={
                "verbose_name": "раздел",
                "verbose_name_plural": "разделы",
            },
        ),
        migrations.CreateModel(
            name="Material",
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
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="название"),
                ),
                (
                    "text_content",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="текстовая часть материала",
                    ),
                ),
                (
                    "file_content",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="file_marerial",
                        verbose_name="файл материла",
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        blank=True, null=True, verbose_name="ссылка на видео"
                    ),
                ),
                (
                    "section",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="material",
                        to="courses.section",
                        verbose_name="учебный материал",
                    ),
                ),
            ],
            options={
                "verbose_name": "материал",
                "verbose_name_plural": "материлы",
            },
        ),
    ]
