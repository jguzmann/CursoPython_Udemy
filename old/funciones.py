# Funciones
def miFuncion():
    print ('Imprime mi Primera Funcion')

#miFuncion()

def imprimeDato(*nombre):
    print('El nombre complero es:', nombre)


# imprimeDato('Juan', 'Guzman', 'Nuñez')

def nomCompleto(ape,nom):
    print(nom,ape)
    
# nomCompleto (nom='Juan', ape='Guzman')


def nomCompleto2 (**kwargs): #Argumentos por Llaves
        print(kwargs['nom'],kwargs['ape'])

# nomCompleto2 (nom='Eduardo', ape='Nuñez')

def miFuncion2 (arg = 'Superman'):
    print (arg)

# miFuncion2 ('Batman')
# miFuncion2()

def miFuncionLista(lista):
    for i in lista:
        print(i)


# miFuncionLista(['Primero','Segundo'])


def concatenaNombres(lista):
    i =''
    for x in lista:
        i = i + x + ' '
    return i

nombre = concatenaNombres (['Eduardo', 'Nuñez'])
# print (nombre)


# Recursividad
def recursion(i):
    if (i < 1):
        return i
    print (i)
    recursion(i - 1)

recursion(10)
