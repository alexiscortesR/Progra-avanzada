from usuario.ususario import Usuario
from usuario.utils.roles import Roles

class Maestro(Usuario): #estudiante clase hija de clase padre, usuario
    # numero_control: str
    # nombre: str
    # apellido: str
    rfc: str
    sueldo: float
    
    # def __init__ (self, numero_control, nombre: str, apellido: str, rfc: str, sueldo: float):
    #     self.numero_control = numero_control
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.rfc = rfc
    #     self.sueldo = sueldo

    def __init__(self, numero_control, nombre: str, apellido: str, rfc: str, sueldo: float, contraseña: str):
        super().__init__(numero_de_control=numero_control, 
                         nombre=nombre, 
                         apellido=apellido, 
                         contraseña=contraseña, 
                         rol=Roles.MAESTRO)
        self.rfc=rfc
        self.sueldo=sueldo


    def mostrar_info_maestro(self):
        nombre_completo=f"{self.nombre} {self.apellido}"
        informacion = f"-Numero de control: {self.numero_control}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}"
        return informacion 