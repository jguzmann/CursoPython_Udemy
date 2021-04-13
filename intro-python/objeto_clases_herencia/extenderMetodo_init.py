
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def saludo (self):
        print ('Hola, soy un,' , self.tipo, 'me llamo', self.nombre, 'y mi sonido es', self.sonido)

class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, sonido):
        Animal.__init__(self, nombre, sonido)
        print ('Soy un Gato Extendido')

class Perro(Animal):
    tipo = 'Perro'
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
        print ('Instanciando un Perro')

class Canario(Animal):
    tipo = 'Canario'

gato = Gato ('Max', 'Maullido')
gato.saludo()

perro = Perro ('Pocker', 'Ladrido')
perro.saludo()

canario = Canario ('Piolin', 'Silvido')
canario.saludo()