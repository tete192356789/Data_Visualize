
from PyQt5.QtWidgets import *
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog,QWidget,QApplication,QTableWidgetItem,QListWidgetItem,QTableView,QSizePolicy,QMessageBox,QAction
from PyQt5.QtCore import  QSortFilterProxyModel, QAbstractTableModel,Qt,QUrl,QDataStream
import json
import openpyxl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from appmanage import *
from io import StringIO
from Model import PandasModel
from PyQt5.QtWebEngineWidgets import *
import altair as alt
from plot_manage import plot_manage
from functools import partial
from PyQt5.QtCore import QTimer
from qtrangeslider import QRangeSlider
from qtrangeslider import QLabeledRangeSlider
import copy
class Ui_win():
    def setupUi(self, win):
        win.setObjectName("win")
        win.resize(1359, 890)
        
        self.centralwidget = QtWidgets.QWidget(win)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(340, 60, 761, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.R_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.R_layout.setContentsMargins(0, 0, 0, 0)
        self.R_layout.setObjectName("R_layout")
        self.tabpage = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabpage.setObjectName("tabpage")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabpage.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.table = QtWidgets.QTableView(self.tab_2)
        self.table.setGeometry(QtCore.QRect(-5, 1, 761, 551))
        self.table.setObjectName("table")
        self.table.setSortingEnabled(True)
     
        self.tabpage.addTab(self.tab_2, "")
        self.R_layout.addWidget(self.tabpage)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 291, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.L_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.L_layout.setContentsMargins(0, 0, 0, 0)
        self.L_layout.setObjectName("L_layout")

        self.head_table = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.head_table.setObjectName("listbox")
    
        self.head_table.setAcceptDrops(True)
        self.head_table.setDragEnabled(True)
        self.head_table.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.head_table.itemDoubleClicked.connect(self.drill_date)
        self.head_table.setSelectionMode(3)
       
        self.lay_wid = QtWidgets.QWidget(self.tab)
        self.lay_wid.setGeometry(QtCore.QRect(0, 0, 751, 551))
        self.lay_wid.setObjectName("lay_wid")
        self.wid_layout = QtWidgets.QVBoxLayout(self.lay_wid)
        self.wid_layout.setContentsMargins(0, 0, 0, 0)
        self.wid_layout.setObjectName("wid_layout")

        '''self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 751, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")'''

      


        self.L_layout.addWidget(self.head_table)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 60, 3, 569))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.import_button = QtWidgets.QPushButton(self.centralwidget)
        self.import_button.setGeometry(QtCore.QRect(50, 770, 221, 31))
        self.import_button.setObjectName("pushButton")
        self.import_button.clicked.connect(self.import_file)

        self.label_path =QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(40, 810, 270, 31))
        self.label_path.setObjectName("label_path")
        

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label.setStyleSheet("font: 57 16pt \"Dubai Medium\";")
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(340, 670, 381, 75))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Vlayout_L = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Vlayout_L.setContentsMargins(0, 0, 0, 0)
        self.Vlayout_L.setObjectName("Vlayout_L")
        self.listWidget_L = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_L.setObjectName("listWidget_L")
        #self.listWidget_L.setAcceptDrops(True)
        #self.listWidget_L.setDragEnabled(True)
        self.listWidget_L.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.listWidget_L.customContextMenuRequested[QtCore.QPoint].connect(self.contextMenuEvent)
        #self.contextMenuEvent(self.listWidget_L)
        
        
      
        self.RD = Row_Drop(self.listWidget_L)
        self.RD.get_list()
        self.RD.setup(self)
        self.RD.setup2(self)
        #self.RD.setup3(self)
        
     

        self.Vlayout_L.addWidget(self.listWidget_L)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(720, 670, 381, 75))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Vlayout_R = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Vlayout_R.setContentsMargins(0, 0, 0, 0)
        self.Vlayout_R.setObjectName("Vlayout_R")
        self.listWidget_R = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget_R.setObjectName("listWidget_R")
        self.listWidget_R.setAcceptDrops(True)
        self.listWidget_R.setDragEnabled(True)
        #self.contextMenuEvent(self.listWidget_R)
        self.listWidget_R.setContextMenuPolicy(Qt.CustomContextMenu)
     

        self.CD = Row_Drop(self.listWidget_R)
        self.CD.get_list()
        self.CD.setup(self)
        self.CD.setup2(self)

        #self.FW = filter_win()
        #self.FW.setup2(self)

        self.Vlayout_R.addWidget(self.listWidget_R)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 640, 101, 31))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(870, 640, 101, 31))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 760, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.plot_graph)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 430, 291, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.L_layout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.L_layout_2.setContentsMargins(0, 0, 0, 0)
        self.L_layout_2.setObjectName("L_layout_2")

        self.measure_table = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.measure_table.setObjectName("mesure_table")

        self.measure_table.setAcceptDrops(True)
        self.measure_table.setDragEnabled(True)
        self.measure_table.setDefaultDropAction(QtCore.Qt.MoveAction)

        self.L_layout_2.addWidget(self.measure_table)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 120, 35))
        self.label_4.setStyleSheet("font: 57 16pt \"Dubai Medium\";")
        self.label_4.setObjectName("label_4")

        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 30, 481, 21))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.search_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.search_layout.setContentsMargins(0, 0, 0, 0)
        self.search_layout.setObjectName("search_layout")

    

        self.unionButton = QtWidgets.QPushButton(self.centralwidget)
        self.unionButton.setGeometry(QtCore.QRect(660, 800, 121, 31))
        self.unionButton.setObjectName("unionButton")
        self.unionButton.clicked.connect(self.union_file)

        ################
        self.cbb =QComboBox()
        self.search_layout.addWidget(self.cbb)
      
        self.cbb.addItem("bar")
        self.cbb.addItem("line")
        self.cbb.addItem("circle")
        self.cbb.addItem("pie")


        win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1111, 21))
        self.menubar.setObjectName("menubar")
        win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(win)
        self.statusbar.setObjectName("statusbar")
        win.setStatusBar(self.statusbar)

        file = self.menubar.addMenu("File")
        save_menu = file.addAction("Save")
        save_menu.triggered.connect(self.save_data)
        load_menu = file.addAction("Load")
        load_menu.triggered.connect(self.load_data)
        group_menu = file.addAction("Group")
        group_menu.triggered.connect(self.group_header)

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")
        self.tabpage.addTab(self.tab3, "")

        self.filt_table = QtWidgets.QTableView(self.tab3)
        self.filt_table.setGeometry(QtCore.QRect(-5, 1, 761, 551))
        self.filt_table.setObjectName("filt_table")
        self.filt_table.setSortingEnabled(True)

        self.retranslateUi(win)
        self.tabpage.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(win)

        self.rower = [{}]

    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "App"))
        self.tabpage.setTabText(self.tabpage.indexOf(self.tab), _translate("win", "Graph"))
        self.tabpage.setTabText(self.tabpage.indexOf(self.tab_2), _translate("win", "Display Table"))
        self.tabpage.setTabText(self.tabpage.indexOf(self.tab3), _translate("win", "Filter Table"))
        self.import_button.setText(_translate("win", "Import File"))
        self.label.setText(_translate("win", "Dimension"))
        self.label_2.setText(_translate("win", "     Row"))
        self.label_3.setText(_translate("win", "   Column"))
        self.pushButton_2.setText(_translate("win", "Plot Graph"))
        self.label_4.setText(_translate("win", "Measurement"))
    
        self.unionButton.setText(_translate("win", "Union"))
        #self.label_path.setText(_translate("win", " "))

    def group_header(self):
        select_item = self.head_table.selectedItems()[0].text()
        select_item2 = self.head_table.selectedItems()[1].text()
        group_header = select_item+','+select_item2
        print(group_header)
    
        self.head_table.addItem(group_header)
        
    #drill down for date type
    def drill_date(self):
        st = self.head_table.selectedItems()[0].text()
        for i in self.type_dict[0]:
            if st == i and self.type_dict[0][i] == 'date':
                manager.split_date(self,i,self.data)
                self.head_table.addItem(f'Month {i}')
                self.head_table.addItem(f'Day {i}')
                self.head_table.addItem(f'Year {i}')
                self.dimension_header.append(f'Month {i}')
                self.dimension_header.append(f'Day {i}')
                self.dimension_header.append(f'Year {i}')
    

    def setup(self,set):
        self.set = set
    #load current data in json file to QlistWidget
    def load_data(self):
        read_file = manager.load_json(self,'metadata.json')

        self.head_table.clear()
        self.measure_table.clear()
        # insert dimension table
        for i in read_file[self.md5_fname]['dimension']:
            self.head_table.addItem(i)
        
        # insert measurement table
        for i in read_file[self.md5_fname]['measurement']:
         
            self.measure_table.addItem(i)
        print('Load data complete')

    #Save current header in mea and di QListWidget to json file
    def save_data(self):
        with open("metadata.json", "r") as jsonFile:
            data = json.load(jsonFile)
        
        fn =self.get_fn()
        print('the fn: ',fn)
        di_list = []
        mea_list = []
        data[fn]['dimension'].clear()
        data[fn]['measurement'].clear()
        for i in range(self.head_table.count()):
         
           # print(self.head_table.item(i,1).text())
            di_list.append(self.head_table.item(i).text())
        for i in range(self.measure_table.count()):

            mea_list.append(self.measure_table.item(i).text())


        

        with open("metadata.json", "w") as jsonFile:
            json.dump(data, jsonFile,indent = 4)
        manager.write_json(self,fn,'dimension',di_list)
        manager.write_json(self,fn,'measurement',mea_list)

    def clear_lb(self):
        self.listWidget_L.clear()
        self.listWidget_R.clear()

        for i in reversed(range(self.wid_layout.count())): 
            self.wid_layout.itemAt(i).widget().setParent(None)

      
    #set table by Model
    def set_table(self,data):
    
        model = PandasModel(data)
        self.table.setModel(model)


    #insert header from json to measure and dimension QListWidget 
    def insert_header_lb(self,fname):
        self.mea_list = []
        read_file = manager.load_json(self,'metadata.json')
 
      
        # insert dimension table
        for i in read_file[fname]['dimension']:
            self.head_table.addItem(i)
        
        # insert measurement table
        for i in read_file[fname]['measurement']:
         
            self.measure_table.addItem(i)
     
  

#################################### current .
    def append_json(self,fname):
        load = manager.load_json(self,'metadata.json')
        manager.check_header_type(self,self.data)
        if load[fname]['dimension'] == [] and load[fname]['measurement'] == []:
        
            
            manager.write_json(self,fname,'dimension',self.dimension_header)
            manager.write_json(self,fname,'measurement',self.measure_header)
        else:
            print('not empty..............')

    def import_file(self):
        self.fname, _ = QFileDialog.getOpenFileName()
        split_fn = self.fname.split('/')
        self.fn = split_fn[-1]
        if self.fname:
            self.data = manager.load_file(self,self.fname)
            print("Import file success File Path is :",self.fname)
            self.set_table(self.data)
            #self.fill_table()
            
            
            self.label_path.setText( self.fname)

            self.md5_fname = manager.md5_convert(self,self.fname)
            manager.create_json(self,self.md5_fname)

            self.append_json(self.md5_fname)
            self.insert_header_lb(self.md5_fname)

        return self.md5_fname
    
    def get_fn(self):
        return self.md5_fname
    
    #edit grid table when
    def edit_table(self,head_list,data,table):
        #set up for gb func
        typer_col = self.get_type()
        typer_row = self.get_type()
        dl = self.get_di_list()

        rr = self.get_roller()
        cr =self.get_roller()

        self.head_data_list = head_list
        
        index_list = []  
        try:                                                        
            for model_index in self.table.selectionModel().selectedRows():       
                index = QtCore.QPersistentModelIndex(model_index)         
                index_list.append(index)                                             

            for index in index_list:                                      
                self.Model.removeRow(index.row())
        except: 
            pass

        print('head list',self.head_data_list)
        for count,i in enumerate(self.head_data_list):
            if ',' in i:
                s = i.split(',')
                self.head_data_list.insert(count,s[0])
                self.head_data_list.remove(i)
        
        #Clear filter table
        #self.filt_table.setRowCount(0)
        #gb = manager.gb(self,typer_row,typer_col,dl,rr,cr,data)
        group_data = data.groupby(self.head_data_list)
      
        print(self.head_data_list)
        pd_gd = pd.DataFrame(group_data[self.head_data_list].head(-1))
        Model = PandasModel(pd_gd)
        table.setModel(Model)
        

    def union_file(self):
       
        self.import_data = self.data
        fname, _ =QFileDialog.getOpenFileName()
        if fname:
            manager.load_file(self,fname)
            manager.get_data(self)
            
            print("File for Union: ",fname)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Do you want to Union? ")
            msg.setWindowTitle(" Union MessageBox")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            ret = QMessageBox.question(msg, 'MessageBox', "Click Ok to Union file", QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Ok:
                print('You have pressed OK...')
                if len(self.import_data.columns) == len(self.data.columns):
                    print('if passed.')
                    self.merge_data = manager.merge_data(self,self.import_data,self.data)
                    self.set_table(self.merge_data)
                    print(self.merge_data)
                    print(self.merge_data.shape[0])
                else:
                    msg2 = QMessageBox()
                    msg2.setIcon(QMessageBox.Question)
                    msg2.setText("Do you want to Union? ")
                    msg2.setWindowTitle(" Union MessageBox")
                    ret = QMessageBox.question(msg2, 'MessageBox', "invalid column", QMessageBox.Ok )

            else:
                print('Merge Canceled...')

    

    def plot_graph(self):
        self.typer_col = self.CD.get_type()
        self.typer_row = self.RD.get_type()
        self.dl = self.RD.get_di_list()

        self.rr = self.RD.get_roller()
        self.cr =self.CD.get_roller()
        
        self.chart_style =str(self.cbb.currentText())
        
     
   
        gb = manager.gb(self,self.typer_row,self.typer_col,self.dl,self.rr,self.cr,self.data)
        print(gb)
        print('**************')
        self.filt_data = manager.query_data(self,self.typer_col,self.typer_row,self.rr,self.cr,self.dimension_header,self.measure_header,gb)
        
       
   
        self.row_list = []
        self.column_list =[]
        
        self.rl = self.RD.get_list()
        self.cl =self.CD.get_list()

        for i in self.rl:
            try:

                x = i.split('(')
                x2 = x[1].split(')')
                self.row_list.append(x2[0])
            except:
                self.row_list.append(i)

        for i in self.cl:
            try:
                x = i.split('(')
                x2 = x[1].split(')')
                self.column_list.append(x2[0])
            except:
                self.column_list.append(i)

        for c,i in enumerate(self.row_list):
            if ',' in i:
                s = i.split(',')[0]
                self.row_list.remove(i)
                self.row_list.insert(c,s)
        for c,i in enumerate(self.column_list):
            if ',' in i:
                s = i.split(',')[0]
                self.column_list.remove(i)
                self.column_list.insert(c,s)

        # print(self.filt_data)
        self.measure_header1 = ['sum(Sales)','sum(Quantity)','sum(Profit)','sum(Discount)','Average(Sales)','Average(Quantity)','Average(Profit)','Average(Discount)',
        'Count(Sales)','Count(Quantity)','Count(Profit)','Count(Discount)','mean(Sales)','mean(Quantity)','mean(Profit)','mean(Discount)','median(Sales)','median(Quantity)','median(Profit)','median(Discount)'
        ]


        for i in reversed(range(self.wid_layout.count())): 
            self.wid_layout.itemAt(i).widget().setParent(None)

        if len(self.row_list) ==1 and len(self.column_list) == 1 and self.cbb.currentText() == "pie":
            plot_manage.pie_chart(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use pie chart')

        elif len(self.row_list) ==1 and len(self.column_list) == 2 and self.cbb.currentText() == "pie":
            plot_manage.pie_chart1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use pie chart1')

        elif len(self.row_list) ==2 and len(self.column_list) == 1 and self.cbb.currentText() == "pie":
            plot_manage.pie_chart2(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use pie chart2')

        elif len(self.row_list) ==2 and len(self.column_list) ==2 and self.cbb.currentText() == "pie":
            plot_manage.pie_chart3(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use pie chart3')

        elif len(self.row_list) ==1 and len(self.column_list) == 1 :
            plot_manage.plot_graph1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph1')
        ##### 2col 1row , 1 measure in row
        elif len(self.row_list) == 1 and len(self.column_list) == 2 and self.column_list[0] not in self.measure_header and self.column_list[1] not in self.measure_header:
            plot_manage.plot_graph2(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph2')
        ##### 2col 1row , 2 measure in col
        elif len(self.row_list) == 1 and len(self.column_list) == 2 and self.column_list[0] in self.measure_header and self.column_list[1] in self.measure_header:
            plot_manage.plot_graph2_1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph2_1')
        ##### 1col 2row , 1 measure in row
        elif len(self.row_list) == 2 and len(self.column_list) == 1 and self.row_list[0] not in self.measure_header and self.row_list[1] not in self.measure_header :
            plot_manage.plot_graph3(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph3')
        ##### 1col 2row , 2 measure in row
        elif len(self.row_list) == 2 and len(self.column_list) == 1 and self.row_list[0] in self.measure_header and self.row_list[1] in self.measure_header :
            plot_manage.plot_graph3_1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph3_1')
        ##### 2col 2row , 2 measure in row
        elif len(self.row_list) == 2 and len(self.column_list) == 2 and self.row_list[0] in self.measure_header and self.row_list[1] in self.measure_header :
            plot_manage.plot_graph4(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph4')
        ##### 2col 2row , 2 measure in col
        elif len(self.row_list) == 2 and len(self.column_list) == 2 and self.column_list[0] in self.measure_header and self.column_list[1] in self.measure_header:
            plot_manage.plot_graph4_1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph4_1')
        ##### 2col 2row , 1 measure in col
        elif len(self.row_list) == 2 and len(self.column_list) == 2 and self.column_list[0] not in self.measure_header and self.column_list[1] in self.measure_header:
            plot_manage.plot_graph5(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph5')
        ##### 3col 1row , 1 measure in row
        elif len(self.row_list) == 1 and len(self.column_list) == 3 :
            plot_manage.plot_graph5_1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph5_1')
        ##### 1col 3row , 1 measure in col
        elif len(self.row_list) == 3 and len(self.column_list) == 1 :
            plot_manage.plot_graph5_2(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph5_2')
        ##### 3col 2row , 2 measure in col
        elif len(self.row_list) == 2 and len(self.column_list) == 3 and self.row_list[0] in self.measure_header:
            plot_manage.plot_graph6_1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph6_1')
        ##### 2col 3row , 2 measure in col
        elif len(self.row_list) == 3 and len(self.column_list) == 2 and self.column_list[0] in self.measure_header:
            plot_manage.plot_graph6_2(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph6_2')
        ##### 3col 3row , 3 measure in col
        elif len(self.row_list) == 3 and len(self.column_list) == 3 and self.column_list[0] in self.measure_header:
            plot_manage.plot_graph7_1(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph7_1')
        ##### 3col 3row , 3 measure in row
        elif len(self.row_list) == 3 and len(self.column_list) == 3 and self.row_list[0] in self.measure_header:
            plot_manage.plot_graph7_2(self,self.row_list,self.column_list,self.filt_data,self.chart_style)
            print('Use graph7_2')
            
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Question)
            msg.setText("Do you want to Union? ")
            msg.setWindowTitle(" Union MessageBox")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            ret = QMessageBox.question(msg, 'MessageBox', "Error row or column invalid.", QMessageBox.Ok)
            
            

        try:
            self.v = WebEngineView()
            self.v.updateChart(self.chart)
            self.wid_layout.addWidget(self.v)
            print(type(self.chart))
        except:
            print('Chart not found....')

    def get_row_lb(self):
        self.row_lb = []
        for i in range(self.listWidget_L.count()):
            self.row_lb.append(self.listWidget_L.item(i).text())
       
        return self.row_lb

    def get_col_lb(self):
        self.col_lb = []
        for i in range(self.listWidget_R.count()):
            self.col_lb.append(self.listWidget_R.item(i).text())
     
        return self.col_lb

    def get_path(self):
        self.fp = self.label_path.text()
        return self.fp
   
    
    def get_mea(self):
        
        return self.measure_header

    def get_di(self):
        return self.dimension_header
    
    def get_data_file(self):
        return self.data
        
    def get_type_dict(self):
        return self.type_dict

    def get_CD(self):
        return self.CD

class Row_Drop(QListWidget,Ui_win):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.u_win = Ui_win()
        self.checked = []
        self.roller =[{}]
        self.val_list = []
        self.type_comp = [{}]
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.resize(381, 75)
        # self.itemDoubleClicked.connect(self.drill_down_dimesion)
    #when drag item in QlistWidget
    def dragEnterEvent(self, event):
        mime = event.mimeData()

        self.mea_list = self.set.get_mea()
        self.di_list = self.set.get_di()
        self.all_data = self.set.get_data_file()
        self.type_row_dict =self.set.get_type_dict() 
        # self.itemDoubleClicked.connect(self.drill_date_row,self.td)
        if (mime.hasText() or 
            mime.hasFormat('application/x-qabstractitemmodeldatalist')):
                event.accept()
        else:
            event.ignore()
     
    #drop item to listbox
    def dropEvent(self, event):
        self.sum_measure = []
        mime = event.mimeData()
        
        
        self.tb = self.set.table
        self.ft =self.set.filt_table
        self.roller_keys = []
        
        
        if mime.hasText():
            if mime in self.mea_list:
             
                item = 'sum'+'('+mime.text()+')'
                self.addItem(item)
            else:
            
                self.addItem(mime.text())
        elif mime.hasFormat('application/x-qabstractitemmodeldatalist'):
            textList = []
            
            stream = QDataStream(mime.data('application/x-qabstractitemmodeldatalist'))
            while not stream.atEnd():
                # we're not using row and columns, but we *must* read them
                row = stream.readInt()
                col = stream.readInt()
                for dataSize in range(stream.readInt()):
                    role, self.value = stream.readInt(), stream.readQVariant()
                    if role == Qt.DisplayRole:
                        item = 'sum'+'('+self.value+')'
                        self.val_list.append(self.value)
                        textList.append(item)
            if self.value in self.mea_list:
              
                self.addItem(', '.join(textList))
           
                self.roller[0][self.value] = []
                self.type_comp[0][self.value] = 'sum'
              
                
               
            else:
                self.addItem(self.value)
                self.roller[0][self.value] = []
            dd = copy.deepcopy(self.roller)
            for i in self.roller[0]:
                if ',' in i:
                    dd[0][i.split(',')[0]]= dd[0][i]
                    del dd[0][i]
            self.roller = copy.deepcopy(dd)
            print('5816846',self.roller)

            
            for i in self.roller[0].keys():
                self.roller_keys.append(i)
            
            Ui_win.edit_table(self,self.roller_keys,self.all_data,self.ft)
            
            self.get_list()
            
    #drag out from listbox
    def dragLeaveEvent(self,event):
        try:
            try:
                self.roller[0].pop(self.currentItem().text())
            except:
                x =self.currentItem().text()
                x2=x.split('(')
                x3=x2[1].split(')')
                self.roller[0].pop(x3[0])
                self.type_comp[0].pop(x3[0])
        except:
            pass
        self.takeItem(self.currentRow())
        self.get_list()

        #self.roller.pop(self.currentItem().text())
    
    def ret_roll(self):
        return self.roller

    def ret_type(self):
        return self.type_comp

    #append data to filter list
    def get_fillist(self,select_item,check,lenlist):
        self.ret_roll()
        self.ret_type()
        self.check = check
        self.lenght_list = lenlist
        self.u_win.setup(self)
        self.filter_val  = "ROW"

        if select_item in self.roller[0]:
            self.roller[0][select_item].clear()

        for i in self.check:
            self.roller[0][select_item].append(i)
     

    def get_type(self):
        return self.type_comp
    #append data in self.roller
    def get_meafill(self,select_item,tup,type):
        self.ret_roll()
        self.si = select_item
        self.my_tup = tup
        self.my_type = type

        if self.si in self.roller[0]:
            self.roller[0][self.si].clear()

        self.roller[0][self.si].append(self.my_tup)
      
   
    def get_filter_val(self):
        return self.filter_val

    def get_roller(self):
        return self.roller

        
    def get_list(self):
        self.row_list = []
        for i in range(self.count()):
            self.row_list.append(self.item(i).text())
        
        return self.row_list
    
    def get_all_data(self):
        return self.all_data

    def get_di_list(self):
        return self.di_list
    #condition of contextmenu event     
    def context_condition(self,measure):
        self.setSelectionMode(QListWidget.SingleSelection)
        self.selected_item = self.selectedItems()[0].text()
        self.selected_row = self.currentRow()
        try:
            self.f_split = self.selected_item.split("(")
            self.s_split = self.f_split[1].split(")")
        except:
            pass
        if self.s_split[0] in self.mea_list:
                
            self.sin_item  = self.s_split[0]
            self.sumitem = measure+"("+self.sin_item+")"
         
            self.insertItem(self.selected_row,self.sumitem)
            #self.addItem(self.sumitem)
            self.takeItem(self.selected_row+1)
            #self.setCurrentRow(self.selected_row)
            QTimer.singleShot(1, partial(self.setCurrentRow, self.selected_row)) 
    #create contextmenu in QlistWidget and get selected item
    def contextMenuEvent(self, event):
        self.selected_item = self.selectedItems()[0].text().split(',')[0]
        st_true = self.selectedItems()[0].text()
     
        if self.selected_item in self.di_list:
            self.filt = filter_win(self,self.all_data,self.selected_item,self.di_list)
            self.filt.setup_filter(self.set2)
        else:
            self.filt = filter_win_measure(self,self.all_data,self.selected_item,self.di_list)
        print('contextMenuEvent active..')
        self.contextMenu = QMenu(self)
      
        self.filterAct = self.contextMenu.addAction("Filter")
       
        
        try:
            
            s1 = self.selected_item.split('(')
            s2=s1[1].split(')')
            if s2[0] in self.mea_list:
                self.sumAct = self.contextMenu.addAction("Sum")
                self.countAct = self.contextMenu.addAction("Count")
                self.meanAct = self.contextMenu.addAction("mean")  
                self.medianAct = self.contextMenu.addAction("median")  
        except:
            pass
        
        for i in self.type_row_dict[0]:
            if self.selected_item == i and self.type_row_dict[0][i] == 'date':
                self.MonthAct = self.contextMenu.addAction("Month")
                self.DateAct = self.contextMenu.addAction("Day")
                self.YearAct = self.contextMenu.addAction("Year")
                manager.split_date(self,self.selected_item,self.all_data)
                
                # self.di_list.append(f'Month {i}')
                # self.di_list.append(f'Date {i}')
                # self.di_list.append(f'Year {i}')
                #self.roller[0][]
            else:
                pass
            
        if 'Month' in self.selected_item :
            self.subDate = self.contextMenu.addAction("Day")
            self.subYear = self.contextMenu.addAction("Year")

        elif 'Day' in self.selected_item:
            self.subMonth = self.contextMenu.addAction("Month")
            self.subYear = self.contextMenu.addAction("Year")

        elif 'Year' in self.selected_item:
            self.subMonth = self.contextMenu.addAction("Month")
            self.subDate = self.contextMenu.addAction("Date")
      
        if ',' in st_true:
            self.drill_down_menu = self.contextMenu.addAction('Drill Down')

        self.action = self.contextMenu.exec_(self.mapToGlobal(event.pos()))

        if self.action == self.filterAct:
            self.get_all_data()
            self.get_select_item()
            self.get_di_list()
            self.filt.show()

        ##### Drill down condition #####    
        try:
            if self.action == self.drill_down_menu:
                dd_split = st_true.split(',')[1]
                self.addItem(dd_split)
                self.roller[0][dd_split] = []
                print(self.roller)
        except:
            pass

        ##### measure context menu add ######
        try:
            if self.action == self.sumAct:
                self.context_condition('sum') 
                self.type_comp[0][self.s_split[0]] = 'sum'
            
            if self.action == self.countAct:
                self.context_condition('count')
                self.type_comp[0][self.s_split[0]] = 'count'
            if self.action == self.meanAct:
                self.context_condition('mean')
                self.type_comp[0][self.s_split[0]] = 'mean'
            if self.action == self.medianAct:
                self.context_condition('median')
                self.type_comp[0][self.s_split[0]] = 'median'
        except:
            pass
        try:
            ##### date menu drilldown #####
            if self. action == self.MonthAct:
                self.addItem(f'Month {self.selected_item}')
                self.di_list.append(f'Month {self.selected_item}')
                self.roller[0][f'Month {self.selected_item}'] = []
                self.takeItem(self.currentRow())
                try:
                    self.roller[0].pop('Ship Date')
                except:
                    pass
            if self. action == self.DateAct:
                self.addItem(f'Day {self.selected_item}')
                self.di_list.append(f'Day {self.selected_item}')
                self.roller[0][f'Day {self.selected_item}']= []   
                self.takeItem(self.currentRow())
                try:
                    self.roller[0].pop('Ship Date')
                except:
                    pass
            if self. action == self.YearAct:
                self.addItem(f'Year {self.selected_item}')
                self.di_list.append(f'Year {self.selected_item}')
                self.roller[0][f'Year {self.selected_item}'] = []
                self.takeItem(self.currentRow())
                try:
                    self.roller[0].pop('Ship Date')
                except:
                    pass
        except:
            pass

        if 'Month' in self.selected_item :
            a = self.selected_item.split('Month ')[1]

        elif 'Day' in self.selected_item:
            a = self.selected_item.split('Day ')[1]

        elif 'Year' in self.selected_item:
            a = self.selected_item.split('Year ')[1]

        try:
            ###### sub date menu drilldown #####
            
            

            if self.action == self.subDate:
                self.addItem(f'Day {a}')
                self.di_list.append(f'Day {a}')
                self.roller[0][f'Day {a}'] = []
                try:
                    self.roller[0].pop('Ship Date')
                except:
                    pass
            if self.action == self.subYear:
                self.addItem(f'Year {a}')
                self.di_list.append(f'Year {a}')
                self.roller[0][f'Year {a}'] = []
                try:
                    self.roller[0].pop('Ship Date')
                except:
                    pass
            if self.action == self.subMonth:
                self.addItem(f'Month {a}')
                self.di_list.append(f'Month {a}')
                self.roller[0][f'Month {a}'] = []
                try:
                    self.roller[0].pop('Ship Date')
                except:
                    pass
        except:
            print('cant')

        

        
        try:
            self.filt.get_checked_item()
            self.checked = self.filt.get_checked_item()
        except:
            pass
    def get_select_item(self):
        return self.selected_item

    def setup2(self,set2):
        self.set2 =set2

    def create_date_menu(self):
        month = self.contextMenu.addAction("Month")
        date = self.contextMenu.addAction("Date")
        year = self.contextMenu.addAction("Year")
    
    def drill_down_dimesion(self):
        select_item = self.selectedItems()[0].text()
        if ',' in select_item:
            s = select_item.split(',')[1]
            self.addItem(s)
            self.roller[0][s] = []
            print(self.roller)

                

#filter window
class filter_win(QMainWindow,Row_Drop,Ui_win):
    def __init__(self,rd,all_data,sel_item,dimension_list):
        super().__init__()
        self.dt = all_data
        self.st = sel_item
        self.dl = dimension_list
        self.checked_item =[]
        self.uf_win = Ui_win()
        #self.uf_win.setup(self)
        self.rd = rd
     

        self.initUI()

    def initUI(self):

        self.setWindowTitle('Filter')
        self.resize(497,576)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 461, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(5, 1, 441, 391))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Apply")
        self.pushButton.clicked.connect(self.apply_callback)
    
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "tab1")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "tab2")

        self.input_list()
    
    def setup_filter(self,set3):
        self.set_filter = set3   

    #append non duplicate data to list 
    def input_list(self):
        self.non_duplicate_data = []
        #No duplicate data in list
    
        if self.st in self.dl:
            for i in self.dt[self.st]:
                if i not in self.non_duplicate_data:
                    self.non_duplicate_data.append(i)
            self.non_duplicate_data.sort()
            for i in self.non_duplicate_data:
                self.item = QtWidgets.QListWidgetItem(i)
                self.item.setFlags(self.item.flags() | QtCore.Qt.ItemIsUserCheckable)
                self.item.setCheckState(QtCore.Qt.Checked)
                self.listWidget.addItem(self.item)
        else:
            print('not Dimension')
    #apply button callback
    def apply_callback(self):
        ## checked item in QlistWidget 
        
        self.checked_item.clear()
        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).checkState() == Qt.Checked:
                self.checked_item.append(self.listWidget.item(i).text())
        
        self.lenlist = self.listWidget.count()
     
        self.rd.get_fillist(self.st,self.checked_item,self.lenlist)  
 
        self.close()
        
    
    def get_checked_item(self):
        return self.checked_item


class filter_win_measure(QMainWindow,Row_Drop,Ui_win):
    def __init__(self,rd,all_data,sel_item,dimension_list):
        super().__init__()
        self.dt = all_data
        self.st = sel_item
        self.st_split1 = self.st.split('(')
        self.st_split2 = self.st_split1[1].split(')')
        self.st_pure = self.st_split2[0]
        self.type_val = self.st_split1[0]
        print('pure: ',self.st_pure)
        self.dl = dimension_list
        
        self.st_max =  getattr(self.dt[self.st_pure],self.type_val)().max()
        self.st_min = getattr(self.dt[self.st_pure],self.type_val)().min()
        self.uf_win = Ui_win()
        #self.uf_win.setup(self)
        self.rd = rd

        self.measure_range = [{}]
        ################# เอาลิส ไปประกาศไว้ใน RowDrop 

        self.initUI()
    def initUI(self):

        self.setWindowTitle('Filter')
        self.resize(497,576)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 461, 421))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
       
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 497, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Apply")
        self.pushButton.clicked.connect(self.measure_apply)
   
    
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "tab1")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "tab2")

        self.label_L = QtWidgets.QLabel(self.tab)
        self.label_L.setGeometry(QtCore.QRect(20, 145, 60, 21))
        self.label_L.setObjectName("label_L")
        self.label_R = QtWidgets.QLabel(self.tab)
        self.label_R.setGeometry(QtCore.QRect(270, 145, 60, 13))
        self.label_R.setObjectName("label_R")
        self.label_L.setText("Min:")
        self.label_R.setText("Max:")

        self.lineedit_L = QLineEdit(self)
        self.lineedit_L.move(65,175)
        self.lineedit_L.resize(150,20)

        self.lineedit_R = QLineEdit(self)
        self.lineedit_R.move(320,175)
        self.lineedit_R.resize(150,20)


        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(57, -1, 350, 401))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.slider = QRangeSlider(Qt.Horizontal)
        self.slider.setObjectName("self.slider")
        self.slider.setGeometry(QtCore.QRect(1, 1, 50, 50))
        self.horizontalLayout.addWidget(self.slider)
        self.slider.valueChanged.connect(self.update_label)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(3)

        self.btn1  = QPushButton(self.tab)
        self.btn1.setObjectName("btn1")
        self.btn1.setText('Submit')
        self.btn1.clicked.connect(self.change_slide_pos)

        self.slider.setMinimum(0)
        self.slider.setMaximum(self.st_max)
        #self.slider.setTickPosition(QSlider.TicksBelow)
      
        print(self.slider.value())

    def change_slide_pos(self):
        le1 = self.lineedit_L.text()
        le2 = self.lineedit_R.text()
        self.slider.setValue((le1,le2))
    def measure_apply(self):
        
        self.measure_range[0][self.st] = self.tup_val
        self.rd.get_meafill(self.st_pure,self.slider.value(),self.type_val)
        self.close()

    def update_label(self):

        self.tup_val = self.slider.value()
        self.lineedit_L.setText(str(self.tup_val[0]))
        self.lineedit_R.setText(str(self.tup_val[1]))
 
#Show Altair Graph in ui by chart
class WebEngineView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.page().profile().downloadRequested.connect(self.onDownloadRequested)
        self.windows = []

    @QtCore.pyqtSlot(QtWebEngineWidgets.QWebEngineDownloadItem)
    def onDownloadRequested(self, download):
        if (
            download.state()
            == QtWebEngineWidgets.QWebEngineDownloadItem.DownloadRequested
        ):
            path, _ = QtWidgets.QFileDialog.getSaveFileName(
                self, self.tr("Save as"), download.path()
            )
            if path:
                download.setPath(path)
                download.accept()

    def createWindow(self, type_):
            if type_ == QtWebEngineWidgets.QWebEnginePage.WebBrowserTab:
                window = QtWidgets.QMainWindow(self)
                view = QtWebEngineWidgets.QWebEngineView(window)
                window.resize(800,550)
                window.setCentralWidget(view)
                window.show()
                return view

    def updateChart(self, chart, **kwargs):
        output = StringIO()
        chart.save(output, "html", **kwargs)
        self.setHtml(output.getvalue())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_win()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
