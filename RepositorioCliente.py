from cliente import Cliente

class RepositorioCliente:

    def __init__(self):
         self._clientes = []

    def cadastrar(self, cliente: Cliente):
        if self.buscar(cliente.getCpf()) is None:
            self._clientes.append(cliente)

        else:
            print("Cliente já cadastrado")


    def buscar(self, cpf: str):
        for cliente in self._clientes:
            if cliente.getCpf() == cpf:
                return cliente

        return None



    def atualizar(self, cliente: Cliente):
        pass
    def deletar(self, cpf: str):
        pass
    def listar(self, cliente: Cliente):
        pass



