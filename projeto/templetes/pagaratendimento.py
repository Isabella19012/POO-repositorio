import streamlit as st
import pandas as pd
from Service import Service
import time

class PagarAtendimento:
    def main():
        st.header("Cadastro de Serviço")#tabs coloca abas na pagina
        tab1, tab2 = st.tabs(["Listar Pagamento", "Pagar Pagamento"])
        with tab1: PagarAtendimento.listar_pagamento()
        with tab2: PagarAtendimento.pagar_pagamento()
    def listar_pagamento():
        st.header('Listar Conta')
        ToPay = Service.cliente_listar_pagamentos(st.session_state["usuario_id"])
        if len(ToPay) == 0: st.write("Não há contas a pagar")
        else:
            list_dic = []
            for obj in ToPay: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def pagar_pagamento():
        st.header('Pagar Atendimento')
        ToPay = Service.cliente_listar_pagamentos(st.session_state["usuario_id"])
        conta = st.selectbox('Informe a conta ', ToPay)
        if st.button('Pagar'):
            Service.atendimento_atualizar(
                conta.id,
                conta.data.strftime("%d/%m/%Y"),
                conta.queixa_principal, 
                conta.historico_saude, 
                conta.avaliacao, 
                conta.prescricao, 
                int(conta.id_horario), 
                int(conta.total), 
                True)
            st.success("Pagamento realizado com sucesso!")
            st.rerun()
