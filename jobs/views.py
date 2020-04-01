from django.shortcuts import render
from .models import Job
# Create your views here.

class Job_list(request):
	jobs=job.objects.all()