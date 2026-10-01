import streamlit as st
import time
from Service import Service

class AlterarSenha:
    def main():
        for admin in Service.cliente_listar():
             if admin.get_email() == 'admin':
                  adm_id=admin.get_id()
                  break 
        st.header("Alterar Senha")
        senha=st.text_input("informe a nova senha",type="password")
        if st.button("Alterar Senha"):
                Service.cliente_atualizar(adm_id, admin.get_nome(), admin.get_email(), senha, admin.get_fone(), admin.get_id_convenio() )
                st.success("Senha do admin alterada com sucesso")
                time.sleep(2)
                st.rerun()