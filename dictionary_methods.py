# arabaaudi = {
#     "marka" : "audi",
#     "model" : "A5",
#     "yil" : 2019,
# }
# sonuc = arabaaudi["marka"]
# sonuc = arabaaudi.get("marka")
# sonuc = "marka2" in arabaaudi
# print(len(arabaaudi))
# sonuc = len(arabaaudi)
# print(sonuc)
# arabaaudi["renk"] = "siyah"
# print(arabaaudi)
# arabaaudi.pop("yil") #yil elemanını siler
# arabaaudi.popitem() #sondaki elemanı siler
# del arabaaudi["marka"]
# del arabaaudi #objeyi tamamen siler
# arabaaudi.clear() #içerisindeki değerlerin hepsini siler
# araba = arabaaudi.copy()
# araba["marka"] = "mercedes"
# arabaaudi.update({
#     "marka": "BMW",
#     "renk" : "beyaz"
#     })
# print(arabaaudi)
arabaPorsche = {
  "marka" : "Porsche",
  "renk" : "beyaz",
  "yil" : 2023,
  }
# sonuc = arabaPorsche["marka"]
# sonuc = arabaPorsche.get("marka")
# del arabaPorsche["marka"]
# print(len(arabaPorsche))
# sonuc = len(arabaPorsche)
# sonuc = "marka2" in arabaPorsche
# # arabaPorsche["yil"] = 2024
# # arabaPorsche.pop("marka")
# # arabaPorsche.popitem()
# # arabaPorsche.clear()
# araba = arabaPorsche.copy()
# arabaPorsche.update({
#     "yil" : 2024,
#     "renk" : "gri",
# })
# print(arabaPorsche)
# print(araba)
str = 'hello python'
print(str + "TEST")
