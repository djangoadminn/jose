#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import (
    Alumno,
    Seccion,
    Inscripcion,
    Enfermedad,
    Enfermedad_alumno,
    Profesor,
    Seccion_profesor
)
# Register your models here.
class AdminAlumno(admin.ModelAdmin):
	list_display = ['__str__','codigo_hab','cedula_escolar','procedencia_alumn',
	'plantel_retiro_alumn','lugar_habi_alumn','punto_referencia_alumn','religion']
	class Meta:
		model = Alumno

admin.site.register(Alumno, AdminAlumno)

class AdminSeccion(admin.ModelAdmin):
	list_display = ['__str__','codigo_seccion','turno','seccion', 
	'grado',]
	class Meta:
		model = Seccion

admin.site.register(Seccion, AdminSeccion)

class AdminInscripcion(admin.ModelAdmin):
	list_display = ['__str__','cedula_escolar','codigo_seccion','fecha_inscrip', 
	'talla_pantalon','talla_franela','talla_Zapato','beca_estudiantil','ano_escolar']
	class Meta:
		model = Inscripcion

admin.site.register(Inscripcion, AdminInscripcion)

class AdminEnfermedad(admin.ModelAdmin):
	list_display = ['__str__','codigo_enfermedad','nombres_enfermedad','descripcion_enfermedad',]
	class Meta:
		model = Enfermedad
admin.site.register(Enfermedad, AdminEnfermedad)

class AdminEnfermedad_alumno(admin.ModelAdmin):
	list_display = ['__str__','cedula_escolar','codigo_enfermedad','fecha_enfer',]
	class Meta:
		model = Enfermedad_alumno

admin.site.register(Enfermedad_alumno, AdminEnfermedad_alumno)

class AdminProfesor(admin.ModelAdmin):
	list_display = ['__str__','codigo_prof','codigo_hab','turno', 
	'especialidad_prof','fecha_ingreso',]
	class Meta:
		model = Profesor
admin.site.register(Profesor, AdminProfesor)

class AdminSeccion_profesor(admin.ModelAdmin):
	list_display = ['__str__','codigo_prof','codigo_seccion',]
	class Meta:
		model = Seccion_profesor


admin.site.register(Seccion_profesor, AdminSeccion_profesor)




