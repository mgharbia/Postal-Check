from django.conf.urls import url

import webApp.views

urlpatterns = patterns('',
    url(r'^$', webApp.views.index, name='index'),
]