# Generated by Django 2.2.6 on 2020-07-22 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20200722_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='books.Author'),
        ),
    ]
