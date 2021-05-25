import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.express as px


def cascade_average(n,data):
    #init
    suma=0
    j=0
    i=0
    table=[]
    
    for i in range(len(data)-n):
        for j in range(n):
            suma += data[i+j]
        table.append(suma/n)
        suma=0
    return(table)


data = pd.read_excel('/home/pi/Programiki/autostart/waga.xlsx')
 

 
waga_np = np.array(data['Waga'].tolist())
czas_np = np.array(data['Czas'].tolist())

voltage =(waga_np/4096)*3.3
new_voltage = cascade_average(10,voltage)

fig2 = go.Figure(data=px.line(x=czas_np, y=waga_np))
fig2.update_layout(
    title="Bez filtracji",
    xaxis={'title': 'Czas'},
    yaxis_title="Waga",
    margin={'l': 40, 'b': 40, 't': 50, 'r': 50}
    )

#make y-10 samples in order to len(x)=len(y)
czas_np = czas_np[:len(czas_np)-10] 

# df.loc[df['column_name'] == some_value]
 
fig = go.Figure(data=px.line(x=czas_np, y=new_voltage))
fig.update_layout(
    title="Waga pojemnika",
    xaxis={'title': 'Czas'},
    yaxis_title="Wartosc czujnika [V]",
    margin={'l': 40, 'b': 40, 't': 50, 'r': 50}
    )

 

#fig.update_xaxes(
#    ticktext = ["Poniedzialek", "Wtorek", "Sroda"],
#    tickvals=["17:02:22","23:16:51", "23:29:10", czas_np]
#)


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
