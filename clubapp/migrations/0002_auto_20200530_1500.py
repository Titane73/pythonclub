# Generated by Django 3.0.5 on 2020-05-30 22:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resource',
            new_name='Resources',
        ),
        migrations.AlterModelTable(
            name='resources',
            table='resources',
        ),
    ]
