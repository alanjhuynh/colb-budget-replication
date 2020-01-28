import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly
import plotly.graph_objects as go

df=pd.read_csv('./data/wide_budget.csv')
entDf=pd.read_csv('./data/enterprise_narrow1_budget.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': 'black',
    'default': 'black',
    'border': 'transparent'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

###################################################################

def clean_column_name(x):
    return x.replace(' ','_').lower()

def create_stacked_line(df):
    stackedLineFig = go.Figure()
    
    for i in range(len(df.index)-1):
        stackedLineFig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0], stackgroup='one'))
    
    return stackedLineFig

def create_line(df):
    lineFig = go.Figure()

    for i in range(len(df.index)-1):
        lineFig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))
        
    return lineFig

def create_percent_line(df):
    percentLineFig = go.Figure()

    for i in range(len(df.index)-1):
        percentLineFig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0], stackgroup='one', groupnorm='percent'))

    return percentLineFig

def create_grouped_bar(df):
    groupedBarFig = go.Figure()

    for i in range(len(df.index)-1):
        groupedBarFig.add_trace(go.Bar(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))
        
    return groupedBarFig

def create_stacked_bar(df):
    stackedBarFig = go.Figure()

    for i in range(len(df.index)-1):
        stackedBarFig.add_trace(go.Bar(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))
        stackedBarFig.update_layout(barmode='stack')
        
    return stackedBarFig

def create_pie(df):
    labels=[]
    values=[]

    for i in range(len(df['2019-20 Proposed Budget'])-1):
        labels.append(df.iloc[i][0])
        values.append((df['2019-20 Proposed Budget'][i]))
        values[i] = values[i].replace(',','')
        values[i] = values[i].replace('$','')
        values[i] = int(values[i])
    
    pieFig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    
    return pieFig

def create_all(df):
    figure = create_stacked_line(df)
    figure = create_line(df)
    figure = create_percent_line(df)
    figure = create_grouped_bar(df)
    figure = create_stacked_bar(df)

stackedLineFig = create_stacked_line(df)
#stackedLineFig.update_layout(height=100%)
#stackedLineFig.update_layout(plot_bgcolor='black', paper_bgcolor='white')

###################################################################

app.layout = html.Div(children=[
    html.Div(className='fullscreen', children=[
        html.Div(className='fullscreen30', children=[
            html.H3(className='sidepanel sp-title', children=[
                'LONG BEACH BUDGET'
            ]),
            html.P(className='sidepanel sp-text', children=[
                'Select different graph types or filter specific departments.'
            ]),
            html.Div(className='sp-dropdown', children=[
                dcc.Dropdown(
                    id='deptDropdown',
                    options=[
                        {'label': 'Departments', 'value': 'dept'},
                        {'label': 'Enterprise', 'value': 'ent'},
                    ],
                    value='dept'
                )
            ]),
            html.Div(className='sp-dropdown', children=[
                dcc.Tabs(id="tabs", value='tab-1', vertical=True, style={'width':'22.5vw'},children=[
                    dcc.Tab(className='sp-tab-text', label='Stacked Line', value='tab-1'),
                    dcc.Tab(className='sp-tab-text', label='Line', value='tab-2'),
                    dcc.Tab(className='sp-tab-text', label='Percent Line', value='tab-3'),
                    dcc.Tab(className='sp-tab-text', label='Grouped Bar', value='tab-4'),
                    dcc.Tab(className='sp-tab-text', label='Stacked Bar', value='tab-5'),
                    dcc.Tab(className='sp-tab-text', label='Pie', value='tab-6')
                ])
            ]),
            dcc.Markdown(className='sidepanel sp-text', children=[
                "Created by [Alan Huynh](https://alanjhuynh.com/)\n",
                "Source: [City of Long Beach](http://www.longbeach.gov/finance/city-budget-and-finances/budget/budget-information/)"
            ]),
        ]),
        html.Div(className='fullscreen70-top', children=[
            html.Div(className='fullscreen70-graph', children=[
                dcc.Graph(
                    id = 'mainFig',
                    figure = stackedLineFig,
                ),
            ]),
        ]),
        html.Div(className='fullscreen70-bottom', children=[
            html.Div(className='fullscreen70-chart', children=[
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict('records'),
                )
            ])
        ]),
    ])
])

###################################################################

@app.callback(Output('mainFig', 'figure'),
              [Input('tabs', 'value'),
               Input('deptDropdown', 'value')])
def render_content(tab, value):
    if value == 'ent':
        currDf = entDf
    elif value == 'dept':
        currDf = df
        
    if tab == 'tab-1':
        figure=create_stacked_line(currDf)
        return figure
    elif tab == 'tab-2':
        figure=create_line(currDf)
        return figure
    elif tab == 'tab-3':
        figure=create_percent_line(currDf)
        return figure
    elif tab == 'tab-4':
        figure=create_grouped_bar(currDf)
        return figure
    elif tab == 'tab-5':
        figure=create_stacked_bar(currDf)
        return figure
    elif tab == 'tab-6':
        figure=create_pie(currDf)
        return figure


if __name__ == '__main__':
    app.run_server(debug=True)

    app.run_server(host='0.0.0.0', port = 8050)