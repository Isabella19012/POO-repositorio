import streamlit as st
import pandas as pd
from Service import Service
class ListarHorariosConfirmadosHojeUI:

    def main():
        horarios = Service.horarios_hoje_listar()
        st.header("Horários para hoje")
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                profissional = Service.profissional_listar_id(obj.get_id_profissional())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                if profissional != None: profissional = profissional.get_nome()
                dic.append({"id" : obj.get_id(), "data e hora" : obj.get_data().strftime("%d/%m/%Y %H:%M"), "nome do cliente" : cliente,
                "descrição do serviço." : servico, "profissional": profissional})
            df = pd.DataFrame(dic) 
            st.dataframe(df)