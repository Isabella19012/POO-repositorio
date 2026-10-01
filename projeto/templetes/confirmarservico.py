from Service import Service
import streamlit as st
import time
class ConfirmarServico:
    def main():
        disponiveis =[]
        id =st.session_state["usuario_id"]
        st.header("Confirmar Serviços")
        horarios = Service.horario_listar()
        for x in horarios: 
            if x.get_confirmado() == False: disponiveis.append(x)
        clientes = Service.cliente_listar()
        if len(horarios) == 0: st.write("Nenhum horário disponivél cadastrado.")
        else: 
            horario = st.selectbox('Informe o horário', disponiveis) 
            cliente = st.selectbox('Informe o cliente', clientes)
            if st.button("Confirmar"):
                Service.horario_atualizar(horario.get_id(), horario.get_data(), True, cliente.get_id(), horario.get_id_servico(), id) #id, data, confirmado, id_cliente, id_servico, id_profissional
                time.sleep(2)
                st.rerun()
                st.success("Horário confirmado com sucesso")