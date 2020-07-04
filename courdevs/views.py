from django.shortcuts import render

# Create your views here.

#MAIN
def main(request):
	return render(request, "main.html", {})

#DJANGO 
def setupdjango(request):
	return render(request, "setupdjango.html", {})


#PROJECTS
def projects(request):
	return render(request, "projects.html", {})
