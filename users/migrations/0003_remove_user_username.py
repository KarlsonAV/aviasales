# Generated by Django 3.2.7 on 2021-09-01 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
