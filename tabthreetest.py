import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QMainWindow, QApplication,
                             QLineEdit, QHBoxLayout, QVBoxLayout)

from src.plots import *

#this is the assembly test for tab3 before adding it to main.py
#move later into src

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window for Plotting")
        self.setGeometry(100,100,800,600)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        top_row_layout = QHBoxLayout()

        main_layout.addLayout(top_row_layout)

class Scenario(QWidget):
    '''
    General scenario class for tab 3
    '''
    def __init__(self, name:str):
        super().__init__()

        layout = QVBoxLayout()

        #set the size later for stylization
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        #widget for the modifier
        self.modWidget = ModifierWidget()
        layout.addWidget(self.modWidget)

        #button for pop-out to get the diceAdjuster grid
        # the results from the grid should be applied to the
        #scenario to be used by the plot



class ModifierWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.label = QLabel("Mod: ")

        layout.addWidget(self.label)

        self.lineEdit = QLineEdit()

        #sets a mask, so that user can only input number
        # decide later if I want to change first 0 to 9
        #that would require user to put in number from 0-9
        self.lineEdit.setInputMask("00000000")
        layout.addWidget(self.lineEdit)

class DiceAdjuster(QWidget):
    '''
    General widget for the dice populator in tab 3 
    '''
    def __init__(self, name: str):
        super().__init__()

        self.name = name
        self.value = 0


    #
    def increase_attribute(self):
        self.value += 1
        self.update_attribute_display()
        return
    
    def decrease_attribute(self):
        self.value -= 1
        self.update_attribute_display()
        return