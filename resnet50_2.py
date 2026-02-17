import torch
import torchvision
import time

def hiz_testi():
    img = torch.randn(1, 3, 800, 800) #rastgele bir görüntü oluşturulur.
    
    det_model = torchvision.models.detection.fasterrcnn_resnet50_fpn(weights="DEFAULT").eval() #nesne tespiti modeli oluşturulur
    

    seg_model = torchvision.models.detection.maskrcnn_resnet50_fpn(weights="DEFAULT").eval() #segmentasyon modeli oluşturulur

    # Nesne Tespiti Süre Ölçümü
    start = time.time()
    with torch.no_grad():
        det_model(img)
    det_time = time.time() - start

    # Segmentasyon Süre Ölçümü
    start = time.time()
    with torch.no_grad():
        seg_model(img)
    seg_time = time.time() - start

    print(f"Nesne Tespiti Süresi: {det_time:.4f} sn")
    print(f"Segmentasyon Süresi: {seg_time:.4f} sn")
    print("Sonuç: Hız öncelikliyse Nesne Tespiti daha uygundur.")

hiz_testi()