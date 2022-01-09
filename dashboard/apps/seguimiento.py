import streamlit as st
from data.get import get_for_id, get_stats, get_stats_species, get_avg_fliplength, get_avg_fliplength, get_avg_culmenlength
from sections.sidebar import Sidebar
from data.chart import graph_stats, graph_stats_pico, test

def app():
    st.title("Seguimiento de pingüinos")

    penguin_tag = st.text_input("Selecciona la ID del pingüino a consultar", value=1)
    family = Sidebar.fam()

    data=get_for_id(penguin_tag, family)
 
    specie = [penguin["Species"] for penguin in data]
    id = [penguin["Individual ID"] for penguin in data]

    if "Adelie Penguin (Pygoscelis adeliae)" in specie:
        st.header(id)
        st.text(specie)
        st.image("https://user-images.githubusercontent.com/62902607/147839599-cc855237-16b3-4560-ab87-61684c44cff2.jpg")
    elif "Chinstrap penguin (Pygoscelis antarctica)" in specie:
        st.header(id)
        st.text(specie)
        st.image("https://user-images.githubusercontent.com/62902607/147839649-ad91aa71-a023-4253-84fa-81bc88585c72.jpg")
    elif "Gentoo penguin (Pygoscelis papua)" in specie:
        st.header(id)
        st.text(specie)
        st.image("https://user-images.githubusercontent.com/62902607/147839664-b85fbc12-819f-4282-bd5c-3a22b6736f70.JPG")

    stat = get_stats(penguin_tag, family)
    graph = graph_stats(stat)
    st.plotly_chart(graph)
    st.text(get_stats(penguin_tag, family))


    avg_fliplength = get_avg_fliplength()
    avg_culmendepth = get_avg_fliplength()
    avg_culmenlength = get_avg_culmenlength()
    graph = test(avg_culmenlength, avg_culmendepth, avg_fliplength)
    st.plotly_chart(graph)

   

