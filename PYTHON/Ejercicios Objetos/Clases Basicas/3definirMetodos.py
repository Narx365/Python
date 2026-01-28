class Perro:
    especie = "Mamífero"
    def __init__(self, nombre, raza):
        print(f"Creando perro: {nombre}, Raza: {raza}")
        self.nombre = nombre
        self.raza = raza
    
    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"caminando {pasos} pasos")

mi_perro = Perro("Odín", "Mastin")
mi_perro.ladra()
mi_perro.camina(10)