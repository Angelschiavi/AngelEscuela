from os import system
system("clear")
def borrar_pantalla():
    system ("clear")
    return
def ingresar_texto():
    """Permite que el operador ingrese un texto y lo procesa"""
    entrada = input("Introduzca un texto (Presione solo ENTER para salir): ")
    return entrada



while True:
    borrar_pantalla()
    c = ingresar_texto()
    largo = len(c)
    if largo== 0:
        break 
    c = c.upper().strip()  
    l = len(c)
    cad = "┌───"  
    print(cad * l, end="┐")
    print()
    for posicion, letra in enumerate(c):
        if posicion != l - 1:
            print("│ " + letra, end=" ")
        else:
            print("│ " + letra + " │", end="")
    print()
    print("└───" * l, end="┘")

    nada = input("Pulse ENTER para retornar: ")
