import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QMainWindow, QApplication, QGridLayout,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QDialog, QFileDialog)

from PyQt5.QtGui import QIntValidator

from src.plots import *

from typing import Callable

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np

#use in the save_graph function
from src.helpers import check_directory

PATH_FIGURES = 'figures'

#this is the assembly test for tab3 before adding it to main.py
#move later into src
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window for Plotting")
        self.setGeometry(100,100,800,600)

        main_widget = QWidget()
        #self.setCentralWidget(self.main_widget)

        main_layout = QVBoxLayout(main_widget)

        layout = QHBoxLayout()

        self.scenarioOneWidget = Scenario("Scenario 1")

        self.scenarioTwoWidget = Scenario("Scenario 2")

        #modifier widget isnt appearing so theres something wrong with it.
        layout.addWidget(self.scenarioOneWidget)
        layout.addWidget(self.scenarioTwoWidget)

        main_layout.addLayout(layout)

        #here is where the plot widget goes
        self.plotWidget = PlotInterface()

        main_layout.addWidget(self.plotWidget)


        self.setCentralWidget(main_widget)

        return



class Scenario(QWidget):
    '''
    General scenario class for tab 3
    '''
    def __init__(self, name:str):
        super().__init__()

        self.dice_array = []
        self.name = name

        layout = QVBoxLayout()

        #set the size later for stylization
        self.label = QLabel(self.name)
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        #widget for the modifier
        self.modWidget = ModifierWidget()
        layout.addWidget(self.modWidget)

        #button for pop-out to get the diceAdjuster grid
        # the results from the grid should be applied to the
        #scenario to be used by the plot
        self.button = ButtonPopOut(self.handle_dice_selection)
        layout.addWidget(self.button)

        self.result_label = QLabel("Selected Dice: ")
        layout.addWidget(self.result_label)

        self.setLayout(layout)


    def handle_dice_selection(self, results: list[int]):
     self.dice_array = results
     self.result_label.setText(f"Selected Dice: {self.dice_array}")
     print(f"{self.name} - Dice Array: {self.dice_array}")       

    def get_modifier(self) -> int:
        return self.modWidget.get_modifier()

    def get_dice_array(self) -> list[int]:
        return self.dice_array

class ButtonPopOut(QPushButton):
    def __init__(self, callback: Callable[[list[int]], None]):
        super().__init__("Choose Dice")
        #lets the parent widget retain the dice chosen (array information to be used later)
        self.callback = callback
        self.clicked.connect(self.popup_window)

    def popup_window(self):
        popup = AdjusterPopup("Select Dice")
        if popup.exec_() == QDialog.Accepted:
            results = popup.get_array()
            self.callback(results)

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

        #mask was adding spaces which was annoying
        #found this instead, testing
        self.lineEdit.setValidator(QIntValidator(-999, 999))
        layout.addWidget(self.lineEdit)

        self.setLayout(layout)

    def get_modifier(self)->int:
        try:
            return int(self.lineEdit.text())
        except ValueError:
            return 0

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
    

class DiceCombo:
    def __init__(self,
                dice: list[int],
                modifier: int):
        
        self.dice = dice
        self.mod = modifier
        self.make_pmf()


    def make_pmf(self)->None:
        self.p = [1/self.dice[0]]*self.dice[0]
        for d in self.dice[1:]:
            p = [1/d]*d
            self.p = np.convolve(self.p, p)
        self.outcomes = np.array(range(len(self.dice), sum(self.dice)+1)) + self.mod


class PlotInterface(QWidget):
    def __init__(self):
        super().__init__()

        #creating the figure and figure canvas (i think this is what it needs??)
        self.figure = Figure(figsize=(5,4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        self.graph_buttons = GraphButtons(self)

        layout.addWidget(self.graph_buttons)

        self.setLayout(layout)

    def draw_plot(self, scenarios: list[DiceCombo]):
        self.figure.clear()
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        colors = ['skyblue', 'red']
        for i, s in enumerate(scenarios):
            ax.bar(s.outcomes, s.p, alpha=0.7, label=f"Combo {i+1}", color=colors[i % len(colors)])
        ax.set_title("Dice Roll Probabilities")
        ax.set_xlabel("Total")
        ax.set_ylabel("Probability")
        ax.legend()
        self.canvas.draw()        

    def reset_plot(self):
        self.figure.clear()
        self.canvas.draw()

    def save_plot(self, filename: str):
        if filename:
            self.figure.savefig(filename)


# class for button row that goes below the graph figure
class GraphButtons(QWidget):
    def __init__(self, plot_interface: PlotInterface):
        super().__init__()

        self.plot_interface = plot_interface

        layout = QHBoxLayout()

        self.reset_button = QPushButton("RESET")
        self.reset_button.clicked.connect(self.reset_graph)

        layout.addWidget(self.reset_button)

        self.calc_button = QPushButton("CALCULATE")
        self.calc_button.clicked.connect(self.calculate_graph)

        layout.addWidget(self.calc_button)

        self.save_button = QPushButton("SAVE")
        self.save_button.clicked.connect(self.save_graph)
        
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def reset_graph(self)->None:
        #this should clear the matplotlib graph and scenarios
        #pass in 0's for the s1=[] and s2=[] to show an empty plot
        self.plot_interface.reset_plot()

    def calculate_graph(self)->None:
        #this should take the into from scenarios 1 and 2 
        #and calculate the info that will be put into matplotlib graph
        main_window = self.plot_interface.parentWidget().parentWidget()

        # Fetch dice and modifier arrays
        s1_dice = main_window.scenarioOneWidget.get_dice_array()
        s2_dice = main_window.scenarioTwoWidget.get_dice_array()
        s1_mod = main_window.scenarioOneWidget.get_modifier()
        s2_mod = main_window.scenarioTwoWidget.get_modifier()

        combos = []
        if s1_dice:
            combos.append(DiceCombo(s1_dice, s1_mod))
        if s2_dice:
            combos.append(DiceCombo(s2_dice, s2_mod))

        if combos:
            self.plot_interface.draw_plot(combos)        

    def save_graph(self)-> None:
        #add functionality
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()

    #with open("style.qss", "r") as f:
    #    _style = f.read()
    #    app.setStyleSheet(_style)

    sys.exit(app.exec_())