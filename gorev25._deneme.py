import cv2
import numpy as np
from PyQt5.QtWidgets import QMainWindow , QMdiArea, QMdiSubWindow , QPushButton,  QFileDialog , QHBoxLayout , QWidget
from PyQt5 import uic
import torch
import open3d as o3d

class UI(QMainWindow):
    count = 0
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("new_win.ui", self)
        self.mdi = self.findChild(QMdiArea , "mdiArea")
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.add_window)
        self.show()
    def add_window(self):
        dosya_yolu , _ = QFileDialog.getOpenFileName(self, "derinleştirme için resim seçiniz")
        if dosya_yolu:
            UI.count += 1
            sub = QMdiSubWindow()
            pencere_icerik = QWidget()
            layouts = QHBoxLayout()
            model_type = "MiDas_small"
            midas = torch.hub.load("intel-isl/Midas", model_type)
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
                    align_corners = False,
                ).squeeze()

                output_norm = prediction.cpu().numpy()
                output = cv2.normalize(output_norm, None, 0, 255, norm_type = cv2.NORM_MINMAX ,dtype=cv2.CV_8U)

                sonuc_yolu =f"derinlik {UI.count}.jpg"
                cv2.imwrite(sonuc_yolu, output)
                self.show_3d_model(output, img_rgb)
                return output , img_rgb
        def show_3d_model(self, depth_data, rgb_data):
            h , w = depth_data.shape
            x , y = np.meshgrid(np.arange(w), np.arange(h))
            points = np.stack((x.flatten(), y.flatten(), depth_data.flatten()), axis = 1)
            colors = rgb_data.reshape(-1, 3) / 255.0

            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(points)
            pcd.colors = o3d.utility.Vector3dVector(colors)
            pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
            o3d.visualization.draw_geometries([pcd])