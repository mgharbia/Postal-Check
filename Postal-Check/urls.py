from django.conf.urls import patterns, include, url

import webApp.views

urlpatterns = patterns('',
    url(r'^$', webApp.views.index, name='index'),
    url(r'^add', webApp.views.add, name='add'),
	url(r'^additem', webApp.views.additem.as_view(), name='additem'),
)