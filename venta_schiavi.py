
from os import system

def borrar_pantalla():
    system("clear")

def descripcion():
    """"Le pedira al usuario una descripcion"""
    while True:
            descripciones = input("Ingresar descrpcion: ").upper()
            if descripciones==str:
                break
            elif descripciones.isdigit():
                print("Error")
                continue
            return descripciones
def cantidad():
    """Le pedira al usuario el numero de cantidad de productos"""
    while True:
        try:
            cantidad = input("Ingresar cantidad: ")
            cantidad = int(cantidad)
            for i in range(5):
                if i=="":
                    print("Proceso terminado")

            break
        except ValueError:
            print("Error")
            continue
    return cantidad
def precio_unitario():
    """Le pedira al usuario el precio por unidad"""
    while True:
        try:
            precio_unitario = input("Ingresar precio: ")
            precio_unitario = float(precio_unitario)
            break
        except ValueError:
            print("Error")
            continue
    return precio_unitario

def escribir_archivo(items):
    with open("ticket.txt", "w") as archivo:
        for valores in items:
            archivo.write(str(valores) + "\n")
            


while True:
    borrar_pantalla()
    datos_de_la_descripcion= descripcion().strip()
    datos_de_la_cantidad = cantidad()   
    datos_de_precios_unitarios =precio_unitario()
    items = ("Descripcion:",datos_de_la_descripcion ) , ("Cantidad:" ,datos_de_la_cantidad ) , ("Precio_unitario:", datos_de_precios_unitarios)
    escribir_archivo(items)
    break
    


       





    



   
    
    