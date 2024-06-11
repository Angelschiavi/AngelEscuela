#trabajar con un achivo externo 
#manejo de errores 
#que tenga una funcion definida 
#holaaaaaaaaaaaaaaaaaaaaa


#---------..-------------#
#range
def ingresar(mensaje):
    """permite el ingreso de datos y valida que sea numerico"""
    while True:
        numero = input(mensaje)
        try:
            numero = int(numero)
            break
        except:
            print("Tipo de dato  incorrecto")
            continue
    return numero

def mostrar_secuencia(s):
    for iterado in s:
        print(iterado)
    return
def archivo():
    archivo = open("Secuencia.txt", "a")
    for valor in secuencia:
    #Grabar un archivo 
        archivo.write(str(valor) + "\n")
        archivo.close
    #leer el archivo
    archivo = open("Secuencia.txt", "r")
    contenido = ( archivo.readline() )
    print(contenido)
    archivo.close()
    return archivo


valor_inicial = ingresar("Ingrese el valor inicial: ")
valor_final = ingresar("Ingrese el valor final: ")
salto = ingresar("ingresar salto: ")

secuencia = range(valor_inicial, valor_final, salto)
print(secuencia)
mostrar_secuencia(secuencia)
archivo()

