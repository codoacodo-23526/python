# variable_1 = "hola"

# variable_2 = 5*variable_1

# print(variable_2) # holaholaholaholahola


# print("La longitud de mi variable_1 es: ", len(variable_1)) # 4

# print("La longitud de la variable_2 es: ", len(variable_2)) # 20

# print(variable_1[0]) # h
# print(variable_1[1]) # o
# print(variable_1[2]) # l
# print(variable_1[3]) # a
# print(variable_1[4]) # IndexError: string index out of range
# print(variable_1[len(variable_1)-1]) # a
# print(variable_1[-2]) # l
# print(variable_1[-3]) # o
# print(variable_1[-4]) # h

# while True:
#     nombre = input("Ingresa tu nombre: ")
#     if nombre.upper() == "SALIR":
#         break # Termina el ciclo palabra reservada
#     print("Hola " + nombre)
    
# nombre = "Juan perez"

# print(nombre.upper()) # JUAN PEREZ
# print(nombre.lower()) # juan perez
# print(nombre.capitalize()) # Juan perez
# print(nombre.title()) # Juan Perez
# print(nombre.swapcase()) # jUAN PEREZ


cadena_1 = "Hola Mundo"
cadena_2 = ";".join(cadena_1)

print(cadena_2) # H;o;l;a

cadena_3 = cadena_2.split(";")

print(cadena_3) # ['H', 'o', 'l', 'a']

cadena_4 = cadena_1.replace("Hola", "Chau")

print(cadena_4) # Chau Mundo


monto = "10000"

monto = monto.zfill(10)

print(monto) # 0000010000


# f-string o formateo de cadenas

print("El monto es: " + monto + " y el tipo de dato es: " + str(type(monto)))
# es lo mismo solo es otra manera de concatenar
print(f"El monto es: {monto} y el tipo de dato es: {type(monto)}")