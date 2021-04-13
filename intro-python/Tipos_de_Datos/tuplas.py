# Tipo de Dato: TUPLA

# tupla = ('Chile', 'Bolivia', 'Colombia')
# print(tupla, 'El tipo de esta variable es: ', type(tupla))
# print('El valor encontrado es: ', tupla.count('Chile'))



# print (type(tupla), ' ' ,type(tupla_to_lista))
# print(tupla_to_lista)

tupla = ('Chile', 'Bolivia', 'Argentina')
print(tupla)
print(tupla.count('Chile'))

print('La posicion (index) es Chile: ', tupla.index('Chile')) #Devuelve la posicion (index) de donde encontro un elemento
print ('El index en la Tuple es: ' , tupla[2])

tupla_to_lista = list(tupla) # Trasformar Tuple a List
print (tupla_to_lista)
print ('La variable tupla es de tipo: ', type(tupla), ' ' ,'y la variable tupla_to_lista es de tipo: ', type(tupla_to_lista))