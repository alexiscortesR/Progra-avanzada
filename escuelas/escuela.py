from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from coordinador.coordinador import Coordinador
from usuario.ususario import Usuario
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint


class Escuela:
   lista_usuarios:List[Usuario] = []
   lista_estudiantes: List[Estudiante] = []
   lista_grupos: List[Grupo] = []
   lista_maestros: List[Maestro] = []
   lista_materias: List[Materia] = []
   lista_carreras: List[Carrera] = []
   lista_semestres: List[Semestre] = []

   #---------------------------------------------------
   def __init__(self):
       coordinador=Coordinador(
           numero_control="12345",
           nombre="Edson",
            apellido="Medina",
            rfc="MEDINA123",
            sueldo=100000,
            años_antiguedad=10,
            contraseña="123*",
       )
       self.lista_usuarios.append(coordinador)

   #---------------------------------------------------

   def registrar_estudiante(self, estudiante_regis: Estudiante):
      self.lista_estudiantes.append(estudiante_regis)
      self.lista_usuarios.append(estudiante_regis)

       
   def generar_numero_control(self):
       #L - 2024 - 09 - longitud +1 - random 0-10000
       #cadena formateada
       ano = datetime.now().year
       mes = datetime.now().month
       longitud_mas_uno = len(self.lista_estudiantes) + 1
       aleatorio = randint(0,10000)
       numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
       #numero_control = "L" + (datetime.year())str + (datetime.month())str + (len(self.lista_estudiantes) + 1)str + (randint(0,10000))str
       return numero_control
   
   def registrar_maestro(self, maestro_regis: Maestro):
      self.lista_maestros.append(maestro_regis)
      self.lista_usuarios.append(maestro_regis)

   def generar_numero_control_maestros(self, año: int, nombre: str, rfc: str):
      ano = año
      dia = datetime.now().day
      aleatorio = randint(500, 5000)
      letras_inicio = nombre [:2]
      letras_final = rfc [-2:]
      longitud_mas_uno = len(self.lista_maestros) + 1
      
      numero_control = f"M{ano}{dia}{aleatorio}{letras_inicio}{letras_final}{longitud_mas_uno}"
      return numero_control

#--------------------------------------------------------------------------------------------------------------------
   def validar_inicio_sesion(self, numero_control:str, contraseña:str):
      for usuario in self.lista_usuarios:
         if usuario.numero_control==numero_control:
             if usuario.contraseña==contraseña:
                 return usuario
      return None

#09/10
      # def validar_inicio_sesion(self, numero_control: str, contrasenia: str):
      #   for usuario in self.lista_usuarios:
      #       if usuario.numero_control == numero_control:
      #           if usuario.contrasenia == contrasenia:
      #               return usuario
                
      #   return None

#--------------------------------------------------------------------------------------------------------------------
#numero control con el 
    # siguiente formato: 
    # "MT{ultimos 2 digitos del nombre}{semestre}{cantidad creditos}{random 1, 1000}"
   def registrar_materia(self,materia_registro: Materia):
      self.lista_materias.append(materia_registro)

   def generar_numero_control_materia(self, nombre: str, semestre: int, creditos: int):
      letras_final = nombre[:-2]
      semestre= semestre
      creditos = creditos
      aleatorio = randint(1,1000)
      numero_control = f"MT{letras_final}{semestre}{creditos}{aleatorio}"
      return numero_control

   def registrar_carrera(self, carrera: Carrera):
      self.lista_carreras.append(carrera)

   def registrar_semestre(self, semestre: Semestre):
      id_carrera = semestre.id

      for carrera in self.lista_carreras:
         if carrera.matricula == id_carrera:
            carrera.registrar_semestre(semestre=semestre)
            self.lista_semestres.append(semestre)
            break
          
      
      self.lista_semestres.append(semestre)

   def registrar_grupo(self, grupo : Grupo ):
      id_semestre = grupo.id_semestre

      for semestre in self.lista_semestres:
         if id_semestre == semestre.id:
            semestre.registrar_grupo_en_semestre(grupo=grupo)
            self.lista_grupos.append()
            break

      self.lista_grupos.append(grupo)


###########################33
   def listar_estudiantes(self):
        print("\n---ESTUDIANTES---\n")
        for estudiante in self.lista_estudiantes:
            #if contraseña== contraaseña:
               #print(estudiante.mostrar_informacion_estudiante()))
            print(estudiante.mostrar_informacion_estudiante()) 

   def listar_maestros(self):
        print("\n---MAESTROS---\n")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_informacion_maestro())  

   def listar_materias(self):
        print("\n---MATERIAS---\n")
        for materia in self.lista_materias:
            print(materia.mostrar_informacion_materia())
######################33

   def listar_grupos(self):
        print("\n---GRUPOS---\n")
        i=0
        for grupo in self.lista_grupos:
            
            i+=1
            print("Grupo ", i) ##############################GRUPO
            print(grupo.mostrar_infomacion_grupo()) 


   def listar_semestres(self):
        print("\n---SEMESTRES---\n")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_infomacion_semestre())


   def listar_carreras(self):
        print("\n---CARRERAS---\n")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_infomacion_carrera())


   def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control==numero_control:
               self.lista_estudiantes.remove(estudiante)
               print("\nEstudiante eliminado con el numero de control que ingresaste")
               return
        print("\nNo se encontró estudiante")

   def eliminar_maestro(self, numero_control_maestro):
        for maestro in self.lista_maestros:
            if numero_control_maestro==maestro.numero_control:
               self.lista_maestros.remove(maestro)
               print("\nMaestro eliminado con el numero de control que ingresaste")
               return
        print("\nNo se encontró Maestro")

   def eliminar_materia(self, id_materia):
        for materia in self.lista_materias:
            if id_materia==materia.numero_control:
               self.lista_materias.remove(materia)
               print("\nMateria eliminada con el id que ingresaste")
               return
        print("\nNo se encontró la materia")
   
   def Mis_datos(self,numero_control:str,contraseña:str):
       for estudiante in self.lista_estudiantes:
            if numero_control==estudiante.numero_control:
               if contraseña==estudiante.contraseña:
                  print("\nMis datos:")
                  print(estudiante.mostrar_informacion_estudiante(),"\n")
         
   def Mis_datos_maestros(self,numero_control:str,contraseña:str):
       for maestro in self.lista_maestros:
            if numero_control==maestro.numero_control:
               if contraseña==maestro.contraseña:
                  print("\nMis datos:")
                  print(maestro.mostrar_info_maestro(),"\n")



    #---------------------------------------------------
   # def __init__(self):
   #     estudiante=Estudiante(
   #         numero_control="000",
   #         nombre="Ian",
   #          apellido="cortes",
   #          curp="CORI01",
   #          fecha_nacimiento=2004,
   #          contraseña="messi",
   #     )
   #     self.lista_usuarios.append(estudiante)

   #---------------------------------------------------