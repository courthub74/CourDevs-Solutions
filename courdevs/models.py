from django.db import models

# Create your models here.

class Projects(models.Model):
	projects = models.CharField(max_length=200)
	projectscomplete = models.BooleanField(default=False)

	def __str__(self):
		return self.projects 