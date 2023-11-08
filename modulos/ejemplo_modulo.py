from math import sin, cos, tan
from datetime import datetime
import random
from funciones.funcion_02 import sumar, num_es_par, tabla_multiplicar, potencia

print(random.randint(1,10))
print(random.random())
 
print(sin(90))
print(cos(90))
print(tan(90))
 
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day) 

print(sumar(1, 5))
print(num_es_par(1))
print(tabla_multiplicar(5))
