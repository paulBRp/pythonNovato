class lavadora:
    def __int__(self):
        pass
    def lavar (self,temperatuta='caliente'):
        self._llenar_tanque_de_agua(temperatuta)
        self._lavar()
        self._anadir_jabon()
        self._centrifugar()
    
    def _llenar_tanque_de_agua(self,temperatuta):
        print(f'Llenando el tanque con agua {temperatuta}')

    def _anadir_jabon(self):
        print('Anadiendo jabon')

    def _lavar(self):
        print('Lavar')

    def _centrifugar(self):
        print('Centrifugando')
    
if  __name__ == "__main__":
    lavadora=lavadora()
    lavadora.lavar()

    
