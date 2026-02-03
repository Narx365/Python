class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self):
        depositado = float(input("Introduzca la cantidad a depositar: "))
        self.saldo += depositado
        print (f"Se han depositado {depositado} dinero correctamente. Saldo total: {self.saldo}")
    def retirar(self):
        restar = float(input("Introduzca la cantidad a retirar: "))
        if self.saldo > restar:
            self.saldo -= restar
            print (f"Se han depositado {restar}dinero correctamente. Saldo total: {self.saldo}")
        else:
            print ("No es posible retirar una cantidad de dinero mayor a la que hay en la cuenta.")
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")
titular = input("Introduzca el titular de la cuenta: ")
saldo = float(input("Introduzca el saldo de la cuenta: "))
cuenta = CuentaBancaria(titular, saldo)
cuenta.depositar()
cuenta.retirar()
cuenta.mostrar_saldo()