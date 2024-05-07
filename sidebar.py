# This Python file uses the following encoding: utf-8
import sys
import PySide6
import pymongo
from PySide6 import QtCore as qtc 
from PySide6 import QtGui as qtg 
from PySide6.QtWidgets import QApplication, QMainWindow,QPushButton,QMessageBox, QTableWidgetItem, QVBoxLayout, QWidget
from widget import Widget
from PySide6.QtCore import Qt
from pymongo import MongoClient
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex,QSize,QDate


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_main import Ui_MainWindow
# from users import UserWindow


class MySideBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        self.widget = Widget()
        # self.users = UserWindow()
        self.widget.login_success.connect(self.show)
        self.widget.show()
        
          # Connect to MongoDB
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['data1']
        self.D1_collection = self.db['D1_DATA']

        # Populate table widget with data from MongoDB
        self.populate_D1_data()
        
        
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['data1']
        self.collection = self.db['B1_DATA']
        
        self.populate_B1_data()
        
        
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['data1']
        self.users_collection = self.db['users']
        
        self.populate_user_data()
        
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['data1']
        self.parent_collection = self.db['parents']
        
        
        self.populate_parents_data()
        


        # Set icon size
        self.set_icon_size()

    def set_icon_size(self):
        # Set icon size for the main window
        self.setIconSize(QSize(5, 24))

        self.ui.icons_widget.setHidden(True)
        

        self.ui.pb_dashboard.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard))
        self.ui.pb_dashboard_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard))
        
        self.ui.pb_view_data.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.Dashboard))

        self.ui.pb_users.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.users))
        self.ui.pb_users_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.users))

        self.ui.pb_Birth.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.births))
        self.ui.pb_birth.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.births))

        self.ui.pb_death.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.death))
        self.ui.pB_death.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.death))

        # self.ui.pb_need.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.HELP))cls
        # self.ui.pb_help.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.HELP))

        # logout widget button
        self.ui.pb_logout.clicked.connect(self.close)
        
        self.ui.pb_saveuser.clicked.connect(self.insert_user)
        # load data
        self.ui.pb_saveuser.clicked.connect(self.populate_user_data)
        
        # d1 data
        self.ui.pb_save_d1.clicked.connect(self.insert_D1_DATA)
        
        self.ui.pb_save_d1.clicked.connect(self.populate_D1_data)
        
        self.ui.pb_save_all.clicked.connect(self.insert_B1_Data)
        
        # parents
        self.ui.pbParents.clicked.connect(self.insert_parents)
        self.ui.pb_edit.clicked.connect(self.edit_user)
    
    def populate_D1_data(self):
        # Clear existing items in the table
        self.ui.D1Table.clear()

        # Fetch data from MongoDB
        data = list(self.D1_collection.find())



        # Set table dimensions
        row_count = self.D1_collection.count_documents({})
        column_count = len(data[0]) if row_count > 0 else 0
        self.ui.D1Table.setRowCount(row_count)
        self.ui.D1Table.setColumnCount(column_count)

        headers = ["id", "name", "ID of dead","Age ","Date of death","date of Admn","gender",
                   "sub-County ","county","residence","occupation","Place of Death","cause","Next of Kin",
                   "Next of kin ID","Nationality","serial no"]  # Replace with your actual column names
        self.ui.D1Table.setColumnCount(len(headers))
        self.ui.D1Table.setHorizontalHeaderLabels(headers)
       
        for row_index, document in enumerate(data):
            for column_index, (key, value) in enumerate(document.items()):
                item = QTableWidgetItem(str(value))
                self.ui.D1Table.setItem(row_index, column_index, item)
                
# --------------------------------------------

    def insert_D1_DATA(self):
        name = self.ui.ldt_name_of_dead.text()
        ID_of_dead = self.ui.ldt_id_of_deceased.text()
        age = self.ui.ldt_age.text()
        date_of_death = self.ui.dateEdit_d1.date().toString("yyyy-MM-dd")
        doa = self.ui.DOA.date().toString("yyyy-MM-dd")
        gender = self.ui.comboBox_gender.currentText()
        subCounty = self.ui.cmb_subcounty.currentText()
        County = self.ui.combo_county.currentText()
        residence  = self.ui.ldt_residence.text()
        occupation  = self.ui.l_occupation.text()
        pod  = self.ui.li_pod.text()
        cause  = self.ui.cause_Editline.text()
        issued_to  = self.ui.l_issued_to.text()
        nok_id = self.ui.nok_id_ldt.text()
        nationality = self.ui.l_nationality.text()
        sno  = self.ui.li_sno.text()
        

        D1_data = {"name": name, "ID_of_dead": ID_of_dead,"age": age,"date_of_death": date_of_death,
                    "doa": doa, "gender": gender,"subCounty": subCounty ,
                    "County": County,"residence": residence,"occupation": occupation,"pod": pod,"cause":cause,
                    "issued_to": issued_to,"nok_id": nok_id,"nationality": nationality,"sno": sno}
        self.D1_collection.insert_one(D1_data)
        
        # Optionally, you can clear the input fields after insertion
        self.ui.ldt_name_of_dead.clear()
        self.ui.ldt_id_of_deceased.clear()
        self.ui.ldt_age.clear()
        self.ui.dateEdit_d1.setDate(QDate.currentDate())
        self.ui.DOA.setDate(QDate.currentDate())
        self.ui.comboBox_gender.setCurrentIndex(0)
        self.ui.cmb_subcounty.setCurrentIndex(0)
        self.ui.combo_county.setCurrentIndex(0)
        self.ui.ldt_residence.clear()
        self.ui.l_occupation.clear()
        self.ui.li_pod.clear()
        self.ui.cause_Editline.clear()
        self.ui.l_issued_to.clear()
        self.ui.nok_id_ldt.clear()
        self.ui.li_sno.clear()
        
        
        self.populate_D1_data()
        self.ui.label_msg.setText("data inserted successfully.")
        print("data inserted successfully.")
        msgBox = QMessageBox()
        msgBox.setText("data inserted successfully.")
        msgBox.exec()
    


#insert and display B1 data 

    def insert_B1_Data(self):
        sno = self.ui.ldt_serial_no.text()
        cfname  = self.ui.chl_firstname.text()
        coname = self.ui.chld_othername.text()
        fathersname  = self.ui.chld_fathersname.text()
        gender = "Male" if self.ui.checkmale.isChecked() else "Female"
        dob = self.ui.DOB.date().toString("yyyy-MM-dd")
        NOB = "Born dead" if self.ui.bornDead.isChecked() else "Born Alive"
        location  = self.ui.liElocation.text()
        district  = self.ui.lieDistrict.text()
        weight  = self.ui.weight.text()
        issuedto  = self.ui.issuedto.text()
        IDNO  = self.ui.IDNO.text()
        nationality_f  = self.ui.l_nationality_f.text()
        TOB = "SINGLE" if self.ui.checkBox.isChecked() else "TWIN"
        

        user_data = {"sno": sno, "cfname": cfname,"coname": coname,"fathersname": fathersname,
                    "dob": dob, "gender": gender,"NOB": NOB,
                    "location": location,"district": district,"weight": weight, "issuedto":issuedto,
                    "IDNO":IDNO,"nationality_f":nationality_f,"TOB":TOB }
        self.collection.insert_one(user_data)
        
        
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['data1']
        self.collection = self.db['B1_DATA']
        
        # Optionally, you can clear the input fields after insertion
        self.ui.ldt_serial_no.clear()
        self.ui.chl_firstname.clear()
        self.ui.chld_othername.clear()
        self.ui.chld_fathersname.clear()
        self.ui.checkmale.setChecked(False)
        self.ui.checkfemale.setChecked(False)
        self.ui.DOB.setDate(QDate.currentDate())
        self.ui.bornDead.setChecked(False)
        self.ui.checkBornalive.setChecked(False)
        self.ui.liElocation.clear()
        self.ui.lieDistrict.clear()
        # self.ui.comboBox_Sex.setCurrentIndex(0)
        # self.ui.DOB.setDate(QDate.currentDate())
        self.ui.weight.clear()
        self.ui.issuedto.clear()
        self.ui.IDNO.clear()
        self.ui.l_nationality_f.clear()
        self.ui.checkBox.setChecked(False)
        self.ui.checkBox_2.setChecked(False)
        
        
        self.populate_B1_data()
        # self.ui.success_label.setText("data inserted successfully.")
        # print("User data inserted successfully.")
        msgBox = QMessageBox()
        msgBox.setText("User data inserted successfully.")
        msgBox.exec()


    def populate_B1_data(self):
    # Clear existing items in the table
        self.ui.B1_data_table.clear()

            # Fetch data from MongoDB
        data = list(self.collection.find())

        # Set table dimensions
        row_count = self.collection.count_documents({})
        column_count = len(data[0]) if row_count > 0 else 0
        self.ui.B1_data_table.setRowCount(row_count)
        self.ui.B1_data_table.setColumnCount(column_count)

        headers = ["id","serial no", "First Name","Second Name", "Sir Name","Date Of Birth","sex","Nature of Birth","Facility",
                    "Sub-county","Weight Of Birth","issued to","Notional ID",
                    "Nationality","Type of Birth"]  # Replace with your actual column names
        self.ui.B1_data_table.setColumnCount(len(headers))
        self.ui.B1_data_table.setHorizontalHeaderLabels(headers)
        
        for row_index, document in enumerate(data):
            for column_index, (key, value) in enumerate(document.items()):
                item = QTableWidgetItem(str(value))
                self.ui.B1_data_table.setItem(row_index, column_index, item)
                
                
                
                
                
                
    #  insert and display user data -----------------------------------------          
    def insert_user(self):
        fname = self.ui.li_firstname.text()
        sname  = self.ui.li_othername.text()
        lname = self.ui.li_sirname.text()
        uname  = self.ui.ldt_username.text()
        gender = self.ui.comboBox_Sex.currentText()
        dob = self.ui.dateEdit_DoB.date().toString("yyyy-MM-dd")
        phone_no  = self.ui.li_phonenumnber.text()
        email  = self.ui.Email.text()
        nid  = self.ui.ldt_userID.text()
        pass1  = self.ui.li_password1.text()
        pass2  = self.ui.li_password2.text()
        

        user_data = {"fname": fname, "sname": sname,"lname": lname,"uname": uname,
                    "dob": dob, "gender": gender,"phone_no": phone_no,
                    "email": email,"nid": nid,"pass1": pass1, "pass2": pass2 }
        self.users_collection.insert_one(user_data)
        
        # Optionally, you can clear the input fields after insertion
        self.ui.li_firstname.clear()
        self.ui.li_othername.clear()
        self.ui.li_sirname.clear()
        self.ui.ldt_username.clear()
        self.ui.Email.clear()
        self.ui.comboBox_Sex.setCurrentIndex(0)
        self.ui.dateEdit_DoB.setDate(QDate.currentDate())
        self.ui.li_phonenumnber.clear()
        self.ui.Email.clear()
        self.ui.ldt_userID.clear()
        self.ui.li_password1.clear()
        self.ui.li_password2.clear()
        
        self.populate_user_data()
        # self.ui.success_label.setText("User data inserted successfully.")
        # print("User data inserted successfully.")
        msgBox = QMessageBox()
        msgBox.setText("User data inserted successfully.")
        msgBox.exec()
    
    
    def populate_user_data(self):
        # Clear existing items in the table
        self.ui.user_table_Widget.clear()

         # Fetch data from MongoDB
        data = list(self.users_collection.find())



        # Set table dimensions
        row_count = self.users_collection.count_documents({})
        column_count = len(data[0]) if row_count > 0 else 0
        self.ui.user_table_Widget.setRowCount(row_count)
        self.ui.user_table_Widget.setColumnCount(column_count)

        headers = ["id", "First Name","Other Name","Last Name", "Username","sex","DOB", "Phone Number","Email","ID NO",]  # Replace with your actual column names
        self.ui.user_table_Widget.setColumnCount(len(headers))
        self.ui.user_table_Widget.setHorizontalHeaderLabels(headers)
       
        for row_index, document in enumerate(data):
            for column_index, (key, value) in enumerate(document.items()):
                item = QTableWidgetItem(str(value))
                self.ui.user_table_Widget.setItem(row_index, column_index, item)
                                
                                
    def edit_user(self):
        fname = self.ui.li_firstname.text()
        sname  = self.ui.li_othername.text()
        lname = self.ui.li_sirname.text()
        uname  = self.ui.ldt_username.text()
        gender = self.ui.comboBox_Sex.currentText()
        dob = self.ui.dateEdit_DoB.date().toString("yyyy-MM-dd")
        phone_no  = self.ui.li_phonenumnber.text()
        email  = self.ui.Email.text()
        nid  = self.ui.ldt_userID.text()
        pass1  = self.ui.li_password1.text()
        pass2  = self.ui.li_password2.text()
        

        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["data1"]
        users_collection = db["users"]

        # Update user document
        result = users_collection.update_one({"fname": fname}, {"$set":{"sname ": sname ,"lname": lname,
                                            "uname ": uname , "gender": gender,
                                            "dob": dob,"phone_no": phone_no,
                                            "email": email,"nid ": nid ,"pass1": pass1,"pass2 ": pass2 }})

        if result.matched_count == 0:
            QMessageBox.warning(self, "Edit", "User not found.")
        else:
            QMessageBox.information(self, "Edit", "User updated successfully.")



# parents

    def insert_parents(self):
        mothersnam = self.ui.mothersname.text()
        idno_mother  = self.ui.idno_mother.text()
        mother_age= self.ui.ldt_mother_age.text()
        occupation  = self.ui.lineEdit.text()
        bornalive = self.ui.ldt_bornalive.text()
        borndead  = self.ui.ldt_borndead.text()
        nationatity  = self.ui.nationatity.text()
        county  = self.ui.occuptation.text()
        location  = self.ui.location.text()
        district = self.ui.district.text()
        edu = self.ui.comboBox.currentText()
        if self.ui.checkBox_6.isChecked():
            STATUS = "Divorced"
        elif self.ui.checkBox_7.isChecked():
            STATUS = "Single"
        elif self.ui.checkBox_5.isChecked():
            STATUS = "Married"
        else:
            STATUS = "Widowed"
        fathername  = self.ui.fathername.text()
        fathernationality = self.ui.fathernationality .text()
        fatherid  = self.ui.fatherid.text()
       

        

        parent_data = {"mothersnam": mothersnam, "idno_mother": idno_mother,"mother_age": mother_age,
                    "occupation": occupation,
                    "bornalive": bornalive, "borndead": borndead,"nationatity": nationatity,
                    "county": county,"location": location,"district": district, "edu": edu, "STATUS ": STATUS, 
                    "fathername ": fathername ,"fathernationality":fathernationality, "fatherid ": fatherid }
        self.parent_collection.insert_one(parent_data)
        
        # Optionally, you can clear the input fields after insertion
        self.ui.mothersname.clear()
        self.ui.idno_mother.clear()
        self.ui.ldt_mother_age.clear()
        self.ui.lineEdit.clear()
        self.ui.ldt_bornalive.clear()
        self.ui.ldt_borndead.clear()
        self.ui.nationatity.clear()
        self.ui.occuptation.clear()
        self.ui.location.clear()
        self.ui.district.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.checkBox_6.setChecked(False)
        self.ui.checkBox_7.setChecked(False)
        self.ui.checkBox_5.setChecked(False)
        self.ui.checkBox_8.setChecked(False)
        self.ui.fathername.clear()
        self.ui.fathernationality.clear() 
        self.ui.fatherid.clear()
        
        
        
        self.populate_parents_data()
        # self.ui.success_label.setText("User data inserted successfully.")
        # print("User data inserted successfully.")
        QMessageBox.information(self, "Insert", "data saved successfully.")

        # msgBox = QMessageBox()
        # msgBox.setText( "data saved successfully.")
        # msgBox.exec()
        
        
    def populate_parents_data(self):
        # Clear existing items in the table
        self.ui.parentsTableWidget.clear()

        # Fetch data from MongoDB
        data = list(self.parent_collection.find())



        # Set table dimensions
        row_count = self.parent_collection.count_documents({})
        column_count = len(data[0]) if row_count > 0 else 0
        self.ui.parentsTableWidget.setRowCount(row_count)
        self.ui.parentsTableWidget.setColumnCount(column_count)

        headers = ["id", "Mothers Name","Mothers Id","Mothers Age", "Occupation","Baby born alive",
                "Babies Born Dead", "nationatity","County","location","sub-county",
                "level of Education","Marital Status","Name of Father","Father's Nationality","Father's ID"]  # Replace with your actual column names
        self.ui.parentsTableWidget.setColumnCount(len(headers))
        self.ui.parentsTableWidget.setHorizontalHeaderLabels(headers)
       
        for row_index, document in enumerate(data):
            for column_index, (key, value) in enumerate(document.items()):
                item = QTableWidgetItem(str(value))
                self.ui.parentsTableWidget.setItem(row_index, column_index, item)
    



    


        

