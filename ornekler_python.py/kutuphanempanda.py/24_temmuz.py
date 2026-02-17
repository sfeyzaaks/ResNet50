import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# veriler = {"günler": ["pazartesi","salı","çarşamba","perşembe","cuma","cumartesi","pazar"],
#             "ekran süresi": [2.5 , 3, 9,5,3.11,2.5,7]}
# df = pd.DataFrame(veriler)
# df.replace("," , " ")
# df.to_csv("ekransuresi.csv")

# df = pd.read_csv("ekransuresi.csv")
# ortalama = df["ekran süresi"].mean()
# print(ortalama)

# veriler = {"isimler": ["ahmet","zeynep","celal","nihal","kerem","kenan","adnan","tarık"],
#            "vize": [23,45,93,89,48,28,77,30],
#            "final": [35,57,29,97,30,70,100,93]}
# df = pd.DataFrame(veriler)


# data = {"tarih": ["2025-07-20","2025-07-21","2025-07-22","2025-07-23","2025-07-24","2025-07-25","2025-07-26"],
#         "kategori": ["ulaşım","gıda","eğlence","eğlence","gıda","ulaşım","sağlık"],
#         "ucret": [350,944,289,3492,994,2000,890]}

# df = pd.DataFrame(data)
# df.to_csv("kategoriler.csv")


# df = pd.read_csv("kategoriler.csv")
# toplam = df.groupby("kategori")["ucret"].sum()
# # print(toplam)
# # en_yuksek = df["ucret"].idxmax()
# # print(en_yuksek)

# plt.pie(toplam, labels = toplam.index)
# plt.title("kategorilere göre toplam harcama")
# plt.show()

# df = pd.read_csv("aylik_harcamalar.csv")
# df["tarih"] = pd.to_datetime(df["tarih"])
# df["ay"] = df["tarih"].dt.to_period("M")
# aylik = df.groupby("ay")["harcama"].sum()


# aylik.plot(marker = "o")
# plt.title("aylara göre harcama grafiği")
# plt.xlabel("aylar")
# plt.ylabel("harcamalar")
# plt.grid()
# plt.show()

# x = np.arange(len(aylik))
# y = aylik.values
# m , b = np.polyfit(x,y,1)
# tahmin = m*(len(aylik)) +b

# print(tahmin)

# data = {"günler": ["pazartesi","salı","çarşamba","perşembe","cuma","cumartesi","pazar"],
#         "giderler": [1200,3788,308,1038,9000,1300,780]}
# df = pd.DataFrame(data)
# df.to_csv("giderler.csv")

# df = pd.read_csv("giderler.csv")

# gunluk = df.groupby("günler")["giderler"].sum()
# siralama = gunluk.mean()
# standart = gunluk.std()

# anomali = gunluk[gunluk > siralama + 2 * standart]
# print(anomali)


# veriler = {"tarih": ["2020-07-19","2020-09-13","2020-07-19","2020-09-24","2020-07-19"],
#            "kategori": ["ulaşım","sağlık","korunma","gıda","eğlence"],
#             "harcamalar":[1200,4880,1630,1830,1900] }
# df = pd.DataFrame(veriler)
# df.to_csv("tarihli_harcamalar.csv")


# df = pd.read_csv("tarihli_harcamalar.csv")

# df["tarih"] = pd.to_datetime(df["tarih"])

# pivot = df.pivot_table(index="tarih", columns="kategori", values="harcamalar", aggfunc="sum")

# pivot.plot(kind="bar", title="günlük yapılan harcamalar")
# plt.xlabel("tarih")
# plt.ylabel("harcamalar")
# plt.show()

# data = {"malzeme": ["çelik"]*3+["aliminyum"]*3+["titanyum"]*3,
#         "kuvvet": [1000,1500,2000,500,800,1000,1200,1700,2200],
#         "uzama(mm)":[0.5, 0.7, 1.1,0.6,1.0,1.6,0.4,0.6,1.0],
#         "orijinal uzunluk(mm)": [50,50,50,50,50,50,50,50,50],
#         "kesit alanı(mm2)": [20,20,20,25,25,25,15,15,15]}

# df = pd.DataFrame(data)
# df.to_csv("malzeme_dayanim.csv")


df = pd.read_csv("malzeme_dayanim.csv")

df["gerilim"] = df["kuvvet"] / df["kesit alanı(mm2)"]
df["gerinim"]= df["uzama(mm)"] / df["orijinal uzunluk(mm)"]


for malzeme in df["malzeme"].unique():
    alt_df = df[df["malzeme"] == malzeme]
    plt.plot(alt_df["gerinim"] , alt_df["gerilim"], label = malzeme)

plt.xlabel("gerinim")
plt.ylabel("gerilim")
plt.title("dayanıklılık")
plt.grid(True)
plt.show()




