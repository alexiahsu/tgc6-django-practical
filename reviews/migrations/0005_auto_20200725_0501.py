# Generated by Django 2.2.6 on 2020-07-25 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20200725_0449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='commentor',
            new_name='user',
        ),
    ]