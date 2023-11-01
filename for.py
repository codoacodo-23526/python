for i in range(0, 11, 1):
    print(i) # imprime del 0 al 10
    

# range (inicio, fin, incremento)

# inicio = 0
# fin = 11
# incremento = 1    

suma= 0
for cont in range(5):
   num= int(input("Ingrese un número: "))
   suma = suma + num   # Acumulamos, es equivalente suma += num

print("La suma es:", suma)
print("El promedio es:", suma/cont)