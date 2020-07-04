from django.shortcuts import render
from .models import Projects

# Create your views here.

#MAIN
def main(request):
	return render(request, "main.html", {})

#DJANGO 
def setupdjango(request):
	return render(request, "setupdjango.html", {})


#PROJECTS
def projects(request):
	all_projects = Projects.objects.all 
	return render(request, "projects.html", {'all_projects': all_projects})
