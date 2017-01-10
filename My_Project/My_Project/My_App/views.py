from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Get Her Done")

# Create your views here.
