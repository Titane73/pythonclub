from django.shortcuts import render, get_object_or_404
from .models import Meetings, Minutes, Resources, Events

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resources_list = Resources.objects.all()
    context={'resources_list' : resources_list}
    return render(request, 'clubapp/resources.html', context=context)

def getMeetings(request):
    meeting_list = Meetings.objects.all()
    context={'meeting_list' : meeting_list}
    return render(request, 'clubapp/meetings.html', context=context)

def meetingDetail(request, id):
    meeting_details = Meetings.objects.get(pk=id)
    context = {'meeting_details' : meeting_details}
    return render(request, 'clubapp/meeting_details.html', context=context)

def getEventss(request):
    event_list = Events.objects.all()
    context={'event_list' : event_list}
    return render(request, 'clubapp/events.html', context=context)

def getEventsInfo(request, id):
    event_info = Events.objects.get(pk=id)
    context = {'event_info' : event_info}
    return render(request, 'clubapp/event_info.html', context=context)

