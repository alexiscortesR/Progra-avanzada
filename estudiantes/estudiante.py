from datetime import datetime
from usuario.ususario import Usuario
from usuario.utils.roles import Roles

class Estudiante(Usuario): #estudiante clase hija de clase padre, usuario
    curp: str
    fecha_nacimiento: datetime          # numero_control: str
                                        # nombre: str
                                        # apellido: str

    
    # def __init__ (self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
    #     self.numero_control = numero_control
    #     self.nombre = nombre
    #     self.apellido = apellido
    #     self.curp = curp
    #     self.fecha_nacimiento = fecha_nacimiento
    
    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contraseña: str):
        
        super().__init__(numero_de_control=numero_control, 
                         nombre=nombre, 
                         apellido=apellido, 
                         contraseña=contraseña,
                            rol=Roles.ESTUDIANTE)
        self.curp=curp
        self.fecha_nacimiento=fecha_nacimiento


    def mostrar_informacion_estudiante(self):
        nombre_completo=f"{self.nombre} {self.apellido}"
        informacion = f"-Numero de control: {self.numero_control}, \nNombre completo: {nombre_completo}, \nCURP: {self.curp}, \nFecha de nacimiento: {self.fecha_nacimiento}"
        return informacion
    