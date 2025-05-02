from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QCheckBox, QLabel,
                             QPushButton, QHBoxLayout, QGridLayout)

from PyQt5.QtCore import Qt, QSize
 
class AttributesLoaded(QWidget):
    def __init__(self,prof_widget):
        super().__init__()

        self.prof_widget = prof_widget

        layout = QVBoxLayout()

        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)
        self.setLayout(layout)

        # Create attributes + checkboxes
        for attr_name in ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']:
            attr_adjuster = AttributeAdjuster(attr_name)
            attr_check = AttributeCheck(attr_name, attr_adjuster, self.prof_widget)

            attr_section = QVBoxLayout()
            attr_section.addWidget(attr_adjuster)
            attr_section.addWidget(attr_check)

            section_widget = QWidget()
            section_widget.setLayout(attr_section)
            layout.addWidget(section_widget)

class CombinedProfInsp(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)

        self.proficiency_bonus = ButtonsUpdateLabel()

        self.inspiration = CheckBoxAndLabel()

        layout.addWidget(self.proficiency_bonus)
        layout.addWidget(self.inspiration)

        self.setLayout(layout)


# EDIT THE SIZE OF THE BUTTONS TO BE FIXED.
#probably setGeometry() or something. 

#for Tab 1. Meant to go at the top right corner
class ButtonsUpdateLabel(QWidget):
    #proficiency bonus widget
    def __init__(self):
        super().__init__()

        self.prof_label = QLabel("Proficiency Bonus")

        layout = QVBoxLayout()
        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)

        layout.addWidget(self.prof_label)

        self.value = 2

        #Horizontal layout for buttons and number bonus
        button_layout = QHBoxLayout()

        self.minus_button = QPushButton('-')
        self.minus_button.setFixedSize(25, 25)
        self.minus_button.clicked.connect(self.decrease_number)
        button_layout.addWidget(self.minus_button)

        #self.prof_bonus_label = QLabel()
        #self.update_prof_display()
        #button_layout.addWidget(self.prof_bonus_label)

        self.proficiency_display = QLabel()
        self.update_prof_display()
        button_layout.addWidget(self.proficiency_display)

        self.plus_button = QPushButton('+')
        self.plus_button.setFixedSize(25, 25)
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
        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)

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



class AttributeAdjuster(QWidget):
    def __init__(self, name: str):
        super().__init__()

        self.name = name
        self.value = 10

        main_layout = QVBoxLayout()
        main_layout.setSpacing(2)
        main_layout.setContentsMargins(5,5,5,5)
        self.setLayout(main_layout)

        #names
        attribute_names = QLabel(self.name)
        attribute_names.setAlignment(Qt.AlignCenter)  # Centered name
        main_layout.addWidget(attribute_names)

        self.adjuster_row = QHBoxLayout()
        self.adjuster_row.setSpacing(2)

        self.minus_button = QPushButton('-')
        self.minus_button.setFixedSize(25, 25)
        self.minus_button.clicked.connect(self.decrease_attribute)

        self.modifier_label = QLabel()
        self.modifier_label.setAlignment(Qt.AlignCenter)
        self.plus_button = QPushButton('+')
        self.plus_button.setFixedSize(25, 25)
        self.plus_button.clicked.connect(self.increase_attribute)

        for w in [self.minus_button, self.modifier_label, self.plus_button]:
            self.adjuster_row.addWidget(w)

        main_layout.addLayout(self.adjuster_row)

        self.attribtue_display = QLabel()
        self.attribtue_display.setAlignment(Qt.AlignCenter)
        self.update_attribute_display()
        main_layout.addWidget(self.attribtue_display)
        return
    
    def update_attribute_display(self):
        self.attribtue_display.setText(str(self.value))
        modifier = (self.value - 10)//2
        self.modifier_label.setText(str(modifier))
        return
    
    def increase_attribute(self):
        self.value += 1
        self.update_attribute_display()
        return
    
    def decrease_attribute(self):
        self.value -= 1
        self.update_attribute_display()
        return
    
    def get_modifier(self):
        return (self.value - 10) // 2

class AttributeCheck(QWidget):
    def __init__(self, attr_name:str, 
                 attr_adjuster:AttributeAdjuster,
                 prof_widget):
        super().__init__()

        self.prof_widget = prof_widget

        self.checks = []

        self.attr_adjuster = attr_adjuster

        layout = QVBoxLayout()
        self.setLayout(layout)

        #number of check boxes based on the the attribute like how in ResultWidget, the second combo box has different number of options
        # when checked, the proficiency bonus should be added to the modifier that the attribute display has
        #list of tuples for the different options

        self.list=[]

        attributes_options = {
            'STR': ['Saving Throw', 'Athletics'],
            'DEX': ['Saving Throw', 'Acrobatics','Sleight of Hand', 'Stealth'],
            'CONS': ['Saving Throw'],
            'INT': ['Saving Throw', 'Arcana', 'History', 'Investigation', 'Nature', 'Religion'],
            'WIS': ['Saving Throw', 'Animal Handling','Insight','Medicine','Perception','Survival'],
            'CHA': ['Saving Throw', 'Deception','Intimidation','Performace','Persuasion']
        }

        skills = attributes_options.get(attr_name, [])
        fixed_row_num = 2
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        #trying to get the rows fixed but cols whatever
        for i, skill in enumerate(skills):
            rows = i % fixed_row_num
            cols = i // fixed_row_num

            checkbox = QCheckBox(skill)

            label = QLabel("")
            label.setAlignment(Qt.AlignCenter)
            label.setFixedWidth(30)

            checkbox.stateChanged.connect(lambda state, c=checkbox, l=label: self.update_label(c, l))

            grid_layout.addWidget(checkbox, rows, cols*2)
            grid_layout.addWidget(label, rows, cols*2)


            self.checks.append((checkbox, label))

    def update_label(self, checkbox, label):
        if checkbox.isChecked():
            prof = self.prof_widget.value
            mod = self.attr_adjuster.get_modifier()
            total = prof + mod
            label.setText(str(total))
        else:
            label.setText("")