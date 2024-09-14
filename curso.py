class Curso:
    nombre_curso = ""
    codigo_curso = 0
    instructor = ""

    # metodo constructor

    def __init__(self,nombre_curso,codigo_curso,instructor):
        self.nombre_curso= nombre_curso    
        self.codigo_curso= codigo_curso    
        self.instructor= instructor     


    def mostrar_info_curso(self):
        print("Nombre del curso:", self.nombre_curso)
        print("codigo del curso:", self.codigo_curso)
        print("Instructor:", self.instructor)

