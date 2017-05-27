#!/usr/bin/python	
# -*- coding: utf-8 -*-
from django import forms
#from dal import autocomplete
from django.forms.widgets import TextInput
from SisconcBNB.apps.habitantes.models import Habitantes
from SisconcBNB.apps.habitantes.models import Beneficios
from SisconcBNB.apps.habitantes.models import Solicitud
from SisconcBNB.apps.habitantes.models import Inspeccion
from SisconcBNB.apps.habitantes.models import Donacion
from SisconcBNB.apps.habitantes.models import Supervision
from SisconcBNB.apps.habitantes.models import Entrega
from SisconcBNB.apps.habitantes.models import Representante
from SisconcBNB.apps.habitantes.forms_date import DateInput


class habiForm(forms.ModelForm):
	toalla_hab=forms.BooleanField(label='Toalla', required=False, initial=True)
	panal_hab=forms.BooleanField(label='Pañal', required=False, initial=True)
	class Meta:
		model = Habitantes 
		fields = [
			'cedula_hab',
			'numero_fam',
			'apellidos',
			'nombres',
			'estados',
			'municipios',
			'parroquias',
			'fecha_habi',
			'parentesco_hab',
			'cod_tel',
			'telef_hab',
			'codigo_movil',
			'movil_hab',
			'genero_hab',
			'ocupacion_hab',
			'direccion',
			'tipo_propiedad_hab',
			'correo',
			'consejoc_pert',

		]
		labels = {
			'cedula_hab':'Cedula ',
			'nombres':'Nombres',
			'apellidos':'Apellidos',
			'numero_fam':'Numero de Familia ',
			'estados':'Estado',
		    'municipios':'Municipios',
			'parroquias':'Parroquias',
			'fecha_habi':'Fecha de Nacimiento',
			'parentesco_hab':'Parentesco ',
			'cod_tel':'Codigo telefono',
			'telef_hab':'Teléfono',
			'codigo_movil':'Codigo movil',
			'movil_hab':'Movil',
			'genero_hab':'Genero',
			'ocupacion_hab':'Ocupacion',
			'direccion':'Direccion',
			'tipo_propiedad_hab':'Tipo de propiedad',
			'correo':'Correo',
			'consejoc_pert':'Sector',

		}
		widgets = {	
			'cedula_hab':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','size':'8','autocomplete': 'off'}),
			'numero_fam':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'Nombres','size':'40','autocomplete': 'off'}),
			'apellidos':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Apellidos','size':'40','autocomplete': 'off'}),
			'nombres':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Nombres','size':'40','autocomplete': 'off'}),
			'estados':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'estados','size':'40','autocomplete': 'off'}),
		    'municipios':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'municipios','size':'40','autocomplete': 'off'}),
			'parroquias':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'parroquias','size':'40','autocomplete': 'off'}),
			'fecha_habi': DateInput(format = '%Y-%m-%d'),
			'parentesco_hab':forms.Select(attrs={'class':'material-control tooltips-general'}),
			'cod_tel':forms.Select(attrs={'class':'material-control tooltips-general'}),
			'telef_hab':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'Telefono','size':'8','autocomplete': 'off'}),
			'codigo_movil':forms.Select(attrs={'class':'material-control tooltips-general'}),
			'movil_hab':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder': 'Movil','size':'8','autocomplete': 'off'}),
	    	'genero_hab': forms.Select(attrs={'class':'material-control tooltips-general','autocomplete':'off'}),
	    	'ocupacion_hab':forms.Select(attrs={'class':'material-control tooltips-general'}),
	    	'direccion':forms.Textarea(attrs={'class':'material-control tooltips-general','placeholder':'Dirección','size':'40','autocomplete': 'off'}),
	    	'tipo_propiedad_hab':forms.Select(attrs={'class':'material-control tooltips-general'}),
	    	'correo':forms.EmailInput(attrs={'class':'material-control tooltips-general','placeholder':'Correo','size':'40','autocomplete': 'off'}),
	    	'consejoc_pert':forms.Select(attrs={'class':'material-control tooltips-general'}),
	    }


	    
def cedula_hab(self):
		diccionario_limpio = self.cleaned_data
		dni = diccionario_limpio.get('cedula_hab')
		if len(cedula_hab) < 8 or len(cedula_hab) > 8:
			raise forms.ValidationError("debe ser de 8 Digitos")
		return cedula_hab



def telef_hab(self):
		diccionario_limpio = self.cleaned_data
		dni = diccionario_limpio.get('telef_hab')
		if len(telef_hab) < 8 or len(telef_hab) > 8:
			raise forms.ValidationError("debe ser de 8 Digitos")
		return telef_hab


#formulario del beneficio 2
class BenefiForm(forms.ModelForm):
	class Meta:
		model = Beneficios
		fields = [
		'codigo_bene',
		'nombre_bene',
		'descripcion_bene',
		'stock',
		'disponibilidad',
		
		]

		labels = {
		'codigo_bene':'codigo_bene',
		'nombre_bene':'Nombre del Beneficio',
		'descripcion_bene':'descripcion_bene',
		'stock':'stock',
		'disponibilidad':'disponibilidad',

		}
		widgets = 	{
		'codigo_bene':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'codigo','size':'40','autocomplete': 'off'}),
		'nombre_bene':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
        'descripcion_bene':forms.Textarea(attrs={'class':'material-control tooltips-general','placeholder':'descripcion','size':'40','autocomplete': 'off'}),
        'stock':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'stok','size':'40','autocomplete': 'off'}),
        'disponibilidad':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'disponibilidad','size':'40','autocomplete': 'off'}),
		
		}

class SolicitForm(forms.ModelForm):
  aprobado=forms.BooleanField(label='aprobado', required=True,initial=False)
  class Meta:
    model = Solicitud
    fields = [
    'codigo_solici',
    'codigo_hab',
    'codigo_bene',
    'cantidad_bene',
    #'fecha_solici',
    'cantidad_probado',
  
    ]

    labels = {
    'codigo_solici':'codigo de la solicitud',
    'codigo_hab':'codigo del habitantes',
    'codigo_bene':'codigo del beneficio',
    'cantidad_bene':'cantidad del beneficio',
    'fecha_solici':'fecha_solici',
    'cantidad_probado':'cantidad de probado',


    }

    widgets =   {
    'codigo_solici':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'codigo','size':'4','autocomplete': 'off'}),
    'codigo_hab':forms.Select(attrs={'class':'material-control tooltips-general'}),
    'codigo_bene':forms.Select(attrs={'class':'material-control tooltips-general'}),
    'cantidad_bene':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cantidad','size':'4','autocomplete': 'off'}),
    'fecha_solici': DateInput(format = '%Y-%m-%d'),
    'cantidad_probado':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'aprobado','size':'4','autocomplete': 'off'}),
    
    }

#formulario de la inspeccion 4
class InspecForm(forms.ModelForm):
    class Meta:
        model = Inspeccion
        fields = [
        'codigo_solici',
        'cedula_ing_ins',
        'apellidos_ing',
        'nombres_ing_ins',
        'cedula_voc',
        'apellidos_voc',
        'nombres_voc',
        'coodenada_uml',
        'topologia_vivienda',
        'tipo_proyecto',
        'observacion',
        'fecha_inspeccion',
        
        ]

        labels = {
        'codigo_solici':'Codigo de Solicitud',
        'cedula_ing_ins':'Cedula del ing Inspector',
        'apellidos_ing':'Apellidos del Inspector',
        'nombres_ing_ins': 'Nombres del Inspector',
        'cedula_voc':'Cédula del Vocero',
        'apellidos_voc':'apellidos del Vocero',
        'nombres_voc':'Nombres del Vocero',
        'coodenada_uml':'Coordenadas UML',
        'topologia_vivienda':'Topologia de la Vivienda',
        'tipo_proyecto':'tipo_proyecto',
        'observacion':'Observacion',
        'fecha_inspeccion':'Fecha de la Inspección',

        }


        widgets={
         'codigo_solici':forms.Select(attrs={'class':'material-control tooltips-general'}),
         'cedula_ing_ins':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','autocomplete': 'off'}),
         'apellidos_ing':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Apellidos','size':'40','autocomplete': 'off'}),
         'nombres_ing_ins':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Nombres','size':'40','autocomplete': 'off'}),
         'cedula_voc':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Cédula','size':'40','autocomplete': 'off'}),
         'apellidos_voc':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Apellidos','size':'40','autocomplete': 'off'}),
         'nombres_voc':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Nombres','size':'40','autocomplete': 'off'}),
         'coodenada_uml':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Coordenada','size':'40','autocomplete': 'off'}),
         'topologia_vivienda':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'TopologÍa','size':'40','autocomplete': 'off'}),
         'tipo_proyecto':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'Tipo de proyectos','size':'40','autocomplete': 'off'}),
         'observacion':forms.Textarea(attrs={'class':'material-control tooltips-general','placeholder':'observación','size':'40','autocomplete': 'off'}),
         'fecha_inspeccion': DateInput(format = '%Y-%m-%d'),
        }


        
#formulario  de donacion 5
class donaForm(forms.ModelForm):
	class Meta:
		model = Donacion
		fields = [
		'codigo_dona',
		'codigo_bene',
		'cedula_ings',
		'apellidos_ing_sup_do',
		'nombres_ing_sup_do',
		'cedula_voc_sup_do',
		'apellidos_voc_sup_do',
		'nombres_voc_sup_do',
		'fecha_dona',
		]

		labels = {
		'codigo_dona':'codigo_dona',
		'codigo_bene':'codigo_bene',
		'cedula_ings':'cedula_ing_sup_do',
		'apellidos_ing_sup_do':'apellidos_ing_sup_do',
		'nombres_ing_sup_do':'nombres_ing_sup_do',
		'cedula_voc_sup_do':'cedula_voc_sup_do',
		'apellidos_voc_sup_do':'apellidos_voc_sup_do',
		'nombres_voc_sup_do':'nombres_voc_sup_do',
		'fecha_dona' : 'fecha_dona',
		}

		widgets = 	{
		'codigo_dona':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'codigo','size':'40','autocomplete': 'off'}),
		'codigo_bene':forms.Select(attrs={'class':'material-control tooltips-general'}),
		'cedula_ings':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','size':'40','autocomplete': 'off'}),
        'apellidos_ing_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
        'nombres_ing_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
        'cedula_voc_sup_do':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','size':'40','autocomplete': 'off'}),
        'apellidos_voc_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
		'nombres_voc_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
		'fecha_dona' : DateInput(format = '%Y-%m-%d'),
		}

#formulario de supervicion 6
class supervForm(forms.ModelForm):
     class Meta:
          model = Supervision 
          fields = [
          'codigo_super',
          'codigo_bene',
          'cedula_ing_sup_do',
          'apellidos_ing_sup_do',
          'nombres_ing_sup_do',
          'cedula_voc_sup_do',
          'apellidos_voc_sup_do',
          'nombres_voc_sup_do',
          'lugar_entre',
          'descrip_luga',
          'cantida_bene',
          'fecha_super',
          ]

          labels = {
          'codigo_super':'codigo_super',
          'codigo_bene':'codigo_bene',
          'cedula_ing_sup_do':'cedula_ing_sup_do',
          'apellidos_ing_sup_do':'apellidos_ing_sup_do',
          'nombres_ing_sup_do':'nombres_ing_sup_do',
          'cedula_voc_sup_do':'cedula_voc_sup_do',
          'apellidos_voc_sup_do':'apellidos_voc_sup_do',
          'nombres_voc_sup_do':'nombres_voc_sup_do',
          'lugar_entre':'lugar_entre',
          'descrip_luga':'descrip_luga',
          'cantida_bene':'cantida_bene',
          'fecha_super':'fecha_super',
          }


          widgets =      {
         'codigo_super':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'codigo','size':'40','autocomplete': 'off'}),
         'codigo_bene':forms.Select(attrs={'class':'material-control tooltips-general'}),
         'cedula_ing_sup_do':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','size':'40','autocomplete': 'off'}),
         'apellidos_ing_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
         'nombres_ing_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
         'cedula_voc_sup_do':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','size':'40','autocomplete': 'off'}), 
         'apellidos_voc_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
         'nombres_voc_sup_do':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
         'lugar_entre':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'lugar','size':'40','autocomplete': 'off'}),
         'descrip_luga':forms.Textarea(attrs={'class':'material-control tooltips-general','placeholder':'descripcion','size':'40','autocomplete': 'off'}),
         'cantida_bene':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cantidad','size':'40','autocomplete': 'off'}),
         'fecha_super': DateInput(format = '%Y-%m-%d'),
          }

#formulario de entrga 7
class entregaForm(forms.ModelForm):
	class Meta:
		model = Entrega
		fields = [
		 'codigo_entre',
		 'codigo_solici',
		 'cantidad_entrega',
		 'fecha_entrega',
		 'cedula_ing',
		 'apellidos_ing',
		 'nombres_ing',
		 'cedula_voc1',
		 'apellidos_voc1',
		 'nombres_voc1',
		 'cedula_voc2',
		 'apellidos_voc2',
		 'nombres_voc2',
		 'cedula_voc3',
		 'apellidos_voc3',
		 'nombres_voc3',
		
		]

		labels = {
		'codigo_entre':'codigo_entre',
		'codigo_solici':'codigo_solici',
		'cantidad_entrega':'cantidad_entrega',
		'fecha_entrega':'fecha_entrega',
		'cedula_ing':'cedula_ing',
		'apellidos_ing':'apellidos_ing',
		'nombres_ing':'nombres_ing',
		'cedula_voc1':'cedula_voc1',
		'apellidos_voc1':'apellidos_voc1',
		'nombres_voc1':'nombres_voc1',
		'cedula_voc2':'cedula_voc2',
		'apellidos_voc2':'apellidos_voc2',
		'nombres_voc2':'nombres_voc2',
		'cedula_voc3':'cedula_voc3',
		'apellidos_voc3':'apellidos_voc3',
		'nombres_voc3':'nombres_voc3',
		
		}


		widgets = 	{
		'codigo_entre':forms.NumberInput(attrs={'class':'material-control tooltips-general','autocomplete': 'off'}),
		'codigo_solici':forms.Select(attrs={'class':'material-control tooltips-general'}),
		'cantidad_entrega':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cantidad','autocomplete': 'off'}),
		'fecha_entrega':DateInput(format = '%Y-%m-%d'),
	    'cedula_ing':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','autocomplete': 'off'}),
		'apellidos_ing':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
		'nombres_ing':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
		'cedula_voc1':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cédula','autocomplete': 'off'}),
		'apellidos_voc1':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
		'nombres_voc1':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
		'cedula_voc2':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cédula','autocomplete': 'off'}),
		'apellidos_voc2':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
		'nombres_voc2':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
		'cedula_voc3':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cédula','autocomplete': 'off'}),
		'apellidos_voc3':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'apellidos','size':'40','autocomplete': 'off'}),
		'nombres_voc3':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombres','size':'40','autocomplete': 'off'}),
		}


#formulario 8
class repreForm(forms.ModelForm):
	class Meta:
		model = Representante
		
		fields = [
		'codigo_representa',
		'cedula_escolar',
		'codigo_hab',
		'paren_representa',
		]

		labels = {
		'codigo_representa':'codigo_representa',
		'cedula_escolar':'cedula_escolar',
		'codigo_hab':'codigo_hab',
		'paren_representa':'paren_representa',
		}


		widgets = 	{
		'codigo_representa':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'codigo','size':'40','autocomplete': 'off'}),
		'cedula_escolar':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'cedula','size':'40','autocomplete': 'off'}),
		'codigo_hab':forms.Select(attrs={'class':'material-control tooltips-general','autocomplete': 'off'}),
		'paren_representa':forms.Select(attrs={'class':'material-control tooltips-general'}),

		}