"""
La orientación a objetos contiene, OBJETOS, CLASES y también HERENCÍA.
Y nosotros vamos a ver eso durante esta sección.
Los objetos en Python son un tipo de dato que contiene propiedades y métodos.
"""

class  Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    ### Metodos ###
    def saludo (self):
        print ('Hola mi nobre es: ', self.nombre, self.apellido)



# usuario = Usuario('Juan', 'Guzman')
usuario2 = Usuario('Marta', 'Castro').saludo()

Usuario('Juan', 'Guzman').saludo()
# usuario2.saludo()

# Eliminar las propiedades que tenga la instacia

# del usuario.saludo()
# del usuario




