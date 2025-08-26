import sys
import math

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QDoubleSpinBox,
)
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader


def float_check(a, b, c):
    """This function checks to see that all user inputs are floats, and that the a coefficient isn't 0. NOTE: checking for floats is no longer necessary because the PySide6 program only takes floats as input."""
    if float(a) == 0.0:
        print("Coefficient a cannot be zero.")
        window.messageBox.setText("Error: Coefficient a cannot be zero.")
        return False
    else:
        return True

def solver(a, b, c):
    """This function does all the math and sets the answer labels/error label."""

    # Step 1: check that input is numbers
    if float_check(a, b, c):

        # Step 2: Math
        sqrt = math.pow(b, 2) - (4 * a * c)
        if sqrt > 0:
            sqrt = math.sqrt(sqrt)
            plus_answer = ((b * (-1)) + sqrt)/(2 * a)
            minus_answer = ((b * (-1)) - sqrt)/(2 * a)

            # Step 3: Put answers in program
            window.answer1.setNum(plus_answer)
            window.answer2.setNum(minus_answer)
            window.messageBox.setText("Status: No errors.")
        else:
            print("Not possible")
            window.messageBox.setText("Error: Not possible.")

def mainwindow_setup(w):
    """This function connects the signal of the pushButton to the calculate slot."""
    w.pushButton.clicked.connect(calculate)

def calculate():
    """Run the solver function with the user's/programs inputs as parameters."""
    solver(window.a.value(), window.b.value(), window.c.value())

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

window = loader.load("window.ui", None)
mainwindow_setup(window)
window.show()
app.exec()
