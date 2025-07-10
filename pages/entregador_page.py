import streamlit as st

def show():
    if not st.session_state.get('logged_in') or st.session_state.get('user_type') != 'entregador':
        st.warning("Acesso negado. Por favor, faça login como entregador.")
        st.session_state.pagina_atual = 'login' 
        st.rerun()
        return
    
    st.title("Área do entregador")
    cliente_obj = st.session_state.get('user_object')
    
    st.write("Bem-vindo(a),")
    st.markdown("---")