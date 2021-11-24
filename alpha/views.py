from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            'kimumar55@gmail.com',
            ['info@noziroh.com.ng'],
            fail_silently=False)
    
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            'kimumar55@gmail.com',
            ['oladeleumaradisa19@gmail.com'],
            fail_silently=False)

    return render(request, 'about.html')

def services(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            'kimumar55@gmail.com',
            ['nozprofessionals@gmail.com'],
            fail_silently=False)
    
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            name,
            message,
            'kimumar55@gmail.com',
            ['oladeleumaradisa19@gmail.com'],
            fail_silently=False)
    
    return render(request, 'contact.html')