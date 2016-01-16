from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf

from .models import Package

def index(request):
    #return HttpResponse('Hello from Python!')
    #package = Package()
    #package.save()
	
    packages = Package.objects.all()
	
    return render(request, 'index.html', {'packages': packages})

def add(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'add.html', c)
	
def additem(request):
    Name = self.request.get('Name')
    TrackNumber = self.request.get('TrackNumber')
    #package.save()
	
    self.redirect('/')

