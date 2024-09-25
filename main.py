
from escuelas.escuela import Escuela
from estudiantes.estudiante import Estudiante
from datetime import datetime
from maestros.maestro import Maestro
from materias.materia import Materia

from datetime import datetime
escuela = Escuela()

while True:
    print("""
          -----**MINDBOX**-----
          1.- Registrar Estudiante
          2.- Registrar maestro
          3.- Registrar grupo
          4.- Registrar materia
          5.- Registrar horario
          6.- Mostrar estudiantes
          7.- Mostrar maestros
          8.- Mostrar materias
          9.- Eliminar estudiante
          10.- Eliminar maestro
          11.- Eliminar materia
          12.- salir
          """)
    
    opcion = input("Ingresa una opcion para continuar: ")
    
    if opcion == "1":
        print("\nSeleccionaste la opcion para registrar un estudiante")
        
        numero_control = escuela.generar_numero_control()
        print ("Numero de Control: ", numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la curp del estudiante: ")
        ano = int(input("Ingresa el año de nacimiento del estudiante: "))
        mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
        dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
        fecha_nacimieto = datetime(ano, mes, dia)
        
        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimieto)
        escuela.registrar_estudiante(estudiante_regis=estudiante)
        
    elif opcion == "2":
        print("\nSeleccionaste la opcion para regitrar un maestro")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa la rfc del maestro: ")
        sueldo = float(input("Ingresa el sueldo del maestro: "))
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        numero_control = escuela.generar_numero_control_maestros(año=ano_nacimiento, nombre=nombre, rfc=rfc)
        print("Numero de control: ", numero_control) 
        
        maestro = Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
        escuela.registrar_maestro(maestro_regis=maestro)
        
        
    elif opcion == "3":
        pass
    elif opcion == "4":
        print("\nSeleccionaste la opcion para registrar una materia")
        nombre= input("Ingresa nombre de la materia: ")
        descripcion = input("Ingresa una pequeña descripcion: ")
        semestre = int(input("Ingresa numero de semestre: "))
        creditos = int(input("Ingresa la cantidad de creditos: "))
        numero_control= escuela.generar_numero_control_materia(nombre = nombre, semestre=semestre, creditos=creditos)
        print("Numero de control de la materia: ", numero_control)

        materia = Materia(numero_control=numero_control, nombre=nombre, descripcion=descripcion, semestre = semestre, creditos = creditos)
        
        escuela.registrar_materia(materia_registro=materia)

    elif opcion == "5":
        pass
    elif opcion == "6":
        escuela.listar_estudiantes()
    elif opcion == "7":
        escuela.listar_maestros()
    elif opcion == "8":
        escuela.listar_materias()
    elif opcion == "9":
        print("\nPara eliminar estudiante:")
        numero_control = input("\nIngresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)
    elif opcion == "10":
        print("\nPara eliminar maestro:")
        numero_control_maestro = input("\nIngresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_control_maestro= numero_control_maestro)
    elif opcion == "11":
        print("\nPara eliminar materia:")
        numero_control_materia = input("\nIngresa el numero de control o matricula de la materia: ")
        escuela.eliminar_materia(id_materia = numero_control_materia)
    elif opcion == "12":
        print("\n Hasta luego")
        break