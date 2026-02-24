from django.shortcuts import render

def home(requests):
    return render(requests, 'portafolio/main.html')

# Create your views here.
