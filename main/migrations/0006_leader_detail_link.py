# Generated by Django 4.2.3 on 2023-08-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_appeal_is_checked_alter_appeal_type_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='detail_link',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
