# ítem 1 

## Función "suma()" 
 
La función "suma" toma tres parámetros, 'a', 'b' y 'c', y calcula la suma de estos haciendo uso de una tupla llamada 'tp' para almacenar los valores. 
 
Para pasar los valores almacenados en la tupla 'tp' como datos de la función "suma", se utiliza el operador de desempaquetado (*), este permite que los elementos de la tupla se descompongan en tres argumentos individuales, el resultado de la suma se almacena en la variable 'resultado' la cual se muestra en pantalla más adelante, es importante mencionar que las tuplas son estructuras de datos inmutables en Python, lo que significa que una vez creadas, no se pueden modificar sus elementos. 

## Función "saluda()" 

La función "saluda" toma cuatro parámetros: 'nombre', 'edad', 'sexo' y 'nacionalidad', y muestra en pantalla un mensaje de saludo con los datos proporcionados. 

El diccionario "dicc" contiene información sobre la persona, al pasar los valores de "dicc" como argumentos de la función "saluda", se utiliza el operador de desempaquetado de diccionario (**). Esto permite que los valores se distribuyan de forma correcta, el desempaquetado de diccionarios es una forma eficiente de pasar múltiples valores a una función utilizando sus claves como nombres de parámetros. Esto facilita la reutilización de la función con diferentes conjuntos de datos, ya que solo es necesario cambiar los valores del diccionario sin modificar la llamada a la función en sí. 

## Función "invierte()" 

La función "invierte" toma una lista como argumento, y su objetivo es imprimir la lista original y luego imprimir la misma lista, pero en orden inverso. en el ejemplo proporcionado, Cuando se llama a la función "invierte" con la lista "lst", la función imprime la lista original: 
 
['IPP', 'Python', 'Scripting', 'Curso', 'Material'] 

Luego, la función crea una nueva lista llamada "lst_rev" que contiene los mismos elementos de la lista original, pero en orden inverso. Para lograr esto, utiliza la sintaxis de rebanado (slicing) con un paso de -1, que invierte el orden de los elementos en la lista: 
 
['Material', 'Curso', 'Scripting', 'Python', 'IPP'] 

La función "invierte" imprime una lista dada y luego imprime la misma lista en orden inverso, lo que puede ser útil en diferentes situaciones cuando se requiere manipular el orden de los elementos en una lista. 
 
## Función "completa" 

En la función "completa" se utilizan dos diccionarios como estructuras de datos pares (clave-valor), "dct1" y "dct2", también se utiliza el método "update()" de los diccionarios para combinar los elementos de "dct1" con el diccionario "dct2". El método "update()" actualiza el diccionario "dct2", sobrescribiendo o agregando las claves y valores de "dct1". Es decir, el diccionario "dct2" se actualiza para incluir los elementos de "dct1". Si coinciden claves en ambos diccionarios los valores del diccionario "dct2" se reemplazan por los valores de "dct1". En conclusión, la función "completa" utiliza diccionarios como estructura de datos para combinar y actualizar sus elementos de acuerdo con los argumentos proporcionados. 

# Ítem 2 

## Script 1 

En este script, se presentan una lista y una tupla. Las listas son modificables después de su creación, mientras que las tuplas una vez creadas, no pueden modificarse.  

1. Variables de entrada: 

    - La entrada inicial es una lista la cual más adelante es convertida a tupla en la variable "mytuple". 

2. Transformaciones o conversiones: 

    - La lista "mylist" se convierte en una tupla utilizando la función tuple() y se almacena en la variable mytuple. 


3. Variables de salida: 

    - El script imprime tanto "mylist" como su tipo utilizando print(). Luego, imprime "mytuple" y su tipo también con print().  

El script tiene como objetivo ilustrar cómo convertir una lista en una tupla, esta misma conversión se podría hacer de forma contraria usando list(). 

## Script 2 


1. Variables de entrada: 

   - lista1: Es una lista que contiene las claves para crear un diccionario. En este caso, contiene los elementos "nombre", "edad" y "dirección". 

   - lista2: Es una lista que contiene los valores pares de las claves para crear un diccionario. En este caso, contiene los elementos "Juan", "30" y "Valparaíso". 

2. Transformaciones o conversiones: 

   - Se convierten las listas "lista1" y "lista2" en tuplas utilizando la función incorporada tuple(). Esto garantiza que las claves y los valores sean inmutables y, por lo tanto, sean adecuados para utilizarlos como elementos de un diccionario. Las nuevas variables creadas son: 

     - clave_tupla: Una tupla que contiene las claves de la lista1, es decir, ("nombre", "edad", "dirección"). 

     - valor_tupla: Una tupla que contiene los valores pares, es decir, ("Juan", "30", "Valparaiso"). 

3. Variables de salida: 

   - dicc: Es un diccionario que se crea utilizando las tuplas "clave_tupla" y "valor_tupla" con la función zip(). La función zip() combina ambas tuplas en pares clave-valor, que luego se utilizan para crear el diccionario. Luego se imprime el contenido del diccionario "dicc". También se imprime el tipo de la variable "dicc" utilizando la función type(). Esto muestra el tipo de dato de "dicc", que será 'dict' 

El script realiza las transformaciones necesarias para crear un diccionario a partir de las listas "lista1" y "lista2", y luego imprime el diccionario resultante junto con su tipo. La estructura del diccionario final contiene las claves "nombre", "edad" y "dirección", con los valores correspondientes "Juan", "30" y "Valparaíso", respectivamente. 

## Item 3

Importamos las librerías correspondientes para poder ejecutar el código correctamente.

Calculamos los promedios de las notas, sumamos las notas y las dividimos según la cantidad de notas que tengan los estudiantes.

Calculamos la varianza para cada valor x en la lista "notas", se resta el promedio "prom", y el resultado se eleva al cuadrado con (x - prom) ** 2., se agrega "for x in notas" para decirle al programa que los valores de "X" se encuentran en "notas", ya que tenemos 3 notas por estudiante debemos sumar los resultados de la operación anterior entre si, para finalmente dividirlos según la cantidad de notas de cada estudiante.
Finalmente usaremos "math.sqrt(var)" que nos dará la desviación estándar como resultado.

A partir de ahora crearemos el area principal del código, también creare un diccionario vació donde de alojaran los los estudiantes y sus notas.

Solicitamos al usuario ingresar, primeramente el numero de estudiantes y el numero de notas que debería tener cada estudiante.

Haciendo uso de range delimitamos la cantidad de veces que se repetirá el bucle, esta cantidad estará dictada por el numero de estudiantes que ingresemos, mientras que el bucle donde ingresaremos las notas se repetirá también cuantas veces hallamos delimitado al momento de colocar cuantas notas presentara cada estudiante.

Ahora crearemos un diccionario que estará compuesto por las listas resultantes de las operaciones siguientes.

Por ultimo calcularemos las estadísticas para cada estudiante y se agregaran los resultados al diccionario anterior.

Creamos un dataframe para poder observar de mejor manera los resulta.

