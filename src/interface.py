import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QGridLayout, 
                             QTabWidget, QWidget, QVBoxLayout, QLabel, QComboBox)

from PyQt5.QtCore import Qt

from src.diceroller import D20DiceRoller, D12DiceRoller, D10DiceRoller, D8DiceRoller, D6DiceRoller, D4DiceRoller
#from qtcomponents import WindowWithVerticalSlots

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DiceRoller")

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        self.setCentralWidget(self.tab_widget)
        self.create_tabs()

    def create_tabs(self):
        #tab 1 - for the dice roller and ability scores
        tab1 = QWidget()
        layout_tab1 = QVBoxLayout()

        #ComboBox to select between dice
        self.dice_selector = QComboBox()
        self.dice_selector.addItems(["D20", "D12", "D10", "D8", "D6", "D4"])
        self.dice_selector.setFixedSize(100,30)
        self.dice_selector.currentTextChanged.connect(self.switch_dice)
        layout_tab1.addWidget(self.dice_selector)

        #creating the dice roller
        self.dice_roller = D20DiceRoller()
        layout_tab1.addWidget(self.dice_selector, alignment=Qt.AlignRight)
        layout_tab1.addWidget(self.dice_roller, alignment=Qt.AlignTop | Qt.AlignRight)

        #tab setup
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

    def switch_dice(self, text:str):
        """
        removing the older dice roller and switching it with a 
        new one based on user selection
        """
        if text == "D4":
            self.dice_roller.deleteLater()
            self.dice_roller = D4DiceRoller()
        elif text == "D6":
            self.dice_roller.deleteLater()
            self.dice_roller = D6DiceRoller()
        elif text == "D8":
            self.dice_roller.deleteLater()
            self.dice_roller = D8DiceRoller()
        
        elif text == "D10":
            self.dice_roller.deleteLater()
            self.dice_roller = D10DiceRoller()

        elif text == "D12":
            self.dice_roller.deleteLater()
            self.dice_roller = D12DiceRoller()

        else:
            self.dice_roller.deleteLater()
            self.dice_roller = D20DiceRoller()

        self.layout_tab1.addWidget(self.dice_roller, alignment=Qt.AlignTop | Qt.AlignRight)

        #re-adding the layout (isnt correctly in place if not reset)
        self.layout_tab1.addWidget(self.dice_roller, alignment=Qt.AlignTop | Qt.AlignRight)



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
