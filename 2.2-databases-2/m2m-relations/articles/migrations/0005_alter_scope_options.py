# Generated by Django 4.1.7 on 2023-02-27 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_options_alter_scope_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['is_main']},
        ),
    ]
