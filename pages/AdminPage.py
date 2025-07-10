import streamlit as st
import pandas as pd
from src.model.Entidades.Cliente import Cliente 
from src.model.Persistencia.Clientes import Clientes 

def show():
    if not st.session_state.get('logged_in') or st.session_state.get('user_type') != 'admin':
        st.warning("Acesso negado. Por favor, faça login como administrador.")
        st.session_state.pagina_atual = 'login' 
        st.rerun()
        return
    
    st.title("Área Administrativa")
    admin_obj = st.session_state.get('user_object')
    col_esquerda,col_centro,col_direita = st.columns([1,1,0.2])
    with col_esquerda:
        st.write("Bem-vindo(a), administrador")
    with col_direita:
        if st.button("Sair",key = "logout_admin_page"):
            st.session_state.logged_in = False
            st.session_state.user_type = None
            st.session_state.user_email = None
            st.session_state.user_object = None

            st.session_state.pagina_atual = "home"
            st.success("Você foi desconectado com sucesso")
            st.rerun()

    st.markdown("---")
    tab_clientes,tab_entregadores,tab_produtos,tab_entregas = st.tabs([
        "Gerenciar Clientes",
        "Gerenciar Entregadores",
        "Gerenciar Produtos",
        "Gerenciar Entregas",
    ])
    with tab_clientes:
        st.header("Gerenciar Clientes")
        opcoes_cliente = st.radio(
            "Selecione uma ação:",
            ("Cadastrar Cliente","Listar Clientes","Listar Compras","Atualizar dados do Cliente","Excluir Cliente"),
            key = "radio_clientes"
        )
        if opcoes_cliente == "Cadastrar Cliente":
            st.subheader("Cadastrar novo cliente")
            st.write("Preencha os dados para criar a conta.")
            with st.form("form_cadastro_cliente", clear_on_submit=True):
                nome_novo = st.text_input("Nome Completo:", key="cadastro_nome")
                email_novo = st.text_input("Email:", key="cadastro_email")
                senha_nova = st.text_input("Senha:", type="password", key="cadastro_senha")
                fone_novo = st.text_input("Telefone:", key="cadastro_fone")

                submitted_cadastro = st.form_submit_button("Cadastrar Cliente")

                if submitted_cadastro:
                    if not nome_novo or not email_novo or not senha_nova or not fone_novo:
                        st.error("Por favor, preencha todos os campos para o cadastro.")
                    else:
                        try:
                            novo_cliente = Cliente(id=0, nome=nome_novo, email=email_novo, senha=senha_nova, fone=fone_novo)
                            Clientes.inserir(novo_cliente)
                            
                            st.success(f"Cliente '{nome_novo}' cadastrado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro no cadastro: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")
        elif opcoes_cliente == "Listar Clientes":
            st.subheader("Lista de clientes cadastrados")
            todos_clientes = Clientes.listar()
            if todos_clientes:
                dados_clientes = [c.to_dict() for c in todos_clientes]
                
                # Opcional: Converter para DataFrame para mais funcionalidades (filtro, ordenação)
                df_clientes = pd.DataFrame(dados_clientes) 
                
                st.dataframe(df_clientes) # Exibe como uma tabela interativa
            else:
                st.info("Nenhum cliente cadastrado ainda.")