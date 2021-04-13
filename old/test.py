# Tipo de Dato: LISTA
# lista = [3, 2, 3]
# lista2 = lista.copy()
# lista.append(4)
# list_cadena = ['Chile', 'Peru', 'Argentina']
# print(lista, lista2.count(3))
# print(len(lista), len(lista2))

# print(list_cadena[1])

# list_cadena.remove('Chile')

# list_cadena.pop()
# print(list_cadena)

# list_cadena.reverse()
# list_cadena.sort()
# print(list_cadena)

# Tipo de Dato: TUPLA

# tupla = ('Chile', 'Bolivia', 'Colombia')
# print(tupla, 'El tipo de esta variable es: ', type(tupla))
# print('El valor encontrado es: ', tupla.count('Chile'))

# print('La posicion (index) es: ', tupla.index('Colombia')) #Devuelve la posicion (index) de donde encontro un elemento
# print ('El index en la Tuple es: ' , tupla[0])

# tupla_to_lista = list(tupla) # Trasformar Tuple a List

# print (type(tupla), ' ' ,type(tupla_to_lista))
# print(tupla_to_lista)

# Tipo de Dato: RANGE

# rango = range(6)
# print (rango, 'Esta Variable un Tipo de dato: ', type(rango))

# Tipo de Datos:  DICTIONARIES

diccionario = {
    "Marca": "Chevrolet",
    "Modelo": "Cruze",
    "Año":"2018"
}

print(diccionario)

# dictionaries_to_list = list(diccionario)
# print(dictionaries_to_list)

print (diccionario['Modelo'])   # Acceder al Valor del Diccionario
print (diccionario['Marca'])    # Acceder al Valor del Diccionario

print(diccionario.get('Año'))   # Metodo Get para acceder alos Valores

diccionario['Año'] = '2010'     # Modifica Valor en el Diccionario
print (diccionario)

diccionario ['Motor'] = '1.8'   # Agregar una nueva llave al Dicionario
print (diccionario)


# diccionario.pop('Motor')      # Eliminar una llave del Diccionario
# print (diccionario)

# diccionario.popitem()         # Eliminar la ultima llave agregada al Diccionario 
# print (diccionario)

# del diccionario ['Modelo']      # Eliminar una llave del Diccionario
# print (diccionario)

# backup_Diccionaio = diccionario.copy()  # Generar copia de un Diccionario
# backup_Diccionaio2 = dict(diccionario)  # Con la funcion Dict tambien genera una copia del Diccionario ¡
# diccionario.clear()                     # Borra todo el Diccionario
# print (diccionario)
# print(backup_Diccionaio)                # Imprime la Copia del Diccionario antes de eliminarlo


# hp = {
#         "Memoria":"4 GB",
#         "Modelo":"ProBook 645",
#         "Color": "Negro"
#     }
# dell= {
#         "Memoria":"8 GB",
#         "Modelo":"Inspiron 3593",
#         "Color": "Plata"
#     }



# computadoras = {
#     "HP":{
#         "Memoria":"4 GB",
#         "Modelo":"ProBook 645",
#         "Color": "Negro"
#     },
#     "DELL":{
#         "Memoria":"8 GB",
#         "Modelo":"Inspiron 3593",
#         "Color": "Plata"
#     }
# }


# computadoras2 = {
#     "HP": hp,
#     "DELL": dell
# }


# print (computadoras)
# print (computadoras2)

# # Crear Diccionario con Contrucctor dict
# perros = dict(nombre = "Pocker", Edad = "8")
# print (perros)

# Tipo de Dato: BOOLEAN

verdadero= True
falso = False

print ('El valor de la variable Verdadero es: ',verdadero,'y', 'El valor de la variable Falso es: ',falso)
