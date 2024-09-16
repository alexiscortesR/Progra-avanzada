
from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2006, 70, 1.90, "Avenida Madero") # 5
paciente_3 = Paciente("Jake", 2002, 80, 1.89, "Avenida Celaya") # 5
paciente_4 = Paciente("Thiago", 2007, 76, 1.70, "Avenida morelos") # 5
paciente_5 = Paciente("Sam", 2012, 87, 1.94, "Avenida Lomas") # 5

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8
medico_2 = Medico("Fidel", 1999, "KLF4687BHHUDO", "Av. Monterrey") # 8
medico_3 = Medico("Angel", 1994, "FGH4815BJKDF", "Av. Quinceo") # 8
medico_4 = Medico("Jorge", 1989, "ACB4843TYDUDF", "Av. Diezmo") # 8

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_3)
hospital.registrar_paciente(paciente=paciente_4)
hospital.registrar_paciente(paciente=paciente_5)

hospital.registrar_medico(medico=medico)
hospital.registrar_medico(medico=medico_2)
hospital.registrar_medico(medico=medico_3)
hospital.registrar_medico(medico=medico_4)

hospital.mostrar_pacientes()
hospital.mostrar_medicos()
hospital.mostrar_pacientes_menores()
hospital.mostrar_pacientes_mayores()

id_a_eliminar = int(input("\nId del PACIENTES a eliminar: "))
hospital.eliminar_paciente(id_a_eliminar)

id_a_eliminar_medico = int(input("\nId del MEDICO a eliminar: "))
hospital.eliminar_medico(id_a_eliminar_medico)

#hospital.registrar_consulta(id_paciente=1, id_medico=1)

