from django.shortcuts import render
from django.http import HttpResponse
from .models import Advetisment

def index(request):
    advertisements = Advetisment.objects.all()
    context = {'advertisements' : advertisements}
    return render(request, 'index.html', context)
def top_sellers(request):
    return render(request, 'top-sellers.html')
def register(request):
    return render(request, 'register.html')
def profile(request):
    return render(request, 'profile.html')
def login(request):
    return render(request, 'login.html')
def advertisement(request):
    return render(request, 'advertisement.html')
def advertisement_post(request):
    return render(request, 'advertisement_post.html')