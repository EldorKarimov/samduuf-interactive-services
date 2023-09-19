# Generated by Django 4.2.3 on 2023-09-19 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_answer_message_alter_appeal_message_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appeal',
            name='type_application_en',
            field=models.CharField(choices=[(None, 'Tanlang'), ('tk', 'taklif'), ('shk', 'shikoyat'), ('apl', 'apellatsiya')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='appeal',
            name='type_application_ru',
            field=models.CharField(choices=[(None, 'Tanlang'), ('tk', 'taklif'), ('shk', 'shikoyat'), ('apl', 'apellatsiya')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='appeal',
            name='type_application_uz',
            field=models.CharField(choices=[(None, 'Tanlang'), ('tk', 'taklif'), ('shk', 'shikoyat'), ('apl', 'apellatsiya')], max_length=15, null=True),
        ),
    ]
