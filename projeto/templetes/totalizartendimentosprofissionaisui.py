import streamlit as st
import pandas as pd
import time
from Service import Service

class TotalAtendimentosUI:
    def main():
        st.header("Total de Atendimentos")
        profissionais = Service.total_atendimentos()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            #list_dic = []
            #for obj in profissionais: list_dic.append(obj.to_dict())
            #df = pd.DataFrame(profissionais)
            #st.dataframe(df)
            st.write(profissionais)