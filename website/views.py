from django.shortcuts import render
from urllib import request
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index_view(request):
    return HttpResponse('<h1>Home</h1>')

def about_view(request):
    return HttpResponse('<h1>about</h1>')

def contact_view(request):
    return HttpResponse('<h1>contact</h1>')