# Generated by Django 4.1.7 on 2023-03-28 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_advertisement_is_favourite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='is_favourite',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
