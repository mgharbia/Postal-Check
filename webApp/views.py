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
    url = "http://www.israelpost.co.il/itemtrace.nsf/trackandtraceJSON?openagent&_=1375340219593&lang=EN&itemcode="
    #bad track RP325501964SG
    #good track RB710452392CN
		
    orders = Order.objects.all()
    for order in orders:
        if order.status == 'NA':
            http = urllib3.PoolManager()
            response = http.urlopen('GET',url + order.trackNumber, preload_content=False)

            jasonString = response.read().decode('utf-8')
            if jasonString.find('for distribution at the customer') != -1:
                order.status = 'Arrived'
                order.save()
            #else:
            #    return HttpResponse('NA')
    return render(request, 'index.html', {'orders': orders})

	
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
