# Generated by Django 4.2.1 on 2023-05-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booktest", "0002_heroinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookinfo",
            name="bcomment",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="bookinfo", name="bread", field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="bookinfo",
            name="is_delete",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="heroinfo",
            name="is_delete",
            field=models.BooleanField(default=False),
        ),
    ]