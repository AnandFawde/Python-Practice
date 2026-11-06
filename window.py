# PyQt5 introhki

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()   
        self.setWindowTitle("My First GUI")
        self.setGeometry(670,290,600,600) 
        label = QLabel("DANGER",self)
        label.setFont(QFont("Arial",20))
        label.setGeometry(10,10,200,200)  
        label.setStyleSheet("color:red;"
                            "backgroung-color:black;"
                            "font-weight: blod;"
                            "font-style: italic;"
                            "text-deoretion: underline;")
        
        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    


if __name__ == "__main__":
    main()