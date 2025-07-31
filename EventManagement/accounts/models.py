from django.db import models

# Create your models here.

class User(models.Model):
    ROLES = (
        ('admin', 'Admin'),
        ('student', 'Student'),
        ('organizer', 'Organizer'),
    )
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()