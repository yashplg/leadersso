# Generated by Django 5.0.7 on 2024-07-25 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_authenticator_static", "0009_throttling"),
    ]

    operations = [
        migrations.AddField(
            model_name="staticdevice",
            name="created",
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(1, 1, 1, 0, 0)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="staticdevice",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="staticdevice",
            name="last_used",
            field=models.DateTimeField(null=True),
        ),
    ]
