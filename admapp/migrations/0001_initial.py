# Generated by Django 3.0 on 2020-01-10 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('facid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=20)),
                ('mobile', models.IntegerField(blank=True, max_length=10, null=True)),
                ('batchincharge', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('stid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('admissionno', models.IntegerField(blank=True, null=True)),
                ('admissiondate', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('guardian', models.CharField(blank=True, max_length=20, null=True)),
                ('batch', models.CharField(blank=True, max_length=10, null=True)),
                ('mobile', models.IntegerField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]