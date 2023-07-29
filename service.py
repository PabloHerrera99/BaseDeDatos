from persona import Persona
from fecha import Fecha
from base import Base

class Service:

    def __init__(self) -> None:
        self.service = []

    def add(self, persona, base):
        base.data[persona.id] = persona

    def order_by_fecha(self, base):
        ord = []
        for i in base.data.values():
            ord.append(i)
        for i in range(len(ord)):
            for j in range(len(ord)):
                if ord[i].fecha.compare_to(ord[j].fecha) == -1:
                    ord[i],ord[j] = ord[j],ord[i]
        return ord
    def order_by_apellido(self, base):
        ord = []
        for i in base.data.values():
            ord.append(i)
        for i in range(len(ord)):
            for j in range(len(ord)):
                if ord[i].nombre < ord[j].nombre:
                    ord[i],ord[j] = ord[j],ord[i]
        return ord
