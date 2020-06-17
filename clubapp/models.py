from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Meetings(models.Model):
    meeting_owner = models.ManyToManyField(User)
    meeting_title = models.CharField(max_length = 255)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_location = models.CharField(max_length = 255)
    meeting_agenda = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.meeting_title
    
    class Meta:
        db_table = 'meetings'
        verbose_name_plural = 'meetings'


class Minutes(models.Model):
    meeting_id = models.ForeignKey(Meetings, on_delete = models.DO_NOTHING)
    attendance = models.ManyToManyField(User)
    minutes = models.TextField()

    def __str__(self):
        return self.minutes
    
    class Meta:
        db_table = 'minutes'
        verbose_name_plural = 'minutes'

class Resources(models.Model):
    resource_name = models.CharField(max_length = 255)
    resource_type = models.CharField(max_length = 255)
    resource_url = models.URLField()
    date_entered = models.DateTimeField(auto_now_add = True)
    resource_user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    resource_description = models.CharField(max_length = 255)

    def __str__(self):
        return self.resource_name
    
    class Meta:
        db_table = 'resources'
        verbose_name_plural = 'resources'

class Events(models.Model):
    event_title = models.CharField(max_length = 255)
    event_location = models.CharField(max_length = 255)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_description = models.TextField()
    event_user = models.ForeignKey(User, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.event_title
    
    class Meta:
        db_table = 'events'
        verbose_name_plural = 'events'


