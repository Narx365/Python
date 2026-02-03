class Clase:
    def metodo(self):
        return 'metodo normal', self
    
    @classmethod
    def metododeclase(cls):
        return 'metodo de clase', cls
    
    @staticmethod
    def metodoestatico():
        return "metodo estatico"
    