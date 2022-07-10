from filme import Filme

class RepositorioFilme:
    def __init__(self):
        self._filmes = []

    def cadastrar(self, filme: Filme):
        if self.buscar(filme.get_Codigo()) is None:
            self._filmes.append(filme)
            print("{} adicionado na lista".format(filme.get_Titulo()))
        else:
            print("Esse filme ja foi cadastrado")

    def buscar(self, codigo: int):
        for filme in self._filmes:
            if filme.get_Codigo() == codigo:
                return filme
            else:
                return None

    def atualizar(self, filme: Filme):
        if self.buscar(filme.get_Codigo()) is None:
            print("Filme n foi encontrado")
        else:
            filme.set_Titulo(filme.get_Titulo())
            filme.set_Genero(filme.get_Genero())
            filme.set_DataLancamento(filme.get_DataLancamento())
            filme.set_Diretor(filme.get_Diretor())
            filme.set_Atores(filme.get_Atores())
            filme.set_Sinopse(filme.get_Sinopse())
            filme.set_Produtores(filme.get_Produtores())
            filme.set_precoLocacao(filme.get_precoLocacao())
            filme.set_numeroCopias(filme.get_numeroCopias())

    def deletar(self, codigo: int()):
        for filme in self._filmes:
            if codigo == filme.get_Codigo():
                self._filmes.pop(self._filmes.index(filme))
                print("Filme {} deletado da lista".format(filme.get_Titulo()))
            else:
                print("Filme n foi encontrado")

    def listar(self):
        return self._filmes
