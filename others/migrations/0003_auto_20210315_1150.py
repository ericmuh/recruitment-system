# Generated by Django 3.1.5 on 2021-03-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('others', '0002_auto_20210121_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(choices=[('Baby Sitting', 'Baby Sitting'), ('Children Care', 'Children Care'), ('Disable Care', 'Disable Care'), ('Cleaning', 'Cleaning'), ('Washing', 'Washing'), ('Ironing', 'Ironing'), ('Arabic Cooking', 'Arabic Cooking'), ('Cooking Capacity', 'Cooking Capacity'), ('Dusting', 'Dusting')], max_length=200),
        ),
    ]