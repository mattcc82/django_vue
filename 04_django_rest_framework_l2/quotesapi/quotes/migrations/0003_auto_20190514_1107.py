# Generated by Django 2.2.1 on 2019-05-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20190510_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='context',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='source',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
