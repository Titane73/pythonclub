# Generated by Django 3.0.5 on 2020-05-13 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_title', models.CharField(max_length=255)),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.TimeField()),
                ('meeting_location', models.CharField(max_length=255)),
                ('meeting_agenda', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'meetings',
                'db_table': 'meeting',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=255)),
                ('resource_type', models.CharField(max_length=255)),
                ('resource_url', models.URLField()),
                ('date_entered', models.DateTimeField(auto_now_add=True)),
                ('resource_description', models.CharField(max_length=255)),
                ('resource_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'resources',
                'db_table': 'resource',
            },
        ),
        migrations.CreateModel(
            name='Minutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.TextField()),
                ('attendance', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('meeting_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clubapp.Meeting')),
            ],
            options={
                'verbose_name_plural': 'minutes',
                'db_table': 'minutes',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=255)),
                ('event_location', models.CharField(max_length=255)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_description', models.TextField()),
                ('event_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
                'db_table': 'event',
            },
        ),
    ]
