class ErrorNombreDeProducto(Exception):
    def __init__(self):
        self.mensaje="Error, No ingresaste el nombre del producto"
        super().__init__(self.mensaje)

class ErrorPrecioDeProducto(Exception):
    def __init__(self):
        self.mensaje="Error, Ingresaste un precio negativo o cero"
        super().__init__(self.mensaje)

class ErrorCantidadDeProducto(Exception):
    def __init__(self):
        self.mensaje="Error, Ingresaste una cantidad de producto negativa"
        super().__init__(self.mensaje)