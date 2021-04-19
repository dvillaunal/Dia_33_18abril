# Funciones Lambda:
'''
Aqui vemos que dos argumentos solamente puede tener una 
expresión,

# Argumento:
No usamos paréntesis alrededor de los parámetros
como hacemos con las funciones regulares.

# Expresión:
Cualquier expresión válida de python
que opere sobre los parámetros que proporcionas a la función.
'''
# Ejemplo 0:

'''
Aquí definimos una variable que contendrá
el resultado retornado por la función lambda:
  1. La palabra clave lambda sirve para definir una función anónima.
  
  2. x e y son los parámetros que pasamos a la función lambda.
  
  3. Este es el cuerpo de la función, que añade los 2 parámetros que pasamos.
    Observa que es una única expresión.
    No puedes escribir varias expresiones en el cuerpo de una función lambda.
  
  4. Llamamos a la función e imprimimos el valor retornado.
'''

## Definimos Función de suma lambda:
suma = lambda x, y: x + y

## Imprimimos el resultado utlizando valores x=1 & y=2:
print('Hola soy una Función Lambda con parametros x=1 & y=2')

print('El retorno de la función lambda suma es:', suma(1, 2))

## Veamos que pasa si imprimimos....

saludo = 'Hola Mundo'

print(lambda string : print(saludo))

'''
Aquí, definimos una cadena que pasará como parámetro a lambda.

Declaramos una lambda que llama a una declaración de impresión e imprime el resultado.

Pero,
¿por qué el programa no imprime la cadena que pasamos?
Esto se debe a que la propia lambda devuelve un objeto de función.
En este ejemplo, la función de impresión no llama a lambda,
sino que simplemente devuelve el objeto de función y
la ubicación de memoria donde se almacena.

Eso es lo que se imprime en la consola.
'''

## Volvemos a intentarlo pero ahora con una sintaxís diferente:
print('----------------------------')
(lambda string : print(saludo))(saludo)

'''
Explicación del código

1. Aquí está la misma cadena que definimos en el ejemplo anterior.

2. En esta parte, definimos una lambda y la llamamos inmediatamente pasando la cadena como argumento.
Esto es algo llamado IIFE (Sacado de https://realpython.com/python-lambda/)
'''

# filter():
'Creamos una lista vacia'
lista_num = list()

'Con el ciclo for añadimos a lista_num numeros desde el 1 al 50'
for i in range(1, 100, 1):
  lista_num.append(i)

'''
Aquí, declaramos una variable llamada filtro,
que almacenará los valores filtrados retornados
por la función filter().'
'''
filtro = filter(lambda i: i <= 50 and i >= 10, lista_num) #Una función lambda que se ejecuta sobre cada elemento de la lista y retorna true si  10 <= i <= 50

'''
Imprimir el resultado retornado por la función filtro.
convirtiendolo a una lista.
'''
print(list(filtro))

# map():

'''
Tomamos la lista anterior con numeros del 1 al 50
veamosla:
'''
print('Nuestra Lista',lista_num)

'''
Declaramos una variable llamada "m"
que almacenará los valores mapeados.
'''
m = map(lambda x: x**(0.5), lista_num) #  función lambda que se ejecuta sobre cada elemento de la lista y retorna la raiz cuadrada de ese número.

'''
Imprimir el resultado retornado por la función map.
convirtiendolo a una lista.
'''
print(list(m))

# reduce():
'''
Calculemos la sumatoria de todos
los elementos de la lista lista_num:
'''

'Importar reduce del módulo functools'
from functools import reduce

'Declaramos una variable llamada sumatoria que almacenará el valor reducido'

#  Una función lambda que se ejecuta sobre cada elemento de la lista.

sumatoria = reduce(lambda x, y: x+y, lista_num) # Devolverá la sumatoria de ese número según el resultado anterior.

'Imprime el resultado retornado por la función reduce()'
print('sumatoria de todos los elementos de la lista es:',sumatoria)
