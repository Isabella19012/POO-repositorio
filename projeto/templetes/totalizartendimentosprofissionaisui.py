import streamlit as st
from Service import Service
from datetime import datetime 
import pandas as pd

class TotalizarAtendimentosProfissionaisUI:
    def main():
        st.header("Totalizar Atendimentos dos Profissionais")
        # horario_inicio = st.text_input("Informe o horário inicial no formato HH:MM")
        # horario_fim = st.text_input("Informe o horário final no formato HH:MM")
        # if st.button("Visualizar Total de Atendimentos"):
        profissional = Service.total_atendimento()
        if len(profissional) == 0: st.write("Nenhum profissional cadastrado")
        else:
            # list_dic = []
            # for obj in profissional: list_dic.append(obj.to_json())
            df = pd.DataFrame(profissional)
            st.dataframe(df)