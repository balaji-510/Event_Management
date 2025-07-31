from django.shortcuts import render, redirect, get_object_or_404
from .models import EventRegistration, Attendance, Team, TeamMember
from events.models import Event
from django.contrib.auth.decorators import login_required

@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    EventRegistration.objects.get_or_create(user=request.user, event=event, status='registered')
    return redirect('event_list')

@login_required
def my_registrations(request):
    registrations = EventRegistration.objects.filter(user=request.user)
    return render(request, 'registrations/my_registrations.html', {'registrations': registrations})

@login_required
def team_list(request, event_id):
    teams = Team.objects.filter(event__id=event_id)
    return render(request, 'registrations/team_list.html', {'teams': teams})
