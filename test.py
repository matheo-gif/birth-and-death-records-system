from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QVBoxLayout,QApplication, QWidget
import pymongo
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MongoDB Data Display")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.populate_table()

    def populate_table(self):
        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")  # Fix the connection string
        db = client["data1"]
        collection = db["users"]

        # Fetch data from MongoDB
        data = list(collection.find())  # Convert cursor to list

        # Set table dimensions
        row_count = collection.count_documents({})
        column_count = len(data[0]) if row_count > 0 else 0
        self.table_widget.setRowCount(row_count)
        self.table_widget.setColumnCount(column_count)

        # Populate table with data
        for row_index, document in enumerate(data):
            for column_index, (key, value) in enumerate(document.items()):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row_index, column_index, item)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()