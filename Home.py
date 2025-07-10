import streamlit as st


from view.VisitorView import usuario 

from pages.AdminPage import show as show_admin
from pages.cliente_page import show as show_cliente
from pages.entregador_page import show as show_entregador 
from src.model.Entidades.Cliente import Cliente 
from src.model.Persistencia.Clientes import Clientes 


if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = "home" 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_type = None
    st.session_state.user_object = None 

if st.session_state.logged_in:
    mostrar_pages = {
        "admin": show_admin, 
        "cliente": show_cliente,
        "entregador": show_entregador,
    }

    if st.session_state.user_type in mostrar_pages:
        mostrar_pages[st.session_state.user_type]()
    else:
        st.error("Tipo de usuário desconhecido. Por favor, faça login novamente.")
else:

    st.title("Mercado eletrônico")
    st.header("Bem-vindo(a) Visitante")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Entrar", key="btn_entrar_home"):
            st.session_state.pagina_atual = "login"
            st.rerun() 
    with col2:
        if st.button("Cadastre-se", key="btn_cadastro_home"):
            st.session_state.pagina_atual = "cadastro"
            st.rerun() 

    st.markdown("---") 



if st.session_state.pagina_atual == "home":
    st.write("Essa é a página inicial. Escolha uma opção acima.")

# Formulário de Login
elif st.session_state.pagina_atual == "login":
    st.subheader("Área de login")
    with st.form("login_usuario_form"):
        email = st.text_input("E-mail:", key="login_email_input")
        senha = st.text_input("Senha:", type="password", key="login_senha_input")

        submitted = st.form_submit_button("Entrar")

        if submitted:
            if not email or not senha:
                st.error("Por favor, preencha todos os campos.")
            else: 
                try:
                    tipo_usuario_logado = usuario.login(email, senha) 
                    
                   
                    st.session_state.logged_in = True
                    st.session_state.user_type = tipo_usuario_logado 
                    st.session_state.user_email = email 
                    
                    
                    st.success(f"Login bem-sucedido como {tipo_usuario_logado.capitalize()}!")
                    
                    
                    if tipo_usuario_logado == 'admin':
                        st.session_state.pagina_atual = "AdminPage" 
                    elif tipo_usuario_logado == 'cliente':
                        st.session_state.pagina_atual = "cliente_page" 
                    elif tipo_usuario_logado == 'entregador':
                        st.session_state.pagina_atual = "entregador_page" 
                    
                    st.rerun() 

                except ValueError as e:
                    st.error(f"Erro no login: {e}")
                except Exception as e:
                    st.error(f"Ocorreu um erro inesperado: {e}")

#CADASTRO
elif st.session_state.pagina_atual == "cadastro":
    st.subheader("Área de Cadastro")
    st.write("Preencha os dados para criar sua conta.")

    nome_novo = st.text_input("Nome Completo:", key="cadastro_nome")
    email_novo = st.text_input("Email:", key="cadastro_email")
    senha_nova = st.text_input("Senha:", type="password", key="cadastro_senha")
    fone_novo = st.text_input("Telefone:", key="cadastro_fone")

    if st.button("Cadastrar", key="btn_cadastrar"):
        if not nome_novo or not email_novo or not senha_nova or not fone_novo:
            st.error("Por favor, preencha todos os campos para o cadastro.")
            
        try:
            novo_cliente = Cliente(id=0, nome=nome_novo, email=email_novo, senha=senha_nova, fone=fone_novo)
            Clientes.inserir(novo_cliente) 
            
            st.success("Cadastro realizado com sucesso! Você já pode fazer login.")
            st.session_state.pagina_atual = 'login' 
            st.rerun()
        except ValueError as e:
            st.error(f"Erro no cadastro: {e}")
        except Exception as e:
            st.error(f"Ocorreu um erro inesperado: {e}")

     