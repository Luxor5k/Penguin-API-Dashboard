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

def graph_stats_pico(stats):
        x=["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)"]
        values = []
        for i in x:
                for s in stats:
                        num=s.pop(i)
                        values.append(num)
        fig = go.Figure(
                data=[go.Bar(x=["Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)"], y=values)],
                layout_title_text="Características del pico"
        
    )
        return fig

def graph_avg_bdmass(avg_bdmass):
        x=["Biscoe", "Dream", "Torgersen"]
        values = []
        for y in avg_bdmass:
                values.append(y["avg"])
        fig = go.Figure(
                data=[go.Bar(x=["Biscoe", "Dream", "Torgersen"], y=values,
                text=values,
                textposition='auto',
                marker_color ="white")],
        )
        fig.update_layout(
                title='Promedio de pesos según islas',
                xaxis_tickfont_size=14,
                yaxis=dict(
                title='kilogramos (kg)',
                titlefont_size=18,
                tickfont_size=16,
    ))
        return fig

def graph_avg_fliplength(avg_fliplength):
        x=["Biscoe", "Dream", "Torgersen"]
        values = []
        for y in avg_fliplength:
                values.append(y["avg"])
        fig = go.Figure(
                data=[go.Bar(x=["Biscoe", "Dream", "Torgersen"], y=values,
                text=values,
                textposition='auto',
                marker_color="Azure")],
        )
        fig.update_layout(
                title='Promedio de Flipper length',
                xaxis_tickfont_size=14,
                yaxis=dict(
                title='milimetros (mm)',
                titlefont_size=18,
                tickfont_size=16,
    ))
        return fig

def graph_avg_culmendepth(avg_culmendepth):
        x=["Biscoe", "Dream", "Torgersen"]
        values = []
        for y in avg_culmendepth:
                values.append(y["avg"])
        fig = go.Figure(
                data=[go.Bar(x=["Biscoe", "Dream", "Torgersen"], y=values,
                text=values,
                textposition='auto',
                marker_color="LightSkyBlue")],
        )
        fig.update_layout(
                title='Promedio de Culmen Depth',
                xaxis_tickfont_size=14,
                yaxis=dict(
                title='milimetros (mm)',
                titlefont_size=18,
                tickfont_size=16,
    ))
        return fig

def graph_avg_culmenlength(avg_culmenlength):
        x=["Biscoe", "Dream", "Torgersen"]
        values = []
        for y in avg_culmenlength:
                values.append(y["avg"])
        fig = go.Figure(
                data=[go.Bar(x=["Biscoe", "Dream", "Torgersen"], y=values,
                text=values,
                textposition='auto',
                marker_color="MediumTurquoise")],
        )
        fig.update_layout(
                title='Promedio de Culmen Length',
                xaxis_tickfont_size=14,
                yaxis=dict(
                title='milimetros (mm)',
                titlefont_size=18,
                tickfont_size=16,
    ))
        return fig

def test(avg_culmenlength, avg_culmendepth, avg_fliplength):
        x=["Biscoe", "Dream", "Torgersen"]
        lengthavg = []
        depthavg = []
        flipavg = []
        for y in avg_culmenlength:
                lengthavg.append(y["avg"])
        for e in avg_culmendepth:
                depthavg.append(e["avg"])
        for f in avg_fliplength:
                flipavg.append(f["avg"])
        fig = go.Figure(
                data=[
                        go.Bar(name="Promedio Culmen Length", x=["Biscoe", "Dream", "Torgersen"], y=lengthavg,
                        text=lengthavg,
                        textposition='auto'),
                        go.Bar(name="Promedio Culmen Depth", x=["Biscoe", "Dream", "Torgersen"], y=depthavg,
                        text=lengthavg,
                        textposition='auto',
                        marker_color="Cornsilk"),
                        go.Bar(name="Promedio Flip Length", x=["Biscoe", "Dream", "Torgersen"], y=flipavg,
                        text=lengthavg,
                        textposition='auto',
                        marker_color="Azure")],
                        layout_title_text="Culmen Length (mm)"
        )
        fig.update_layout(
                title='Promedio de Culmen Depth',
                xaxis_tickfont_size=14,
                yaxis=dict(
                title='milimetros (mm)',
                titlefont_size=18,
                tickfont_size=16,
    ))
        fig.update_layout(barmode='stack')
        return fig