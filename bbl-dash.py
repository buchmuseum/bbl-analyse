import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import datetime

df = pd.read_csv("seitenliste_clean_neu.csv", delimiter=",")
df.ausgabe = pd.to_datetime(df.ausgabe)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

jahresliste = []

for i in range(1834,1945):
    jahresliste.append({'label': str(i), 'value': str(i)})


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    # html.H1('Seitenverteilung Börsenblatt'),

    dcc.Graph(
        id='bbl-seiten',
        figure={
            'data': [
                {'x': df.ausgabe, 'y': df.seiten, 'type': 'bar', 'name': 'Bbl'},
            ],
            'layout': {
                'title': 'Börsenblatt'
            }
        }
    ),
    dcc.Dropdown(
        id='start-dropdown',
        options= jahresliste,
        value='1834'
    ),
    dcc.Dropdown(
        id='end-dropdown',
        options= jahresliste,
        value='1945'
    )

])

@app.callback(
    dash.dependencies.Output('bbl-seiten', 'figure'),
    [dash.dependencies.Input('start-dropdown','value'), dash.dependencies.Input('end-dropdown','value')]
)

def update_figure(start_year, end_year):
    start_date = datetime.datetime(int(start_year),1,1)
    end_date = datetime.datetime(int(end_year),12,31)
    filtered_df = df[(df.ausgabe >= start_date) & (df.ausgabe <= end_date)]
    return {
        'data' : [
            {'x': filtered_df.ausgabe, 'y': filtered_df.seiten, 'type': 'bar'},
        ]
    }

if __name__ == '__main__':
    app.run_server(debug=True)