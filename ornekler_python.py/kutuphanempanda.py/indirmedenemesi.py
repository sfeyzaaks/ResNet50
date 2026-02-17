import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# harcamalar = [{"harcamalar": 1200 , "tarih": "2025-07-10" , "kategori": "gıda"},
#               {"harcamalar":2500 , "tarih": "2025-07-11" , "kategori": "aletler"}, 
#               {"harcamalar":900, "tarih": "2025-07-12", "kategori": "temizlik"} , 
#               {"harcamalar": 650 , "tarih": "2025-07-14", "kategori": "giyim"}]
# baslik = ["harcamalar","tarih","kategori"]
# with open("marketim_harcamalarım.csv", "w", encoding = "utf-8", newline="") as file:
#     csv_writer = csv.DictWriter(file,fieldnames=baslik)
#     csv_writer.writeheader()
#     csv_writer.writerows(harcamalar)

# df = pd.read_csv("marketim_harcamalarım.csv")
# toplam_harcama = df["harcamalar"].sum()
# en_cok = df.groupby("kategori")["harcamalar"].idxmax()

# print(en_cok)




# data = [{"tarih": "2025-07-10" , "sicaklik": 34.5},
#         {"tarih": "2025-07-11", "sicaklik": 35.2},
#         {"tarih": "2025-07-12", "sicaklik": 33.8},
#         {"tarih": "2025-07-13", "sicaklik": 36.1},
#         {"tarih": "2025-07-14", "sicaklik": 32.7}]
# headers = ["tarih", "sicaklik"]
# with open("sicaklik.csv", "w", newline="", encoding="utf-8") as file:
#     csv_writer = csv.DictWriter(file, fieldnames= headers)
#     csv_writer.writeheader()
#     csv_writer.writerows(data)

# df = pd.read_csv("sicaklik.csv")
# sicaklik = df["sicaklik"].values

# en_buyuk = df[df["sicaklik"] > 35]
# df["tarih"] = pd.to_datetime(df["tarih"])

# plt.plot(df["tarih"], df["sicaklik"], marker = "o")
# plt.show()




# data = {"günler":["pazartesi","salı","çarşamba","perşembe","cuma","cumartesi","pazar"],
#         "adım sayısı": [1200,3500,9470,6777,9874,2748,8900]}

# df = pd.DataFrame(data)
# df.to_csv("adimlar.csv")

# ortalama_adim = df["adım sayısı"].mean()

# deger = df["adım sayısı"].values
# toplam_adim = np.sum(deger)
# print(toplam_adim)

# plt.bar(df["günler"],df["adım sayısı"])
# plt.show()



# data = { "günler": ["pazartesi", "salı", "çarşamba","perşembe","cuma","cumartesi","pazar"],
#         "okunan sayfa": [120,np.nan,25,489,928,12,192]}
# df = pd.DataFrame(data)
# df.to_csv("okunan_sayfa.csv")

# toplam_okunan = df["okunan sayfa"].sum()
# en_cok_okunan = df.groupby("günler")["okunan sayfa"].idxmax()
# ortalama = df["okunan sayfa"].mean()

# print(toplam_okunan)
# print(en_cok_okunan)
# print(ortalama)


# plt.xlabel("günler")
# plt.ylabel("okunan sayfa")
# plt.plot(df["günler"], df["okunan sayfa"])
# plt.show()


# data = { "günler": ["pazartesi", "salı", "çarşamba","perşembe","cuma","cumartesi","pazar"],
#         "kahve sayısı": [1,4,2,4,3,2,0]}
# df = pd.DataFrame(data)
# df.to_csv("kahve_sayisi.csv" , index=False)

# toplam = df["kahve sayısı"].sum()
# ortalama = df["kahve sayısı"].mean()
# deger = df["kahve sayısı"].idxmax()
# en_yuksek = df.loc[deger , "günler"]

# x = df["günler"]
# y = df["kahve sayısı"]
# plt.plot(x,y, label = "kahve sayısı")
# plt.xlabel("günler")
# plt.ylabel("kahve sayısı")
# plt.title("haftalık kahve tüketimi")
# plt.legend()
# plt.show()




