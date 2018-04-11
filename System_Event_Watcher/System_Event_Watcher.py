# -*- coding: utf-8 -*-

"""

主界面程序
作者:韦俊杰
最后编辑:

"""
import sys
import winsound
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
from time import sleep

import UI_main
import UI_about
from db_conn import *
from Part_001_Scan_Auto_Job import sf_time_handle
#from Part_002_Wran_LN_SCN import ln_scn_handle

faliao_now = faliao_clyc = faliao_flyc = faliao_yc_second = 0
shouhuo_now = shouhuo_clyc = shouhuo_shyc = shouhuo_yc_second = 0
shouhuotime = faliaotime = db_stat = 0
ln_scn_date = rows = 0
song = 0

class mainshow(QtWidgets.QWidget, UI_main.Ui_Form):
    def __init__(self):
        super(mainshow,self).__init__()
        self.setupUi(self)

        QApplication.setStyle('Fusion')

        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint\
                            |Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.conn_db_botton.clicked.connect(self.db_manual)#数据连接,网络测试接入
        self.timer = QTimer(self)  #自动刷新定时
        self.timer.timeout.connect(self.autoprdate)
        self.checkBox_auto_Flash.stateChanged.connect(self.autoflash) #自动刷新接入
        self.checkBox_Slient.stateChanged.connect(self.noSoung) #静音接入

        self.ln_sncb=QStandardItemModel(0,4);
        self.ln_sncb.setHorizontalHeaderLabels(['编号组', '系列', '第一个空号', '系列说明'])
        self.ln_snc.setModel(self.ln_sncb)
        self.ln_snc.horizontalHeader().setStretchLastSection(True)
        self.ln_snc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ln_scn_db_mu.clicked.connect(self.prLnscn_m)
        #self.prLnscn()

    def db_manual(self):
        """
        手动刷新界面(收货发料)
        :return:
        """
        self.manual_lock()
        update = threading.Thread(target=self.db_data_update,daemon=True)
        update.start()
        #update.join()
        self.db_getimg_fail()
        release = threading.Thread(target=self.manual_release,args=(5,))
        release.start()

    def autoflash(self,state):
        """自动刷新"""
        if state == Qt.Checked:
            self.timer.start(5000)
            self.manual_lock()
        else:
            self.timer.stop()
            self.manual_release(0)

    def autoprdate(self):

        update = threading.Thread(target=self.db_data_update,daemon=True)
        update.start()
        #update.join()
        self.db_getimg_fail()

    def db_data_update(self):
        """
        后台更新数据
        :return:
        """
        global no_conn
        db = Db_Contro()
        db.conn('ln')
        global shouhuotime,faliaotime,db_stat
        shouhuotime,faliaotime,db_stat = db.get_sfimg(no_conn)
        no_conn = db_stat
        self.prData()


    def manual_lock(self):
        self.conn_db_botton.setDisabled(True)

    def manual_release(self,time):
        sleep(time)
        self.conn_db_botton.setDisabled(False)

    def db_getimg_fail(self):
        global no_conn
        if no_conn == 1: #异常检测
            do = QMessageBox.warning(self,"网络异常","数据获取失败,是否重新连接?",\
                                     QMessageBox.Retry,QMessageBox.No)
            if do == 524288:
                no_conn = 0
                self.db_data_update()
                self.db_getimg_fail()
            else:
                end = QMessageBox.critical(self,"网络异常","无法获取数据,程序即将退出",\
                                           QMessageBox.Ok,QMessageBox.No)
                print(end)
                if end == 1024:
                    sys.exit(1)
                else:
                    pass
        else:
            pass

    def prData(self):
        """更新界面数据"""

        global faliao_now,faliao_clyc,faliao_flyc,faliao_yc_second
        global shouhuo_now,shouhuo_clyc,shouhuo_shyc,shouhuo_yc_second
        global shouhuotime,faliaotime,db_stat
        global song


        time = sf_time_handle()
        faliao_now, faliao_clyc, faliao_flyc, faliao_yc_second\
            = time.faliao_handle(faliaotime,db_stat)
        shouhuo_now, shouhuo_clyc, shouhuo_shyc, shouhuo_yc_second\
            = time.shouhuo_handle(shouhuotime,db_stat)

        warn_time = 600

        self.cpfaliaotime.setText(str(faliao_now))
        self.ln_flyc.setText(str(faliao_flyc))
        self.cpshouhuotime.setText(str(shouhuo_now))
        self.ln_shyc.setText(str(shouhuo_shyc))
        if shouhuo_yc_second >= warn_time :
            self.sh_ln_clyc.setText(str(shouhuo_clyc))
            self.sh_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
        else:
            self.sh_ln_clyc.setText(str(shouhuo_clyc))
            self.sh_ln_clyc.setStyleSheet("background-color: none;color:black")
        if faliao_yc_second >= warn_time :
            self.fl_ln_clyc.setText(str(faliao_clyc))
            self.fl_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
        else:
            self.fl_ln_clyc.setText(str(faliao_clyc))
            self.fl_ln_clyc.setStyleSheet("background-color: none;color:black")

        if shouhuo_yc_second >= warn_time or faliao_yc_second >= warn_time:
            while song == 0:
                self.waring()
                sleep(3)

    def waring(self):
        """报警声音文件"""
        winsound.PlaySound('Feed.wav', \
                           winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_NOWAIT)

    def noSoung(self,state):
        """静音"""
        global song
        if state == Qt.Checked:
             song = 1
        else:
             song = 0

    def prLnscn(self):

        global no_conn
        db = Db_Contro()
        db.conn('ln')
        global ln_scn_date,db_stat,rows
        ln_scn_date,rows,db_stat = db.get_lnscn(no_conn)
        no_conn = db_stat
        #date_handle = ln_scn_handle.get_ln_scn(self,ln_scn_date,rows,db_stat)
        for row in range(rows):
            for column in range(4):
                temp_data = ln_scn_date[row][column]  # 临时记录，不能直接插入表格
                #data = QTableWidgetItem(str(temp_data))  # 转换后可插入表格
                data = QStandardItem(str(temp_data))
                self.ln_sncb.setItem(row, column, data)

    def prLnscn_m(self):

        self.manual_lock_scn()
        update = threading.Thread(target=self.prLnscn,daemon=True)
        update.start()
        #update.join()

        release = threading.Thread(target=self.manual_release_scn,args=(5,))
        release.start()

    def manual_lock_scn(self):
        self.ln_scn_db_mu.setDisabled(True)

    def manual_release_scn(self,time):
        sleep(time)
        self.ln_scn_db_mu.setDisabled(False)

class About_Window(QWidget, UI_about.Ui_Dialog):
    def __init__(self, parent=None):
        super(About_Window, self).__init__(parent)
        self.setupUi(self)
        #QApplication.setStyle('Fusion')
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint|Qt.CustomizeWindowHint)

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