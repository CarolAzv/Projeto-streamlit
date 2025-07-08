import streamlit as st

def cliente_inserir_ui():
    st.title("Cadastro")
    with st.form("cadastro_cliente_form"):
        nome = st.text_input("Nome completo:")
        email = st.text_input("E-mail:")
        senha = st.text_input("Senha:", type="password") 
        fone = st.text_input("Telefone:")

        submitted = st.form_submit_button("Cadastrar") 

    if submitted:
            try:
                import VisitorView
                VisitorView.abrir_conta(nome, email, senha, fone) 
                st.info("Você pode fazer login agora.")
                st.session_state.logged_in = False
                st.switch_page("Login")

            except ValueError as e:
                st.error(f"Erro ao cadastrar: {e}")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")
        
cliente_inserir_ui()