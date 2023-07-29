import datetime

class Fecha:

    def __init__(self, año=2023, mes=7, dia=29):
        self.año = año
        self.mes = mes
        self.dia = dia

    def __repr__(self) -> str:
        return f'{self.año}/{self.mes}/{self.dia}'
    
    def compare_to(self,fecha2):
        fecha1 = datetime.datetime(self.año, self.mes, self.dia)
        fecha2 = datetime.datetime(fecha2.año, fecha2.mes, fecha2.dia)
        if fecha1 < fecha2:
            return -1
        if fecha1 == fecha2:
            return 0
        if fecha1 > fecha2:
            return 1
