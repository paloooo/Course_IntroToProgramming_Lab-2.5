### Print

<!--intro-start-->
**Sintaxis:**

Después del comando print hay un par de paréntesis `( )`. Dentro de estos paréntesis está lo que debería ser imprimido por pantalla.

> :pushpin: **¡RECUERDA!**
>
>Usar paréntesis para pasar información a una función es una práctica muy común en las matemáticas y en los lenguajes de programación.

#### Cadenas de texto (`strings`)

Para imprimir cadenas de texto (`strings`)hay que añadir comillas (`" "`) antes y despuésdel texto a imprimir.

```python title="Ejemplo de la función de print" linenums="1" hl_lines="1"
print("Hola Mundo")
```
Pero, si no se escriben las comillas (`" "`), ***Python :snake:*** va a interpretar que estás tratando de escribir una expresión matemática. Observa el siguiente ejemplo: 
```python title="Un error al tratar de imprimir un texto" linenums="1" hl_lines="1"
print(Hola Mundo)#Esto va a devolver un error.  
```
#### Números

Para imprimir números, no se necesitan las comillas (`" "`) 

```python title="La función de print con números" linenums="1" hl_lines="1"
print(3 + 2)# En este caso va a imprimir 5
```
Pero, si añadimos las comillas (`" "`), entonces ***Python :snake:*** va a interpretar que estás tratando de imprimir un `string`

```python title="La función de print con números" linenums="1" hl_lines="1"
print("3 + 2")# En este caso va a imprimir 3 + 2
```

***
<!--intro-end-->