import torch
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image
import requests
from io import BytesIO


weights = ResNet50_Weights.DEFAULT
model = resnet50(weights=weights)
model.eval() # Test modu

img_path = "kedi.jpeg" 
img = Image.open(img_path)

preprocess = weights.transforms() # ResNet-50 için standart ayarlar
img_transformed = preprocess(img).unsqueeze(0) # Resmi paket haline getir

# 4. MODELİ TEST ET (Tahmin Yap)
with torch.no_grad():
    prediction = model(img_transformed).squeeze(0)
    class_id = prediction.argmax().item() # En yüksek puanlı sınıfın ID'si
    category_name = weights.meta["categories"][class_id] # ID'yi kelimeye çevir

print(f"Test Sonucu: Bu resimdeki nesne bir '{category_name}'")