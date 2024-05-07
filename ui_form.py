# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import resources2_rc

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(900, 398)
        Widget.setMinimumSize(QSize(900, 398))
        Widget.setMaximumSize(QSize(900, 398))
        Widget.setSizeIncrement(QSize(900, 398))
        font = QFont()
        font.setPointSize(11)
        Widget.setFont(font)
        icon = QIcon()
        icon.addFile(u"resources/icons/icons/data-management-9858.png", QSize(), QIcon.Normal, QIcon.Off)
        Widget.setWindowIcon(icon)
        Widget.setStyleSheet(u"*{\n"
"background-color: #334155;\n"
"border: 1;\n"
"\n"
"}")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(463, 600))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(-6)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 300))
        self.label.setMaximumSize(QSize(463, 600))
        self.label.setStyleSheet(u"label{\n"
"	background-color: #020617;\n"
"    width: 130; height: 100;\n"
"    fillMode: Image.PreserveAspectFit;\n"
"    source: \"\\resources\\icons\\login.png\"\n"
"}\n"
"background:\"\\resources\\icons\\login.png\" ;")
        self.label.setPixmap(QPixmap(u"resources/icons/login.png"))

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(2, 6, 23);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setWeight(QFont.Medium)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(2, 6, 23);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setIndent(0)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_4)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_2.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.lusername = QLineEdit(self.groupBox)
        self.lusername.setObjectName(u"lusername")
        font4 = QFont()
        font4.setBold(True)
        self.lusername.setFont(font4)
        self.lusername.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(8, 8, 8);")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lusername)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.lpassword = QLineEdit(self.groupBox)
        self.lpassword.setObjectName(u"lpassword")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(False)
        self.lpassword.setFont(font5)
        self.lpassword.setTabletTracking(True)
        self.lpassword.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(4, 4, 4);")
        self.lpassword.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.lpassword.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lpassword)

        self.lblMessages = QLabel(self.groupBox)
        self.lblMessages.setObjectName(u"lblMessages")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setWeight(QFont.Medium)
        self.lblMessages.setFont(font6)
        self.lblMessages.setStyleSheet(u"color: rgb#dc2626;")

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.lblMessages)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.verticalSpacer)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.verticalSpacer_3)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.gridLayout_4 = QGridLayout(self.widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.pb_Cancel = QPushButton(self.widget)
        self.pb_Cancel.setObjectName(u"pb_Cancel")
        self.pb_Cancel.setFont(font2)
        self.pb_Cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_Cancel.setMouseTracking(True)
        self.pb_Cancel.setTabletTracking(True)
        self.pb_Cancel.setStyleSheet(u"\n"
"QPushButton{\n"
"background-color: #dc2626;\n"
"padding:4px;\n"
"padding-left:10px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-right:25px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"resources/icons/icons/icons8-close-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Cancel.setIcon(icon1)
        self.pb_Cancel.setIconSize(QSize(25, 25))
        self.pb_Cancel.setCheckable(True)
        self.pb_Cancel.setAutoExclusive(True)
        self.pb_Cancel.setFlat(True)

        self.gridLayout_4.addWidget(self.pb_Cancel, 1, 1, 1, 1)

        self.pb_Login = QPushButton(self.widget)
        self.pb_Login.setObjectName(u"pb_Login")
        self.pb_Login.setEnabled(True)
        font7 = QFont()
        font7.setPointSize(9)
        font7.setBold(True)
        self.pb_Login.setFont(font7)
        self.pb_Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_Login.setMouseTracking(True)
        self.pb_Login.setTabletTracking(True)
        self.pb_Login.setAutoFillBackground(False)
        self.pb_Login.setStyleSheet(u"QPushButton{\n"
"background-color:#0369a1;\n"
"padding:4px;\n"
"padding-left:10px;\n"
"text-align:left;\n"
"border-radius:3px;\n"
"margin-right:25px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"resources/icons/icons/icons8-login-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Login.setIcon(icon2)
        self.pb_Login.setIconSize(QSize(25, 25))
        self.pb_Login.setCheckable(True)
        self.pb_Login.setChecked(True)
        self.pb_Login.setAutoExclusive(True)
        self.pb_Login.setFlat(True)

        self.gridLayout_4.addWidget(self.pb_Login, 1, 0, 1, 1)


        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.widget)


        self.gridLayout_2.addWidget(self.groupBox, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)


        self.retranslateUi(Widget)

        self.pb_Cancel.setDefault(True)
        self.pb_Login.setDefault(True)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"BAA1", None))
        self.label.setText("")
        self.groupBox.setTitle("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"LOGIN NOW", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"username  :", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"password    : ", None))
        self.lblMessages.setText("")
        self.pb_Cancel.setText(QCoreApplication.translate("Widget", u"CLOSE", None))
        self.pb_Login.setText(QCoreApplication.translate("Widget", u"LOGIN", None))
    # retranslateUi

