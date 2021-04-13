class Animal:
    def __init__(self, nom, sonido):
        self.nom = nom
        self.sonido = sonido
    def saludo(self):
        print ('Hola, soy un',self.tipoAnimal,'y mi sonido es el', self.sonido)

class Gato(Animal):
    tipoAnimal = 'Gato'
    def __init__(self, nom, sonido):
        Animal.__init__(self, nom, sonido)
        print ('Hola soy un', self.tipoAnimal,'EXTENDIDO!')

class Perro(Animal):
    tipoAnimal = 'Perro'
    def __init__(self, nom, sonido):
        super().__init__(nom, sonido)   # Palabra reservada SUPER simpre hace referencia a la CLASE PADRE
        print ('INSTANCIANDO un', self.tipoAnimal)

class Canario(Animal):
    tipoAnimal = 'Canario'

gato = Gato ('Cat','Maullido')
gato.saludo()

perro = Perro ('Pocker', 'Ladrido')
perro.saludo()

canario = Canario ('Piolin', 'Slvido')
canario.saludo()