import streamlit as st

class Sidebar:
    def fam():
        with st.sidebar:
            st.header("Select family")
            info = st.slider("Pick", 0, 2)
            return int(info)
    
    def avg():
        with st.sidebar:
            st.header("Mostrar gráficos necesitados")
            info = st.checkbox("Gráfico body mass")
            info2 = st.checkbox("Gráfico Flipper Length")
            info3 = st.checkbox("Gráfico Culmen Depth")
            info4 = st.checkbox("Gráfiico Culmen Length")
            info5 = st.checkbox("Gráfico estadísticas del pico")
            return info, info2, info3, info4, info5