# Generated by Django 4.2.1 on 2023-07-25 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='can_activate',
        ),
    ]
