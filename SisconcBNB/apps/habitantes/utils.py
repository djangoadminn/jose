 #!/usr/bin/python
# -*- coding: utf-8 -*-
class Selects(object):
    def __init__(self):
    #------------------------Select Parentesco------------------------
        self.Madre = 'Madre'
        self.Padre = 'Padre'
        self.Hijoa = 'Hijo(a)'
        self.Tioa = 'Tio(a)'
        self.Hermanoa = 'Hermano(a)'
        self.Abueloa = 'Abuelo(a)'
        self.Otroa = 'Otro(a)'
        self.nada = '---------'

    #------------------------Select Ocupación------------------------
        self.Comerciante = 'Comerciante'
        self.Barbero = 'Barbero'
        self.Estudiante = 'Estudiante'
        self.Empleadoa ='Empleado(a)'
        self.Jubiladoa = 'Jubilado(a)'
        self.Tecnico = 'Tecnico'
        self.Pensionadoa = 'Pensionado(a)'
        self.Obreroa = 'Obrero(a)'
        self.Educadora = 'Educador(a)'  
        self.Pastora = 'Pastor(a)'
        self.Herrero ='Herrero'
        self.Maternal ='Maternal'
        self.Soldador ='Soldador'
        self.Estilita ='Estilita'
        self.Manicurista ='Manicurista'
        self.Amao_de_casa ='Ama(o) de casa'
        self.Nutricionista ='Nutricionista'
        self.Obreroa_Educacional ='Obrero(a) Educacional'
        self.Contador ='Contador'
        self.Cocineroa ='Cocinero(a)'
        self.Policia ='Policia'
        self.Administradorar ='Administrador(ar)'
        self.Promotora_Social ='Promotor(a) Social'
        self.Docente ='Docente'
        self.Custodio ='Custodio'
        self.Pencionadoa ='Pencionado(a)'
        self.Mecanico ='Mecanico'
        self.Abogadoa ='Abogado(a)'
        self.Chofer ='Chofer'
        self.Empleadoa_Publico ='Empleado(a) Publico'
        self.Laboratorista ='Laboratorista'
        self.Peluqueroa ='Peluquero(a)'
        self.Educadora ='Educador(a)'
        self.Agricultora ='Agricultor(a)'
        self.TSU ='TSU'
        self.Enfermeroa ='Enfermero(a)'
        self.Carpinteroa ='Carpintero(a)'
        self.Ambientalista ='Ambientalista'
        self.Militar ='Militar'
        self.Albanil ='Albañil'
        self.Secretariao ='Secretaria(o)'
        self.Deportista ='Deportista'
        self.Vigilante ='Vigilante'
        self.Costurera ='Costurera'
        self.Discapacidad ='Discapacidad'
        self.Camarerao ='Camarera(o)'
        self.Luc_social ='Luc. social'
        self.Ejecutivoa_Bancaria ='Ejecutivo(a) Bancaria'
        self.Otroa ='Otros(as)'
        self.nada = '---------'


        #------------------------Select Codigo del Telelefono------------------------
        
        self.Pcasa = '0257'
        self.nada = '---------'

        #------------------------Select Codigo del Movil------------------------

        self.Movilnet = '0426'
        self.Movilnet2 = '0416'
        self.Movistar = '0424'
        self.Movistar2 = '0414'
        self.Digitel = '0412'
        self.nada = '---------'

        #------------------------Select Genero------------------------

        self.Masculino = 'M'
        self.Femenino   = 'F'
        self.nada = '---------'

        #------------------------Select Propiedad------------------------

        self.Propia = 'Propia'
        self.Arquilada = 'Arquilada'
        self.nada = '---------'

        #------------------------Select Consejo comunal que pertenece------------------------

        self.uno = '1'
        self.dos = '2'
        self.nada = '---------'

    def parentesco(self):
        return (
            (self.Madre, 'Madre'),
            (self.Padre, 'Padre'),
            (self.Hijoa, 'Hijo(a)'),
            (self.Tioa, 'Tio(a)'),
            (self.Hermanoa, 'Hermano(a)'),
            (self.Abueloa, 'Abuelo(a)'),
            (self.Otroa, 'Otros(as)'),
            (self.nada , '---------')
            )
    def ocupacion(self):
        return (
            (self.Comerciante, 'Comerciante'),
            (self.Barbero,'Barbero'),
            (self.Estudiante,'Estudiante'),
            (self.Empleadoa,'Empleado(a)'),
            (self.Jubiladoa,'Jubilado(a)'),
            (self.Tecnico,'Tecnico'),
            (self.Pensionadoa,'Pensionado(a)'),
            (self.Obreroa,'Obrero(a)'),
            (self.Educadora,'Educador(a)'), 
            (self.Pastora,'Pastor(a)'),
            (self.Herrero,'Herrero'),
            (self.Maternal,'Maternal'),
            (self.Soldador,'Soldador'),
            (self.Estilita,'Estilita'),
            (self.Manicurista,'Manicurista'),
            (self.Amao_de_casa,'Ama(o) de casa'),
            (self.Nutricionista,'Nutricionista'),
            (self.Obreroa_Educacional,'Obrero(a) Educacional'),
            (self.Contador,'Contador'),
            (self.Cocineroa,'Cocinero(a)'),
            (self.Policia,'Policia'),
            (self.Administradorar,'Administrador(ar)'),
            (self.Promotora_Social,'Promotor(a) Social'),
            (self.Docente,'Docente'),
            (self.Custodio,'Custodio'),
            (self.Pencionadoa,'Pencionado(a)'),
            (self.Mecanico,'Mecanico'),
            (self.Abogadoa,'Abogado(a)'),
            (self.Chofer,'Chofer'),
            (self.Empleadoa_Publico,'Empleado(a) Publico'),
            (self.Laboratorista,'Laboratorista'),
            (self.Peluqueroa,'Peluquero(a)'),
            (self.Educadora,'Educador(a)'),
            (self.Agricultora,'Agricultor(a)'),
            (self.TSU,'TSU'),
            (self.Enfermeroa,'Enfermero(a)'),
            (self.Carpinteroa,'Carpintero(a)'),
            (self.Ambientalista,'Ambientalista'),
            (self.Militar,'Militar'),
            (self.Albanil,'Albañil'),
            (self.Secretariao,'Secretaria(o)'),
            (self.Deportista,'Deportista'),
            (self.Vigilante,'Vigilante'),
            (self.Costurera,'Costurera'),
            (self.Discapacidad,'Discapacidad'),
            (self.Camarerao,'Camarera(o)'),
            (self.Luc_social,'Luc. social'),
            (self.Ejecutivoa_Bancaria,'Ejecutivo(a) Bancaria'),
            (self.Otroa,'Otros(as)'),
            (self.nada , '---------')
        )



    def telefono(self):
        return(
            (self.Pcasa, '0257'),
            (self.nada , '---------')
        )

    def movil(self):
        return(
            (self.Movilnet, '0426'),
            (self.Movilnet2, '0416'),
            (self.Movistar, '0424'),
            (self.Movistar2, '0414'),
            (self.Digitel, '0412'),
            (self.nada , '---------')
        )
    def genero(self):
        return(
            (self.Masculino, 'M'),
            (self.Femenino, 'F'),
            (self.nada , '---------')
        )

    def propiedad(self):
        return(
            (self.Propia, 'Propia'),
            (self.Arquilada , 'Arquilada'),
            (self.nada , '---------')
        )
    def consejocomunal(self):
        return(
            (self.uno, '1'),
            (self.dos, '2'),
            (self.nada , '---------')
            )