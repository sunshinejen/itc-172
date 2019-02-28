from django import forms
from .models import Meeting, Resource, Event, MeetingMinutes


class MeetingForm (forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
