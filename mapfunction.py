
# sayilar = [1,3,5,8,12]
# kareleri = []
# for sayi in sayilar:
#     kareleri.append(sayi ** 2)
# print(kareleri)


# sayilar = [1,3,5,7,11]
# def kareal(sayi):
#     return sayi ** 2
# sonuc = list(map(kareal,sayilar))
# sonuc = list(map(lambda sayi : sayi ** 2,sayilar))
# print(sonuc)

# sayilar = ["1","3","4","11"]
# sonuc = list(map(int,sayilar))
# print(sonuc)

# sayilar = [1,3,-5,-11]
# sonuc = list(map(abs,sayilar))
# print(sonuc)  #abs negatifleri pozitife çevirir

# isimler = ["ayça","mehmet","zeren","kemal"]
# sonuc = list(map(str.capitalize,isimler))
# print(sonuc)

# kullanicilar = [
#     {"ad": "yağmur", "soyad": "yalçın"},
#     {"ad": "selin" , "soyad": "kaya"}
# ]
# sonuc = list(map(lambda x : x["ad"], kullanicilar))
# print(sonuc)

# liste = [10,3,2,5]
# yeniliste = list(map(lambda x : x * 2, liste))
# print(yeniliste) #map i list içine almak gerekiyor.

#################
#for döngüsü kullanarak kareleri ekle
#def ve map i aynı kullan
#def lambda map
#str int e dönüştür
#abs
#kullanıcıların adını al


# sayilar = [1,3,5,77]
# katlar = []
# for i in sayilar:
#     katlar.append(i*2)
# print(katlar)

# sayilar = [3,5,7,9]
# def sayilar1(sayi):
#     return sayi ** 2
# sonuc = list(map(sayilar1,sayilar))
# print(sonuc)

# sayilar = [3,5,7,9]
# sonuc = list(map(lambda x : x**2,sayilar))
# print(sonuc)

# sayilar = ["1","3","4","15"]
# sonuc = list(map(int,sayilar))
# print(sonuc)

# sayilar = [-1,-3,4]
# sonuc = list(map(abs,sayilar))
# print(sonuc)

isimler = [ {"ad":"kerem" , "soyad":"aktürk"},{"ad":"cemile","soyad":"demir"}]
sonuc = list(map(lambda x : x["soyad"],isimler))
print(sonuc)