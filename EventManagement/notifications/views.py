from django.shortcuts import render
from .models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/user_notifications.html', {'notifications': notifications})
