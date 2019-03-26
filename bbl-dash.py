import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from datetime import datetime as dt

df = pd.read_csv("seitenliste_clean.csv", delimiter=",")
df.ausgabe = pd.to_datetime(df.ausgabe)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1('Seitenverteilung Börsenblatt'),

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
    dcc.RangeSlider(
        id='year-slider',
        marks={i: '{}'.format(i) for i in range(1834,1945)},
        min=1834,
        max=1945,
        value=[1834, 1945]
    ),
    dcc.DatePickerRange(
        id='date-picker',
        min_date_allowed=dt(1834, 1, 1),
        max_date_allowed=dt(1945, 12, 31),
        initial_visible_month=dt(1834, 1, 1),
        end_date=dt(1945, 12, 31)
    )
])

@app.callback(
    dash.dependencies.Output('bbl-seiten', 'figure'),
    [dash.dependencies.Input('date-picker','start_date'), dash.dependencies.Input('date-picker','end_date')]
)

def update_figure(start_date, end_date):
    filtered_df = df[(df.ausgabe >= start_date) & (df.ausgabe <= end_date)]
    return {
        'data' : [
            {'x': filtered_df.ausgabe, 'y': filtered_df.seiten, 'type': 'bar'},
        ]
    }

if __name__ == '__main__':
    app.run_server(debug=True)