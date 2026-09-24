import streamlit as st
from datetime import datetime 
from Service import Service
import time

class AbrirMinhaAgenda:
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe o a data no formato dd/mm/aaaa", datetime.strftime("%d/%m/%Y"))
        horario_inicial = st.text_input("Informe o horário inicial no formato HH:MM",datetime.strftime("%H:%M"))
        horario_final = st.text_input("Informe o horário final no formato HH:MM",datetime.strftime("%H:%M"))
        intervalo = st.text_input("Informe o intervalo entre os horários(minutos)", type='password')
        if st.button('Abrir Agenda'):
            Service.profissional_inserir_atendimento(data, horario_inicial, horario_final, int(intervalo))
            st.success("Agenda aberta com sucesso")
            time.sleep(2)
            st.rerun()
