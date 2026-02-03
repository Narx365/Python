class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        print(f"El area es {self.base * self.altura}")
    def perimetro(self):
        print(f"El perimetro es {self.base*2 + self.altura*2}")
base = int(input("Dame la base: "))
altura = int(input("Dame la altura: "))
rectangulo = Rectangulo(base, altura)
rectangulo.area()
rectangulo.perimetro()