import streamlit as st

def ClientPage():
    st.title("Mercado eletrônico")
    st.header("Bem-vindo(a) Cliente")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)

    with col1:
        if st.button("Listar minhas compras"):
            st.switch_page("Categorias")
    with col2:
        if st.button("Comprar novamente"):
           st.switch_page("Clientes")
    with col3:
        if st.button("Listar produtos"):
            st.switch_page("Entregadores")
    with col4:
        if st.button("Inserir produto no carrinho"):
           st.switch_page("Produtos")
    with col5:
        if st.button("Visualizar o carrinho"):
            st.switch_page("Reajustar")
    with col6:
        if st.button("Confimar a compra"):
           st.switch_page("Listar")

ClientPage()
