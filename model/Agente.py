from model.MaquinaDeMealy import MaquinaDeMealy

class Agente:


    def __init__(self,estadoInicial):
        self.maquinaDeMealy = MaquinaDeMealy(estadoInicial)
        print(self.maquinaDeMealy.funcaoDeTransicao(estadoInicial))
        



