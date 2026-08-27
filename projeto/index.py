from templetes.manterclienteui import ManterClienteUI
from templetes.manterservicoui import ManterServicoUI
from templetes.manterhorarioui import ManterHorarioUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horario"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == 'Horario': ManterHorarioUI.main()

IndexUI.main()