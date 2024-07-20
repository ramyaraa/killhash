from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(request):
    msg = "you are in the project"
    return render(request,'projects/projects.html',{'message':msg})# for adding this message to templates just create a vireable and pass the message key

def project(request,pk):
    return render(request,'projects/single_project.html')



