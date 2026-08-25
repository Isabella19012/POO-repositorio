import streamlit as st 
import pandas as pd #
import time #
from Service import Service 

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviço")#tabs coloca abas na pagina
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir",
        "Atualizar", "Excluir"])
        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir() 
    def listar():
        servico = Service.servico_listar()
        if len(servico) == 0: st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servico: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        id = st.text_input('Informe o ID')
        descricao = st.text_input('Informe a descrição')
        valor = st.text_input('Infome o valor')
        if st.button('Inserir'):
            Service.servico_inserir(int(id), descricao, float(valor))
            st.sucess('Serviço inserido com sucesso!')
            time.sleep(2)
            st.rerun() #roda o programa denovo - recarregar

    def atualizar():
        servico = Service.servico_listar()
        if len(servico) == 0: st.write('Nemhum serviço cadastrado')
        else:
            op = st.selectbox('Atualização de serviço', servico)
            id= st.text_input("Novo ID", op.get_id())
            descricao= st.text_input("Nova descrição", op.get_descricao())
            valor = st.text_input("Novo valor", op.get_valor())
        if st.button("Atualizar"):
            id = op.get_id()
            Service.servico_atualizar(int(id), descricao, float(valor))
            st.success("Serviço atualizado com sucesso")
            st.rerun()
    def excluir():
        servico = Service.servico_listar()
        if len(servico) == 0: st.write('Nenhum serviço cadastrado')
        else:
            op = st.selectbox('Exclusão de serviços', servico)
            if st.button('Excluir'):
                id = op.get_id()
                Service.servico_excluir(id)
                st.success('Serviço excluido com sucesso!')
ManterServicoUI.main()
