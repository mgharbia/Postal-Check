from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect

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
    ItemName = self.request.get('Name')
    ItemNumber = self.request.get('TrackNumber')
    
    package = Package(Name='test', TrackNumber='test num', Status='NA')
    package.save()
    
    return redirect('./')

