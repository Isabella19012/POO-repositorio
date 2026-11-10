import streamlit as st
import pandas as pd
from Service import Service
class ListarAgendaProfissionalUI:
    def main():
        st.header("Listar Agenda Profissional")
        profissionais = Service.profissional_listar()
        profissional = st.selectbox("Informe o profissional", profissionais)
        id_profissional = profissional.get_id()
        horarios = Service.horario_visualizar_minha_agenda(id_profissional)
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({"id" : obj.get_id(), "data e hora" : obj.get_data().strftime("%d/%m/%Y %H:%M"), "nome do cliente" : cliente,
                "descrição do serviço." : servico})
            df = pd.DataFrame(dic) 
            st.dataframe(df)