from Service import Service
import streamlit as st
import pandas as pd
class VisualizarServicos:
    def listar():
            servico = Service.servico_listar()
            if len(servico) == 0: st.write("Nenhum serviço cadastrado")
            else:
                list_dic = []
                for obj in servico: list_dic.append(obj.to_json())
                df = pd.DataFrame(list_dic)
                st.dataframe(df)