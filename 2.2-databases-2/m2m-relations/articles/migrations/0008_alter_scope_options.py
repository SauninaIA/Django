# Generated by Django 4.1.7 on 2023-02-27 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_scope_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['-is_main']},
        ),
    ]
