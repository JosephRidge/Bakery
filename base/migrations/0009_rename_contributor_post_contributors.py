# Generated by Django 5.2.1 on 2025-05-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_post_contributor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='contributor',
            new_name='contributors',
        ),
    ]
