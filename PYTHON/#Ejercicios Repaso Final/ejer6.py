class Empleado:
    def __init__(self, nombre, dni):
        self.nombre= nombre
        self.dni= dni
    def calcular_salario(self):
        pass

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, dni, salario_mensual):
        super().__init__(nombre, dni)
        self.salario_mensual= salario_mensual
    def calcular_salario(self):
            return self.salario_mensual

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, dni, horas_tabajadas, precio_hora):
        super().__init__(nombre, dni)
        self.horas_tabajadas= horas_tabajadas
        self.precio_hora= precio_hora
    def calcular_salario(self):
        return self.horas_tabajadas * self.precio_hora

empleados= [EmpleadoFijo("Ajia", "123M", 1200), 
            EmpleadoPorHoras("Pollato", "123456A", 8, 6),
            EmpleadoFijo("pepino", "31231233G", 1000)
]

print ("Mostrar salario")
for i in empleados:
    print (f"su nombre es {i.nombre}, dni {i.dni} y cobra {i.calcular_salario()}€")

print ("Gasto en salarios")
total= 0
for i in empleados:
    total += i.calcular_salario()
print (f"El gasto total en salarios es de {total} €")

x = float(input("Mostrar empleados que cobren más de X €. X = "))
print(f"EMPLEADOS QUE COBRAN MÁS DE {x}€:")
for e in empleados:
    if e.calcular_salario() > x:
        print(f"{e.nombre} cobra {e.calcular_salario()}€")
