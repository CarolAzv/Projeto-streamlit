import streamlit as st
from model.Entidades.Cliente import Cliente
from model.Persistencia.Categorias import Categorias
from model.Persistencia.Produtos import Produtos
from model.Entidades.Categoria import Categoria
from model.Entidades.Produto import Produto
from model.Entidades.Pedido import Pedido
from model.Persistencia.Pedidos import Pedidos
from model.Persistencia.Entregadores import Entregadores
from model.Entidades.Entregador import Entregador
from datetime import datetime
def show():
    if not st.session_state.get('logged_in') or st.session_state.get('tipo_usuario') != 'cliente':
        st.warning("Acesso negado. Por favor, faça login como cliente.")
        st.session_state.pagina_atual = 'login' 
        st.rerun()
        return
    
    st.title("Área do cliente")
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    if "object_usuario" in st.session_state and st.session_state.object_usuario is not None:
        cliente_logado = st.session_state.object_usuario
    
    
        col_esquerda,col_centro,col_direita = st.columns([1,1,0.2])
        with col_esquerda:
            st.write("Bem-vindo(a),",cliente_logado.get_nome())
        with col_direita:
            if st.button("Sair",key = "logout_cliente_page"):
                st.session_state.logged_in = False
                st.session_state.tipo_usuario = None
                st.session_state.obejct_usuario = None

                st.session_state.pagina_atual = "home"
                st.success("Você foi desconectado com sucesso")
                st.rerun()
    

        tab_explorar,tab_compras_anteriores,tab_carrinho = st.tabs([
            "Loja",
            "Compras anteriores",
            "Carrinho de compras"
        ])
        with tab_explorar:
            st.subheader("Explore Nossos Produtos por Categoria")
            todas_categorias = Categorias.listar()
            if not todas_categorias:
                st.info("Nenhuma categoria disponível no momento.")
            else:
                opcoes_categorias_map = {f"{c.get_nome()} (ID: {c.get_id()})": c for c in todas_categorias}
            nomes_categorias_para_selectbox = list(opcoes_categorias_map.keys())

            categoria_selecionada_str = st.selectbox(
                "Selecione uma Categoria:",
                nomes_categorias_para_selectbox,
                key="cliente_select_categoria"
            )
            
            categoria_selecionada_obj = opcoes_categorias_map.get(categoria_selecionada_str)

            if categoria_selecionada_obj:
                st.subheader(f"Produtos em '{categoria_selecionada_obj.get_nome()}'")
                produtos_da_categoria = Produtos.buscar_por_categoria(categoria_selecionada_obj.get_id())

                if not produtos_da_categoria:
                    st.info("Nenhum produto nesta categoria ainda.")
                else:
                    for produto in produtos_da_categoria:
                        st.markdown(f"**{produto.get_nome()}** (ID: {produto.get_id()})")
                        st.write(f"Descrição: {produto.get_descricao()}")
                        st.write(f"Preço: R$ {produto.get_preco():.2f}")
                        st.write(f"Estoque: {produto.get_estoque()}")

                        # Permite selecionar a quantidade
                        quantidade_key = f"qtd_produto_{produto.get_id()}"
                        quantidade = st.number_input(
                            "Quantidade:",
                            min_value=1,
                            max_value=produto.get_estoque(),
                            value=1,
                            key=quantidade_key
                        )

                        # Botão para adicionar ao carrinho
                        if st.button(f"Adicionar {quantidade} ao Carrinho", key=f"add_cart_{produto.get_id()}"):
                            if quantidade > 0 and quantidade <= produto.get_estoque():
                                item_adicionado = {
                                    "produto_id": produto.get_id(),
                                    "nome": produto.get_nome(),
                                    "preco_unitario": produto.get_preco(),
                                    "quantidade": quantidade
                                }
                                # Verifica se o item já está no carrinho para atualizar a quantidade
                                item_existente = next((item for item in st.session_state.cart if item['produto_id'] == produto.get_id()), None)
                                if item_existente:
                                    item_existente['quantidade'] += quantidade
                                else:
                                    st.session_state.cart.append(item_adicionado)
                                st.success(f"{quantidade} '{produto.get_nome()}' adicionado(s) ao carrinho!")
                            else:
                                st.error("Quantidade inválida ou estoque insuficiente.")
                        st.markdown("---") # Separador para produtos

            with tab_compras_anteriores:
                st.header("Minhas Compras Anteriores")
                cliente_id = cliente_logado.get_id()
                
                minhas_compras = [p for p in Pedidos.listar() if p.get_cliente_id() == cliente_id] 

                if not minhas_compras:
                    st.info("Você ainda não fez nenhuma compra.")
                else:
                    for i, pedido in enumerate(minhas_compras):
                        st.subheader(f"Pedido ID: {pedido.get_id()}")
                        st.write(f"Data do Pedido: {pedido.get_data_pedido().strftime('%d/%m/%Y %H:%M')}")
                        st.write(f"Status: **{pedido.get_status()}**")
                        st.write(f"Valor Total: R$ {pedido.get_valor_total():.2f}")
                        st.write(f"Endereço de Entrega: {pedido.get_endereco()}") # Usando o getter correto

                        entregador = Entregadores.listar_id(pedido.get_entregador_id()) if pedido.get_entregador_id() else None
                        entregador_nome = entregador.get_nome() if entregador else "Não Atribuído"
                        st.write(f"Entregador: {entregador_nome}")

                        
                        if pedido.get_itens_pedidos(): 
                            st.write("**Itens:**")
                            for item in pedido.get_itens_pedidos():
                                produto_info = Produtos.listar_id(item.get('produto_id'))
                                produto_nome = produto_info.get_nome() if produto_info else "Produto Desconhecido"
                                
                                st.write(f"- {produto_nome} (Qtd: {item.get('quantidade')}, R$ {item.get('preco_unitario'):.2f} cada)")
                        
                        
                        if st.button("Comprar Novamente", key=f"buy_again_{pedido.get_id()}"):
                            for item in pedido.get_itens_pedidos(): 
                                produto_original = Produtos.listar_id(item.get('produto_id'))
                                if produto_original and produto_original.get_estoque() >= item.get('quantidade'):
                                    item_para_carrinho = {
                                        "produto_id": item.get('produto_id'),
                                        "nome": produto_original.get_nome(),
                                        "preco_unitario": produto_original.get_preco(),
                                        "quantidade": item.get('quantidade')
                                    }
                                    
                                    item_existente_no_carrinho = next((cart_item for cart_item in st.session_state.cart if cart_item['produto_id'] == item.get('produto_id')), None)
                                    if item_existente_no_carrinho:
                                        item_existente_no_carrinho['quantidade'] += item.get('quantidade')
                                    else:
                                        st.session_state.cart.append(item_para_carrinho)
                                    st.success(f"'{produto_original.get_nome()}' adicionado ao carrinho para compra novamente.")
                                else:
                                    st.warning(f"Não foi possível adicionar '{item.get('nome')}' ao carrinho (estoque insuficiente ou produto não encontrado).")
                            st.info("Itens do pedido anterior adicionados ao seu carrinho.")
                            st.rerun() # Recarrega para mostrar o carrinho atualizado
                        st.markdown("---")


            with tab_carrinho:
                st.header("Seu Carrinho de Compras")
                if not st.session_state.cart:
                    st.info("Seu carrinho está vazio.")
                else:
                    total_carrinho = 0
                    for i, item in enumerate(st.session_state.cart):
                        st.markdown(f"**{item['nome']}**")
                        st.write(f"Preço Unitário: R$ {item['preco_unitario']:.2f}")

                        
                        nova_quantidade = st.number_input(
                            f"Quantidade de {item['nome']}:",
                            min_value=0, 
                            value=item['quantidade'],
                            key=f"cart_item_qty_{item['produto_id']}"
                        )

                        if nova_quantidade != item['quantidade']:
                            if nova_quantidade == 0:
                                st.session_state.cart.pop(i) 
                                st.warning(f"'{item['nome']}' removido do carrinho.")
                            else:
                                
                                produto_real = Produtos.listar_id(item['produto_id'])
                                if produto_real and nova_quantidade <= produto_real.get_estoque():
                                    st.session_state.cart[i]['quantidade'] = nova_quantidade
                                    st.success(f"Quantidade de '{item['nome']}' atualizada para {nova_quantidade}.")
                                else:
                                    st.error(f"Estoque insuficiente para {item['nome']}. Máximo disponível: {produto_real.get_estoque() if produto_real else 'N/A'}")
                                    
                                    if produto_real:
                                        st.session_state.cart[i]['quantidade'] = min(nova_quantidade, produto_real.get_estoque())
                                    else:
                                        st.session_state.cart[i]['quantidade'] = item['quantidade'] 
                            st.rerun() 

                        subtotal = item['preco_unitario'] * st.session_state.cart[i]['quantidade'] 
                        st.write(f"Subtotal: R$ {subtotal:.2f}")
                        total_carrinho += subtotal
                        st.markdown("---")

                    st.subheader(f"Total do Carrinho: R$ {total_carrinho:.2f}")

                    if st.button("Finalizar Compra", key="checkout_button"):
                        if not st.session_state.cart:
                            st.warning("Seu carrinho está vazio. Adicione produtos antes de finalizar a compra.")
                        else:
                            try:
                                # 1. Verificar estoque final antes de criar o pedido
                                itens_para_pedido = []
                                for cart_item in st.session_state.cart:
                                    produto_no_estoque = Produtos.listar_id(cart_item['produto_id'])
                                    if not produto_no_estoque or produto_no_estoque.get_estoque() < cart_item['quantidade']:
                                        st.error(f"Estoque insuficiente para '{cart_item['nome']}'. Compra cancelada.")
                                        st.rerun() # Recarrega para o usuário ajustar o carrinho
                                        return

                                    # Reduzir o estoque
                                    produto_no_estoque.set_estoque(produto_no_estoque.get_estoque() - cart_item['quantidade'])
                                    Produtos.atualizar(produto_no_estoque) 

                                    itens_para_pedido.append({
                                        "produto_id": cart_item['produto_id'],
                                        "nome": cart_item['nome'], 
                                        "quantidade": cart_item['quantidade'],
                                        "preco_unitario": cart_item['preco_unitario']
                                    })

                                
                                novo_pedido = Pedido(
                                    id=None, 
                                    cliente_id=cliente_logado.get_id(),
                                    data_pedido=datetime.now(),
                                    status="Pendente",
                                    valor_total=total_carrinho,
                                    endereco=cliente_logado.get_endereco(), 
                                    itens_pedidos=itens_para_pedido,
                                    entregador_id=None,
                                    data_entrega=None

                                )
                                Pedidos.inserir(novo_pedido)

                                st.success(f"Compra finalizada com sucesso! Pedido ID: {novo_pedido.get_id()}.")
                                st.session_state.cart = []
                                st.rerun() 
                            except ValueError as e:
                                st.error(f"Erro ao finalizar compra: {e}")
                            except Exception as e:
                                st.error(f"Ocorreu um erro inesperado ao finalizar a compra: {e}")