class Dispositivo:
    def __init__ (self, encendido):
        self.encendido = encendido
    
class Telefono(Dispositivo):
    def __init__ (self, encendido):
        super().__init__(encendido)
        
    def llamar(self):
        if self.encendido == True:
            return "Llamando..."
        else:
            return "El teléfono está apagado"

ent1=Telefono(False)
print(ent1.llamar())