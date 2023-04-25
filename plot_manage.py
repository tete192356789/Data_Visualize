from altair import *
import pandas as pd
import altair as alt
import altair_viewer
from altair import Chart, load_dataset
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication
from io import StringIO

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from appmanage import *
import sys

class plot_manage():
    alt.data_transformers.enable('data_server')
    alt.data_transformers.disable_max_rows()
    altair_viewer._global_viewer._use_bundled_js = False
##### 1col 1row
    def plot_graph1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
            y=row[0],
            x=col[0],
            tooltip = row + col
            ).resolve_scale(
            x='independent',
            y='independent'
            ),self.chart_style)()
        return self.chart

##### 2col 1row , 1 measure
    def plot_graph2(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        column=col[0],
        x= alt.X(col[1],sort=alt.EncodingSortField(field=col[1], order='ascending')),
        y= row[0],
        tooltip = row + col,
        ).resolve_scale(
        x='independent',
        ),self.chart_style)()
    
        return self.chart

##### 2col 1row , 2 measure
    def plot_graph2_1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        y= alt.Y(row[0],sort=alt.EncodingSortField(field=row[0], order='ascending')),
        tooltip = row + col
        ).resolve_scale(
        y='independent'
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.X(col[0])) | self.chart.encode(alt.X(col[1]))
        return self.chart

##### 1col 2row , 1 measure
    def plot_graph3(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        row=row[0],
        x= col[0],
        y= alt.Y(row[1],sort=alt.EncodingSortField(field=row[1], order='ascending')),
        tooltip = row + col
        ).resolve_scale(
        y='independent'
        ),self.chart_style)()
    
        return self.chart
##### 1col 2row , 2 measure
    def plot_graph3_1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        x= alt.X(col[0],sort=alt.EncodingSortField(field=col[0], order='ascending')),
        tooltip = row + col
        ).resolve_scale(
        x='independent',
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.Y(row[0])) & self.chart.encode(alt.Y(row[1]))
        return self.chart
##### 2col 2row , 2 measure, groupby column
    def plot_graph4(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        column=alt.Column(col[0]),
        x= alt.X(col[1],sort=alt.EncodingSortField(field=col[1], order='ascending')),
        tooltip = row + col
        ).resolve_scale(
        x='independent',
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.Y(row[0])) & self.chart.encode(alt.Y(row[1]))
    
        return self.chart

##### 2col 2row , 2 measure, groupby row
    def plot_graph4_1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        row=row[0],
        y= alt.Y(row[1],sort=alt.EncodingSortField(field=row[1], order='ascending')),
        tooltip = row + col
        ).resolve_scale(
        y='independent'
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.X(col[0])) | self.chart.encode(alt.X(col[1]))
        return self.chart
#### 2col 2row, 1 measure in col
    def plot_graph5(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        column=col[0],
        x= alt.X(col[1],sort=alt.EncodingSortField(field=col[1], order='ascending')),
        y= row[1],
        row = row[0],
        tooltip = row + col
        ).resolve_scale(
        y='independent'
        ),self.chart_style)()
        return self.chart

#### 3col 1row, 1 measure in row
    def plot_graph5_1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        column=col[0],
        x= alt.X(col[1],sort=alt.EncodingSortField(field=col[1], order='ascending')),
        y= row[0],
        color = col[2] ,
        tooltip = row + col
        ).resolve_scale(
        x='independent',
        ),self.chart_style)()

        return self.chart
#### 1col 3row, 1 measure in col
    def plot_graph5_2(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        row=row[0],
        x= col[0],
        y= alt.Y(row[1],sort=alt.EncodingSortField(field=row[1], order='ascending')),
        color = row[2],
        tooltip = row + col
        ).resolve_scale(
        y='independent'
        ),self.chart_style)()

        return self.chart

#### 3col 2row, 2 measure in row
    def plot_graph6_1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        column=col[0],
        x= alt.X(col[1],sort=alt.EncodingSortField(field=col[1], order='ascending')),
        color = col[2] ,
        tooltip = row + col
        ).resolve_scale(
        x='independent'
       
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.Y(row[0])) & self.chart.encode(alt.Y(row[1]))
        return self.chart

    #### 3col 2row, 2 measure in col
    def plot_graph6_2(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        row=row[0],
        y= alt.Y(row[1],sort=alt.EncodingSortField(field=row[1], order='ascending')),
        color = row[2] ,
        tooltip = row + col
        ).resolve_scale(
        y='independent'
       
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.X(col[0])) | self.chart.encode(alt.X(col[1]))
        return self.chart

    ##### 3col 3row , 3 measure in col
    def plot_graph7_1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        row=row[0],
        color = row[2],
        y= alt.Y(row[1],sort=alt.EncodingSortField(field=row[1], order='ascending')),
        tooltip = row + col
        ).resolve_scale(
        y='independent'
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.X(col[0])) | self.chart.encode(alt.X(col[1])) | self.chart.encode(alt.X(col[2]))
        return self.chart

    ##### 3col 3row , 3 measure in row
    def plot_graph7_2(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
        column=col[0],
        color = col[2],
        x = alt.X(col[1],sort=alt.EncodingSortField(field=col[1], order='ascending')),
        tooltip = row + col
        ).resolve_scale(
        x='independent'
        ),self.chart_style)()
        self.chart = self.chart.encode(alt.Y(row[0])) & self.chart.encode(alt.Y(row[1])) & self.chart.encode(alt.Y(row[2]))
        return self.chart

    def plot_graph1_1(self,row,col,data,type):
        self.type =type
        self.chart_style = 'mark_'+self.type
        self.chart = getattr(alt.Chart(data).mark_bar().encode(
            x=alt.X(col[0], axis = alt.Axis(title = 'Date'.upper(), format = ("%Y"))),
            y=row[0],
            tooltip = row + col
            ).resolve_scale(
            x='independent',
            y='independent'
            ),self.chart_style)()

        return self.chart
        

    def pie_chart(self,row,col,data,type):
        measure = []
        colour = []
        self.type =type
        self.chart_style = 'mark_'+self.type

        if row[0] in self.measure_header:
            measure.append(row[0])
            colour.append(col[0])
        else: #col[0] in self.measure_header:
            measure.append(col[0])
            colour.append(row[0])
       
        circle = alt.Chart(data).encode(
        theta=alt.Theta(measure[0], stack=True), color=alt.Color(colour[0]),
        tooltip = row + col 
).resolve_scale(theta = 'independent')

        self.chart = circle.mark_arc(outerRadius=120) 
       # text = base.mark_text(radius=140, size=20).encode(text="Region:N")
        return self.chart

    def pie_chart1(self,row,col,data,type):
        measure = []
        colour = []
        self.type =type
        self.chart_style = 'mark_'+self.type

        if row[0] in self.measure_header:
            measure.append(row[0])
            colour.append(col[0])
        else: #col[0] in self.measure_header:
            measure.append(col[0])
            colour.append(row[0])
       
        circle = alt.Chart(data).encode(
        theta=alt.Theta(measure[0], stack=True),
        column = col[1],
        color=alt.Color(colour[0]),
        tooltip = row + col 
).resolve_scale(theta = 'independent')
        self.chart = circle.mark_arc(outerRadius=120) 
        return self.chart

    def pie_chart2(self,row,col,data,type):
        measure = []
        colour = []
        
        if row[0] in self.measure_header:
            measure.append(row[0])
            colour.append(col[0])
        else: #col[0] in self.measure_header:
            measure.append(col[0])
            colour.append(row[0])
       
        circle = alt.Chart(data).encode(
        theta=alt.Theta(measure[0], stack=True),
        row = row[1],
        color=alt.Color(colour[0]),
        tooltip = row + col 
).resolve_scale(theta = 'independent')

        self.chart = circle.mark_arc(outerRadius=120) 
       # text = base.mark_text(radius=140, size=20).encode(text="Region:N")
        return self.chart
    def pie_chart3(self,row,col,data,type):
        measure = []
        colour = []

        for i in range(len(row)):
            if row[i] in self.measure_header:
                measure.append(row[i])
             
            else: #col[0] in self.measure_header:
             
                colour.append(row[i])
        for i in range(len(col)):
            if col[i] in self.measure_header:
                measure.append(col[i])
             
            else: #col[0] in self.measure_header:
             
                colour.append(col[i])
        print('++++++++++++++++++++',measure,colour)
        circle = alt.Chart(data).encode(
        column = colour[0],
        color=alt.Color(colour[1],sort=alt.EncodingSortField(field=colour[1], order='ascending')),
        tooltip = row + col 
).resolve_scale(theta = 'independent')

        self.chart = circle.mark_arc(outerRadius=120) 
        self.chart = self.chart.encode(alt.Theta(measure[0],stack=True)) & self.chart.encode(alt.Theta(measure[1],stack=True))
       # text = base.mark_text(radius=140, size=20).encode(text="Region:N")
        return self.chart