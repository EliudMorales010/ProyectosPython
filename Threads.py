import threading
import time


# Crear un hilo
hilo1 = threading.Thread()
# target: es el objeto invocable a ser invocado por el método run(). Por defecto es None, lo que significa que nada es llamado.

# name:  es el nombre del hilo. Por defecto, se construye un nombre único con la forma «Thread-N» donde N es un número decimal pequeño.

# args:  es la tupla de argumento para la invocación objetivo. Por defecto es ().

# kwargs:  es un diccionario de argumentos de palabra clave para la invocación objetivo. Por defecto es {}.
# Si no es None, daemon establece explícitamente si el hilo es demoníaco. Si es None (el valor por defecto), 
# la propiedad demoníaca es heredada del hilo actual.



