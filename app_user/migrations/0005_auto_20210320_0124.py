# Generated by Django 3.1.6 on 2021-03-20 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0004_contactmessage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmessage',
            old_name='note',
            new_name='phone',
        ),
    ]
