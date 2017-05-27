#!/usr/bin/python
# -*- coding: utf-8 -*-
# Create your views here.
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
from django.views.generic import CreateView 
from django.views.generic import ListView 
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
#paginacion de django#
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from SisconcBNB.apps.alumnos.models import Alumno,Seccion,Inscripcion,Enfermedad,Enfermedad_alumno,Profesor,Seccion_profesor
from SisconcBNB.apps.alumnos.forms import alumnForm,seccForm,inscripForm,enferForm,enfermalumnForm,profeForm,seccproForm

# Create your views here.


# crear habitante.1
class alumno(CreateView):
	form_class = alumnForm
	model = Alumno
	template_name = 'alumnos/alumnos.html'
	

def detallealumno(request):
    queryset = Alumno.objects.all()
    Context={"queryset":queryset}
    return render(request,'alumnos/detallealumno.html',Context)


#update 1#

class actuzalialumno(UpdateView):
	model = Alumno
	form_class = alumnForm
	template_name = 'alumnos/alumnos.html'
	success_url = reverse_lazy('alumno:listado_alumno')

# crear habitante.1
class seccion(CreateView):
	form_class = seccForm
	model = Seccion
	template_name = 'alumnos/seccion.html'
	success_url = '/seccion'

# crear listado del habitante.1
class Listseccion(ListView):
	context_object_name = 'seccion'
	model = Seccion
	template_name = 'alumnos/listseccion_form.html'

class actuzaliseccion(UpdateView):
	model = Seccion
	form_class = seccForm
	template_name = 'alumnos/seccion.html'
	success_url = reverse_lazy('alumno:listado_seccion')

# vista de inscripcion 3

class inscripcion(CreateView):
	form_class = inscripForm
	model = Inscripcion
	template_name = 'alumnos/inscripcion.html'
	success_url = '/inscripcion'

# crear listado del habitante.1
class Listinscrip(ListView):
	context_object_name = 'seccion'
	model = Inscripcion
	template_name = 'alumnos/listinscrip_form.html'


#update 3#
class actuzalinscrip(UpdateView):
	model = Inscripcion
	form_class = inscripForm
	template_name = 'alumnos/inscrip_form.html'
	success_url = reverse_lazy('alumno:listado_inscripcion')

class enfermedad(CreateView):
	form_class = enferForm
	model = Enfermedad
	template_name = 'alumnos/enfermedad.html'
	success_url = '/enfermedad'

# crear listado del habitante.1
class Listenfermedad(ListView):
	context_object_name = 'seccion'
	model = Enfermedad
	template_name = 'alumnos/listenfermed_form.html'

# vista de enfermedad 4

#update 4#
#
#
class actuzalienfermedad(UpdateView):
	model = Enfermedad
	form_class = enferForm
	template_name = 'alumnos/enfermedad_form.html'
	success_url = reverse_lazy('alumno:listado_enfermedad')

def enfermealumno(request):
    form = enfermalumnForm(request.POST or None)
    queryset=Enfermedad_alumno.objects.all()
    
    for enfermealumno in queryset:
        print enfermealumno.codigo_enfermedad 
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "alumnos/enfermedalumnos.html", context)


# crear listado del habitante.1
class Listenfermedaal(ListView):
	context_object_name = 'seccion'
	model = Enfermedad_alumno
	template_name = 'alumnos/listenferalumn_form.html'


#update 5#
class actuzalienfermalun(UpdateView):
	model = Enfermedad_alumno
	form_class = enfermalumnForm
	template_name = 'alumnos/enfermedalumn_form.html'
	success_url = reverse_lazy('alumno: listado_enfermedadal')

class profesor(CreateView):
	form_class = profeForm
	model = Profesor
	template_name = 'alumnos/profesor.html'
	success_url = '/profesor'

# crear listado del habitante.1
class Listprofesor(ListView):
	context_object_name = 'seccion'
	model = Profesor
	template_name = 'alumnos/listprof_form.html'

#update 6#
class actuzaliprofesor(UpdateView):
	model = Profesor
	form_class = profeForm
	template_name = 'alumnos/profesor.html'
	success_url = reverse_lazy('alumno:listado_profesor')

def seccionprofesor(request):
    form = seccproForm(request.POST or None)
    queryset=Seccion_profesor.objects.all()
    
    for seccionprofesor in queryset:
        print seccionprofesor.codigo_seccion
    context = {
        "form": form,
        "queryset": queryset
    }
    if form.is_valid():
  
        form.save()
    return render(request, "alumnos/seccionprofesor.html", context)


# crear listado del habitante.1
class Listseccprof(ListView):
	context_object_name = 'seccion'
	model = Seccion_profesor
	template_name = 'alumnos/listseccionprof_form.html'

#update 7#
class actuzaliseccprof(UpdateView):
	model = Seccion_profesor
	form_class = seccproForm
	template_name = 'alumnos/seccionprof_form.html'
	success_url = reverse_lazy('alumno:listado_seccionprof')