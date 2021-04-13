""" 
def miFuncion ():
    print ('Mi primera funcion')

miFuncion()

def imprimeDato(argUno):
    print ('Mi Argumento es:', argUno)


imprimeDato('Parametro')


def imprimeDato(nom, ape):
    print ('Su Nombre completo es:', nom, ape)


imprimeDato('Juan', 'Guzman')


####
def argVariable (*nombre):
    print ('El nombre ompleto es: ', nombre[1]) #Impreme como una Tuple

argVariable('Juan', 'Guzman')

def nomCompleto (apellido, nombre):
    print (nombre, apellido)

nomCompleto(nombre = 'Juanito', apellido='Guzman')

###
def nomCompleto2 (**kwargs): 
    print(kwargs['nombre'], kwargs['apellido'])

nomCompleto2 (nombre ='Juanito2' , apellido='Guzman2')

###

def miFuncion2(auto = 'KIA'):
    print (auto)


# miFuncion2 ('Batman') # Si se pasa una parametro al Argumento de la Funcion la Imprime
miFuncion2 () # De lo contrario imprime el Argumento por defecto que es KIA

###
def funcLista (lista):
    for ls in lista:
        print (ls)

funcLista (['Kia','Audi','Chevrolet'])
"""
###
def contatenaNom(lista):
    i = ''
    for ls in lista:
        i = i + ls + ' '
    return i

nombres = contatenaNom (['Cata', 'Marti', 'Magda'])
print (nombres)