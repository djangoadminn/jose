from django.shortcuts import render

# Create your views here.
#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from io import BytesIO
#from reportlab.pdfgen import canvas
from django.views.generic import View
#________________________________________
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Context
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
import re
import json
#paginacion de django#
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from SisconcBNB.apps.habitantes.models import Habitantes,Beneficios,Solicitud,Inspeccion,Donacion,Supervision,Entrega,Representante
from SisconcBNB.apps.habitantes.forms import habiForm,BenefiForm,SolicitForm,InspecForm,donaForm,supervForm,entregaForm,repreForm
# Create your views here.


# crear habitante.1
class habitante(CreateView):
	form_class = habiForm
	model = Habitantes
	template_name = 'habitantes/habitante.html'
	success_url = '/detallehabitan'

# crear listado 
def detallehabitan(request):
    queryset = Habitantes.objects.all()
    Context={"queryset":queryset}
    return render(request,'habitantes/detallehabitante.html',Context)

# actualizar habitante.1
class actuzalihabi(UpdateView):
	form_class = habiForm
	model = Habitantes
	template_name = 'habitantes/habitante.html'
	success_url = '/detallehabitan'


def solicitud(request):
    form = SolicitForm(request.POST or None)
    queryset=Solicitud.objects.all()

    for solicitud in queryset:
        print solicitud.codigo_hab     
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "habitantes/solicitud.html", context)

# listado beneficio.3
def detallesolicitud(request):
    queryset = Solicitud.objects.all()
    Context={"queryset":queryset}
    return render(request,'habitantes/detallesolicitud.html',Context)

# actualiza beneficio.3
class actuzalisoli(UpdateView):
	form_class =SolicitForm
	model = Solicitud
	template_name = 'habitantes/solicitud.html'
	success_url='/solicitu'

class Eliminarsoli(DeleteView):
	model = Solicitud
	template_name = 'habitantes/eliminarsolicitud.html'
	success_url='/solicitu'

# crear inspeccion4

def inspeccion(request):
    form = InspecForm(request.POST or None)
    queryset=Inspeccion.objects.all()
    
    for inspeccion in queryset:
        print inspeccion.codigo_inspe    
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "habitantes/inspeccion.html", context)

# listado inspecion.4
class Listainspe(ListView):
	context_object_name = 'inspeccion'
	model = Inspeccion
	template_name = 'habitantes/listinspeci_form.html'

# actualizar inspecion.4
class actuzalinpe(UpdateView):
	form_class = InspecForm
	model = Inspeccion
	template_name = 'habitantes/inspeccion.html'
	success_url= reverse_lazy('habitantes:listinspeci_form.html')

# crear beneficio.1
def beneficio(request):
    form = BenefiForm(request.POST or None)
    queryset=Beneficios.objects.all()
    
    for beneficios in queryset:
        print beneficios.codigo_bene   
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "habitantes/beneficio.html", context)

# listado beneficio.2
def mostrar_benefici(request):
    queryset = Beneficios.objects.all()
    Context={"queryset":queryset}
    return render(request,'habitantes/listbene_form.html',Context)
 
# actualizar beneficio.2
class actuzalbene(UpdateView):
	model = Beneficios
	form_class = BenefiForm
	template_name = 'habitantes/beneficio_form.html'
	#success_url='/mostrarbenefici'

def donacion(request):
    form = donaForm(request.POST or None)
    queryset=Donacion.objects.all()

    for donacion in queryset:
        print donacion.codigo_dona    
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "habitantes/donacion.html", context)

	
# listado beneficio.2
class Listadona(ListView):
	context_object_name = 'donacion'
	model = Donacion
	template_name = 'habitantes/listdona_form.html'


class actuzalidona(UpdateView):
	form_class = donaForm
	model = Donacion
	template_name = 'habitantes/inspeci_form.html'
	success_url = reverse_lazy('habitantes:listado_donaciones')

def supervicion(request):
    form = supervForm(request.POST or None)
    queryset=Supervision.objects.all()
    
    for supervicion in queryset:
        print supervicion.cedula_ing_sup_do
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "habitantes/supervicion.html", context)

# crear beneficio.1
class Listasuper(ListView):
	context_object_name = 'super'
	model = Supervision
	template_name = 'habitantes/listsupervic_form.html'

# crear beneficio.1
class actuzalisuper(UpdateView):
	model = Supervision
	form_class = supervForm
	template_name = 'habitantes/supervic_form.html'
	success_url = reverse_lazy('habitantes:listado_supervicion')


def entrega(request):
    form = entregaForm(request.POST or None)
    queryset=Entrega.objects.all()
    
    for entrega in queryset:
        print entrega.codigo_solici   
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "habitantes/entrega.html", context)

# mostrar entregar
def mostrar_entrega(request):
    queryset=Entrega.objects.all()
    Context={"queryset":queryset}
    return render(request,'habitantes/listentre_form.html',Context)
 

class actuzalientre(UpdateView):
	model = Entrega
	form_class = entregaForm
	template_name = 'habitantes/entre_form.html'
	success_url = reverse_lazy('habitantes:listado_entrega')

#vista de representante 8

def representante(request):
    form = repreForm(request.POST or None)
    queryset=Representante.objects.all()
    
    for representante in queryset:
        print representante.cedula_escolar  
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "habitantes/representante.html", context)

def representa(request):
    queryset = Representante.objects.all()
    Context={"queryset":queryset}
    return render(request,'habitantes/listrepre_form.html',Context)

class actuzalirepre(UpdateView):
	model = Representante
	form_class = repreForm
	template_name = 'habitantes/representante.html'
	success_url = reverse_lazy('habitantes:listado_de_representante')