
import os
# sonuc = dir(os)
# sonuc = os.name #işletim sis bilgisi alınabilir

# sonuc = os.getcwd() #nerde olduğumuzu verir
# os.chdir("..")
# os.chdir("//Users")
# sonuc = os.getcwd()
# # os.mkdir("yeniklasör") #yeni klasör oluşturur
# os.makedirs("yeniklasor/deneme") #iç içe klasör oluşturur
# os.rename("yeniklasor","ustklasor")
# os.rmdir("ustklasor") #üst klasörü siler
# os.removedirs("yeniklasor/deneme")

#listeleme
sonuc = os.listdir()
for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)

#dosya hakkında bilgi alma
sonuc = os.stat("errors.py")
print(sonuc)
