from django.contrib import admin
from .models import Meeting, Minutes, Resources, Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Minutes)
admin.site.register(Resources)
admin.site.register(Event)