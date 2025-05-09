from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QCheckBox, QLabel,
                             QPushButton, QHBoxLayout, QComboBox, QMainWindow)
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QMovie

import random

from src.buttons import CombinedProfInsp

import os

# Tab 1-specific widgets
class SimulatedDice:
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
    roll_made = pyqtSignal(int) #signal to emit rolled value
    def __init__(self):
        super().__init__()

        #combo box should choose dice simulated
        #simulated should roll with click of button
        #result should be saved for results

        #initializing
        self.last_roll = None

        #dice roller label
        self.label = QLabel("Dice Roller")

        #list of the different drop downs for the combo box
        item_list = ["D20","D12","D10","D8","D6","D4"]
        self.combo_box = QComboBox()
        self.combo_box.setFixedSize(100,30)
        self.combo_box.addItems(item_list)
        self.combo_box.setCurrentIndex(0)
        #based on what die is chosen, gif is changed.
        self.combo_box.currentIndexChanged.connect(self.update_image)

        top_layout = QHBoxLayout()
        top_layout.addWidget(self.label)
        top_layout.addWidget(self.combo_box)

        #the gifs
        self.gif_width = 400
        self.gif_height = 400

        self.die_gif = QLabel()
        self.die_gif.setAlignment(Qt.AlignCenter)
        self.die_gif.setFixedSize(400,400)
        self.gif = QMovie(os.path.join("src","gifs","d20.gif"))
        self.die_gif.setMovie(self.gif)
        self.gif.start()    

        #button to roll the die
        self.button = QPushButton("Roll")
        self.button.clicked.connect(self.roll_die)

        #layout for the widget
        layout = QVBoxLayout()
        layout.addLayout(top_layout)
        layout.addWidget(self.die_gif)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def roll_die(self):
        # should roll one of the functions from the SimulatedDice class
        #This i had to get external help with because pyqt5Signal was a little confusing
        #it seems to be related to getting more advanced signals than just a button press (?)
        die = self.combo_box.currentText()
        result = {
            "D20": SimulatedDice.DTwenty,
            "D12": SimulatedDice.DTwelve,
            "D10": SimulatedDice.DTen,
            "D8": SimulatedDice.DEight,
            "D6": SimulatedDice.DSix,
            "D4": SimulatedDice.DFour
        }[die]()
        self.roll_made.emit(result)


    def update_image(self):
        # this should update the image (gif) shown based on the dice chosen from the combo box.
        die = self.combo_box.currentText()
        gif_path = os.path.join("src","gifs",f"{die}.gif")

        self.gif.stop()
        self.gif = QMovie(gif_path)

        self.gif.setScaledSize(QSize(self.gif_width, self.gif_height))

        self.die_gif.setMovie(self.gif)
        self.gif.start()


class ResultWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.combo_box_attribute = QComboBox()
        self.combo_box_attribute.setFixedSize(100,30)
        self.combo_box_attribute.addItems(["STR", "DEX", "CONS", "INT", "WIS", "CHA"])
        self.combo_box_attribute.currentIndexChanged.connect(self.update_second_combo)

        self.combo_2 = QComboBox()
        self.combo_2.setFixedSize(100,30)

        #maybe make conditional on the d20
        self.result_label = QLabel("Result of STR : Athletics")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.value_label = QLabel("0")
        self.value_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.combo_box_attribute)
        layout.addWidget(self.combo_2)
        layout.addWidget(self.result_label)
        layout.addWidget(self.value_label)

        self.setLayout(layout)

        self.update_second_combo(0)

    def update_second_combo(self,index):
        #clear previous results
        self.combo_2.clear()

        if index == 0: #STR
            self.str_attribute_list = ["Saving Throw", "Athletics"]
            self.combo_2.addItems(self.str_attribute_list)

        elif index == 1: #DEX
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
        #should be a number. based on the roll of the die and the choice from the combo 2.
        # example: if a d20 rolled a 10, and the combo chosen was str: athletics and the player has a +2 and the proficiency checked (lets say another +2)
        # then the resulting roll should be 10 + 2 + 2 which would be 14
        # result should come out as a label. 

        #maybe only have it appear when combo box is on d20, then the result probably is fine...
        stat = self.combo_box_attribute.currentText()
        attribute = self.combo_2.currentText()
        self.result_label.setText(f"Result of {stat} : {attribute}")
        self.value_label.setText(str(value))

#Debugging class
class WindowCheck(QWidget):
    def __init__(self):
        super().__init__()

        self.roller = RollerBoxWidget()
        self.result = ResultWidget()
        self.prof_insp = CombinedProfInsp()

        self.roller.roll_made.connect(self.result.update_result_label)

        layout = QVBoxLayout()
        layout.addWidget(self.prof_insp)
        layout.addWidget(self.roller)
        layout.addWidget(self.result)
        
        self.setLayout(layout)