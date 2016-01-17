from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.views.generic import View

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
	
def newitem(request):
    def post(self, request, *args, **kwargs):
        ItemName = self.request.get('Name')
        ItemNumber = self.request.get('TrackNumber')
    
        #order = Order(name='test', trackNumber='test num', status='NA')
        order = Order()
        order.name = 'test'
        order.trackNumber = '123'
        order.status = 'NA'
        order.save()
    
        return redirect('./')
        #return HttpResponse('Saved')
