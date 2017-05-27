# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import inicio,mision,resena,iniciohab,vision

urlpatterns = [
  url(r'^$' ,inicio,name='inicio'),
  url(r'^mision/$', mision,name='mision'),
  url(r'^vision/$', vision,name='vision'),
  url(r'^resena/$', resena,name='resena'), 
  url(r'^iniciohab/$', iniciohab,name='iniciohab'), 
  #url(r'^preloader/$', preloader,name='preloader'),  
]