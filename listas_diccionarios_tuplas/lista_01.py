# DECLARACION DE LISTAS

numeros = [1, 2, 3, 4, 5] # Lista de numeros
colores = ["rojo", "verde", "azul"] # Lista de colores
lista_vacia = [] # Lista vacia
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Lista de listas
#            0           1           2
#          0 1 2       0 1 2       0 1 2

# ACCEDEMOS POR SUBINDICES
print(numeros[0]) # 1
print(colores[1]) # verde
print(matriz[1][2]) # 6

i = 0
while i < len(numeros): # tamaño de mi lista
    print(f"El numero es: {numeros[i]}")
    i += 1 #i = i + 1
    
for numero in numeros:
    print(f"El numero es: {numero}") 

for color in colores:
    print(f"El color es: {color} y {color}")
    
    print("El coler es:" + color + "algo" + "mas" + color)

c1, c2, c3 = colores

color1 = colores[0]
color2 = colores[1]
color3 = colores[2]

print(c1)
print(c2)
print(c3)

# Funciones listas

print(f"el numero maximo de la lista es {max(numeros)}")
print(f"el numero minimo de la lista es {min(numeros)}")
print(f"la suma de los numeros de la lista es {sum(numeros)}")


# Agregar un nuevo elemento a la lista al final

numeros.append(6)
print(numeros)

# Agregar un nuevo elemento en una posicion determinada

numeros.insert(0,0)
numeros.insert(3,45)
print(numeros)


numeros.pop() # EL ULTIMO ELEMENTO DE LA LISTA
#numeros.pop(3) # EL ELEMENTO DE LA POSICION 3

numeros.remove(5)

print(numeros.index(45))

print(numeros.count(450))
