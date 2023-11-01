# print("Hola Mundo")

# '''
# Comentarios en bloque
# Este es un ejemplo de los tipos de comentarios que posee Python.
# asdasdasdas
# '''
# # Comentario de una sola linea

# # Tipos de datos en PYTHON

# cadena = "Hola Mundo"  # Cadena de caracteres

# entero = 20  # Numero entero

# flotante = 20.5  # Numero flotante

# booleano = True  # Booleano (True o False)

# snake_case = "Esto es una variable con snake case"  # Snake case


# una_variable_con_un_nombre_largo = "Esto es una variable con snake case"  # Snake case

# print(una_variable_con_un_nombre_largo)

# print(3+5)


# def nombre_funcion():
#     return "Hola Mundo"


# print(nombre_funcion())


# #Tipos de operadores en Python
# # De asignacion
# # Matematicos
# # Logicos
# # Relacionales

# # MATEMATICOS

# print(3+5) # Suma
# print(3-5) # Resta
# print(3*5) # Multiplicacion
# print(3/5) # Division
# print(3%5) # Modulo
# print(3**5) # Exponente
# print(3//5) # Division entera

# # ASIGNACION

# x = 3 # Asignacion
# print(x)
# x += 3 # x = x + 3
# print(x) 
# x -= 3 # x = x - 3
# print(x)

# # Logicos (AND, OR, NOT) 
# print(True and True) # True
# print(True and False) # False

# print (True or False) # True

# print(not True) # False

# # Relacionales

# print(3 == 5) # False
# print(3 != 5) # True
# print(3 > 5) # False
# print(3 < 5) # True
# print(3 >= 5) # False
# print(3 <= 5) # True

# # operadores bit a bit

# print(3 & 5) # 011 & 101 = 001
# print(3 | 5) # 011 | 101 = 111


# # Malas practicas NO SE PUEDEN USAR
# '''
# mi variable ? = 3 # No se puede usar espacios en las variables

# 2pesos = 0

# 21%pesos = 0

# $pesos = 0
# '''

# mi_nombre = "Juan"

# print("mi es nombre: " + mi_nombre)

# a = 10
# b = 2


# print("la suma de a + b es: ", str(a+b))


# #entrada = input("Ingrese su nombre: ")

# #print("Hola " + entrada)

# #numero1 = input("Ingrese un numero: ")
# #numero2 = input("Ingrese otro numero: ")

# # print("La suma de los numeros es: ", int(numero1) + int(numero2))

# Tipos de datos en Python
print(type(3))  # int
print(type(3.5))  # float
print(type("Hola"))  # str
print(type(True))  # bool
print(type(False))  # bool
print(type([1, 2, 3, 4]))  # list
print(type((1, 2, 3, 4)))  # tuple
print(type({"nombre": "Juan", "apellido": "Perez"}))  # dict
print(type(None))  # NoneType
print(type(3j))  # complex


print("Mi perro 'Toby'") # Mi perro 'Toby'
print('Mi perro "Toby"') # Mi perro "Toby"


print("UN STRING" + " " + "OTRO STRING")

#var3 = 3 + "5"   # TypeError

codo_a_codo = "Codo a codo"

print("C" in codo_a_codo) # True
print("c" in codo_a_codo)
print("c" not in codo_a_codo)
