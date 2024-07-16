from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def projects(request):
    return HttpResponse("Welcome to the Projects App")

def project(request,pk):
    return HttpResponse("single project"+" "+pk)

