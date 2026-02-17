import cv2
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QApplication
from ultralytics import YOLO
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import uic
import sys

class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("kamera_arayuz2.ui", self)
        self.model = YOLO("yolov8n.pt")
        self.button1 = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.label = self.findChild(QLabel, "label_camera")
        self.timer = QTimer()

        self.timer.timeout.connect(self.update_frame)
        self.button1.clicked.connect(self.start_cam)
        self.button2.clicked.connect(self.stop_cam)
        self.show()

    def start_cam(self):
        self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            self.timer.start(30)

    def stop_cam(self):
        self.timer.stop()
        if hasattr(self, "cap"):
            self.cap.release()
        self.label.clear()


    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            results = self.model(frame)
            kullanilmis = results[0].plot()
            rgb_img = cv2.cvtColor(kullanilmis, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_img.shape
            bytes_per_line = ch*w

            convert_Qt = QImage(rgb_img.data, w,h, bytes_per_line, QImage.Format_RGB888)
            p = convert_Qt.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)

            self.label.setPixmapmap(QPixmap.fromImage(p))

if __name__ == "__main__": #programın ana kısmı
    app = QApplication(sys.argv) #uygulama başlatıldı
    window = UI() 
    sys.exit(app.exec_()) 
    




