
#Esta línea pide un "input" y lo convierte en un "string". El "string" se almacena en la variable llamada palabra1
palabra1 = str(input("Favor de entrar una palabra... la que sea "))
#En esta línea imprimimos en la pantalla (Console) el contenido de la variable "palabra1"
print("Escribiste la palabra "+ palabra1)
#Esta línea pide un "input" y lo convierte en un "string". El "string" se almacena en la variable llamada palabra2
palabra2 = str(input("Ahora, favor de entrar otra palabra... la que sea "))
#En esta línea imprimimos en la pantalla (Console) el contenido de la variable "palabra2"
print("Ahora escribiste la palabra "+ palabra2)
#En está línea imprimimos el mensaje "Ahora veamos cuál de las palabras, entre" (aquí insertamos el contenido de la variable palabra1) " y " (aquí insertamos el contenido de la variable palabra2)
print("Ahora veamos cuál de las palabras, entre "+palabra1+ " y " +palabra2+" tiene más caracteres." )
#En esta línea creamos la variable llamada largo_palabra1 y le asignamos el valor de la funcón len(palabra1) 
largo_palabra1 = len(palabra1)
#En esta línea creamos la variable llamada largo_palabra1 y le asignamos el valor de la funcón len(palabra2) 
largo_palabra2 = len(palabra2)

