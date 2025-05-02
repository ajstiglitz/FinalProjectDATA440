import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QMainWindow, QApplication,
                             QLineEdit, QHBoxLayout, QVBoxLayout)
from src.buttons import CombinedProfInsp
from src.diceroller import WindowCheck

#this is the assembly test for tab1 before adding it to main.py

class RollerTab(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()

        #at the top are the prof bonus and inspiration widget and then the dice roller widget
        top_row_layout = QHBoxLayout()

        self.prof_insp_widget = CombinedProfInsp()
        top_row_layout.addWidget(self.prof_insp_widget)

        #dice roller widget and result added here
        self.roller_widget = WindowCheck()
        top_row_layout.addWidget(self.roller_widget)
        #Maybe have dice roll AND result of roll with modifiers
        #since nat 1 is nat 1 regardless of what you have added


        main_layout.addLayout(top_row_layout)


        #bottom layout here.
        # Should include the attribute adjuster and roll result widgets.
        #attribute adjuster needs to be fixed to have the check marks

        bottom_row_layout = QHBoxLayout()
        #self.result_widget = ResultWidget()
        #bottom_row_layout.addWidget(self.result_widget)

        main_layout.addLayout(bottom_row_layout)


        central_widget.setLayout(main_layout)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RollerTab()
    window.show()

    #uses a qss style sheet. Need to look online and cycle through some to see what colors look best.
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())