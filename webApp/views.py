from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect

from .models import Order

def index(request):
    #return HttpResponse('Hello from Python!')
    #package = Package()
    #package.save()
	
    order = Order.objects.all()
	
    return render(request, 'index.html', {'packages': order})

def add(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'add.html', c)
	
def additem(request):
    ItemName = self.request.get('Name')
    ItemNumber = self.request.get('TrackNumber')
    
    order = Order(name='test', trackNumber='test num', status='NA')
    order.save()
    
    return redirect('./')

