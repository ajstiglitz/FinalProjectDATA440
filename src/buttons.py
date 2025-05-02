from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QCheckBox, QLabel,
                             QPushButton, QHBoxLayout)

from PyQt5.QtCore import Qt
 
#for Tab 1. Meant to go at the top right corner
class ButtonsUpdateLabel(QWidget):
    #proficiency bonus widget
    def __init__(self):
        super().__init__()

        self.prof_label = QLabel("Proficiency Bonus")

        layout = QVBoxLayout()

        layout.addWidget(self.prof_label)

        self.value = 2

        #Horizontal layout for buttons and number bonus
        button_layout = QHBoxLayout()

        self.minus_button = QPushButton('-')
        self.minus_button.clicked.connect(self.decrease_number)
        button_layout.addWidget(self.minus_button)

        #self.prof_bonus_label = QLabel()
        #self.update_prof_display()
        #button_layout.addWidget(self.prof_bonus_label)

        self.proficiency_display = QLabel()
        self.update_prof_display()
        button_layout.addWidget(self.proficiency_display)

        self.plus_button = QPushButton('+')
        self.plus_button.clicked.connect(self.increase_number)
        button_layout.addWidget(self.plus_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.update_button_states()

    
    def update_prof_display(self):
        #this might be superfluous
        self.proficiency_display.setText(str(self.value))

    def decrease_number(self):
        #see if this works
        if self.value > 2:
            self.value -= 1
            self.update_prof_display()
            self.update_button_states()

    def increase_number(self):
        #see if this works
        if self.value < 6:
            self.value += 1
            self.update_prof_display()
            self.update_button_states()
    
    def update_button_states(self):
        self.minus_button.setEnabled(self.value > 2)
        self.plus_button.setEnabled(self.value < 6)


#for Tab 1. Meant to go below ButtonsUpdateLabel at the top right corner
# NTS: might need to change stylesheet for it
class CheckBoxAndLabel(QWidget):
    def __init__(self):
        super().__init__()
        #Check box for inspiration
        #can probably find a way to make it more general for other use

        layout = QVBoxLayout()

        self.checkBox = QCheckBox("Inspiration")
        self.checkBox.stateChanged.connect(self.update_message)
        self.checkBox.setChecked(False) # want it to start unchecked
        self.checkBox.setGeometry(200,150,100,30)
        #label needs to have its state changed by the modifiers
        #and additionally if checkbox is checked, modifier needs to have prof bonus added
        self.label = QLabel("")
        self.label.setAlignment(Qt.AlignLeft)

        layout.addWidget(self.checkBox)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def update_message(self, state):
        if state == Qt.Checked:
            self.label.setText("Inspired!")
        else:
            self.label.setText("")