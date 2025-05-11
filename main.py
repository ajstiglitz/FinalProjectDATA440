import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel,
                             QTabWidget, QWidget, QHBoxLayout)

from PyQt5.QtGui import *

from src.tabtwotest import CharacterInfoTab
from src.tabonetest import RollerTab
from src.tabthreetest import GraphTab


#from qtcomponents import WindowWithVerticalSlots

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DiceRoller")

        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.West)

        self.setCentralWidget(self.tab_widget)
        self.create_tabs()

    def create_tabs(self):
        #tab 1 - for the dice roller and ability scores
        dice_roller_tab = RollerTab()
        self.tab_widget.addTab(dice_roller_tab, "Dice Roller")

        #tab 2
        character_info_tab = CharacterInfoTab()
        self.tab_widget.addTab(character_info_tab, "Character Info")


        #tab 3
        grapher_tab = GraphTab()
        self.tab_widget.addTab(grapher_tab, "Grapher")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    #uses a qss style sheet. Need to look online and cycle through some to see what colors look best.
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())