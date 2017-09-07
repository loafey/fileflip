# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import time
import threading
import atexit
import webbrowser
import multiprocessing
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import FileFlip_Module
working_dir = "C:\\"
port = 8000
server_on = False

output_file= str(os.getcwdb(),'utf-8')+"\\hiddenservice.txt"
temp_del = open(output_file,"w")
temp_del.close()

#class Ui_MainWindow(object):
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.using_tor = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 310)
        MainWindow.setFixedHeight(160)
        MainWindow.setFixedWidth(264)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tOutput.setGeometry(QtCore.QRect(0, 74, 264, 121))
        self.tOutput.setReadOnly(True)
        self.tOutput.setObjectName("tOutput")
        self.bStart = QtWidgets.QPushButton(self.centralwidget)
        self.bStart.setGeometry(QtCore.QRect(0, 29, 75, 23))
        self.bStart.setObjectName("bStart")
        self.bStop = QtWidgets.QPushButton(self.centralwidget)
        self.bStop.setGeometry(QtCore.QRect(80, 29, 75, 23))
        self.bStop.setObjectName("bStop")
        self.tDirectory = QtWidgets.QLineEdit(self.centralwidget)
        self.tDirectory.setGeometry(QtCore.QRect(0, 0, 191, 20))
        self.tDirectory.setAccessibleDescription("")
        self.tDirectory.setObjectName("tDirectory")
        self.bBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.bBrowse.setGeometry(QtCore.QRect(190, -1, 75, 23))
        self.bBrowse.setObjectName("bBrowse")
        self.tPort = QtWidgets.QLineEdit(self.centralwidget)
        self.tPort.setGeometry(QtCore.QRect(162, 30, 101, 20))
        self.tPort.setObjectName("tPort")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(270, 0, 301, 311))
        self.treeView.setObjectName("treeView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tDirectory.textChanged.connect(self.updateWorkingDir)
        self.tPort.textChanged.connect(self.updatePort)
        self.bStart.clicked.connect(self.StartServer)
        self.bStop.clicked.connect(self.KillServer)
        self.bBrowse.clicked.connect(self.FindDirectory)

        self.bCheckTor = QtWidgets.QCheckBox(self.centralwidget)
        self.bCheckTor.setGeometry(2,57,100,15)
        self.bCheckTor.setText("Use Tor?")
        self.bCheckTor.clicked.connect(self.EnableTor)

        self.tAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.tAddress.setGeometry(QtCore.QRect(102,52,160,20))
        self.tAddress.setAccessibleDescription("")
        self.tAddress.setObjectName("tAddress")
        self.tAddress.setPlaceholderText("Onion address")
        self.tAddress.setReadOnly(True)

        self.update_address = QtCore.QTimer()
        self.update_address.setInterval(500)
        self.update_address.timeout.connect(self.func_update_address)
        self.update_address.start()
        

        self.bStop.setEnabled(False)

        self.Output("Program made by samhamnam.")
        self.Output("Make sure you press stop server before you quit!")
        self.Output("Failing to do so may require killing the process in your activty manager!")
        self.Output("To use tor you need TOR Browser running, address will appear in hiddenservice.txt")

    def closeEvent(self, event):
        print("X is clicked")

    def func_update_address(self):
        self.tAddress.setText(open(output_file).read())

    def EnableTor(self):
        if self.bCheckTor.isChecked() == True:
            self.using_tor = True
            print("Using TOR? "+str(self.using_tor))
        else:
            self.using_tor = False
            print("Using TOR? " +str(self.using_tor))

    def updateWorkingDir(self):
        working_dir = self.tDirectory.text()
        #self.e = multiprocessing.Process(target=FileFlip_Module.start_server, args=(port, self.tDirectory.text()))

    def updatePort(self):
        port = self.tPort.text()
    
    def StartServer(self):
        if self.using_tor == False:
            webbrowser.open("http://127.0.0.1:"+str(port))
            print("Started without TOR: "+str(self.using_tor))
            self.e = multiprocessing.Process(target=FileFlip_Module.start_server, args=(port, self.tDirectory.text()))
            self.e.start()
            self.server_on_button()
        if self.using_tor == True:
            if FileFlip_Module.check_tor() == True:
                self.e = multiprocessing.Process(target=FileFlip_Module.start_server_tor, args=(port,self.tDirectory.text(),output_file))
                self.e.start()
                print("Started with TOR "+str(self.using_tor))
                self.server_on_button()
            else:
                buttonReply = QMessageBox.question(self, 'Error', "Make sure TOR is running!", QMessageBox.Yes)

    def server_on_button(self):
        server_on = True
        self.bCheckTor.setEnabled(False)
        self.bStart.setEnabled(False)
        self.bStop.setEnabled(True)
        self.tDirectory.setEnabled(False)
        self.tPort.setEnabled(False)
        self.bBrowse.setEnabled(False)
     
    def KillServer(self):
        self.e.terminate()
        self.e = multiprocessing.Process(target=FileFlip_Module.start_server, args=(port, self.tDirectory.text()))
        server_on = False
        self.bCheckTor.setEnabled(True)
        self.bStart.setEnabled(True)
        self.bStop.setEnabled(False)
        self.tDirectory.setEnabled(True)
        self.tPort.setEnabled(True)
        self.bBrowse.setEnabled(True)
        temp_del = open(output_file,"w")
        temp_del.close()

    def KillServer_AndQuit(self):
        print("Terminating")
        self.e.terminate()
        self.e = multiprocessing.Process(target=FileFlip_Module.start_server, args=(port, self.tDirectory.text()))
        server_on = False
        self.bCheckTor.setEnabled(True)
        self.bStart.setEnabled(True)
        self.bStop.setEnabled(False)
        self.tDirectory.setEnabled(True)
        self.tPort.setEnabled(True)
        self.bBrowse.setEnabled(True)
        temp_del = open(output_file,"w")
        temp_del.close()
        exit()

    def FindDirectory(self):
        temp = QtWidgets.QFileDialog.getExistingDirectory()
        self.tDirectory.setText(temp)

    def Output(self, text):
        self.tOutput.appendPlainText(text)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("FileFlip", "FileFlip"))
        self.bStart.setText(_translate("MainWindow", "Start Server"))
        self.bStop.setText(_translate("MainWindow", "Stop Server"))
        self.tDirectory.setText(_translate("MainWindow", "C:\\"))
        self.tDirectory.setPlaceholderText(_translate("MainWindow", "Directory"))
        self.bBrowse.setText(_translate("MainWindow", "Browse"))
        self.tPort.setText(_translate("MainWindow", "8000"))
        self.tPort.setPlaceholderText(_translate("MainWindow", "Port"))


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    finally:
        temp_del = open(ui.output_file,"w")
        temp_del.close()
        ui.e.terminate()