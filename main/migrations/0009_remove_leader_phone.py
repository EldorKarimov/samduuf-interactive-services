# Generated by Django 4.2.3 on 2023-08-09 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_leader_options_alter_leader_position_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leader',
            name='phone',
        ),
    ]