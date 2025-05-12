from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout, QScrollArea)
from src.buttons import AttributesLoaded, ButtonsUpdateLabel, CombinedProfInsp
from src.diceroller import WindowCheck

#This is the for tab1 before adding it to main.py

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

        #Widgets for the Proficiency and Inspiration
        self.prof_bonus = ButtonsUpdateLabel()
        #Updates label passed in so that the number of modifier + proficiency is correct
        self.prof_insp = CombinedProfInsp(self.prof_bonus)

        self.attributes = AttributesLoaded(self.prof_bonus)

        #Scrollbar so that user can see all the attributes easily in tab 1
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        #Container for the attributes. It is what the scrollbar can scroll for
        scroll_container = QWidget()
        scroll_container.setMaximumWidth(self.attributes.sizeHint().width())      

        scroll_layout = QVBoxLayout(scroll_container)
        scroll_layout.addWidget(self.attributes)
        scroll_area.setWidget(scroll_container)

        left_column.addWidget(scroll_area)

        #Right side of window
        right_col = QVBoxLayout()
        self.roller_widget = WindowCheck()
        right_col.addWidget(self.prof_insp)
        right_col.addWidget(self.roller_widget)
        #Maybe have dice roll AND result of roll with modifiers
        #since nat 1 is nat 1 regardless of what you have added

        #Add to main layout
        main_layout.addLayout(left_column, stretch=1)
        main_layout.addLayout(right_col, stretch=2)

        self.setLayout(main_layout)