# Generated by Django 4.2.3 on 2023-07-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='district',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='eduForm',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='eduLang',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='eduType',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='full_name',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='occommodation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='paymentForm',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='specialty',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentStatus',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id_number',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='third_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
