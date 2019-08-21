#!/usr/bin/env python
# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly
import plotly.graph_objects as go

df=pd.read_csv('./data/wide_budget.csv')

def clean_column_name(x):
    return x.replace(' ','_').lower()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': 'black',
    'default': 'black',
    'border': 'transparent'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


stackedLineFig = go.Figure()

for i in range(len(df.columns)-1):
    stackedLineFig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0], stackgroup='one'))
#stackedLineFig.show()


lineFig = go.Figure()

for i in range(len(df.columns)-1):
    lineFig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))    
#lineFig.show()


percentLineFig = go.Figure()

for i in range(len(df.columns)-1):
    percentLineFig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0], stackgroup='one', groupnorm='percent'))
#percentLineFig.show()


groupedBarFig = go.Figure()

for i in range(len(df.columns)-1):
    groupedBarFig.add_trace(go.Bar(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))
#groupedBarFig.show()


stackedBarFig = go.Figure()

for i in range(len(df.columns)-1):
    stackedBarFig.add_trace(go.Bar(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))
stackedBarFig.update_layout(barmode='stack')
#fig.show()


labels=[]
values=[]

for i in range(len(df['2019-20 Proposed Budget'])-1):
    labels.append(df.iloc[i][0])
    values.append((df['2019-20 Proposed Budget'][i]))
    values[i] = values[i].replace(',','')
    values[i] = values[i].replace('$','')
    values[i] = int(values[i])
    
pieFig = go.Figure(data=[go.Pie(labels=labels, values=values)])
#pieFig.show()


app.layout = html.Div(children=[
    html.Div(children=[
        dcc.Graph(
            figure = stackedLineFig
        ),
        dcc.Graph(
            figure = lineFig
        ),
        dcc.Graph(
            figure = percentLineFig
        ),
        dcc.Graph(
            figure = groupedBarFig
        ),
        dcc.Graph(
            figure = stackedBarFig
        ),
    ])
    
])


if __name__ == '__main__':
    #app.run_server(debug=True)

    app.run_server(host='0.0.0.0', port = 8050)

