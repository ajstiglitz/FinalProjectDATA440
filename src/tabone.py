from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout)
from src.buttons import AttributesLoaded, ButtonsUpdateLabel
from src.diceroller import WindowCheck

#this is the assembly test for tab1 before adding it to main.py

class RollerTab(QWidget):
    """
    This class is for the complete assembly in the correct layout 
    of the different widgets to be used in Tab 1.
    """
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout()

        #at the top are the prof bonus and inspiration widget and then the dice roller widget
        left_column = QVBoxLayout()

        self.prof_bonus = ButtonsUpdateLabel()

        #splitting until we figure out issues with adjustor
        #left_column.addWidget(QLabel("ADJUSTER HERE"))
        self.attributes = AttributesLoaded(self.prof_bonus)
        left_column.addWidget(self.attributes)


        #right side of window
        right_col = QVBoxLayout()
        self.roller_widget = WindowCheck()
        right_col.addWidget(self.roller_widget)
        #Maybe have dice roll AND result of roll with modifiers
        #since nat 1 is nat 1 regardless of what you have added

        #add to main layout
        main_layout.addLayout(left_column, stretch=1)

        main_layout.addLayout(right_col, stretch=2)

        self.setLayout(main_layout)