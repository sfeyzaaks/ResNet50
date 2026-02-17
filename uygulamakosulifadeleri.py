#kullanıcıdan veri almak istediğimizde input fonksiyonunu kullanırız.

# sayi = int(input("sayı giriniz: "))

# if (sayi > 0):
#     if(sayi % 2 == 1):
#         print("Girilen sayı pozitif tek sayıdır.")
#     else:
#         print("Girilen sayı pozitif fakat tek değil.")
# else:
#     print("Girilen sayı negatiftir.")



# x = int(input("x : "))
# y = int(input("y : "))
# z = int(input("z : "))

# if (x>y) and (x>z):
#    print("x en büyük sayıdır.")
# elif (y>x) and (y>z):
#    print("y en büyük sayıdır.")
# elif (z>x) and (z>y):
#    print("z en büyük sayıdır.")


# isim = input("isim: ")
# yas = int(input("yaş: "))
# egitim = input("eğitim: ")
# if (yas >= 18):
#     if(egitim == "lise" or egitim == "üniversite"):
#         print("ehliyet alabilirsiniz.")
#     else:
#         print(f'{isim} ehliyet alamazsınız çünkü eğitim durumunuz yetersiz.')
# else:
#     print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor.')


# sayi = int(input("Sayı giriniz: "))
# if (sayi > 0):
#     if (sayi % 2 == 0):
#         print("Girilen sayı çift ve pozitif.")
#     else:
#         print("Girilen sayı tek ve pozitif.")
# elif (sayi == 0):
#     print("Girilen sayı 0.")
# else:
#     print("Girilen sayı negatiftir.")



# x = int(input("x giriniz: "))
# y = int(input("y giriniz: "))
# z = int(input("z giriniz: "))

# if (x>y) and (x>z):
#     print("x en büyük sayıdır.")
# elif (y>x) and (y>z):
#     print("y en büyük sayıdır.")
# else:
#     print("z en büyük sayıdır.")

isim = input("isim: ")
yas = int(input("yaş: "))
egitim = input("eğitim durumu: ")

if (yas >= 18):
    if (egitim == "lise") or (egitim == "üniversite"):
        print("Ehliyet alabilirsiniz.")
    else:
        print(f'{isim} eğitim durumunuz yetersiz olduğundan ehliyet alamazsınız.')
else:
    print(f'{isim} yaşınız tutmadığından ehliyet alamazsınız.')


