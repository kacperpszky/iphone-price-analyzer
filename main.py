from scraping.scraper import get_offers
from processing.cleaner import clean_iphone_data
from analysis.analyzer import analyze_csv, plot_model_trend, plot_price_trend
import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

WOJEWODZTWO = ""

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone Price Analyzer")
        self.setGeometry(600,250,700,700)
        self.setFixedSize(700,700)
        self.setWindowIcon(QIcon("data//pic.jpg"))
        
        self.labelMain = QLabel("iPhone Prize Analyzer", self)
        self.labelMain.setFont(QFont("Segoe UI", 40))
        self.labelMain.setGeometry(0, 0, 700, 100)
        self.labelMain.setStyleSheet("color: rgba(94,60,158,255);"
                                "font-weight: bold;")
        self.labelMain.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        
        self.label1 = QLabel("Provide Locations: ", self)
        self.label1.setFont(QFont("Segoe UI", 15))
        self.label1.setGeometry(0, 100, 250, 50)
        self.label1.setStyleSheet("padding-left: 10px;"
                                    "padding-right: 10px;"
                                    "margin-left: 20px;"
                                    "margin-right: 20px;")
        
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(200, 100, 300, 50)
        self.input_field.setStyleSheet("padding-left: 10px;"
                                    "padding-right: 10px;"
                                    "margin-left: 20px;"
                                    "margin-right: 20px;")
        
        self.button = QPushButton("Analyze", self)
        self.button.setGeometry(500, 110, 150, 35)
        self.button.clicked.connect(self.handle_button_click)
        
        self.table = QTableWidget(self)
        self.table.setGeometry(0, 180, 700, 400)
        self.table.setColumnCount(5) 
        self.table.setHorizontalHeaderLabels(["Count", "Mean", "Min", "Max", "Median"])
        self.table.verticalHeader().setVisible(False)
        self.table.setStyleSheet("padding-left: 10px;"
                                    "padding-right: 10px;"
                                    "margin-left: 20px;"
                                    "margin-right: 20px;")
     
        self.button_trend = QPushButton("Show Trend Plot", self)
        self.button_trend.setGeometry(200, 600, 150, 35)
        self.button_trend.clicked.connect(self.handle_trend_button)
        
        self.button_price = QPushButton("Show Price Plot", self)
        self.button_price.setGeometry(350, 600, 150, 35)
        self.button_price.clicked.connect(self.handle_price_button)      
       
    def display_analysis(self, results):
        headers = ["Model", "count", "mean", "min", "max", "median"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(results))
        self.table.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)

        for i, row in enumerate(results):
            for j, key in enumerate(headers):
                value = str(row.get(key, ""))
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(i, j, item)   
             
    def handle_button_click(self):
        WOJEWODZTWO = str(self.input_field.text())
        if WOJEWODZTWO=="polska":
            url = "https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/?search%5Border%5D=created_at:desc"
        else:
            url = f"https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/{WOJEWODZTWO}/?search%5Border%5D=created_at:desc"
       
        offers = get_offers(url)
        clean_iphone_data(WOJEWODZTWO)
        result = analyze_csv()
        self.display_analysis(result)
        time.sleep(1)
        
    def handle_trend_button(self):
        plot_model_trend(WOJEWODZTWO)
        
    def handle_price_button(self):
        plot_price_trend(WOJEWODZTWO)
      
if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

    
    
    
        
        
    