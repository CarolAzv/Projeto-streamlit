from src.model.Persistencia.Clientes import Clientes
from src.model.Persistencia.Entregadores import Entregadores


class usuario:
    admin_email = "admin"
    admin_senha = "1234"
    @classmethod
    def login(cls,email,senha):
        email = email.strip().lower()
        if email == cls.admin_email and senha == cls.admin_senha:
            return "admin"
        clientes = Clientes.listar()
        for cliente in clientes:
            if cliente.get_email().lower() == email:
                if cliente.get_senha() == senha:
                    return "cliente"
                else:
                    raise ValueError("Credenciais inválidas: Senha incorreta.")
        entregadores = Entregadores.listar()
        for entregador in entregadores:
            if entregador.get_email().lower() == email:
                if entregador.get_senha() == senha:
                    return "entregador"
                else:  
                    raise ValueError("Credenciais inválidas: Senha incorreta.")
            
        raise ValueError("Credenciais inválidas: Email não cadastrado.")

