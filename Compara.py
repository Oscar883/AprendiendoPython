numero1=input("Numero 1: ")
numero2=input("Numero 2: ")
salida=("Los numeros proporcionados {} y {}. {}.")
if (numero1==numero2):
    #Entra aqui si los numero capturados son iguales
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    #Condicionales anidadas, if dentro de otro if.
    #Si los numeros no son iguales.
    if numero1>numero2:
        #Reporta si el primero es mayor que el segundo
        print(salida.format(numero1, numero2, "El mayor es el primero"))
    else:
        #o de lo contrario, si el primero no es mayor al segundo
        print(salida.format(numero1, numero2, "El mayor es el segundo"))