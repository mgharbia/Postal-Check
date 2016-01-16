from django.conf.urls import patterns, include, url

import webApp.views

urlpatterns = patterns('',
    url(r'^$', webApp.views.index, name='index'),
    url(r'^add', webApp.views.index, name='add'),
)