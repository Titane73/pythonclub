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
    path('meetingDetail/<int:id>', views.meetingDetail, name='details')
]