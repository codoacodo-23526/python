# Diccionarios
# almacenan datos , CLAVE - VALOR

#CREACION DE UN DICCIONARIO 

estudiantes = { 'Juan': 10 , 'Ana': 10 , 'Maria': 9 }

print(estudiantes)

mis_llaves = estudiantes.keys() # ['Juan','Ana','Maria']

print(estudiantes.keys())

# Podemos recorrer el diccionario con un for y keys()
for elemento in mis_llaves:
    print(elemento)


# Podemos recorrer el diccionario con las claves y los valores
suma = 0
contador = 0

for c, v in estudiantes.items():
    print(f"Estudiante: {c}, Nota: {v}", end= "\n")
    suma = suma + v
    contador = contador + 1
    
    
promedio = suma/contador

print(f"el promedio es: {promedio}")
    