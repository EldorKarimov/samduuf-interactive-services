# Generated by Django 4.2.3 on 2023-08-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_answer_message_en_remove_answer_message_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='is_viewed',
            field=models.BooleanField(default=False),
        ),
    ]