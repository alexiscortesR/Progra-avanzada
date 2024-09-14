import random
class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante= 0
    cursos = [] 

    # metodo constructor    self.cursos = cursos if cursos is not None else []  

    def __init__(self,nombre,edad,id_estudiante,cursos=None):
        self.nombre= nombre    
        self.edad= edad 
        self.id_estudiante = random.randint(1, 1000)   
        # self.id_estudiante= id_estudiante    
        self.cursos= cursos if cursos is not None else []

    #PRIMER METODO
    def agregar_curso(self,curso):
        self.cursos.append(curso)
        #print("¡¡") #esta es extra
        

    def mostrar_informacion(self): 
        print("*********DATOS DEL ESTUDIANTE*************")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Id: ", self.id_estudiante)
        for curso in self.cursos:
            curso.mostrar_info_curso()
        print("*******************")


                  
