# Generated by Django 4.1.2 on 2022-10-20 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commet',
            new_name='Comment',
        ),
    ]
