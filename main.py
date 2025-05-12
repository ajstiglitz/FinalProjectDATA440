import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QTabWidget)

from PyQt5.QtGui import *

from src.tabone import RollerTab
from src.tabtwo import CharacterInfoTab
from src.tabthree import GraphTab

#The MainWindow which contains all of the compoments for the GUI
class MainWindow(QMainWindow):
    """
    This class creates the main window for the GUI.
    It is where all of the different components/elements will appear.
    """
    def __init__(self):
        super().__init__()

        #Sets the title of the window
        self.setWindowTitle("DiceRoller")

        self.tab_widget = QTabWidget()
        #Sets the direction of the tabs. If you wanted them at the top, change 'West' to 'North'
        #If you want them to the right, set it to 'East'
        self.tab_widget.setTabPosition(QTabWidget.West)

        self.setCentralWidget(self.tab_widget)
        self.create_tabs()

    def create_tabs(self):
        """
        This function calls the instances of the classes that have 
        all the assembled widgets for the different tabs.
        """
        #Tab 1 - for the dice roller and ability scores
        dice_roller_tab = RollerTab()
        self.tab_widget.addTab(dice_roller_tab, "Dice Roller")

        #Tab 2 - for the character sheet
        character_info_tab = CharacterInfoTab()
        self.tab_widget.addTab(character_info_tab, "Character Info")


        #Tab 3 - for the graph-creator
        grapher_tab = GraphTab()
        self.tab_widget.addTab(grapher_tab, "Grapher")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    #A qss style sheet to change how the standard GUI looks
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())