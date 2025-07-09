import streamlit as st
import sys
import os

folder_path = os.path.abspath('src/model/Entidades/Categoria')
sys.path.append(folder_path)

from Categoria import Categoria

def inserir_catogita(descricao):
    c = Categoria(0, descricao)
    Categorias.inserir(c)

def inserir_catogitaUI():
    st.title("Criar categoria")
    with st.form("inserir_categoria_form"):
        descrição = st.text_input("Descrição:")

        submitted = st.form_submit_button("Finalizar")

    if submitted:
        if not descrição:
            st.error("Preencha o campo.")
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



    #descricao = input("Informe a descrição: ")
    #    c = Categoria(0, descricao)
    #    Categorias.inserir(c)
