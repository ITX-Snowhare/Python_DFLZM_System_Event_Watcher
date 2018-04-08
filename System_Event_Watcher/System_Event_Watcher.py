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

import time, threading

import data.main
import data.about
from db_conn import *

faliao_now = faliao_clyc = faliao_flyc = faliao_yc_second = 0
shouhuo_now = shouhuo_clyc = shouhuo_shyc = shouhuo_yc_second = 0

class mainshow(QtWidgets.QWidget,data.main.Ui_Form):
    def __init__(self):
        super(mainshow,self).__init__()
        self.setupUi(self)
        self.conn_db_botton.clicked.connect(self.db_manual) #数据连接,网络测试接入

        # self.timer = QTimer(self)  #自动刷新定时(旧的)
        # self.timer.timeout.connect(self.prData)

        # self.checkBox_auto_Flash.stateChanged.connect(self.autoflash) #自动刷新接入
        # self.checkBox_Slient.stateChanged.connect(self.noSoung) #静音接入

    def db_manual(self):
        """
        手动刷新界面(收货发料)
        :return:
        """
        self.conn_db_botton.setDisabled(True)
        db = Db_Contro()
        db.conn('ln')
        self.if_net_lost()
        update = threading.Thread(target=self.db_data_update)
        update.start()

        # update.join()
        self.prData()
        # if
        #     self.conn_db_botton.setDisabled(False)


    def db_data_update(self):
        """
        后台更新数据
        :return:
        """
        db = Db_Contro()
        db.conn('ln')
        shuohuotime,faliaotime,db_stat = db.get_sfimg()
        self.conn_db_botton.setDisabled(False)

    def if_net_lost(self):
        if no_conn == 1:
            QMessageBox.critical(self,"网络连接失败","网络不通或无法连接数据库,程序即将退出")
            sys.exit(1)
        else:
            pass


    def prData(self):
        """更新界面数据"""

        global faliao_now,faliao_clyc,faliao_flyc,faliao_yc_second
        global shouhuo_now,shouhuo_clyc,shouhuo_shyc,shouhuo_yc_second

        self.cpfaliaotime.setText(str(faliao_now))
        self.ln_flyc.setText(str(faliao_flyc))
        self.cpshouhuotime.setText(str(shouhuo_now))
        self.ln_shyc.setText(str(shouhuo_shyc))
        if shouhuo_yc_second >= 600 :
            self.sh_ln_clyc.setText(str(shouhuo_clyc))
            self.sh_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
            #self.label_5.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
        else:
            self.sh_ln_clyc.setText(str(shouhuo_clyc))
            self.sh_ln_clyc.setStyleSheet("background-color: none;color:black")
        if faliao_yc_second >= 600 :
            self.fl_ln_clyc.setText(str(faliao_clyc))
            self.fl_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
        else:
            self.fl_ln_clyc.setText(str(faliao_clyc))
            self.fl_ln_clyc.setStyleSheet("background-color: none;color:black")

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

class About_Window(QWidget,data.about.Ui_Dialog):
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