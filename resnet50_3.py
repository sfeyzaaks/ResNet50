import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weights
from PIL import Image
import torchvision.transforms as T

weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT #modelin eğitildiği ağırlıklar indirildi
model = fasterrcnn_resnet50_fpn(weights=weights) #model oluşturuldu ve ağırlıklar yüklendi
model.eval()


img = Image.open("kedi.jpeg").convert("RGB") #resnet50 rgb formatında resim beklediği için rgb formatına dönüştürülür
transform = T.Compose([T.ToTensor()]) #
img_tensor = transform(img).unsqueeze(0)


with torch.no_grad():
    prediction = model(img_tensor)

tahmin_kutu = prediction[0]['boxes'][0].tolist() # [x1, y1, x2, y2]


gercek_kutu = [50, 45, 160, 155] 

def iou_hesapla(boxA, boxB):
    xA = max(boxA[0], boxB[0]); yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2]); yB = min(boxA[3], boxB[3])
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
    boxAArea = (boxA[2]-boxA[0]+1)*(boxA[3]-boxA[1]+1)
    boxBArea = (boxB[2]-boxB[0]+1)*(boxB[3]-boxB[1]+1)
    return interArea / float(boxAArea + boxBArea - interArea)

hassasiyet = iou_hesapla(tahmin_kutu, gercek_kutu)
print(f"ResNet-50 Tahmin Hassasiyeti (IoU): %{hassasiyet*100:.2f}")