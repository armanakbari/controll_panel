# Generated by Django 3.1.7 on 2021-02-28 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210228_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='document',
            field=models.FileField(default='No file', upload_to='files'),
        ),
    ]