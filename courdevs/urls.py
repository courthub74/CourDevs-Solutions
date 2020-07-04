from django.urls import path
from . import views

urlpatterns = [
	path('', views.main, name='main'),
	path('setupdjango/', views.setupdjango, name="setupdjango"),
	path('projects/', views.projects, name="projects"),
]