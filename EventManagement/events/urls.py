from django.urls import path
from . import views

urlpatterns = [
    #path('events/all/', views.all_events, name='all_events'),
    #path('events/create/', views.create_event, name='create_event'),
    path('events/createcat/',views.create_category, name='create_category'),

# Events
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),

    # Event Links
    path('events/<int:event_id>/links/', views.event_link_list, name='event_link_list'),
    path('events/<int:event_id>/links/add/', views.add_event_link, name='add_event_link'),

    # Media
    path('events/<int:event_id>/media/', views.media_list, name='media_list'),
    path('events/<int:event_id>/media/upload/', views.upload_media, name='upload_media'),

    # Metrics
    path('events/<int:event_id>/metrics/', views.event_metrics, name='event_metrics'),

    # Announcements
    path('events/<int:event_id>/announcements/', views.announcement_list, name='announcement_list'),
    path('events/<int:event_id>/announcements/create/', views.create_announcement, name='create_announcement'),
]