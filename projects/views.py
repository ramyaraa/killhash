from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projects(request):
    page= "projects"
    number = 11
    context = {'page': page,'number': number}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    return render(request,'projects/single_project.html')



