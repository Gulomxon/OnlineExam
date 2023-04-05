# Generated by Django 4.1.7 on 2023-03-17 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0002_alter_school_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subject",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Test",
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
                ("level", models.IntegerField(default=1)),
                (
                    "clas",
                    models.IntegerField(
                        choices=[
                            (0, "1-sinf"),
                            (1, "2-sinf"),
                            (2, "3-sinf"),
                            (3, "4-sinf"),
                            (4, "5-sinf"),
                            (5, "6-sinf"),
                            (6, "7-sinf"),
                            (7, "8-sinf"),
                            (8, "9-sinf"),
                            (9, "10-sinf"),
                            (10, "11-sinf"),
                        ],
                        default=0,
                        verbose_name="sinf",
                    ),
                ),
                ("question", models.TextField()),
                ("correct", models.TextField()),
                ("incorrect1", models.TextField()),
                ("incorrect2", models.TextField()),
                ("incorrect3", models.TextField()),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="data.subject"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Result",
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
                ("result", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.student",
                    ),
                ),
                (
                    "subject",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="data.subject",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Exam",
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
                    "clas",
                    models.IntegerField(
                        choices=[
                            (0, "1-sinf"),
                            (1, "2-sinf"),
                            (2, "3-sinf"),
                            (3, "4-sinf"),
                            (4, "5-sinf"),
                            (5, "6-sinf"),
                            (6, "7-sinf"),
                            (7, "8-sinf"),
                            (8, "9-sinf"),
                            (9, "10-sinf"),
                            (10, "11-sinf"),
                        ],
                        verbose_name="sinf",
                    ),
                ),
                ("deadline", models.DateTimeField(verbose_name="boshlanish vaqti")),
                ("duration", models.TimeField(verbose_name="davomiylig")),
                ("level", models.IntegerField(default=1)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "subject",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="data.subject"
                    ),
                ),
            ],
        ),
    ]
