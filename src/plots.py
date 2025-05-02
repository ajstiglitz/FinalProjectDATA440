import matplotlib.pyplot as plt

from PyQt5.QtWidgets import (QWidget, QLabel, QMainWindow, QApplication,
                             QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton)

from PyQt5.QtCore import Qt

class VarPlots(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()



        self.graph_button = QPushButton()


class Scenarios(QWidget):
    def __init__(self, text="Label"):
        super().__init__()

        #this should be a general class for scenarios 1 and 2.
        #label for name, ability to add in modifier to calculation
        #show how many dice/which dice are in the scenario
    


    def modifier(self):
        #modifier that can be input by user
        #can be any number if they just want to play around 
        #with variance and mean plot calculations
        pass


class DiceAdder(QWidget):
    def __init__(self):
        super().__init__()


class GraphButtons(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        self.reset_button = QPushButton("RESET")
        self.reset_button.clicked.connect(self.reset_graph)

        layout.addWidget(self.reset_button)

        self.calc_button = QPushButton("CALCULATE")
        self.calc_button.clicked.connect(self.calculate_graph)


    def reset_graph(self):
        #this should clear the matplotlib graph and scenarios
        pass

    def calculate_graph(self):
        #this should take the into from scenarios 1 and 2 
        #and calculate the info that will be put into matplotlib graph
        pass