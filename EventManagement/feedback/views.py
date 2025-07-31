from django.shortcuts import render, redirect, get_object_or_404
from .models import Feedback, Certificate
from events.models import Event
from django.contrib.auth.decorators import login_required

@login_required
def give_feedback(request, event_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        Feedback.objects.create(
            user=request.user,
            event_id=event_id,
            rating=rating,
            comments=comments
        )
        return redirect('event_list')
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'feedback/give_feedback.html', {'event': event})

@login_required
def my_certificates(request):
    certificates = Certificate.objects.filter(user=request.user)
    return render(request, 'feedback/my_certificates.html', {'certificates': certificates})
