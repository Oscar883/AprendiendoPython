#python posee muchas librerias listas para utilizarse.
#A dichas librerias se les da el nombre de modules (module),
#para utilizar un modulo en un programa, primero debe
#importarse, usando la instruccion import
import random

#Se define variable (float) y se le asiga valor
num1=float(10.5)

#Una funcion es un conjunto de intrucciones que procesan
#una tarea especifica, como una unidad de ejecucion.
#Se declara con (def). Todo el codigo posicionado a la derecha
#de la definicion (identado), forma parte de la funcion.
def FunRandom():
    #Se convierte a float el numero aleatorio generado por
    #random.randrange() (solo esta disponible si se importa
    # el modulo random)
    num2=float(random.randrange(1,10))
    #Se utilizan meta sustituciones para mostrar resultados
    mensaje="La suma de {} y {} es {}"
    #({}=num1, {}=num2, {}=num1+num2)
    print(mensaje.format(num1,num2,num1+num2))

#Finalmente se ejecuta la funcion en el codigo
FunRandom()