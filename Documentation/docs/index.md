---
hide:
  - navigation
---
# Ejercicio :muscle: practico: Comparar el tamaño de dos cadenas de texto *(`string`)*

***
## Introducción

En este ejercicio :muscle: practico vamos a diseñar e implementar un programa que haga lo siguiente:

* Pedir al usuario que entre 2 palabras 
* Imprima las 2 palabras entradas 
* Cuente cuantos caracteres tienen esas 2 palabras usando la función de `len( )`
* Imprima cuantos caracteres tiene cada palabra
* Compare las 2 palabras y diga cuál tiene más caracteres. 

Para lograr esto necesitas haber adquirido ciertos conocimientos. En la sección de [**Prerrequisitos**](https://largo-de-un-string.palo-ooo.repl.co/#prerequisitos "Ir a la sección de Prerequisitos") te muestro cuales son esos conocimientos. Al principio de la sección de [**Prerrequisitos**](https://largo-de-un-string.palo-ooo.repl.co/#prerequisitos "Ir a la sección de Prerequisitos") verás un enlace a una preprueba. Si obtienes una puntuación de 10 puntos o más en la preprueba entonces puedes pasar directo a la sección de [**Discusión**](https://largo-de-un-string.palo-ooo.repl.co/#discusion "Ir a la sección de Discusión"). 

***
## Prerrequisitos

Para poder entender el código con el que estarás trabajando, ***primero necesitas conocer y entender las siguientes funciones*** de ***Python :snake:*** :

En la tabla a continuación :point_down: te muestro que conceptos y destrezas necesitas dominar **antes de continuar**.

>:loudspeaker: **¡ATENCIÓN!**
>
>Si ya conoces y entiendes todas las funciones que aparecen a en la tabla a continuación :point_down:, puedes continuar a tomar la  
[**preprueba**](https://introtoprogramminglab-025.palo-ooo.repl.co/#preprueba)

| **FUNCIÓN**  | **APLICACIÓN**                                                      |
|--------------|---------------------------------------------------------------------|
| [print( )](https://introtoprogramminglab-025.palo-ooo.repl.co/#print "Leer sobre la función de print( )")     | Cómo imprimir mensajes que Incluyan el valor de 1 o más variables   |
| [print( )](https://introtoprogramminglab-025.palo-ooo.repl.co/#print "Leer sobre la función de print( )")     | Cómo concatenar varios `strings` y expresiones númericas            |
| [input( )](https://introtoprogramminglab-025.palo-ooo.repl.co/#print "Leer sobre la función de print( )")     | Cómo asignar valores a variables                                    |
| [>, <, >=, <=](https://introtoprogramminglab-025.palo-ooo.repl.co/#print "Leer sobre la función de print( )") | Comparar 1 o más valores                                            |
| [if else](https://introtoprogramminglab-025.palo-ooo.repl.co/#print "Leer sobre la función de print( )")     | Cambiar mensajes de print( ) dependiendo el valor de las variables. |
|              |                                                                     |

***
:loudspeaker: **¡ATENCIÓN!**

Para que estemos seguros que dominas los conceptos y destrezas necesarias para que puedas aprovechar al máximo el ejercicio vamos a tomar una prueba corta

### Preprueba

:crossed_swords: 
<a href="https://forms.office.com/r/uDJuzsBDik"  target="_new"><strong>Haz clic en este enlace para tomar la Preprueba</strong></a>

### :stop_sign: ¿Obtuviste menos de 10 puntos en la prueba? ###

Si te equivocas en alguna de las preguntas de la prueba te recomiendo visitar la sección que corresponda para que repases el material. Para encontrar la sección (puedes usar la **`Tabla de contenidos a la derecha`** :point_right:) ó usar la barra de busqueda en la parte superior :point_up: de la página.   

***
### Print

**Sintaxis:**

Después del comando print hay un par de paréntesis `( )`. Dentro de estos paréntesis está lo que se va a imprimir (presentar) en la pantalla o en la consola. 

> :pushpin: **¡RECUERDA!**
>
>Usar paréntesis para pasar información a una función es una práctica muy común en las matemáticas y en la mayoría de los lenguajes de programación.

#### Cadenas de texto (`strings`)

Para imprimir cadenas de texto (`strings`) hay que añadir comillas (`" "`) antes y después del texto a imprimir.

```python title="Ejemplo de la función de print" linenums="1" hl_lines="1"
print("Hola Mundo")
```
![Replit.com - Captura de pantalla](https://user-images.githubusercontent.com/67485637/169345546-d18290be-9f8d-4d2c-8f90-72080b70ddc7.png "Captura de pantalla de replit.com. Se muestra el editor de código y la consola.")

Pero, si no se escriben las comillas (`" "`), ***Python :snake:*** va a interpretar que estás tratando de escribir una expresión matemática. Observa el siguiente ejemplo: 
```python title="Un error al tratar de imprimir un texto (string)" linenums="1" hl_lines="1"
print(Hola Mundo)#Esto va a devolver un error.  
```
![Replit.com - Captura de pantalla](https://user-images.githubusercontent.com/67485637/169346827-3b451284-e5ac-405e-aab8-57409dcf4ae1.png "Captura de pantalla de replit.com. Se muestra el editor de código y el error producido en la consola.")

#### Números

Para imprimir números, no se necesitan las comillas (`" "`) 

```python title="La función de print con números" linenums="1" hl_lines="1"
print(3 + 2)# En este caso va a imprimir 5
```
Pero, si añadimos las comillas (`" "`), entonces ***Python :snake:*** va a interpretar que estás tratando de imprimir un `string`

```python title="La función de print con números interpretados como texto (strings)" linenums="1" hl_lines="1"
print("3 + 2")# En este caso va a imprimir 3 + 2
```



***
### Input


***
### Operadores

>**Nota: En la siguiente tabla :point_down: usamos dos variables, `num1` y `num2`** 

| **FUNCIÓN / OPERADOR**       | **EXPRESIÓN EN PYTHON** |
|:------------------:|:-----------------------:|
| [asignación](https://largo-de-un-string.palo-ooo.repl.co/#operador-de-asignacion"Leer sobre el operador de asignación")        | num1 = 3                |
| [igualdad](https://largo-de-un-string.palo-ooo.repl.co/#operador-de-igualdad"Leer sobre el operador de igualdad")         | num1 == num2            |
| [no igualdad](https://largo-de-un-string.palo-ooo.repl.co/#operador-de-no-es-igual"Leer sobre el operador de no igualdad")        | num1 != num2            |
| [mayor que](https://largo-de-un-string.palo-ooo.repl.co/#mayor-que-y-menor-que"Leer sobre el operador de mayor que")          | num1 > num2             |
| [mayor o igual que](https://largo-de-un-string.palo-ooo.repl.co/#mayor-o-igual-que-y-menor-o-igual-que"Leer sobre el operador de mayor o igual que")  | num1 >= num2            |
| [menor que](https://largo-de-un-string.palo-ooo.repl.co/#mayor-que-y-menor-que"Leer sobre el operador de menor que")          | num1 < num2             |
| [menor o igual que](https://largo-de-un-string.palo-ooo.repl.co/#mayor-o-igual-que-y-menor-o-igual-que"Leer sobre el operador de menor o igual que")  | num1 <= num2            |
|                    |                         |

***
#### Operador de asignación `=`

**Descripción:**

El operador de asignación se usa para asignar un valor a una variable. 

>:loudspeaker: **¡ATENCIÓN!**
> Esto es para :reminder_ribbon: **¡RECORDAR!**
>
>**Una sentencia de asignación (*una línea de código usando el operador `=`*) es diferente a la igualdad algebráica que aprendiste en matemáticas.** **¡No te confundas!, NO pienses que son la misma cosa.**

**En la parte de la izquierda de un operador de asignación `=` sólo debe haber una variable. ¡Y nada más!**

**A la derecha del símbolo igual (`=`) / operador de asignación hay una expresión. Una expresión es algo que evalúa un valor.** 
Cómo ejemplo examina el siguiente código:
```python title="Ejemplo de una expresión" linenums="1"
x = x + 1
```
Estamos de acuerdo en que, el código anterior no puede ser una igualdad algebraica. Pero para ***Python :snake:*** es válido ya que es una **sentencia de asignación**. Las ecuaciones matemáticas son diferentes a las sentencias de asignación, incluso si tienen variables, números y un signo de igual (`=`).

Continuando con el ejemplo en el código anterior vemos que el programa toma el valor actual de la variable **`x`**, le añade una unidad y almacena el nuevo resultado en **`x`**.

Vamos a ampliar la expresión anterior. El siguiente código imprime el número 6 en la consola. 

```python title="Ejemplo de cómo usar el operador de asignación" linenums="1" hl_lines="1 2"
x = 5
x = x + 1
print(x)
```
**Las sentencias (*cada línea de código*) son ejecutadas secuencialmente.** En el código siguiente, :point_down: ***Python :snake:*** **imprimirá un 5 en la línea 2** y **un 6 en la línea 4**. Esto es porque en la línea 2, el código para añadir una unidad a x aún no se ha ejecutado.

```python title="Sustituyendo el contenido de una variable" linenums="1" hl_lines="2 4"
x = 5
print(x) # Imprime 5
x = x + 1
print(x) # Imprime 6
```
En el código a continuación :point_down: la sentencia en la línea 1 **no tiene ningún sentido.** Intenta ejecutar este código y verás el error:  

```python title="Una línea de código sin sentido" linenums="1"
x + 1
```
![Error al entrar la expresión x + 1](https://user-images.githubusercontent.com/67485637/169199874-39daf619-d435-45f5-9715-b9e81de26de4.png "Error que nos devuelve la consola de Replit al entrar la expresión x + 1")

***Python :snake:*** añadirá una unidad a **`x`**, pero el resultado nunca se almacenará ni tampoco se imprimirá. 


El código a continuación :point_down: imprimirá 5 en vez de 6 porque la programadora o el programador olvidó almacenar el resultado de `x + 1` en la variable `x`

```python title="Un error  al omitir un operador de asignación" linenums="1" hl_lines="2"
x = 5
x + 1
print(x)
```
![replit com - python - results in the console](https://user-images.githubusercontent.com/67485637/169205219-f39a3bdd-99e2-497b-b208-bd948122d264.png "Resultados en la consola de Replit.com")

**Sintaxis:**

A la izquierda del signo (`=`) escribe el ***nombre de la variable*** y a la derecha del signo (`=`) escribe el ***valor asignado a la variable***
```python title="Ejemplo del operador de asignación" linenums="1" hl_lines="1"
num1 = 3
print(num1)
```

--- 
#### Operador de igualdad `==`
**Descripción:**

El operador de igualdad se usa para verificar si 2 variables o 2 valores son iguales. 

**Sintaxis:**

A la izquierda del signo (`==`) el ***se escribe un valor o una variable*** y a la derecha del signo (`==`) se escribe el ***otro valor o variable***
```python title="Ejemplo del operador de igualdad" linenums="1" hl_lines="2 6"
# Ejemplo # 1
print(3 == 3) # Cómo 3 es igual a 3, va a imprimir la palabra True
# Ejemplo # 2; Usando variables
num1 = 3
num2 = 2
print(num1 == num2) # Cómo 3 NO es igual a 2, va a imprimir la palabra False
```

---
#### Operador de "no es igual" `!=`

**Descripción:**

El operador de igualdad se usa para verificar si 2 variables o 2 valores son iguales. 

**Sintaxis:**

A la izquierda del signo (`!=`) se escribe el ***un valor o una variable*** y a la derecha del signo (`!=`) se escribe el ***otro valor o variable***
```python title="Ejemplo del operador de NO Igualdad" linenums="1" hl_lines="2 6"
# Ejemplo # 1
print(3 != 3) # Cómo 3 es igual a 3, va a imprimir la palabra False
# Ejemplo # 2; Usando variables
num1 = 3
num2 = 2
print(num1 != num2) # Cómo 3 NO es igual a 2, va a imprimir la palabra True
```
---
#### Operadores de comparación 

**Descripción:**

>:loudspeaker: **¡Atención!**
>
>**Existen 4 operadores de comparación**

| **OPERADOR**       | **EXPRESIÓN EN PYTHON** |
|--------------------|-------------------------|
| mayor que          | num1 > num2             |
| mayor o igual que  | num1 >= num2            |
| menor que          | num1 < num2             |
| menor o igual que  | num1 <= num2            |
|                    |                         |

##### Mayor que y Menor que
**Sintaxis:**

A la izquierda del signo (`<`) o del signo (`>`) se escribe el ***un valor o una variable*** y a la derecha del signo (`<`) o del signo (`>`) se escribe el ***otro valor o variable***
```python title="Ejemplo de los operadores de MAYOR QUE y MENOR QUE" linenums="1" hl_lines="2 4"
# Ejemplo # 1
print(3 > 2) # Cómo 3 ES MAYOR que 2, va a imprimir la palabra True
# Ejemplo # 2; 
print(3 < 2) # Cómo 3 NO ES MENOR que 2, va a imprimir la palabra False
```
---
##### Mayor o igual que y Menor o igual que
**Sintaxis:**

A la izquierda del signo (`<=`) o del signo (`>=`) se escribe el ***un valor o una variable*** y a la derecha del signo (`<=`) o del signo (`>=`) se escribe el ***otro valor o variable***
```python title="Ejemplo de los operadores de MAYOR O IGUAL QUE y MENOR O IGUAL QUE" linenums="1" hl_lines="2 4 6 8"
# Ejemplo # 1
print(3 >= 2) # Cómo 3 ES MAYOR que 2 pero, 3 NO ES IGUAL A 2, va a imprimir la palabra True
# Ejemplo # 2; 
print(3 >= 3) # Cómo 3 NO ES MAYOR QUE 3 pero, 3 SI ES IGUAL que 3, va a imprimir la palabra True
# Ejemplo # 3; 
print(3 <= 2) # Cómo 3 NO ES NI MENOR NI IGUAL que 2, va a imprimir la palabra False
# Ejemplo # 4; 
print(3 <= 3) # Cómo 3 NO ES MENOR PERO que 2 pero, 3 SI ES IGUAL que 3, va a imprimir la palabra True
```
---

## Discusión

```python title="Cómo usar input()" linenums="1" hl_lines="2"
#Esta línea pide un "input" y lo convierte en un "string". El "string" se almacena en la variable llamada palabra1{ .annotate }
palabra1 = str(input("Favor de entrar una palabra... la que sea "))
#En esta línea imprimimos en la pantalla (Console) el contenido de la variable "palabra1"
print("Escribiste la palabra "+ palabra1)
```


***
## Glosario

***
<!-- Templates --> 
<!----- Notifications -----> 
<!--
>:loudspeaker: **¡ATENCIÓN!**
>
>Si ya conoces y entiendes todas las funciones en la tabla a continuación :point_down: entonces, puedes continuar a la sección de [**Discusión**](https://largo-de-un-string.palo-ooo.repl.co/#discusion "Ir a la sección de Discusión")
-->