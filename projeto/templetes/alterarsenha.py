import streamlit as st
import time
from Service import Service

class AlterarSenha:
    def main():
        st.header("Alterar Senha")
        st.text_input("informe a nova s" \
        "enha")
        if st.button("Alterar Senha"):
                time.sleep(2)
                st.rerun()
                st.success("Senha do adm alterada com sucesso")