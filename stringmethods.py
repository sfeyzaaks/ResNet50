yazi = "Benim adım feyza aksoy. İstanbul'da yaşıyorum.   "

#sonuc = yazi.upper() #yazi daki bütün harfleri büyütür.
#sonuc = yazi.capitalize() # yazi daki bütün harfleri küçültür.

#sonuc = yazi.islower() #yazi daki bütün harfler küçük mü?
#sonuc = yazi.strip() #cümle başındaki boşluğu siler.
#sonuc = yazi.split(".") #cümledeki her bir kelimeyi liste şeklinde yazar. 
#sonuc = "-".join(yazi)
#sonuc = yazi.index("feyza") # f harfinin kaçıncı indekste olduğunu bulur.
#sonuc = yazi.startswith("a")
#sonuc = yazi.endswith(" ")
#sonuc = yazi.replace("İstanbul","bursa")

#sonuc = yazi.replace("ı","i").replace("ş","s")
#print(sonuc)
#print("bu yazıda {} konusu işlendi.".format("string"))
ders1 = "matematik"
ders2 = "fizik"
print("{ilk_ders} sınavından 90, {ikinci_ders} sınavından ise 45 aldı.".format(ilk_ders = ders1, ikinci_ders = ders2))



