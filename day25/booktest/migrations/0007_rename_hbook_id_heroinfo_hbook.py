# Generated by Django 4.2.1 on 2023-05-21 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("booktest", "0006_alter_bookinfo_bprice"),
    ]

    operations = [
        migrations.RenameField(
            model_name="heroinfo", old_name="hbook_id", new_name="hbook",
        ),
    ]
