
isim = "feyza aksoy"

# for harf in isim:
#     if ( harf == "y"):
#         break   #y harfine gelince sonlanması için break kullandık.
#     print(harf)

# i = 0
# while (i < 10):
#     i += 1
#     if ( i == 5):
#         continue
#     print(i)  #continue 5 i atlayarak devam etmesini sağlar.
    
# i = 5
# while (i < 50):
#     i += 1
#     if ( i%2 == 0):
#         continue
#     print(i)

# i = 0
# toplam = 0
# while (i <= 100):
#     i += 1
#     if ( i%2 == 0):
#         continue
#     toplam += i
# print(f'toplam: {toplam}' )


# string1 = "abc def ghi"
# string2 = "def ghi abc"
# print(string1 == string2)
# print(string1 != string2)

# sayilar = [1,2,3]
# def toplama():
#     sonuc = 0 
#     for sayi in sayilar:
#         sonuc += sayi
#     return sonuc

# sayim = toplama()
# print(sayim)

def fonksiyonum(**islemler):
    if 'toplama' in islemler.keys():
        sonuc = sum(islemler['toplama'])
        print(sonuc)
    if 'carpma' in islemler.keys():
        carp = 1
        for i in islemler['carpma']:
            carp *= i
            print(carp)
islemler = {'toplama': [1,2,3] , 'carpma': [3,4] }
fonksiyonum()
