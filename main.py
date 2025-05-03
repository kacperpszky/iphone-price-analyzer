from scraping.scraper import get_offers
from processing.cleaner import clean_iphone_data
from analysis.analyzer import analyze_csv
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


# [DONE] dodac mozliwosc edycji url z requestem aby przyjmowac jedynie rekordy z danej lokalizacji np. sam Gdansk/Gdynia itd i dawac analize jako 
# pomorskie/dolnoslaskie/kujawsko-pomorskie/lubelskie/lubuskie/lodzkie/malopolskie/mazowieckie/opolskie/podkarpackie/podlaskie/slaskie/swietokrzyskie/warminsko-mazurskie/wielkopolskie/zachodniopomorskie.

# [in progress] zrobic zajebiste GUI najlepiej w czyms praktycznym, moze byc PyQt / streamlit
# export analizy/wykresu na pewno musi sie tu znalezc, wiec dodac w przyszlosci
# co do analizy dodac trend ip, jakie kiedy byly najbardziej popularne itd.....


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
        
    def handle_button_click(self):
        wojewodztwo = str(self.input_field.text())
        if wojewodztwo=="polska":
            url = "https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/?search%5Border%5D=created_at:desc"
        else:
            url = f"https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/iphone/{wojewodztwo}/?search%5Border%5D=created_at:desc"
       
        offers = get_offers(url)
        clean_iphone_data()
        analyze_data = analyze_csv()
        print(analyze_data)
        
    
        
        
        
        
        


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    

    
    
    
        
        
    