import streamlit as st
from src.model.Entidades.Categoria import Categoria
from src.model.Persistencia.Categorias import Categorias
from src.model.Entidades.Cliente import Cliente
from src.model.Persistencia.Clientes import Clientes
from src.model.Entidades.Entregador import Entregador
from src.model.Persistencia.Entregadores import Entregadores
from src.model.Entidades.Produto import Produto
from src.model.Persistencia.Produtos import Produtos

class AdminView:

    def inserir_catogita(descricao):
        c = Categoria(0, descricao)
        Categorias.inserir(c)


    def inserir_cliente(nome, email, senha, fone):
        c = Cliente(0, nome, email, senha, fone)
        Clientes.inserir(c)


    def inserir_entregador(nome, email, senha, fone):
        e = Entregador(0, nome, email, senha, fone)
        Entregadores.inserir(e)


    def inserir_produto(descricao, preco, estoque):
        p = Produto(0, descricao, preco, estoque)
        Produtos.inserir(p)
