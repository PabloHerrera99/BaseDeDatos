class Persona:

    def __init__(self, id, nombre, fecha) -> None:
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
    
    def __repr__(self) -> str:
        return f'{self.id} : {self.nombre}'