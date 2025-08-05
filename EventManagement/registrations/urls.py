# registrations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/<int:event_id>/', views.register_for_event, name='register_for_event'),
]
