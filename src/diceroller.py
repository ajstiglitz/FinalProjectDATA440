# actually rolling the dice
# putting in the equation for the probabilities and the velocity of the rolls
# have it here that it implemetns those equations
import sys
import time
import pygame

import random
import os

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer, QSize
from PyQt5.QtGui import QPainter, QImage

class D20DiceRoller():
    def __init__(self):
        pygame.init()
        self.game_init()


class D12DiceRoller(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        pygame.init()


class D10DiceRoller(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        pygame.init()


class D8DiceRoller(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        pygame.init()


class D6DiceRoller(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        pygame.init()


class D4DiceRoller(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        pygame.init()
