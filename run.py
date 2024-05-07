 
        # Populate table with data
        # row_count = 0
        # for document in data:
        #     print(document)
        #     print('--------users------------')
        #     self.ui.user_table_Widget.insertRow(row_count)
        #     for col_count, key in enumerate(headers):
        #         item = QTableWidgetItem(str(document.get(key, "")))
        #         item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make cells non-editable
        #         self.ui.user_table_Widget.setItem(row_count, col_count, item)
        #     row_count += 1
    
    # def populate_table(self):
    # # Clear existing items in the table
    #     self.ui.user_table_Widget.clear()

    #     # Get data from MongoDB
    #     data = self.collection.find()

    #     # Debug print to check data retrieval
    #     for document in data:
            
    #         print(document)
    #         print('--------users------------')




#         # Rest of your existing code...
#         self.client = MongoClient('mongodb://localhost:27017/')
#         self.db = self.client['data1']
#         self.collection = self.db['B1_DATA']


 
#  def populate_table1(self):
#     # Clear existing items in the table
#         self.ui.user_table_Widget.clear()

#         # Get data from MongoDB
#         data = self.collection.find()

#         # Debug print to check data retrieval
#         for document in data:
            
#             print(document)
#             print('--------births------------')


        #     headers = ["id", "name", "age","city"]  # Replace with your actual column names
#     self.ui.user_table_Widget.setColumnCount(len(headers))
#     self.ui.user_table_Widget.setHorizontalHeaderLabels(headers)

#     # Populate table with data
#     row_count = 0
#     for document in data:
#         self.ui.user_table_Widget.insertRow(row_count)
#         for col_count, key in enumerate(headers):
#             item = QTableWidgetItem(str(document.get(key, "")))
#             item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make cells non-editable
#             self.ui.user_table_Widget.setItem(row_count, col_count, item)



    #     self.client = MongoClient('mongodb://localhost:27017/')
    #     self.db = self.client['data1']
    #     self.collection = self.db['D1_DATA']


    # def populate_table2(self):
    # # Clear existing items in the table
    #     self.ui.user_table_Widget.clear()

        # Get data from MongoDB
        # data = self.collection.find()

        # # Debug print to check data retrieval
        # for document in data:
            
        #     print(document)

        #     print('----------death----------')


    #     headers = ["id", "name", "age","city"]  # Replace with your actual column names
    #     self.ui.user_table_Widget.setColumnCount(len(headers))
    #     self.ui.user_table_Widget.setHorizontalHeaderLabels(headers)

    #     # Populate table with data
    #     row_count = 0
    #     for document in data:
    #         self.ui.user_table_Widget.insertRow(row_count)
    #         for col_count, key in enumerate(headers):
    #             item = QTableWidgetItem(str(document.get(key, "")))
    #             item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make cells non-editable
    #             self.ui.user_table_Widget.setItem(row_count, col_count, item)
