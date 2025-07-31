from django.shortcuts import render, get_object_or_404
from .models import Event, EventCategory, EventSchedule

def event_list(request):
    events = Event.objects.filter(is_open=True)
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    schedule = EventSchedule.objects.filter(event=event)
    return render(request, 'events/event_detail.html', {'event': event, 'schedule': schedule})

def category_list(request):
    categories = EventCategory.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})
