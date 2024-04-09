from django.urls import path
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('event_list', views.event_list, name='event_list'),
    path('event_details', views.event_details, name='event_details'),
    path('add_event', views.add_event, name='add_event'),
    path('update_event', views.update_event, name='update_event'),
    path('delete_event', views.delete_event, name='delete_event'),
    path('del_logic', views.del_logic, name='del_logic'),
]