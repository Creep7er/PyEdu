from PyQt6 import QtWidgets, QtCore 

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
            QtWidgets.QWidget.__init__(self, parent) #инициализируем
            self.label = QtWidgets.QLabel('Hello epta') 
            self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter) # центруем текст
            self.btnQuit = QtWidgets.QPushButton("&Закрыть окно")
            self.vbox = QtWidgets.QVBoxLayout()
            self.vbox.addWidget(self.label)
            self.vbox.addWidget(self.btnQuit)
            self.setLayout(self.vbox)
            self.btnQuit.clicked.connect(QtWidgets.QApplication.instance().quit)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow() # создаем объект класса 
    window.setWindowTitle("OOP STYLE APP") 
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec())           
            
        