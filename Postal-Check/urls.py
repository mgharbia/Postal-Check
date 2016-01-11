from django.conf.urls import url

from . import webApp.views

urlpatterns = patterns('',
    url(r'^$', webApp.views.index, name='index'),
]