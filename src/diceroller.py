from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel,
                             QPushButton, QHBoxLayout, QComboBox)
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QMovie

import random

import os

# Tab 1-specific widgets
class SimulatedDice:
    """
    This class creates the random number generators that represent the different dice.
    The dice that can be generated are the D4, D6, D8, D10, D12, and D20.
    """

    #The static methods are so that we don't use self. Can't be overridden.
    @staticmethod
    def DTwenty():
        rand_num = random.randint(1,20)
        return rand_num

    @staticmethod
    def DTwelve():
        rand_num = random.randint(1,12)
        return rand_num        

    @staticmethod
    def DTen():
        rand_num = random.randint(1,10)
        return rand_num

    @staticmethod
    def DEight():
        rand_num = random.randint(1,8)
        return rand_num

    @staticmethod
    def DSix():
        rand_num = random.randint(1,6)
        return rand_num

    @staticmethod
    def DFour():
        rand_num = random.randint(1,4)
        return rand_num

class RollerBoxWidget(QWidget):
    """
    This class chooses the dice that is simulated and changes the GIF accordingly.
    """
    #Signal to emit rolled value
    roll_made = pyqtSignal(int) 

    def __init__(self):
        super().__init__()

        #combo box should choose dice simulated
        #simulated should roll with click of button
        #result should be saved for results

        #Initializing the first roll
        self.last_roll = None

        #Dice roller label
        self.label = QLabel("Dice Roller")

        #List of the different drop downs for the combo box
        item_list = ["D20","D12","D10","D8","D6","D4"]
        self.combo_box = QComboBox()
        self.combo_box.setFixedSize(100,30)
        self.combo_box.addItems(item_list)
        self.combo_box.setCurrentIndex(0)

        #Based on what die is chosen, gif is changed
        self.combo_box.currentIndexChanged.connect(self.update_image)

        #Layout is horizontal and the label and combobox widgets are added to the layout
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.label)
        top_layout.addWidget(self.combo_box)

        #The gif size is set
        self.gif_width = 400
        self.gif_height = 400

        #A Label for the gifs
        self.die_gif = QLabel()
        #Alignment and size set for the gifs
        self.die_gif.setAlignment(Qt.AlignCenter)
        self.die_gif.setFixedSize(self.gif_width, self.gif_height)
        
        #First gif that appears is the d20 gif
        self.gif = QMovie(os.path.join("src","gifs","d20.gif"))
        #Sets the gif
        self.die_gif.setMovie(self.gif)
        #Starts the gif so that it moves
        self.gif.start()    

        #Button to roll the die
        self.button = QPushButton("Roll")
        #When clicked the die is rolled
        self.button.clicked.connect(self.roll_die)

        #Layout for the widget
        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addWidget(self.die_gif)
        layout.addWidget(self.button)

        #Layout set so that the widgets appear
        self.setLayout(layout)

    def roll_die(self):
        # This function rolls one of the functions from the SimulatedDice class
        die = self.combo_box.currentText()
        #Depending on which dice it is, the function called will change
        result = {
            "D20": SimulatedDice.DTwenty,
            "D12": SimulatedDice.DTwelve,
            "D10": SimulatedDice.DTen,
            "D8": SimulatedDice.DEight,
            "D6": SimulatedDice.DSix,
            "D4": SimulatedDice.DFour
        }[die]()
        #Gives the result
        self.roll_made.emit(result)


    def update_image(self):
        #This function updates the image (gif) shown based on the dice chosen from the combo box.
        die = self.combo_box.currentText()
        gif_path = os.path.join("src","gifs",f"{die}.gif")

        #The previous gif stops
        self.gif.stop()
        #New gif QMovie instance created with the correct gif
        self.gif = QMovie(gif_path)

        #Gif scaled
        self.gif.setScaledSize(QSize(self.gif_width, self.gif_height))
        self.die_gif.setMovie(self.gif)
        #Gif movement started
        self.gif.start()


class ResultWidget(QWidget):
    """
    This class assembles the widgets for the results.
    """
    def __init__(self):
        super().__init__()

        #Combobox created with the different possible attributes
        self.combo_box_attribute = QComboBox()
        #The size is set
        self.combo_box_attribute.setFixedSize(100,30)
        #Items in the dropdown
        self.combo_box_attribute.addItems(["STR", "DEX", "CONS", "INT", "WIS", "CHA"])
        #Changes what is shown in the second combobox based on the first dropdown
        self.combo_box_attribute.currentIndexChanged.connect(self.update_second_combo)

        #This is the second combo box
        self.combo_2 = QComboBox()
        #Size is fixed
        self.combo_2.setFixedSize(100,30)

        #Label initialized
        self.result_label = QLabel("Result of STR : Athletics")
        #aligned to the center
        self.result_label.setAlignment(Qt.AlignCenter)
        #Label initialized with 0
        self.value_label = QLabel("0")
        #Alignment set to the center
        self.value_label.setAlignment(Qt.AlignCenter)

        #The layout is vertical
        layout = QVBoxLayout()
        #Widgets are added
        layout.addWidget(self.combo_box_attribute)
        layout.addWidget(self.combo_2)
        layout.addWidget(self.result_label)
        layout.addWidget(self.value_label)

        #Interface is set to make the widgets appear
        self.setLayout(layout)

        #The index of the second widget is set to 0, since all of the abilities have "Saving Throw" as an option
        self.update_second_combo(0)

    def update_second_combo(self,index):
        #This function should update what the second dropdown shows based on the first

        #Clears previous results
        self.combo_2.clear()

        if index == 0: #STR
            #possible choice is: saving throw, athletics
            self.str_attribute_list = ["Saving Throw", "Athletics"]
            self.combo_2.addItems(self.str_attribute_list)

        elif index == 1: #DEX
            #possible choice is: saving throw, acrobatics, sleight of hand, stealth
            self.dex_attribute_list = ["Saving Throw", "Acrobatics", "Sleight of Hand", "Stealth"]
            self.combo_2.addItems(self.dex_attribute_list)

        elif index == 2: #CONS
            #possible choice is: saving throw
            self.cons_attribute_list = ["Saving Throw"]
            self.combo_2.addItems(self.cons_attribute_list)

        elif index == 3: #INT
            #possible choices are: saving throw, arcana, history, investigation, nature, religion
            self.int_attribute_list = ["Saving Throw", "Arcana", "History", "Investiagtion", "Nature", "Religion"]
            self.combo_2.addItems(self.int_attribute_list)

        elif index == 4: #WIS
            #possible choices are: saving throw, animal handling, insight, medicine, perception, survival
            self.wis_attribute_list = ["Saving Throw", "Animal Handling", "Insight", "Medicine", "Perception", "Survival"]
            self.combo_2.addItems(self.wis_attribute_list)

        elif index == 5: #CHA
            #possible choices are: saving throw, deception, intimidation, performance, persuasion
            self.cha_attribute_list = ["Saving Throw", "Deception", "Intimidation", "Performance", "Persuasion"]
            self.combo_2.addItems(self.cha_attribute_list)

        self.update_result_label(0)

    def update_result_label(self, value):
        #This function is based on the roll of the die and the choice from the combo 2.
        # example: if a d20 rolled a 10, and the combo chosen was str: athletics and the player has a +4 and the proficiency checked (lets say another +2)
        # then the resulting roll should be 10 + 4 + 2 which would be 16
        # result should come out as a label. 

        #Right now the roll doesnt seem to add anything
        #Add a secondary label to show the roll of the die (So that you know if you rolled a nat one)

        stat = self.combo_box_attribute.currentText()
        attribute = self.combo_2.currentText()
        #Label for the attribute and the skill being rolled for
        self.result_label.setText(f"Result of {stat} : {attribute}")
        #Sets the label to the resulting value
        self.value_label.setText(str(value))

class WindowCheck(QWidget):
    """
    This class Assembles the widgets in order to be used by the tabone.py file.
    """
    def __init__(self):
        super().__init__()


        self.roller = RollerBoxWidget()
        self.result = ResultWidget()

        self.roller.roll_made.connect(self.result.update_result_label)

        layout = QVBoxLayout()
        layout.addWidget(self.roller)
        layout.addWidget(self.result)
        
        self.setLayout(layout)