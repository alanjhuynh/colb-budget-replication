#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv('./data/wide_budget.csv')


fig = go.Figure()

for i in range(len(df.columns)-1):
    fig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0], stackgroup='one'))

fig.show()


fig = go.Figure()

for i in range(len(df.columns)-1):
    fig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))
    
fig.show()


fig = go.Figure()

for i in range(len(df.columns)-1):
    fig.add_trace(go.Scatter(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0], stackgroup='one', groupnorm='percent'))

fig.show()


fig = go.Figure()

for i in range(len(df.columns)-1):
    fig.add_trace(go.Bar(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))

fig.show()


fig = go.Figure()

for i in range(len(df.columns)-1):
    fig.add_trace(go.Bar(x=df.columns[1:], y=df.iloc[i][1:], name=df.iloc[i][0]))

fig.update_layout(barmode='stack')
fig.show()


labels=[]
values=[]

def clean_column_name(x):
    return x.replace(' ','_').lower()

for i in range(len(df['2019-20 Proposed Budget'])-1):
    labels.append(df.iloc[i][0])
    values.append((df['2019-20 Proposed Budget'][i]))
    values[i] = values[i].replace(',','')
    values[i] = values[i].replace('$','')
    values[i] = int(values[i])
    
values
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()




