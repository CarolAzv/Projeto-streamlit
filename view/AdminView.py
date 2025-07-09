import streamlit as st
from src.model.Entidades.Categoria import Categoria
from src.model.Persistencia.Categorias import Categorias
from src.model.Entidades.Cliente import Cliente
from src.model.Persistencia.Clientes import Clientes
from src.model.Entidades.Produto import Produto
from src.model.Persistencia.Produtos import Produtos

def inserir_catogita(descricao):
    c = Categoria(0, descricao)
    Categorias.inserir(c)

def inserir_catogitaUI():
    st.title("Criar categoria")
    with st.form("inserir_categoria_form"):
        descrição = st.text_input("Descrição:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not descrição:
            st.error("Preencha o campo.")
            return
    try:   
        inserir_catogita(descrição)


def inserir_cliente(nome, email, senha, fone):
    c = Cliente(0, nome, email, senha, fone)
    Clientes.inserir(c)

def inserir_clienteUI():
    st.title("Criar cliente")
    with st.form("inserir_categoria_form"):
        nome = st.text_input("nome:")
        email = st.text_input("email:")
        senha = st.text_input("senha:")
        fone = st.text_input("fone:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not nome or email or senha or fone:
            st.error("Preencha todos os campos.")
            return
    try:   
        inserir_cliente(nome, email, senha, fone)


def inserir_produto(descricao, preco, estoque):
    p = Produto(0, descricao, preco, estoque)
    Produtos.inserir(p)

def inserir_produtoUI():
    st.title("Criar cliente")
    with st.form("inserir_categoria_form"):
        descricao = st.text_input("descrição:")
        preco = st.text_input("preço:")
        estoque = st.text_input("estoque:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not id or descricao or preco or estoque:
            st.error("Preencha todos os campos.")
            return
    try:   
        inserir_produto(descricao, preco, estoque)


def atualizar_preço(id, descricao, preco, estoque):
    c = Produto(id, descricao, preco, estoque)
    Produtos.atualizar(c)

def atualizar_preçoUI():
    st.title("Atualiar cliente")
    with st.form("inserir_categoria_form"):
        id = st.text_input("id do produto a ser atualizado:")
        descricao = st.text_input("nova descrição:")
        preco = st.text_input("novo preço:")
        estoque = st.text_input("novo estoque:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not id or descricao or preco or estoque:
            st.error("Preencha todos os campos.")
            return
    try:   
        atualizar_preço(id, descricao, preco, estoque)


def listar_produtoUI():
    st.title("Atualiar cliente")
    with st.form("inserir_categoria_form"):
        id = st.text_input("id do produto a ser atualizado:")
        descricao = st.text_input("nova descrição:")
        preco = st.text_input("novo preço:")
        estoque = st.text_input("novo estoque:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not id or descricao or preco or estoque:
            st.error("Preencha todos os campos.")
            return
    try:   
        atualizar_preço(id, descricao, preco, estoque)
