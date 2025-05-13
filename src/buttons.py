from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QCheckBox, QLabel,
                             QPushButton, QHBoxLayout, QGridLayout)

#Keeping QSize here for now if I use it for formatting later
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont
 
from functools import partial

class AttributesLoaded(QWidget):
    """
    This class loads the attribute widgets and adds them to the layout.
    """
    def __init__(self, prof_widget):
        super().__init__()

        #Prof widget is the widget for Proficiency
        self.prof_widget = prof_widget
        self.setMaximumWidth(500)

        layout = QVBoxLayout()

        # Trying to mess with the format of the widgets to see if I can fix the spacing
        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)
        self.setLayout(layout)

        #Creates attributes + checkboxes
        for attr_name in ['STR', 'DEX', 'CONS', 'INT', 'WIS', 'CHA']:
            attr_adjuster = AttributeAdjuster(attr_name)
            attr_check = AttributeCheck(attr_name, attr_adjuster, self.prof_widget)

            attr_section = QVBoxLayout()
            attr_section.addWidget(attr_adjuster)
            attr_section.addWidget(attr_check)

            section_widget = QWidget()

            section_widget.setLayout(attr_section)
            layout.addWidget(section_widget)



class CombinedProfInsp(QWidget):
    """
    This class combines the widgets for Inspiration and Proficiency.
    They were combined here to be called for easier readbility and formatting.
    """
    def __init__(self, prof_widget):
        super().__init__()

        #Prof widget is the widget for Proficiency
        self.prof_widget = prof_widget

        layout = QVBoxLayout()
        
        #Trying to mess with the formatting 
        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)

        self.inspiration = CheckBoxAndLabel()

        layout.addWidget(self.prof_widget)
        layout.addWidget(self.inspiration)

        self.setLayout(layout)


#for Tab 1. Meant to go at the top right corner
class ButtonsUpdateLabel(QWidget):
    """
    This class creates the widget for the Proficiency bonus in the GUI.
    """
    #Signal emitted to connect widgets so that the attribute gets the correct proficiency value
    proficiency_changed = pyqtSignal(int)
    def __init__(self):
        super().__init__()

        #Creates a label with the name
        self.prof_label = QLabel("Proficiency Bonus")

        #Sets the layout
        layout = QVBoxLayout()
        #Messing with the format
        layout.setSpacing(5)
        #layout.setContentsMargins(2,2,2,2)

        #Adds the widget to the layout
        layout.addWidget(self.prof_label)

        #This sets the initial value of the Proficiency bonus
        self.value = 2

        #Horizontal layout for buttons and number bonus
        button_layout = QHBoxLayout()

        #Creates the minus button for the Proficiency bonus widget
        self.minus_button = QPushButton('-')
        #Sets the button's size
        self.minus_button.setFixedSize(25, 25)
        #When this minus button is clicked, the number decreases
        self.minus_button.clicked.connect(self.decrease_number)
        #Adds the widget to the layout
        button_layout.addWidget(self.minus_button)

        #Creates an empty label that will show the proficiency bonus number
        self.proficiency_display = QLabel()
        #Aligns it to the center so that it is centered and not closer to one button or the other in the widget
        self.proficiency_display.setAlignment(Qt.AlignCenter)
        #Calls the update_prof_display to ensure that the number is correctly updated in the display
        self.update_prof_display()
        #Adds the widget
        button_layout.addWidget(self.proficiency_display)

        #Creates the plus button for the widget
        self.plus_button = QPushButton('+')
        #Sets the size
        self.plus_button.setFixedSize(25, 25)
        #When the plus is clicked, the number will increase
        self.plus_button.clicked.connect(self.increase_number)
        #Adds the widget to the button_layout
        button_layout.addWidget(self.plus_button)

        #Adds the button layout to the main layout of the widget
        layout.addLayout(button_layout)

        #Sets the layout so that it will appear
        self.setLayout(layout)

        #Updates the states of the buttons
        self.update_button_states()
    
    def update_prof_display(self):
        #Updates the text in the label to make sure it is the right value
        self.proficiency_display.setText(str(self.value))

    def decrease_number(self):
        #This function will decrease the number of the counter by 1
        #Unless the value is 2, then it cannot decrease any more and button becomes inactive
        if self.value > 2:
            self.value -= 1
            self.update_prof_display()
            self.update_button_states()
            self.proficiency_changed.emit(self.value)

    def increase_number(self):
        #This function will increase the number of the counter by 1
        #Unless the value is 6, then it cannot increase any more and button becomes inactive
        if self.value < 6:
            self.value += 1
            self.update_prof_display()
            self.update_button_states()
            self.proficiency_changed.emit(self.value)
    
    def update_button_states(self):
        #This function checks the value
        #Button states are updated based on the number
        self.minus_button.setEnabled(self.value > 2)
        self.plus_button.setEnabled(self.value < 6)

    def get_prof_bonus(self):
        #Function gets the value of the proficiency bonus
        return self.value


#For Tab 1 formatting, this is meant to go below ButtonsUpdateLabel at the top right corner
class CheckBoxAndLabel(QWidget):
    """
    This class is for the creation of the "Inspired" checkbox.
    When clicked, the label should appear and say "Inspired!" to 
    notify the user that they can roll with advantage.
    """
    def __init__(self):
        super().__init__()

        #Makes the main layout a QVBox
        layout = QVBoxLayout()

        #Messing with the format
        layout.setSpacing(2)
        layout.setContentsMargins(5,5,5,5)

        #Creates and Names the Checkbox
        self.checkBox = QCheckBox("Inspiration")
        #When the checkbox is clicked, a message should appear
        self.checkBox.stateChanged.connect(self.update_message)
        self.checkBox.setChecked(False) #Want it to start with the checkbox unchecked
        #Sets the geometry for formatting
        self.checkBox.setGeometry(200,150,100,30)

        #Empty label
        self.label = QLabel("")
        #Sets the alignment of the label
        self.label.setAlignment(Qt.AlignLeft)

        #Adds the widgets to the layout
        layout.addWidget(self.checkBox)
        layout.addWidget(self.label)

        #Sets the layout so that it appears in the widget
        self.setLayout(layout)

    def update_message(self, state):
        #This function updates the label when the checkbox is clicked
        if state == Qt.Checked:
            self.label.setText("Inspired!")
        else:
            self.label.setText("")


class AttributeAdjuster(QWidget):
    """
    This class creates the general Attribute Adjuster that can be called on and used
    for the six different attributes in Tab 1.
    """
    def __init__(self, name: str):
        super().__init__()

        #Sets the name of the attribute to the name given
        self.name = name
        #Sets the initial value to 10
        self.value = 10

        #Main layout variable is QVBox
        main_layout = QVBoxLayout()

        #Messing with the formatting
        main_layout.setSpacing(2)
        main_layout.setContentsMargins(5,5,5,5)

        #The window's main layout is set to the main_layout variable
        self.setLayout(main_layout)

        #What the attribute name will be for the widget
        attribute_names = QLabel(self.name)
        #Can directly access this from the qss now
        attribute_names.setObjectName("AttributeTitle")

        #Setting the font of the attribute
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        attribute_names.setFont(font)

        #Aligns the label to the center
        attribute_names.setAlignment(Qt.AlignCenter)
        #Adds the label to the widget
        main_layout.addWidget(attribute_names)

        #Creates a variable of QHBox to be used for the row of buttons and label
        self.adjuster_row = QHBoxLayout()
        #Messing with format
        self.adjuster_row.setSpacing(2)

        #Creates the minus button
        self.minus_button = QPushButton('-')
        #Sets the size of the button
        self.minus_button.setFixedSize(25, 25)
        #When clicked, the number is decreased
        self.minus_button.clicked.connect(self.decrease_attribute)

        #QLabel for the modifier is created
        self.modifier_label = QLabel()

        #Setting object name to affect in the qss
        self.modifier_label.setObjectName("ModLabel")

        #Aligned to the center
        self.modifier_label.setAlignment(Qt.AlignCenter)

        #Creates the button for the plus
        self.plus_button = QPushButton('+')
        #Sets the size of the button
        self.plus_button.setFixedSize(25, 25)
        #When clicked, the number in the label is increased
        self.plus_button.clicked.connect(self.increase_attribute)

        #Adds the minus, label, and plus in a row to the adjuster_row
        for w in [self.minus_button, self.modifier_label, self.plus_button]:
            self.adjuster_row.addWidget(w)

        #Adds the adjuster row to the main layout of the widget
        main_layout.addLayout(self.adjuster_row)

        #Creates an empty label for the attribute to display
        self.attribtue_display = QLabel()

        #Sets the object name to be adjusted in the qss directly
        self.attribtue_display.setObjectName("AttributeLabel")

        #Aligns the label to the center
        self.attribtue_display.setAlignment(Qt.AlignCenter)
        #Updates the attribute
        self.update_attribute_display()
        #Adds the widget to the main layout
        main_layout.addWidget(self.attribtue_display)
        return
    
    def update_attribute_display(self):
        #This function updates the attribute display

        #This sets the label text to the value
        self.attribtue_display.setText(str(self.value))
        #The modifier value is calculated
            #For example, if an attribute for a character is 10-11, then the modifier would be 0
        modifier = (self.value - 10)//2
        #The label for the modifier is set
        self.modifier_label.setText(str(modifier))
        return
    
    def increase_attribute(self):
        #This function increases the number and updates the display
        self.value += 1
        self.update_attribute_display()
        return
    
    def decrease_attribute(self):
        #This function decreases the number and updates the display
        self.value -= 1
        self.update_attribute_display()
        return
    
    def get_modifier(self):
        #This function gets the modifier
        return (self.value - 10) // 2

class AttributeCheck(QWidget):
    """
    This class creates the check boxes for the different attributes.
    """
    def __init__(self, attr_name:str, 
                 attr_adjuster:AttributeAdjuster,
                 prof_widget):
        super().__init__()

        #Creates a variable of the proficiency widget
        self.prof_widget = prof_widget

        #takes the emmitted signal from the proficiency
        self.prof_widget.proficiency_changed.connect(self.update_all_labels)

        #Empty list that will have values appended into it
        self.checks = []

        #Creates variable of the attribute ajuster
        self.attr_adjuster = attr_adjuster

        #Sets the layout to a QVBox
        layout = QVBoxLayout()
        self.setLayout(layout)

        #NTS: number of check boxes based on the the attribute like how in ResultWidget, the second combo box has different number of options
        # when checked, the proficiency bonus should be added to the modifier that the attribute display has
        #list of tuples for the different options
        #Right now, the proficiency bonus is set at 2 and doesn't update when it is increased
        #checkboxes just do modifier + 2 and not modifier + proficiency bonus

        #This is a dictionary containing the possible skills for the main attributes
        attributes_options = {
            'STR': ['Saving Throw', 'Athletics'],
            'DEX': ['Saving Throw', 'Acrobatics','Sleight of Hand', 'Stealth'],
            'CONS': ['Saving Throw'],
            'INT': ['Saving Throw', 'Arcana', 'History', 'Investigation', 'Nature', 'Religion'],
            'WIS': ['Saving Throw', 'Animal Handling','Insight','Medicine','Perception','Survival'],
            'CHA': ['Saving Throw', 'Deception','Intimidation','Performace','Persuasion']
        }

        #Gets the corresponding skills from the attribute options
        skills = attributes_options.get(attr_name, [])

        #For formatting. It sets the number of labels in a column to 2
        fixed_row_num = 2
        #Grid layout created for easier formatting of labels
        grid_layout = QGridLayout()
        layout.addLayout(grid_layout)

        #Loop for getting the number of rows fixed
        for i, skill in enumerate(skills):
            rows = i % fixed_row_num
            cols = i // fixed_row_num

            #Checkboxes depending on what the skill is created
            checkbox = QCheckBox(skill)

            #Setting object name to directly affect object in qss
            checkbox.setObjectName("CheckboxWords")

            label = QLabel("")

            #HERE IS WHERE THE LABEL NEEDS TO BE MOVED
            #FIND OUT HOW TO MOVE IT FURTHER LEFT, AS IT STILL IS IN THE CHECKBOX
            #CHECKBOX ALSO IS NOT LIGHTING UP WHEN HOVERED OVER
            #IT SEEMS THAT THE LABEL NEEDS TO BE CLICKED AND NOT THE BOX ITSELF TO CHECK IT
            #FIX
            label.setAlignment(Qt.AlignLeft)
            label.setFixedWidth(30)

            #Function to change the state of the checkbox when checked. It updates the label
            checkbox.stateChanged.connect(partial(self.update_label, checkbox, label))

            #Adds the widgets
            grid_layout.addWidget(checkbox, rows, cols*2)
            grid_layout.addWidget(label, rows, cols*2)

            #Checks list gets the checkboxes and labels corresponding to a skill appended
            self.checks.append((checkbox, label))

    def update_label(self, checkbox, label):
        #This function updates the label of the checkbox when it is checked
        #here is probably where the proficiency needs to be looked at so that it isn't the set value
        if checkbox.isChecked():
            mod = self.attr_adjuster.get_modifier()
            #right not it seems that prof is set to 2 and doesnt update based on the proficiency label
            prof_bonus = self.prof_widget.get_prof_bonus()
            label.setText(str(mod + prof_bonus))
        else:
            label.setText("")

    def update_all_labels(self):
        # Loop through all checkboxes and update if checked
        for checkbox, label in self.checks:
            if checkbox.isChecked():
                self.update_label(checkbox, label)