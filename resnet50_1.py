import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weights
from PIL import Image
import torchvision.transforms as T
import matplotlib.pyplot as plt
import matplotlib.patches as patches

weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT #model ve ağırlıklar yüklendi
model = fasterrcnn_resnet50_fpn(weights=weights)
model.eval()


img_path = "kedi.jpeg" 
img = Image.open(img_path).convert("RGB") #rgb formatına dönüştürülür
transform = T.Compose([T.ToTensor()])
img_tensor = transform(img).unsqueeze(0)

with torch.no_grad(): #tahmin yapılır
    prediction = model(img_tensor)


tahmin_kutu = prediction[0]['boxes'][0].tolist() #en yüksek güvene sahip tahmin kutusu alınır


gercek_kutu = [50, 45, 160, 155] 

#IoU hesaplanır
def iou(boxA, boxB):
    xA = max(boxA[0], boxB[0]); yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2]); yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    boxAArea = (boxA[2]-boxA[0]+1)*(boxA[3]-boxA[1]+1)
    boxBArea = (boxB[2]-boxB[0]+1)*(boxB[3]-boxB[1]+1)
    return interArea / float(boxAArea + boxBArea - interArea)

hassasiyet = iou(tahmin_kutu, gercek_kutu)

# 6. GÖRSELLEŞTİRME (Raporun için en önemli kısım)
fig, ax = plt.subplots(1, figsize=(10, 6))
ax.imshow(img)

#tahmin kutusu çizilir (kırmızı)
rect_tahmin = patches.Rectangle((tahmin_kutu[0], tahmin_kutu[1]), 
                                 tahmin_kutu[2]-tahmin_kutu[0], 
                                 tahmin_kutu[3]-tahmin_kutu[1], 
                                 linewidth=2, edgecolor='r', facecolor='none', label=f'ResNet-50 Tahmin (IoU: %{hassasiyet*100:.2f})')

#gerçek kutu çizilir (yeşil)
rect_gercek = patches.Rectangle((gercek_kutu[0], gercek_kutu[1]), 
                                 gercek_kutu[2]-gercek_kutu[0], 
                                 gercek_kutu[3]-gercek_kutu[1], 
                                 linewidth=2, edgecolor='g', facecolor='none', label='Gerçek Sınır')

ax.add_patch(rect_tahmin)
ax.add_patch(rect_gercek)
plt.title(f"ResNet-50 Nesne Tespiti Analizi  %{hassasiyet*100:.2f}")
plt.legend()
# Görseli proje klasörüne kaydeder
plt.savefig("resnet50_analiz_sonucu.png")
plt.show()