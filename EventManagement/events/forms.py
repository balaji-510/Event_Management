from django import forms
from .models import Event
from .models import EventCategory

class EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ['category_name', 'description']

from django import forms
from .models import Event, EventLink, Media, Announcement

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class EventLinkForm(forms.ModelForm):
    class Meta:
        model = EventLink
        fields = '__all__'

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = '__all__'

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = '__all__'
