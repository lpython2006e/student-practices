# Generated by Django 3.1 on 2020-08-23 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('student', '0002_remove_students_sid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]