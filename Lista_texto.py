"""Ejercicio:

Escribir una función que reciba un texto y devuelva una lista anidada que representa un ranking de palabras.
El texto puede tener gran cantidad de palabras. 
La función deberá devolver una lista anidada, en la que cada sublista, esté formada por un par [palabra, cantidad de veces en el texto], ordenada por la cantidad de veces que aparece la palabra.
Las palabras sólo deben aparecer una vez en la lista."""

texto = "hola hola hola como va va ?"
lista_texto = texto.split()
lista_2 = []
lista_3 = []

#print(lista_texto)

for i in lista_texto:
    
    if i not in lista_2:
        lista_2.append(i)
    
for i in lista_2:
    lista_3.append([i, lista_texto.count(i)])

#print (lista_3)
    
lista_3.sort(key = lambda item:item[1], reverse = True)

print (lista_3)