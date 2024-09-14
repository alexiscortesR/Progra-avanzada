from estudiante import Estudiante
from curso import Curso


#self.id = random.randint(1, 1000)
estudiante_uno = Estudiante("Juan", 18, None)
estudiante_dos = Estudiante("Manuel", 24, None)

curso_uno = Curso("Matematicas", "Juan Jose", None)
curso_dos = Curso("Fisica",  "Gerardo Ismael", None)
curso_tres = Curso("Dinamica", "Jose Alan", None)


estudiante_uno.agregar_curso(curso=curso_uno)
estudiante_uno.agregar_curso(curso=curso_tres)
estudiante_dos.agregar_curso(curso=curso_dos)

estudiante_uno.mostrar_informacion()
estudiante_dos.mostrar_informacion()



# hospital.registrar_paciente(paciente=paciente)
# hospital.registrar_paciente(paciente=paciente_dos)

# FALTA ID y codigo del curso EL IMPORT
# TRES CURSOS
# DOS ESTUDIANTES