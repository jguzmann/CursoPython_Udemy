diccionario = {
    "Marca" : "Kia",
    "Modelo": "Seltos",
    "Año"   : "2021"
}

diccionario1 = {
    "Marca" : "Kia",
    "Modelo": "Rio",
    "Año"   : "2021"
}

print (diccionario, type(diccionario))
print (diccionario['Modelo']) #Acceder a un valor del diccionario

print(diccionario.get('Año')) #Otro metodo para poder acceder a un valor del diccionario

diccionario['Marca'] = 'Rio'
print (diccionario) # Cambiar un varlor que tiene el diccionario


diccionario ['Motor'] = '1.6'   # Agregar valor nuevo al Dicionario
print (diccionario)

diccionario.pop('Marca')      # Eliminar una llave del Diccionario
print (diccionario)

diccionario.popitem()         # Eliminar la ultima llave agregada al Diccionario 
print (diccionario)

del diccionario ['Año']      # Eliminar una llave del Diccionario
print (diccionario)


# copiaDiccionario1 = diccionario1.copy()  # Generar copia de un Diccionario
copiaDiccionario1 = dict(diccionario1)
print (copiaDiccionario1)

diccionario1.clear()                     # Borra todo el Diccionario
print (diccionario1)


notebooks = {
    "Hp": {
        "Memoria"   :"4 GB",
        "Modelo"    :"ProBook 645",
        "Color"     : "Negro"
    },
    "Dell": {
        "Marca"     : "Dell",
        "Memoria"   :"8 GB",
        "Modelo"    :"Inspiron 3593",
        "Color"     : "Plata"
    }
}
print (notebooks)

hombres ={
    "nombre"    : "Juan",
    "Apellido"  : "Guzman",
    "edad"      : "40"
}
mujeres={
     "nombre"   : "Marta",
    "Apellido"  : "Castro",
    "edad"      : "40"
}

personas={
    "hombres"   : hombres,
    "mujeres"   : mujeres
}
print(personas)

perros = dict(nombre="Pocker", Edad= "8")#Crear Diccionario con Contrucctor dict
print (perros)

