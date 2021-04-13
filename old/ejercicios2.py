# 63 Ejercicios

# EJERCICIO 1
# Multiplicar 2 num sin usar el simbolo multiplicar
factor1 = 4
factor2 = 8

producto = 0

for f in range (factor2):
    producto += factor1

print (producto)

# EJERCICIO 2
# Ingresar nombre y apellido e imprimirlo al revez

nom = 'Juan'
ape = 'Guzman'

concatenar = nom + ' ' + ape
print (concatenar [::-1])

# EJERCICIO 3
# Función que encuentre el elemento menor de una lista

lista = [24,1,0,-24,-50]

menor = 'init'

for i in lista:
    if menor == 'init':
        menor = i
    else:
        menor = i if i < menor else menor

print ('Nro. Menor', menor)

# EJERCICIO 4
# Función que devuelva el volumen de una esfera por su radio
# 4/3 * pi * r ** 3

def calcVolumen (r):
    return 4 / 3 * 3.14 * r ** 3
resul = calcVolumen (6)
print ('El Volumenn de una Esfera por su Radio es: ', resul)


# EJERCICIO 5
# Función que indique si el usuario es mayor de edad

def esMayor (usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self, edad):
        self.edad = edad

usuario1 = Usuario (15)
usuario2 = Usuario (21)

resul1 = esMayor (usuario1)
resul2 = esMayor (usuario2)

print ('Usuario1:', resul1,' / ' ,'Usuario1:',resul2)

# EJERCICIO 6
# Función que indique si un número es par o impar









