# Generated by Django 4.2.3 on 2023-08-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_appeal_is_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='is_viewed',
            field=models.BooleanField(default=False),
        ),
    ]
