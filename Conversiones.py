#Declaramos variable str, con cadena de numeros.
numero = "1234"
#Se MUESTRA el tipo de variable ,
# type = da un dato type, no un str(<class 'str'>).
print(type(numero))
#Convertimos la cadena a int.
numero=int(numero)
#Se MUESTRA como el tipo ha cambiado,
#aunque se usa la misma variable (<class 'int'>).
print(type(numero))
#Se declara un str con meta sustitucion
#(posiciones donde iran valores usando format).
salida="El numero utilizado es {}"
#Se MUESTRA el resultado. La meta sustitucion hara que donde
#donde esta {} se coloque el valor de la variable numero, (El numero utilizado es 1234).
print(salida.format(numero))
