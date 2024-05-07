# This Python file uses the following encoding: utf-8
import sys
import PySide6
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6.QtWidgets import QApplication, QWidget,QPushButton,QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    
    login_success = qtc.Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        
        self.ui.pb_Cancel.clicked.connect(self.close)
        self.ui.pb_Login.clicked.connect(self.process_login)
        
    @qtc.Slot()
    def process_login(self):
        if self.ui.lusername.text() == "mathew" and self.ui.lpassword.text()== "password":
            self.login_success.emit()
            self.close()
        else:
            QMessageBox.warning(self, "Warning", "Check Password or Username.")
            
            # self.ui.lblMessages.setText("check password or username")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
