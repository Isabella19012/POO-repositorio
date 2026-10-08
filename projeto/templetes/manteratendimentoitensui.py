import streamlit as st
import pandas as pd
import time
from Service import Service
class ManterAtendimentoItensUI:
    def main():
            st.header("Cadastro de Itens de Atendimento")
            tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
            with tab1: ManterAtendimentoItensUI.listar()
            with tab2: ManterAtendimentoItensUI.inserir()
            with tab3: ManterAtendimentoItensUI.atualizar()
            with tab4: ManterAtendimentoItensUI.excluir()
    def inserir():
        atendimentos=Service.atendimento_listar()
        servicos=Service.servico_listar()
        atendimento = st.selectbox("Informe o atendimento", atendimentos, index = None)
        servico = st.selectbox("Informe o serviço", servicos, index = None)
        quantidade = st.text_input("Informe o nome")
        valor = st.text_input("Informe o e-mail")

        if st.button("Inserir"):
            id_servico = None
            id_atendimento = None
            if atendimento != None: id_atendimento = atendimento.get_id()
            if servico != None: id_servico = servico.get_id()
            Service.atendimentoitens_inserir(id_atendimento, id_servico, quantidade, valor)
            st.success("Itens de atendimento inseridos com sucesso")
            time.sleep(2)
            st.rerun()
    def listar():
        itens = Service.atendimentoitens_listar()
        if len(itens) == 0: st.write("Nenhum item cadastrado")
        else:
            for i in itens:
                lista=[]
                lista.append(i)
                df = pd.DataFrame(lista)
                st.dataframe(df)
            return lista
    def atualizar():
        atendimentositens = Service.atendimentositens_listar()

        if len(atendimentositens) == 0:
            st.write("Nenhum item de atendimento cadastrado")
        else:
            op = st.selectbox("Atualização de Horários", atendimentositens)
            id_servico = op.get_id_servico()
            id_atendimento = op.get_id_atendimento()
            atendimentos=Service.atendimento_listar()
            servicos=Service.servico_listar()

            atendimento = st.selectbox("Informe o novo atendimento", atendimentos, index = None)
            servico = st.selectbox("Informe o novo serviço", servicos, index = None)
            quantidade = st.text_input("Informe a nova quantidade", op.get_quantidade )
            valor = st.text_input("Informe o novo valor", op.get_valor)

            if st.button("Atualizar"):
                id_servico = None
                id_atendimento = None
                if atendimento != None: id_atendimento = atendimento.get_id()
                if servico != None: id_servico = servico.get_id()
                Service.atendimentoitens_atualizar(op.get_id(), id_atendimento, id_servico, quantidade, valor)
                st.success("Itens de atendimento atualizados com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        itens = Service.atendimentoitens_listar()
        if len(itens) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Exclusão de atendimento", itens)
            if st.button("Excluir"):
                id = op.get_id()
                Service.atendimentoitens_excluir(id)
                st.success("Atendimento excluído com sucesso")
                time.sleep(2)
                st.rerun()