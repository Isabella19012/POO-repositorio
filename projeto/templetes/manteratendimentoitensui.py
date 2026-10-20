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

        atendimentos = Service.atendimento_listar()
        servicos = Service.servico_listar()

        if len(atendimentos) == 0:
            st.write("Cadastre um atendimento primeiro.")
            return

        if len(servicos) == 0:
            st.write("Cadastre um serviço primeiro.")
            return

        atendimento = st.selectbox("Informe o atendimento", atendimentos, index=None)
        servico = st.selectbox("Informe o serviço", servicos, index=None)
        quantidade = st.text_input("Informe a quantidade")
        valor = st.text_input("Informe o valor")

        if st.button("Inserir"):
            if atendimento is None or servico is None:
                st.error("Selecione o atendimento e o serviço.")
            elif quantidade == "" or valor == "":
                st.error("Preencha a quantidade e o valor.")
            else:
                id_atendimento = atendimento.get_id()
                id_servico = servico.get_id()

                Service.atendimentoitens_inserir(
                    id_atendimento,
                    id_servico,
                    int(quantidade),
                    float(valor))

                st.success("Itens de atendimento inseridos com sucesso")
                time.sleep(2)
                st.rerun()

    def listar():
        itens = Service.atendimentoitens_listar()
        if len(itens) == 0: st.write("Nenhum item de atendimento cadastrado")
        else:
            list_dic = []
            for obj in itens: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def atualizar():
        atendimentositens = Service.atendimentoitens_listar()

        if len(atendimentositens) == 0:
            st.write("Nenhum item de atendimento cadastrado")
        else:
            op = st.selectbox("Atualização de Itens de atendimento", atendimentositens)

            atendimentos = Service.atendimento_listar()
            servicos = Service.servico_listar()

            atendimento = st.selectbox("Informe o novo atendimento", atendimentos, index=None)
            servico = st.selectbox("Informe o novo serviço", servicos, index=None)
            quantidade = st.text_input("Informe a nova quantidade", str(op.get_quantidade()))
            valor = st.text_input("Informe o novo valor", str(op.get_valor()))

            if st.button("Atualizar"):
                id_servico = op.get_id_servico()
                id_atendimento = op.get_id_atendimento()

                if atendimento != None:
                    id_atendimento = atendimento.get_id()
                if servico != None:
                    id_servico = servico.get_id()

                if quantidade == "" or valor == "":
                    st.error("Preencha a quantidade e o valor.")
                else:
                    Service.atendimentoitens_atualizar(
                        op.get_id(),
                        id_atendimento,
                        id_servico,
                        int(quantidade),
                        float(valor))
                    st.success("Itens de atendimento atualizados com sucesso")
                    time.sleep(2)
                    st.rerun()

    def excluir():
        itens = Service.atendimentoitens_listar()
        if len(itens) == 0: st.write("Nenhum item de atendimento cadastrado")
        else:
            op = st.selectbox("Exclusão de item de atendimento", itens)
            if st.button("Excluir"):
                id = op.get_id()
                Service.atendimentoitens_excluir(id)
                st.success("Item de atendimento excluído com sucesso")
                time.sleep(2)
                st.rerun()