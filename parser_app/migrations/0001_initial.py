# Generated by Django 5.1.6 on 2025-05-27 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharterRecord',
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
