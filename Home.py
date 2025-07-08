import streamlit as st
#from categoria import Categorias
#from produto import Produtos
#from cliente import Cliente, Clientes
#from venda import Venda, Vendas
st.title("Mercado eletrônico")
st.header("Bem-vindo(a) Visitante")


col1, col2 = st.columns(2)
with col1:
    if st.button("Entrar"):
        st.switch_page("Login")
with col2:
    if st.button("Cadastro"):
        st.switch_page("Cadastro")

st.markdown("---") 
