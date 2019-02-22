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
