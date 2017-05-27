#!/usr/bin/python	
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import habitante,inspeccion,beneficio,solicitud,donacion,supervicion,entrega,representante
from .views import actuzalihabi,actuzalbene,actuzalisoli,actuzalinpe,actuzalidona,actuzalisuper,actuzalientre,actuzalirepre
from .views import detallehabitan,detallesolicitud,mostrar_benefici,mostrar_entrega,mostrar_entrega,representante
from .views import Eliminarsoli,Listainspe,Listadona,Listasuper




urlpatterns = [
    #-------CREAR---------------#
	url(r'^habitante/$', habitante.as_view(), name='habitante'),
	url(r'^beneficio/$', beneficio, name='beneficio'),
	url(r'^solicitud/$',solicitud,name='solicitud'), 
	url(r'^inspeccion/$',inspeccion,name='inspeccion'), 
	url(r'^donacion/$',donacion, name='donacion'),
	url(r'^supervicion/$',supervicion, name='supervicion'),
	url(r'^entrega/$',entrega, name='entrega'),
	url(r'^representante/$',representante, name='representante'),

	#-------LISTADO---------------#
	url(r'^listado_habitante/$',detallehabitan,name='listado_habitante'), 
	url(r'^mostrarbene/$',mostrar_benefici,name='mostrarbene'), 
	#url(r'^listado_beneficiario/$',Listabene.as_view(), name ='listado_beneficiario'),
	url(r'^listado_solicitud/$',detallesolicitud, name = 'listado_solicitud'),
	url(r'^listado_inspeccion/$',Listainspe.as_view(), name = 'listado_inspeccion'),
	url(r'^listado_donacion/$',Listadona.as_view(), name = 'listado_donacion'),
	url(r'^listado_supervicion/$',Listasuper.as_view(), name = 'listado_supervicion'),
	url(r'^mostrarentrega/$',mostrar_entrega,name='mostrarentrega'),
	#url(r'^listado_entrega/$',Listaentre.as_view(), name = 'listado_entrega'),
	url(r'^mostra_representante/$',representante,name='mostra_representante'),
	
	#-------ACTUALIZAR---------------#
	url(r'^actualhabitante(?P<pk>\d+)$',actuzalihabi.as_view(), name ="actualhabitante"),
	url(r'^actualizabenefi/(?P<pk>\d+)$',actuzalbene.as_view(),name='actualizar_beneficio'),
	url(r'^actualizar_inspeccio/(?P<pk>\d+)$',actuzalinpe.as_view(), name ="actualizar_inspeccio"),
	url(r'^actualsolicitud/(?P<pk>\d+)$',actuzalisoli.as_view(), name='actualsolicitud'),
	url(r'^actualizar_donacion/(?P<pk>\d+)$',actuzalidona.as_view(), name='actualizar_donacion'),
	url(r'^actualizar_supervicion/(?P<pk>\d+)$',actuzalisuper.as_view(), name='actualizar_supervicion'),
	url(r'^actualizar_entrega/(?P<pk>\d+)$',actuzalientre.as_view(), name='actualizar_entrega'),
	url(r'^actualizar_representante/(?P<pk>\d+)$',actuzalirepre.as_view(), name='actualizar_representante'),
	
	#-------ELIMINAR---------------#
	url(r'^eliminsolicitud/(?P<pk>\d+)/$', Eliminarsoli.as_view(), name="eliminsolicitud"),

]