
# def usalma(a):
#     return a ** 2
# print(usalma(3))

# sonuc = (lambda a : a ** 2)(2)
# print(sonuc)

# usalma = lambda a : a **2 
# sonuc = usalma(6)
# print(sonuc)

# toplama = lambda a,b,c : a + b + c
# sonuc = toplama(2,3,4)
# print(sonuc)

# terscevir = lambda x : x[::-1]
# sonuc = terscevir("feyza")
# print(sonuc)

# def fn1(n):
#     return lambda a : a**n
# usalma2 = fn1(2)
# sonuc = usalma2(3)
# print(sonuc)

#us al.

sonuc = (lambda a : a**2)(3)
print(sonuc)

sonuc = lambda a : a**2
print(sonuc(2))

def fn1(n):
    return lambda a : a**n
usalma=fn1(2)
sonuc = usalma(3)
print(sonuc)

