from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiArea, QMdiSubWindow, QTextEdit, QPushButton, QLabel, QFileDialog, QHBoxLayout, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from ultralytics import YOLO

class UI(QMainWindow):
    count = 0

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("new_win.ui", self)
        self.mdi = self.findChild(QMdiArea, "MDI_AREA")
        self.button = self.findChild(QPushButton , "PUSH BUTTON")
        self.button.clicked.connect(self.add_window)
        self.show()

    def add_window(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self, "analiz için resim seçiniz")
        if dosya_yolu:
            UI.count += 1
            sub = QMdiSubWindow()
            pencere_icerik = QWidget()
            layout = QHBoxLayout()

            model = YOLO("yolov8n-seg.pt")
            results = model(dosya_yolu, device = "cpu")
            sonuc = "sonuc_segmentasyon.jpg"
            results[0].save(sonuc)

            label_orj = QLabel()
            label_orj.setPixmap(QPixmap(sonuc).scaled(300,400))

            label_islenmis = QLabel()
            label_islenmis.setPixmap(QPixmap(sonuc).scaled(300,400))
            layout.addWidget(label_orj)
            layout.addWidget(label_islenmis)

            pencere_icerik.setLayout(layout)
            sub.setWidget(pencere_icerik)
            sub.setWindowTitle(f"analiz sonucu {UI.count}")

            self.mdi.addSubWindow(sub)
            sub.show()
            self.mdi.tileSubWindows()