# Generated by Django 3.2.13 on 2022-06-28 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_alter_bugreport_occured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugreport',
            name='bug_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='bugreport',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
