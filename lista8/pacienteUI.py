import streamlit as st
from paciente import paciente
from datetime import date
from datetime import datetime
class pacienteUI:
    def main():
        st.header('Dados do paciente')
        nome = st.text_input('Nome: ')
        cpf = st.text_input('CPF: ')
        fone = st.text_input('Telefone: ')
        # dt_nasc = st.text_input('Data de nascimento: ')
        dt_nasc = st.date_input("Data de nascimento: ", value=date(2000,1,1), \
                                min_value=date(1900,1,1), \
                                max_value=date.today(), \
                                format='DD/MM/YYYY')
        dt_nasc = datetime.combine(dt_nasc, datetime.min.time())
        if st.button('Idade'):
            p=paciente(nome, cpf, fone, dt_nasc)
            st.write(f'Você tem {p.idade()}')