
from PyQt5.QtWidgets import QMainWindow, QApplication, QMdiArea, QMdiSubWindow, QPushButton, QLabel,QFileDialog,QHBoxLayout,QWidget
from PyQt5 import uic #tasarlanılan pencereler manuel olarak kodla yazılmadan pythona aktarıldı
from PyQt5.QtGui import QPixmap
from ultralytics import YOLO
import sys
import os



class UI(QMainWindow): #miras alma, bir pencerenin sahip olması gereken bütün özellikler atandı
    count = 0  #açılan her bir pencereye numara vermek için

    def __init__(self):
        super(UI, self).__init__() #miras alınan sınıfa gidip oradaki özellikleri yükle
        uic.loadUi("new_win.ui", self)  #tasarımdaki her şey pythona yüklendi
        
        self.mdi = self.findChild(QMdiArea, "mdiArea") #çerçevemiz
        self.button = self.findChild(QPushButton, "pushButton") 
        
        self.button.clicked.connect(self.add_window)
        self.show() #bilgisayar ekranında pencereyi göster

    def model_sec(self):
        # QFileDialog ile model dosyasını seçtiriyoruz
        model_yolu, _ = QFileDialog.getOpenFileName(self, "Semantik Segmentasyon Modeli Seçin", "", "Model Dosyaları (*.pt *.onnx *.weights)")
        
        if model_yolu:
            self.secilen_model_yolu = model_yolu # Seçilen yolu bir değişkende saklıyoruz
            self.btn_model_sec.setText(os.path.basename(model_yolu))

    def add_window(self):  #çalışan asıl analiz motorumuz
        dosya_yolu , _ = QFileDialog.getOpenFileName(self, "Analiz için resim seçin")

        if dosya_yolu:  #eğer dosya yolu açıldıysa ve geçerli bir dosya yoluysa
            UI.count = UI.count + 1
            sub = QMdiSubWindow() #ana pencere içinde hareket edebilen alt pencereler oluşturuldu

            pencere_icerik = QWidget() #pencerenin içine koyulcak widgetlar için bir alan oluşturuldu (alanımız)
            layout = QHBoxLayout() #her bir nesnenin soldan sağa dizilmesi sağlandı

            model = YOLO("yolov8n-seg.pt") #segmentasyon modeli yüklendi
            
            results = model(dosya_yolu, device='cpu') 
            sonuc_yolu = "sonuc_segmentasyon.jpg"
            results[0].save(sonuc_yolu) #ilk nesne üzerinde işlem yapılıp kaydedildi, koordinat verileri, maske verileri vs.(piksel piksel)

            lbl_orj = QLabel()
            
            lbl_orj.setPixmap(QPixmap(dosya_yolu).scaled(400,400)) #scaled ile frame boyutu sabitlendi, 

            lbl_islenmis = QLabel()
            lbl_islenmis.setPixmap(QPixmap(sonuc_yolu).scaled(400,400))

            layout.addWidget(lbl_orj) #işlenmiş ve orijinal resmi yan yana ekledik
            layout.addWidget(lbl_islenmis)

            pencere_icerik.setLayout(layout) #hazırladığımız pencere içerisine layoutları ekledik
            sub.setWidget(pencere_icerik) ##pencere içeriklerini alt pencereye yerleştirdik
            sub.setWindowTitle(f"Analiz sonucu - {UI.count}") #her pencereye numara verdik

            self.mdi.addSubWindow(sub) #subwindowları mdi alanına ekledik 
            sub.show()
            self.mdi.tileSubWindows() #alt pencereleri düzenli bir şekilde yerleştirdik

if __name__ == "__main__":
    app = QApplication(sys.argv) # Uygulama nesnesini oluşturur
    pencere = UI()               # Hazırladığın arayüzü başlatır
    sys.exit(app.exec_())