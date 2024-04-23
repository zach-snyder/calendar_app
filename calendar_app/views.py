from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import EventForm



# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render(request, 'index.html')

def add_event(request):
   if request.method == 'POST':
      form = EventForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('event_list')
      
   else:
      form = EventForm()

   return render(request, 'add_event.html', {'form' : form})
      


def event_list(request):
   
   events = Event.objects.all()
   return render(request, 'event_list.html', {'events': events})


def event_details(request):
   event_id = request.GET.get('event_id')
   event = Event.objects.get(id=event_id)
   return render(request, 'event_details.html', {'event':event})

def update_event(request):
   event_id = request.GET.get('event_id')
   event = Event.objects.get(id=event_id)

   if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            
            return redirect('event_list')
    
   else: 
         form = EventForm(instance=event)

   return render(request, 'edit_event.html', {'form': form})

def delete_event(request):
    event_id = request.GET.get('event_id')
    event = Event.objects.get(id = event_id)

    return render(request, 'delete_event.html', {'event' : event})

def del_logic(request):
 

    delete_conf = request.GET.get('del')


    if delete_conf == "1":
        
      event_id = request.GET.get('event_id')
      event = Event.objects.get(id = event_id)
      event.delete()

    return redirect('event_list')