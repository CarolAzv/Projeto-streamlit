import streamlit as st

def DelivererPage():
    st.title("Mercado eletrônico")
    st.header("Bem-vindo(a) Visitante")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Listar minhas entregas"):
            st.switch_page("Categorias")
    with col2:
        if st.button("Confirmar entrega"):
           st.switch_page("Clientes")

DelivererPage()
