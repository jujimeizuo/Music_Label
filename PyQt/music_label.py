# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speech_python_demo'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

from speech_txt import creat_task
import qtawesome as qta
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 310, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Music_label", "Music_label"))
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.pushButton.setText(_translate("MainWindow", "上传"))
        self.pushButton.setStyleSheet( "QPushButton{color:black}"
                                       "QPushButton:hover{color:red}"
                                       "QPushButton{background-color:lightgreen}"
                                       "QPushButton{border:2px}"
                                       "QPushButton{border-radius:10px}"
                                       "QPushButton{padding:2px 4px}"
                                       "QPushButton{font-family:'宋体'}")

        self.pushButton.clicked.connect(self.OpenClick)

    def OpenClick(self) :
        FilePath = self.GetFilePath()
        # print(FilePath)
        FileName = FilePath.__str__().split('/')[-1].split('\'')[0]
        with open("../speech_txt/speech_url_list.txt", "w") as f:
            f.write("https://music-label.fsh.bcebos.com/music/" + FileName)
        print(FileName)
        creat_task.creat()

    def GetFilePath(self):
        FilePath = QtWidgets.QFileDialog.getOpenFileName(filter="音频文件(*.mp3 *.mp4 *.amr *.wav *.m4a *.pcm)")
        return FilePath

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
