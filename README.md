# Reto_11

## 1. Consulte que hacen los siguientes métodos de strings en python: 

### endswith

Es una funcion definida para strings, la cual, recibe un string que busca al final en algun otro string, esto lo hace tambien con la posibilidad de definir el rango en el que se buscara de la siguiente manera

cadena_a_la_que_se_le_hara_la_verificacion.endswith(cadena_a_buscar_al_final, indice_inicio, indice_final)

tambien es posible solo especificar la cadena a buscar y el tomara por defecto toda la longitud de la cadena


```python
estring="cadena de caracteres"
print(estring.endswith(caracteres, 3, 20)) #True
print(estring.endswith(caracteres, 3, 18)) #False
```

### startswith

Es una funcion definida para strings, la cual, recibe un string que busca al inicio en algun otro string, esto lo hace tambien con la posibilidad de definir el rango en el que se buscara de la siguiente manera

cadena_a_la_que_se_le_hara_la_verificacion.endswith(cadena_a_buscar_al_inicio, indice_inicio, indice_final)

tambien es posible solo especificar la cadena a buscar y el tomara por defecto toda la longitud de la cadena

```python
estring="cadena de caracteres"
print(estring.endswith(cadena, 0, 18)) #True
print(estring.endswith(caracteres, 3, 18)) #False
```

### isalpha

Es una funcion definida para strings, la cual, recibe un string al que le hara la comprobacion que este escrito unicamente a partir de caracteres alfabeticos

```python
estring="cadena de caracteres"
otro_estring="otracadenadecaracteres"
print(estring.isalpha()) #False
print(otro_estring.isalpha()) #True
```

### isalnum

Es una funcion definida para strings, la cual recibe un string al que le hara la comprobacion de que este escrito unicamente a partir de caracteres alfanumericos

```python
estring="cadenadecaracteres@"
otro_estring="otracadenadecaracteres1231241"
print(estring.isalpha()) #False
print(otro_estring.isalpha()) #True
```
 
### isdigit

Es una funcion definida para strings, la cual recibe un string al que le hara la comprobacion de que este escrito unicamente a partir de numeros

```python
estring="213214a"
otro_estring="14141331421"
print(estring.isalpha()) #False
print(otro_estring.isalpha()) #True
```
### isspace

Es una funcion definida para strings, la cual recibe un string al que le hara la comprobacion de que este escrito unicamente a partir de espacios en blancos, saltos de linea, espacios, sangrias, etc.

```python
estring="casi en blanco                    "
otro_estring="            "
print(estring.isalpha()) #False
print(otro_estring.isalpha()) #True
```

### istitle

Es una funcion definida para strings, la cual recibe un string al que le hara la comprobacion de que este escrito con cada palabra iniciando en mayuscula y el resto en minsucula (ignora loss numeros que contenga)

```python
estring="no Un Titulo Del Todo"
otro_estring="Un Titulo Del Todo"
print(estring.isalpha()) #False
print(otro_estring.isalpha()) #True
```

### islower

Es una funcion definida para strings, la cual recibe un string al que le hara la comprobacion de que este escrito unicamente a partir letras minusculas (ignora los numeros que contenga)

```python
estring="No del todo solo letras minusculas"
otro_estring="del todo letras minusuculas"
print(estring.isalpha()) #False
print(otro_estring.isalpha()) #True
```

### isupper

Es una funcion definida para strings, la cual recibe un string al que le hara la comprobacion de que este escrito con todos las letras en mayuscula (ignora los numeros que contenga)

```python
estring="cadenadecaracteres@"
otro_estring="otracadenadecaracteres1231241"
print(estring.isalpha()) #False
print(otro_estring.isalpha()) #True
```

## 2. Procesar el archivo y extraer:

Cantidad de vocales
Cantidad de consonantes
Listado de las 50 palabras que más se repiten 

Comentado dentro de su propio archivo
