from django.urls import path
from . import views

urlpatterns = [
    # default index page
    path('', views.index, name='index'),
    # reference to getResources method in views.py
    path('getResources/', views.getResources, name='resources')

]