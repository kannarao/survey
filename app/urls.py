from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^rating/$',cntinue),
    url(r'^ThankYou/$',nextPage),
    url(r'^Questions/$',answers),
    url(r'^submit/$',thankss),
    url(r'^contact/$',thanks),
    url(r'^thankss/$',thankss)
]
