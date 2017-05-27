 #!/usr/bin/python
# -*- coding: utf-8 -*-
class Selects(object):
    def __init__(self):
    #------------------------Select Religion------------------------
        self.Catolico = 'Catolico'
        self.Cristiano = 'Cristiano'
        self.Ateo = 'Ateo'
        self.nada = '---------'

        self.Manana = 'Mañana'
        self.Tarde = 'Tarde'
        self.nada = '---------'

        self.A = 'A'
        self.B = 'B'
        self.C = 'C'
        self.D = 'D'
        self.E = 'E'
        self.F = 'F'
        self.nada = '---------'


        self.primero = '1''ro.'
        self.segundo = '2''do.'
        self.tercero = '3''ro.'
        self.nada = '---------'



        self.uno = '1'
        self.dos = '2'
        self.tres = '3'
        self.cuatro = '4'
        self.cinco = '5'
        self.seies = '6'
        self.siete = '7'
        self.ocho = '8'
        self.nueve = '9'
        self.dies = '10'
        self.Otros = 'Otros'
        self.nada = '---------'


        self.vente = '20'
        self.ventiuno = '21'
        self.ventidos = '22'
        self.ventitres = '23'
        self.venticuatro = '24'
        self.venticinco = '25'
        self.ventiseis = '26'
        self.ventisiete = '27'
        self.ventiocho = '28'
        self.ventinueve = '29'
        self.treinta = '30'
        self.treintayuno = '31'
        self.treintaydos = '32'
        self.treintaytres = '33'
        self.treintaycuatro = '34'
        self.treintaycinco = '35'
        self.Otros = 'Otros'
        self.nada = '---------'



        self.qw = '2017-2018'
        self.qww = '2017-2018'
        self.qwww = '2018-2019'
        self.qwww = '2018-2019'
        self.qwww = '2019-2020'
        self.asa = '2019-2020'
        self.asaa = '2020-2021'
        self.asas = '2020-2021'
        self.saaas = '2021-2022'
        self.sasa = '2021-2022'
        self.asaasa = '2022-2023'
        self.sdsf = '2022-2023'
        self.sffsfs = '2023-2024'
        self.cacacs = '2023-2024'
        self.sxaxs = '2024-2025'
        self.awerr = '2024-2025'
        self.asasw = '2025-2026'
        self.csefg = '2025-2026'
        self.Otros = 'Otros'
        self.nada = '---------'

    def religion(self):
        return(
            (self.Catolico , 'Catolico'),
            (self.Cristiano , 'Cristiano'),
            (self.Ateo , 'Ateo'),
            (self.nada , '---------')
        )

    def turno(self):
        return(
            (self.Manana, 'Mañana'),
            (self.Tarde, 'Tarde'),
            (self.nada, '---------')           
            )

    def seccion(self):
        return(
            (self.A, 'A'),
            (self.B, 'B'),
            (self.C, 'C'),
            (self.D, 'D'),
            (self.E, 'E'),
            (self.F, 'F'),
            (self.nada, '---------')
        )
    def grado(self):
        return(
            (self.primero, '1''ro.'),
            (self.segundo, '2''do.'),
            (self.tercero, '3''ro.'),
            (self.nada, '---------')
        )
    def talla(self):
        return(
            (self.uno, '1'),
            (self.dos, '2'),
            (self.tres, '3'),
            (self.cuatro, '4'),
            (self.cinco, '5'),
            (self.seies, '6'),
            (self.siete, '7'),
            (self.ocho, '8'),
            (self.nueve, '9'),
            (self.dies, '10'),
            (self.Otros, 'Otros'),
            (self.nada , '---------')
        )

    def zapato(self):
        return(
            (self.vente, '20'),
            (self.ventiuno, '21'),
            (self.ventidos, '22'),
            (self.ventitres, '23'),
            (self.venticuatro, '24'),
            (self.venticinco, '25'),
            (self.ventiseis, '26'),
            (self.ventisiete, '27'),
            (self.ventiocho, '28'),
            (self.ventinueve, '29'),
            (self.treinta, '30'),
            (self.treintayuno, '31'),
            (self.treintaydos, '32'),
            (self.treintaytres, '33'),
            (self.treintaycuatro, '34'),
            (self.treintaycinco, '35'),
            (self.Otros, 'Otros'),
            (self.nada , '---------')
        )
    def ano_escolar(self):
        return(
            (self.qw, '2017-2018'),
            (self.qww, '2017-2018'),
            (self.qwww, '2018-2019'),
            (self.qwww, '2018-2019'),
            (self.qwww, '2019-2020'),
            (self.asa, '2019-2020'),
            (self.asaa, '2020-2021'),
            (self.asas, '2020-2021'),
            (self.saaas, '2021-2022'),
            (self.sasa, '2021-2022'),
            (self.asaasa, '2022-2023'),
            (self.sdsf, '2022-2023'),
            (self.sffsfs, '2023-2024'),
            (self.cacacs, '2023-2024'),
            (self.sxaxs, '2024-2025'),
            (self.awerr, '2024-2025'),
            (self.asasw, '2025-2026'),
            (self.csefg, '2025-2026'),
            (self.Otros, 'Otros'),
            (self.nada , '---------'),
        )