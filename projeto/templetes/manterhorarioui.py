import streamlit as st 
import pandas as pd #
import time #
from Service import Service 
from datetime import datetime

class ManterHorarioUI: 
    def main():
        st.header("Cadastro de Horario")#tabs coloca abas na pagina
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir",
        "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir() 
    def listar():
        horario = Service.horario_listar()
        if len(horario) == 0: st.write("Nenhum horario cadastrado")
        else:
            dic = []
            cliente = Service.cliente_listar_id(obj.get_id_cliente())
            servico = Service.servico_listar_id(obj.get_id_servico())
            if cliente != None: cliente = cliente.get_nome()
            if cliente != None: servico = servico.get_descricao()
            dic.append({'id':get_id(), 'data': obj.get_data(),
                        'confirmado': obj.get_confirmado(), 'cliente': cliente,
                        'serviço': servico})
            df = pd.DataFrame(dic)
            st.dataframe(df)
    def inserir():
        #id = st.text_input('Informe o ID')
        descricao = st.text_input('Informe a descrição')
        valor = st.text_input('Infome o valor')
        if st.button('Inserir'):
            Service.horario_inserir( descricao, float(valor))
            st.success('Serviço inserido com sucesso!')
            time.sleep(2)
            st.rerun() #roda o programa denovo - recarregar

    def atualizar():
        horario = Service.horario_listar()
        if len(horario) == 0: st.write('Nemhum horario cadastrado')
        else:
            op = st.selectbox('Atualização de serviço', horario)
            descricao= st.text_input("Nova descrição", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                Service.horario_atualizar(int(id), descricao, float(valor))
                st.success("Horario atualizado com sucesso")
                st.rerun()
    def excluir():
        horario = Service.horario_listar()
        if len(horario) == 0: st.write('Nenhum horario cadastrado')
        else:
            op = st.selectbox('Exclusão de horario', horario)
            if st.button('Excluir'):
                id = op.get_id()
                Service.horario_excluir(id)
                st.success('Horario excluido com sucesso!')
