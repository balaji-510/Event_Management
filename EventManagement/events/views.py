#from django.shortcuts import render, get_object_or_404
#from .models import Event, EventCategory, EventSchedule
#
#def event_list(request):
#    events = Event.objects.filter(is_open=True)
#    return render(request, 'events/event_list.html', {'events': events})
#
#def event_detail(request, event_id):
#    event = get_object_or_404(Event, id=event_id)
#    schedule = EventSchedule.objects.filter(event=event)
#    return render(request, 'events/event_detail.html', {'event': event, 'schedule': schedule})
#
#def category_list(request):
#    categories = EventCategory.objects.all()
#    return render(request, 'events/category_list.html', {'categories': categories})
#
from django.shortcuts import render
#from .models import Event
#from django.contrib.auth.decorators import login_required
#from django.shortcuts import render, redirect
#from django.http import HttpResponseForbidden
#from .forms import EventForm,EventCategoryForm
#
#@login_required
#def create_event(request):
#    # Allow only organizers and admins
#    if request.user.role not in ['organizer', 'admin']:
#        return HttpResponseForbidden("You are not authorized to create events.")
#
#    if request.method == 'POST':
#        form = EventForm(request.POST)
#        if form.is_valid():
#            event = form.save(commit=False)
#            event.organizer = request.user
#            event.save()
#            return redirect('event_list')
#    else:
#        form = EventForm()
#
#    return render(request, 'events/create_event.html', {'form': form})
#

#
#def all_events(request):
#    events = Event.objects.select_related('category').all().order_by('event_date')
#    return render(request, 'events/all_events.html', {'events': events})
#

#from django.shortcuts import render, get_object_or_404, redirect
#from django.contrib.auth.decorators import login_required
#from .models import Event, EventCategory, EventLink, Media, EventMetric, Announcement
#from .forms import EventForm, EventLinkForm, MediaForm, AnnouncementForm
#
#@login_required
#def event_list(request):
#    events = Event.objects.all()
#    return render(request, 'events/event_list.html', {'events': events})
#
#@login_required
#def event_detail(request, event_id):
#    event = get_object_or_404(Event, id=event_id)
#    links = EventLink.objects.filter(event=event)
#    media = Media.objects.filter(event=event)
#    announcements = Announcement.objects.filter(event=event)
#    return render(request, 'events/event_detail.html', {
#        'event': event,
#        'links': links,
#        'media': media,
#        'announcements': announcements
#    })
#
#@login_required
#def create_event(request):
#    if request.user.role not in ['admin', 'organizer']:
#        return redirect('event_list')
#
#    if request.method == 'POST':
#        form = EventForm(request.POST)
#        if form.is_valid():
#            event = form.save(commit=False)
#            event.organizer = request.user
#            event.save()
#            return redirect('event_list')
#    else:
#        form = EventForm()
#    return render(request, 'events/create_event.html', {'form': form})
#
#@login_required
#def add_event_link(request, event_id):
#    event = get_object_or_404(Event, id=event_id)
#    if request.user.role not in ['admin', 'organizer']:
#        return redirect('event_detail', event_id=event_id)
#
#    if request.method == 'POST':
#        form = EventLinkForm(request.POST)
#        if form.is_valid():
#            link = form.save(commit=False)
#            link.event = event
#            link.save()
#            return redirect('event_detail', event_id=event_id)
#    else:
#        form = EventLinkForm()
#    return render(request, 'events/add_event_link.html', {'form': form, 'event': event})
#
#@login_required
#def upload_media(request, event_id):
#    event = get_object_or_404(Event, id=event_id)
#    if request.user.role not in ['admin', 'organizer']:
#        return redirect('event_detail', event_id=event_id)
#
#    if request.method == 'POST':
#        form = MediaForm(request.POST)
#        if form.is_valid():
#            media = form.save(commit=False)
#            media.event = event
#            media.save()
#            return redirect('event_detail', event_id=event_id)
#    else:
#        form = MediaForm()
#    return render(request, 'events/upload_media.html', {'form': form, 'event': event})
#
#@login_required
#def add_announcement(request, event_id):
#    event = get_object_or_404(Event, id=event_id)
#    if request.user.role not in ['admin', 'organizer']:
#        return redirect('event_detail', event_id=event_id)
#
#    if request.method == 'POST':
#        form = AnnouncementForm(request.POST)
#        if form.is_valid():
#            announcement = form.save(commit=False)
#            announcement.event = event
#            announcement.save()
#            return redirect('event_detail', event_id=event_id)
#    else:
#        form = AnnouncementForm()
#    return render(request, 'events/add_announcement.html', {'form': form, 'event': event})
# events/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, EventCategory, EventLink, Media, EventMetric, Announcement
from .forms import EventForm, EventLinkForm, MediaForm, AnnouncementForm, EventCategoryForm

@login_required
def event_list(request):
    events = Event.objects.all().select_related('category')
    for event in events:
        metric = EventMetric.objects.filter(event=event).first()
        if metric:
            event.spots_left = max(event.max_participants - metric.registrations, 0)
            event.percent_filled = round((metric.registrations / event.max_participants) * 100) if event.max_participants else 0
            event.has_metric = True
        else:
            event.spots_left = event.max_participants
            event.percent_filled = 0
            event.has_metric = False
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    links = EventLink.objects.filter(event=event)
    media = Media.objects.filter(event=event)
    announcements = Announcement.objects.filter(event=event)
    return render(request, 'events/event_detail.html', {
        'event': event,
        'links': links,
        'media': media,
        'announcements': announcements
    })

@login_required
def create_event(request):
    if request.user.role not in ['admin', 'organizer']:
        return redirect('event_list')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            EventMetric.objects.create(event=event)
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.organizer and request.user.role != 'admin':
        return redirect('event_detail', event_id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form, 'event': event})

@login_required
def event_link_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    links = EventLink.objects.filter(event=event)
    return render(request, 'events/event_link_list.html', {'event': event, 'links': links})

@login_required
def add_event_link(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user.role not in ['admin', 'organizer']:
        return redirect('event_detail', event_id=event_id)

    if request.method == 'POST':
        form = EventLinkForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.event = event
            link.save()
            return redirect('event_link_list', event_id=event_id)
    else:
        form = EventLinkForm()
    return render(request, 'events/add_event_link.html', {'form': form, 'event': event})

@login_required
def media_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    media = Media.objects.filter(event=event)
    return render(request, 'events/media_list.html', {'event': event, 'media': media})

@login_required
def upload_media(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user.role not in ['admin', 'organizer']:
        return redirect('event_detail', event_id=event_id)

    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            media = form.save(commit=False)
            media.event = event
            media.save()
            return redirect('media_list', event_id=event_id)
    else:
        form = MediaForm()
    return render(request, 'events/upload_media.html', {'form': form, 'event': event})

@login_required
def event_metrics(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    metrics = get_object_or_404(EventMetric, event=event)
    return render(request, 'events/event_metrics.html', {'event': event, 'metrics': metrics})

@login_required
def announcement_list(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    announcements = Announcement.objects.filter(event=event)
    return render(request, 'events/announcement_list.html', {'event': event, 'announcements': announcements})

@login_required
def create_announcement(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user.role not in ['admin', 'organizer']:
        return redirect('event_detail', event_id=event_id)

    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.event = event
            announcement.save()
            return redirect('announcement_list', event_id=event_id)
    else:
        form = AnnouncementForm()
    return render(request, 'events/create_announcement.html', {'form': form, 'event': event})

def create_category(request):
    if request.method == 'POST':
        form = EventCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_event')
    else:
        form = EventCategoryForm()
    return render(request, 'events/create_category.html', {'form': form})