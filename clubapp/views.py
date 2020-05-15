from django.shortcuts import render
from .models import Meeting, Minutes, Resources, Event

# Create your views here.
def index(request):
    return render(request, 'clubapp/index.html')

def getResources(request):
    resources_list = Resources.objects.all()
    context={'resources_list' : resources_list}
    return render(request, 'clubapp/resources.html', context=context)
