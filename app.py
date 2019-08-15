#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv('./data/wide_budget.csv')
yeardf, pwdf, devservicedf, entdf, electdf, internaldf, safetydf, comservicedf, econdf, citywidedf = [], [], [], [], [], [], [], [], [], []
totaldf = []

for col in range(1, len(df.columns)):
    yeardf.append(df.columns[col]) #x axis, year
    pwdf.append(df.iloc[0][col]) #y axis, public works
    devservicedf.append(df.iloc[1][col]) # y axis, development services
    entdf.append(df.iloc[2][col]) # y axis, enterprise 
    electdf.append(df.iloc[3][col]) # y axis, elected and appointed
    internaldf.append(df.iloc[4][col]) #y axis, internal services
    safetydf.append(df.iloc[5][col]) # y axis, public safety
    comservicedf.append(df.iloc[6][col]) # y axis, community services
    econdf.append(df.iloc[7][col]) # y axis, economic development
    citywidedf.append(df.iloc[8][col]) #y axis, city wide activities
    totaldf.append(df.iloc[9][col]) # y axis, total

#print(yeardf)
#print (pwdf)
#print(df.iloc[9][:])

fig = go.Figure()
fig.add_trace(go.Scatter(x=yeardf, y=citywidedf, name='city wide activities', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=econdf, name='economic development', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=comservicedf, name='community services', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=safetydf, name='public safety', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=internaldf, name='internal services', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=electdf, name='elected and appointed', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=entdf, name='enterprise', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=devservicedf, name='development services', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=pwdf, name='public works', stackgroup='one')) 
#fig.add_trace(go.Scatter(x=yeardf, y=totaldf, name='total'))

fig.show()


# In[6]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=yeardf, y=citywidedf, name='city wide activities'))
fig.add_trace(go.Scatter(x=yeardf, y=econdf, name='economic development'))
fig.add_trace(go.Scatter(x=yeardf, y=comservicedf, name='community services'))
fig.add_trace(go.Scatter(x=yeardf, y=safetydf, name='public safety'))
fig.add_trace(go.Scatter(x=yeardf, y=internaldf, name='internal services'))
fig.add_trace(go.Scatter(x=yeardf, y=electdf, name='elected and appointed'))
fig.add_trace(go.Scatter(x=yeardf, y=entdf, name='enterprise'))
fig.add_trace(go.Scatter(x=yeardf, y=devservicedf, name='development services'))
fig.add_trace(go.Scatter(x=yeardf, y=pwdf, name='public works')) 
#fig.add_trace(go.Scatter(x=yeardf, y=totaldf, name='total'))

fig.show()


# In[7]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=yeardf, y=citywidedf, name='city wide activities', stackgroup='one', groupnorm='percent'))
fig.add_trace(go.Scatter(x=yeardf, y=econdf, name='economic development', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=comservicedf, name='community services', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=safetydf, name='public safety', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=internaldf, name='internal services', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=electdf, name='elected and appointed', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=entdf, name='enterprise', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=devservicedf, name='development services', stackgroup='one'))
fig.add_trace(go.Scatter(x=yeardf, y=pwdf, name='public works', stackgroup='one')) 
#fig.add_trace(go.Scatter(x=yeardf, y=totaldf, name='total'))

fig.show()


# In[8]:


df['2019-20 Proposed Budget']
df.iloc[0][0]

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


# In[9]:


fig = go.Figure()
fig.add_trace(go.Bar(x=yeardf, y=citywidedf, name='city wide activities'))
fig.add_trace(go.Bar(x=yeardf, y=econdf, name='economic development'))
fig.add_trace(go.Bar(x=yeardf, y=comservicedf, name='community services'))
fig.add_trace(go.Bar(x=yeardf, y=safetydf, name='public safety'))
fig.add_trace(go.Bar(x=yeardf, y=internaldf, name='internal services'))
fig.add_trace(go.Bar(x=yeardf, y=electdf, name='elected and appointed'))
fig.add_trace(go.Bar(x=yeardf, y=entdf, name='enterprise'))
fig.add_trace(go.Bar(x=yeardf, y=devservicedf, name='development services'))
fig.add_trace(go.Bar(x=yeardf, y=pwdf, name='public works')) 
fig.update_layout(barmode='stack')
fig.show()

