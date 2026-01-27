class perro:
    especie = "mamifero"
    def __init__(self, nombre, raza):
        print(f"Creando perro: {nombre}, Raza: {raza}")
        self.nombre = nombre
        self.raza = raza

mi_perro = perro("Odín", "Mastin")

print(mi_perro.nombre)
print(mi_perro.raza)