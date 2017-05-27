#!/usr/bin/python 
# -*- coding: utf-8 -*-
# 
from django.conf.urls import url
from .views import alumno,seccion,inscripcion,enfermedad,enfermealumno,profesor,seccionprofesor
from .views import detallealumno,Listseccion,Listinscrip,Listenfermedad,Listenfermedaal,actuzalienfermalun,Listprofesor,Listseccprof
from .views import actuzalialumno,actuzaliseccion,actuzalinscrip,actuzalienfermedad,actuzaliprofesor,actuzaliseccprof

urlpatterns = [
  #-------crear---------------#
  url(r'^alumno/$',alumno.as_view(), name='alumno'),
  url(r'^seccion/$',seccion.as_view(), name='seccion'),
  url(r'^inscripcion/$',inscripcion.as_view(), name='inscripcion'),
  url(r'^enfermedad/$',enfermedad.as_view(), name='enfermedad'),
  url(r'^enfermedalum/$',enfermealumno, name='enfermedalum'),
  url(r'^profesor/$',profesor.as_view(), name='profesor'),
  url(r'^seccionprof/$',seccionprofesor, name='seccionprof'),
  
  
  #-------listado---------------#
  #url(r'^listado_alumno/$',detallealumno, name = 'listado_alumno'),
  url(r'^listado_seccion/$',Listseccion.as_view(), name = 'listado_seccion'),
  url(r'^listado_inscripcion/$',Listinscrip.as_view(), name = 'listado_inscripcion'),
  url(r'^listado_enfermedad/$',Listenfermedad.as_view(), name = 'listado_enfermedad'),
  url(r'^listado_enfermedadal/$',Listenfermedaal.as_view(), name = 'listado_enfermedadal'),
  url(r'^listado_profesor/$',Listprofesor.as_view(), name = 'listado_profesor'),
  url(r'^listado_seccionprof/$',Listseccprof.as_view(), name = 'listado_seccionprof'),
  
  #-------actualizar---------------#
  url(r'^actualizar_alumno/(?P<pk>\d+)$',actuzalialumno.as_view(), name ="actualizar_alumno"),
  url(r'^actualizar_seccion/(?P<pk>\d+)$',actuzaliseccion.as_view(), name ="actualizar_seccion"),
  url(r'^actualizar_inscrip/(?P<pk>\d+)$',actuzalinscrip.as_view(), name ="actualizar_inscrip"),
  url(r'^actualizar_enfermedad/(?P<pk>\d+)$',actuzalienfermedad.as_view(), name ="actualizar_enfermedad"),
  url(r'^actualizar_enfermedadal/(?P<pk>\d+)$',actuzalienfermedad.as_view(), name ="actualizar_enfermedadal"),
  url(r'^actuzaliprofesor/(?P<pk>\d+)$',actuzaliprofesor.as_view(), name ="actuzaliprofesor"),
  url(r'^actuzaliseccpero/(?P<pk>\d+)$',actuzaliseccprof.as_view(), name ="actuzaliseccpero"),
  
  
]