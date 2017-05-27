#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from dal import autocomplete
from django.db import models
from django.utils import timezone
import decimal
from.utils import Selects


# Create your models here.
#tabla de habitantes 1
class Habitantes (models.Model):
	codigo_hab=models.AutoField('Codigo del habitante',primary_key=True)     
	cedula_hab=models.CharField('Cedula', max_length=8,unique=True)
	numero_fam=models.CharField('Numero de Familia', max_length=3, default=0)
	nombres=models.CharField('Nombres',max_length=30,null=True)
	apellidos=models.CharField('Apellidos',max_length=30,null=True)
	estados=models.CharField('Estados',max_length=30,null=True,blank=True)
	municipios=models.CharField('Municipios', max_length=30,null=True,blank=True)
	parroquias=models.CharField('Parroquias', max_length=30,null=True,blank=True)
	fecha_habi=models.DateField('Fecha de nacimiento', max_length=100)
	parentesco_hab=models.CharField('Parentesco del Habitante', blank=True,max_length=20,choices=Selects().parentesco())
	cod_tel=models.CharField('Codigo del Telefono',blank=True, max_length=45,choices=Selects().telefono())
	telef_hab=models.CharField('Telefono', blank=True,max_length=8)
	codigo_movil=models.CharField('Codigo del Movil', blank=True, max_length=45,choices=Selects().movil())
	movil_hab=models.CharField('Movil', blank=True,max_length=7)
	genero_hab=models.CharField('Genero', blank=True,max_length=45,choices=Selects().genero())
	toalla_hab=models.NullBooleanField('¿Utiliza Toalla?', blank=True,default=False) #status
	panal_hab=models.NullBooleanField('¿Utiliza Pañal?', blank=True,default=False) #status
	ocupacion_hab=models.CharField('Ocupación del Habitante', blank=True,max_length=20,choices=Selects().ocupacion())
	direccion=models.TextField('Dirección del Habitante', max_length=100 ,null=True, blank=True)
	tipo_propiedad_hab=models.CharField('Tipo de Propiedad', blank=True, max_length=45,choices=Selects().propiedad())
	correo=models.EmailField('Correo electronico', max_length=70,blank=True)  
	consejoc_pert=models.CharField('Consejo comunal que pertenece', max_length=45,choices=Selects().consejocomunal())

	
	def __str__(self):
		return '{},{}'.format(self.codigo_hab,self.nombres)

#tabla de beneficio 2
class Beneficios(models.Model):
		codigo_bene=models.AutoField('Codigo del Beneficio',primary_key=True)
		nombre_bene=models.CharField('Nombre del Beneficio', max_length=25,null=True)
		descripcion_bene=models.TextField('Descripción del Beneficio', max_length=100,null=True)
		stock=models.PositiveSmallIntegerField('Stock')#no permite campos negativos
		disponibilidad=models.CharField('Disponibilidad', max_length=100,null=True)
		fecha_ingreso=models.DateField('Fecha de Ingreso', auto_now=True)
	
		def __str__(self):
		 return '{},{}'.format(self.codigo_bene,self.nombre_bene)


#tabla de solicitud 3
class Solicitud(models.Model):
		codigo_solici=models.AutoField('Codigo Solicitud', primary_key=True)
		codigo_hab=models.ForeignKey(Habitantes,on_delete=models.CASCADE)
		codigo_bene=models.ForeignKey(Beneficios,on_delete=models.CASCADE)
		cantidad_bene=models.IntegerField('Cantidad del Beneficio', null=True, default=0)
		cantidad_probado=models.IntegerField('Cantidad de beneficios Aprobados', blank=True,null=True, default=0)
		fecha_solici=models.DateTimeField('Fecha de la Solicitud', auto_now=True)
		aprobado=models.BooleanField('Aprobado', default=False)

		def __str__(self):
			return '{}'.format(self.codigo_solici)

		def save(self, *args, **kwargs):
			if self.cantidad_bene:
				if self.cantidad_bene < 3 :
					super(Solicitud, self).save(*args, **kwargs)
			else:
				self.cantidad_bene = 0 
				raise RuntimeError("ya esite la solicitud")
				super(Solicitud, self).save(*args, **kwargs)
				
#tabla de inspeccion 4
class Inspeccion(models.Model):
		codigo_inspe=models.AutoField('Codigo de Inspección', primary_key=True)
		codigo_solici=models.ForeignKey(Solicitud,null=True,on_delete=models.CASCADE )
		cedula_ing_ins=models.CharField('Cedula del Ing Supervisor', blank= True,max_length=8,null=True)
		apellidos_ing=models.CharField('Apellidos del Ing supervisor', blank= True,max_length=50,null=True)
		nombres_ing_ins=models.CharField('Nombres del Ing supervisor', blank= True,max_length=25,null=True)
		cedula_voc=models.CharField('Cedula del Vocero', blank= True,max_length=8,null=True)
		apellidos_voc=models.CharField('Apellidos del Vocero', blank= True,max_length=50,null=True)
		nombres_voc=models.CharField('Nombres del Vocero', blank= True,max_length=25,null=True)
		coodenada_uml=models.CharField('Coordenada UML', blank= True,max_length=45,null=True)
		topologia_vivienda=models.CharField('Topologia de Vivienda', blank= True,max_length=45,null=True)
		tipo_proyecto=models.CharField('Tipo de Proyecto', blank= True,max_length=100,null=True)
		observacion=models.TextField('Observación', blank= True,max_length=100,null=True)
		fecha_inspeccion=models.DateField('Fecha de Inspección', max_length=100)

		def __str__(self):
			return '{}'.format(self.codigo_inspe)


#tabla de donacion 5
class Donacion(models.Model):
		codigo_dona=models.AutoField('Codigo de Donación', primary_key=True)
		codigo_bene=models.OneToOneField(Beneficios,null=True,on_delete=models.CASCADE , unique=True)
		cedula_ings=models.CharField('Cedula del Ing supervisor de la Donación', max_length=8,unique=True)
		apellidos_ing_sup_do=models.CharField('Apellidos del Ing supervisor de la Donación', max_length=100,null=True)
		nombres_ing_sup_do=models.CharField('Nombres del Ing supervisor de la Donación', max_length=100,null=True)
		cedula_voc_sup_do=models.CharField('Cedula del Vocero supervisor de la Donación', max_length=8,unique=True)
	 	apellidos_voc_sup_do=models.CharField('Apellidos del Vocero supervisor de la Donación', max_length=100,null=True)
	 	nombres_voc_sup_do=models.CharField('Nombres del Vocero supervisor de la Donación', max_length=100,null=True)
	     	fecha_dona=models.DateField('Fecha de la Donación', max_length=100)

	   	def __str__(self):
			return '{},{}'.format(self.codigo_dona,self.fecha_dona)


#tabla de supervicion 6
class Supervision(models.Model):
	  codigo_super=models.AutoField('Codigo de la supervición', primary_key=True)
	  codigo_bene=models.OneToOneField(Beneficios,null=True,on_delete=models.CASCADE,unique=True)
	  cedula_ing_sup_do=models.CharField('Cedula del Ing supervición Donación', max_length=8,unique=True)
	  apellidos_ing_sup_do=models.CharField('Apellidos del Ing supervisor Donación', max_length=45,null=True)
	  nombres_ing_sup_do=models.CharField('Nombres del Ing supervisor de la Donación', max_length=45,null=True)
	  cedula_voc_sup_do=models.CharField('Cedula del Vocero Supervisor de la Donación', max_length=8,unique=True)
	  apellidos_voc_sup_do=models.CharField('Apellidos del Vocero Supervisor de la Donación', max_length=45,null=True)
	  nombres_voc_sup_do=models.CharField('Nombres del Vocero Supervisor de la Donación', max_length=45,null=True)
	  lugar_entre=models.CharField('Lugar de la entrega', max_length=45,null=True)
	  descrip_luga=models.TextField('Descripción del lugar de la Entrega', max_length=100,null=True,blank=True)
	  cantida_bene=models.IntegerField('Cantidad de Beneficio(s)', null=True)
	  fecha_super=models.DateField('Fecha de la supervisión', null=True)
	
	  def __str__(self):
		return '{}'.format(self.codigo_super)

#tabla de entrega 7
class Entrega(models.Model):
	 	codigo_entre=models.AutoField('Codigo de la Entrega', primary_key=True)
	 	codigo_solici=models.OneToOneField(Solicitud,null=True,on_delete=models.CASCADE,unique=True )
	 	cantidad_entrega=models.IntegerField('Cantidad de Beneficio(s) Entregado(s)' ,null=True)
	 	fecha_entrega=models.DateField('Fecha de la(s) Entrega(s)', null=True)
	 	cedula_ing=models.CharField('Cedula del Ingeniero', max_length=8,unique=True)
	 	apellidos_ing=models.CharField('Apellidos del Ingeniero' , max_length=45,null=True)
	 	nombres_ing=models.CharField('Nombres del Ingeniero', max_length=45,null=True)
	 	cedula_voc1=models.CharField('Cedula del Vocero n°1', max_length=8,unique=True)
	 	apellidos_voc1=models.CharField('Apellidos del Vocero n°1', max_length=45,null=True)
	 	nombres_voc1=models.CharField('Nombres del Vocero n°1', max_length=45,null=True)
	 	cedula_voc2=models.CharField('Cedula del Vocero n°2', max_length=8,unique=True)
	 	apellidos_voc2=models.CharField('Apellidos del Vocero n°2', max_length=45,null=True)
	 	nombres_voc2=models.CharField('Nombres del Vocero n°2', max_length=45,null=True)
	 	cedula_voc3=models.CharField('Cedula del Vocero n°3', max_length=8,unique=True)
	 	apellidos_voc3=models.CharField('Apellidos del Vocero n°3', max_length=45,null=True)
	 	nombres_voc3=models.CharField('Nombres del Vocero n°3', max_length=45,null=True)

		def __str__(self):
			return '{}'.format(self.codigo_entre)


#tabla de representante 8
class Representante(models.Model):
		codigo_representa=models.AutoField('Codigo del Representante', primary_key=True)
		cedula_escolar=models.CharField('Cedula Escolar', max_length=8,unique=True)
		codigo_hab=models.OneToOneField(Habitantes,null=True,on_delete=models.CASCADE,unique=True )
		paren_representa=models.CharField('Parentesco del Representante', max_length=45,choices=Selects().parentesco())
		
		def __str__(self):	
			return '{}'.format(self.cedula_escolar)
			
			