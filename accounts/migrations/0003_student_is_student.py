# Generated by Django 4.2.3 on 2023-08-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_student_birth_date_student_country_student_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_student',
            field=models.BooleanField(default=True),
        ),
    ]