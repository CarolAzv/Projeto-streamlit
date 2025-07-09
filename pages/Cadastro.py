import streamlit as st
from view.VisitorView import VisitorView

def cliente_inserir_ui():
    st.title("Cadastro")
    with st.form("cadastro_cliente_form"):
        nome = st.text_input("Nome completo:")
        email = st.text_input("E-mail:")
        senha = st.text_input("Senha:", type="password") 
        fone = st.text_input("Telefone:")

        submitted1 = st.form_submit_button("Cadastrar como cliente")
        submitted2 = st.form_submit_button("Cadastrar como entregador") 

    if submitted1:
            try:
                VisitorView.abrir_conta_cliente(nome, email, senha, fone) 
                st.info("Você pode fazer login agora.")
                st.session_state.logged_in = False
                st.switch_page("Login")

            except ValueError as e:
                st.error(f"Erro ao cadastrar: {e}")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")

    if submitted2:
            try:
                VisitorView.abrir_conta_entregador(nome, email, senha, fone) 
                st.info("Você pode fazer login agora.")
                st.session_state.logged_in = False
                st.switch_page("Login")

            except ValueError as e:
                st.error(f"Erro ao cadastrar: {e}")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")
        
cliente_inserir_ui()
