# Generated by Django 3.0 on 2020-01-13 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admapp', '0003_auto_20200113_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='guardian',
        ),
    ]