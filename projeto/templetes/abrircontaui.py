import streamlit as st
from Service import Service
import time
class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        fone = st.text_input("Informe o fone")
        
        if st.button("Inserir"):
            Service.cliente_inserir(nome, email, senha, fone,0)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()