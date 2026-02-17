# liste = [1,2,3,4]
# print(len(liste))

# isim = "levent ertunalılar"
# print(len(isim))

class Urun:
    def __init__(self,urunkodu,urunadi,fiyati):
        self.urunkodu =urunkodu
        self.urunadi = urunadi
        self.fiyati = fiyati
    def __len__(self):
        return self.fiyati
    def __str__(self):
        return f"{self.urunkodu}, {self.urunadi}, ürün listelendi."
    def __repr__(self):
        return f"{self.urunkodu}, {self.urunadi}, ürün listelendi."
urun1 = Urun("5666637","Tv",5000)
print(len(urun1))
print(str(urun1))
print(repr(urun1))