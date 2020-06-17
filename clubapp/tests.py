from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Meetings, Minutes, Resources, Events

# Test for models
class MeetingsTest(TestCase):
    def test_string(self):
        type = Meetings(meeting_title = 'Townhall')
        self.assertEqual(str(type),type.meeting_title)

    def test_table(self):
        self.assertEqual(str(Meetings._meta.db_table),'meetings')
    

class ResourceTest(TestCase):
    def setUp(self):
        self.type = Resources(resource_type = 'Starfleet Database')
        self.resource = Resources(resource_name = 'Dilithium', resource_type = self.type.resource_type, resource_description = 'control agent')
        
    def test_string(self):
        self.assertEqual(str(self.resource), self.resource.resource_name)
    
    def test_resource(self):
        self.assertEqual(str(self.resource.resource_type), 'Starfleet Database')
    
    
    
class MinutesTest(TestCase):
    def test_string(self):
        detail = Minutes(minutes = 'detail')
        self.assertEqual(str(detail),detail.minutes)

    def test_table(self):
        self.assertEqual(str(Minutes._meta.db_table),'minutes')

class EventsTest(TestCase):
    def test_string(self):
        title = Events(event_title = 'title')
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
        response = self.client.get(reverse('add_meeting'))
        self.assertEqual(response.status_code, 200)



# Test for authentication      
class Test_New_Meeting_Authentication(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'P@ssw0rd1')
        self.meeting = 'meeting_test'
        self.meet = Meetings.objects.create(meeting_owner = self.test_user, meeting_title = self.meeting, 
        meeting_date = '2020-07-01', meeting_time = '13:00', meeting_location = 'Here', meeting_agenda = 'Test')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('add_meeting'))
        self.assertRedirects(response, '/accounts/login/?next=/clubapp/addMeeting/')
        
    def test_Logged_in_uses_correct_template(self):
        login = self.client.login(username = 'testuser1', password = 'P@ssw0rd1')
        response = self.client.get(reverse('add_meeting'))
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'clubapp/add_meeting.html')

