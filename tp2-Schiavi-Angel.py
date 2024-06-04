from os import system
def borrar_pantalla():
    """Se borrara la pantalla"""
    system("clear")
    return
def texto1():
    """Le pedira al usuario un texto"""
    entrada = input("Ingresar primera parte de la cadena: ")
    return entrada
def texto2():
    """Le pedira al usuario otro texto"""
    entrada2 = input("ingresar segunda parte de la cadena: ")
    return entrada2
def enteros():
    """Le pedira al usuario un numero entero"""
    num = input("Ingresar un numero entero: ")
    return int(num)
def crear_lista():
    """Le pedira al usuario datos para una lista"""
    lista = input("Ingrese datos para una lista (Separada por comas):  ")
    lista = lista.split(",")
    return lista
def crear_tupla():
    """Le pedira al usuario datos para una tupla"""
    tupla = input("ingrese datos para una tupla (Separada por comas):  ")
    tupla = tuple(tupla.split(","))
    return tupla
def crear_diccionario():
    return


def mostrar_menu():
    print("¡¡¡BIENVENIDO!!!")
    print()
    print("Menu:")
    print("1. Formar una cadena")
    print("2. Hacer suma entre enteros")
    print("3. Crear una lista (separada por comas)")
    print("4. Crear una tupla (separada por comas)")
    print("5. Crear un diccionario")
    print("6. Salir")
   


diccionario = {}


while True:
    
    borrar_pantalla()
    mostrar_menu()
    print()
    opcion = input("ingresar una opcion: ")
    borrar_pantalla()
    if opcion=="1":
        resultado = texto1() + " " + texto2()
        print("La cadena quedo conformada con:", resultado)
    
        print(type(resultado))
    elif opcion=="2":
        try:
            resultado = enteros() + enteros()
            print("La suma entre numeros enteros es:", resultado)
            print(type(resultado))
        except:
            print("Formato no valido (Leer bien la consigna)")
    elif opcion=="3":
        resultado= crear_lista()
        borrar_pantalla()
        print("La lista contiene:", resultado)
        cantidad = len(resultado)
        print('la lista contiene:', cantidad ,'elementos')
        for item in resultado:
            print(item, end="")
            print()
        print(type(resultado))
    elif opcion=="4":
        resultado= crear_tupla()
        borrar_pantalla()
        print("la tupla contiene:", resultado)
        print(type(resultado))
        cantidad= len(resultado)
        print("La tupla contiene", cantidad ,"elementos")
    elif opcion=="5":
        clave= input("ingresar una clave: ")
        valor= input("ingresar valor para la clave (separado por comas):  ")
        valor = valor.split(",")
        diccionario[clave] = valor
        print(diccionario)
        contenido = len(valor)
        print("El diccionario contiene", contenido ,"elementos")
        print(type(diccionario))
    elif opcion=="6":
        print("Hasta Pronto!!!")
        break
    else:
        print("Error! seleccionar una opcion valida") 


    input("Presione Enter para continuar...")
