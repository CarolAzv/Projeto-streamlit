from src.model.Entidades.Cliente import Cliente
from src.model.Persistencia.Clientes import Clientes
from src.model.Entidades.Entregador import Entregador
from src.model.Persistencia.Entregadores import Entregadores

class VisitorView:
    def abrir_conta_cliente(nome, email, senha, fone):
        c = Cliente(0, nome, email, senha, fone)
        Clientes.inserir(c)

    def abrir_conta_entregador(nome, email, senha, fone):
        c = Entregador(0, nome, email, senha, fone)
        Entregadores.inserir(c)
