class Animal:
    def __init__ (self):
        pass
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau Guau")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau Miau")

perro = Perro()
gato = Gato()
perro.hacer_sonido()
gato.hacer_sonido()