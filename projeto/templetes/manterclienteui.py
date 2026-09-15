import sys
import os

import streamlit as st
import pandas as pd
import time
from Service import Service

class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()
    def listar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        convenio=Service.convenio_listar()
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type='password')

        #id_convenio = st.text_input("Informe o id do convenio")
        id_convenio = st.selectbox("Informe o convenio", convenio, index = None)

        if st.button("Inserir"):
            id_convenio = None
            if id_convenio != None: id_convenio = id_convenio.get_id_convenio()
            Service.cliente_inserir(nome, email, fone, senha, id_convenio)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()
    def atualizar():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            convenios = Service.convenio_listar()
            op = st.selectbox("Atualização de Clientes", clientes)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            senha = st.text_input("Nova senha", op.get_senha())
            fone = st.text_input("Novo fone", op.get_fone())
            id_convenio = st.selectbox('Novo id do convenio', op.get_id_convenio())
            convenio = st.selectbox(
                "Informe o novo convenio",
                convenios,
                index=next(
                    (i for i, p in enumerate(convenios)
                    if p.get_id_convenio() == id_convenio),None))
            if st.button("Atualizar"):
                id = op.get_id()
                Service.cliente_atualizar(id, nome, email, fone, senha, convenio.get_id_convenio() if convenio else 0)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        clientes = Service.cliente_listar()
        if len(clientes) == 0: st.write("Nenhum cliente cadastrado")
        else:
            op = st.selectbox("Exclusão de Clientes", clientes)
            if st.button("Excluir"):
                id = op.get_id()
                Service.cliente_excluir(id)
                st.success("Cliente excluído com sucesso")
                time.sleep(2)
                st.rerun()
