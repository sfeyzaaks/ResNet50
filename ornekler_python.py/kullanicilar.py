# import csv 
# import os 
# dosya_adi = "kullanicilar.csv"
# if os.path.exists(dosya_adi):
#     with open(dosya_adi , encoding = 'utf-8') as f :
#         satir_sayisi = sum(1 for _ in f )
# else :
#     satir_sayisi = 1


# alan = ["id", "isim", "yas"]
# isim = input("isminizi giriniz: ")
# yas = input("yaşınızı giriniz: ")

# with open("kullanicilar.csv" , "a", encoding= 'utf-8') as dosya:
#     yazici = csv.DictWriter(dosya , fieldnames = alan)
#     if satir_sayisi == 1:
#         yazici.writeheader()

#     yazici.writerow({
#         "id": satir_sayisi,
       
#         "isim" : isim ,
#         "yas" : yas
#     })
# print("veri kaydedildi")
# import csv
# with open("C:/Users/feyza/Desktop/spotify_history.cvs", mode = "r", encoding = "utf-8") as file:
#     csv_reader = csv.reader(file)
#     print(csv_reader)

# import csv 
# with open("spotif_history.csv" , "w" , encoding = "utf-8") as file:
#     csv_writer = csv.writer(file)
#     print(csv_writer)

# import csv
# data = [{"isim": "ali", "yas" : "25" , "sehir" : "istanbul"}]
# with open("personeller.csv" , "w" , newline = "" , encoding = "utf-8") as file:
#     colonlar = ["isim" , "yas" ,"sehir"]
#     csv_dict_writer = csv.DictWriter(file , fieldnames = colonlar)
#     # csv_dict_writer.writeheader() başlıklar çağırıldı
#     csv_dict_writer.writerows(data) her bir başlık sözlüktekilerle eşleşti

# import csv
# import os

# dosya_adi = 'kullanicilari.csv'
# basliklar = ['id', 'isim' ,'yas']

# if os.path.exists(dosya_adi):
#     with open('kullanicilari.csv' ,'r' , encoding = 'utf-8') as file:
#         satir_sayisi = sum(1 for _ in file)
# else:
#     satir_sayisi = 1 

# isim = input('isim giriniz: ')
# yas = int(input('yaşınızı giriniz : '))

# with open('kullanicilari.csv', 'a' ,newline ='', encoding = 'utf-8'):
#     csv_writer = csv.DictWriter(file, fieldnames = basliklar )
#     if satir_sayisi == 1:
#         csv_writer.writeheader()
#     csv_writer.writerow({'id': satir_sayisi , 'isim': isim , 'yas' : yas})

# with open('kullanicilari.csv', 'r' , encoding = 'utf-8') as file:
#     csv_reader = csv.reader(file)
#     print( '/n kullanıcılar:')
#     for satir in csv_reader:
#         print(satir)


# import csv

# with open("notlar.csv", "r", encoding= "utf-8") as file:
#     csv_reader = csv.DictReader(file)
#     ortalama = (vize* 0.4) + (final* 0.6)
#     for satir in csv_reader:
#         isim = satir["isim"]
#         vize = int(satir["vize"])
#         final = int(satir["final"])

#         durum = "geçti" if ortalama >= 50 else "kaldi"
#         print(f"{isim} isimli öğrenci {durum}")


# import csv
# basliklar = ["ID","KİTAP ADI", "YAZAR","YİL"]
# data = [{"ID": 1 , "KİTAP ADI": "SUÇ VE CEZA" , "YAZAR": "DOSTOYEVSKİ", "YİL": 1866}
#         {"ID": 2 , "KİTAP ADI": "1984", "YAZAR": "GEORGE ORWELL", "YİL": 1949}
#         {"ID": 3, "KİTAP ADI": "HAYVAN ÇİFTLİĞİ", "YAZAR": "GEORGE ORWELL"}]

# with open("kitaplar.csv", "w", newlines ="" , encoding="utf-8" ) as file:
#     csv_writer = csv.DictWriter(file, fieldnames = basliklar)
#     csv_writer.writerows(data)


# yazar_adi = input("aradığınız yazarı giriniz: ")

# with open("kitaplar.csv", "r", encoding = "utf-8") as file:
#     csv_reader = csv.DictReader(file)
#     bulundu = False


#     for kitaplar in csv_reader:
#         if yazar_adi.lower() == kitaplar["YAZAR"] or yazar_adi.upper() == kitaplar["YAZAR"]:
#             print(f"{kitaplar["KİTAP ADI"]} {kitaplar["YİL"]}")
#             bulundu = True
#     if not bulundu :
#             print("yazar bulunamadı")

# import csv
# basliklar = ["isimler","devamsizliklar"]
# data = [{"isim": "ali", "devamsizliklar": 3} , 
#         {"isim": "ayşe" , "devamsizliklar": 7}, 
#         {"isim": "mehmet", "devamsizliklar": 5},
#         {"isim": "zeynep", "devamsizliklar": 8},
#         {"isim": "ahmet", "devamsizliklar": 2}]
# with open("devamsızlık.csv", "w", newline ="", encoding = "utf-8") as file:
#     csv_writer = csv.DictWriter(file, fieldnames = basliklar)
#     csv_writer.writeheader()
#     csv_writer.writerows(data)

# with open("devamsızlık.csv", "r", encoding = "utf-8") as file:
#     csv_reader = csv.DictReader(file)
#     for ogrenci in csv_reader:
#         if ogrenci ["devamsizliklar"]> 5:
#             print(ogrenci["isim"])

# import csv
# basliklar = ["isim", "saatlik ücret", "çalışma saati"]
# data = [{"isim": "ali", "saatlik ücret": 100 , "çalışma saati": 160}
#         {"isim": "ayşe", "saatlik ücret": 120, "çalışma saati": 140}
#         {"isim": "mehmet", "saatlik ücret": 90 , "çalışma saati": 170}
#         {"isim": "zeynep", "saatlik ücret": 110 , "çalışma saati": 150}]
# with open("calisanlar.csv", "w", newline= "", encoding= "utf-8") as file:
#     csv_writer = csv.DictWriter(file, fieldnames = basliklar)
#     csv_writer.writeheader()
#     csv_writer.writerows(data)
    
# with open("calisanlar.cvs", "r", encoding="utf-8") as file:
#     csv_reader = csv.DictReader(file)
#     print("\n maaş bordrosu:")

#     for calisan in csv_reader:
#         isim = calisan["isim"]
#         ucret = calisan["saatlik ücret"]
#         saat = calisan["çalışma saati"]
#         maas = ucret * saat
#         print(f"{isim.title()} maaş bordrosu {maas}")
        

#     sonuc = []
    

#     for calisan in csv_reader:
#         aylik_maas = int(calisan["saatlik ücret"]) * int(calisan["çalışma saati"])
#         sonuc.append(calisan)
#     print(sonuc)
print("hello")



        



            