# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import webbrowser
import multiprocessing
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import FileFlip_Module
import clipboard


working_dir = "C:\\"
port = 8000
server_on = False

output_file = str(os.getcwdb(), "utf-8")+"\\hiddenservice.txt"
normal_dir = str(os.getcwdb(), "utf-8")
temp_del = open(output_file, "w")
temp_del.close()


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        # Main UI
        self.site_list = []
        self.using_tor = False
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(572, 310)
        MainWindow.setFixedHeight(94)
        MainWindow.setFixedWidth(264)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tOutput.setGeometry(QtCore.QRect(0, 0, 0, 0))
        # self.tOutput.setGeometry(QtCore.QRect(0, 74, 264, 121))
        # self.tOutput.setReadOnly(True)
        # self.tOutput.setObjectName("tOutput")
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

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tDirectory.textChanged.connect(self.updateWorkingDir)
        self.tPort.textChanged.connect(self.updatePort)
        self.bStart.clicked.connect(self.StartServer)
        self.bStop.clicked.connect(self.KillServer)
        self.bBrowse.clicked.connect(self.FindDirectory)

        self.bCheckTor = QtWidgets.QCheckBox(self.centralwidget)
        self.bCheckTor.setGeometry(2, 55, 100, 15)
        self.bCheckTor.setText("Use Tor?")
        self.bCheckTor.clicked.connect(self.EnableTor)

        self.tAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.tAddress.setGeometry(QtCore.QRect(102, 52, 160, 20))
        self.tAddress.setAccessibleDescription("")
        self.tAddress.setObjectName("tAddress")
        self.tAddress.setPlaceholderText("Onion address")
        self.tAddress.setReadOnly(True)

        self.update_address = QtCore.QTimer()
        self.update_address.setInterval(500)
        self.update_address.timeout.connect(self.func_update_address)
        self.update_address.start()

        self.bStop.setEnabled(False)

        self.bEnableDownloads = QtWidgets.QCheckBox(self.centralwidget)
        self.bEnableDownloads.setGeometry(2, 75, 100, 15)
        self.bEnableDownloads.setText("Download")
        self.bEnableDownloads.clicked.connect(self.EnableDownloads)

        self.bCopyOnion = QtWidgets.QPushButton(self.centralwidget)
        self.bCopyOnion.setGeometry(188, 72, 75, 23)
        self.bCopyOnion.setText("Copy Address")
        self.bCopyOnion.setEnabled(False)
        self.bCopyOnion.clicked.connect(self.copyonion)

        # Download ui
        self.SiteList = QtWidgets.QTreeView(self.centralwidget)
        self.SiteList.setGeometry(QtCore.QRect(270, 0, 301, 310))

        self.siteModel = QtGui.QStandardItemModel()
        self.SiteList.setModel(self.siteModel)

        self.bAddsite = QtWidgets.QPushButton(self.centralwidget)
        self.bAddsite.setGeometry(QtCore.QRect(192, 286, 75, 20))
        self.bAddsite.setObjectName("bAddsite")
        self.bAddsite.setText("Add site")
        self.bAddsite.clicked.connect(self.addDownload)

        self.tSite = QtWidgets.QLineEdit(self.centralwidget)
        self.tSite.setGeometry(QtCore.QRect(2, 286, 186, 20))
        self.tSite.setAccessibleDescription("")
        self.tSite.setObjectName("tSite")
        self.tSite.setPlaceholderText("Site")
        
        self.bRemoveSite = QtWidgets.QPushButton(self.centralwidget)
        self.bRemoveSite.setGeometry(QtCore.QRect(2, 264, 267, 20))
        self.bRemoveSite.setObjectName("bRemoveSite")
        self.bRemoveSite.setText("Remove selected site(s)")
        self.bRemoveSite.clicked.connect(self.removeSites)

   #Main UI
    def copyonion(self):
        clipboard.copy(open(output_file).read())


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
            webbrowser.open("http://127.0.0.1:"+self.tPort.text())
            print("Started without TOR: "+str(self.using_tor))
            self.e = multiprocessing.Process(target=FileFlip_Module.start_server, args=(self.tPort.text(), self.tDirectory.text()))
            self.e.start()
            self.server_on_button()
        if self.using_tor == True:
            if FileFlip_Module.check_tor() == True:
                self.e = multiprocessing.Process(target=FileFlip_Module.start_server_tor, args=(self.tPort.text(), self.tDirectory.text(),output_file))
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
        self.bCopyOnion.setEnabled(True)
     

    def KillServer(self):
        self.e.terminate()
        self.e = multiprocessing.Process(target=FileFlip_Module.start_server, args=(port, self.tDirectory.text()))
        server_on = False
        self.bCopyOnion.setEnabled(False)
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
  
   #Download
    def EnableDownloads(self):
        if self.bEnableDownloads.isChecked()==True:
            #MainWindow.resize(572, 310)
            MainWindow.setFixedHeight(310)
            MainWindow.setFixedWidth(570)
        else:
            #MainWindow.resize(572, 310)
            MainWindow.setFixedHeight(94)
            MainWindow.setFixedWidth(264)


    def addDownload(self):
        if len(self.tSite.text()) >= 1:
            self.site_list.append(self.tSite.text())
            self.siteModel.clear()
            for x in range(len(self.site_list)):
                item = QStandardItem(self.site_list[x])
                item.setCheckable(True)
                self.siteModel.appendRow(item)


    def removeSites(self):
        for x in range(len(self.site_list)):
            temp2 = QModelIndex(x)
            temp = self.siteModel.itemFromIndex(temp2)
            if temp.isChecked == True:
                self.site_list.remove(x)
                
        self.siteModel.clear()
        
        for x in range(len(self.site_list)):
                item = QStandardItem(self.site_list[x])
                item.setCheckable(True)
                self.siteModel.appendRow(item)

   #Misc
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
        temp_del = open(output_file,"w")
        temp_del.close()
        if server_on:
            ui.e.terminate()