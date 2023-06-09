# Generated by Django 4.2.1 on 2023-05-23 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("booktest", "0008_rename_hcontent_heroinfo_hcomment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Areas",
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
                ("atitle", models.CharField(max_length=20)),
                (
                    "aparent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="booktest.areas",
                    ),
                ),
            ],
        ),
    ]
