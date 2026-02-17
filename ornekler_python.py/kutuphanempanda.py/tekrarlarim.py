import csv

import numpy as np
import random
# data = [{"isim":"zeynep", "vize": 69 , "final": 55},
#         {"isim": "kerem", "vize": 78, "final": 89},
#         {"isim": "taner" , "vize": 100, "final":76}]
# basliklar = ["isim","vize","final"]
# with open("ogrenciler.csv", "w", newline="", encoding = "utf-8") as file:
#     csv_writer = csv.DictWriter(file, fieldnames=basliklar )
#     csv_writer.writeheader()
#     csv_writer.writerows(data)

# print("başarıyla yazıldı")


# print(np.random.randint(0,55))

# listem = np.random.randint(0,10,(3,3)) 
# print(listem)

# numbers = np.array([10,20,30,40,50])
# sonuc = np.mean(numbers)
# print(sonuc)
# dizi = np.array([12,45,7,30,22,5,18])
# filterli = dizi[dizi>20]

# dizi = np.array([12,7,9,14,22,31,40,3])
# ciftler = dizi[dizi % 2 == 0 ]
# tekler = dizi[dizi % 2 != 0 ]
# print(ciftler)
# print(tekler)

# dizi = np.arange(16)
# sonuc = dizi.reshape(4,4)
# print(sonuc)

# matris = np.array([[2,4,6],
#                    [1,3,5],
#                    [7,8,9]])
# sonuc =

# dizi = np.array([4,18,9,27,14,6])
# sonuc =np.argmax(dizi)
# print(sonuc)

# data = [{"isim": "ahmet", "yaş": 25, "şehir": "istanbul"},
#         {"isim": "ayşe", "yaş": 30, "şehir": "ankara"},
#         {"isim": "mehmet", "yaş": 22, "şehir": "izmir"}]
# df = pd.DataFrame(data)
# ortalama = df["yaş"].mean()
import pandas as pd
import time
# data = {"isim": ["kerem","kerem","mehmet","ayşe","mehmet","tolga"],
#         "yaş": [27,31,11,37,43,33]}
# df = pd.DataFrame(data)
# sonuc= df.groupby("isim")["yaş"].mean()
# print(sonuc)

# data = { "tarih": ["01-05-2025","31-09-2005","12-11-2023","06-07-2023"]}
# df = pd.DataFrame(data)
# sonuc = pd.to_datetime(df)
# print(sonuc)

# data = { "maas": [10000,15000,45000,98000,34000]}
# df = pd.DataFrame(data)
# df["maaş kategori"] = df["maas"].apply(lambda x : "yüksek" if x >20000  )
# print(df)

import numpy as np
import pandas as pd
import random

# sayi = np.arange(0,20,2)
# print(sayi)

# sayi = np.array([[1,2,3],
#                  [4,5,6]])
# karesi = sayi ** 2
# print(karesi)
# sayi = np.array([5,10,15,20,25,30])
# ortalama = np.mean(sayi)
# medyan = np.median(sayi)
# sapma = np.std(sayi)

# sayi = np.array([3,14,7,25,9,18])
# sonuc = sayi[sayi > 10]
# print(sonuc)

# dizi = np.random.randint(0,100,size=10)
# sonuc = np.max(dizi)
# print(sonuc)

# dizi = np.random.randint(0,100,(4,4))
# satir = np.sum(dizi, axis=1)
# sutun = np.sum(dizi, axis=0)
# print(satir)
# print(sutun)
# a = np.array([1,2,3,5,2,3,1,4,5,3,5,3])
# deger , tekrar = np.unique(a, return_counts=True)
# print(deger)
# print(tekrar)

# dizi = np.random.randint(0,100,size=15)
# sonuc = np.sort(dizi)
# print(sonuc)

# a = np.random.randint(0,100,(10,10))
# sonuc = ( (a - a.min())/ (a.max()- a.min()))
# print(sonuc)

# vize =np.random.randint(0,101,size=20)
# final = np.random.randint(0,101,size=20)
# ortalama = vize* 0.4 + final * 0.6
# sonuc = np.where(ortalama >60, "geçti", "kaldı")
# gecen = np.sum(ortalama >60)
# kalan = np.sum(ortalama<=60)

# print(sonuc)
# print(gecen)
# print(kalan)

# sicaklik = np.random.randint(5,34,size=24)
# yuksek = np.max(sicaklik)
# dusuk = np.min(sicaklik)
# ortalama = np.mean(sicaklik)
# toplam = np.sum(sicaklik>30)
# print(ortalama)
# print(yuksek, dusuk)
# print(toplam)


# zar1 = np.random.randint(1,7,size=1000)
# zar2= np.random.randint(1,7,size=1000)
# sonuc = zar1 + zar2
# deger , tekrar = np.unique(sonuc , return_counts=True)
# en_cok_gelen = deger[np.argmax(tekrar)]
# kackez= np.sum(sonuc == 7 )
# toplam = np.sum(kackez)
# print(kackez)



# dizi = np.random.randint(0,100,(10,10))
# normalized = ((dizi - dizi.min())/ (dizi.max()- dizi.min()))
# ort = np.mean(normalized)
# print(normalized)
# print(ort)

# puan = np.random.randint(0,101,size=30)
# gruplar = np.where(puan<50, "kötü", 
#                    np.where(puan<75, "orta","iyi"))
# iyi = np.sum(gruplar == "iyi")
# orta = np.sum(gruplar == "orta")
# kotu = np.sum(gruplar == "kötü")
# print(gruplar)
# print(iyi, orta, kotu)

# urun_miktari = np.random.randint(4,70,size=50)
# siparis = np.random.randint(0,5,size=50)
# kalan_urun = urun_miktari - siparis

# tukenen = np.where(kalan_urun == 0)[0]
# a = np.argsort(kalan_urun[tukenen])

# print(a)
import pandas as pd
import numpy as np
import csv
# data = { "isimler": ["ali", "ayşe"],
#         "yaş": [25,31]}
# df = pd.DataFrame(data)
# ortalama = df["yaş"].mean()
# df["maaş"] = [5000,6000]
# yasa = df["yaş"].sort_values(ascending=True)
# print(yasa)

# data = [{"isim":"zeynep","soyad":"aksoy","yas":25,"maas":8000,"cinsiyet":"k"},
#          {"isim": "mehmet","soyad":"teker","yas":34,"maas":5600 ,"cinsiyet": "e"},
#          {"isim":"mahmut","soyad":"akan","yas":23,"maas":7000 , "cinsiyet":"e"},
#          {"isim":"utku","soyad":"uçar","yas":17,"maas":2300, "cinsiyet":"e"}]
# headers = ["isim","soyad","yas","maas","cinsiyet"]
# with open("data.csv","w",newline="",encoding="utf-8") as file:
#      csv_writer = csv.DictWriter(file, fieldnames=headers)
#      csv_writer.writeheader()
#      csv_writer.writerows(data)

# print("başarıyla gerçekleştirildi")
# data = [{"maas":7000 , "cinsiyet":"k"},
#         {"maas":8000,"cinsiyet":"e"},
#         {"maas":5600 ,"cinsiyet": "e"},
#         {"maas":2300, "cinsiyet":"e"}]
# basliklar = ["maas","cinsiyet"]
# with open("datamm.csv", "a",newline="", encoding="utf-8") as file:
#     csv_writer = csv.DictWriter(file,fieldnames=basliklar)
#     csv_writer.writeheader()
#     csv_writer.writerows(data)



# with open("data.csv","r",encoding="utf-8") as file:
#      csv_reader = csv.reader(file)
#      for f in csv_reader:
#           print(f)
# import time
# import pandas as pd
# # df = pd.read_csv("data.csv")
# # cinsiyet = df["cinsiyet"].value_counts()
# # #print(cinsiyet)
# # df["tarih"]= ["12/5/2005","31/9/1998","12/9/1908","2/8/2003"]
# # df.to_csv("data.csv",index=False)

# # df["tarih"]= pd.to_datetime(df["tarih"], dayfirst=True,errors="coerce")

# # sonuc = df.isnull()
# # df["tarih"]= df["tarih"].fillna("31/07/1998")
# # print(df["tarih"])

# # data = {"isim":["zeynep","mehmet","karaca","mercan"],
# #         "yas":[23,45,34,22]}
# # df = pd.DataFrame(data)
# # def yasgrubu(yas):
# #     if yas<25:
# #         return "genç"
# #     elif yas<35:
# #         return "orta"
# #     else:
# #         return "yaşlı"
# # df["yaş grubu"]= df["yas"].apply(yasgrubu)
# # print(df)
# data = [{"isim":"zeynep","vize":56,"final":98},
#         {"isim":"talat","vize":78,"final":45},
#         {"isim":"yaren","vize":98,"final":44}]
# headers = ["isim","vize","final"]
# with open("ogrenciler.csv","w",newline="",encoding="utf-8") as file:
#     csv_writer = csv.DictWriter(file,fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerows(data)

# df = pd.read_csv("ogrenciler.csv")
# df["ortalama"]= df["vize"]*0.4 + df["final"]*0.6
# def calculate(ortalama):
    
#     if ortalama < 40:
#         return "cc"
#     elif ortalama <60:
#         return "bb"
#     else:
#         return "aa"
# df["sonuç"]= df["ortalama"].apply(calculate)
# print(df)
