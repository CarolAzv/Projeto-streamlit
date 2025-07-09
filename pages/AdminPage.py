import streamlit as st
from view.AdminView import AdminView

def AdminPage():
    st.title("Mercado eletrônico")
    st.header("Bem-vindo(a) Admin")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    col5, col6, col7 = st.columns(3)
    #col5, col6 = st.columns(2)
    #col7 = st.columns(1)

    with col1:
        if st.button("Cadastrar categorias"):
            AdminView.inserir_catogitaUI()
    with col2:
        if st.button("Cadastrar clientes"):
           st.switch_page("Clientes")
    with col3:
        if st.button("Cadastrar entregadores"):
            st.switch_page("Entregadores")
    with col4:
        if st.button("Cadastrar produtos"):
           st.switch_page("Produtos")
    with col5:
        if st.button("Reajustar preço de produtos"):
            st.switch_page("Reajustar")
    with col6:
        if st.button("Listar as compras"):
           st.switch_page("Listar")
    with col7:
        if st.button("Iniciar a entrega"):
            st.switch_page("IniciarEntregas")

AdminPage()
