# Generated by Django 3.0 on 2020-01-14 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admapp', '0005_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
