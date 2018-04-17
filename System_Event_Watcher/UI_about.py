# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_about.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(440, 270)
        Dialog.setMinimumSize(QtCore.QSize(440, 270))
        Dialog.setMaximumSize(QtCore.QSize(440, 270))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 131))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pic/image/about2.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 271, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 401, 41))
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setScaledContents(True)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 51, 51))
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/pic/image/about1.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(90, 210, 171, 51))
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/pic/image/公司LOGO-透明.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(160, 50, 251, 51))
        self.label_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "关于本软件"))
        self.label_2.setText(_translate("Dialog", "ITX-系统事件信息查看器  版本 1.3.9 beta 1"))
        self.label_3.setText(_translate("Dialog", "本软件使用Python 3.6以及PyQt5(GPL)进行开发。                            问题反馈及源码索取：请发送邮件至 weijj@dflzm.com"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label_6.setText(_translate("Dialog", "本软件还处于开发阶段，可能还存在较多的问题。本软件适用于监控收货发料，LN序号，各接口的异常预警。"))

import UI_aboutRcc_rc
