# Generated by Django 3.1.4 on 2021-02-23 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('function', '0005_auto_20210223_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='age',
        ),
    ]
