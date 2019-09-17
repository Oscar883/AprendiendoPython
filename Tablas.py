for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    #print sin argumentos es un salto de linea
    print()
    for j in range(1,11):
        #Aqui i contiene el numero base de la tabla
        #y j el elemento de la tabla
        salida="{} x {} = {}"
        print(salida.format(i,j,i*j))
    else:
        #Al concluir con las iteraciones indicadas
        #se ejecuta este codigo, que es un salto de linea
        print()