import sys

from PyQt5.QtWidgets import (QMainWindow, QApplication, QGridLayout, 
                             QTabWidget, QWidget, QVBoxLayout, QLabel, QComboBox,
                             QCheckBox, QLineEdit, QFormLayout, QFrame)

from PyQt5.QtCore import Qt

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
        tab1 = QWidget()
        layout_tab1 = QVBoxLayout()

        #ComboBox to select between dice
        self.dice_selector = QComboBox()
        self.dice_selector.addItems(["D20", "D12", "D10", "D8", "D6", "D4"])

        #tab setup
        tab1.setLayout(layout_tab1)
        self.tab_widget.addTab(tab1, "Dice Roller")

        #tab 2
        tab2 = QWidget()
        layout_tab2 = QVBoxLayout()
        tab2.setLayout(layout_tab2)
        self.tab_widget.addTab(tab2, "Character Info")
#        layout_tab2.addWidget()


        label2 = QLabel()
        label2.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label2.setText("TEXT TEST")
        label2.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        layout_tab2.addWidget(label2)

        label2_2 = QLabel()
        label2_2.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label2_2.setText("TESTING")
        label2_2.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        layout_tab2.addWidget(label2_2)

        label2_2_2 = QLabel()
        label2_2_2.setFrameStyle(QFrame.Panel | QFrame.Sunken)
        label2_2_2.setText("TESTING AGAIN")
        label2_2_2.setAlignment(Qt.AlignTop | Qt.AlignRight)
        layout_tab2.addWidget(label2_2_2)


        #tab 3
        tab3 = QWidget()
        layout_tab3 = QVBoxLayout()
        tab3.setLayout(layout_tab3)
        self.tab_widget.addTab(tab3, "Visualization")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    #uses a qss style sheet. Need to look online and cycle through some to see what colors look best.
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())