class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante= 0
    cursos = [] 

    # metodo constructor    self.cursos = cursos if cursos is not None else []  

    def __init__(self,nombre,edad,id_estudiante,cursos=None):
        self.nombre= nombre    
        self.edad= edad    
        self.id_estudiante= id_estudiante    
        self.cursos= cursos if cursos is not None else []

    #PRIMER METODO
    def agregar_curso(self,curso):
        self.cursos.append(curso)
        

    def mostrar_informacion(self):
        print("nombre: ", self.nombre)
        print("edad: ", self.edad)
        print("id: ", self.id_estudiante)
        for curso in self.cursos:
            print(curso)
