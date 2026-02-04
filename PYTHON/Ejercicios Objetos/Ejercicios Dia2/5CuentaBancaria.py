class CuentaBancaria:
    def __init__ (self, titular, saldo):
        self.titular=titular
        self.saldo=saldo

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes_anual):
        super().__init__(titular, saldo)
        self.interes_anual=interes_anual
    def Calculo_saldo (self, saldo, interes_anual):
        print(self.saldo+(self.saldo*(self.interes_anual/100)))

cuenta1 = CuentaAhorro("narx", 1500, 5)
cuenta1.Calculo_saldo(cuenta1.saldo, cuenta1.interes_anual)