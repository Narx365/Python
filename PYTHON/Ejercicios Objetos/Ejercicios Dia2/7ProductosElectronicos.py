class Producto:
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia_meses):
        super().__init__(nombre, precio)
        self.garantia_meses=garantia_meses
    
    def mostrar(self):
        print(f"producto {self.nombre} de precio {self.precio}€ y {self.garantia_meses} meses de garantía")

ent1 = ProductoElectronico("pc", 500, 6)
ent1.mostrar(ent1.nombre, ent1.precio, ent1.garantia_meses)