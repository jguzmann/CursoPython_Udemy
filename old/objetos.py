# OBJETOS / CLASES / HERENCIAS
'''
class Usuario:
    def __init__(self, nom, ape):
        self.nom = nom
        self.ape = ape


urs = Usuario ('Felipe', 'Gonzalez')
urs2 = Usuario ('Juan','Guzman')
print(urs.nom, urs.ape, urs2.nom, urs2.ape)
'''

# METODO
'''
class Usuario:
        def __init__(self, nom, ape):
            self.nom = nom
            self.ape = ape
        def saludo(self,):
            print ('Hola!, mi nombre es:',self.nom, self.ape)

urs = Usuario ('Felipe', 'Gonzalez')
urs2 = Usuario ('Juan','Guzman')

urs.saludo()
urs2.saludo()
'''

#  Self, eliminar propiedades y objetos
class Usuario:
        def __init__(self, nom, ape):
            self.nom = nom
            self.ape = ape
        def saludo(self,):
            print ('Hola!, mi nombre es:',self.nom, self.ape)

urs = Usuario ('Felipe', 'Gonzalez')
urs.saludo()

urs.nom = 'Fernando'    # Cambiar las propiedades de las instancias de los objetos
urs.saludo()
'''
del urs.nom             # Eliminar las propiedades que tengam estas intancias
#urs.saludo()           # Genera un ERROR que nombre no se encuentra definido, es por que fue ELIMINADO (del urs.nom)

del urs                 #  Eliminar un Objeto por completo
print (urs)             # Genera un ERROR que usuario no se encuentra definido, es por que fue ELIMINADO (del urs)
'''
# HERENCIA
class Admin(Usuario):
    def superSaludo(self):      # Agrega Metodo
        print ('Me llamo,', self.nom, 'y soy Administrador')

adm = Admin('Superx', 'Administrador')           # Crea una Insancia de un Administrador
adm.saludo()
adm.superSaludo()