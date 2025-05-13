from PyQt5.QtWidgets import (QWidget, QLabel, QGridLayout, QPushButton,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QDialog)

from PyQt5.QtGui import QIntValidator, QFont

from typing import Callable

from PyQt5.QtCore import Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from datetime import datetime as dt

import numpy as np

from src.helpers import check_directory

import os

PATH_FIGURES = 'figures'

class GraphTab(QWidget):
    """
    This class is for the complete assembly in the correct layout 
    of the different widgets to be used in Tab 3.
    """
    def __init__(self):
        super().__init__()

        #Creates the main layout
        main_layout = QVBoxLayout()

        #Creates the layout for the Scenarios
        scenario_layout = QHBoxLayout()

        #Creates instances of the Scenario widget and adds the names to the labels
        self.scenarioOneWidget = Scenario("Scenario 1")
        self.scenarioTwoWidget = Scenario("Scenario 2")

        #These lines add the two widgets into the layout
        scenario_layout.addWidget(self.scenarioOneWidget)
        scenario_layout.addWidget(self.scenarioTwoWidget)

        #Adds the scenario layout to the main layout
        main_layout.addLayout(scenario_layout)

        #Here is where the instance of the plot widget is created
        self.plotWidget = PlotInterface(self)

        #Adds the plotting widget to the main layout
        main_layout.addWidget(self.plotWidget)

        #Sets the layout as the main layout so that all the widgets appear
        self.setLayout(main_layout)


class Scenario(QWidget):
    '''
    General scenario class for tab 3. 
    Includes a label for the title, a text editor to show the modfier, and a 
    button that accesses a popup dialog with the dice adjusters.
    '''
    def __init__(self, name:str):
        super().__init__()

        #Empty array that will hold the dice
        self.dice_array = []
        #The name that will be in the label
        self.name = name

        #Creates the layout for the widgets
        layout = QVBoxLayout()

        #Set the size later for stylization
        #Label that will use a provided name
        self.label = QLabel(self.name)

        #Setting font of Label
        font_one = QFont()
        font_one.setPointSize(15)
        font_one.setBold(True)
        self.label.setFont(font_one)

        #Sets the alignement to the center
        self.label.setAlignment(Qt.AlignCenter)
        #Adds the widget to the layout
        layout.addWidget(self.label)

        #Widget for the modifier
        self.modWidget = ModifierWidget()
        #Adds the widget to the layout
        layout.addWidget(self.modWidget)

        #Button for pop-out to get the diceAdjuster grid
        #The results from the grid are applied to the scenario to be used by the plot
        self.button = ButtonPopOut(self.handle_dice_selection)
        #Adds the widget to the layout
        layout.addWidget(self.button)

        #Label to show the result of the dice selected so that the user knows what is being tested
        self.result_label = QLabel("Selected Dice: ")
        #Setting font of Label
        font_two = QFont()
        font_two.setBold(True)
        self.result_label.setFont(font_two)
        #Adds the widget to the layout
        layout.addWidget(self.result_label)

        #Sets the layout so that the widgets appear 
        self.setLayout(layout)

    def handle_dice_selection(self, results: list[int]):
     #This function handles the selected dice and saves the results in a list of integers
     self.dice_array = results
     self.result_label.setText(f"Selected Dice: {self.dice_array}") 

    def get_modifier(self) -> int:
        #This function gets the modifier from the textbox
        return self.modWidget.get_modifier()

    def get_dice_array(self) -> list[int]:
        #This function returns the dice array
        return self.dice_array

class ButtonPopOut(QPushButton):
    """
    This general class is the for the Choose Dice button to be used by the Scenario class. 
    It connects the button to the popup dialog.
    """
    def __init__(self, callback: Callable[[list[int]], None]):
        super().__init__("Choose Dice")
        #Lets the parent widget retain the dice chosen (array information to be used by grapher)
        self.callback = callback
        self.clicked.connect(self.popup_window)

    def popup_window(self):
        #This function calls an instance of the AjusterPopup class so that when the button is clicked
        #The dice popup will appear
        popup = AdjusterPopup("Select Dice")
        if popup.exec_() == QDialog.Accepted:
            #The results are saved and can be used by other classes
            results = popup.get_array()
            self.callback(results)

class AdjusterPopup(QDialog):
    """
    This class creates a popup window with the Dice Adjusters for the scenarios.
    Allows the user to add and/or subtract dice from the 
    array that will be used for the bar plot
    """
    def __init__(self, title: str):
        super().__init__()

        #Window title will depend on which scenario's button was clicked
        self.setWindowTitle(title)

        #Creates the layout as a QVBox
        layout = QVBoxLayout()

        #Grid layout created for the dice adjusters themselves
        grid = QGridLayout()
        
        #Empty list that will hold the different adjusters
        self.adjusters = []

        #List of tuples for the dice and their corresponding value
        dice_list = [("D4", 4), ("D6", 6), ("D8", 8),
                     ("D10", 10), ("D12", 12), ("D20", 20)]

        #Creates an instance of an adjuster and adds the name and information from the dice list
        for i, (name,sides) in enumerate(dice_list):
            adj_info = DiceAdjuster(name, sides)
            self.adjusters.append(adj_info)
            #The widgets are formatted to have two columns and three rows
            grid.addWidget(adj_info, i//2, i%2)

        #Adds the grid layout to the main layout
        layout.addLayout(grid)

        #Button to click to accept totals
        self.ok_button = QPushButton('Ok')

        #When the button is clicked, it calls the accept() method
        #of the QDialog which lets the application know that 
        #the interaction with the dialog is complete.
        self.ok_button.clicked.connect(self.accept)

        #Adds the widget to the layout
        layout.addWidget(self.ok_button) 

        #Sets the layout of the widget
        self.setLayout(layout)

    def get_array(self)->list[int]:
        #This function gets the array of the dice
        result = []
        for adj_info in self.adjusters:
            result.extend(adj_info.get_dice_array())
        return result


class ModifierWidget(QWidget):
    """
    This class creates the modifier widget that is used by the Scenario class.
    """
    def __init__(self):
        super().__init__()

        #Layout is horizontal
        layout = QHBoxLayout()

        #Label is created for user to know what the textbox is for
        self.label = QLabel("Mod: ")
        #Font changed
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        #Adds the widget to the layout
        layout.addWidget(self.label)

        #Creates a box that can be typed in
        self.lineEdit = QLineEdit()

        #Makes sure thatthe user input was a number
        self.lineEdit.setValidator(QIntValidator(-999, 999))
        #Adds the widget to the layout
        layout.addWidget(self.lineEdit)

        #Sets the layout so that the widgets appear
        self.setLayout(layout)

    def get_modifier(self)->int:
        #This function gets the number that was inputted for the modifer to be used by the graphs
        try:
            return int(self.lineEdit.text())
        except ValueError:
            return 0

class DiceAdjuster(QWidget):
    '''
    General widget for the dice populator in tab 3.
    '''
    def __init__(self, name: str, sides:int):
        super().__init__()

        #The name for the dice label
        self.name = name
        #The value is automatically set to zero so that it isn't populated
        self.value = 0
        #The sides are set to sides for changes to happen later
        self.sides = sides

        #Layout is vertical
        layout = QVBoxLayout()
        #Since this is meant to be a general widget, the name is not hardcoded
        layout.addWidget(QLabel(self.name))

        #The layout for the buttons will be horizontal (in one row)
        button_layout = QHBoxLayout()
        #A minus button created
        self.minus_button = QPushButton('-')
        #Size is fixed
        self.minus_button.setFixedSize(25, 25)
        #When the button is clicked, the number will decrease
        self.minus_button.clicked.connect(self.decrease_attribute)

        #Label for the value
        self.value_label = QLabel(str(self.value))
        #Label centered
        self.value_label.setAlignment(Qt.AlignCenter)

        #Plus button created
        self.plus_button = QPushButton('+')
        #Size is fixed
        self.plus_button.setFixedSize(25, 25)
        #When the plus button is clicked, the number will increase
        self.plus_button.clicked.connect(self.increase_attribute)

        #Adds the widgets to the horizontal layout in this order
        for w in [self.minus_button, self.value_label, self.plus_button]:
            button_layout.addWidget(w)

        #Button layout is added to the main layout
        layout.addLayout(button_layout)
        #Layout is set so that the widgets appear
        self.setLayout(layout)

    def increase_attribute(self):
        #This function handles the increase by 1 of a value
        self.value += 1
        self.value_label.setText(str(self.value))
        return
    
    def decrease_attribute(self):
        #This function handles the decrease by 1 of a value
        #Does not let the dice go into the negatives
        if self.value > 0:

            self.value -= 1
            self.value_label.setText(str(self.value))
        return
    
    def get_dice_array(self)->list[int]:
        #This function gets the amount of the dice that were chosen and puts them into a list of integers
        return [self.sides] * self.value
    

class DiceCombo:
    """
    This class is for the calculation of the different scenarios of dice.
    """
    def __init__(self,
                dice: list[int],
                modifier: int):
        
        #The dice that will be used in the calculations
        self.dice = dice
        #The modifier
        self.mod = modifier
        #Instance of the function for the probability mass function called
        self.make_pmf()

    def make_pmf(self)->None:
        #This function handles the calculation of the probability mass function
        #It handles the convolutions of the different dice and calculates the outcomes
        self.p = [1/self.dice[0]]*self.dice[0]
        for d in self.dice[1:]:
            p = [1/d]*d
            self.p = np.convolve(self.p, p)
        self.outcomes = np.array(range(len(self.dice), sum(self.dice)+1)) + self.mod


class PlotInterface(QWidget):
    """
    This class is for showing the matplotlib visualizations in the PyQT5 GUI.
    """
    def __init__(self, graph_tab: GraphTab):
        super().__init__()

        self.graph_tab = graph_tab 

        #Creating the figure and figure canvas for the visualization to go in
        self.figure = Figure(figsize=(5,4), dpi=100)
        self.canvas = FigureCanvas(self.figure)

        #Sets the layout to be vertical
        layout = QVBoxLayout()
        #Adds the canvas widget
        layout.addWidget(self.canvas)

        #Creates an instance of the graph buttons for widget
        self.graph_buttons = GraphButtons(self, graph_tab)

        #Adds the graph buttons to the widget
        layout.addWidget(self.graph_buttons)

        #Sets the layout so that the widgets appear in the GUI
        self.setLayout(layout)

    def draw_plot(self, scenarios: list[DiceCombo]):
        #This function draws the visualization of the results

        #Ensures that its an empty figure before trying to graph
        self.figure.clear()

        #This makes sure that the visualizations are on one plot together
        ax = self.figure.add_subplot(111)
        #These colors separate the two visualizations to make sure that the user is clear which combo is for what
        colors = ['skyblue', 'red']
        #Creates the bar graphs based on the number of scenarios. Max number of scenarios in this GUI is 2
        for i, s in enumerate(scenarios):
            ax.bar(s.outcomes, s.p, alpha=0.7, label=f"Combo {i+1}", color=colors[i % len(colors)])
        #Sets the title of the graph
        ax.set_title("The Chance of Dice Rolls")
        #Sets the name of the x-label
        ax.set_xlabel("Possible Results of a Roll")
        #Sets the name of the y-label
        ax.set_ylabel("Probability of a Roll")
        #Shows a legend so that the user can see which combo connects to which bar graph
        ax.legend()
        #Draws the graph on the canvas to be seen in the GUI
        self.canvas.draw()        

    def reset_plot(self):
        #This function clears the information and redraws the canvas so that it is empty
        self.figure.clear()
        self.canvas.draw()

    def save_plot(self, filename: str):
        #This button saves the graph in the 'figures' folder
        if filename:
            self.figure.savefig(filename)


#Timestamp function for the file name
def timestamp() -> str:
    """
    Creates a timestamp
    """
    t = str(dt.now())
    r = t.replace(' ', '-').replace(':', '-').replace('.', '-')
    return r

class GraphButtons(QWidget):
    """
    This class is for the button row that goes below the graph figure.
    """
    def __init__(self, plot_interface: PlotInterface, graph_tab: GraphTab):
        super().__init__()

        #This creates an instance of the PlotInterface class to be able to use it's functions
        self.plot_interface = plot_interface

        #This creates an instance of the GraphTab class to be able to use it's functions
        self.graph_tab = graph_tab

        #Layout is set to horizontal
        layout = QHBoxLayout()

        #First button is the reset button
        self.reset_button = QPushButton("RESET")
        #Connects the reset graph function to when the button is clicked
        self.reset_button.clicked.connect(self.reset_graph)

        #Adds the widget to the layout
        layout.addWidget(self.reset_button)

        #This button is for calculating the scenarios and getting the graph
        self.calc_button = QPushButton("CALCULATE")
        #Connects the calculate graph function to when the button is clicked
        self.calc_button.clicked.connect(self.calculate_graph)

        #Adds the widget to the layout
        layout.addWidget(self.calc_button)

        #Last button is for saving the graph
        self.save_button = QPushButton("SAVE")
        #When the button is clicked, the graph is saved
        self.save_button.clicked.connect(self.save_graph)
        
        #Adds the widget to the layout
        layout.addWidget(self.save_button)
        #Sets the layout so that the widgets appear
        self.setLayout(layout)

    def reset_graph(self)->None:
        #This clears the matplotlib graph and scenarios
        self.plot_interface.reset_plot()

    def calculate_graph(self)->None:
        #This takes the information from scenarios 1 and 2 
        #and calculates what will be put into matplotlib graph

        #Fetches dice and modifier arrays
        s1_dice = self.graph_tab.scenarioOneWidget.get_dice_array()
        s2_dice = self.graph_tab.scenarioTwoWidget.get_dice_array()
        s1_mod = self.graph_tab.scenarioOneWidget.get_modifier()
        s2_mod = self.graph_tab.scenarioTwoWidget.get_modifier()

        #Empty list that will have the combo information appended into it
        combos = []
        #Calls instances of DiceCombo and calculates the results which are put into combos
        if s1_dice:
            combos.append(DiceCombo(s1_dice, s1_mod))
        if s2_dice:
            combos.append(DiceCombo(s2_dice, s2_mod))

        if combos:
            #draws the plot with the information
            self.plot_interface.draw_plot(combos)        

    def save_graph(self)-> None:
        #This function saves the graph
        # Ensure the folder exists
        check_directory(PATH_FIGURES)
        # Generate timestamped filename
        ts = timestamp()
        filename = os.path.join(PATH_FIGURES, f"plot_{ts}.png")
        # Save the figure
        self.plot_interface.save_plot(filename)