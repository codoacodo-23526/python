def imprimir_mensaje(mensaje):
    print(mensaje)

def sumar(numero1, numero2):
    suma = 0
    cantidad = 0
    for elemento in range(numero1, numero2+1):
        suma += elemento
        cantidad += 1
        
    if suma > 100:
        imprimir_mensaje(f"La suma de los numeros entre {numero1} y {numero2} es: {suma}")
    else:
        #print(f"La suma de los numeros entre {numero1} y {numero2} es: {suma}")
        return suma, cantidad
    
def tabla_multiplicar(numero):
    resultado = [] # lista vacia
    for elemento in range(1, 11):
        resultado.append(numero * elemento)    
    return resultado
    
def num_es_par(numero):
    if numero % 2 == 0:
        return True # ES PAR
    else:
        return False # ES IMPAR

def potencia(numero, exponente = 2):
    resultado = numero ** exponente
    return resultado

#PROGRAMA PRINCIPAL
sumar(1, 5)
sumar(1, 100)
sumar(10, 500)

numero1 = 1
numero2 = 5
suma, cantidad = sumar(numero1, numero2)

print(f"La suma de los numeros entre {numero1} y {numero2} es: {suma}")
print(f"La cantidad de numeros entre {numero1} y {numero2} es: {cantidad}")

resultado = num_es_par(numero1)
print(f"El numero {numero1} es par? {resultado}")


res = tabla_multiplicar(5)
print(res)


print(f"La potencia de este numero es: {potencia(4,2)}")


potencia_con_lambda = lambda numero, exponente: numero ** exponente

print(f"La potencia de este numero es: {potencia_con_lambda(4,2)}")


lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]

cuadrados = list(map(lambda numero: numero ** 2, lista_de_numeros))
print(cuadrados)
