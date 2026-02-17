
# def selamla(isim,mesaj):
#     print(f"{mesaj} {isim}")

# selamla("mehmet","merhaba")

# def selamla(isim = "kullanıcı",mesaj = "hoş geldin"):
#     print(f"{mesaj} {isim}")
# selamla("selin")
#eksik bilgi verildiği zaman atadığımız ilk cümleyi yazar.
#yani isim verildi ancak mesaj yok o zaman hoş geldin yazar.

# def usalma(taban,us):
#     return taban ** us
# sonuc = usalma(5,2)
# print(sonuc)

# def carpma(a,b):
#     return a*b
# def toplama(a,b):
#     return a+b
# def islem(a,b):
#     return carpma(a,b)
# sonuc = islem(10,5)
# print(sonuc)



#isim mesaj yaz.kullanıcı vs yaz.üs al.toplama çıkarmadan birini yaptır.

# def bilgi(isim,mesaj):
#     return f"{mesaj} {isim}"
# sonuc= bilgi("mehmet","hoş geldiniz")
# print(sonuc)

# def bilgi(isim="kullanıcı",mesaj="hoşgeldiniz"):
#     return f"{mesaj} {isim}"
# sonuc = bilgi("selin")
# print(sonuc)

# def usalma(a,b):
#     return a**b
# sonuc = usalma(5,5)
# print(sonuc)

def toplama(a,b):
    return a+b
def carpma(a,b):
    return a*b
def islem(a,b):
    return carpma(a,b)
sonuc = islem(5,4)
print(sonuc)


