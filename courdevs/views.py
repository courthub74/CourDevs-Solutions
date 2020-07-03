from django.shortcuts import render

# Create your views here.

#MAIN
def main(request):
	return render(request, "main.html", {})
