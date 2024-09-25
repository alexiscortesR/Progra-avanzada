class Materia:
    numero_control: str
    nombre: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__ (self, numero_control, nombre: str , descripcion: str, semestre: int, creditos: int):
        self.numero_control = numero_control
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre 
        self.creditoa = creditos

    def mostrar_info_materia(self):
        informacion = f"-Id: {self.numero_control}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Semestre: {self.semestre}, Creditos: {self.creditoa}"
        return informacion
    