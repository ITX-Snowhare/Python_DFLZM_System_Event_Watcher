# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 320)
        Form.setMinimumSize(QtCore.QSize(500, 320))
        Form.setMaximumSize(QtCore.QSize(500, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/confirm_24px_1209036_easyicon.net.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.conn_db_botton = QtWidgets.QPushButton(self.tab_3)
        self.conn_db_botton.setGeometry(QtCore.QRect(400, 10, 61, 21))
        self.conn_db_botton.setObjectName("conn_db_botton")
        self.checkBox_auto_Flash = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_auto_Flash.setGeometry(QtCore.QRect(400, 50, 71, 16))
        self.checkBox_auto_Flash.setTabletTracking(False)
        self.checkBox_auto_Flash.setAcceptDrops(False)
        self.checkBox_auto_Flash.setChecked(True)
        self.checkBox_auto_Flash.setObjectName("checkBox_auto_Flash")
        self.checkBox_Slient = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_Slient.setGeometry(QtCore.QRect(400, 70, 47, 16))
        self.checkBox_Slient.setObjectName("checkBox_Slient")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 381, 171))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.cpshouhuotime = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpshouhuotime.sizePolicy().hasHeightForWidth())
        self.cpshouhuotime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.cpshouhuotime.setFont(font)
        self.cpshouhuotime.setObjectName("cpshouhuotime")
        self.gridLayout.addWidget(self.cpshouhuotime, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.sh_ln_clyc = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sh_ln_clyc.sizePolicy().hasHeightForWidth())
        self.sh_ln_clyc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.sh_ln_clyc.setFont(font)
        self.sh_ln_clyc.setAutoFillBackground(False)
        self.sh_ln_clyc.setObjectName("sh_ln_clyc")
        self.gridLayout.addWidget(self.sh_ln_clyc, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.ln_shyc = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.ln_shyc.sizePolicy().hasHeightForWidth())
        self.ln_shyc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ln_shyc.setFont(font)
        self.ln_shyc.setObjectName("ln_shyc")
        self.gridLayout.addWidget(self.ln_shyc, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_2 = QtWidgets.QFrame(self.layoutWidget1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 0, 0, 1, 1)
        self.cpfaliaotime = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cpfaliaotime.sizePolicy().hasHeightForWidth())
        self.cpfaliaotime.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.cpfaliaotime.setFont(font)
        self.cpfaliaotime.setObjectName("cpfaliaotime")
        self.gridLayout_2.addWidget(self.cpfaliaotime, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 1)
        self.fl_ln_clyc = QtWidgets.QLabel(self.layoutWidget1)
        self.fl_ln_clyc.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fl_ln_clyc.sizePolicy().hasHeightForWidth())
        self.fl_ln_clyc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.fl_ln_clyc.setFont(font)
        self.fl_ln_clyc.setAutoFillBackground(False)
        self.fl_ln_clyc.setObjectName("fl_ln_clyc")
        self.gridLayout_2.addWidget(self.fl_ln_clyc, 1, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 0, 1, 1)
        self.ln_flyc = QtWidgets.QLabel(self.layoutWidget1)
        self.ln_flyc.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ln_flyc.sizePolicy().hasHeightForWidth())
        self.ln_flyc.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ln_flyc.setFont(font)
        self.ln_flyc.setObjectName("ln_flyc")
        self.gridLayout_2.addWidget(self.ln_flyc, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.ln_snc = QtWidgets.QTableView(self.tab_5)
        self.ln_snc.setGeometry(QtCore.QRect(10, 10, 451, 151))
        self.ln_snc.setObjectName("ln_snc")
        self.ln_scn_db_mu = QtWidgets.QPushButton(self.tab_5)
        self.ln_scn_db_mu.setGeometry(QtCore.QRect(10, 170, 61, 21))
        self.ln_scn_db_mu.setObjectName("ln_scn_db_mu")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.CP_LOG = QtWidgets.QTableView(self.tab)
        self.CP_LOG.setGeometry(QtCore.QRect(10, 10, 361, 171))
        self.CP_LOG.setObjectName("CP_LOG")
        self.CP_LOG_FLASH = QtWidgets.QPushButton(self.tab)
        self.CP_LOG_FLASH.setGeometry(QtCore.QRect(380, 20, 81, 23))
        self.CP_LOG_FLASH.setObjectName("CP_LOG_FLASH")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(380, 50, 81, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.about_button = QtWidgets.QPushButton(self.layoutWidget)
        self.about_button.setObjectName("about_button")
        self.horizontalLayout_2.addWidget(self.about_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(Form.close)
        self.about_button.clicked.connect(Form.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "系统事件信息查看器"))
        self.label.setText(_translate("Form", "系统事件信息查看器"))
        self.conn_db_botton.setText(_translate("Form", "开始刷新"))
        self.checkBox_auto_Flash.setText(_translate("Form", "自动刷新"))
        self.checkBox_Slient.setText(_translate("Form", "静音"))
        self.label_6.setText(_translate("Form", "当前收货时间："))
        self.cpshouhuotime.setText(_translate("Form", "待刷新..."))
        self.label_3.setText(_translate("Form", "LN处理延迟："))
        self.sh_ln_clyc.setText(_translate("Form", "待刷新..."))
        self.label_4.setText(_translate("Form", "LN收货延迟："))
        self.ln_shyc.setText(_translate("Form", "待刷新..."))
        self.label_11.setText(_translate("Form", "当前发料时间："))
        self.cpfaliaotime.setText(_translate("Form", "待刷新..."))
        self.label_14.setText(_translate("Form", "LN处理延迟："))
        self.fl_ln_clyc.setText(_translate("Form", "待刷新..."))
        self.label_15.setText(_translate("Form", "LN发料延迟："))
        self.ln_flyc.setText(_translate("Form", "待刷新..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "收发监控"))
        self.ln_scn_db_mu.setText(_translate("Form", "获取数据"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "LN序号"))
        self.CP_LOG_FLASH.setText(_translate("Form", "检查日志"))
        self.label_2.setText(_translate("Form", "该界面提示7天内存在问题的CP接口文件夹名及出现问题的日期。请检查对应文件夹的接口文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "CP日志检查"))
        self.about_button.setText(_translate("Form", "关于"))
        self.pushButton.setText(_translate("Form", "退出"))

