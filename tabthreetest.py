import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QMainWindow, QApplication, QGridLayout,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QDialog)

from src.plots import *

from typing import Callable

#this is the assembly test for tab3 before adding it to main.py
#move later into src

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window for Plotting")
        self.setGeometry(100,100,800,600)

        main_widget = QWidget()
        #self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(main_widget)

        self.button = ButtonPopOut()

        layout.addWidget(self.button)

        self.setCentralWidget(main_widget)

        return



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
        self.button = ButtonPopOut()
        layout.addWidget(self.button)

        return

class ButtonPopOut(QPushButton):
    def __init__(self):
        super().__init__("Choose Dice")
        self.clicked.connect(self.popup_window)

    def popup_window(self):
        popup = AdjusterPopup("Select Dice")
        if popup.exec_() == QDialog.Accepted:
            results = popup.get_array()
            print("Selected Dice:", results)

def configure_button(button: QPushButton,
                     command: Callable
                     )->None:
    button.clicked.connect(command)
    return None
        
class AdjusterPopup(QDialog):

    """
    A popup window with the Dice Adjusters for the scenario.
    Allows the user to add and/or subtract dice from the 
    array that will be used for the bar plot
    """
    
    def __init__(self, title: str):
        super().__init__()

        #window title will depend on which scenario's button was clicked
        self.setWindowTitle(title)

        layout = QVBoxLayout()

        # 6 adjuster widgets total
        # D4  D6
        # D8  D10
        # D12 D20
        grid = QGridLayout()
        
        self.adjusters = []

        dice_list = [("D4", 4), ("D6", 6), ("D8", 8),
                     ("D10", 10), ("D12", 12), ("D20", 20)]

        for i, (name,sides) in enumerate(dice_list):
            adj_info = DiceAdjuster(name, sides)
            self.adjusters.append(adj_info)
            grid.addWidget(adj_info, i//2, i%2)

        layout.addLayout(grid)

        #button to click to accept totals
        self.ok_button = QPushButton('Ok')


        # When the button is clicked, it calls the accept() method
        # of the QDialog which lets the application know that 
        # the interaction with the dialog is complete.
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button) 

        # Create a vertical layout and add the widgets
        self.setLayout(layout)

    def get_array(self)->list[int]:
        result = []
        for adj_info in self.adjusters:
            result.extend(adj_info.get_dice_array())
        return result


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
    def __init__(self, name: str, sides:int):
        super().__init__()

        self.name = name
        self.value = 0
        self.sides = sides

        layout = QVBoxLayout()
        layout.addWidget(QLabel(self.name))

        button_layout = QHBoxLayout()
        self.minus_button = QPushButton('-')
        self.minus_button.setFixedSize(25, 25)
        self.minus_button.clicked.connect(self.decrease_attribute)

        self.value_label = QLabel(str(self.value))
        self.value_label.setAlignment(Qt.AlignCenter)

        self.plus_button = QPushButton('+')
        self.plus_button.setFixedSize(25, 25)
        self.plus_button.clicked.connect(self.increase_attribute)

        for w in [self.minus_button, self.value_label, self.plus_button]:
            button_layout.addWidget(w)

        layout.addLayout(button_layout)
        self.setLayout(layout)


    #
    def increase_attribute(self):
        self.value += 1
        self.value_label.setText(str(self.value))
        return
    
    def decrease_attribute(self):
        if self.value > 0:

            self.value -= 1
            self.value_label.setText(str(self.value))
        return
    
    def get_dice_array(self)->list[int]:
        return [self.sides] * self.value
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    #with open("style.qss", "r") as f:
    #    _style = f.read()
    #    app.setStyleSheet(_style)

    sys.exit(app.exec_())