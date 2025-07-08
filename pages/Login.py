import streamlit as st
def login():
    st.title("Login")
    with st.form("login_cliente_form"):
        email = st.text_input("E-mail:")
        senha = st.text_input("Senha:",type="password")
    
        submitted = st.form_submit_button("Entrar")
    if submitted:
        if not email or not senha:
            st.error("Preencha todos os campos.")
            return
    try:
                
        user_type = VisitorView.autenticar_usuario(email, senha)

        if user_type == "Admin":
            st.success("Login de Admin bem-sucedido!")
            st.switch_page("AdminPage") 
        elif user_type == "Client":
            st.success("Login de Cliente bem-sucedido!")
            st.switch_page("ClientPage") 
        elif user_type == "Deliverer":
            st.success("Login de Entregador bem-sucedido!")
            st.switch_page("DelivererPage") 
        else:
            st.error("Tipo de usuário desconhecido.") 

    except ValueError as e:
            st.error(f"Erro de Login: {e}") 
    except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}") 
login()