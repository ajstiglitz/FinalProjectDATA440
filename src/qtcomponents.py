from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QTextEdit,
                             QPushButton, QFileDialog, QHBoxLayout)
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QPixmap

#All of these components are Tab 2-specific
class LabelTextEditWidget(QWidget):
    """
    General Template class for a Widget with a QLabel and QTextEditor.
    """
    def __init__(self, label_text="Label"):
        super().__init__()

        #Sets the layout as a QVBox, so that the widgets are vertical
        layout = QVBoxLayout()
        self.label = QLabel(label_text)
        self.text_edit = QTextEdit()

        #Components added in this order so that the label is above the text editor
        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)

        #Makes sure that the 
        self.setLayout(layout)

# *Check README Links to resources section*
class PhotoLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
        QLabel {
            border: 4px dashed #aaa;
        }''')
        #Sets the height and width of the image
        self.fixed_height = 400
        self.fixed_width = 400
        self.setFixedSize(self.fixed_width, self.fixed_height)

    def setPixmap(self, pixmap):
        #This function sets the pixmap (image) and scales it for the interface
        scaled_pixmap = pixmap.scaled(
            self.fixed_width,
            self.fixed_height,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        super().setPixmap(scaled_pixmap)
        self.setStyleSheet('''
        QLabel {
            border: none;
        }''')

class ImageUploadWidget(QWidget):
    """
    This class has the implementation to upload an image from your computer.
    """
    def __init__(self):
        super().__init__()

        self.photo = PhotoLabel()
        self.button = QPushButton('Browse')
        self.button.clicked.connect(self.open_image)
        self.appearance_label = QLabel('Appearance')

        layout = QVBoxLayout()
        layout.addWidget(self.photo)
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.appearance_label)
        h_layout.addWidget(self.button)
        layout.addLayout(h_layout)
        
        self.setLayout(layout)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        #This function is for the implementation of dragging an image to be used
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        #This function is for the implementation of dropping an image and accepting it
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            filename = event.mimeData().urls()[0].toLocalFile()
            event.accept()
            self.open_image(filename)
        else:
            event.ignore()

    def open_image(self, filename=None):
        #This function is for the implementation of being able to go into the computer folders to choose an image manually
        if not filename:
            filename, _ = QFileDialog.getOpenFileName(self, 'Select Photo', QDir.currentPath(), 'Images (*.png *.jpg)')
            if not filename:
                return
        self.photo.setPixmap(QPixmap(filename))