# Generated by Django 3.1.7 on 2021-02-24 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamrin',
            name='deadline_tamrin',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]