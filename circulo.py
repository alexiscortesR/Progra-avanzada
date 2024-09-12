import math
class Circulo:
    
    radio = 0
    
    #METODO CONSTRUCTOR
    def __init__(self,radio):
        self.radio = radio

    #PRIMER METODO. COMENTAR TODO CTRL CK
    # def mostrar_info(self):
    #     print("Radio: ", self.radio)

    def calcular_Area(self):
        
        area= math.pi* self.radio ** 2
        print("Area: ", area)

    def calcular_perimetro(self):
        perimetro = math.pi *2* self.radio
        print("Perimetro: ", perimetro)

    