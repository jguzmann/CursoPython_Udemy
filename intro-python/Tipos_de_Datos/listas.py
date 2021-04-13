lista1 = [] #lista desclarada vacia
print ('Imprime Lista vacia')
print (lista1) #Imprime Lista vacia


# Delara valores a la Lista
print ('\n')
lista1 = [1, 2, 3] #lista desclarada vacia
print ('Lista declarada del 1 al 3')
print (lista1)

# Manipular lista
# Crear una copia de la Lista
print ('\n')
print ('Imprime copia de Lista1 en Lista2')
lista2 = lista1.copy()
print (lista1, lista2)

# Agregar mas elemntos a la lista
print ('\n') #Imprime Salto de Linea
lista1.append(4)
print ('Agrega Elemento 4 a la Lista1')
print (lista1)

# Eliminar todos los elemntos que se encunetran en la lista
print ('\n') #Imprime Salto de Linea
print ('Elimina todos los elemetos de la Lista')
lista1.clear()
print (lista1)

