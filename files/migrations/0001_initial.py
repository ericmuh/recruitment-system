# Generated by Django 3.1.5 on 2021-01-19 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClearanceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('clearance_no', models.CharField(max_length=100, unique=True, verbose_name='Clearance Number')),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('clearance_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('client_count', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.FileField(blank=True, upload_to='clients/%Y/%m/%d/')),
                ('created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='ClientFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('document', models.FileField(blank=True, upload_to='clients/%Y/%m/%d/')),
                ('created', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.ImageField(blank=True, upload_to='client/%Y/%m/%d/', verbose_name='Passport Size')),
                ('full', models.ImageField(blank=True, upload_to='client/%Y/%m/%d/', verbose_name='Full Size')),
                ('others', models.ImageField(blank=True, upload_to='client/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]