import streamlit as st
from datetime import datetime

from model.Entidades.Entregador import Entregador
from model.Entidades.Pedido import Pedido
from model.Persistencia.Pedidos import Pedidos
from model.Persistencia.Clientes import Clientes
from model.Persistencia.Produtos import Produtos

def show():
    
    if not st.session_state.get('logged_in') or st.session_state.get('tipo_usuario') != 'entregador':
        st.warning("Acesso negado. Por favor, faça login como entregador.")
        st.session_state.pagina_atual = 'login'
        st.rerun()
        return

    st.title("Área do Entregador")

    
    if "object_usuario" in st.session_state and st.session_state.object_usuario is not None:
        entregador_logado = st.session_state.object_usuario
        
        
        col_esquerda, col_centro, col_direita = st.columns([1, 1, 0.2])
        with col_esquerda:
            st.write("Bem-vindo(a),", entregador_logado.get_nome())
        with col_direita:
            if st.button("Sair", key="logout_entregador_page"):
                st.session_state.logged_in = False
                st.session_state.tipo_usuario = None
                st.session_state.object_usuario = None
                st.session_state.pagina_atual = "home"
                st.success("Você foi desconectado com sucesso")
                st.rerun()
        st.markdown("---")

        
        tab_pendentes, tab_concluidas = st.tabs([
            "Entregas Pendentes",
            "Entregas Concluídas"
        ])

        
        with tab_pendentes:
            st.header("Entregas Pendentes")
            
            # Filtra os pedidos que estão atribuídos a este entregador e não foram entregues/cancelados
            pedidos_pendentes = [
                p for p in Pedidos.listar() 
                if p.get_entregador_id() == entregador_logado.get_id() and 
                   p.get_status() not in ["Entregue", "Cancelado"]
            ]

            if not pedidos_pendentes:
                st.info("Nenhuma entrega pendente no momento.")
            else:
                
                pedidos_pendentes.sort(key=lambda p: p.get_data_pedido())

                for i, pedido in enumerate(pedidos_pendentes):
                    st.markdown(f"---")
                    st.subheader(f"Pedido ID: {pedido.get_id()}")
                    
                    cliente = Clientes.listar_id(pedido.get_cliente_id())
                    cliente_nome = cliente.get_nome() if cliente else "Cliente Desconhecido"
                    st.write(f"**Cliente:** {cliente_nome} (ID: {pedido.get_cliente_id()})")
                    st.write(f"**Endereço de Entrega:** {pedido.get_endereco()}")
                    st.write(f"**Status Atual:** {pedido.get_status()}")
                    st.write(f"**Valor Total:** R$ {pedido.get_valor_total():.2f}")

                    if pedido.get_itens_pedidos():
                        st.write("**Itens do Pedido:**")
                        for item in pedido.get_itens_pedidos():
                            produto_info = Produtos.listar_id(item.get('produto_id'))
                            produto_nome = produto_info.get_nome() if produto_info else "Produto Desconhecido"
                            st.markdown(f"- **{produto_nome}** (Qtd: {item.get('quantidade')}, R$ {item.get('preco_unitario'):.2f} cada)")
                    else:
                        st.info("Nenhum item detalhado para este pedido.")

                    
                    if st.button(f"Confirmar Entrega do Pedido {pedido.get_id()}", key=f"confirm_delivery_{pedido.get_id()}"):
                        try:
                            pedido.set_status("Entregue")
                            pedido.set_data_entrega(datetime.now()) 
                            Pedidos.atualizar(pedido)
                            st.success(f"Entrega do Pedido ID {pedido.get_id()} confirmada com sucesso!")
                            st.rerun() 
                        except ValueError as e:
                            st.error(f"Erro ao confirmar entrega: {e}")
                        except Exception as e:
                            st.error(f"Ocorreu um erro inesperado: {e}")

        
        with tab_concluidas:
            st.header("Histórico de Entregas Concluídas")
            
            
            pedidos_concluidos = [
                p for p in Pedidos.listar() 
                if p.get_entregador_id() == entregador_logado.get_id() and 
                   p.get_status() == "Entregue"
            ]

            if not pedidos_concluidos:
                st.info("Nenhuma entrega concluída ainda.")
            else:
                
                pedidos_concluidos.sort(key=lambda p: p.get_data_entrega() if p.get_data_entrega() else datetime.min, reverse=True)

                for i, pedido in enumerate(pedidos_concluidos):
                    st.markdown(f"---")
                    st.subheader(f"Pedido ID: {pedido.get_id()}")
                    
                    cliente = Clientes.listar_id(pedido.get_cliente_id())
                    cliente_nome = cliente.get_nome() if cliente else "Cliente Desconhecido"
                    st.write(f"**Cliente:** {cliente_nome} (ID: {pedido.get_cliente_id()})")
                    st.write(f"**Endereço de Entrega:** {pedido.get_endereco()}")
                    st.write(f"**Status:** {pedido.get_status()}")
                    st.write(f"**Valor Total:** R$ {pedido.get_valor_total():.2f}")
                    st.write(f"**Data de Entrega:** {pedido.get_data_entrega().strftime('%d/%m/%Y %H:%M') if pedido.get_data_entrega() else 'N/A'}")

                    if pedido.get_itens_pedidos():
                        st.write("**Itens do Pedido:**")
                        for item in pedido.get_itens_pedidos():
                            produto_info = Produtos.listar_id(item.get('produto_id'))
                            produto_nome = produto_info.get_nome() if produto_info else "Produto Desconhecido"
                            st.markdown(f"- **{produto_nome}** (Qtd: {item.get('quantidade')}, R$ {item.get('preco_unitario'):.2f} cada)")
                    else:
                        st.info("Nenhum item detalhado para este pedido.")

    else:
        st.error("Erro: Dados do entregador não encontrados na sessão. Por favor, tente novamente.")
        if st.button("Voltar para o Login", key="back_to_login_error_entregador"):
            st.session_state.pagina_atual = 'login'
            st.rerun()

