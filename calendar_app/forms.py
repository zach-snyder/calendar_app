from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_time', 'end_time', 'description', 'location']
        labels = {'name' : 'Name', 'start_time': 'Start Time', 'end_time' : 'End Time', 'description':'Description', 'location':'Location'}