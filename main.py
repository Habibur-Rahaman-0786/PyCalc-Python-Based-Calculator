import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator_ui import Ui_MainWindow

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.display = self.ui.lineEdit

        # Connect buttons
        self.ui.btn_0.clicked.connect(lambda: self.add_to_input('0'))
        self.ui.btn_1.clicked.connect(lambda: self.add_to_input('1'))
        self.ui.btn_2.clicked.connect(lambda: self.add_to_input('2'))
        self.ui.btn_3.clicked.connect(lambda: self.add_to_input('3'))
        self.ui.btn_4.clicked.connect(lambda: self.add_to_input('4'))
        self.ui.btn_5.clicked.connect(lambda: self.add_to_input('5'))
        self.ui.btn_6.clicked.connect(lambda: self.add_to_input('6'))
        self.ui.btn_7.clicked.connect(lambda: self.add_to_input('7'))
        self.ui.btn_8.clicked.connect(lambda: self.add_to_input('8'))
        self.ui.btn_9.clicked.connect(lambda: self.add_to_input('9'))

        self.ui.btn_add.clicked.connect(lambda: self.add_to_input('+'))
        self.ui.btn_subtract.clicked.connect(lambda: self.add_to_input('-'))
        self.ui.btn_multiply.clicked.connect(lambda: self.add_to_input('*'))
        self.ui.btn_divide.clicked.connect(lambda: self.add_to_input('/'))
        self.ui.btn_dot.clicked.connect(lambda: self.add_to_input('.'))

        self.ui.btn_clear.clicked.connect(self.clear_input)
        self.ui.btn_equal.clicked.connect(self.calculate_result)

    def add_to_input(self, value):
        self.display.setText(self.display.text() + value)

    def clear_input(self):
        self.display.clear()

    def calculate_result(self):
        try:
            result = str(eval(self.display.text()))
            self.display.setText(result)
        except:
            self.display.setText("Error")

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())
