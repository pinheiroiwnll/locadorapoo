from cliente import Cliente

class RepositorioCliente:

    def __init__(self):
         self._clientes = []

    def cadastrar(self, cliente: Cliente):
          if self.buscar(cliente.getCpf()) is None:
            self._clientes.append(cliente)
          else:
            print("Cliente ja foi cadastrado")

    def buscar(self, cpf: str):
        for cliente in self._clientes:
           if cliente.getCpf() == cpf:
                return cliente
           else:
                return None

    def atualizar(self, cliente: Cliente):
         if self.buscar(cliente.get_Cpf()) is None:
            print("Cliente n foi encontrado")
         else:
            print("Nome {}".format(cliente.get_Nome()))
            print("Endereço {}".format(cliente.get_Endereco()))

    def deletar(self, cpf: str):
        for cliente in self._clientes:
            if cpf == cliente.get_Cpf():
                self._clientes.pop(self._clientes.index(cliente))
                print("Cliente {} foi deletado da lista".format(cpf))
            else:
                print("Cliente n foi encontrado")

    def listar(self):
        return self._clientes
