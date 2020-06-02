from django.test import TestCase
from .models import Meetings, Minutes, Resources

# Create your tests here.
class MeetingsTest(TestCase):
    meeting=Meetings(meetname='townhall')
    self.assertEqual(str(meeting), meeting.meetname)

def test_table(self):
    self.assertEqual(str(Meetings._meta.db_talbe), 'Meetings')
