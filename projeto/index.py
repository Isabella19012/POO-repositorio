from templetes.manterclienteui import ManterClienteUI
from templetes.manterservicoui import ManterServicoUI
from templetes.manterhorarioui import ManterHorarioUI
from templetes.manterprofissionalui import ManterProfissionalUI
from templetes.manteratendimentoui import ManterAtendimentoUI
from templetes.manterconvenioui import ManterConvenioUI
import streamlit as st

class IndexUI:
    def main():
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horario", "Profissional", "Atendimento", "Convenio"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == 'Horario': ManterHorarioUI.main()
        if op == 'Profissional': ManterProfissionalUI.main()
        if op == 'Atendimento': ManterAtendimentoUI.main()
        if op == 'Convenio': ManterConvenioUI.main()

IndexUI.main()