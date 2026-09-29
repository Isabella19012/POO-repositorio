import streamlit as st
from datetime import datetime
from Service import Service
import time

class AbrirMinhaAgenda:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe o a data no formato dd/mm/aaaa", datetime.now().strftime("%d/%m/%Y"))
        horario_inicial = st.text_input("Informe o horário inicial no formato HH:MM")
        horario_final = st.text_input("Informe o horário final no formato HH:MM")
        intervalo = st.text_input("Informe o intervalo entre os horários(minutos)")
        id_profissional = st.session_state["usuario_id"]
        if st.button('Abrir Agenda'):
            Service.horario_abrir_minha_agenda(data, horario_inicial, horario_final, int(intervalo), id_profissional)
            st.success("Horários inseridos com sucesso")
            time.sleep(2)
            st.rerun()
