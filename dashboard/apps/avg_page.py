from sections.sidebar import Sidebar
import streamlit as st
from data.chart import graph_avg_bdmass, graph_avg_fliplength, graph_avg_culmendepth, graph_avg_culmenlength, test
from data.get import get_avg_bdmass, get_avg_fliplength, get_avg_culmendepth, get_avg_culmenlength

def app():

    
    family = Sidebar.avg()
    print(family)

    if family[0] == True:
        avg_bdmass = get_avg_bdmass()
        graph = graph_avg_bdmass(avg_bdmass)
        st.plotly_chart(graph)
    
    if family[1]==True:
        avg_fliplength = get_avg_fliplength()
        graph = graph_avg_fliplength(avg_fliplength)
        st.plotly_chart(graph)

    if family[2]==True:
        avg_culmendepth = get_avg_culmendepth()
        graph = graph_avg_culmendepth(avg_culmendepth)
        st.plotly_chart(graph)

    if family[3]==True:
        avg_culmenlength = get_avg_culmenlength()
        graph = graph_avg_culmenlength(avg_culmenlength)
        st.plotly_chart(graph)

    if family[4]==True:
        avg_fliplength = get_avg_fliplength()
        avg_culmendepth = get_avg_culmendepth()
        avg_culmenlength = get_avg_culmenlength()
        graph = test(avg_culmenlength, avg_culmendepth, avg_fliplength)
        st.plotly_chart(graph)
