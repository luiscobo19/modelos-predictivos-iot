#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) 
# y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
import random
lista = [random.randint(1,10) for _ in range(10)]
print(lista)
for i in lista:
    cuadrado = i ** 2
    cubo = i ** 3
    print(f"numero : {i}, Cuadrado: {cuadrado}, Cubo: {cubo}") 
