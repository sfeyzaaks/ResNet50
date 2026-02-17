
# def toplama(x,y):
#     return x + y
# toplam = toplama(y=2,x=4)
# print(toplam)

# def toplama(*args,**kwargs):
#     print(args)
#     print(kwargs)
# toplama(1,2,3,4,y=2,x=4)
#değerler belirtilmişse ,yani x=a y=b gibi bunlar kwargslara yazılır.geri kalanlar args lara yazılır

# def toplama(a,b,*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print(a,b)
# toplama(1,2,3,4,y=2,x=9)
#a ve b yi dışarı çıkardık(sıra önemli) belirtilmemiş olanlar args a belirtilmişler kwargsa yazıldı.

def toplama(*args,**kwargs):
    toplam = 0
    for i in args:
        toplam += i
    return toplam
sonuc = toplama(1,2,3,4,5,6)
print(sonuc)


