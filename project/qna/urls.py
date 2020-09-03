from django.conf.urls import url
from django.urls import path

from .views import *

app_name = 'polls'

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view()),
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteView.as_view()),
    url(r'^(?P<pk>[0-9]+)/vote/$', SwitchboardView.as_view(), name='vote_result')
]
