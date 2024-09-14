from estudiante import Estudiante
from curso import Curso

estudiante_uno = Estudiante("Juan", 18, 1213123)
estudiante_dos = Estudiante("Manuel", 24, 354636)

curso_uno = Curso("Matematicas", 2345346, "Juan Jose")
curso_dos = Curso("Fisica", 23534676, "Gerardo Ismael")
curso_tres = Curso("Dinamica", 654234, "Jose Alan")


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