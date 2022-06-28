from operacao import Operacao

class Locacao(Operacao):

    def __init__(self, cpf: str, codigo: int):
        super().__init__(cpf, codigo)
        self.periodo = int()

    def setPeriodo(self, periodo: int):
        self.periodo = periodo

    def getPeriodo(self):
        return self.periodo
