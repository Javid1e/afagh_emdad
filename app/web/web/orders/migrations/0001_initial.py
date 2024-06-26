# Generated by Django 5.0.6 on 2024-06-05 23:35

import orders.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
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
                    "service_type",
                    models.CharField(
                        max_length=100,
                        validators=[orders.validations.validate_service_type],
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("completed", "Completed"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=20,
                        validators=[orders.validations.validate_status],
                    ),
                ),
                ("request_time", models.DateTimeField()),
                ("completion_time", models.DateTimeField(blank=True, null=True)),
                ("location", models.CharField(max_length=255)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
