#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .utils import Selects
from SisconcBNB.apps.habitantes.models import Habitantes
from SisconcBNB.apps.habitantes.models import Representante
# Create your models here.

#tabla de alumnos 1
class Alumno(models.Model):
	codigo_hab=models.OneToOneField(Habitantes,null=True,on_delete=models.CASCADE, unique=True)
	cedula_escolar=models.OneToOneField(Representante,null=True,on_delete=models.CASCADE,unique=True)
	procedencia_alumn=models.CharField('Procedencia del Alumno', max_length=25,null=True,blank=True)
	plantel_retiro_alumn=models.CharField('Plantel de Retiro el Alumno', max_length=25,null=True,blank=True)
	lugar_habi_alumn=models.CharField('Lugar donde vive el Alumno', max_length=25,null=True,blank=True)# lugar donde vive
	punto_referencia_alumn=models.CharField('Punto de Referencia del Alumno', max_length=25,null=True,blank=True)
	religion=models.CharField('Religión',max_length=45,choices=Selects().religion())
    
	def __str__(self):
		return '{}'.format(self.cedula_escolar)


#tabla de seccion 2
class Seccion(models.Model):
		codigo_seccion=models.AutoField('Codigo de la Sección', primary_key=True)
		turno=models.CharField('Turno',max_length=45,choices=Selects().turno())
		seccion=models.CharField('Sección',max_length=45,choices=Selects().seccion())
		grado=models.CharField('Grado',max_length=45,choices=Selects().grado())

		def __str__(self):
			return '{}'.format(self.codigo_seccion)

#tabla de inscripcion 3
class Inscripcion(models.Model):
		cod_inscri=models.AutoField(primary_key=True)
		cedula_escolar=models.OneToOneField(Alumno,null=True,on_delete=models.CASCADE,unique=True)
		codigo_seccion=models.OneToOneField(Seccion,null=True,on_delete=models.CASCADE,unique=True)
		fecha_inscrip=models.DateField(auto_now=True)
		talla_pantalon=models.CharField('Talla Pantalón',max_length=45,choices=Selects().talla())
	    	talla_franela=models.CharField('Talla Franela',max_length=45,choices=Selects().talla())
	    	talla_Zapato=models.CharField('Talla Zapato',max_length=45,choices=Selects().zapato())
	    	beca_estudiantil=models.BooleanField('¿Posee Beca Estudiantil?', blank=True,default=False)
	    	ano_escolar=models.CharField('Año Escolar',max_length=45,choices=Selects().ano_escolar())
		def __str__(self):
			return '{}'.format(self.cedula_escolar)

#tabla de enfermedad 4
class Enfermedad(models.Model):
		codigo_enfermedad=models.AutoField('Codigo de la Enfermedad', primary_key=True)
		nombres_enfermedad=models.CharField('Nombre(s) de la(s) Enfermedad(es)', max_length=25,null=True)
		descripcion_enfermedad=models.TextField('Descripción de las Enfermedad(es)',max_length=100,null=True)

		def __str__(self):
			return '{}'.format(self.codigo_enfermedad)

#tabla de enfermedad_alumno 5
class Enfermedad_alumno(models.Model):
		cedula_escolar=models.OneToOneField(Alumno,null=True,on_delete=models.CASCADE,unique=True)
		codigo_enfermedad=models.OneToOneField(Enfermedad,null=True,on_delete=models.CASCADE,unique=True)
		fecha_enfer=models.DateField('Fecha de padesimiento de la Enfermedad', null=True)
		

		def __str__(self):
			return '{}'.format(self.cedula_escolar)

#tabla de profesor 6
class Profesor(models.Model):
		codigo_prof=models.AutoField('Codigo del Profesor', primary_key=True)
		codigo_hab=models.OneToOneField(Habitantes,null=True,on_delete=models.CASCADE,unique=True )
		turno=models.CharField('Turno',max_length=45,choices=Selects().turno())
		especialidad_prof=models.CharField('Especialidad del Profesor', max_length=25,blank=True,null=True)
		fecha_ingreso=models.DateField('Fecha del Ingreso del Profesor', null=True)
		
		def __str__(self):
			return '{}'.format(self.codigo_prof)

#tabla de seccion_profesor 7
class Seccion_profesor(models.Model):
		codigo_prof=models.OneToOneField(Profesor,null=True,on_delete=models.CASCADE,unique=True )
		codigo_seccion=models.OneToOneField(Seccion,null=True,on_delete=models.CASCADE,unique=True )
		

		def __str__(self):
		  return '{}'.format(self.codigo_prof)