# Generated by Django 4.1.7 on 2023-04-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='duration',
            field=models.TimeField(verbose_name='tugash vaqti'),
        ),
    ]
