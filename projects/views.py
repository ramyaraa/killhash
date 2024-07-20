from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {'id': 1, 'title': 'Project 1', 'description': 'This is project 1 description'},
    {'id': 2, 'title': 'Project 2', 'description': 'This is project 2 description'},
    {'id': 3, 'title': 'Project 3', 'description': 'This is project 3 description'},
    #... add more projects here...
]
def projects(request):
    page= "projects"
    number = 11
    context = {'page': page,'number': number,'projects': projectsList}
    return render(request,'projects/projects.html',context)

def project(request,pk):
    return render(request,'projects/single_project.html')



