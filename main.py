# creating grid layout, vertical, horizontal or grid layout we will use grid layout

import sys  # importing sys stem level operations
import math
from PyQt5.QtWidgets import *

class Button:
    def __init__(self, text, results):
        self.b = QPushButton(str(text))
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handleInput(self.text))

    def handleInput(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "√":
            value = float(self.results.text())
            self.results.setText(str(math.sqrt(value)))
        elif v == "DEL":
            current_value = self.results.text()
            self.results.setText(current_value[:-1])
        else:
            current_value = self.results.text()
            new_value = current_value + str(v)
            self.results.setText(new_value)
# creating window

class Application(QWidget):
    def __init__(self):        # setting initialization
        super().__init__()  # super is a method
        self.setWindowTitle("Calculator")
        self.CreateApp()


    def CreateApp(self):

        # Creating grid
        grid = QGridLayout()
        results = QLineEdit()
        buttons = ["AC", "√", "DEL", "/",
                    7, 8, 9, "*",
                    4, 5, 6, "-",
                    1, 2, 3, "+",
                    0, ".", "="]

        grid.addWidget(results, 0, 0, 1, 4)
        row = 1
        col = 0

        for button in buttons:

            if col > 3: # next row when column is full
                col = 0
                row += 1

            buttonObject = Button(button, results)

            if button == 0:
                grid.addWidget(buttonObject.b, row, col, 1, 2)
                col += 1      # cuz 0 button is 2 col long we need to add another one to col, so 0 is not on dot
            else:
                grid.addWidget(buttonObject.b, row, col, 1, 1)
            col += 1

        self.setLayout(grid)

        self.show()

# running the code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())   # until it exits it's  going to run the code, when method inside will be true it will exit




