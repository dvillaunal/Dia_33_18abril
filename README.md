# Funciones Lambda (Lambda functions):

En Python, __función anónima significa que una función no tiene nombre.__ Como ya sabemos, la palabra clave ``def`` se utiliza para definir las funciones normales y la palabra clave ``lambda`` se utiliza para crear funciones anónimas. Tiene la siguiente sintaxis:

### Sintaxis:
  Se ejecuta la expresión y se retorna el resultado:
  ~~~
  lambda argumentos: expresión
  ~~~


### Nota 1:

  * Esta función puede tener cualquier número de argumentos, pero sólo una expresión, que se evalúa y retorna.

  * Uno es libre de utilizar las funciones lambda siempre que se necesiten objetos de función.

  * Hay que tener en cuenta que las funciones lambda están restringidas sintácticamente a una sola expresión.

  * Tiene varios usos en campos particulares de la programación además de otros tipos de expresiones en funciones.

## IIFE en Python ``Lambda``:

Un patrón utilizado en otros lenguajes como JavaScript es ejecutar inmediatamente una función lambda de Python. Esto se conoce como __Ejecución de Función Invocada Inmediatamente__ o en ingles: __Immediately Invoked Function Expression__ (IIFE, pronúnciese "iffy")

### Nota 2:
  * Varios ejemplos en el reto de hoy utilizan este formato para resaltar el aspecto anónimo de una función lambda y evitar centrarse en el lambda como una forma más corta de definir una función (porque es más que claro que es una forma más corta para definir funciones).

  * Python no fomenta el uso de expresiones lambda invocadas inmediatamente. Simplemente resulta que una expresión lambda es invocable, a diferencia del cuerpo de una función normal.


## Uso de lambdas con los métodos incorporados de Python (Built-ins):
  * Las funciones lambda proporcionan una forma elegante y potente de realizar operaciones con los métodos incorporados en Python. Es posible porque las lambdas pueden ser invocadas inmediatamente y pasadas como argumento a estas funciones.


### Funciones Lambda con ``map()``, ``reduce()`` y ``filter()`` en Python:
 
 
 Bibliografria: 
 
 https://j2logo.com/python/funciones-lambda-en-python/

 * ``filter()``:
   * La función filter se utiliza para seleccionar algunos elementos particulares de una secuencia de elementos. La secuencia puede ser cualquier iterador como listas, conjuntos, tuplas, etc.
   
   * Los elementos que se seleccionan se basan en alguna restricción predefinida. Toma 2 parámetros:
     
     1. Una función que define la restricción de filtrado
     
     2. Una secuencia (cualquier iterador como listas, tuplas, etc.)
  
 * ``map()``:
   la función map se utiliza para aplicar una operación determinada a cada elemento de una secuencia. Al igual que filter(), también toma 2 parámetros:
   
   1. Una función que define la operación a realizar sobre los elementos
   
   2. Una o más secuencias 
 
 * ``reduce()``:
   * La función reduce(), al igual que map(), se utiliza para aplicar una operación a cada elemento de una secuencia. Sin embargo, difiere de map en su funcionamiento.
     - Estos son los pasos que sigue la función reduce() para calcular una salida:
      
       1. Realizar la operación definida sobre los 2 primeros elementos de la secuencia.
       
       2. Guarda este resultado.
       
       3. Realizar la operación con el resultado guardado y el siguiente elemento de la secuencia.
       
       4. Repetir hasta que no queden más elementos.
    
   * __También toma dos parámetros:__
    
     1. Una función que define la operación a realizar.
     
     2. Una secuencia (cualquier iterador como listas, tuplas, etc.)
