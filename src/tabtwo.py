from PyQt5.QtWidgets import (QWidget, QLabel,
                             QLineEdit, QHBoxLayout, QVBoxLayout)
from src.qtcomponents import LabelTextEditWidget, ImageUploadWidget

class CharacterInfoTab(QWidget):
    """
    This class is for the complete assembly in the correct layout 
    of the different widgets to be used in Tab 2.
    """
    def __init__(self):
        super().__init__()

        #Main layout is vertical
        main_layout = QVBoxLayout()

        # At the top are character details like name, race, class, etc.
        top_row_layout = QHBoxLayout()
        #Names that the labels will use
        labels = ["Name", "Class", "Race", "Alignment", "Level", "Age"]
        self.line_edits = {}

        for label_text in labels:
            #Container for the label widget and text editor is a vertical layout
            container = QVBoxLayout()
            #Creates the label with the label names
            label = QLabel(label_text)
            #Creates the text box widget
            edit = QLineEdit()
            #Adds the label to the layout
            container.addWidget(label)
            #Adds the text editor to the layout
            container.addWidget(edit)
            #Adds the container layout to the layout for the top of the tab
            top_row_layout.addLayout(container)
            self.line_edits[label_text] = edit

        #Main layout has the top row layout added
        main_layout.addLayout(top_row_layout)

        #Layout for the widgets for the middle of the window
        middle_layout = QHBoxLayout()

        #Left widget: Image Upload
        self.image_upload_widget = ImageUploadWidget()
        middle_layout.addWidget(self.image_upload_widget, 1)

        #Right widget: Features
        self.features_widget = LabelTextEditWidget("Features & Traits")
        middle_layout.addWidget(self.features_widget, 2)

        #Main layout has the middle layout added
        main_layout.addLayout(middle_layout)

        #At the bottom are the widgets for the inventory and proficiencies a character may have
        bottom_layout = QHBoxLayout()
        self.traits_widget = LabelTextEditWidget("Inventory")
        self.notes_widget = LabelTextEditWidget("Other Proficiencies & Languages")

        #Widgets added to the bottom layout
        bottom_layout.addWidget(self.traits_widget)
        bottom_layout.addWidget(self.notes_widget)

        #Bottom layout added to the main layout
        main_layout.addLayout(bottom_layout)

        #Layout set so that the widgets appear
        self.setLayout(main_layout)