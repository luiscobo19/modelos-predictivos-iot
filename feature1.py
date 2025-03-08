frase = "El mejor regalo? El perdón..."
list_frase = list(frase)

# Aquí va la solución optimizada
lista = list_frase

# Reemplazar "regalo?" por "perdón"
lista[9:15] = lista[20:26]

# Eliminar los elementos sobrantes (incluyendo los puntos suspensivos)
del lista[15:]

# Unir la lista en una nueva cadena
nueva_frase = ''.join(lista)

print(nueva_frase)
print(lista)