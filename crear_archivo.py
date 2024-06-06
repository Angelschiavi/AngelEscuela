archivo = open("Archivo.txt", "a")
archivo.write(input("Como estas: "))
archivo.close

archivo = open("Archivo.txt", "r")
contenido = (archivo.readline())
print("La respuesta fue:" , contenido)
archivo.close
