import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
 
data = pd.read_excel('/home/pi/Programiki/autostart/temp.xlsx')
 
# data = df['AverageTemperatureFahr', 'year']
 
#data = df.loc[(df['year'] > 2000) & (df['City'] == 'Auckland') & (df['AverageTemperatureFahr'] > 0)
 #             & (df['AverageTemperatureFahr'] < 400)]
 
temp_np = np.array(data['Temp'].tolist())
czas_np = np.array(data['Czas'].tolist())
# df.loc[df['column_name'] == some_value]
 
fig = go.Figure(data=px.line(x=czas_np, y=temp_np))
fig.update_layout(
    title="Temperatura w Norze",
    xaxis={'title': 'Czas'},
    yaxis_title="Temperatura [Celsjusz]",
    margin={'l': 40, 'b': 40, 't': 50, 'r': 50}
    )

fig.update_xaxes(
    ticktext = ["Poniedzialek", "Wtorek", "Sroda"],
    tickvals=["17:02:22","23:16:51", "23:29:10", czas_np]
)

 
fig2 = go.Figure(data=px.line(x=czas_np, y=temp_np))
fig2.update_layout(
    title="Another data",
    xaxis={'title': 'Czas'},
    yaxis_title="wilgotnosc ",
    margin={'l': 40, 'b': 40, 't': 50, 'r': 50}
    )


app = dash.Dash()

body = {
    'background-image': 'clouds.jpg',
     'background-color':'red'
    }


app.layout = html.Div(children=[
 
    html.H1(children="Simple Div",
            style={'textAlign': 'center',
                    'color': '#ff0040',
                   'background-color':'#33F0FF'
                   }),
 
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig2)
 
])
 
 #192.168.216.235
if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port=8888,debug=True)