# cumle = "python çok eğlenceli bir dildir."
# kelimeler = cumle.split()
# enuzun= max(kelimeler, key = len)
# print(enuzun)


# cumle = "python çok güzel bir dildir."
# kelimeler = cumle.split()


# tek =[]
# cift=[]
# for i in range(30):
#     if i %2 ==0 :
#         cift.append(i)
#     else:
#         tek.append(i)
# print("tek sayılar:" , tek)
# print("çift sayılar: " , cift)


# cumle ="python öğrenmek gerçekten eğlencelidir."
# kelime = cumle.split()
# enuzun = max(kelime , key = len)
# print(enuzun)

# kelime = input("bir kelime yazınız:")
# ters= kelime[::-1]
# kelimemiz = "".join(ters)
# print(kelimemiz)
# sayi =[]
# harf=[]
# listem = [1,2,"m","a",33]
# kelimem = "".join(str(m) for m in listem)
# for i in kelimem:
#     if i.isdigit():
#         sayi.append(int(i))
#     else:
#         harf.append(i)

# print("sayılar:" , sayi)
# print("harfler: " , harf)

# kelimeler = ["efe","kelime","amama","elif"]
# palindromlar = []
# for kelime in kelimeler:
#     if kelime == kelime[::-1]:
#         palindromlar.append(kelime)
# print(palindromlar)

# cumle = "python çok güzel bir dil"
# kelime = cumle.split()
# budur = []
# for i in kelime:
#     budur.append(i[::-1])
# sonuc = " ".join(budur)
# print(sonuc)

# cumle = "python çok güzel bir dil"
# kelime = sorted(cumle.split(), key = len, reverse=True)
# sonuc = " ".join(kelime)
# print(sonuc)


# cumlem = "bu kızıl pembe hoşuma gitti"
# kelime = sorted(cumlem.split() , key = len, reverse = True)
# sonuc = " ".join(kelime)
# print(sonuc)

# cumle = "bunun ne olduğu hakkında bir fikrim yok"
# kelime = sorted(cumle.split(), key = len, reverse = True)
# sonuc = " ".join(kelime)
# print(sonuc)


# listem = [5,10,15,20,25,30]
# yeni = []
# for i in listem :
#     if i %3 ==0 :
#         yeni.append(i)
# print(yeni)


# cumle = input("bir cümle yazınız:" )
# kelime =cumle.upper()
# print(kelime)


# cumlem = "abcdefg17368"

# harf = 0
# sayi = 0
# for i in cumlem:
#     if i.isdigit():
#         sayi +=1
#     else:
#         harf += 1
# print("harf:", harf)
# print("sayı:" , sayi)


# sayilar = [12,45,78,23,56]
# sonuc = 0
# yeni = []
# for sayi in sayilar:
#     sonuc += sayi
# result = sonuc / len(sayilar)
# for i in sayilar:
#     if i>result:
#         yeni.append(i)


# print(yeni)

# cumle = "hello"
# kelime = cumle[::-1]
# print(kelime)

# kelime = input("bir kelime yazınız: ")
# uzunluk = len(kelime)
# if uzunluk %2 == 0 :
#     print(kelime[uzunluk//2 -1 : uzunluk//2 +1])
# else:
#     print(kelime[uzunluk//2])


# listem = [2,4,6,8,10]
# cevap = list(map(lambda x : x **2 , listem))
# print(cevap)

# listem = ["kalem", "defter", "kitap", "bardak"]
# print(sorted(listem, reverse = True))

# listem = [3,4,5,3,4,6,7]

# import time
# for saniye in range(20,0,-1):
#     print(saniye , end= " ", flush = True)
#     time.sleep(1)
# print("roket ateslendi")

# listem = [3,4,5,3,4,6,7]
# benzersizler= []
# for i in listem:
#     if listem.count(i) == 1:
#         benzersizler.append(i)
# sayi = max(benzersizler)
# print(sayi)
# liste = [3,4,5,3,4,6,7]
# from collections import Counter
# sayilar = Counter(liste)
# benzersizler = [sayi for sayi, adet in sayilar.items() if adet == 1]
# if benzersizler:
#     print(max(benzersizler))
# else:
#     print("benzersiz sayı yok")




# kelimeleri harflerine göre sırala , aynı olanları sözlüğün içine ata, sorted fonks
