import streamlit as st
from Service import Service
import pandas as pd

class VisualizarAgenda:
    def main():
        st.header("Visualizar Minha Agenda")
        horario = Service.horario_listar()
        if len(horario) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horario:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                if profissional != None: servico = profissional.get_nome()
                dic.append({'id':obj.get_id(), 'data': obj.get_data(),
                            'confirmado': obj.get_confirmado(), 'cliente': cliente,
                            'serviço': servico, 'profissional': profissional})
            df = pd.DataFrame(dic)
            st.dataframe(df)