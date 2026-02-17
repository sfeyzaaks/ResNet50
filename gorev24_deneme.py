import cv2
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication , QMdiArea , QMdiSubWindow , QTextEdit, QPushButton , QLabel , QFileDialog, QHBoxLayout, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import torch

class UI(QMainWindow):
    count = 0

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("new_win.ui",self)

        self.mdi = self.findChild(QMdiArea, "mdiArea")
        self.button = self.findChild(QPushButton,"pushButton")
        self.button.clicked.connect(self.add_window)

    def add_window(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self, "derinleştirme için resim seçiniz")
        if dosya_yolu:
            UI.count += 1
            sub = QMdiSubWindow()
            pencere_icerik = QWidget()
            layout = QHBoxLayout()


            model_type = "MiDas_small"
            midas = torch.hub.load("intel-isl/MiDas", model_type)
            midas.eval()
            midas_transforms = torch.hub.load("intel-isl/MiDas", "transforms")
            transform = midas_transforms.small_transform if model_type == "MiDas_small" else midas_transforms.dpt_transform

            img = cv2.imread(dosya_yolu)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            input_batch = transform(img_rgb)

            with torch.no_grad():
                prediction = midas(input_batch)
                prediction = torch.nn.functional.interpolate(
                    prediction.unsqueeze(1),
                    size = img.shape[:2],
                    mode = "bicubic",
                    align_corners= False,
                ).squeeze()

                output = prediction.cpu().numpy()
                output_norm = cv2.normalize(output, None ,0,255, cv2.NORM_MINMAX, cv2.CV_8U)

                sonuc_yolu = f"derinlik {UI.count}.jpg"
                cv2.imwrite(sonuc_yolu, output_norm)

                lbl_orj = QLabel()
                lbl_orj.setPixmap(QPixmap(dosya_yolu).scaled(400,400))

                lbl_islenmis = QLabel()
                lbl_islenmis.setPixmap(QPixmap(sonuc_yolu).scaled(400,400))

                layout.addWidget(lbl_orj)
                layout.addWidget(lbl_islenmis)

                pencere_icerik.setLayout(layout)
                sub.setWidget(pencere_icerik)
                sub.setWindowTitle(f"Derinlik Analizi - {UI.count}")
                self.mdi.addSubWindow(sub)
                sub.show()
                self.mdi.tileSubWindows()