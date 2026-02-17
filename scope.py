
# a = "global değer"
# def fn1(): #fonksiyon içinde tanımladığımız değer sadece fonksiyon içinde kullanılabilir
#     a ="local değer"
#     print(a)
# fn1()
# print(a)

# city = "istanbul"
# def changecity(newcity):
#     city = newcity
#     print(city)
# changecity("bursa")
# print(city)


# city = "istanbul"
# def disfonksiyon():
#     city = "izmir"
    
#     def icfonksiyon():
#         city = "ankara"
#         print("iç fonksiyonu " + city)

#     icfonksiyon()
# disfonksiyon() #en içteki fonksiyonu çağırarak devam eder


# a = 10
# def fn2():
#     global a  #dışarıdaki a yı da 20 ye çevirir

#     a = 20
#     print(f"changed a to {a}")
# fn2()
# print(a)

# global local f fonks tanımla.ist brsa.iç dış fonksiyon.global kullan.


# a  = "global değer"
# def fn1():
#     a = "local değer"
#     print(a)
# fn1()
# print(a)

# city ="istanbul"
# def changecity(newcity):
#     city = newcity
#     print(city)
# changecity("bursa")

# city = "istanbul"
# def disfonksiyon():
#     city = "izmir"
#     print(city)
#     def icfonksiyon():
#         city = "ankara"
#         print("içfonksiyonu " + city)
#     icfonksiyon()
# disfonksiyon()
# print(city)
    
# a = 10
# def change():
#     global a
#     a = 7
# change()
# print(a)
    

# a = "global değer"
# def change():
#     a = "local değer"
#     print(a)
# change()

# city = "istanbul"
# def change(newcity):
#     city = newcity
#     print(city)
# change("bursa")

# city = "istanbul"
# def disfonk():
#     city = "izmir"
#     print(city)
#     def icfonk():
#         city = "bursa"
#         print("iç fonksiyon: ", city)
#     icfonk()
# disfonk()
    
a = 7
def turn():
    global a
    a = 15
    print(a)
turn()
print(a)