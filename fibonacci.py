asdasdas
#la suma de dos elementos define el siguiente 

def ingresar_tope():
    """Solicita al operado un numero para la serie de fibo"""
    numero = input("Ingresar tope: ")
    
    return int (numero) 
def fibo(n): # devuelve la serie de Fibonacci hasta un cierto limite
    sucesion = []
    a, b = 0, 1
    while a < n:
        sucesion.append(a) # ver abajo
        a, b = b, a+b
        return sucesion
#cuerpo principal del programa

t = ingresar_tope()
print(t)
rf = fibo(t)
print()

