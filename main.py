import tkinter as tk
from productos import Producto
from excepciones import ErrorNombreDeProducto, ErrorPrecioDeProducto, ErrorCantidadDeProducto
from typing import List

lista_productos: List[Producto]= []

def registrar():
    global producto
    
    try:
        nombre=str(entry_producto.get())
        precio=float(entry_precio.get())
        cantidad=int(entry_cantidad.get())
        if(nombre == ""):
            raise ErrorNombreDeProducto
        elif(precio <= 0):
            raise ErrorPrecioDeProducto
        elif(cantidad < 0):
            raise ErrorCantidadDeProducto
        
        producto=Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        lista_productos.append(producto)

        label_mensaje.config(text="Producto registrado", bg="#a2fdb1")

    except ErrorNombreDeProducto as error_nombre:
        label_mensaje.config(text=error_nombre, bg="#ff7272")
    except ErrorPrecioDeProducto as error_precio:
        label_mensaje.config(text=error_precio, bg="#ff7272")
    except ErrorCantidadDeProducto as error_cantidad:
        label_mensaje.config(text=error_cantidad, bg="#ff7272")
    except ValueError:
        label_mensaje.config(text="Ingresaste un valor no valido", bg="#ff7271")

def mostrar_precio_total():
    precio_total=0
    for producto in lista_productos:
        precio_total=precio_total + producto.calcular_valor_total()
    label_mensaje.config(text=f"Precio total en inventario: ${precio_total}", bg="#a2fdb1")

def detalles_producto():
    try:
        label_mensaje.config(text=producto.mostrar_detalles(), bg="#a2fdb1")
    except NameError:
        label_mensaje.config(text="Producto no registrado", bg="#ff7272")

ventana=tk.Tk()
ventana.title("Inventario")
ventana.geometry("400x400")
ventana.config(bg="sky blue")


label_titulo = tk.Label(ventana, text="Gestion de productos", bg="yellow", fg="black")
label_titulo.pack(pady=5)


label_producto = tk.Label(ventana, text="Nombre del producto", bg="red", fg="black")
label_producto.pack(pady=5)
entry_producto = tk.Entry(ventana)
entry_producto.pack(pady=5)


label_precio = tk.Label(ventana, text="Precio del producto", bg="red", fg="black")
label_precio.pack(pady=5)
entry_precio = tk.Entry(ventana)
entry_precio.pack(pady=5)


label_cantidad = tk.Label(ventana, text="Cantidad en inventario", bg="red",fg="black")
label_cantidad.pack(pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.pack(pady=5)


boton_registrar = tk.Button(ventana, text="Registro producto", bg="green", fg="white", command=registrar)
boton_registrar.pack(pady=10)


boton_precio_total = tk.Button(ventana, text="Precio total en inventario", bg="green", fg="white", command=mostrar_precio_total)
boton_precio_total.pack(pady=10)


boton_detalles_producto = tk.Button(ventana, text="Detalles del producto", bg="green", fg="white", command=detalles_producto)
boton_detalles_producto.pack(pady=10)


label_mensaje=tk.Label(ventana, text="", bg="#a2fdb1", fg="black")
label_mensaje.pack(pady=5)


ventana.mainloop()
