from operacao import Operacao

class Reserva(Operacao):

    def __init__(self, cpf: str, codigo: int):
        super().__init__(cpf, codigo)
        self._prioridade = int()

    def setPrioridade(self, prioridade: int):
        self._prioridade = prioridade

    def getPrioridade(self):
        return self._prioridade
