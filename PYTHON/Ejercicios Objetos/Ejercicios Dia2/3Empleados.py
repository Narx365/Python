class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def mostrar_info(self):
        print(f"Gerente Nombre: {self.nombre}, Salario: ${self.salario}, Departamento: {self.departamento}")


gerente1 = Gerente("Ana", 80000, "Ventas")
gerente1.mostrar_info()