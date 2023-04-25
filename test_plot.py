from altair import *
import pandas as pd
import altair as alt
import altair_viewer
from altair import Chart, load_dataset
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from appmanage import *
import sys
import itertools as it
row = ['State','Region']
col= ['Sales']
data =pd.read_csv('Superstore.csv', encoding='windows-1252')

def plot_graph1(row,col,data):
        
    chart_name = []    
    for i in range(len(row)):
        chart = alt.Chart(data).transform_window(
        rank='rank'+'('+row[i]+')',
        sort=[alt.SortField(row[i], order='descending')],
        groupby=[row[i]]
        ).mark_bar().encode(
        row=Row(row[i]),
        y=row[i],
        x=col[0],
        ).resolve_scale(
        x='independent'
        )

        '''i = chart
        chart_name.append(i)
        plot_chart = alt.vconcat(
        chart_name,
        data=data,
        title="Superstore"
        )
    print(chart_name)
    plot_chart.serve()'''

plot_graph1(row,col,data)
