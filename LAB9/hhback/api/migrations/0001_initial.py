# Generated by Django 2.1.5 on 2021-04-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('address', models.TextField(default=False, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('salary', models.FloatField(verbose_name='Salary')),
            ],
        ),
    ]
