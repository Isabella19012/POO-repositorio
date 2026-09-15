import streamlit as st
from Service import Service
import time
class PerfilClienteUI:
    def main():
        st.header("Meus Dados")
        op = Service.cliente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
        if st.button("Atualizar"):
            id = op.get_id()
            Service.cliente_atualizar(id, nome, email, senha, fone,0)
            time.sleep(2)
            st.success("Cliente atualizado com sucesso")