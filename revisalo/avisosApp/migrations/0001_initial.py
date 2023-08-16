# Generated by Django 4.2.3 on 2023-08-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Aviso",
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
                ("asunto", models.CharField(max_length=50)),
                ("mensaje", models.CharField(max_length=500)),
            ],
        ),
    ]
