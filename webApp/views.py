from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import redirect
from django.views.generic import View
import urllib, json


from .models import Order

def index(request):
    #return HttpResponse('Hello from Python!')
    #package = Package()
    #package.save()
	
    order = Order.objects.all()
    url = "http://track-chinapost.com/track_chinapost.php?code=pdxn8&cookie=/home/johnyu/vhosts/track-chinapost.com/public/cookie/ikfoemkuh3aihob64hlc0evlp4cookie183.txt&num=RB710452392CN"
    response = urllib.urlopen(url)
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
