from PyQt5.QtWidgets import *
from anapencere_python import  Ui_MainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

class AnaPencerePage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.AnaPencereform = Ui_MainWindow()
        self.AnaPencereform.setupUi(self)
        