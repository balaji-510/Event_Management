from django.shortcuts import render
from .models import Payment
from django.contrib.auth.decorators import login_required

@login_required
def my_payments(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payments/my_payments.html', {'payments': payments})
