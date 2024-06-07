# Generated by Django 5.0.6 on 2024-06-05 23:35

import certificates.validations
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Certificate",
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
                ("name", models.CharField(max_length=100)),
                ("issued_by", models.CharField(max_length=100)),
                ("issue_date", models.DateField()),
                (
                    "expiry_date",
                    models.DateField(
                        blank=True,
                        null=True,
                        validators=[certificates.validations.validate_expiry_date],
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
