from django.shortcuts import (render
from .models import *
                              redirect, get_object_or_404)
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'base/home.html')

def