from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('organizer', 'Organizer'),
    )
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
