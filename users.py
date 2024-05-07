# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
# from PySide6.QtCore import Qt
# from pymongo import MongoClient
# from ui_main import Ui_MainWindow 


# class UserWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         # Connect to MongoDB
#         self.client = MongoClient('mongodb://localhost:27017/')
#         self.db = self.client['data1']
#         self.collection = self.db['D1_DATA']

#         # Populate table widget with data from MongoDB
#         self.populate_table()

      

#     def populate_table(self):
#         # Clear existing items in the table
#         self.ui.D1Table.clear()

#          # Fetch data from MongoDB
#         data = list(self.collection.find())



#         # Set table dimensions
#         row_count = self.collection.count_documents({})
#         column_count = len(data[0]) if row_count > 0 else 0
#         self.ui.D1Table.setRowCount(row_count)s
#         self.ui.D1Table.setColumnCount(column_count)

       
#         # Populate table with data
#         for row_index, document in enumerate(data):
#             for column_index, (key, value) in enumerate(document.items()):
#                 item = QTableWidgetItem(str(value))
#                 self.ui.D1Table.setItem(row_index, column_index, item)
#                 print(document)

