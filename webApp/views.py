from django.shortcuts import render
from django.http import HttpResponse

from .models import Package

def index(request):
    #return HttpResponse('Hello from Python!')
    #package = Package()
    #package.save()
	
    packages = Package.objects.all()
	
    return render(request, 'index.html', {'packages': packages})

def add(request):
    return render(request, 'add.html')

