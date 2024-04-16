from django import forms
from .models import *
from django.contrib.auth import get_user_model

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'start_time', 'end_time', 'description', 'location']
        labels = {'name' : 'Name', 'start_time': 'Start Time', 'end_time' : 'End Time', 'description':'Description', 'location':'Location'}

class Register(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        labels = {'first_name' : 'First Name', 'last_name' : 'Last Name', 'email' : 'Email', 'username' : 'Username', 'password' : 'Password'}
