# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import pandas as pd
import os
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QTableWidgetItem, QApplication
import numpy as np
import seaborn as sns
import statistics as stat
import time
from PyQt5.QtGui import QPixmap, QScreen
# import pyscreenshot
# import cv2
import subprocess

import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 754)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Open_File = QtWidgets.QLabel(self.centralwidget)
        self.Open_File.setGeometry(QtCore.QRect(380, 60, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Open_File.setFont(font)
        self.Open_File.setObjectName("Open_File")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 10, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 220, 741, 411))
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_vd = QtWidgets.QWidget()
        self.tab_vd.setObjectName("tab_vd")
        self.tableWidget1 = QtWidgets.QTableWidget(self.tab_vd)
        self.tableWidget1.setGeometry(QtCore.QRect(40, 20, 651, 341))
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)
        self.tabWidget.addTab(self.tab_vd, "")
        self.tab_s = QtWidgets.QWidget()
        self.tab_s.setObjectName("tab_s")
        self.tableWidget2 = QtWidgets.QTableWidget(self.tab_s)
        self.tableWidget2.setGeometry(QtCore.QRect(50, 20, 651, 341))
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
        self.tabWidget.addTab(self.tab_s, "")
        self.tab_corr = QtWidgets.QWidget()
        self.tab_corr.setObjectName("tab_corr")
        self.tableWidget3 = QtWidgets.QTableWidget(self.tab_corr)
        self.tableWidget3.setGeometry(QtCore.QRect(50, 20, 631, 341))
        self.tableWidget3.setObjectName("tableWidget3")
        self.tableWidget3.setColumnCount(0)
        self.tableWidget3.setRowCount(0)
        self.tabWidget.addTab(self.tab_corr, "")
        self.tab_mv = QtWidgets.QWidget()
        self.tab_mv.setObjectName("tab_mv")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_mv)
        self.textEdit_4.setGeometry(QtCore.QRect(90, 30, 281, 211))
        self.textEdit_4.setObjectName("textEdit_4")
        self.mv_comboBox = QtWidgets.QComboBox(self.tab_mv)
        self.mv_comboBox.setGeometry(QtCore.QRect(480, 60, 161, 22))
        self.mv_comboBox.setObjectName("mv_comboBox")
        self.mv_comboBox_2 = QtWidgets.QComboBox(self.tab_mv)
        self.mv_comboBox_2.setGeometry(QtCore.QRect(480, 110, 161, 22))
        self.mv_comboBox_2.setObjectName("mv_comboBox_2")
        self.mv_pushButton_2 = QtWidgets.QPushButton(self.tab_mv)
        self.mv_pushButton_2.setGeometry(QtCore.QRect(510, 280, 93, 28))
        self.mv_pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mv_pushButton_2.setObjectName("mv_pushButton_2")
        self.mv_shape = QtWidgets.QLabel(self.tab_mv)
        self.mv_shape.setGeometry(QtCore.QRect(190, 280, 55, 16))
        self.mv_shape.setAlignment(QtCore.Qt.AlignCenter)
        self.mv_shape.setObjectName("mv_shape")
        self.mv_lineEdit = QtWidgets.QLineEdit(self.tab_mv)
        self.mv_lineEdit.setGeometry(QtCore.QRect(560, 160, 81, 22))
        self.mv_lineEdit.setObjectName("mv_lineEdit")
        self.mv_value = QtWidgets.QLabel(self.tab_mv)
        self.mv_value.setGeometry(QtCore.QRect(490, 160, 55, 16))
        self.mv_value.setObjectName("mv_value")
        self.SaveData_2 = QtWidgets.QPushButton(self.tab_mv)
        self.SaveData_2.setGeometry(QtCore.QRect(350, 330, 101, 31))
        self.SaveData_2.setObjectName("SaveData_2")
        self.tabWidget.addTab(self.tab_mv, "")
        self.tab_g = QtWidgets.QWidget()
        self.tab_g.setObjectName("tab_g")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_g)
        self.textEdit_6.setGeometry(QtCore.QRect(40, 110, 651, 241))
        self.textEdit_6.setObjectName("textEdit_6")
        self.g_comboBox_3 = QtWidgets.QComboBox(self.tab_g)
        self.g_comboBox_3.setGeometry(QtCore.QRect(70, 50, 161, 31))
        self.g_comboBox_3.setObjectName("g_comboBox_3")
        self.gcomboBox_4 = QtWidgets.QComboBox(self.tab_g)
        self.gcomboBox_4.setGeometry(QtCore.QRect(280, 50, 161, 31))
        self.gcomboBox_4.setObjectName("gcomboBox_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_g)
        self.pushButton_3.setGeometry(QtCore.QRect(530, 50, 93, 28))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_g, "")
        self.graphtab = QtWidgets.QWidget()
        self.graphtab.setObjectName("graphtab")
        self.comboBox = QtWidgets.QComboBox(self.graphtab)
        self.comboBox.setGeometry(QtCore.QRect(80, 30, 181, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.graphtab)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 30, 181, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButtongraph = QtWidgets.QPushButton(self.graphtab)
        self.pushButtongraph.setGeometry(QtCore.QRect(550, 30, 75, 23))
        self.pushButtongraph.setObjectName("pushButtongraph")
        self.gridLayoutWidget = QtWidgets.QWidget(self.graphtab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 100, 531, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayoutgraph = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayoutgraph.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutgraph.setObjectName("gridLayoutgraph")
        self.tabWidget.addTab(self.graphtab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(120, 30, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(330, 25, 341, 81))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(100, 110, 191, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(330, 110, 341, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 160, 191, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(330, 160, 341, 16))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(112, 70, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(110, 240, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_4.setGeometry(QtCore.QRect(110, 280, 161, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.Drop = QtWidgets.QPushButton(self.tab_3)
        self.Drop.setGeometry(QtCore.QRect(490, 270, 93, 28))
        self.Drop.setObjectName("Drop")
        self.SaveData = QtWidgets.QPushButton(self.tab_3)
        self.SaveData.setGeometry(QtCore.QRect(330, 320, 101, 31))
        self.SaveData.setObjectName("SaveData")
        self.addColBtn = QtWidgets.QPushButton(self.tab_3)
        self.addColBtn.setGeometry(QtCore.QRect(330, 210, 101, 31))
        self.addColBtn.setObjectName("addColBtn")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(0, 110, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(0, 160, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.tabWidget.addTab(self.tab_3, "")
        self.File_Size = QtWidgets.QLabel(self.centralwidget)
        self.File_Size.setGeometry(QtCore.QRect(270, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.File_Size.setFont(font)
        self.File_Size.setObjectName("File_Size")
        self.Size = QtWidgets.QLabel(self.centralwidget)
        self.Size.setGeometry(QtCore.QRect(370, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Size.setFont(font)
        self.Size.setObjectName("Size")
        self.File_Size_2 = QtWidgets.QLabel(self.centralwidget)
        self.File_Size_2.setGeometry(QtCore.QRect(460, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.File_Size_2.setFont(font)
        self.File_Size_2.setObjectName("File_Size_2")
        self.Col = QtWidgets.QLabel(self.centralwidget)
        self.Col.setGeometry(QtCore.QRect(560, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Col.setFont(font)
        self.Col.setObjectName("Col")
        self.File_Size_3 = QtWidgets.QLabel(self.centralwidget)
        self.File_Size_3.setGeometry(QtCore.QRect(650, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.File_Size_3.setFont(font)
        self.File_Size_3.setObjectName("File_Size_3")
        self.Row = QtWidgets.QLabel(self.centralwidget)
        self.Row.setGeometry(QtCore.QRect(750, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Row.setFont(font)
        self.Row.setObjectName("Row")
        self.filename = QtWidgets.QLabel(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(380, 110, 321, 41))
        font = QtGui.QFont()
        font.setItalic(True)
        self.filename.setFont(font)
        self.filename.setAlignment(QtCore.Qt.AlignCenter)
        self.filename.setWordWrap(True)
        self.filename.setObjectName("filename")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 70, 41, 28))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.snip = QtWidgets.QPushButton(self.centralwidget)
        self.snip.setGeometry(QtCore.QRect(510, 190, 81, 21))
        self.snip.setObjectName("snip")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.setIcon(QtGui.QIcon("images\Open-512.png"))
        self.pushButton.setIconSize(QtCore.QSize(25, 25))

        self.snip.setIcon(QtGui.QIcon("images\scissors.png"))
        self.snip.setIconSize(QtCore.QSize(25, 25))

        self.pushButton.clicked.connect(self.OpenFile)
        self.mv_pushButton_2.clicked.connect(self.replace_val)
        self.pushButton_3.clicked.connect(self.grouping)
        self.snip.clicked.connect(self.snipfun)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayoutgraph.addWidget(self.canvas, 1, 1)

        self.pushButtongraph.clicked.connect(self.viewGraph)
        self.addColBtn.clicked.connect(self.addColumnsAction)

        self.Drop.clicked.connect(self.dropCol)
        self.SaveData_2.clicked.connect(self.saveFile)
        self.SaveData.clicked.connect(self.saveFile)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto EDA - MADHUR CHHAJED"))
        self.Open_File.setText(_translate("MainWindow", "Load Data File"))
        self.label_3.setText(_translate("MainWindow", "Auto EDA"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_vd), _translate("MainWindow", "View Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_s), _translate("MainWindow", "Summary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_corr), _translate("MainWindow", "Co-relation "))
        self.mv_pushButton_2.setText(_translate("MainWindow", "Go"))
        self.mv_shape.setText(_translate("MainWindow", "Shape"))
        self.mv_value.setText(_translate("MainWindow", "Value :"))
        self.SaveData_2.setText(_translate("MainWindow", "Save Data File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mv), _translate("MainWindow", "Missing Values"))
        self.pushButton_3.setText(_translate("MainWindow", "Go"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_g), _translate("MainWindow", "Grouping"))
        self.pushButtongraph.setText(_translate("MainWindow", "GO"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.graphtab), _translate("MainWindow", "View Graph"))
        self.label.setText(_translate("MainWindow", "Add Columns"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Drop Columns"))
        self.Drop.setText(_translate("MainWindow", "Drop"))
        self.SaveData.setText(_translate("MainWindow", "Save Data File"))
        self.addColBtn.setText(_translate("MainWindow", "Add Column"))
        self.label_7.setText(_translate("MainWindow", "Selected Column"))
        self.label_8.setText(_translate("MainWindow", "Bins"))
        self.label_9.setText(_translate("MainWindow", "Label"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Add/Drop Columns"))
        self.File_Size.setText(_translate("MainWindow", "File Size :"))
        self.Size.setText(_translate("MainWindow", "size"))
        self.File_Size_2.setText(_translate("MainWindow", "Columns :"))
        self.Col.setText(_translate("MainWindow", "size"))
        self.File_Size_3.setText(_translate("MainWindow", "Rows : "))
        self.Row.setText(_translate("MainWindow", "size"))
        self.filename.setText(_translate("MainWindow", "Filename"))
        self.snip.setText(_translate("MainWindow", "Snip"))


    def OpenFile(self):
        time.sleep(2)
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None)
        time.sleep(1)
        self.filename.setText(filename)
        # print(filename)
        global data, data2
        data = pd.read_csv(filename)
        data = pd.DataFrame(data)
        data2 = data

        file_info = os.stat(filename)
        self.Size.setText(self.convert_bytes(file_info.st_size))

        self.clearComboBox()

        #  VIEW TABLE FUNCTIONS HERE
        time.sleep(1)
        self.viewDataTable()
        time.sleep(1)
        self.viewSummaryTable()
        self.viewCorrTable()
        time.sleep(1)

        self.textEdit_4.setText(str(data.isna().sum()))

        for i in data.columns:
            self.mv_comboBox.addItem(i)

        replace_value = ['mean', 'mode', 'median', 'drop rows', 'enter value']
        for i in replace_value:
            self.mv_comboBox_2.addItem(i)

        # self.mv_comboBox.currentIndexChanged.connect(self.replace_val())

        for i in data.columns:
            if data[i].dtypes == 'object':
                self.g_comboBox_3.addItem(i)
            else:
                self.comboBox_3.addItem(i)

        group_item = ['size', 'unique values', 'mean', 'median']

        for i in group_item:
            self.gcomboBox_4.addItem(i)

        # time.sleep(1)

        self.comboBox_2.addItem('Not Required')
        for i in data.columns:
            self.comboBox.addItem(i)
            self.comboBox_2.addItem(i)
            self.comboBox_4.addItem(i)

        self.label_2.setText('Create categorical column based on continuous column \n For creating 2 columns like\n Kid in range (0,8)\n Teenage in range (8,18)')
        self.label_4.setText('Enter bin size like -> 0,8,18')
        self.label_5.setText('Enter label like -> Kid,Teenage')

    def clearComboBox(self):
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.g_comboBox_3.clear()
        self.mv_comboBox.clear()
        self.gcomboBox_4.clear()
        self.mv_comboBox_2.clear()
        self.comboBox_4.clear()
        self.comboBox_3.clear()

    def viewDataTable(self):
        global ncol, nrow
        ncol = len(data.columns)
        nrow = len(data.index)
        # self.Col.setText(str(len(data.columns)))
        # self.Row.setText(str(data.shape[0]))

        self.Col.setText(str(ncol))
        self.Row.setText(str(nrow))

        self.tableWidget1.setRowCount(nrow)
        self.tableWidget1.setColumnCount(ncol)

        # for i in data:
        #     j = data.index(i)
        #     print(j)
        global data_columns
        data_columns = np.array(data.columns)
        for j in range(self.tableWidget1.columnCount()):
            self.tableWidget1.setItem(0, j, QTableWidgetItem(str(data_columns[j])))

        for i in range(self.tableWidget1.rowCount()):
            for j in range(self.tableWidget1.columnCount()):
                x = data.iloc[i, j]
                self.tableWidget1.setItem(i + 1, j, QTableWidgetItem(str(x)))

    # self.tableWidget1.cellChanged.connect(self.onCellChanged)

    def viewSummaryTable(self):

        global num_col
        summ_col = []
        summ_stat = ['count', 'mean', 'std dev', 'min value', '25% quantile', '50% quantile', '75% quantile',
                     'max value']

        for i in data.columns:
            if data[i].dtypes == 'int64' or data[i].dtypes == 'float64':
                summ_col.append(i)

        num_col = summ_col

        print('summ col = ', summ_col)

        summ_ncol = len(summ_col) + 1
        summ_nrow = len(summ_stat) + 1

        print('summary table row and col = ', summ_nrow, summ_ncol)

        self.tableWidget2.setRowCount(summ_nrow)
        self.tableWidget2.setColumnCount(summ_ncol)

        for j in range(self.tableWidget2.columnCount() - 1):
            self.tableWidget2.setItem(0, j + 1, QTableWidgetItem(str(summ_col[j])))

        for i in range(self.tableWidget2.rowCount() - 1):
            self.tableWidget2.setItem(i + 1, 0, QTableWidgetItem(str(summ_stat[i])))

        for i in range(self.tableWidget2.rowCount() - 1):
            for j in range(self.tableWidget2.columnCount() - 1):
                x = data.describe().iloc[i, j]
                h = round(x, 2)
                self.tableWidget2.setItem(i + 1, j + 1, QTableWidgetItem(str(h)))

    def viewCorrTable(self):

        corr_col = num_col
        corr_ncol = len(corr_col) + 1
        self.tableWidget3.setRowCount(corr_ncol)
        self.tableWidget3.setColumnCount(corr_ncol)

        for j in range(self.tableWidget3.columnCount() - 1):
            self.tableWidget3.setItem(0, j + 1, QTableWidgetItem(str(corr_col[j])))

        for i in range(self.tableWidget3.rowCount() - 1):
            self.tableWidget3.setItem(i + 1, 0, QTableWidgetItem(str(corr_col[i])))

        for i in range(self.tableWidget3.rowCount() - 1):
            for j in range(self.tableWidget3.columnCount() - 1):
                x = data.corr().iloc[i, j]
                h = round(x, 2)
                self.tableWidget3.setItem(i + 1, j + 1, QTableWidgetItem(str(h)))

        pass

    def replace_val(self):
        global mv_a, mv_b
        mv_a = self.mv_comboBox.currentText()
        mv_b = self.mv_comboBox_2.currentText()

        # if mv_a in data.columns:
        #     pass
        # print(mv_a, mv_b)

        # for i in data.columns:
        #     if mv_a == i:
        #         selected_col = i
        #         print('selected_col=', selected_col)

        if mv_b == 'mean':
            print('aaaaa')

            temp_mean = data[mv_a].mean()
            print('temp mean = ', temp_mean)
            data[mv_a].fillna(temp_mean, inplace=True)
            print('bbbbbb')


        elif mv_b == 'median':
            temp_median = data[mv_a].median()
            print('temp mean = ', temp_median)
            data[mv_a].fillna(temp_median, inplace=True)

        elif mv_b == 'mode':
            temp_mode = data[mv_a].mode()
            print('temp mean = ', temp_mode)
            data[mv_a].fillna(temp_mode, inplace=True)

        elif mv_b == 'enter value':
            mv_value = self.mv_lineEdit.text()
            print('\n\n\n Selected Col Dtype', data[mv_a].dtypes)

            if data[mv_a].dtypes == 'float64':
                data[mv_a].fillna(float(mv_value), inplace=True)
            elif data[mv_a].dtypes == 'int64':
                data[mv_a].fillna(int(mv_value), inplace=True)
            else:
                data[mv_a].fillna(str(mv_value), inplace=True)


        else:
            data.dropna(subset=[mv_a], inplace=True)
            self.mv_shape.setText(str(data.shape))

        self.textEdit_4.setText(str(data.isna().sum()))

        # self.textEdit_4.setText('')
        # self.textEdit_4.setText(str(data.isna().sum()))

        # print('\n\n mv_a \n\n', str(data[mv_a][:10]))

    def grouping(self):
        #

        # if self.g_comboBox_3.SelectedIndex == -1:    # (comboBox1.SelectedIndex == -1)
        #     print('TEST')
        #     pass
        #
        # else:

        g_a = self.g_comboBox_3.currentText()
        g_b = self.gcomboBox_4.currentText()

        if g_b == 'size':

            self.textEdit_6.setText(str(data.groupby(g_a).size()))
        elif g_b == 'unique values':
            self.textEdit_6.setText(str(data.groupby(g_a).nunique()))
        elif g_b == 'mean':
            self.textEdit_6.setText(str(data.groupby(g_a).mean()))
        elif g_b == 'median':
            self.textEdit_6.setText(str(data.groupby(g_a).median()))
        else:
            pass

    def onCellChanged(self, row, column):

        text = self.tableWidget1.item(row, column).text()
        number = QTableWidgetItem(text)
        self.tableWidget1.setItem(row, column, number)

        # text = self.tableWidget1.item(row, column).text()
        # number = float(text)
        # data.set_value(row, column, number)

    def convert_bytes(self, num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0

    def snipfun(self):

        # print('SNIP')
        #
        # #shot = MainWindow.grabWindow(widget)
        # #img = QPixmap.grabWindow(app.desktop().winId(),180, 220, 741, 411)
        #
        subprocess.call(r'SnippingTool.exe')
        # monitor = (400,500,3000,1000)
        # im = pyscreenshot.grab(bbox=monitor)
        # print('TEST1')
        #
        # # im = QScreen.grabWindow(
        # #     app.primaryScreen(),
        # #     QApplication.desktop().winId()
        # # )
        #
        # print('TEST1')
        #

        #
        #
        # #img.save('shot.jpg', 'jpg')
        # print('TEST2')
        #
        # im.show()
        #
        # print('TEST3')
        # roi = QRect(
        #     180, 220, 741, 411
        # )

        # im2 = cv2.imread('screenshot2.png')
        # time.sleep(1)
        # cropped = im2.copy(180, 220, 741, 411)
        # print('TEST1')
        # im.save('screenshot33.png')
        # # print('TEST1')
        # im.show()
        # print('TEST1')

        pass

    def viewGraph(self):

        self.figure.clear()
        ax = self.figure.add_subplot(1, 1, 1)

        vg_a = self.comboBox.currentText()
        vg_b = self.comboBox_2.currentText()

        # print('vga',np.dtype(data[vg_a]))
        # print('vgb', np.dtype(data[vg_b]))

        if vg_a == vg_b or vg_b == 'Not Required':
            # 1 VARAIBLE GRAPH
            if np.dtype(data[vg_a]) == 'int64' or np.dtype(data[vg_a]) == 'float64':
                sns.distplot(data[vg_a], hist=True, ax=ax)
                pass
            else:
                sns.countplot(x=vg_a, data=data, ax=ax)
                pass

        else:
            # 2 VARIABLE GRAPH
            if np.dtype(data[vg_a]) != 'object' and np.dtype(data[vg_b]) == 'object':
                sns.boxplot(y=vg_a, x=vg_b, data=data, ax=ax)
                pass
            elif np.dtype(data[vg_a]) != 'object' or np.dtype(data[vg_b]) != 'object':
                sns.lineplot(x=vg_a, y=vg_b, data=data, ax=ax)
                pass
            elif np.dtype(data[vg_a]) == 'object' and np.dtype(data[vg_b]) != 'object':
                sns.barplot(ax=ax, x=vg_a, y=vg_b, data=data)
            else:
                # sns.catplot(ax=ax, x=vg_a, y=vg_b, data=data,kind='bar')
                pass

        # rand_d = [random.random() for i in range(10)]
        # print('rand d',rand_d)
        # self.figure.clear()
        # print('test')
        # ax = self.figure.add_subplot(1,1,1)
        # print('test')
        # #sns.lineplot( x='sepal_length',y='sepal_width',data=data, ax=ax )
        # sns.boxplot(data=data,ax=ax)
        # print('test')
        #
        # self.canvas.draw()
        # print('test')
        self.canvas.draw()
        pass

    def addColumnsAction(self):

        addcolselect = self.comboBox_3.currentText()
        newcol = 'Categorical_' + str(addcolselect)

        bins = list(map(int, self.lineEdit.text().split(',')))
        label = self.lineEdit_2.text().split(',')

        print('new col = ', newcol)
        print('col = ', addcolselect)
        print('bin = ', bins)
        print('label = ', label)

        temp = pd.cut(data[addcolselect], bins=bins, labels=label)
        #colnum = ncol + 1
        data[newcol] = temp

        print('data = \n', data.head())

        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("New column "+ newcol+ 'is added to dataframe')
        msg.exec_()

        pass

    def dropCol(self):
        drop_col = self.comboBox_4.currentText()
        data.drop([str(drop_col)], axis=1, inplace=True)
        print('data \n', data.head())

        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("Selected column is dropped")
        msg.exec_()

        pass


    def saveFile(self):
        #data, _ = QtWidgets.QFileDialog.getSaveFileName(None)
        print('TEST')
        newname = str(self.filename.text())
        print('newname = ',newname)
        print('TEST')
        #data.to_csv(str(newname)+'.csv')
        data.to_csv('newfile.csv',index=False)

        #a, _ = QtWidgets.QFileDialog.getSaveFileName(None)

        print('TEST')
        #QMessageBox.about(self, "Information ", "csv file with name"+newname+'is saved ')
        msg = QMessageBox()
        msg.setWindowTitle("Information")
        msg.setText("New modified dataset file newfile.csv is saved ")
        msg.exec_()
        pass




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
