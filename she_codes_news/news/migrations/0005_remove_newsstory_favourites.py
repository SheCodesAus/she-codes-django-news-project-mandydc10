# Generated by Django 4.1.3 on 2022-12-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsstory_favourites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsstory',
            name='favourites',
        ),
    ]
