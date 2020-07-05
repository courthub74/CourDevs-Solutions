from django.shortcuts import render, redirect
from .models import Projects
from .forms import ProjectsForm
from django.contrib import messages

# Create your views here.

#MAIN
def main(request):
	return render(request, "main.html", {})

#DJANGO 
def setupdjango(request):
	return render(request, "setupdjango.html", {})


#PROJECTSentry
def projects(request):
	if request.method == 'POST':
		pform = ProjectsForm(request.POST or None)

		if pform.is_valid():
			pform.save()
			all_projects = Projects.objects.all
			messages.success(request, ("Project Has Been Added To 'Projects' List"))
			return render(request, "projects.html", {'all_projects': all_projects})

	else:
		all_projects = Projects.objects.all
		return render(request, "projects.html", {'all_projects': all_projects})

#PROJECTScrossoff
def project_cross_off(request, list_id):
	projects = Projects.objects.get(pk=list_id)
	projects.projectscomplete = True
	projects.save()
	return redirect ('projects')

#PROJECTSuncross
def project_uncross(request, list_id):
	projects = Projects.objects.get(pk=list_id)
	projects.projectscomplete = False
	projects.save()
	return redirect ('projects')

#PROJECTSdelete
def project_delete(request, list_id):
	projects = Projects.objects.get(pk=list_id)
	projects.delete()
	messages.success(request, ('Project Has Been Deleted'))
	return redirect ('projects')


	 
	
