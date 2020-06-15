from django.contrib import admin
from .models import Meetings, Minutes, Resources, Events

# Register your models here.
admin.site.register(Meetings)
admin.site.register(Minutes)
admin.site.register(Resources)
admin.site.register(Events)