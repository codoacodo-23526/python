

def sumar(numero1 , numero2):
    suma = 0
    for elemento in range(numero1, numero2+1):
        suma += elemento
    print(f"La suma de los numeros entre {numero1} y {numero2} es: {suma}")
    

sumar(1, 5)
sumar(1, 100)
sumar(10, 500)