# Generated by Django 5.1.3 on 2024-11-18 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0003_address_zip"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="last_updated",
            new_name="last_update",
        ),
    ]