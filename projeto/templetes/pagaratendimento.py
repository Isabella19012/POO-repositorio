import streamlit as st
import pandas as pd
from Service import Service
import time

class PagarAtendimento:
    def main():
        st.header('Pagar Atendimento')
        id_cliente = st.session_state["usuario_id"]
        ToPay = Service.atendimento_pagar(id_cliente)


