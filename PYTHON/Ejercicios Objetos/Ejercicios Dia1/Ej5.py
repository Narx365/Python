class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def vender(self):
        vendido = input(f"Introduzca la cantidad vendida de {self.nombre}: ")
        if self.stock > vendido:
            self.stock -= vendido
            print(f"Se han vendido {self.stock} {self.nombre}s, quedan {self.stock}(s). Precio total: {self.precio*vendido}€")
        else:
            print(f"No se pueden vender {vendido} {self.nombre}s, no hay tantas")
    def reponer(self):
        repuesto = input(f"Introduzca la cantidad de {self.nombre} que va a reponer: ")
        if repuesto < 0:
            self.stock += repuesto
            print (f"Se ha repuesto {repuesto} {self.nombre}s")
        else:
            print (f"No se puede reponer un número negativo")
    def mostrar_info(self):
        print(f"Producto: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Cantidad disponible: {self.stock}")
nombre = input("Introduzca el nombre del producto: ")
precio = int(input("Introduzca el precio del producto: "))
stock = int(input("Introduzca la cantidad de producto disponible: "))
prod = Producto(nombre, precio, stock)
prod.vender()
prod.reponer()
prod.mostrar_info()