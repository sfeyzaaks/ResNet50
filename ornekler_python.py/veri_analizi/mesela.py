# import numpy as np
# a = np.array([1,2,3])
# print(a)
# import numpy
# n
# import numpy as np
# result = np.array([[3,85,78,100], [1,2,4,2]])
# print(result)
# print(np.zeros(6))
# print(np.linspace(1,98,5))
# print(np.random.randint(5))
# listem = np.array([[1,3,4,25,5],[46,57,4,8,2]])
# result = listem.reshape(3,7)
# print(result)

# listem = np.array([45,33,98,467])
# # result = listem.mean()
# # print(result)
# result = listem.shape
# print(result)


# vize = np.array([70,80,90,60,50])
# final = np.array([80,85,70,65,55])
# ortalama = vize * 0.4 + final * 0.6
# durum = np.where(ortalama >= 60 , "geçti", "kaldı")
# print(ortalama , durum)

# vize = [70,80,90,60,50]
# final = [80,85,70,65,55]
# ortalama = []
# durum = []
# for i in range(len(vize)):
#     ort = vize[i]* 0.4 + final[i] * 0.6
#     ortalama.append(ort)
#     if ort >= 60:
#         durum.append("geçti")
#     else:
#         durum.append("kaldı")
# print(ortalama, durum)


# vize = np.array([70,80,90,60,50])
# final = np.array([80,85,70,65,55])
# ortalama = vize * 0.4 + final * 0.6
# listem = np.where(ortalama >= 60 , "geçti", "kaldı")
# print(ortalama)


# zar = np.random.randint(1,7, size = 1000)
# deger , tekrar = np.unique(zar ,return_counts=True )
# print("en çok gelen sayı :" ,np.bincount())

# a = np.arange(12).reshape((3,4))
# print(a)

# sicaklik = np.random.randint(18,36, size = 30)
# ortalama = sicaklik.mean()
# buyuk = sicaklik.argmax()

# print(ortalama)
# print(buyuk)

# veri = np.array([10,12,15,1000,14,13,11])
# temiz_veri = np.clip(veri, 10,20)
# print(veri)
# print(temiz_veri)

# veriler = np.random.randint(0,101, size = 100)
# ortalama = np.mean(veriler)
# durum = np.where(veriler >= 60 , "geçti", "kaldı")
# buyuk = np.max(veriler)
# kucuk = np.min(veriler)
# print(durum)
# print(ortalama)
# print(buyuk)
# print(kucuk)

# import csv
# import numpy as np
# baslik = ["NUMARA","NOT","DURUM"]
# with open("notlar.csv", "w", encoding = "utf-8", newline = "") as file:
    
#     ogrenciler = np.random.randint(0,101,size = 100)
   
#     durum = np.where(ogrenciler >= 50, "geçti","kaldı")
#     csv_writer = csv.DictWriter(file, fieldnames= baslik )
#     csv_writer.writeheader()
#     for i , ( not_ , dr) in enumerate(zip(ogrenciler,durum,start=1)):
#         csv_writer.writerow({"NUMARA": i , 
#                              "NOT": not_}, 
#                              "DURUM": dr})
# import csv
# import numpy as np
# basliklar =["numara","devamsizlik","durum"]
# isimler = ["ali","ayşe","mehmet","selim","tekin","selin","kardelen"]
# with open("rapor.csv","w",encoding= "utf-8",newline = "") as file:
#     devamsizliklar = np.random.randint(0,15,size = 7)
#     durum = np.where(devamsizliklar > 10, "kaldı", "geçti")
#     csv_writer = csv.DictWriter(file, fiealdnames = basliklar)
#     for i , devam, secim in enumerate(zip(devamsizliklar,durum)):
#         csv_writer.writerow(i, devam, secim)


# import csv
# import numpy as np
# with open("ogrenciler.csv","w",newline ="", encoding = "utf-8") as file:
#     vize1 = np.random.randint(0,101,size = 10)
#     vize2 = np.random.randint(0,101,size= 10)
#     ortalama = vize1 * 0.4 + vize2 * 0.6
#     for i in ortalama:
#         durum = []
#         if ortalama >= 85 :
#             durum.append("takdir")
#         elif 70<ortalama<85 :
#             durum.append("teşekkür")
#         else:
#             durum.append("geçti")
#     obje = enumerate(ortalama)
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(durum)



# import csv
# import numpy as np

# with open("notlar.csv","w", newline = "", encoding = "utf-8") as file:
#     vize = np.random.randint(0,101,size = 100)
#     final = np.random.randint(0,101,size = 100)
#     ortalama = vize * 0.4 + final * 0.6
#     ortalamam = np.mean(ortalama)
#     durum = np.where(ortalama >= 85 , "takdir", 
#                      np.where(ortalama >=70, "teşekkür", 
#                               np.where(ortalama >= 50 "geçti", "kaldı")))

#     buyuk = np.max(ortalama)
#     kucuk = np.min(ortalama)
#     obje = enumerate(zip(vize, final , ortalama,durum))
    
#     csv_writer = csv.writer(file)
#     csv_writer.writerow(["numara","vize","final","oratalama","durum"])
#     for i,a,b,c,d in obje:
#         csv_writer.writerow(i,a,b,c,d)



    



