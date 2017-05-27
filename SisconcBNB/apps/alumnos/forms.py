#!/usr/bin/python   
# -*- coding: utf-8 -*-
from django import forms
from SisconcBNB.apps.alumnos.models import Alumno
from SisconcBNB.apps.alumnos.models import Seccion
from SisconcBNB.apps.alumnos.models import Inscripcion
from SisconcBNB.apps.alumnos.models import Enfermedad
from SisconcBNB.apps.alumnos.models import Enfermedad_alumno
from SisconcBNB.apps.alumnos.models import Profesor
from SisconcBNB.apps.alumnos.models import Seccion_profesor
from SisconcBNB.apps.alumnos.forms_date import DateInput

#formulario del alumno 1
class alumnForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
        'codigo_hab',
        'cedula_escolar',
        'procedencia_alumn',
        'plantel_retiro_alumn',
        'lugar_habi_alumn',
        'punto_referencia_alumn',
        'religion',
        ]

        labels = {
        'codigo_hab':'codigo_hab',
        'cedula_escolar':'cedula_escolar',
        'procedencia_alumn':'procedencia_alumn',
        'plantel_retiro_alumn':'plantel_retiro_alumn',
        'lugar_habi_alumn':'Lugar_habi_alumn',
        'punto_referencia_alumn':'punto_referencia_alumn',
        'religion':'religion',
        }


        widgets = {
        'codigo_hab':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'cedula_escolar':forms.Select(attrs={'class':'material-control tooltips-general','autocomplete': 'off'}),
        'procedencia_alumn':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'procedencia','size':'40','autocomplete': 'off'}),
        'plantel_retiro_alumn':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'plantel','size':'40','autocomplete': 'off'}),
        'lugar_habi_alumn':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'lugar','size':'40','autocomplete': 'off'}),
        'punto_referencia_alumn':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'punto de referencia','size':'40','autocomplete': 'off'}),
        'religion':forms.Select(attrs={'class':'material-control tooltips-general'}),
        }

#formulario  de seccion 2 
class seccForm(forms.ModelForm):
  class Meta:
        model = Seccion
        fields = [
        'codigo_seccion',
        'turno',
        'seccion',
        'grado',
        ]

        labels = {
        'codigo_seccion':'codigo_seccion',
        'turno':'turno',
        'seccion':'seccion',
        'grado':'grado',
       
        }


        widgets =   {
        'codigo_seccion':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'codigo','size':'40','autocomplete': 'off'}),
        'turno':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'seccion':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'grado':forms.Select(attrs={'class':'material-control tooltips-general'}),
        }
 
#formulario de inscripcion 3
class inscripForm(forms.ModelForm):
    beca_estudiantil=forms.BooleanField(label='beca_estudiantil', required=True,initial=False)
    class Meta:
        model = Inscripcion
        fields = [
        'cod_inscri',
        'cedula_escolar',
        'codigo_seccion',
        'talla_pantalon',
        'talla_franela',
        'talla_Zapato',
        'beca_estudiantil',
        'ano_escolar',
        
        ]

        labels = {
        'cod_inscri':'cod_inscri',
        'cedula_escolar':'cedula_escolar',
        'codigo_seccion':'codigo_seccion',
        'talla_pantalon':'talla_pantalon',
        'talla_franela':'talla_franela',
        'talla_Zapato':'talla_Zapato',
        'beca_estudiantil':'beca_estudiantil',
        'ano_escolar':'ano_escolar',

        }


        widgets =   {
        'cod_inscri':forms.NumberInput(attrs={'class':'material-control tooltips-general'}),
        'cedula_escolar':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'codigo_seccion':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'talla_pantalon':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'talla_franela':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'talla_Zapato':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'ano_escolar':forms.Select(attrs={'class':'material-control tooltips-general'}),
        
        }

#enfermedad de alumno 4
class enferForm(forms.ModelForm):
    class Meta:
        model = Enfermedad
        fields = [
        'codigo_enfermedad',
        'nombres_enfermedad',
        'descripcion_enfermedad',
        
        ]

        labels = {
        'codigo_enfermedad':'codigo_enfermedad',
        'nombres_enfermedad':'nombres_enfermedad',
        'descripcion_enfermedad':'descripcion_enfermedad',
        

        }


        widgets =   {
        'codigo_enfermedad':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'código','size':'40','autocomplete': 'off'}),
        'nombres_enfermedad':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'nombre de la enfermedad','size':'40','autocomplete': 'off'}),
        'descripcion_enfermedad':forms.Textarea(attrs={'class':'material-control tooltips-general','placeholder':'descripción','size':'40','autocomplete': 'off'}),
        
        }

#formulario del alumnos 5
class enfermalumnForm(forms.ModelForm):
    #fecha_enfer=forms.DateField()
    class Meta:
        model = Enfermedad_alumno
        
        fields = [
        'cedula_escolar',
        'codigo_enfermedad',
        'fecha_enfer',
        ]

        labels = {
        'cedula_escolar':'cedula_escolar',
        'codigo_enfermedad':'codigo_enfermedad',
        'fecha_enfer':'fecha_enfer',
        }


        widgets =   {
        'cedula_escolar':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'codigo_enfermedad':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'fecha_enfer': DateInput(format = '%Y-%m-%d'),
        }

#formulario del pofesor 6
class profeForm(forms.ModelForm):
  class Meta:
        model = Profesor
    
        fields = [
        #'codigo_prof',
        'codigo_hab',
        'turno',
        'especialidad_prof',
        'fecha_ingreso',
        ]

        labels = {
        #'codigo_prof':'codigo_prof',
        'codigo_hab':'codigo_hab',
        'turno':'turno',
        'especialidad_prof':'especialidad_prof',
        'fecha_ingreso':'fecha_ingreso',
        }


        widgets =   {
        'codigo_prof':forms.NumberInput(attrs={'class':'material-control tooltips-general','placeholder':'codigo','size':'40','autocomplete': 'off'}),
        'codigo_hab':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'turno':forms.Select(attrs={'class':'material-control tooltips-general'}),
        'especialidad_prof':forms.TextInput(attrs={'class':'material-control tooltips-general','placeholder':'especialidad','size':'40','autocomplete': 'off'}),
        'fecha_ingreso':DateInput(format = '%Y-%m-%d'),
        }
 
#formulario de la seccion de profesor 7
class seccproForm(forms.ModelForm):
  class Meta:
        model = Seccion_profesor
        fields = [
        'codigo_prof',
        'codigo_seccion',
        ]

        labels = {
        'codigo_prof':'codigo_prof',
        'codigo_seccion':'codigo_seccion',
       
        }


        widgets =   {
        'codigo_prof':forms.Select(attrs={'class':'material-control tooltips-general','autocomplete': 'off'}),
        'codigo_seccion':forms.Select(attrs={'class':'material-control tooltips-general','autocomplete': 'off'}),
        }