from usuario.ususario import Usuario
from usuario.utils.roles import Roles

class Coordinador(Usuario):
    sueldo: float
    rfc: str
    años_antiguedad:int

    def __init__(self, numero_control: str, nombre: str, apellido: str, contraseña: str, sueldo: float, rfc: str, años_antiguedad:int):
        super().__init__(nuemro_de_control=numero_control, 
                         nombre=nombre, 
                         apellido= apellido, 
                         contraseña=contraseña, 
                         rol=Roles.COORDINADOR)
        self.sueldo=sueldo
        self.rfc=rfc
        self.años_antiguedad=años_antiguedad

    def mostrar_info_coordinador(self):
        nombre_apellido=f"{self.nombre} {self.apellido}"
        info=f"-Numero de control: {self.numero_control}\n, -Nombre completo: {nombre_apellido}\n, -Rol: {self.rol.value}\n, -Años de antiguedad: {self.años_antiguedad}"
        return info
