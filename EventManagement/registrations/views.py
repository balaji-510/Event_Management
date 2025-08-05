#from django.shortcuts import render, redirect, get_object_or_404
#from .models import EventRegistration, Attendance, Team, TeamMember
#from events.models import Event
#from django.contrib.auth.decorators import login_required
#
#@login_required
#def register_event(request, event_id):
#    event = get_object_or_404(Event, id=event_id)
#    EventRegistration.objects.get_or_create(user=request.user, event=event, status='registered')
#    return redirect('event_list')
#
#@login_required
#def my_registrations(request):
#    registrations = EventRegistration.objects.filter(user=request.user)
#    return render(request, 'registrations/my_registrations.html', {'registrations': registrations})
#
#@login_required
#def team_list(request, event_id):
#    teams = Team.objects.filter(event__id=event_id)
#    return render(request, 'registrations/team_list.html', {'teams': teams})
## registrations/views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from events.models import Event, EventMetric
from .models import EventRegistration

def register_for_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if not request.user.is_authenticated:
        messages.error(request, "Please login to register for an event.")
        return redirect('login')

    if EventRegistration.objects.filter(user=request.user, event=event, status='registered').exists():
        messages.warning(request, "You are already registered for this event.")
        return redirect('event_list')

    registration_count = EventRegistration.objects.filter(event=event, status='registered').count()
    if registration_count >= event.max_participants:
        messages.error(request, "Sorry, the event is full.")
        return redirect('event_list')

    EventRegistration.objects.create(
        user=request.user,
        event=event,
        status='registered'
    )

    # Update event metrics
    metric, created = EventMetric.objects.get_or_create(event=event)
    metric.registrations += 1
    metric.save()

    messages.success(request, f"Successfully registered for {event.title}.")
    return redirect('event_list')
