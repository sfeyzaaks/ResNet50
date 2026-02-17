x = 15
#sonuc = 10 < x < 20

sonuc = ( x > 10) and (x < 20)

# True and True => True
# True and False => False
# False and False => False

# karnenotu = 80
# devamsizlik = 12
# sonuc = (karnenotu >= 50) and (devamsizlik < 10)
# print(sonuc)

#or operatörü (veya)
# True veya True => True
# True veya False => True
# False veya False => False

# sonuc = (x < 10) or (x % 3 == 0)
# print(sonuc)

# not operatörü

sonuc = not(x > 0) #not değil anlamına geliyor
karnenotu = 90
devamsizlik = 3
cezabilgisi = False
sonuc = (karnenotu >= 85) and (devamsizlik < 10) and (cezabilgisi == False)
print(sonuc)




