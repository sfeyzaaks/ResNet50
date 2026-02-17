from PyQt5.QtWidgets import *
from login_python import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from anapencere import AnaPencerePage
class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.anapencereac = AnaPencerePage()
        self.loginform.pushButton.clicked.connect(self.GirisYap)
    def GirisYap(self):
        k_adi = self.loginform.lineEdit_kullaniciadi.text()
        sifre = self.loginform.lineEdit_sifre.text()
        if k_adi == "feyza" and sifre == "12345":
            self.anapencereac.show()
            