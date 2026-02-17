# a = 10
# b = 20
# c = 30

# a, b, c = 10, 2, 30
# a, b = b, a #a ve b nin yeri değişti
#a += 5 #a = a + 5 #ikisi de aynı anlama geliyor
#a -= 5 #a = a - 5
#a *= 5 #a = a * 5
#a /= 5 #a = a / 5
# a **= 5 #a = a ** 5
# a //= 5 #a = a // 5
# sayilar = (1,2)
# a,b,c = sayilar
# print(a, b, c) #yeterli düzeyde değer yok.

# sayilar = (1,2,3,4,5,6)
# a,b,*c = sayilar
# print(a, b, c) #a=1 b=2 c=3,4,5,6 şeklinde olur.

# sayilar = (1,2,3,4,5,6)
# a,*b,c = sayilar
# print(a, b, c) #a=1 b=2,3,4,5 c=6 şeklinde olur.


#sayıları yaz yer değiştir + - print(sayilar) şeklinde ata

# a = 3
# b = 4
# c = 5

# a, b = b, a
# a += 15
# a -= 2
# a *= 3
sayilar = (1,3,5,8)
# a, b, c = sayilar
*a, b, c = sayilar
print(a, b, c)




