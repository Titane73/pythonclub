from django.shortcuts import render, get_object_or_404
from .models import Meetings, Minutes, Resources, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resources_list = Resources.objects.all()
    context={'resources_list' : resources_list}
    return render(request, 'clubapp/resources.html', context=context)

def getMeetings(request):
    meetings_list = Meetings.objects.all()
    context={'meetings_list' : meetings_list}
    return render(request, 'clubapp/meetings.html', context=context)

def meetingDetail(request, id):
    details = Meetings.objects.get(pk=id)
    context = {'details' : details}
    return render(request, 'clubapp/details.html', context=context)

