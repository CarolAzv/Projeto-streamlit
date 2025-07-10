import streamlit as st
import pandas as pd
from src.model.Entidades.Cliente import Cliente 
from src.model.Persistencia.Clientes import Clientes 
from src.model.Persistencia.Vendas import Vendas
from src.model.Entidades.Entregador import Entregador 
from src.model.Persistencia.Entregadores import Entregadores
from src.model.Entidades.Categoria import Categoria 
from src.model.Persistencia.Categorias import Categorias
from src.model.Entidades.Produto import Produto 
from src.model.Persistencia.Produtos import Produtos 

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

        elif opcoes_cliente == "Listar Compras":
            st.subheader("Lista de Compras realizadas")
            todas_vendas = Vendas.listar()
            if todas_vendas:
                dados_vendas = [c.to_dict() for c in todas_vendas]
                
                # Opcional: Converter para DataFrame para mais funcionalidades (filtro, ordenação)
                df_vendas = pd.DataFrame(dados_vendas) 
                
                st.dataframe(df_vendas) # Exibe como uma tabela interativa
            else:
                st.info("Nenhum compra feita ainda.")

        elif opcoes_cliente == "Atualizar dados do Cliente":
            st.subheader("Atualizar cliente")
            st.write("Preencha os dados para atualizar a conta.")
            with st.form("form_atualizar_cliente", clear_on_submit=True):
                id_atl = st.text_input("id da conta a ser atualizada", key="atualizar_id")
                nome_atl = st.text_input("Nome Completo:", key="atualizar_nome")
                email_atl = st.text_input("Email:", key="atualizar_email")
                senha_atl = st.text_input("Senha:", type="password", key="atualizar_senha")
                fone_atl = st.text_input("Telefone:", key="atualizar_fone")

                submitted_atualizacao = st.form_submit_button("Atualizar Cliente")

                if submitted_atualizacao:
                    if not id_atl or not nome_atl or not email_atl or not senha_atl or not fone_atl:
                        st.error("Por favor, preencha todos os campos para a atualização.")
                    else:
                        try:
                            atl_cliente = Cliente(id=id_atl, nome=nome_atl, email=email_atl, senha=senha_atl, fone=fone_atl)
                            Clientes.atualizar(atl_cliente)
                            
                            st.success(f"Cliente '{nome_atl}' atualizado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro na atualização: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

        elif opcoes_cliente == "Excluir Cliente":
            st.subheader("Excluit cliente")
            st.write("Preencha o id para deletar a conta.")
            with st.form("form_deletar_cliente", clear_on_submit=True):
                id_del = st.text_input("id da conta a ser excluida", key="deletetar_id")

                submitted_exclucao = st.form_submit_button("Excluir Cliente")

                if submitted_exclucao:
                    if not id_del:
                        st.error("Por favor, informe o id da conta a ser excluida.")
                    else:
                        try:
                            del_cliente = Cliente(id=id_del, nome="", email="", senha="", fone="")
                            Clientes.excluir(del_cliente)
                            
                            st.success(f"Cliente '{nome_atl}' excluido com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro na exclusão: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")


    with tab_entregadores:
        st.header("Gerenciar Entregadores")
        opcoes_entregador = st.radio(
            "Selecione uma ação:",
            ("Cadastrar Entregador","Listar Entregadores","Atualizar dados do Entregador","Excluir Entregador"),
            key = "radio_entregadores"
        )
        if opcoes_entregador == "Cadastrar Entregador":
            st.subheader("Cadastrar novo Entregador")
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
                            novo_entregador = Entregador(id=0, nome=nome_novo, email=email_novo, senha=senha_nova, fone=fone_novo)
                            Entregadores.inserir(novo_entregador)
                            
                            st.success(f"Entregador '{nome_novo}' cadastrado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro no cadastro: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")
                            
        elif opcoes_entregador == "Listar Entregadores":
            st.subheader("Lista Entregador")
            todos_entregadores = Entregadores.listar()
            if todos_entregadores:
                dados_entregadores = [c.to_dict() for c in todos_entregadores]
                
                # Opcional: Converter para DataFrame para mais funcionalidades (filtro, ordenação)
                df_entregadores = pd.DataFrame(dados_entregadores) 
                
                st.dataframe(df_entregadores) # Exibe como uma tabela interativa
            else:
                st.info("Nenhum entregador cadastrado ainda.")

        elif opcoes_entregador == "Atualizar dados do Entregador":
            st.subheader("Atualizar Entregador")
            st.write("Preencha os dados para atualizar a conta.")
            with st.form("form_atualizar_entregador", clear_on_submit=True):
                id_atl = st.text_input("id da conta a ser atualizada", key="atualizar_id")
                nome_atl = st.text_input("Nome Completo:", key="atualizar_nome")
                email_atl = st.text_input("Email:", key="atualizar_email")
                senha_atl = st.text_input("Senha:", type="password", key="atualizar_senha")
                fone_atl = st.text_input("Telefone:", key="atualizar_fone")

                submitted_atualizacao = st.form_submit_button("Atualizar Entregador")

                if submitted_atualizacao:
                    if not id_atl or not nome_atl or not email_atl or not senha_atl or not fone_atl:
                        st.error("Por favor, preencha todos os campos para a atualização.")
                    else:
                        try:
                            atl_entregador = Entregador(id=id_atl, nome=nome_atl, email=email_atl, senha=senha_atl, fone=fone_atl)
                            Entregadores.atualizar(atl_entregador)
                            
                            st.success(f"Entregador '{nome_atl}' atualizado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro na atualização: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

        elif opcoes_entregador == "Excluir Entregador":
            st.subheader("Excluit entregador")
            st.write("Preencha o id para deletar a conta.")
            with st.form("form_deletar_entregador", clear_on_submit=True):
                id_del = st.text_input("id da conta a ser exluida", key="deletetar_id")

                submitted_exclucao = st.form_submit_button("Excluir Entregador")

                if submitted_exclucao:
                    if not id_del:
                        st.error("Por favor, informe o id da conta a ser excluida.")
                    else:
                        try:
                            del_entregador = Entregador(id=id_del, nome="", email="", senha="", fone="")
                            Entregadores.excluir(del_entregador)
                            
                            st.success(f"Entregador '{nome_atl}' excluido com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro na exclusão: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

    with tab_produtos:
        st.header("Gerenciar Produtos")
        opcoes_produto = st.radio(
            "Selecione uma ação:",
            ("Cadastrar Categoria","Cadastrar Produto","Listar Produtos","Reajustar preço do Porduto"),
            key = "radio_produtos"
        )

        if opcoes_produto == "Cadastrar Categoria":
            st.subheader("Cadastrar nova Categoria")
            st.write("Preencha os dados para criar cstegoria.")
            with st.form("form_cadastro_categoria", clear_on_submit=True):
                descricao_novo = st.text_input("Descrição:", key="cadastro_descricao")

                submitted_cadastro = st.form_submit_button("Cadastrar Categoria")

                if submitted_cadastro:
                    if not descricao_novo:
                        st.error("Por favor, preencha o campo para o cadastro.")
                    else:
                        try:
                            novo_categoria = Categoria(id=0, descricao=descricao_novo)
                            Categorias.inserir(novo_categoria)
                            
                            st.success(f"Categoria '{descricao_novo}' cadastrado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro no cadastro: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

        elif opcoes_produto == "Cadastrar Produto":
            st.subheader("Cadastrar nova Produto")
            st.write("Preencha os dados para criar cstegoria.")
            with st.form("form_cadastro_categoria", clear_on_submit=True):
                descricao_novo = st.text_input("Descrição:", key="cadastro_descricao")

                submitted_cadastro = st.form_submit_button("Cadastrar Produto")

                if submitted_cadastro:
                    if not descricao_novo:
                        st.error("Por favor, preencha o campo para o cadastro.")
                    else:
                        try:
                            novo_produto = Produto(id=0, descricao=descricao_novo)
                            Produtos.inserir(novo_produto)
                            
                            st.success(f"Produto '{nome_novo}' cadastrado com sucesso!")
                            
                        except ValueError as e:
                            st.error(f"Erro no cadastro: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

show()
