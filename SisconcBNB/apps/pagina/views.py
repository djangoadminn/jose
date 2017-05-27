#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
################

from django.contrib.auth.decorators import login_required


	
# Create your views here.


def inicio(request):
	
	return render(request,'pagina/paginicio.html',) 

def mision(request):
	
	return render(request,'pagina/pagmision.html',) 
def vision(request):
	
	return render(request,'pagina/pagvision.html',) 

def resena(request):
	
	return render(request,'pagina/pagreseña.html',) 


def iniciohab(request):
	
	return render(request,'pagina/bienahab.html',) 




"""
@login_required()
def preloader(request):
    return render_to_response('pagina/preloader.html', {'user': request.user},
    context_instance=RequestContext(request))
"""