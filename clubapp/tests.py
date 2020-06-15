from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Meetings, Minutes, Resources, Events

# Test for models
class MeetingsTest(TestCase):
    def test_string(self):
        type=Meetings(meeting_title='Townhall')
        self.assertEqual(str(type),type.meeting_title)

    def test_table(self):
        self.assertEqual(str(Meetings._meta.db_table),'meetings')
    

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resources(resource_type='Starfleet Database')
        self.resource = Resources(resource_name='Dilithium', resource_type = self.type.resource_type, resource_description = 'control agent')
        
    def test_string(self):
        self.assertEqual(str(self.resource), self.resource.resource_name)
    
    def test_resource(self):
        self.assertEqual(str(self.resource.resource_type), 'Starfleet Database')
    
    
    
class MinutesTest(TestCase):
    def test_string(self):
        detail = Minutes(minutes='detail')
        self.assertEqual(str(detail),detail.minutes)

    def test_table(self):
        self.assertEqual(str(Minutes._meta.db_table),'minutes')

class EventsTest(TestCase):
    def test_string(self):
        title = Events(event_title='title')
        self.assertEqual(str(title),title.event_title)

    def test_table(self):
        self.assertEqual(str(Events._meta.db_table),'events')


# Tests for views
class IndexText(TestCase):
    def test_index_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

class NewMeetTest(TestCase):
    def test_newmeet(self):
        response = self.client.get(reverse('new_meeting'))
        self.assertEqual(response.status_code, 200)



