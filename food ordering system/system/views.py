# I have created this file - Darshan
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')



def about(request):
    return render(request, 'about.html')