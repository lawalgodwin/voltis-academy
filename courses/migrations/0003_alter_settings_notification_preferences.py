# Generated by Django 5.2 on 2025-04-27 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='notification_preferences',
            field=models.JSONField(default=dict),
        ),
    ]
