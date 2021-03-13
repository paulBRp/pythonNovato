class Automovil:

    def __int__(self,modelo,marca,color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self._estado='En reposo'
        self._motor=Motor(cilindro=4)

    def acelerar(self, tipo='despacio'):
        if tipo=='rapido'
            self._motor.inyecta_gasolina()
            
class Motor:
    def __init__(self, cilindro, tipo='gasolina'):
        self.cilindros=cilindros
        self.tipo=tipo
        self._temperatura=0

    def inyecta_gasolina(self,cantidad):
        pass