# def fonksiyonum(**islemler):
#     if 'toplama' in islemler.keys():
#         sonuc = sum(islemler['toplama'])
#         print(sonuc)
#     if 'carpma' in islemler.keys():
#         carp = 1
#         for i in islemler['carpma']:
#             carp *= i
#         print(carp)
# islemler = {'toplama': [1,2,3] , 'carpma': [3,4] }
# fonksiyonum(**islemler)

# string = ("This must be true")
# sonuc = string.split()
# sonucum = sonuc[::-1]
# print(sonucum)

# def calculate(a,b, operator):
#     if operator == "+":
#         return a+b
#     elif operator == "-":
#         return a-b
#     elif operator == "*":
#         return a*b
#     elif operator == "/":
#         return a/b
#     else:
#         return "division by zero error"
    
# sonuc = calculate(5,2,"/")
# print(sonuc)

# list = [2,3,6,11]
# for i in list:
#     if i % 2 == 0:
#         print(" sayı çifttir")
#     else:
#         print("sayı tektir.")
       
# sayi = int(input("sayı giriniz:"))
# if sayi % 2 == 0:
#     print("girdiğiniz sayı çifttir.")
# else:
#     print("girdiğiniz sayı tektir.")  

# saat = 12.00 
# name = input("isminizi giriniz: ")
# surname = input("soyisminizi giriniz: ")
# if saat >=12.00 and saat <= 18.00:
#     print("iyi günler")
# elif saat < 12.00:
#     print("günaydın")
# else:
#     print("iyi akşamlar")
# print(f"sisteme hoşgeldiniz {name} {surname} ")


# number = int(input("Bir sayı giriniz: "))
# print(number**2)

# def factorial(n):
#     sonuc = 1
#     for i in range(1,n+1):
#         sonuc *= i
#     return sonuc
# print(factorial(3)) 

# def reverse(kelime):
#     return kelime[::-1]

# print(reverse("hello"))
#1
# sayi = int(input("sayıyı giriniz: "))
# if sayi % 2 == 0:
#     print("girilen sayı çifttir.")
# else:
#     print("girilen sayı tektir.")


# sayilar = [42,17,56,3,89,12]
# sayilar.sort()
# print(sayilar[0])


# isimler = ["ahmet","mehmet","zeynep"]
# ????

# sayilar = list(filter(lambda x:  x%2 == 0 , [1,2,3,4,5,6,7,8]))
# print(sayilar)

# string= "hello"
# print(string[::-1])

# sayi = int(input("bir sayı giriniz: "))
# if sayi >0 :
#     print("girilen sayı pozitif.")
# elif sayi < 0:
#     print("girilen sayı negatif.")
# else:
#     print("girilen sayı 0 dır.")

# yazi ="python harika!"
# yazim = yazi.upper()
# print(yazim)

# sayilar = [80,90,70,100]
# sonuc = 0
# for sayi in sayilar:
#     sonuc += sayi
# islem = sonuc / len(sayilar)
# print(islem)

# string = "python çok güzel"
# cevap = string.split()
# cevabim = cevap[::-1]
# cevabimiz = " ".join(cevabim)
# print(cevabimiz)

# kelimeler = ["ev","masa","kitap","elma","kalem","su"]
# liste =[]
# for i in kelimeler:
#     if len(i) == 4:
#         liste.append(i)
# print(liste)

# ciftler = []
# tekler = []
# for i in range(20):
#     if i %2 == 0:
#         ciftler.append(i)
#     else:
#         tekler.append(i)
# print(ciftler, tekler)

# yazi = "güzel bir gün"
# cevap = yazi.split()
# birinci = cevap[0][::-1] 
# ikinci = cevap[1][::-1]
# ucuncu = cevap[2][::-1]
# sonuc = " ".join([birinci, ikinci, ucuncu])
# print(sonuc)

# yazi = "güzel bir gün"
# kelimeler = yazi.split()
# listem = [kelime[::-1] for kelime in kelimeler]
# cevap = " ".join(listem)
# print(cevap)

# harf = 0
# sayi = 0
# yazi = "abcdefg1234"
# for i in yazi:
#     if i.isalpha():
#         harf += 1
#     else:
#         sayi +=1
# print("harf sayısı : " , harf)
# print("rakam sayısı :" , sayi)

# yazi = list(map(lambda x : x**2 , [1,2,3,4]))
# print(yazi)

# isimler = ["ayşe","ali","mehmet","mustafa","aslı","murat"]
# gruplar = {}
# for isim in isimler:
#     harf = isim[0]
#     if harf not in gruplar:
#         gruplar[harf]= []
#     gruplar[harf].append(isim)
# for harf , isim_listesi in gruplar.items():
#     print(f"{harf} : {', '.join(isim_listesi)}")


sayilar= [10,20,30,40]
sonuc = 0
listem = []
for sayi in sayilar:
    sonuc += sayi
    result = sonuc / len(sayilar)
if sayi > result :
    listem.append(sayi)
print(listem)
