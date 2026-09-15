from templetes.manterclienteui import ManterClienteUI
from templetes.manterservicoui import ManterServicoUI
from templetes.manterhorarioui import ManterHorarioUI
from templetes.manterprofissionalui import ManterProfissionalUI
from templetes.manteratendimentoui import ManterAtendimentoUI
from templetes.manterconvenioui import ManterConvenioUI
from templetes.abrircontaui import AbrirContaUI
from templetes.loginui import LoginUI
from templetes.perfilclienteui import PerfilClienteUI
from Service import Service
from Service import Service
import streamlit as st

class IndexUI:
    def main():
        # verifica a existe o usuário admin
        Service.cliente_criar_admin()
        # monta o sidebar
        IndexUI.sidebar()
    def main_admin():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horario", "Profissional", "Atendimento", "Convenio"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == 'Horario': ManterHorarioUI.main()
        if op == 'Profissional': ManterProfissionalUI.main()
        if op == 'Atendimento': ManterAtendimentoUI.main()
        if op == 'Convenio': ManterConvenioUI.main()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema",
        "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if op == "Meus Dados": PerfilClienteUI.main()
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes",
        "Cadastro de Serviços", "Cadastro de Horários",
        "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
    def sair_do_sistema():
            if st.sidebar.button("Sair"):
                del st.session_state["usuario_id"]
                del st.session_state["usuario_nome"]
                st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " +
                st.session_state["usuario_nome"])
        if admin: IndexUI.menu_admin()
        else: IndexUI.menu_cliente()
        IndexUI.sair_do_sistema()

IndexUI.main()