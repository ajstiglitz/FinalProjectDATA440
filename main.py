#from src.interfaceTest import main
#from pathlib import Path
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)
from src.qtcomponents import LabelTextEditWidget
from src.qtcomponents import ImageUploadWidget

#Class for the main window. All I have so far is the window which should actually be in the second tab.
#Need to digure out how to do that...
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Character Sheet")
        self.setGeometry(100, 100, 800, 600)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # At the top are character details like name, race, class, etc.
        top_row_layout = QHBoxLayout()
        labels = ["Name", "Class", "Race", "Alignment", "Level", "Age"]
        self.line_edits = {}

        for label_text in labels:
            container = QVBoxLayout()
            label = QLabel(label_text)
            edit = QLineEdit()
            container.addWidget(label)
            container.addWidget(edit)
            top_row_layout.addLayout(container)
            self.line_edits[label_text] = edit

        main_layout.addLayout(top_row_layout)

        # widgets for the middle of the window. Are the image of character and the features
        middle_layout = QHBoxLayout()

        # Left widget: Image Upload
        self.image_upload_widget = ImageUploadWidget()
        middle_layout.addWidget(self.image_upload_widget, 1)

        # Right widget: Features
        self.features_widget = LabelTextEditWidget("Features & Traits")
        middle_layout.addWidget(self.features_widget, 2)

        main_layout.addLayout(middle_layout)

        # at the bottom are the widgets for the inventory and proficiencies a character may have
        bottom_layout = QHBoxLayout()
        self.traits_widget = LabelTextEditWidget("Inventory")
        self.notes_widget = LabelTextEditWidget("Other Proficiencies & Languages")

        bottom_layout.addWidget(self.traits_widget)
        bottom_layout.addWidget(self.notes_widget)

        main_layout.addLayout(bottom_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    #uses a qss style sheet. Need to look online and cycle through some to see what colors look best.
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())