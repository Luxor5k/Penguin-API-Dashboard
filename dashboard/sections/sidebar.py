import streamlit as st

class Sidebar:
    def fam():
        with st.sidebar:
            st.header("Select family")
            info = st.slider("Pick", 0, 2)
            return int(info)