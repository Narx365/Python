class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.historial_movimientos = []

    def ingresar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad de dinero invalida")
        else:
            self.saldo += cantidad
            self.historial_movimientos.append(cantidad)
            print(f"Ingreso de: +{cantidad}€")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad de dinero invalida")
        elif cantidad > self.saldo:
            print("No tienes suficiente saldo")
        else:
            self.saldo -= cantidad
            self.historial_movimientos.append(-cantidad)
            print(f"Retirada de: -{cantidad}€")

    def mostrar_historial(self):
        if len(self.historial_movimientos) == 0:
            print("No hay movimientos")
        else:
            print("Historial de movimientos:")
            for m in self.historial_movimientos:
                print(m)

    def mostrar_saldo(self):
        print(f"Tienes un saldo de: {self.saldo}€")

cuenta = CuentaBancaria("Iván", 300)

while True:
    print("\n1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Mostrar saldo")
    print("4. Mostrar historial")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        cantidad = float(input("Cantidad a ingresar: "))
        cuenta.ingresar(cantidad)

    elif opcion == "2":
        cantidad = float(input("Cantidad a retirar: "))
        cuenta.retirar(cantidad)

    elif opcion == "3":
        cuenta.mostrar_saldo()

    elif opcion == "4":
        cuenta.mostrar_historial()

    elif opcion == "5":
        print("Hasta luego")
        break

    else:
        print("Opción no válida")