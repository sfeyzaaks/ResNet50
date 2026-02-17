import pandas as pd

# df = pd.read_csv("kullanicilar.csv")
# df


# data = {"isimler": ["ali","ayşe"],
#         "yas":[ 20,30]}
# df = pd.DataFrame(data)
# print(df)
# print(df["isimler"])
# df["şehir"]= ["istanbul","ankara"]
# print(df)

# print(df["yas"].mean())
# dem = df.sort_values("yas",ascending= False)
# print(dem)
import numpy as np
# data = {"isimler":["ayşe","mehmet","selen","mehmet"],
#          "yaş": [25,34,46,33]}
# df = pd.DataFrame(data=data,index= [1,2,3,4])
# # print(df)
# # ismim = df["isimler"]
# # print(ismim)
# df["şehirler"]= ["istanbul","ankara","istanbul","izmir"]
# # print(df[df["yaş"] > 25])
# # print(df.shape)
# # print(df.sort_values("yaş"))
# df.to_csv("veriler.csv")
import numpy as np

# df = pd.DataFrame(data)
# print(df.head(3)["isimler"])
# df = pd.DataFrame(data)
# # print(df[df["yaşlar"]>25]["isimler"])
# print(df.value_counts("isimler").head(3))

# data = {"isimler": ["ayşe","mehmet","derin","kerem","azize","kerem","ayşe","kerem"],
#         "doğum yılı": [1998,2005,1989,1967,1955,np.nan,np.nan,np.nan],
#         "cinsiyet": ["k","e","k","e","k","e","k","e"],
#         "maas":[10000,250000,45000,32000,90000,56000,23000,87000],
#         "tarih":["2007","2025","2023","2023","2018","2016","2023","2021"]}
# df = pd.DataFrame(data)
# sonuc =df.groupby("isimler").apply(lambda x : 2025- x["doğum yılı"])
# print(sonuc)
# sonuc =df.groupby("cinsiyet")["maas"].mean()
# print(sonuc)
# df["tarih"]= pd.to_datetime(df["tarih"])
# df_2023 = df[df["tarih"].dt.year==2023]
# print(df_2023)
# print(df.isnull().value_counts(normalize=True)*100)

# data = {"isimler": ["ayşe","mehmet","derin","kerem","azize","kerem","ayşe","kerem"],
#         "vize1": [24,37,98,45,99,34,76,58],
#         "final": [45,96,47,86,93,99,12,90]}
# df = pd.DataFrame(data)
# ortalama = df.groupby("isimler")[["vize1","final"]].apply(lambda x : (x["vize1"]*0.4 + x["final"]*0.6).mean())
# yuksek = ortalama.sort_values(ascending = False).head(3)
# print(yuksek)
# data = {"isimler": ["ayşe","mehmet","derin","kerem","azize","kerem","ayşe","kerem"],
#          "vize1": [24,37,98,45,99,34,76,58],
#          "final": [45,96,47,86,93,99,12,90]}

# df = pd.DataFrame(data)
# kisiler = df[df["isimler"].str.startswith("a")]["isimler"]
# sonuc = kisiler.count()
# print(sonuc)

