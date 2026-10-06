import streamlit as st
from Service import Service
import time
from datetime import datetime 

class RegistrarAtendimento:
    def main():
        horarios = Service.horario_listar_disponiveis(st.session_state["usuario_id"])
        st.header('Registrar Atendimento')
        data = st.text_input("Informe a data", datetime.now().strftime("%d/%m/%Y"))
        queixa_principal = st.text_input("Informe a queixa principal")
        historico_saude = st.text_input("Informe o histórico de saúde: ")
        avaliacao = st.text_input("Informe a avaliação")
        prescricao = st.text_input('informe a prescrição')
        id_horario = st.selectbox('Informe o id do horário', horarios)
        total = st.text_input('Total do atendimento')
        pago = st.checkbox("Pago")
        if st.button("Inserir"):
            Service.atendimento_inserir(datetime.strptime(data, "%d/%m/%Y"), queixa_principal, historico_saude, avaliacao, prescricao, int(id_horario), int(total), pago)
            st.success("Atendimento inserido com sucesso")
            time.sleep(2)
            st.rerun()