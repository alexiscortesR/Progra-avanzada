class Hospital:
    pacientes = []
    medicos = []
    consultas = []

    def registrar_consulta(self, id_paciente, id_medico):
        if not self.validar_cantidad_usuarios():
            return
        
        if self.validar_existencia_paciente(id_paciente) == False or self.validar_existencia_medico(id_medico) == False:
            print("No se puede registrar la consulta, no existe el médico o el paciente")
            return
        
        print("Continuamos con el registro")

    def registrar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def registrar_medico(self, medico):
        self.medicos.append(medico)

    def mostrar_pacientes(self):
        print("\n*** Pacientes en el Sistema ***")
        for paciente in self.pacientes:
            paciente.mostrar_informacion()
    

    def mostrar_pacientes_menores(self):            ###############################AÑADIDA
        print("\n*** Pacientes Menores de edad ***")
        for paciente in self.pacientes:
            if paciente.ano_nacimiento >= 2007: #para acceder a un atributo
                paciente.mostrar_informacion()
                print("Es menor de edad")
    
    
    def mostrar_pacientes_mayores(self):            ###############################AÑADIDA
        print("\n*** Pacientes Mayores de edad ***")
        for paciente in self.pacientes:
            if paciente.ano_nacimiento <= 2006: #para acceder a un atributo
                paciente.mostrar_informacion()
                print("Es mayor de edad")


    def mostrar_medicos(self):              ###############################AÑADIDA
        print("\n*** Medicos en el Sistema ***")
        for medico in self.medicos:
            medico.mostrar_informacion_medico()


    def eliminar_paciente(self,id_a_eliminar):#################################3
        for paciente in self.pacientes:
            if paciente.id == id_a_eliminar:
                self.pacientes.remove(paciente)
                print("\nSe eliminó el paciente con id: ", id_a_eliminar)
                break

    def eliminar_medico(self,id_a_eliminar_medico):#################################3
        for medico in self.medicos:
            if medico.id == id_a_eliminar_medico:
                self.medicos.remove(medico)
                print("\nSe eliminó el medico con id: ", id_a_eliminar_medico)
                break


    def validar_existencia_paciente(self, id_paciente):
        for paciente in self.pacientes:
            if paciente.id == id_paciente:
                return True
  
        return False
    
    def validar_existencia_medico(self, id_medico):
        for medico in self.medicos:
            if medico.id == id_medico:
                return True
            
        return False
        
    def validar_cantidad_usuarios(self):
        if len(self.pacientes) == 0:
            print("No puedes registra una consulta, no existen pacientes")
            return False
        
        if len(self.medicos) == 0:
            print("No puedes registra una consulta, no existen médicos")
            return False
        
        return True

