import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QGridLayout, 
                             QTabWidget, QWidget, QVBoxLayout, QLabel)

#from qtcomponents import WindowWithVerticalSlots

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DiceRoller")

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        self.setCentralWidget(self.tab_widget)
        self.create_tabs()

        #grid layout to easliy place widgets in certain spots
        layout = QGridLayout()

        #layout.addWidget()

    def create_tabs(self):
        #tab 1
        tab1 = QWidget()
        layout_tab1 = QVBoxLayout()
        tab1Label = QLabel("Contents")
        layout_tab1.addWidget(tab1Label)


        tab1.setLayout(layout_tab1)
        self.tab_widget.addTab(tab1, "Dice Roller")

        #tab 2
        tab2 = QWidget()
        layout_tab2 = QVBoxLayout()
        tab2.setLayout(layout_tab2)
        self.tab_widget.addTab(tab2, "Character Sheet (?)")        

        #tab 3
        tab3 = QWidget()
        layout_tab3 = QVBoxLayout()
        tab3.setLayout(layout_tab3)
        self.tab_widget.addTab(tab3, "Visualization")


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
