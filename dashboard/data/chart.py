import plotly.io as pio
import plotly.graph_objs as go
import plotly.express as px
from requests.models import parse_url

def graph_stats(stats):
        x=["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)"]
        values = []
        for i in x:
                for s in stats:
                        num=s.pop(i)
                        values.append(num)
        fig = go.Figure(
                data=[go.Bar(x=["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)"], y=values)],
                layout_title_text="Características"
        
    )
        return fig

def graph_avg_bdmass(avg_bdmass):
        x=["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)"]
        values = []
        for i in x:
                for s in stats:
                        num=s.pop(i)
                        values.append(num)
        fig = go.Figure(
                data=[go.Bar(x=["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)", "Body Mass (g)"], y=values)],
                layout_title_text="Características"
        )