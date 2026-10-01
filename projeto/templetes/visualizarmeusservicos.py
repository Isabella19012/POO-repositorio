from Service import Service
import streamlit as st
import pandas as pd
class VisualizarServicos:
    def main():
            st.header('Visualizar Meus Serviços')
            servico = Service.servico_listar()
            if len(servico) == 0: st.write("Nenhum serviço cadastrado")

            else:
                list_dic = []
                for obj in servico:
                    if obj.get_id() == st.session_state["usuario_id"]: list_dic.append(obj.to_json())
                df = pd.DataFrame(list_dic)
                st.dataframe(df)