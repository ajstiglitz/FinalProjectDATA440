# import lines
# widgets are all sorts of interface components
from PyQt5 import QtWidgets as qtw
import sys

from typing import Callable


class WindowWithVerticalSlots(qtw.QWidget):
    '''
    A window with a title and an empty 
    vertical container (QVBoxLayout)

    Intended use of this class is to 
    inherit and extend.
    
    This is now an object you would directly use
    '''
    def __init__(self, title: str):
        super().__init__()

        # Set the window title
        self.setWindowTitle(title)

        # Create an empty vertical layout container
        self.my_layout = qtw.QVBoxLayout(self)
        return
    