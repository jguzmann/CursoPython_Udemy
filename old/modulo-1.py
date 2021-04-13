# import modulos as mdl
from modulos import saludo, mascotas
from camelcase import CamelCase


print (mascotas)
saludo ('Juan')

# Generar instancia de CamelCase
c = CamelCase()
s = "esta oracion es con funcion camelcase"

camelcase = c.hump(s)

print (camelcase)


c = CamelCase()
s = 'this is a sentence that needs juan!'
print (c.hump(s))