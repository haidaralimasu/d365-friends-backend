# Generated by Django 5.1.1 on 2024-09-28 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField()),
                ("thumbnail", models.ImageField(upload_to="photos/")),
                ("excerpt", models.CharField(max_length=150)),
                ("content", models.TextField()),
                ("featured", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "updated_at",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
            ],
        ),
    ]
