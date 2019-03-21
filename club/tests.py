from .forms import MeetingForm, ResourceForm
from django.urls import reverse
from django.test import TestCase
from.models import Meeting, Resource, Event, MeetingMinutes
# Create your tests here.

class MeetingTest(TestCase):
    def test_stringOutputM(self):
        meeting = Meeting(meetingtitle='MeetingOne')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename_meeting(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def test_stringOutputR(self):
        resource = Resource(resourcename='Book')
        self.assertEqual(str(resource), resource.resourcename)

    def test_tablename_resource(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
    def test_stringOutputE(self):
        event = Event(eventtitle='EventOne')
        self.assertEqual(str(event), event.eventtitle)

    def test_tablename_event(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


# testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')

#View Meeting Tests 
class TestGetMeeting(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/meetings')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getmeeting'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getmeeting'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/meetings.html')

# testing forms
# valid Form Data

class New_Meeting_Form_Test(TestCase):
    def test_meetingForm_is_valid(self):
        form = MeetingForm(data={'meetingtitle': "MeetingTest1", 'meetingdate': "2018-12-17",
                                'meetingtime': "05:00", 'meetinglocation': "Seattle", 'agenda': "Testing the meeting"})
        self.assertTrue(form.is_valid())

    def test_UserForm_invalid(self):
        form = MeetingForm(data={'meetingtitle': "MeetingTest1", 'meetingdate': "2018-12-17",
                            'meetingtime': "05:00", 'meetinglocation': "Seattle", 'agenda': "Testing the meeting"})
        self.assertFalse(form.is_valid())


class New_Resource_Form_Test(TestCase):
    def test_resourceForm_is_valid(self):
        form = ResourceForm(data={'resourcename': "ResourceTest1", 'resourcetype': "Book", 'resourceURL': "https://www.codingforentrepreneurs.com",
                                'dateentered': "2019-12-17", 'userid': "jennifer", 'resourcedescription': "Testing the new resource"})
        self.assertTrue(form.is_valid())

    def test_resourceForm_is_invalid(self):
        form = ResourceForm(data={'resourcename': "ResourceTest1", 'resourcetype': "Book", 'resourceURL': "https://www.codingforentrepreneurs.com",
                                'dateentered': "2019-12-17", 'userid': "jennifer", 'resourcedescription': "Testing the new resource"})
        self.assertFalse(form.is_valid())
