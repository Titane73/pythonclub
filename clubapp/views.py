from django.shortcuts import render, get_object_or_404
from .models import Meetings, Minutes, Resources, Events
from .forms import AddMeetingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'clubapp/index.html')

@login_required
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

def getEvents(request):
    event_list = Events.objects.all()
    context={'event_list' : event_list}
    return render(request, 'clubapp/events.html', context=context)

def getEventsInfo(request, id):
    event_info = Events.objects.get(pk=id)
    context = {'event_info' : event_info}
    return render(request, 'clubapp/event_info.html', context=context)

@login_required
def addMeeting(request):
     form = AddMeetingForm
     if request.method == 'POST':
          form = AddMeetingForm(request.POST)
          if form.is_valid():
               post = form.save(commit=True)
               post.save()
               form = AddMeetingForm()
     else:
          form = AddMeetingForm()
     return render(request, 'clubapp/add_meeting.html', {'form': form})

def loginMsg(request):
    return render(request, 'clubapp/login_msg.html')

def logoutMsg(request):
    return render(request, 'clubapp/logout_msg.html')