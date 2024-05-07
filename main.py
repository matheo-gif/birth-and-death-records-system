import sys
import PySide6
from PySide6 import QtCore as qtc 
from PySide6 import QtGui as qtg 
from PySide6.QtWidgets import QApplication, QWidget,QPushButton
from sidebar import MySideBar

app = QApplication(sys.argv)


window = MySideBar()


app.exec()