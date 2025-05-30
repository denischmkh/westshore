# Generated by Django 5.1.6 on 2025-05-27 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parser_app', '0003_delete_charterrecordbraemaroffshore_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharterRecordBraemaroffshore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('vessel', models.CharField(max_length=255)),
                ('charterer', models.CharField(max_length=255)),
                ('scope_of_work', models.TextField()),
                ('asset', models.CharField(max_length=255)),
                ('period', models.CharField(max_length=255)),
                ('onhire', models.CharField(max_length=255)),
                ('rate', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharterRecordHowerobinsonoffshore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('vessel', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('charterer', models.CharField(max_length=255)),
                ('scope_of_work', models.TextField()),
                ('period', models.CharField(max_length=255)),
                ('commencement', models.CharField(max_length=255)),
                ('rate', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CharterRecordWestshore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('vessel', models.CharField(max_length=255)),
                ('charterer', models.CharField(max_length=255)),
                ('scope_of_work', models.TextField()),
                ('comm', models.CharField(max_length=100)),
                ('rate', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
