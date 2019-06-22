from django.shortcuts import render
from django.http import HttpResponse
from .models import posts


# Create your views here.
def index(request):
   return HttpResponse('Hello from post')

def detail(request, posts_id):
    response = "You're looking at the detail of question %s."
    return HttpResponse(response % posts_id)

def results(request, posts_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % posts_id)