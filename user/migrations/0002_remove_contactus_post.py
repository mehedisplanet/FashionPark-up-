# Generated by Django 5.0.1 on 2024-01-26 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='post',
        ),
    ]
