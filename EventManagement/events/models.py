from django.db import models
from accounts.models import User
# Create your models here.
class EventCategory(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    event_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    max_participants = models.IntegerField()
    is_open = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class EventLink(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=50)
    join_link = models.TextField()
    passcode = models.CharField(max_length=50, blank=True, null=True)
    scheduled_time = models.DateTimeField()

class Media(models.Model):
    MEDIA_TYPES = (('image', 'Image'), ('video', 'Video'), ('poster', 'Poster'))
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    file_path = models.TextField()
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class EventMetric(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE,related_name='metrics')
    views = models.IntegerField(default=0)
    registrations = models.IntegerField(default=0)
    attendance_count = models.IntegerField(default=0)
    feedback_count = models.IntegerField(default=0)

class Announcement(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)