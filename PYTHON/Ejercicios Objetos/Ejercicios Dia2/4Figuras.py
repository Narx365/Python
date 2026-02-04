import math
class Figura:
    def calcular_area():
        pass

class Rectangulo(Figura):
    def __init__ (self, base, altura):
        self.base=base
        self.altura=altura

    def calcular_area(self):
        print(f"el area del rectangulo es {self.base*self.altura}")

class Circulo(Figura):
    def __init__ (self, radio):
        self.radio=radio

    def calcular_area(self):
        print(f"el area del circulo es de {math.pi*(self.radio*self.radio)}")

Rectangulo1 = Rectangulo(5, 6)
Circulo1 = Circulo(2)
Rectangulo1.calcular_area()
Circulo1.calcular_area()
