# Generated by Django 4.2.3 on 2023-08-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_appeal_is_viewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
    ]