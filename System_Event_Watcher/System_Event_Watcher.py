# -*- coding: utf-8 -*-

"""

主界面程序
作者:韦俊杰
最后编辑: 2018年04月23日

获取自动收货及厂内发料的运行状态
获取LN“第一个空号”大于900000的预警
获取各生产系统接口的情况（未启用）

"""
import sys
import os
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

import logging
from logging.handlers import TimedRotatingFileHandler

faliao_now = faliao_clyc = faliao_flyc = faliao_yc_second = 0
shouhuo_now = shouhuo_clyc = shouhuo_shyc = shouhuo_yc_second = 0
shouhuotime = faliaotime = db_stat = 0
ln_scn_date = rows = 0
song = 0
autof = 1
begin = 0

LOG_FORMAT = '%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - %(levelname)s - %(message)s'
formatter = logging.Formatter(LOG_FORMAT)

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(os.path.join(os.getcwd(), 'log.txt'))
fh.setLevel(logging.DEBUG)
fh = TimedRotatingFileHandler(filename='log.txt',when='midnight',interval=1,backupCount=7)
#logging.handlers.suffix = "%Y-%m-%d"

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


class mainshow(QtWidgets.QWidget, UI_main.Ui_Form):
    def __init__(self):
        super(mainshow,self).__init__()
        self.setupUi(self)

        #界面风格
        QApplication.setStyle('Fusion')
        self.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint\
                            |Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)

        #监控收货发料界面：
        self.conn_db_botton.clicked.connect(self.db_manual)#开始刷新的按钮功能
        # self.timer = QTimer(self)  #自动刷新定时
        # self.timer.timeout.connect(self.autoprdate)
        self.checkBox_auto_Flash.stateChanged.connect(self.autoflash) #自动刷新开关
        self.checkBox_Slient.stateChanged.connect(self.noSoung) #静音开关

        #LN序号界面代码：
        self.ln_sncb=QStandardItemModel(0,4);
        self.ln_sncb.setHorizontalHeaderLabels(['编号组', '系列', '第一个空号', '系列说明'])
        self.ln_snc.setModel(self.ln_sncb)
        self.ln_snc.horizontalHeader().setStretchLastSection(True)
        self.ln_snc.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ln_scn_db_mu.clicked.connect(self.prLnscn_m)


    def db_manual(self):
        """
        开始刷新界面(收货发料)
        """
        global begin
        self.manual_lock() #按钮变灰
        # update = threading.Thread(target=self.db_data_update,daemon=True)
        # update.start()
        # update.join()
        # if no_conn == 1:
        #     self.db_getimg_fail()
        # release = threading.Thread(target=self.manual_release,args=(5,))
        # release.start()
        if begin == 0:
            # 界面定时更新
            self.timer = QTimer(self)  # 初始化一个定时器
            self.timer.timeout.connect(self.prData)  # 计时结束调用operate()方法
            self.timer.start(5000)  # 设置计时间隔并启动,单位为毫秒
            begin = 1
        else:
            pass

        autoupdate = threading.Thread(target=self.autoprdate, daemon=True) #自动刷新数据的线程
        autoupdate.start()

    # def autoflash(self,state):
    #     """自动刷新"""
    #     if state == Qt.Checked:
    #         self.timer.start(5000)
    #         self.manual_lock()
    #     else:
    #         self.timer.stop()
    #         self.manual_release(0)

    def autoprdate(self):

        global no_conn
        global autof
        #self.db_getimg_fail()
        try:
            while autof:
                db = Db_Contro()
                db.conn('ln')
                global shouhuotime,faliaotime,db_stat
                shouhuotime,faliaotime,db_stat = db.get_sfimg(no_conn)
                no_conn = db_stat
                self.prData()
                # if no_conn == 1:
                #     logger.warning('无法正确获取数据库数据')
                sleep(5)
        except:
            logger.exception("Exception Logged")





    def db_data_update(self):
        """
        后台更新数据
        :return:
        """
        global no_conn
        db = Db_Contro()
        db.conn('ln')
        global shouhuotime,faliaotime,db_stat
        try:
            shouhuotime,faliaotime,db_stat = db.get_sfimg(no_conn)
        except:
            logger.exception("Exception Logged")
        no_conn = db_stat
        #self.prData()


    def manual_lock(self):
        self.conn_db_botton.setDisabled(True)

    def manual_release(self,time):
        sleep(time)
        self.conn_db_botton.setDisabled(False)

    def db_getimg_fail(self):
        global no_conn
        if no_conn == 1: #异常检测

            logger.warning('网络异常，正在重试连接')
        #     do = QMessageBox.warning(self,"网络异常","数据获取失败,是否重新连接?",\
        #                              QMessageBox.Retry,QMessageBox.No)
        #     if do == 524288:
            no_conn = 0
        #         #self.manual_release(0)  #是否需要解锁按钮还要测试
        #     else:
        #         end = QMessageBox.critical(self,"网络异常","无法获取数据,程序即将退出",\
        #                                    QMessageBox.Ok,QMessageBox.No)
        #         if end == 1024:
        #             sys.exit(1)
        #         else:
        #             pass
        else:
            pass

    def prData(self):
        """更新界面数据"""

        global faliao_now,faliao_clyc,faliao_flyc,faliao_yc_second
        global shouhuo_now,shouhuo_clyc,shouhuo_shyc,shouhuo_yc_second
        global shouhuotime,faliaotime,db_stat
        global song,no_conn

        warn_time = 600  # 报警条件，单位是秒

        try:

            time = sf_time_handle()
            faliao_now, faliao_clyc, faliao_flyc, faliao_yc_second\
                = time.faliao_handle(faliaotime,db_stat)
            shouhuo_now, shouhuo_clyc, shouhuo_shyc, shouhuo_yc_second\
                = time.shouhuo_handle(shouhuotime,db_stat)
            #self.db_getimg_fail()

            # save_log = 'faliao_yc_second: ' + str(faliao_yc_second)\
            #            + ',' + 'shouhuo_yc_second: ' + str(shouhuo_yc_second)\
            #            + ',' + 'db_stat: ' + str(db_stat)
            # logger.info(save_log)
        except:
            logger.exception("Exception Logged")

        try:

            if no_conn == 1:
                self.sh_ln_clyc.setText(str('网络异常，请重新刷新！'))
                self.fl_ln_clyc.setText(str('网络异常，请重新刷新！'))
                self.sh_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
                self.fl_ln_clyc.setStyleSheet("background-color: rgb(250, 250, 0);color:red")
                self.waring(1)
                logger.warning('网络异常，无法获取数据库数据')
                #self.manual_release(0)
                self.db_getimg_fail()  # 网络失败重连

            else:

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


            if song == 0 and (shouhuo_yc_second >= warn_time or faliao_yc_second >= warn_time):
                self.waring(0)

            if shouhuo_yc_second >= warn_time:
                logger.warning('收货处理时间超时')

            if faliao_yc_second >= warn_time:
                logger.warning('发料处理时间超时')
            #         song_play = threading.Thread(target=self.waring, daemon=True,args=(warn_time,),name='p_warn')
            #         if song_play.is_alive():
            #             pass
            #         else:
            #             song_play.start()
        except:
            logger.exception("Exception Logged")
            #
    def waring(self,option):
    #     """报警声音"""
        global song,no_conn
        global ps
        if option == 0:
            if song == 0:
                ps = winsound.PlaySound('Feed.wav', \
                        winsound.SND_FILENAME | winsound.SND_ASYNC )
        elif option == 1:
            if song == 0:
                if no_conn == 1:
                    ps = winsound.PlaySound('Feed.wav', \
                                            winsound.SND_FILENAME | winsound.SND_ASYNC)
                else:
                    pass
            else:
                pass
        else:
            pass
    #     wtime = time
    #     global song,shouhuo_yc_second,faliao_yc_second
    #     while song == 0 and (shouhuo_yc_second >= wtime or faliao_yc_second >= wtime):
    #         winsound.PlaySound('Feed.wav', \
    #                        winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_NOWAIT)
    #         sleep(3)

    def noSoung(self,state):
        """静音"""
        global song
        if state == Qt.Checked:
             song = 1
        else:
             song = 0

    def autoflash(self,state):
        """自动刷新"""
        global autof
        if state == Qt.Checked:
            autof = 1
            self.manual_lock()
            self.db_manual()
        else:
            autof = 0
            self.manual_release(0)

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