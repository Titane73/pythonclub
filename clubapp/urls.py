from django.urls import path
from . import views

urlpatterns = [
    # default index page
    path('', views.index, name='index'),
    # reference to getResources method in views.py
    path('getResources/', views.getResources, name='resources'),
    #  getMeetings 
    path('getMeetings/', views.getMeetings, name='meetings'),
    #  minutes detail added to the meetings
    path('meetingDetail/<int:id>', views.meetingDetail, name='meeting_details'),
    # events page, with info link
    path('getEventss/', views.getEventss, name = 'events'), 
    # event info linked to event title
    path('getEventsInfo/<int:id>', views.getEventsInfo, name='event_info')
]