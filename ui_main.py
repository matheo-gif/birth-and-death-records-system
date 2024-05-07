# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowSWyHtl.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1340, 785)
        font = QFont()
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"resources/icons/icons/data-management-9858.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"MainWindow{\n"
"	margin:0px;\n"
"	background-color: #1f2937;\n"
"	padding:2px;\n"
"}")
        MainWindow.setIconSize(QSize(5, 24))
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.icons_widget = QWidget(self.centralwidget)
        self.icons_widget.setObjectName(u"icons_widget")
        self.icons_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(15, 23, 42);\n"
"	border:none;\n"
"\n"
"}\n"
"QPushButton{\n"
"	background-color: #1e293b;\n"
"	border-radius:2px;\n"
"	border-left:#0f766e;\n"
"	padding:4px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: #d4d4d4;\n"
"}")
        self.gridLayout_10 = QGridLayout(self.icons_widget)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(4, 0, 9, 0)
        self.label = QLabel(self.icons_widget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"margin:4px;")
        self.label.setPixmap(QPixmap(u"resources/icons/icons/data-management-9858.png"))

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 50, -1, -1)
        self.pb_dashboard = QPushButton(self.icons_widget)
        self.pb_dashboard.setObjectName(u"pb_dashboard")
        icon1 = QIcon()
        icon1.addFile(u"resources/icons/icons/four-squares-10585.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_dashboard.setIcon(icon1)
        self.pb_dashboard.setIconSize(QSize(30, 30))
        self.pb_dashboard.setCheckable(True)
        self.pb_dashboard.setAutoExclusive(True)
        self.pb_dashboard.setFlat(True)

        self.verticalLayout.addWidget(self.pb_dashboard)

        self.pb_Birth = QPushButton(self.icons_widget)
        self.pb_Birth.setObjectName(u"pb_Birth")
        icon2 = QIcon()
        icon2.addFile(u"resources/icons/icons/mother.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Birth.setIcon(icon2)
        self.pb_Birth.setIconSize(QSize(35, 35))
        self.pb_Birth.setCheckable(True)
        self.pb_Birth.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pb_Birth)

        self.pb_death = QPushButton(self.icons_widget)
        self.pb_death.setObjectName(u"pb_death")
        icon3 = QIcon()
        icon3.addFile(u"resources/icons/icons/heart-beat-3519.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_death.setIcon(icon3)
        self.pb_death.setIconSize(QSize(30, 30))
        self.pb_death.setCheckable(True)
        self.pb_death.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pb_death)

        self.verticalSpacer = QSpacerItem(20, 298, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pb_users = QPushButton(self.icons_widget)
        self.pb_users.setObjectName(u"pb_users")
        icon4 = QIcon()
        icon4.addFile(u"resources/icons/icons/settings-5670.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_users.setIcon(icon4)
        self.pb_users.setIconSize(QSize(30, 30))
        self.pb_users.setCheckable(True)
        self.pb_users.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.pb_users)


        self.gridLayout_10.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.icons_widget, 0, 0, 1, 1)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.verticalLayout_5 = QVBoxLayout(self.main_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.main_widget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"background-color: #4b5563;\n"
"\n"
"padding-left:3px;\n"
"padding-right:9px;\n"
"}\n"
"QPushButton{\n"
"	border:none;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_menu = QPushButton(self.widget)
        self.pb_menu.setObjectName(u"pb_menu")
        self.pb_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"resources/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_menu.setIcon(icon5)
        self.pb_menu.setIconSize(QSize(30, 30))
        self.pb_menu.setCheckable(True)
        self.pb_menu.setAutoExclusive(False)

        self.horizontalLayout_2.addWidget(self.pb_menu)

        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.ldt_search_1 = QLineEdit(self.widget)
        self.ldt_search_1.setObjectName(u"ldt_search_1")
        self.ldt_search_1.setFont(font)
        self.ldt_search_1.setAutoFillBackground(False)
        self.ldt_search_1.setStyleSheet(u"QLineEdit{\n"
"border-color:#020617;\n"
"background-color:#f8fafc;\n"
"border-radius:4px;\n"
"margin-right:0px;\n"
"padding:2px;\n"
"}")
        self.ldt_search_1.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.ldt_search_1)

        self.pb_search = QPushButton(self.widget)
        self.pb_search.setObjectName(u"pb_search")
        self.pb_search.setAutoFillBackground(False)
        self.pb_search.setStyleSheet(u"padding:0px;\n"
"margin-left:0px;")
        icon6 = QIcon()
        icon6.addFile(u"resources/icons/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_search.setIcon(icon6)
        self.pb_search.setIconSize(QSize(20, 20))
        self.pb_search.setCheckable(True)
        self.pb_search.setAutoExclusive(True)
        self.pb_search.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pb_search)

        self.horizontalSpacer_4 = QSpacerItem(70, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.pb_logout = QPushButton(self.widget)
        self.pb_logout.setObjectName(u"pb_logout")
        icon7 = QIcon()
        icon7.addFile(u"resources/icons/icons/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_logout.setIcon(icon7)
        self.pb_logout.setIconSize(QSize(20, 20))
        self.pb_logout.setCheckable(True)
        self.pb_logout.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.pb_logout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setTabletTracking(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(51, 65, 85);")
        self.Dashboard = QWidget()
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setStyleSheet(u"QWidget{\n"
"	background-color:#1e293b;\n"
"	color:white;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.Dashboard)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.Dashboard)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_15 = QWidget(self.frame_3)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_5 = QGridLayout(self.widget_15)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lblTabelMessages = QLabel(self.widget_15)
        self.lblTabelMessages.setObjectName(u"lblTabelMessages")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setItalic(True)
        self.lblTabelMessages.setFont(font2)
        self.lblTabelMessages.setStyleSheet(u"color: rgb(34, 86, 38);")
        self.lblTabelMessages.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lblTabelMessages, 0, 0, 1, 1)

        self.label_10 = QLabel(self.widget_15)
        self.label_10.setObjectName(u"label_10")
        font3 = QFont()
        font3.setFamilies([u"Britannic Bold"])
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(True)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.label_10.setFont(font3)
        self.label_10.setCursor(QCursor(Qt.ForbiddenCursor))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_15, 1, 0, 1, 1)

        self.widget_14 = QWidget(self.frame_3)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_3 = QGridLayout(self.widget_14)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_editB1data = QPushButton(self.widget_14)
        self.btn_editB1data.setObjectName(u"btn_editB1data")
        self.btn_editB1data.setFont(font)
        self.btn_editB1data.setStyleSheet(u"QPushButton{\n"
"background-color: #0f766e;;\n"
"padding:6px;\n"
"padding-right:5px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-right:120px;\n"
"margin-left:120px\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"resources/icons/icons/edit.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_editB1data.setIcon(icon8)
        self.btn_editB1data.setIconSize(QSize(24, 24))
        self.btn_editB1data.setCheckable(True)
        self.btn_editB1data.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_editB1data, 0, 1, 1, 1)

        self.btn_deletB1data = QPushButton(self.widget_14)
        self.btn_deletB1data.setObjectName(u"btn_deletB1data")
        self.btn_deletB1data.setFont(font)
        self.btn_deletB1data.setStyleSheet(u"QPushButton{\n"
"background-color: #7c2d10;\n"
"padding:6px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-right:100px;\n"
"margin-left:120px\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"resources/icons/icons/trash.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deletB1data.setIcon(icon9)
        self.btn_deletB1data.setIconSize(QSize(24, 24))
        self.btn_deletB1data.setCheckable(True)
        self.btn_deletB1data.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_deletB1data, 0, 2, 1, 1)

        self.btn_reloadB1data = QPushButton(self.widget_14)
        self.btn_reloadB1data.setObjectName(u"btn_reloadB1data")
        self.btn_reloadB1data.setFont(font)
        self.btn_reloadB1data.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(22, 78, 99);\n"
"padding:6px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-right:120px;\n"
"margin-left:120px\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"resources/icons/icons/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reloadB1data.setIcon(icon10)
        self.btn_reloadB1data.setIconSize(QSize(24, 24))
        self.btn_reloadB1data.setCheckable(True)
        self.btn_reloadB1data.setFlat(True)

        self.gridLayout_3.addWidget(self.btn_reloadB1data, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_14, 4, 0, 1, 1)

        self.B1_data_table = QTableWidget(self.frame_3)
        if (self.B1_data_table.columnCount() < 1):
            self.B1_data_table.setColumnCount(1)
        self.B1_data_table.setObjectName(u"B1_data_table")
        font4 = QFont()
        font4.setFamilies([u"Myanmar Text"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.B1_data_table.setFont(font4)
        self.B1_data_table.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.B1_data_table.setMouseTracking(True)
        self.B1_data_table.setTabletTracking(True)
        self.B1_data_table.setAutoFillBackground(True)
        self.B1_data_table.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"   color:white;\n"
"	 background-color:#232326;\n"
"    border: 1px solid white ;\n"
"	margin: 0px;\n"
"	text-align: right;\n"
"	font-family: arial;\n"
"	font-size:12px;\n"
"    height: 32px;\n"
"}")
        self.B1_data_table.setFrameShape(QFrame.NoFrame)
        self.B1_data_table.setFrameShadow(QFrame.Plain)
        self.B1_data_table.setLineWidth(0)
        self.B1_data_table.setAlternatingRowColors(False)
        self.B1_data_table.setSortingEnabled(True)
        self.B1_data_table.setColumnCount(1)
        self.B1_data_table.horizontalHeader().setVisible(True)
        self.B1_data_table.horizontalHeader().setCascadingSectionResizes(True)
        self.B1_data_table.horizontalHeader().setStretchLastSection(True)
        self.B1_data_table.verticalHeader().setVisible(True)
        self.B1_data_table.verticalHeader().setCascadingSectionResizes(True)
        self.B1_data_table.verticalHeader().setProperty("showSortIndicator", True)
        self.B1_data_table.verticalHeader().setStretchLastSection(False)

        self.gridLayout_4.addWidget(self.B1_data_table, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.Dashboard)
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.users.setStyleSheet(u"QWidget{\n"
"background-color:#334155;\n"
"color:#f8fafc;\n"
"\n"
"}")
        self.gridLayout_16 = QGridLayout(self.users)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.widget_2 = QWidget(self.users)
        self.widget_2.setObjectName(u"widget_2")
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.widget_2.setFont(font5)
        self.widget_2.setMouseTracking(True)
        self.widget_2.setTabletTracking(True)
        self.widget_2.setStyleSheet(u"background-color: #0f172a;")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, -1, -1)
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 16))
        self.label_6.setSizeIncrement(QSize(0, 16))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        self.label_7.setFont(font6)

        self.verticalLayout_3.addWidget(self.label_7)

        self.li_firstname = QLineEdit(self.widget_2)
        self.li_firstname.setObjectName(u"li_firstname")
        self.li_firstname.setFont(font)
        self.li_firstname.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(6, 6, 6);")
        self.li_firstname.setFrame(False)

        self.verticalLayout_3.addWidget(self.li_firstname)

        self.label_29 = QLabel(self.widget_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font)

        self.verticalLayout_3.addWidget(self.label_29)

        self.li_othername = QLineEdit(self.widget_2)
        self.li_othername.setObjectName(u"li_othername")
        self.li_othername.setFont(font)
        self.li_othername.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(4, 4, 4);")
        self.li_othername.setFrame(False)

        self.verticalLayout_3.addWidget(self.li_othername)

        self.label_30 = QLabel(self.widget_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)

        self.verticalLayout_3.addWidget(self.label_30)

        self.li_sirname = QLineEdit(self.widget_2)
        self.li_sirname.setObjectName(u"li_sirname")
        self.li_sirname.setFont(font)
        self.li_sirname.setStyleSheet(u"color: rgb(2, 2, 2);\n"
"background-color: #f8fafc;")
        self.li_sirname.setFrame(False)

        self.verticalLayout_3.addWidget(self.li_sirname)

        self.label_54 = QLabel(self.widget_2)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.verticalLayout_3.addWidget(self.label_54)

        self.ldt_username = QLineEdit(self.widget_2)
        self.ldt_username.setObjectName(u"ldt_username")
        self.ldt_username.setFont(font)
        self.ldt_username.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(2, 2, 2);")
        self.ldt_username.setFrame(False)

        self.verticalLayout_3.addWidget(self.ldt_username)

        self.label_67 = QLabel(self.widget_2)
        self.label_67.setObjectName(u"label_67")

        self.verticalLayout_3.addWidget(self.label_67)

        self.comboBox_Sex = QComboBox(self.widget_2)
        self.comboBox_Sex.addItem("")
        self.comboBox_Sex.addItem("")
        self.comboBox_Sex.addItem("")
        self.comboBox_Sex.addItem("")
        self.comboBox_Sex.setObjectName(u"comboBox_Sex")
        self.comboBox_Sex.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_Sex.setMouseTracking(True)
        self.comboBox_Sex.setTabletTracking(True)
        self.comboBox_Sex.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(2, 2, 2);")
        self.comboBox_Sex.setEditable(True)
        self.comboBox_Sex.setFrame(False)

        self.verticalLayout_3.addWidget(self.comboBox_Sex)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.dateEdit_DoB = QDateEdit(self.widget_2)
        self.dateEdit_DoB.setObjectName(u"dateEdit_DoB")
        self.dateEdit_DoB.setAutoFillBackground(True)
        self.dateEdit_DoB.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(2, 2, 2);")
        self.dateEdit_DoB.setWrapping(True)
        self.dateEdit_DoB.setFrame(False)
        self.dateEdit_DoB.setAccelerated(True)
        self.dateEdit_DoB.setProperty("showGroupSeparator", True)
        self.dateEdit_DoB.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.dateEdit_DoB)

        self.label_31 = QLabel(self.widget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)

        self.verticalLayout_3.addWidget(self.label_31)

        self.li_phonenumnber = QLineEdit(self.widget_2)
        self.li_phonenumnber.setObjectName(u"li_phonenumnber")
        self.li_phonenumnber.setFont(font)
        self.li_phonenumnber.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(2, 2, 2);")
        self.li_phonenumnber.setFrame(False)

        self.verticalLayout_3.addWidget(self.li_phonenumnber)

        self.label_25 = QLabel(self.widget_2)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_3.addWidget(self.label_25)

        self.Email = QLineEdit(self.widget_2)
        self.Email.setObjectName(u"Email")
        self.Email.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(2, 2, 2);")
        self.Email.setFrame(False)

        self.verticalLayout_3.addWidget(self.Email)

        self.label_55 = QLabel(self.widget_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)

        self.verticalLayout_3.addWidget(self.label_55)

        self.ldt_userID = QLineEdit(self.widget_2)
        self.ldt_userID.setObjectName(u"ldt_userID")
        self.ldt_userID.setFont(font)
        self.ldt_userID.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(2, 2, 2);")
        self.ldt_userID.setFrame(False)

        self.verticalLayout_3.addWidget(self.ldt_userID)

        self.label_32 = QLabel(self.widget_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.verticalLayout_3.addWidget(self.label_32)

        self.li_password1 = QLineEdit(self.widget_2)
        self.li_password1.setObjectName(u"li_password1")
        self.li_password1.setFont(font)
        self.li_password1.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(2, 2, 2);")
        self.li_password1.setFrame(False)
        self.li_password1.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.li_password1)

        self.label_33 = QLabel(self.widget_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)

        self.verticalLayout_3.addWidget(self.label_33)

        self.li_password2 = QLineEdit(self.widget_2)
        self.li_password2.setObjectName(u"li_password2")
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        self.li_password2.setFont(font7)
        self.li_password2.setStyleSheet(u"background-color: #f8fafc;\n"
"color: rgb(4, 4, 4);")
        self.li_password2.setFrame(False)
        self.li_password2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.li_password2)

        self.verticalSpacer_4 = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_saveuser = QPushButton(self.widget_2)
        self.pb_saveuser.setObjectName(u"pb_saveuser")
        self.pb_saveuser.setFont(font)
        self.pb_saveuser.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_saveuser.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(22, 78, 99);\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u"resources/icons/icons/data-storage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_saveuser.setIcon(icon11)
        self.pb_saveuser.setIconSize(QSize(20, 20))
        self.pb_saveuser.setCheckable(True)
        self.pb_saveuser.setAutoExclusive(True)
        self.pb_saveuser.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pb_saveuser)

        self.push_canceluser = QPushButton(self.widget_2)
        self.push_canceluser.setObjectName(u"push_canceluser")
        self.push_canceluser.setFont(font5)
        self.push_canceluser.setCursor(QCursor(Qt.PointingHandCursor))
        self.push_canceluser.setStyleSheet(u"QPushButton{\n"
"background-color: #7c2d12;\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u"resources/icons/icons/close-x-10324.png", QSize(), QIcon.Normal, QIcon.Off)
        self.push_canceluser.setIcon(icon12)
        self.push_canceluser.setIconSize(QSize(20, 20))
        self.push_canceluser.setCheckable(True)
        self.push_canceluser.setAutoExclusive(True)
        self.push_canceluser.setFlat(True)

        self.horizontalLayout_4.addWidget(self.push_canceluser)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout_16.addWidget(self.widget_2, 0, 1, 3, 1)

        self.widget_13 = QWidget(self.users)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setStyleSheet(u"background-color: rgb(15, 23, 42);")
        self.gridLayout_17 = QGridLayout(self.widget_13)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, -1)
        self.user_table_Widget = QTableWidget(self.widget_13)
        self.user_table_Widget.setObjectName(u"user_table_Widget")
        self.user_table_Widget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.user_table_Widget.setMouseTracking(True)
        self.user_table_Widget.setTabletTracking(True)
        self.user_table_Widget.setAutoFillBackground(True)
        self.user_table_Widget.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"   color:white;\n"
"	 background-color:#1f2937;\n"
"    border: 1px solid white ;\n"
"	margin: 0px;\n"
"	text-align: right;\n"
"	font-family: arial;\n"
"	font-size:12px;\n"
"    height: 32px;\n"
"}\n"
"\n"
"")
        self.user_table_Widget.setFrameShape(QFrame.NoFrame)
        self.user_table_Widget.setFrameShadow(QFrame.Plain)
        self.user_table_Widget.setAutoScroll(True)
        self.user_table_Widget.setAutoScrollMargin(9)
        self.user_table_Widget.setShowGrid(False)
        self.user_table_Widget.setGridStyle(Qt.SolidLine)
        self.user_table_Widget.setSortingEnabled(True)
        self.user_table_Widget.horizontalHeader().setProperty("showSortIndicator", True)
        self.user_table_Widget.horizontalHeader().setStretchLastSection(True)
        self.user_table_Widget.verticalHeader().setHighlightSections(False)
        self.user_table_Widget.verticalHeader().setProperty("showSortIndicator", True)
        self.user_table_Widget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_17.addWidget(self.user_table_Widget, 2, 0, 1, 1)

        self.widget_18 = QWidget(self.widget_13)
        self.widget_18.setObjectName(u"widget_18")
        self.gridLayout_19 = QGridLayout(self.widget_18)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_8 = QLabel(self.widget_18)
        self.label_8.setObjectName(u"label_8")
        font8 = QFont()
        font8.setPointSize(15)
        font8.setBold(True)
        self.label_8.setFont(font8)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_8, 1, 0, 1, 1)

        self.success_label = QLabel(self.widget_18)
        self.success_label.setObjectName(u"success_label")
        self.success_label.setStyleSheet(u"color: rgb(5, 57, 55);\n"
"font: 700 12pt \"Segoe UI\";")

        self.gridLayout_19.addWidget(self.success_label, 2, 0, 1, 1)


        self.gridLayout_17.addWidget(self.widget_18, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.widget_13)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_15 = QGridLayout(self.widget_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.pb_edit = QPushButton(self.widget_3)
        self.pb_edit.setObjectName(u"pb_edit")
        self.pb_edit.setFont(font7)
        self.pb_edit.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_edit.setMouseTracking(True)
        self.pb_edit.setTabletTracking(True)
        self.pb_edit.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: #0f766e;\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u"resources/icons/icons/content-9813.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_edit.setIcon(icon13)
        self.pb_edit.setIconSize(QSize(25, 25))
        self.pb_edit.setCheckable(True)
        self.pb_edit.setAutoExclusive(True)
        self.pb_edit.setFlat(False)

        self.gridLayout_15.addWidget(self.pb_edit, 0, 0, 1, 1)

        self.pbtn_download = QPushButton(self.widget_3)
        self.pbtn_download.setObjectName(u"pbtn_download")
        self.pbtn_download.setFont(font)
        self.pbtn_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_download.setMouseTracking(True)
        self.pbtn_download.setTabletTracking(True)
        self.pbtn_download.setLayoutDirection(Qt.LeftToRight)
        self.pbtn_download.setAutoFillBackground(False)
        self.pbtn_download.setStyleSheet(u"QPushButton{\n"
"background-color:#082f49;\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u"resources/icons/icons/download-pdf.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pbtn_download.setIcon(icon14)
        self.pbtn_download.setIconSize(QSize(25, 25))
        self.pbtn_download.setCheckable(True)
        self.pbtn_download.setChecked(True)
        self.pbtn_download.setAutoRepeat(True)
        self.pbtn_download.setAutoExclusive(True)
        self.pbtn_download.setFlat(True)

        self.gridLayout_15.addWidget(self.pbtn_download, 0, 2, 1, 1)

        self.pbtn_del = QPushButton(self.widget_3)
        self.pbtn_del.setObjectName(u"pbtn_del")
        self.pbtn_del.setFont(font)
        self.pbtn_del.setCursor(QCursor(Qt.PointingHandCursor))
        self.pbtn_del.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: rgb(127, 29, 29);\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"\n"
"}")
        self.pbtn_del.setIcon(icon9)
        self.pbtn_del.setIconSize(QSize(25, 25))
        self.pbtn_del.setCheckable(True)
        self.pbtn_del.setAutoExclusive(True)
        self.pbtn_del.setFlat(True)

        self.gridLayout_15.addWidget(self.pbtn_del, 0, 1, 1, 1)


        self.gridLayout_17.addWidget(self.widget_3, 3, 0, 1, 1)


        self.gridLayout_16.addWidget(self.widget_13, 0, 0, 3, 1)

        self.stackedWidget.addWidget(self.users)
        self.SETTINGS = QWidget()
        self.SETTINGS.setObjectName(u"SETTINGS")
        self.stackedWidget.addWidget(self.SETTINGS)
        self.death = QWidget()
        self.death.setObjectName(u"death")
        self.death.setStyleSheet(u"color: rgb(255, 251, 235);")
        self.gridLayout_32 = QGridLayout(self.death)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.widget_4 = QWidget(self.death)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_31 = QGridLayout(self.widget_4)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(15, 23, 42);")
        self.gridLayout_23 = QGridLayout(self.widget_9)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_9)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setStyleSheet(u"background-color: rgb(17, 24, 39);")
        self.gridLayout_11 = QGridLayout(self.widget_17)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_39 = QLabel(self.widget_17)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font5)
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setWordWrap(True)

        self.gridLayout_11.addWidget(self.label_39, 0, 2, 1, 3)

        self.widget_16 = QWidget(self.widget_17)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_14 = QGridLayout(self.widget_16)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.btn_editD1data = QPushButton(self.widget_16)
        self.btn_editD1data.setObjectName(u"btn_editD1data")
        self.btn_editD1data.setFont(font)
        self.btn_editD1data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editD1data.setMouseTracking(True)
        self.btn_editD1data.setTabletTracking(True)
        self.btn_editD1data.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(22, 78, 99);\n"
"padding:4px;\n"
"text-align:centre;\n"
"border-radius:3px;\n"
"\n"
"}")
        self.btn_editD1data.setIcon(icon8)
        self.btn_editD1data.setIconSize(QSize(25, 25))
        self.btn_editD1data.setCheckable(True)
        self.btn_editD1data.setAutoExclusive(True)

        self.gridLayout_14.addWidget(self.btn_editD1data, 1, 0, 1, 1)

        self.btn_deleteD1data = QPushButton(self.widget_16)
        self.btn_deleteD1data.setObjectName(u"btn_deleteD1data")
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setItalic(False)
        self.btn_deleteD1data.setFont(font9)
        self.btn_deleteD1data.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deleteD1data.setMouseTracking(True)
        self.btn_deleteD1data.setTabletTracking(True)
        self.btn_deleteD1data.setStyleSheet(u"QPushButton{\n"
"background-color:#9a3412;\n"
"font: 700 9pt \"Segoe UI\";\n"
"padding:4px;\n"
"text-align:centre;\n"
"border-radius:3px;\n"
"\n"
"}")
        self.btn_deleteD1data.setIcon(icon9)
        self.btn_deleteD1data.setIconSize(QSize(25, 25))
        self.btn_deleteD1data.setCheckable(True)
        self.btn_deleteD1data.setAutoExclusive(True)

        self.gridLayout_14.addWidget(self.btn_deleteD1data, 3, 0, 1, 1)

        self.D1Table = QTableWidget(self.widget_16)
        self.D1Table.setObjectName(u"D1Table")
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(False)
        self.D1Table.setFont(font10)
        self.D1Table.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.D1Table.setMouseTracking(True)
        self.D1Table.setTabletTracking(True)
        self.D1Table.setAcceptDrops(True)
        self.D1Table.setAutoFillBackground(True)
        self.D1Table.setStyleSheet(u"QHeaderView::section {\n"
"   color:white;\n"
"	 background-color:#232326;\n"
"    border: 1px solid white ;\n"
"	margin: 0px;\n"
"	text-align: right;\n"
"	font-family: arial;\n"
"	font-size:12px;\n"
"    height: 32px;\n"
"\n"
"	\n"
"\n"
"}\n"
"")
        self.D1Table.setFrameShape(QFrame.NoFrame)
        self.D1Table.setFrameShadow(QFrame.Plain)
        self.D1Table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.D1Table.setAutoScroll(True)
        self.D1Table.setAutoScrollMargin(16)
        self.D1Table.setDragEnabled(True)
        self.D1Table.setDragDropOverwriteMode(False)
        self.D1Table.setAlternatingRowColors(False)
        self.D1Table.setShowGrid(False)
        self.D1Table.setGridStyle(Qt.NoPen)
        self.D1Table.setSortingEnabled(True)
        self.D1Table.horizontalHeader().setVisible(True)
        self.D1Table.horizontalHeader().setCascadingSectionResizes(True)
        self.D1Table.horizontalHeader().setMinimumSectionSize(80)
        self.D1Table.horizontalHeader().setDefaultSectionSize(150)
        self.D1Table.horizontalHeader().setStretchLastSection(True)
        self.D1Table.verticalHeader().setVisible(True)
        self.D1Table.verticalHeader().setCascadingSectionResizes(True)
        self.D1Table.verticalHeader().setHighlightSections(True)
        self.D1Table.verticalHeader().setProperty("showSortIndicator", True)
        self.D1Table.verticalHeader().setStretchLastSection(False)

        self.gridLayout_14.addWidget(self.D1Table, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.widget_16, 3, 3, 1, 1)


        self.gridLayout_23.addWidget(self.widget_17, 0, 1, 1, 1)

        self.widget_12 = QWidget(self.widget_9)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setAutoFillBackground(False)
        self.widget_12.setStyleSheet(u"background-color: #1e293b;\n"
"padding-left:1px;\n"
"padding-right:0px;\n"
"margin-right:1px;")
        self.gridLayout_12 = QGridLayout(self.widget_12)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_12.setContentsMargins(6, 9, 9, 9)
        self.pb_save_d1 = QPushButton(self.widget_12)
        self.pb_save_d1.setObjectName(u"pb_save_d1")
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setItalic(False)
        self.pb_save_d1.setFont(font11)
        self.pb_save_d1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_save_d1.setStyleSheet(u"QPushButton{\n"
"background-color:#0369a1;\n"
"padding:3px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-left:50px\n"
"}")
        self.pb_save_d1.setIcon(icon11)
        self.pb_save_d1.setIconSize(QSize(24, 24))
        self.pb_save_d1.setCheckable(True)
        self.pb_save_d1.setAutoExclusive(True)
        self.pb_save_d1.setFlat(True)

        self.gridLayout_12.addWidget(self.pb_save_d1, 26, 0, 1, 1)

        self.DOA = QDateTimeEdit(self.widget_12)
        self.DOA.setObjectName(u"DOA")
        font12 = QFont()
        font12.setPointSize(11)
        self.DOA.setFont(font12)
        self.DOA.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")
        self.DOA.setWrapping(False)
        self.DOA.setFrame(False)
        self.DOA.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.DOA.setMinimumTime(QTime(0, 0, 0))
        self.DOA.setCalendarPopup(True)
        self.DOA.setTimeSpec(Qt.LocalTime)

        self.gridLayout_12.addWidget(self.DOA, 5, 2, 1, 2)

        self.ldt_residence = QLineEdit(self.widget_12)
        self.ldt_residence.setObjectName(u"ldt_residence")
        font13 = QFont()
        font13.setPointSize(10)
        self.ldt_residence.setFont(font13)
        self.ldt_residence.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.ldt_residence, 10, 0, 1, 4)

        self.label_51 = QLabel(self.widget_12)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.gridLayout_12.addWidget(self.label_51, 6, 0, 1, 1)

        self.l_issued_to = QLineEdit(self.widget_12)
        self.l_issued_to.setObjectName(u"l_issued_to")
        self.l_issued_to.setFont(font13)
        self.l_issued_to.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.l_issued_to, 14, 0, 1, 4)

        self.dateEdit_d1 = QDateEdit(self.widget_12)
        self.dateEdit_d1.setObjectName(u"dateEdit_d1")
        self.dateEdit_d1.setFont(font12)
        self.dateEdit_d1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(26, 26, 26);\n"
"padding:4px")
        self.dateEdit_d1.setFrame(False)
        self.dateEdit_d1.setCalendarPopup(True)
        self.dateEdit_d1.setTimeSpec(Qt.UTC)

        self.gridLayout_12.addWidget(self.dateEdit_d1, 4, 0, 1, 4)

        self.ldt_name_of_dead = QLineEdit(self.widget_12)
        self.ldt_name_of_dead.setObjectName(u"ldt_name_of_dead")
        self.ldt_name_of_dead.setFont(font12)
        self.ldt_name_of_dead.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.ldt_name_of_dead, 0, 0, 1, 4)

        self.li_sno = QLineEdit(self.widget_12)
        self.li_sno.setObjectName(u"li_sno")
        self.li_sno.setFont(font13)
        self.li_sno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.li_sno, 19, 0, 1, 4)

        self.label_52 = QLabel(self.widget_12)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_12.addWidget(self.label_52, 6, 2, 1, 1)

        self.additional_field = QPushButton(self.widget_12)
        self.additional_field.setObjectName(u"additional_field")
        self.additional_field.setCursor(QCursor(Qt.PointingHandCursor))
        self.additional_field.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color:#083344;\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-left:50px;\n"
"margin-right:50px\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u"resources/icons/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.additional_field.setIcon(icon15)
        self.additional_field.setIconSize(QSize(24, 24))
        self.additional_field.setCheckable(True)

        self.gridLayout_12.addWidget(self.additional_field, 26, 2, 1, 1)

        self.cmb_subcounty = QComboBox(self.widget_12)
        self.cmb_subcounty.addItem("")
        self.cmb_subcounty.addItem("")
        self.cmb_subcounty.setObjectName(u"cmb_subcounty")
        self.cmb_subcounty.setFont(font7)
        self.cmb_subcounty.setCursor(QCursor(Qt.PointingHandCursor))
        self.cmb_subcounty.setMouseTracking(True)
        self.cmb_subcounty.setTabletTracking(True)
        self.cmb_subcounty.setStyleSheet(u"background-color: #94a3b8;\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")
        self.cmb_subcounty.setEditable(True)
        self.cmb_subcounty.setFrame(False)

        self.gridLayout_12.addWidget(self.cmb_subcounty, 7, 2, 1, 2)

        self.li_pod = QLineEdit(self.widget_12)
        self.li_pod.setObjectName(u"li_pod")
        self.li_pod.setFont(font13)
        self.li_pod.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px\n"
"")

        self.gridLayout_12.addWidget(self.li_pod, 12, 0, 1, 4)

        self.label_34 = QLabel(self.widget_12)
        self.label_34.setObjectName(u"label_34")
        font14 = QFont()
        font14.setBold(False)
        self.label_34.setFont(font14)

        self.gridLayout_12.addWidget(self.label_34, 3, 0, 1, 1)

        self.ldt_id_of_deceased = QLineEdit(self.widget_12)
        self.ldt_id_of_deceased.setObjectName(u"ldt_id_of_deceased")
        self.ldt_id_of_deceased.setFont(font13)
        self.ldt_id_of_deceased.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.ldt_id_of_deceased, 1, 0, 1, 4)

        self.label_9 = QLabel(self.widget_12)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_12.addWidget(self.label_9, 8, 2, 1, 1)

        self.l_occupation = QLineEdit(self.widget_12)
        self.l_occupation.setObjectName(u"l_occupation")
        self.l_occupation.setFont(font13)
        self.l_occupation.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.l_occupation, 11, 0, 1, 4)

        self.cause_Editline = QLineEdit(self.widget_12)
        self.cause_Editline.setObjectName(u"cause_Editline")
        self.cause_Editline.setFont(font13)
        self.cause_Editline.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.cause_Editline, 13, 0, 1, 4)

        self.comboBox_gender = QComboBox(self.widget_12)
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.addItem("")
        self.comboBox_gender.setObjectName(u"comboBox_gender")
        font15 = QFont()
        font15.setFamilies([u"Segoe UI Emoji"])
        font15.setPointSize(10)
        self.comboBox_gender.setFont(font15)
        self.comboBox_gender.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_gender.setMouseTracking(True)
        self.comboBox_gender.setAutoFillBackground(False)
        self.comboBox_gender.setStyleSheet(u"background-color: #94a3b8;\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")
        self.comboBox_gender.setFrame(False)

        self.gridLayout_12.addWidget(self.comboBox_gender, 7, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_12.addItem(self.verticalSpacer_5, 20, 0, 1, 3)

        self.label_38 = QLabel(self.widget_12)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.gridLayout_12.addWidget(self.label_38, 5, 0, 1, 1)

        self.nok_id_ldt = QLineEdit(self.widget_12)
        self.nok_id_ldt.setObjectName(u"nok_id_ldt")
        self.nok_id_ldt.setFont(font13)
        self.nok_id_ldt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.nok_id_ldt, 15, 0, 1, 4)

        self.label_35 = QLabel(self.widget_12)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_12.addWidget(self.label_35, 9, 0, 1, 1)

        self.ldt_age = QLineEdit(self.widget_12)
        self.ldt_age.setObjectName(u"ldt_age")
        self.ldt_age.setFont(font12)
        self.ldt_age.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.ldt_age, 2, 0, 1, 4)

        self.combo_county = QComboBox(self.widget_12)
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.addItem("")
        self.combo_county.setObjectName(u"combo_county")
        self.combo_county.setFont(font)
        self.combo_county.setCursor(QCursor(Qt.PointingHandCursor))
        self.combo_county.setMouseTracking(True)
        self.combo_county.setTabletTracking(True)
        self.combo_county.setAutoFillBackground(False)
        self.combo_county.setStyleSheet(u"background-color:#94a3b8;\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")
        self.combo_county.setFrame(False)

        self.gridLayout_12.addWidget(self.combo_county, 9, 2, 1, 2)

        self.label_msg = QLabel(self.widget_12)
        self.label_msg.setObjectName(u"label_msg")
        self.label_msg.setStyleSheet(u"color: rgb(0, 170, 0);")

        self.gridLayout_12.addWidget(self.label_msg, 27, 0, 1, 2)

        self.l_nationality = QLineEdit(self.widget_12)
        self.l_nationality.setObjectName(u"l_nationality")
        self.l_nationality.setFont(font13)
        self.l_nationality.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(30, 30, 30);\n"
"padding:4px")

        self.gridLayout_12.addWidget(self.l_nationality, 16, 0, 1, 4)


        self.gridLayout_23.addWidget(self.widget_12, 0, 0, 1, 1)


        self.gridLayout_31.addWidget(self.widget_9, 0, 0, 2, 1)


        self.gridLayout_32.addWidget(self.widget_4, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.death)
        self.births = QWidget()
        self.births.setObjectName(u"births")
        self.gridLayout_8 = QGridLayout(self.births)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget_7 = QWidget(self.births)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"QWidget{\n"
"background-color:#334155;\n"
"color:#f8fafc;\n"
"}")
        self.gridLayout_9 = QGridLayout(self.widget_7)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.widget_8 = QWidget(self.widget_7)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"QWidget{\n"
"background-color: rgb(3, 7, 18);\n"
"width:80px;\n"
"margin-right:0px;\n"
"border-radius:4px;\n"
"}\n"
"QLineEdit{\n"
"	background-color:#f0fdfa;\n"
"	border-radius:3px;\n"
"	padding:3px;\n"
"	color:dark\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.widget_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(10, 2, 1, -1)
        self.checkBornalive = QCheckBox(self.widget_8)
        self.checkBornalive.setObjectName(u"checkBornalive")
        self.checkBornalive.setFont(font)
        self.checkBornalive.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.checkBornalive, 15, 1, 1, 1)

        self.label_64 = QLabel(self.widget_8)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_6.addWidget(self.label_64, 18, 0, 1, 1)

        self.ldt_serial_no = QLineEdit(self.widget_8)
        self.ldt_serial_no.setObjectName(u"ldt_serial_no")
        self.ldt_serial_no.setFont(font)

        self.gridLayout_6.addWidget(self.ldt_serial_no, 2, 0, 1, 4)

        self.chl_firstname = QLineEdit(self.widget_8)
        self.chl_firstname.setObjectName(u"chl_firstname")
        self.chl_firstname.setFont(font)
        self.chl_firstname.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.chl_firstname, 5, 0, 1, 4)

        self.label_56 = QLabel(self.widget_8)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)

        self.gridLayout_6.addWidget(self.label_56, 1, 0, 1, 1)

        self.pb_save_all = QPushButton(self.widget_8)
        self.pb_save_all.setObjectName(u"pb_save_all")
        self.pb_save_all.setFont(font)
        self.pb_save_all.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_save_all.setLayoutDirection(Qt.LeftToRight)
        self.pb_save_all.setAutoFillBackground(False)
        self.pb_save_all.setStyleSheet(u"QPushButton{\n"
"background-color:#0369a1;\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"}")
        self.pb_save_all.setIcon(icon11)
        self.pb_save_all.setIconSize(QSize(20, 20))
        self.pb_save_all.setCheckable(True)
        self.pb_save_all.setAutoExclusive(True)
        self.pb_save_all.setFlat(True)

        self.gridLayout_6.addWidget(self.pb_save_all, 32, 0, 1, 1)

        self.label_41 = QLabel(self.widget_8)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_6.addWidget(self.label_41, 11, 0, 1, 1)

        self.checkBox = QCheckBox(self.widget_8)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font)
        self.checkBox.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.checkBox, 31, 0, 1, 1)

        self.weight = QLineEdit(self.widget_8)
        self.weight.setObjectName(u"weight")
        self.weight.setFont(font)
        self.weight.setStyleSheet(u"color: rgb(31, 41, 55);")

        self.gridLayout_6.addWidget(self.weight, 23, 0, 1, 4)

        self.checkBox_2 = QCheckBox(self.widget_8)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font)
        self.checkBox_2.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.checkBox_2, 31, 1, 1, 1)

        self.label_42 = QLabel(self.widget_8)
        self.label_42.setObjectName(u"label_42")
        font16 = QFont()
        font16.setBold(True)
        font16.setKerning(False)
        self.label_42.setFont(font16)

        self.gridLayout_6.addWidget(self.label_42, 14, 0, 1, 3)

        self.IDNO = QLineEdit(self.widget_8)
        self.IDNO.setObjectName(u"IDNO")
        self.IDNO.setFont(font)
        self.IDNO.setStyleSheet(u"color: rgb(31, 41, 55);")

        self.gridLayout_6.addWidget(self.IDNO, 25, 0, 1, 4)

        self.checkfemale = QCheckBox(self.widget_8)
        self.checkfemale.setObjectName(u"checkfemale")
        self.checkfemale.setFont(font)
        self.checkfemale.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.checkfemale, 11, 2, 1, 3)

        self.chld_othername = QLineEdit(self.widget_8)
        self.chld_othername.setObjectName(u"chld_othername")
        self.chld_othername.setFont(font)
        self.chld_othername.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.chld_othername, 7, 0, 1, 4)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_6.addWidget(self.label_5, 4, 0, 1, 2)

        self.pb_view_data = QPushButton(self.widget_8)
        self.pb_view_data.setObjectName(u"pb_view_data")
        self.pb_view_data.setFont(font)
        self.pb_view_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_view_data.setAutoFillBackground(False)
        self.pb_view_data.setStyleSheet(u"QPushButton{\n"
"background-color: #3f3f46;\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u"resources/icons/icons/budget-pie-chart-and-yellow-dollar-coin-18866.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_view_data.setIcon(icon16)
        self.pb_view_data.setIconSize(QSize(20, 20))
        self.pb_view_data.setCheckable(True)
        self.pb_view_data.setAutoExclusive(True)
        self.pb_view_data.setFlat(True)

        self.gridLayout_6.addWidget(self.pb_view_data, 32, 1, 1, 1)

        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_6.addWidget(self.label_12, 8, 0, 1, 2)

        self.pb_clearfileds = QPushButton(self.widget_8)
        self.pb_clearfileds.setObjectName(u"pb_clearfileds")
        self.pb_clearfileds.setFont(font)
        self.pb_clearfileds.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_clearfileds.setAutoFillBackground(False)
        self.pb_clearfileds.setStyleSheet(u"QPushButton{\n"
"background-color: #e5e5e5;\n"
"padding:6px;\n"
"color:black;\n"
"border-radius:3px;\n"
"text-align:left;\n"
"\n"
"}")
        self.pb_clearfileds.setCheckable(True)
        self.pb_clearfileds.setAutoExclusive(True)
        self.pb_clearfileds.setFlat(True)

        self.gridLayout_6.addWidget(self.pb_clearfileds, 32, 3, 1, 1)

        self.l_nationality_f = QLineEdit(self.widget_8)
        self.l_nationality_f.setObjectName(u"l_nationality_f")
        self.l_nationality_f.setFont(font)
        self.l_nationality_f.setStyleSheet(u"color: rgb(31, 41, 55);")
        self.l_nationality_f.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.l_nationality_f, 28, 0, 1, 4)

        self.liElocation = QLineEdit(self.widget_8)
        self.liElocation.setObjectName(u"liElocation")
        self.liElocation.setFont(font)
        self.liElocation.setStyleSheet(u"color: rgb(31, 41, 55);")

        self.gridLayout_6.addWidget(self.liElocation, 19, 0, 1, 4)

        self.label_53 = QLabel(self.widget_8)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font)

        self.gridLayout_6.addWidget(self.label_53, 30, 0, 1, 2)

        self.label_40 = QLabel(self.widget_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)

        self.gridLayout_6.addWidget(self.label_40, 12, 0, 1, 2)

        self.chld_fathersname = QLineEdit(self.widget_8)
        self.chld_fathersname.setObjectName(u"chld_fathersname")
        self.chld_fathersname.setFont(font)
        self.chld_fathersname.setClearButtonEnabled(True)

        self.gridLayout_6.addWidget(self.chld_fathersname, 10, 0, 1, 4)

        self.DOB = QDateEdit(self.widget_8)
        self.DOB.setObjectName(u"DOB")
        self.DOB.setFont(font)
        self.DOB.setStyleSheet(u"background-color:#f0fdfa;\n"
"	border-radius:3px;\n"
"	padding:4px;\n"
"color: rgb(62, 62, 62);")
        self.DOB.setInputMethodHints(Qt.ImhDate|Qt.ImhPreferNumbers|Qt.ImhTime)
        self.DOB.setCalendarPopup(True)

        self.gridLayout_6.addWidget(self.DOB, 13, 0, 1, 4)

        self.issuedto = QLineEdit(self.widget_8)
        self.issuedto.setObjectName(u"issuedto")
        self.issuedto.setFont(font)
        self.issuedto.setStyleSheet(u"color: rgb(31, 41, 55);")

        self.gridLayout_6.addWidget(self.issuedto, 24, 0, 1, 4)

        self.checkmale = QCheckBox(self.widget_8)
        self.checkmale.setObjectName(u"checkmale")
        self.checkmale.setFont(font)
        self.checkmale.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkmale.setAutoExclusive(True)

        self.gridLayout_6.addWidget(self.checkmale, 11, 1, 1, 1)

        self.bornDead = QCheckBox(self.widget_8)
        self.bornDead.setObjectName(u"bornDead")
        self.bornDead.setFont(font)
        self.bornDead.setAutoExclusive(True)
        self.bornDead.setTristate(False)

        self.gridLayout_6.addWidget(self.bornDead, 15, 0, 1, 1)

        self.lieDistrict = QLineEdit(self.widget_8)
        self.lieDistrict.setObjectName(u"lieDistrict")
        self.lieDistrict.setFont(font)
        self.lieDistrict.setStyleSheet(u"color: rgb(31, 41, 55);")

        self.gridLayout_6.addWidget(self.lieDistrict, 21, 0, 1, 4)

        self.label_11 = QLabel(self.widget_8)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_6.addWidget(self.label_11, 6, 0, 1, 2)


        self.gridLayout_9.addWidget(self.widget_8, 1, 0, 1, 1)

        self.label_27 = QLabel(self.widget_7)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_27, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"QWidget{background-color: rgb(3, 7, 18);\n"
"border-radius:3px;\n"
"}\n"
"QLineEdit{\n"
"	background-color:#f0fdfa;\n"
"	border-radius:3px;\n"
"	padding:3px\n"
"}")
        self.gridLayout_7 = QGridLayout(self.widget_11)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(2, 2, 2, -1)
        self.fatherid = QLineEdit(self.widget_11)
        self.fatherid.setObjectName(u"fatherid")
        self.fatherid.setFont(font14)
        self.fatherid.setStyleSheet(u"color: #1f2937")
        self.fatherid.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.fatherid, 22, 1, 1, 1)

        self.fathername = QLineEdit(self.widget_11)
        self.fathername.setObjectName(u"fathername")
        self.fathername.setFont(font14)
        self.fathername.setStyleSheet(u"color: #1f2937")

        self.gridLayout_7.addWidget(self.fathername, 18, 1, 1, 1)

        self.label_43 = QLabel(self.widget_11)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)

        self.gridLayout_7.addWidget(self.label_43, 14, 1, 1, 1)

        self.district = QLineEdit(self.widget_11)
        self.district.setObjectName(u"district")
        self.district.setFont(font)
        self.district.setStyleSheet(u"color: rgb(31, 41, 55);")
        self.district.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.district, 12, 1, 1, 1)

        self.label_17 = QLabel(self.widget_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout_7.addWidget(self.label_17, 7, 1, 1, 1)

        self.label_22 = QLabel(self.widget_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font7)
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_22, 16, 1, 1, 1)

        self.occuptation = QLineEdit(self.widget_11)
        self.occuptation.setObjectName(u"occuptation")
        self.occuptation.setFont(font)
        self.occuptation.setStyleSheet(u"color: #1f2937")
        self.occuptation.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.occuptation, 10, 1, 1, 1)

        self.label_24 = QLabel(self.widget_11)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.gridLayout_7.addWidget(self.label_24, 21, 1, 1, 1)

        self.pbParents = QPushButton(self.widget_11)
        self.pbParents.setObjectName(u"pbParents")
        self.pbParents.setFont(font)
        self.pbParents.setStyleSheet(u"QPushButton{\n"
"background-color:#0369a1;\n"
"padding:3px;\n"
"text-align:center;\n"
"border-radius:3px;\n"
"}")
        self.pbParents.setIcon(icon11)
        self.pbParents.setIconSize(QSize(18, 18))
        self.pbParents.setCheckable(True)

        self.gridLayout_7.addWidget(self.pbParents, 23, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.ldt_bornalive = QLineEdit(self.widget_11)
        self.ldt_bornalive.setObjectName(u"ldt_bornalive")
        self.ldt_bornalive.setFont(font)
        self.ldt_bornalive.setStyleSheet(u"color: rgb(31, 41, 55);")
        self.ldt_bornalive.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.ldt_bornalive)

        self.ldt_borndead = QLineEdit(self.widget_11)
        self.ldt_borndead.setObjectName(u"ldt_borndead")
        self.ldt_borndead.setFont(font)
        self.ldt_borndead.setStyleSheet(u"color: #1f2937")
        self.ldt_borndead.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.ldt_borndead)


        self.gridLayout_7.addLayout(self.horizontalLayout_16, 8, 1, 1, 1)

        self.nationatity = QLineEdit(self.widget_11)
        self.nationatity.setObjectName(u"nationatity")
        self.nationatity.setFont(font)
        self.nationatity.setStyleSheet(u"color: #1f2937")
        self.nationatity.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.nationatity, 9, 1, 1, 1)

        self.location = QLineEdit(self.widget_11)
        self.location.setObjectName(u"location")
        self.location.setFont(font)
        self.location.setStyleSheet(u"color: rgb(31, 41, 55);")
        self.location.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.location, 11, 1, 1, 1)

        self.idno_mother = QLineEdit(self.widget_11)
        self.idno_mother.setObjectName(u"idno_mother")
        self.idno_mother.setFont(font)
        self.idno_mother.setStyleSheet(u"color: #1f2937")
        self.idno_mother.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.idno_mother, 2, 1, 1, 1)

        self.mothersname = QLineEdit(self.widget_11)
        self.mothersname.setObjectName(u"mothersname")
        self.mothersname.setFont(font)
        self.mothersname.setStyleSheet(u"color: #1f2937")
        self.mothersname.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.mothersname, 1, 1, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_45 = QLabel(self.widget_11)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_45)

        self.comboBox = QComboBox(self.widget_11)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(30, 30, 30);")
        self.comboBox.setEditable(True)
        self.comboBox.setFrame(False)

        self.horizontalLayout_18.addWidget(self.comboBox)


        self.gridLayout_7.addLayout(self.horizontalLayout_18, 13, 1, 1, 1)

        self.label_36 = QLabel(self.widget_11)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_7.addWidget(self.label_36, 0, 1, 1, 1)

        self.label_23 = QLabel(self.widget_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_7.addWidget(self.label_23, 19, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.checkBox_6 = QCheckBox(self.widget_11)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setFont(font)
        self.checkBox_6.setAutoExclusive(True)
        self.checkBox_6.setTristate(True)

        self.horizontalLayout_15.addWidget(self.checkBox_6)

        self.checkBox_7 = QCheckBox(self.widget_11)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setFont(font)
        self.checkBox_7.setAutoExclusive(True)

        self.horizontalLayout_15.addWidget(self.checkBox_7)

        self.checkBox_5 = QCheckBox(self.widget_11)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setFont(font)
        self.checkBox_5.setAutoExclusive(True)
        self.checkBox_5.setTristate(True)

        self.horizontalLayout_15.addWidget(self.checkBox_5)

        self.checkBox_8 = QCheckBox(self.widget_11)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setFont(font)
        self.checkBox_8.setAutoExclusive(True)
        self.checkBox_8.setTristate(True)

        self.horizontalLayout_15.addWidget(self.checkBox_8)


        self.gridLayout_7.addLayout(self.horizontalLayout_15, 15, 1, 1, 1)

        self.pbCancel = QPushButton(self.widget_11)
        self.pbCancel.setObjectName(u"pbCancel")
        self.pbCancel.setFont(font)
        self.pbCancel.setStyleSheet(u"QPushButton{\n"
"background-color:#ef4444;\n"
"padding:4px;\n"
"text-align:center;\n"
"border-radius:3px;\n"
"}")

        self.gridLayout_7.addWidget(self.pbCancel, 24, 1, 1, 1)

        self.lineEdit = QLineEdit(self.widget_11)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: #1f2937")

        self.gridLayout_7.addWidget(self.lineEdit, 5, 1, 1, 1)

        self.fathernationality = QLineEdit(self.widget_11)
        self.fathernationality.setObjectName(u"fathernationality")
        self.fathernationality.setStyleSheet(u"color: #1f2937")

        self.gridLayout_7.addWidget(self.fathernationality, 20, 1, 1, 1)

        self.ldt_mother_age = QLineEdit(self.widget_11)
        self.ldt_mother_age.setObjectName(u"ldt_mother_age")
        self.ldt_mother_age.setFont(font)
        self.ldt_mother_age.setStyleSheet(u"color: #1f2937")
        self.ldt_mother_age.setClearButtonEnabled(True)

        self.gridLayout_7.addWidget(self.ldt_mother_age, 4, 1, 1, 1)

        self.label_26 = QLabel(self.widget_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.gridLayout_7.addWidget(self.label_26, 17, 1, 1, 1)


        self.gridLayout_9.addWidget(self.widget_11, 1, 3, 1, 1)

        self.widget_5 = QWidget(self.widget_7)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(15, 23, 42);")
        self.gridLayout_13 = QGridLayout(self.widget_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.pushButton = QPushButton(self.widget_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color:#854d0e;\n"
"padding:4px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-left:30px\n"
"\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u"resources/icons/icons/icons8-login-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon17)
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)
        self.pushButton.setFlat(True)

        self.gridLayout_13.addWidget(self.pushButton, 0, 6, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 0, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.parentsTableWidget = QTableWidget(self.widget_5)
        self.parentsTableWidget.setObjectName(u"parentsTableWidget")
        self.parentsTableWidget.setStyleSheet(u"QHeaderView::section {\n"
"   color:white;\n"
"	 background-color:#232326;\n"
"    border: 1px solid white ;\n"
"	margin: 0px;\n"
"	text-align: right;\n"
"	font-family: arial;\n"
"	font-size:12px;\n"
"    height: 32px;\n"
"}")

        self.gridLayout_13.addWidget(self.parentsTableWidget, 1, 0, 1, 7)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.label_18 = QLabel(self.widget_5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_13.addWidget(self.label_18, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.widget_5, 1, 1, 1, 2)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_9.addWidget(self.label_13, 0, 1, 1, 2)


        self.gridLayout_8.addWidget(self.widget_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.births)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_widget, 0, 3, 1, 1)

        self.sidebar_widget = QWidget(self.centralwidget)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        self.sidebar_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(15, 23, 42);\n"
"	color:white;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	margin:2px;\n"
"	width: 90px;\n"
"	padding:4px;\n"
"	border-radius:2px;\n"
"	border-left:#0f766e;\n"
"	\n"
"}\n"
"QPushButton:checked{\n"
"	background-color:#1e293b;\n"
"	color: #f7fee7;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.sidebar_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 4, 9, -1)
        self.label_2 = QLabel(self.sidebar_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"resources/icons/icons/data-management-9858.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.sidebar_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.pb_dashboard_2 = QPushButton(self.sidebar_widget)
        self.pb_dashboard_2.setObjectName(u"pb_dashboard_2")
        self.pb_dashboard_2.setFont(font)
        self.pb_dashboard_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_dashboard_2.setIcon(icon1)
        self.pb_dashboard_2.setCheckable(True)
        self.pb_dashboard_2.setAutoExclusive(True)
        self.pb_dashboard_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.pb_dashboard_2)

        self.pb_birth = QPushButton(self.sidebar_widget)
        self.pb_birth.setObjectName(u"pb_birth")
        self.pb_birth.setFont(font)
        self.pb_birth.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u"resources/icons/icons/maternity.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_birth.setIcon(icon18)
        self.pb_birth.setIconSize(QSize(30, 30))
        self.pb_birth.setCheckable(True)
        self.pb_birth.setAutoExclusive(True)
        self.pb_birth.setFlat(True)

        self.verticalLayout_2.addWidget(self.pb_birth)

        self.pB_death = QPushButton(self.sidebar_widget)
        self.pB_death.setObjectName(u"pB_death")
        self.pB_death.setFont(font)
        self.pB_death.setCursor(QCursor(Qt.PointingHandCursor))
        self.pB_death.setIcon(icon3)
        self.pB_death.setIconSize(QSize(25, 25))
        self.pB_death.setCheckable(True)
        self.pB_death.setAutoExclusive(True)
        self.pB_death.setFlat(True)

        self.verticalLayout_2.addWidget(self.pB_death)

        self.verticalSpacer_2 = QSpacerItem(20, 308, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pb_users_2 = QPushButton(self.sidebar_widget)
        self.pb_users_2.setObjectName(u"pb_users_2")
        self.pb_users_2.setFont(font)
        self.pb_users_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u"resources/icons/icons/SETTINGS.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_users_2.setIcon(icon19)
        self.pb_users_2.setIconSize(QSize(25, 25))
        self.pb_users_2.setCheckable(True)
        self.pb_users_2.setAutoExclusive(True)
        self.pb_users_2.setFlat(True)

        self.verticalLayout_2.addWidget(self.pb_users_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.sidebar_widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pb_menu.toggled.connect(self.icons_widget.setHidden)
        self.pb_menu.toggled.connect(self.sidebar_widget.setVisible)
        self.pb_dashboard_2.toggled.connect(self.pb_dashboard.setChecked)
        self.pb_users_2.toggled.connect(self.pb_users.setChecked)
        self.pb_birth.toggled.connect(self.pb_Birth.setChecked)
        self.pB_death.toggled.connect(self.pb_death.setChecked)
        self.pb_death.toggled.connect(self.pB_death.setChecked)
        self.pb_Birth.toggled.connect(self.pb_birth.setChecked)
        self.pb_users.toggled.connect(self.pb_users_2.setChecked)
        self.pb_dashboard.toggled.connect(self.pb_dashboard_2.setChecked)
        self.pushButton.toggled.connect(self.widget_11.setVisible)
        self.pb_menu.toggled.connect(self.sidebar_widget.setVisible)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BAA-1", None))
        self.label.setText("")
        self.pb_dashboard.setText("")
        self.pb_Birth.setText("")
        self.pb_death.setText("")
        self.pb_users.setText("")
        self.pb_menu.setText("")
        self.ldt_search_1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search here", None))
        self.pb_search.setText("")
        self.pb_logout.setText("")
        self.lblTabelMessages.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"B1 DATA", None))
        self.btn_editB1data.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.btn_deletB1data.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.btn_reloadB1data.setText(QCoreApplication.translate("MainWindow", u"RELOAD", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ADD NEW USER", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"first name", None))
        self.li_firstname.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"other name", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"sirname", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"GENDER", None))
        self.comboBox_Sex.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.comboBox_Sex.setItemText(1, QCoreApplication.translate("MainWindow", u"MALE", None))
        self.comboBox_Sex.setItemText(2, QCoreApplication.translate("MainWindow", u"FEMALE", None))
        self.comboBox_Sex.setItemText(3, QCoreApplication.translate("MainWindow", u"OTHERS", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"phone number", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Email.setInputMask("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"ID NO:", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"password", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"confirm password", None))
        self.pb_saveuser.setText(QCoreApplication.translate("MainWindow", u"SAVE DATA", None))
        self.push_canceluser.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"USERS TABLE DATA", None))
        self.success_label.setText("")
        self.pb_edit.setText(QCoreApplication.translate("MainWindow", u"Edit user", None))
        self.pbtn_download.setText(QCoreApplication.translate("MainWindow", u"download", None))
        self.pbtn_del.setText(QCoreApplication.translate("MainWindow", u"delete user", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"DATA VIEW", None))
        self.btn_editD1data.setText(QCoreApplication.translate("MainWindow", u"EDIT DATA", None))
        self.btn_deleteD1data.setText(QCoreApplication.translate("MainWindow", u"REMOVE DATA", None))
        self.pb_save_d1.setText(QCoreApplication.translate("MainWindow", u"SAVE DATA", None))
        self.DOA.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd/MM/yyyy", None))
        self.ldt_residence.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RESIDENCE", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"SEX", None))
        self.l_issued_to.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Permit issued To/ Next of Kin", None))
        self.ldt_name_of_dead.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Name of Deceased", None))
        self.li_sno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"serial number", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SUB-COUNTY</p></body></html>", None))
        self.additional_field.setText(QCoreApplication.translate("MainWindow", u"MORE FIELDS", None))
        self.cmb_subcounty.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.cmb_subcounty.setItemText(1, QCoreApplication.translate("MainWindow", u"BUTERE", None))

        self.li_pod.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Place of death", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Date of Death", None))
        self.ldt_id_of_deceased.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID number of the Deceased:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"COUNTY OF RESIDENCE", None))
        self.l_occupation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"OCCUPATION", None))
        self.cause_Editline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cause of Death", None))
        self.comboBox_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.comboBox_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"MALE", None))
        self.comboBox_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"FEMALE", None))
        self.comboBox_gender.setItemText(3, QCoreApplication.translate("MainWindow", u"OTHERS", None))

        self.label_38.setText(QCoreApplication.translate("MainWindow", u"DOA", None))
        self.nok_id_ldt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id of the Next of Kin", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"RESIDENCE", None))
        self.ldt_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.combo_county.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.combo_county.setItemText(1, QCoreApplication.translate("MainWindow", u"MOMBASA", None))
        self.combo_county.setItemText(2, QCoreApplication.translate("MainWindow", u"KILIFI", None))
        self.combo_county.setItemText(3, QCoreApplication.translate("MainWindow", u"Kisumu", None))
        self.combo_county.setItemText(4, QCoreApplication.translate("MainWindow", u"Nakuru", None))
        self.combo_county.setItemText(5, QCoreApplication.translate("MainWindow", u"Wajir", None))
        self.combo_county.setItemText(6, QCoreApplication.translate("MainWindow", u"TURKANA", None))
        self.combo_county.setItemText(7, QCoreApplication.translate("MainWindow", u"Mandera", None))
        self.combo_county.setItemText(8, QCoreApplication.translate("MainWindow", u"Marsabit", None))
        self.combo_county.setItemText(9, QCoreApplication.translate("MainWindow", u"Isiolo", None))
        self.combo_county.setItemText(10, QCoreApplication.translate("MainWindow", u"Meru", None))
        self.combo_county.setItemText(11, QCoreApplication.translate("MainWindow", u"Tharaka-Nithi", None))
        self.combo_county.setItemText(12, QCoreApplication.translate("MainWindow", u"Embu", None))
        self.combo_county.setItemText(13, QCoreApplication.translate("MainWindow", u"Kitui", None))
        self.combo_county.setItemText(14, QCoreApplication.translate("MainWindow", u"Machakos", None))
        self.combo_county.setItemText(15, QCoreApplication.translate("MainWindow", u"Makueni", None))
        self.combo_county.setItemText(16, QCoreApplication.translate("MainWindow", u"Nyandarua", None))
        self.combo_county.setItemText(17, QCoreApplication.translate("MainWindow", u"Nyeri", None))
        self.combo_county.setItemText(18, QCoreApplication.translate("MainWindow", u"Kirinyaga", None))
        self.combo_county.setItemText(19, QCoreApplication.translate("MainWindow", u"Murang\u2019a", None))
        self.combo_county.setItemText(20, QCoreApplication.translate("MainWindow", u"Kiambu", None))
        self.combo_county.setItemText(21, QCoreApplication.translate("MainWindow", u"West Pokot", None))
        self.combo_county.setItemText(22, QCoreApplication.translate("MainWindow", u"Samburu", None))
        self.combo_county.setItemText(23, QCoreApplication.translate("MainWindow", u"Trans-Nzoia", None))
        self.combo_county.setItemText(24, QCoreApplication.translate("MainWindow", u"Uasin Gishu", None))
        self.combo_county.setItemText(25, QCoreApplication.translate("MainWindow", u"Elgeyo-Marakwet", None))
        self.combo_county.setItemText(26, QCoreApplication.translate("MainWindow", u"Nandi", None))
        self.combo_county.setItemText(27, QCoreApplication.translate("MainWindow", u"Baringo", None))
        self.combo_county.setItemText(28, QCoreApplication.translate("MainWindow", u"Laikipia", None))
        self.combo_county.setItemText(29, QCoreApplication.translate("MainWindow", u"Narok", None))
        self.combo_county.setItemText(30, QCoreApplication.translate("MainWindow", u"Kajiado", None))
        self.combo_county.setItemText(31, QCoreApplication.translate("MainWindow", u"Kericho", None))
        self.combo_county.setItemText(32, QCoreApplication.translate("MainWindow", u"Bomet", None))
        self.combo_county.setItemText(33, QCoreApplication.translate("MainWindow", u"Kakamega", None))
        self.combo_county.setItemText(34, QCoreApplication.translate("MainWindow", u"Vihiga", None))
        self.combo_county.setItemText(35, QCoreApplication.translate("MainWindow", u"Bungoma", None))
        self.combo_county.setItemText(36, QCoreApplication.translate("MainWindow", u"Busia", None))
        self.combo_county.setItemText(37, QCoreApplication.translate("MainWindow", u"Siaya", None))
        self.combo_county.setItemText(38, QCoreApplication.translate("MainWindow", u"Homa Bay", None))
        self.combo_county.setItemText(39, QCoreApplication.translate("MainWindow", u"Migori", None))
        self.combo_county.setItemText(40, QCoreApplication.translate("MainWindow", u"Kisii", None))
        self.combo_county.setItemText(41, QCoreApplication.translate("MainWindow", u"Nyamira", None))
        self.combo_county.setItemText(42, QCoreApplication.translate("MainWindow", u"Kwale", None))
        self.combo_county.setItemText(43, QCoreApplication.translate("MainWindow", u"Kilifi", None))
        self.combo_county.setItemText(44, QCoreApplication.translate("MainWindow", u"Tana River", None))
        self.combo_county.setItemText(45, QCoreApplication.translate("MainWindow", u"Lamu", None))
        self.combo_county.setItemText(46, QCoreApplication.translate("MainWindow", u"Taita\u2013Taveta", None))
        self.combo_county.setItemText(47, QCoreApplication.translate("MainWindow", u"Garissa", None))

        self.label_msg.setText("")
        self.l_nationality.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.checkBornalive.setText(QCoreApplication.translate("MainWindow", u"Born Alive", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"HEALTH FACILITY", None))
        self.ldt_serial_no.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Serial No.", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"serial number", None))
        self.pb_save_all.setText(QCoreApplication.translate("MainWindow", u"SAVE ALL", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"SEX", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"SINGLE", None))
        self.weight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"WEIGHT OF BIRTH", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"TWIN", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"NATURE OF BIRTH", None))
        self.IDNO.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID NO.", None))
        self.checkfemale.setText(QCoreApplication.translate("MainWindow", u"FEMALE", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.pb_view_data.setText(QCoreApplication.translate("MainWindow", u"VIEW DATA", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Farther's Name", None))
        self.pb_clearfileds.setText(QCoreApplication.translate("MainWindow", u" CLEAR FIELDS", None))
        self.l_nationality_f.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nationality", None))
        self.liElocation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Sub-location/healt instatution", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"TYPE OF BIRTH", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"DATE OF BIRTH", None))
        self.issuedto.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOTIFICATION ISSUED TO:", None))
        self.checkmale.setText(QCoreApplication.translate("MainWindow", u"MALE", None))
        self.bornDead.setText(QCoreApplication.translate("MainWindow", u"Born Dead", None))
        self.lieDistrict.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DISTRICT/SUB-COUNTY", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Other Name", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"NAME OF THE CHILD", None))
        self.fatherid.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FATHER'S ID NO:", None))
        self.fathername.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NAMES OF THE FATHER", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"MARITAL STATUS", None))
        self.district.setPlaceholderText(QCoreApplication.translate("MainWindow", u"sub-county", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"previous Birth to mother", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"FATHER", None))
        self.occuptation.setPlaceholderText(QCoreApplication.translate("MainWindow", u"county of residence", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"FATHER'S ID NO:", None))
        self.pbParents.setText(QCoreApplication.translate("MainWindow", u"save ", None))
        self.ldt_bornalive.setPlaceholderText(QCoreApplication.translate("MainWindow", u"number born alive", None))
        self.ldt_borndead.setPlaceholderText(QCoreApplication.translate("MainWindow", u"No. born dead", None))
        self.nationatity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"nationality", None))
        self.location.setPlaceholderText(QCoreApplication.translate("MainWindow", u"sub-location/Estate/Town", None))
        self.idno_mother.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID NO./Passport/Alien Card Number", None))
        self.mothersname.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Mother's Names", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"level of eductation", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"primary", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"secondary", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"college/tivet", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"universty", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"junior level", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"senior level", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"phd", None))

        self.label_36.setText(QCoreApplication.translate("MainWindow", u"PARENT INFORMATION", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"FATHER'S NATIONATY", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Divorced ", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Single", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"married", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"Widowed", None))
        self.pbCancel.setText(QCoreApplication.translate("MainWindow", u"cancel", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"accupation", None))
        self.fathernationality.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FATHER'S NATIONATY", None))
        self.ldt_mother_age.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter age", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"NAMES OF THE FATHER", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"ADD PARENTS DATA", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"PARENTS INFORMATION", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"PARENTS AND CHILD DATA", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"BAA-1", None))
        self.pb_dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dasboard", None))
        self.pb_birth.setText(QCoreApplication.translate("MainWindow", u"B1", None))
        self.pB_death.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.pb_users_2.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
    # retranslateUi

