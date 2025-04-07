import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout

from qtcomponents import WindowWithVerticalSlots

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DiceRoller")

        #grid layout to easliy place widgets in certain spots
        layout = QGridLayout()

        #layout.addWidget()


def main():
    app = QApplication([])
    window = MainWindow()

    #set the window size permanently, in pixels
    #not adjustable for user.
    window.setFixedSize(920,950)

    #show the window
    window.show()
    #ensure that the window stays open until user closes it
    sys.exit(app.exec())
