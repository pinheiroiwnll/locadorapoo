from operacao import Operacao


class RepositorioOperacao(Operacao):

    def __init__(self, cpf: str, codigo: int):
        super().__init__(cpf, codigo)
        self.operacoes = []

    def cadastrar(self, operacao: Operacao):

    def buscarReservas(self, cpf):


    def buscarLocacoes(self, cpf):


    def deletarReservas(self, cpf, codigo):


    def deletarLocacao(self, cpf, codigo):


    def listarLocacoes(self, cpf):


    def numeroLocacoes(self, cpf):


    def numeroLocacoes(self, codigo):


    def numeroLocacoesAtivas(self, cpf):


    def numeroLocacoesAtivas(self, codigo):


    def numeroReservas(self, codigo):
        