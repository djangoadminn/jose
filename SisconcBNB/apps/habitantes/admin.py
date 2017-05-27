from django.contrib import admin
from SisconcBNB.apps.habitantes import *

# Register your models here.

from .models import (
    Habitantes,
    Beneficios,
    Solicitud,
    Inspeccion,
    Donacion,
    Supervision,
    Entrega,
    Representante,

)
@admin.register(Habitantes)
class AdminHabitantes(admin.ModelAdmin):
	list_display = ['__str__','codigo_hab','cedula_hab','numero_fam', 
	'apellidos','nombres','estados','municipios','parroquias','fecha_habi','parentesco_hab','telef_hab','movil_hab','genero_hab',]
	class Meta:
		model = Habitantes



@admin.register(Beneficios)
class AdminBeneficios(admin.ModelAdmin):
	list_display = ['__str__','codigo_bene','nombre_bene','descripcion_bene',
	'stock','disponibilidad','fecha_ingreso',]
	class Meta:
		model = Beneficios


@admin.register(Solicitud)
class AdminSolicitud(admin.ModelAdmin):
	list_display = ['__str__','codigo_solici','codigo_hab','codigo_bene','fecha_solici','cantidad_probado','aprobado',]
	class Meta:
		model = Solicitud


@admin.register(Inspeccion)
class AdminInspeccion(admin.ModelAdmin):
	list_display = ['__str__','codigo_inspe','codigo_solici','cedula_ing_ins', 
	'apellidos_ing','nombres_ing_ins','cedula_voc','apellidos_voc','nombres_voc','coodenada_uml',
	'topologia_vivienda','tipo_proyecto','observacion','fecha_inspeccion',]
	class Meta:
		model = Inspeccion

@admin.register(Donacion)
class AdminDonacion(admin.ModelAdmin):
	list_display = ['__str__','codigo_dona','codigo_bene','cedula_ings',
	'apellidos_ing_sup_do','nombres_ing_sup_do','cedula_voc_sup_do','apellidos_voc_sup_do','nombres_voc_sup_do','fecha_dona']
	class Meta:
		model = Donacion

@admin.register(Supervision)
class AdminSupervision(admin.ModelAdmin):
	list_display = ['__str__','codigo_super','codigo_bene','cedula_ing_sup_do','apellidos_ing_sup_do','nombres_ing_sup_do',
	'cedula_voc_sup_do','apellidos_voc_sup_do','nombres_voc_sup_do','lugar_entre',
	'descrip_luga','cantida_bene','fecha_super',]
	class Meta:
		model = Supervision

@admin.register(Entrega)
class AdminEntrega(admin.ModelAdmin):
	list_display = ['__str__','codigo_entre','codigo_solici','cantidad_entrega', 
	'fecha_entrega','cedula_ing','apellidos_ing','nombres_ing','cedula_voc1','apellidos_voc1','nombres_voc1','cedula_voc2',
	'apellidos_voc2','nombres_voc2','cedula_voc3','apellidos_voc3','nombres_voc3',]
	class Meta:
		model = Entrega

@admin.register(Representante)
class AdminRepresentante(admin.ModelAdmin):
	list_display = ['__str__','codigo_representa','cedula_escolar','codigo_hab', 
	'paren_representa',]
	class Meta:
		model = Representante

