# Generated by Django 4.1.7 on 2023-03-15 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='photo_url',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]