class Personaje:
    def __init__ (self, nombre, nivel):
        self.nombre=nombre
        self.nivel=nivel
class Mago(Personaje):
    def __init__ (self, nombre, nivel, mana):
        super().__init__(nombre, nivel)
        self.mana=mana
    
    def fireball(self):
        if self.mana>10:    
            self.mana=self.mana-10
            print(f"{self.nombre} usa el hechizo fireball, gastando 10 de mana, ahora tiene un total de {self.mana} mana!")
        else:
            print(f"no tienes suficiente mana <mana total es {self.mana}>")

ent1 = Mago("narx", 15, 200)
ent1.fireball()