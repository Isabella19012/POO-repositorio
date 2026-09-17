import streamlit as st
from Service import Service

class LoginUI:
    @staticmethod
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")

        if st.button("Entrar"):
            c = Service.cliente_autenticar(email, senha)
            p = Service.profissionl_autenticar(email, senha)

            if c:
                st.session_state["usuario_id"] = c["id"]
                st.session_state["usuario_nome"] = c["nome"]
                st.session_state["perfil"] = "cliente"
                st.rerun()
            elif p:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.session_state["perfil"] = "profissional"
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos")