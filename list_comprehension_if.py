
# [expression for item in liste if koşul ]

# sayilar = [1,3,7,12,22,34]
# sonuc = []

# for sayi in sayilar:
#     if(sayi %2 == 0):
#         sonuc.append(sayi)
# print(sonuc)

# sonuc = [sayi for sayi in sayilar if sayi % 2 == 0]
# print(sonuc) #sadece if kullanırsak for başa yazılır.

# sonuc = [sayi if sayi % 2 ==1 else "çift sayı" for sayi in sayilar]
# print(sonuc) #if ve else yi birlikte kullanırsak for sona yazılır.
# koşul durumuna bakarak döngüyü çalıştırır.



#çiftse if kullan.çiftse if ve else kullan.

# sonuc = []
# sayilar = [1,2,3,4,5,6,7,8,9]
# for i in sayilar:
#     if( i %2 == 0):
#         sonuc.append(i)
# print(sonuc)

# sayilar = [1,2,3,4,5,6]
# sonuc = [sayi for sayi in sayilar if sayi% 2 == 0]
# print(sonuc)

sayilar = [1,2,3,4,5,6]
sonuc = [sayi if sayi %2 == 0 else "tek sayı" for sayi in sayilar]
print(sonuc)
   
    


