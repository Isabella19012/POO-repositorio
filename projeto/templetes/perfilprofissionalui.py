import streamlit as st
from Service import Service
import time
class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        op = Service.profissional_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especializacao = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(),type="password")
        if st.button("Atualizar"):
            id = op.get_id()
            Service.profissional_atualizar(nome, email, especializacao, senha)
            time.sleep(2)
            st.success("Profissional atualizado com sucesso")