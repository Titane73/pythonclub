# Generated by Django 3.0.5 on 2020-06-12 21:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clubapp', '0004_auto_20200611_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='meeting_owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
