class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad): 
        if cantidad <= 0:
            print("La cantidad a depositar debe ser mayor que cero.")
            return
        else:
            self.saldo = self.saldo + cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        
    
    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor que cero.")
            return
        else:
            self.saldo = self.saldo - cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
    
    def mostrar_saldo(self):
        print(f"El saldo actual de la cuenta es: {self.saldo}")

opcion = 0
while opcion != 5:
    print( "menu de opciones")
    print("1. Crear cuenta bancaria")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Mostrar saldo")
    print( "5. Salir")
    opcion = int(input("Seleccione una opción (1-5): "))
    if opcion == 1:
        titular = input("Ingrese el nombre del titular de la cuenta: ")
        cuenta = CuentaBancaria(titular)
        print(f"Cuenta bancaria creada para {titular}.")
    elif opcion == 2:
        if 'cuenta' in locals():
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)

            