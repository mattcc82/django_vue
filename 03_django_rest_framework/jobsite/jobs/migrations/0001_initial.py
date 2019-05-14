# Generated by Django 2.2.1 on 2019-05-10 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('company_email', models.EmailField(max_length=60, unique=True)),
                ('job_title', models.CharField(max_length=120)),
                ('job_description', models.TextField(blank=True)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=60)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]