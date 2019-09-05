#!/usr/bin/env python
# coding: utf-8

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
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

stackedLineFig.update_layout(height=600)


app.layout = html.Div(children=[
    html.H1(children=[
            'city of long beach budget'
    ], style={'text-align' : 'center', 'font-family' : 'Verdana', 'padding-top' : '10px'}),
    
    html.Div(className='row', children=[
        html.Div(className='nine columns', id = 'figDiv', children=[
            dcc.Graph(
                id = 'mainFig',
                figure = stackedLineFig,
            ),
        ]),
        
        html.Div(className='three columns', id = 'controlDiv', children=[
           html.Div([
            dcc.Tabs(id="tabs", value='tab-1', vertical='true', style={'width':'250px'}, children=[
                dcc.Tab(label='stacked line', value='tab-1'),
                dcc.Tab(label='line', value='tab-2'),
                dcc.Tab(label='percent line', value='tab-3'),
                dcc.Tab(label='grouped bar', value='tab-4'),
                dcc.Tab(label='stacked bar', value='tab-5'),
            ]),
           ])
        ], style = {'padding-top' : '5%'})
        
    ]),
    
    html.Div(dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
    ), style = {'padding-top' : '2%',
                'padding-bottom' : '5%'})
    
], style={
    'padding-right' : '5%',
    'padding-left' : '5%'
})


@app.callback(Output('mainFig', 'figure'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        figure=stackedLineFig
        return figure
    elif tab == 'tab-2':
        figure=lineFig
        return figure
    elif tab == 'tab-3':
        figure=percentLineFig
        return figure
    elif tab == 'tab-4':
        figure=groupedBarFig
        return figure
    elif tab == 'tab-5':
        figure=stackedBarFig
        return figure


if __name__ == '__main__':
    #app.run_server(debug=True)

    app.run_server(host='0.0.0.0', port = 8050)

