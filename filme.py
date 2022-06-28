import datetime

class Filme:

    def __init__(self, codigo: int, titulo: str):
        self.codigo = codigo
        self.titulo = titulo
        self.genero = []
        self.datalancamento = str()
        self.diretor = str()
        self.atores = []
        self.sinopse = str()
        self.produtores = []
        self.precolocacao = float()
        self.numerocopias = int()

    def setCodigo(self, codigo: int):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def setTitulo(self, titulo: str):
        self.titulo = titulo

    def getTitulo(self):
        return self.titulo

    def setGenero(self, genero):
        self.genero = genero

    def getGenero(self):
        return self.genero

    def addGenero(self, genero: str):
        self.genero += genero

    def setdatalancamento(self, datalancamento: str):
        self.datalancamento = datalancamento

    def getdatalancamento(self):
        return self.datalancamento

    def setDiretor(self, diretor:str):
        self.diretor = diretor

    def getDiretor(self):
        return self.diretor

    def setAtores(self, atores):
        self.atores = atores

    def getAtores(self):
        return self.atores

    def addAtor(self, ator):
        self.atores += ator

    def setSinopse(self, sinopse: str):
        self.sinopse = sinopse

    def getSinopse(self):
        return self.sinopse

    def setProdutores(self, produtores):
        self.produtores = produtores

    def getProdutores(self):
        return self.produtores

    def addProdutor(self, produtor: str):
        self.produtores += produtor

    def setprecolocacao(self, precolocacao: float):
        self.precolocacao = precolocacao

    def getPrecoLocacao(self):
        return self.precoLocacao

    def setnumerocopias(self, numerocopias: int):
        self.numerocopias = numerocopias

    def getnumerocopias(self):
        return self.numerocopias

    def imprimir(self):
        return print('código', self.codigo, 'filme', self.titulo, 'gênero', self.genero, 'data de lançamento', self.datalancamento,
                     'atores', self.atores, 'diretor', self.diretor, 'sinopse', self.sinopse)
