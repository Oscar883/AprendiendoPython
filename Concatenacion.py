#Se declaran dos variables con input para ingresar la informacion
#necesaria en este caso nombre y apellido
nombre=input("Nombre:")
apellidos=input("Apellidos:")
#Se concatenan los valores str, junto con la literal " " (para tomar un espacio)
NombreCompleto=nombre+" "+apellidos
#Se asigna a la variable la representacion en mayusculas
#de lo que contenia (Nombre/Apellidos)
NombreCompleto=NombreCompleto.upper()
print(NombreCompleto)