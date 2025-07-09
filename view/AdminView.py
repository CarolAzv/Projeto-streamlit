import streamlit as st
#need to import Categoria
#need to import Cliente

def inserir_catogita(descricao):
    Categorias.inserir(0, descricao)

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

def inserir_catogita(descricao):
    Categorias.inserir(0, descricao)

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
        inserir_catogita(descricao)


def inserir_cliente(id, nome, email, senha, fone):
    Cliente.inserir(id, nome, email, senha, fone)

def inserir_clienteUI():
    st.title("Criar cliente")
    with st.form("inserir_categoria_form"):
        id = st.text_input("id:")
        nome = st.text_input("nome:")
        email = st.text_input("email:")
        senha = st.text_input("senha:")
        fone = st.text_input("fone:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not id or nome or email or senha or fone:
            st.error("Preencha todos os campos.")
            return
    try:   
        inserir_cliente(id, nome, email, senha, fone)

def inserir_produto(id, descricao, preco, estoque):
    Produto(id, descricao, preco, estoque)

def inserir_produtoUI():
    st.title("Criar cliente")
    with st.form("inserir_categoria_form"):
        id = st.text_input("id:")
        descricao = st.text_input("descrição:")
        preco = st.text_input("preço:")
        estoque = st.text_input("estoque:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not id or descricao or preco or estoque:
            st.error("Preencha todos os campos.")
            return
    try:   
        inserir_produto(id, nome, email, senha, fone)
