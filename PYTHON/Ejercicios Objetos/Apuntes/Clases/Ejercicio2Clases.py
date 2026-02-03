class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura 

    def perimetro(self):
        return(self.base + self.altura) * 2

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

rectangulo = Rectangulo(base, altura)
print(f"El área del rectángulo es: {rectangulo.area()}")
print(f"El perímetro del rectángulo es: {rectangulo.perimetro()}")