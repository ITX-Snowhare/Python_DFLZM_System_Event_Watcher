# -*- coding: utf-8 -*-

"""

主界面程序
作者:韦俊杰
最后编辑:

"""
import sys
sys.path.append("../data") #添加资源路径
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import data.main
import data.about


class mainshow(QtWidgets.QWidget,data.main.Main_Form):
    def __init__(self):
        super(mainshow,self).__init__()
        self.setupUi(self)
        self.conn_db_botton.clicked.connect(self.prData) #数据连接,网络测试接入

        # self.timer = QTimer(self)  #自动刷新定时(旧的)
        # self.timer.timeout.connect(self.prData)

        # self.checkBox_auto_Flash.stateChanged.connect(self.autoflash) #自动刷新接入
        # self.checkBox_Slient.stateChanged.connect(self.noSoung) #静音接入


    def prData(self):
        """更新界面数据"""
        self.conn_db_botton.setDisabled(True)
        # self.upData_process = upData()
        # # 启动线程
        # self.upData_process.start()


        # if t >= 600 :
        #     self.sh_ln_clyc.setText(str(cl))
        #     self.sh_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
        #     #self.label_5.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
        # else:
        #     self.sh_ln_clyc.setText(str(cl))
        #     self.sh_ln_clyc.setStyleSheet("background-color: none;color:black")
        # if f >= 600 :
        #     self.fl_ln_clyc.setText(str(fl))
        #     self.fl_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
        # else:
        #     self.fl_ln_clyc.setText(str(fl))
        #     self.fl_ln_clyc.setStyleSheet("background-color: none;color:black")

    #
    # def autoflash(self,state):
    #     """自动刷新"""
    #     if state == QtCore.Qt.Checked:
    #         self.timer.start(10000)
    #     else:
    #         self.timer.stop()
    #
    # def waring(self):
    #     """报警声音文件"""
    #     winsound.PlaySound('Feed.wav', winsound.SND_FILENAME)
    #
    # def noSoung(self,state):
    #     """静音"""
    #     global song
    #     if state == QtCore.Qt.Checked:
    #          song = 1
    #     else:
    #          song = 0
    # def workend(self,ls):
    #     for word in ls:
    #         print(word)
    #     self.pushButton_2.setDisabled(False)

class About_Window(QWidget,data.about.About_Dialog):
    def __init__(self, parent=None):
        super(About_Window, self).__init__(parent)
        self.setupUi(self)
    def handle_click(self):
        if not self.isVisible():
            self.show()

    def handle_close(self):
        self.close()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainW = mainshow()
    MainW.show()
    AboutW = About_Window()
    MainW.about_button.clicked.connect(AboutW.handle_click)
    sys.exit(app.exec_())