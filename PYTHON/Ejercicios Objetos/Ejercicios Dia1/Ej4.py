class Estudiante: 
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
    def promedio(self):
        return(sum(self.notas) / len(self.notas))
    def estado(self):
        if self.promedio() >= 6:
            print("Aprobado!")
        else:
            print("Suspendido!!")

            
estudiante = Estudiante("hahaasd", [10, 5, 6 ,7, 8])
estudiante.estado()