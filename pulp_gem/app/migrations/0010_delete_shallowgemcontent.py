# Generated by Django 4.2.4 on 2023-09-12 10:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("gem", "0009_check_datarepair"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ShallowGemContent",
        ),
    ]