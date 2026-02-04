class Persona:
    def __init__ (self, name, age):
        self.name=name
        self.age=age

class Estudiante(Persona):
    def __init__(self, name, age, matricula):
        super().__init__(name, age)
        self.matricula=matricula
    def mostrar(self, name, age, matricula):
        print(f"el estudiante se llama {name}, tiene {age} años y su numero de matricula es {matricula}")

std1 = Estudiante("narx", 17, "0001")
std1.mostrar(std1.name, std1.age, std1.matricula)