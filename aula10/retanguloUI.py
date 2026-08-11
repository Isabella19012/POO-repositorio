import streamlit as st
from retangulo import Retangulo
class retanguloUI:
    def main():
        st.header('Calculo com retangulo')
        b=st.text_input("Base")
        h=st.text_input("Altura")
        if st.button('Calcular'):
            r = Retangulo(float(b), float(h))
            st.write(f'area: {r.calc_area():.2f}')
            st.write(f'diagonal: {r.calc_diagonal():.2f}')
            st.write(r)