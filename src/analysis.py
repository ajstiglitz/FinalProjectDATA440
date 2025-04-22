from PyQt5 import QtWidgets as qtw
import sys

from src.helpers import check_directory


from src.plots import PATH_FIGURES

PATH_DATA = 'data/'


class DiceDataAnalysis:
    '''
    Contains a data object which is a pandas DataFrame where the dice rolls are simulated
    '''

    __slots__ = ('data')

    def __init__(self):
        self.check_directories()
        return
    
    def check_directories(self) -> None:
        '''
        Making sure that any required directories already exist
        '''
        check_directory(PATH_DATA)
        return None