#Logistica y estrucura 1ra clase en visual studio code 
#cartelito

#primero introduzco el el texto 
while True:
    cartel= input("Introduzca el texto (Presione ENTER para salir): ")
    if not cartel:
            break
    largo = len(cartel)
    cartel = cartel.upper().strip()
    print("+---+" * largo)
    for letras in cartel:
         print("‖ "+letras+ "  ", end="")
    print("‖")
    print("+---+" * largo)
from os import system
system("clear")