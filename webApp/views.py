from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.views.generic import View
import urllib3
#from urllib3.request import urlopen

from .models import Order

def index(request):
    #return HttpResponse('Hello from Python!')
    #package = Package()
    #package.save()
	
    order = Order.objects.all()
    url = "http://www.israelpost.co.il/itemtrace.nsf/trackandtraceJSON?openagent&_=1375340219593&lang=EN&itemcode=RB710452392CN"
    http = urllib3.PoolManager()
    #response = urllib3.request.urlopen(url)
    response = http.urlopen('GET',url, preload_content=False)
    return HttpResponse(response)
    #return render(request, 'index.html', {'orders': order})

def add(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'add.html', c)
	
class newitem(View):
    def post(self, request, *args, **kwargs):
        ItemName = self.request.POST.get("Name", "")
        ItemNumber = self.request.POST.get("TrackNumber", "")
    
        #order = Order(name='test', trackNumber='test num', status='NA')
        order = Order()
        order.name = ItemName
        order.trackNumber = ItemNumber
        order.status = 'NA'
        order.save()
    
        #return redirect('./')
        return HttpResponse('added')
