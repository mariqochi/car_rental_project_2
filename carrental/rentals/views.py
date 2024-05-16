from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render (request, 'home.html') #HttpResponse ("<h1> Home Page</h1>")

def room (request):
    return render (request, 'room.html')

# Create your views here.
