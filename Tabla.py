numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)

#for ejecuta un bloque de codigo un numero determinado
#de veces cuando se pide que recorra un rango de
#valores. El segundo parametro de range no se incluye
#en la serie de valores. Aqui seria del 1 al 10 (11 no cuenta, es limite del rango)
for i in range(1,11):
    # i va variando a cada iteracion
    salida="{} x {} = {}"
    print(salida.format(numero,i,numero*i))
