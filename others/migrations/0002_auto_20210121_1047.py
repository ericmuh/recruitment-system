# Generated by Django 3.1.5 on 2021-01-21 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210119_1120'),
        ('others', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextofkin',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.client'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(choices=[('Baby Sitting | يجلس الطفل', 'Baby Sitting'), ('Children Care | رعاية الأطفال', 'Children Care'), ('Disable Care | تعطيل الرعاية', 'Disable Care'), ('Cleaning | تنظيف', 'Cleaning'), ('Washing | غسل', 'Washing'), ('Ironing | كى الملابس', 'Ironing'), ('Arabic Cooking | الطبخ العربي', 'Arabic Cooking'), ('Cooking Capacity | قدرة الطبخ', 'Cooking Capacity'), ('Dusting | تنفيض الأتربة', 'Dusting')], max_length=200),
        ),
    ]
