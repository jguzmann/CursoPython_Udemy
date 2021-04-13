# Herencia
# Es un concepto que se utiliza en programación orientada a objetos para poder reutilizar lo máximo posible el código en estructuras que sean similares.

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print ('Hola, Mi Nombre es: ', self.nombre, self. apellido)

class Admin(Usuario):
    def superSaludo (self):
        print ('Hola me llamo, ', self.nombre, 'y soy Administrador')

admin = Admin('Super', 'Administrador')
admin.saludo()
admin.superSaludo()

