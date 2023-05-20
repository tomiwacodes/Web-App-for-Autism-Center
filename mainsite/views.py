from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'mainsite/home.html')

def about(request):
    return render(request, 'mainsite/about.html')

def faqs(request):
    return render(request, 'mainsite/faqs.html')

def login(request):
    return render(request, 'mainsite/login.html')

def news(request):
    return render(request, 'mainsite/news.html')

def resources(request):
    return render(request, 'mainsite/resources.html')

def waystohelp(request):
    return render(request, 'mainsite/waystohelp.html')

def my_view(request):
    return render(request, 'mainsite/home.html', {
        'model/': reverse('Model'),
    })