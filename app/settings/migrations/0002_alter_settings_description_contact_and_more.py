# Generated by Django 4.2 on 2025-01-30 12:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="description_contact",
            field=ckeditor.fields.RichTextField(verbose_name="Описание контакта"),
        ),
        migrations.AlterField(
            model_name="settings",
            name="description_cool",
            field=ckeditor.fields.RichTextField(verbose_name="Описание cool"),
        ),
    ]
