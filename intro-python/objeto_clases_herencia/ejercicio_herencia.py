
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def saludo (self):
        print ('Hola, soy un,' , self.tipo, 'me llamo', self.nombre, 'y mi sonido es', self.sonido)

class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
        
"""  def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def saludo (self):
        print ('Hola, soy un Gato y mi sonido es el', self.sonido)
"""

class Perro(Animal):
    tipo = 'Perro'
"""  def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def saludo (self):
        print ('Hola, soy un Perro y mi sonido es', self.sonido)
"""

class Canario(Animal):
    tipo = 'Canario'

gato = Gato ('Max', 'Maullido')
gato.saludo()

perro = Perro ('Pocker', 'Ladrido')
perro.saludo()

canario = Canario ('Piolin', 'Silvido')
canario.saludo()