from django.db import models
from accounts.models import User
from events.models import Event
# Create your models here.

class Payment(models.Model):
    STATUS_CHOICES = (('paid', 'Paid'), ('failed', 'Failed'), ('pending', 'Pending'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payment_method = models.CharField(max_length=50)