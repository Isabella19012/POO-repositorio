from templetes.manterclienteui import ManterClienteUI
from templetes.manterservicoui import ManterServicoUI
from templetes.manterhorarioui import ManterHorarioUI
from templetes.manterprofissionalui import ManterProfissionalUI
from templetes.manteratendimentoui import ManterAtendimentoUI
from templetes.manterconvenioui import ManterConvenioUI
from templetes.abrircontaui import AbrirContaUI
from templetes.loginui import LoginUI
from templetes.perfilclienteui import PerfilClienteUI
from templetes.perfilprofissionalui import PerfilProfissionalUI
from templetes.agendarservicoui import AgendarServicoUI
from templetes.abrirminhaagenda import AbrirMinhaAgenda
from templetes.visualizarmeusservicos import VisualizarServicos
from templetes.visualizarminhaagenda import VisualizarAgenda
from templetes.confirmarservico import ConfirmarServico
from templetes.alterarsenha import AlterarSenha

from Service import Service
import streamlit as st

class IndexUI:
    def main():
        Service.cliente_criar_admin()
        IndexUI.sidebar()

    def menu_admin():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("Menu", ["Clientes", "Serviços", "Horario", "Profissional", "Atendimento", "Convenio", "Alterar Senha"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Serviços": ManterServicoUI.main()
        if op == 'Horario': ManterHorarioUI.main()
        if op == 'Profissional': ManterProfissionalUI.main()
        if op == 'Atendimento': ManterAtendimentoUI.main()
        if op == 'Convenio': ManterConvenioUI.main()
        if op == "Alterar Senha" : AlterarSenha.main()
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema",
        "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Visualizar Serviços"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Agendar Serviço": AgendarServicoUI.main()
        if op == "Visualizar Serviços": VisualizarServicos.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Visualizar Minha Agenda", "Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Minha Agenda": AbrirMinhaAgenda.main()
        if op == "Visualizar Minha Agenda": VisualizarAgenda.main()
        if op == "Confirmar Serviço": ConfirmarServico.main()
    def sair_do_sistema():
            if st.sidebar.button("Sair"):
                del st.session_state["usuario_id"]
                del st.session_state["usuario_nome"]
                del st.session_state["perfil"]
                st.rerun()
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            profissional = st.session_state["perfil"] == "profissional"
            st.sidebar.write("Bem-vindo(a), " +
                st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            elif profissional: IndexUI.menu_profissional()
            else: IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()
IndexUI.main()

