# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asd.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_win(object):
    def setupUi(self, win):
        win.setObjectName("win")
        win.resize(1119, 849)
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
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 0, 751, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(240, 210, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.tabpage.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 761, 551))
        self.tableView.setSortingEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tabpage.addTab(self.tab_2, "")
        self.R_layout.addWidget(self.tabpage)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 291, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.L_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.L_layout.setContentsMargins(0, 0, 0, 0)
        self.L_layout.setObjectName("L_layout")
        self.head_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget)
        self.head_table.setObjectName("head_table")
        self.head_table.setColumnCount(0)
        self.head_table.setRowCount(0)
        self.L_layout.addWidget(self.head_table)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(320, 60, 3, 569))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 770, 221, 31))
        self.pushButton.setObjectName("pushButton")
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
        self.Vlayout_L.addWidget(self.listWidget_L)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(720, 670, 381, 75))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Vlayout_R = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Vlayout_R.setContentsMargins(0, 0, 0, 0)
        self.Vlayout_R.setObjectName("Vlayout_R")
        self.listWidget_R = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget_R.setObjectName("listWidget_R")
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 430, 291, 331))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.L_layout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.L_layout_2.setContentsMargins(0, 0, 0, 0)
        self.L_layout_2.setObjectName("L_layout_2")
        self.measure_table = QtWidgets.QTableWidget(self.horizontalLayoutWidget_2)
        self.measure_table.setObjectName("measure_table")
        self.measure_table.setColumnCount(0)
        self.measure_table.setRowCount(0)
        self.L_layout_2.addWidget(self.measure_table)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 400, 111, 31))
        self.label_4.setStyleSheet("font: 57 16pt \"Dubai Medium\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(470, 30, 481, 21))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.search_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.search_layout.setContentsMargins(0, 0, 0, 0)
        self.search_layout.setObjectName("search_layout")
        win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 21))
        self.menubar.setObjectName("menubar")
        win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(win)
        self.statusbar.setObjectName("statusbar")
        win.setStatusBar(self.statusbar)

        self.retranslateUi(win)
        self.tabpage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "App"))
        self.tabpage.setTabText(self.tabpage.indexOf(self.tab), _translate("win", "Tab 1"))
        self.tabpage.setTabText(self.tabpage.indexOf(self.tab_2), _translate("win", "Tab 2"))
        self.pushButton.setText(_translate("win", "Import File"))
        self.label.setText(_translate("win", "Dimension"))
        self.label_2.setText(_translate("win", "     Row"))
        self.label_3.setText(_translate("win", "   Column"))
        self.pushButton_2.setText(_translate("win", "Plot Graph"))
        self.label_4.setText(_translate("win", "Measurement"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_win()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())