import sys
import os
from datetime import datetime

# Adiciona a pasta raiz do projeto ('projeto') ao caminho de busca do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
import pandas as pd
import time
from Service import Service

class ManterAtendimentoUI:
    def main():
        st.header("Cadastro de Atendimento")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterAtendimentoUI.listar()
        with tab2: ManterAtendimentoUI.inserir()
        with tab3: ManterAtendimentoUI.atualizar()
        with tab4: ManterAtendimentoUI.excluir()
    def listar():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            list_dic = []
            for obj in atendimentos: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        horarios = Service.horario_listar()
        data = st.text_input("Informe a data", datetime.now().strftime("%d/%m/%Y"))
        queixa_principal = st.text_input("Informe a queixa principal")
        historico_saude = st.text_input("Informe o histórico de saúde: ")
        avaliacao = st.text_input("Informe a avaliação")
        prescricao = st.text_input('informe a prescrição')
        id_horario = st.selectbox('Informe o id do horário', horarios)
        total = st.text_input('Total do atendimento')
        pago = st.checkbox("Pago", key="pago_inserir")
        if st.button("Inserir"):
            Service.atendimento_inserir(datetime.strptime(data, "%d/%m/%Y"), queixa_principal, historico_saude, avaliacao, prescricao, id_horario.get_id(), int(total), pago)
            st.success("Atendimento inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = Service.horario_listar()
        atendimentos = Service.atendimento_listar()

        if len(atendimentos) == 0:
            st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Atualização de Atendimentos", atendimentos)

            data = st.text_input("Informe a data",op.get_data().strftime("%d/%m/%Y"))
            queixa_principal = st.text_input("Informe a queixa principal", op.get_queixa_principal())
            historico_saude = st.text_input("Informe o histórico de saúde",op.get_historico_saude())
            avaliacao = st.text_input("Informe a avaliação",op.get_avaliacao())
            prescricao = st.text_input("Informe a prescrição",op.get_prescricao())
            id_horario = st.selectbox("Informe o horário", horarios)
            total = st.text_input("Total do atendimento",str(op.get_total()))
            pago = st.checkbox("Pago", value=op.get_pago(), key="pago_atualizar")

            if st.button("Atualizar"):
                data = datetime.strptime(data, "%d/%m/%Y")
                id_horario = id_horario.get_id()
                total = int(total)

                Service.atendimento_atualizar(
                    op.get_id(), data, queixa_principal,
                    historico_saude, avaliacao, prescricao,
                    id_horario, total, pago)

                st.success("Atendimento atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        atendimentos = Service.atendimento_listar()
        if len(atendimentos) == 0: st.write("Nenhum atendimento cadastrado")
        else:
            op = st.selectbox("Exclusão de atendimento", atendimentos)
            if st.button("Excluir"):
                id = op.get_id()
                Service.atendimento_excluir(id)
                st.success("Atendimento excluído com sucesso")
                time.sleep(2)
                st.rerun()