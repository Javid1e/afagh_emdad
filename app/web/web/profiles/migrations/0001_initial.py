# Generated by Django 5.0.6 on 2024-06-05 23:35

import profiles.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                    "personal_information",
                    models.JSONField(
                        validators=[profiles.validations.validate_personal_information]
                    ),
                ),
                (
                    "car_information",
                    models.JSONField(
                        validators=[profiles.validations.validate_car_information]
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
