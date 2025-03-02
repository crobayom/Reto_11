
def contar_vocales (text):
    #contador de las vocales iniciado en 0 para evitar confusiones
    vocales:int=0
    #todas las vocales que pueden haber y se le suma al contador si es que esta en el caracter actual del texto
    vocales+=text.count("a")
    vocales+=text.count("e")
    vocales+=text.count("i")
    vocales+=text.count("o")
    vocales+=text.count("u")
    return vocales

def contar_consonantes (text):
    #contador de las consonantes iniciado en 0 para evitar confusiones
    consonantes:int=0
    #todas las consonantes que pueden haber y se le suma al contador si es que esta alguna en el caracter actual del texto
    consonantes+=text.count("b")
    consonantes+=text.count("c")
    consonantes+=text.count("d")
    consonantes+=text.count("f")
    consonantes+=text.count("h")
    consonantes+=text.count("j")    
    consonantes+=text.count("k")
    consonantes+=text.count("l")
    consonantes+=text.count("m")
    consonantes+=text.count("n")
    consonantes+=text.count("p")
    consonantes+=text.count("q")
    consonantes+=text.count("r")
    consonantes+=text.count("s")
    consonantes+=text.count("t")
    consonantes+=text.count("v")
    consonantes+=text.count("w")
    consonantes+=text.count("x")
    consonantes+=text.count("y")
    consonantes+=text.count("z")
    return consonantes

def palabras_repetidas(text):

    # eliminamos caracteres no deseados desde los extremos
    text = text.strip()
    # creamos una lista de palabras usando espacios como delimitadores (estandar en split)
    palabras = text.split()
    
    # organizamos en un diccionario iniciado como vacio, la frecuencia de las palabras
    frecuencia = {}
    #for que recorrera todas las cadenas separadas de palabras
    for palabra in palabras:
        # quita los caracteres extra (innecesarios y que dejan errores) de los lados de las palabras
        palabra = palabra.strip(',.!?;:')  
        # revisamos que no hayan palabras consideradas que sean vacias
        if palabra:
            #revisamos que no se repitan palabras en la cuenta (es decir definir dos veces en lguar de sumar cantidad)
            if palabra in frecuencia:
                frecuencia[palabra] += 1
            else:
                #si es la primera definicion se crea el valor
                frecuencia[palabra] = 1

    ##* esta fue la parte mas compleja 
    # se entregan ordenados los los elemtons de la lista (de diccionarios) con sorted, usando de criterio (o key)
    # para ordenarlos el numero de veces que existiera (que es valor que tiene, es decir se tiene que acceder al valor de cada llave)
    # se accede a cada valor del diccionario con una funcion que reciba cada pareja de clave valor (en la funcion lambda como una x)
    # y le indexe el valor con "[1]", por lo que revisa el valor para el criterio, no el nombre (o llave), finalmente compara los valores
    # y los organiza de manera descendente con el reverse=True, por lo que los que mas veces esten en el archivo, estaran de primeras
    palabras_mas_comunes = sorted(frecuencia.items(), key=lambda x: x[1], reverse=True)
    # se recorta la lista a los primeros 50 de la lista (o los que necesitemos) con la funcion del slicing nuevamente, pero ahora usada
    # en listas (de diccionarios en este caso)
    palabras_mas_comunes=palabras_mas_comunes[:50]
    return palabras_mas_comunes

if __name__=="__main__":
    # abre el archivo y lo iguala a una variable (que sera un string larguisimo)
    file = open("mbox.txt", "r")
    # convertimos todo el texto a minúsculas para trabajarlo sin distinguir mayúsculas y minúsculas para que solo sea una comprobacion por tipo
    text = file.read().lower()



    

    # muestra la cantidad de vocales y consonantes del archivo
    print("La cantidad de vocales en el archivo es: "+str(contar_vocales(text)))
    print("La cantidad de consonantes en el archivo es: "+str(contar_consonantes(text)))

    # crea una variable que trabajo como el regreso de la funcion
    palabras_repetidas = palabras_repetidas(text)
    
    print("Las 50 palabras más repetidas son:")
    # recorre las parejas y las imprime
    for palabra, cantidad in palabras_repetidas:
        print(str(palabra)+" : "+str(cantidad))
    
    #cierra el archivo por buena practica
    file.close()
    