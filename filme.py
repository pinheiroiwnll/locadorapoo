from datetime import date


class Filme:

    def __init__(self, codigo: int, titulo: str):
        self._codigo = codigo
        self._titulo = titulo
        self._generos = []
        self._datalancamento = date.today()
        self._diretor = str()
        self._atores = []
        self._sinopse = str()
        self._produtores = []
        self._precolocacao = float()
        self._numerocopias = int()

    def setCodigo(self, codigo: int):
        self._codigo = codigo

    def getCodigo(self):
        return self._codigo

    def setTitulo(self, titulo: str):
        self._titulo = titulo

    def getTitulo(self):
        return self._titulo

    def setGeneros(self, generos):
        self._generos = generos

    def getGeneros(self):
        return self._generos

    def addGenero(self, genero: str):
        self._generos.append(genero)

    def setdatalancamento(self, datalancamento: date):
        self._datalancamento = datalancamento

    def getdatalancamento(self):
        return self._datalancamento

    def setDiretor(self, diretor: str):
        self._diretor = diretor

    def getDiretor(self):
        return self._diretor

    def setAtores(self, atores):
        self._atores = atores

    def getAtores(self):
        return self._atores

    def addAtor(self, ator):
        self._atores.append(ator)

    def setSinopse(self, sinopse: str):
        self._sinopse = sinopse

    def getSinopse(self):
        return self._sinopse

    def setProdutores(self, produtores):
        self._produtores = produtores

    def getProdutores(self):
        return self._produtores

    def addProdutor(self, produtor: str):
        self._produtores.append(produtor)

    def setprecolocacao(self, precolocacao: float):
        self._precolocacao = precolocacao

    def getPrecoLocacao(self):
        return self.precoLocacao

    def setnumerocopias(self, numerocopias: int):
        self._numerocopias = numerocopias

    def getnumerocopias(self):
        return self._numerocopias

    def imprimir(self):
        return print('codigo', self._codigo, 'filme', self._titulo, 'generos', self._generos, 'data de lançamento',
                     self._datalancamento,
                     'atores', self._atores, 'diretor', self._diretor, 'sinopse', self._sinopse)
