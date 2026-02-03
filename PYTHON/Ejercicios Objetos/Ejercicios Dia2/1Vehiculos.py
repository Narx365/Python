class Vehiculo:
    def __init__(self, marca, velocidad_maxima):
        self.marca = marca
        self.velocidad_maxima = velocidad_maxima

class Auto(Vehiculo):
    def __init__(self, marca, velocidad_maxima, cantidad_puertas):
        super().__init__(marca, velocidad_maxima)
        self.cantidad_puertas = cantidad_puertas
    
    def mostrar_info(self):
        print(f"Auto Marca: {self.marca}, Velocidad Máxima: {self.velocidad_maxima} km/h, Número de Puertas: {self.numero_puertas}")

ent1 = Auto("Toyota", 180, 4)
ent1.mostrar_info()