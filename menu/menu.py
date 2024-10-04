from escuelas.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupo import Grupo
from datetime import datetime

class Menu:
    
    escuela: Escuela = Escuela()
    
    usuario_estudiante: str = "ZZZ"
    contraseña_estudiante: str = "1234"
    
    usuario_maestro: str = "GuizarBB"
    contraseña_maestro: str = "12345"
    
    def login(self):
        intentos = 0
        while intentos < 5:

            print("""
                -----BIENVENIDO-----
                Inicia sesión para continuar
                """)
            
            nombre_usuario = input("Ingresa tu nombre de usuario: ")
            contraseña_usuario = input("Ingresa tu contraseña: ")
            
            if nombre_usuario == self.usuario_estudiante:
                if contraseña_usuario == self.contraseña_estudiante:
                    self.mostrar_menu_estudiante()
                    intentos = 0
                else:
                    print("Nombre o contraseña incorrectos")
                    print("\nError, intento numero ", intentos+1)
                    intentos+=1
                    #self.contador_intentos()
                    
            elif nombre_usuario == self.usuario_maestro:
                if contraseña_usuario == self.contraseña_maestro:
                    self.mostrar_menu_maestro()
                    intentos = 0
                else:
                    print("Nombre o contraseña incorrectos")
                    print("\nError, intento numero ", intentos+1)
                    intentos+=1
                    #self.contador_intentos()
            else: 
                print("\nError, intento numero ", intentos+1)
                intentos+=1
                #self.contador_intentos(intentos)
                 
        print("Intentos máximos alcanzados, bye.")
        
    def mostrar_menu_estudiante(self):
        opcion = 0
        while opcion != 3:
            print("""------TEC DE MORELIA------
                1. Ver horarios.
                2. Ver grupos
                3. Salir""")
            opcion = input("Ingresa una opción: ")
            
            if opcion == "3":
                break
            
            
    def mostrar_menu_maestro(self):
        print("Menú Maestro")

#--------------------------------------------------------------------------------------------
    # def contador_intentos(self):
    #     intentos+=1
    #     print("\nError, intento numero ", intentos)
    #     return intentos

#---------------------------------------------------------------------------------------------------
        
    def mostrar_menu(self):
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
                    11.- Eliminar materiaa
                    12.- Registrar carrera
                    13.- Registrar semestre
                    14.- Mostrar grupos
                    15.- Mostrar semestres
                    16.- Mostrar carreras
                    
                    17.- salir
                    """)
                
                opcion = input("Ingresa una opcion para continuar: ")
                
                if opcion == "1":
                    print("\nSeleccionaste la opcion para registrar un estudiante")
                    
                    numero_control = self.escuela.generar_numero_control()
                    print ("Numero de Control: ", numero_control)
                    nombre = input("Ingresa el nombre del estudiante: ")
                    apellido = input("Ingresa el apellido del estudiante: ")
                    curp = input("Ingresa la curp del estudiante: ")
                    ano = int(input("Ingresa el año de nacimiento del estudiante: "))
                    mes = int(input("Ingresa el mes de nacimiento del estudiante: "))
                    dia = int(input("Ingresa el dia de nacimiento del estudiante: "))
                    fecha_nacimieto = datetime(ano, mes, dia)
                    
                    estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimieto)
                    self.escuela.registrar_estudiante(estudiante_regis=estudiante)
                    
                elif opcion == "2":
                    print("\nSeleccionaste la opcion para regitrar un maestro")
                    nombre = input("Ingresa el nombre del maestro: ")
                    apellido = input("Ingresa el apellido del maestro: ")
                    rfc = input("Ingresa la rfc del maestro: ")
                    sueldo = float(input("Ingresa el sueldo del maestro: "))
                    ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
                    numero_control = self.self.escuela.generar_numero_control_maestros(año=ano_nacimiento, nombre=nombre, rfc=rfc)
                    print("Numero de control: ", numero_control) 
                    
                    maestro = Maestro(numero_control=numero_control, nombre=nombre, apellido=apellido, rfc=rfc, sueldo=sueldo)
                    self.escuela.registrar_maestro(maestro_regis=maestro)
                    
                    
                elif opcion == "3":
                    print("\nSeleccionaste la opcion para registrar un grupo")
                    tipo = input("Ingresa el tipo de grupo A o B ")
                    id_semestre = input("ingresa el ID del semestre al que pertenece el grupo ")

                    grupo = Grupo(tipo = tipo, id_semestre=id_semestre)
                    self.escuela.registrar_grupo(grupo=grupo)

                elif opcion == "4":
                    print("\nSeleccionaste la opcion para registrar una materia")
                    nombre= input("Ingresa nombre de la materia: ")
                    descripcion = input("Ingresa una pequeña descripcion: ")
                    semestre = int(input("Ingresa numero de semestre: "))
                    creditos = int(input("Ingresa la cantidad de creditos: "))
                    numero_control= self.escuela.generar_numero_control_materia(nombre = nombre, semestre=semestre, creditos=creditos)
                    print("Numero de control de la materia: ", numero_control)

                    materia = Materia(numero_control=numero_control, nombre=nombre, descripcion=descripcion, semestre = semestre, creditos = creditos)
                    
                    self.escuela.registrar_materia(materia_registro=materia)

                elif opcion == "5":
                    pass
                elif opcion == "6":
                    self.escuela.listar_estudiantes()

                elif opcion == "7":
                    self.escuela.listar_maestros()

                elif opcion == "8":
                    self.escuela.listar_materias()

                elif opcion == "9":
                    print("\nPara eliminar estudiante:")
                    numero_control = input("\nIngresa el numero de control del estudiante: ")
                    self.escuela.eliminar_estudiante(numero_control=numero_control)

                elif opcion == "10":
                    print("\nPara eliminar maestro:")
                    numero_control_maestro = input("\nIngresa el numero de control del maestro: ")
                    self.escuela.eliminar_maestro(numero_control_maestro= numero_control_maestro)

                elif opcion == "11":
                    print("\nPara eliminar materia:")
                    numero_control_materia = input("\nIngresa el numero de control o matricula de la materia: ")
                    self.escuela.eliminar_materia(id_materia = numero_control_materia)

                elif opcion == "12":
                    print("\nSeleccionaste la opcion para registrar un carrera")
                    nombre = input("Ingresa nombre de la carrera: ")
                    carrera = Carrera(nombre=nombre )
                    self.escuela.registrar_carrera(carrera=carrera)

                elif opcion == "13":
                    print("\nSeleccionaste la opcion para registrar un semestre")
                    numero = input("Ingresa numero del semestre ")
                    id_carrera = input("Ingresa id de la carrera ")
                    semestre= Semestre(numero= numero, id_carrera= id_carrera)
                    self.escuela.registrar_semestre(semestre=semestre)

                elif opcion == "14":
                    print("\nSeleccionaste la opcion para Mostrar los grupos")
                    self.escuela.listar_grupos()

                elif opcion == "15":
                    print("\nSeleccionaste la opcion para Mostrar los semestres")
                    self.escuela.listar_semestres()
                elif opcion == "16":
                    print("\nSeleccionaste la opcion para Mostrar las carreras")
                    self.escuela.listar_carreras()

                elif opcion == "17":
                    print("\n Hasta luego")
                    break