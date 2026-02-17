#list
#tuple
#dictionary
#sets => indekslenemez, sıralanamaz
#içerisindeki değerleri değiştirmeyeceğimizde, indekslemeyeceğimizde ve sıralamayacağımız zaman kullanılan 
#bir liste türüdür.
# markalar = {"audi","mercedes","BMW","Porsche"}

# sonuc = markalar[0]

# sonuc = "BMW" in markalar #BMW nin markalar içerisinde olup olmadığını sorgular

# markalar.add("honda") #markaların en başına honda yı ekler.
# markalar.update(["toyota","scoda"]) #listedeki herhangi bir yere toyota ve scodayı ekler
# markalar.remove("BMW") #BMW yi kaldırır
# markalar.pop() #rastgele bir elemanı siler
# markalar2 = {"toyota","opel"}
# sonuc = markalar.union(markalar2) #markalar + markalar2 yapar.
# print(sonuc)


isimler = {"ceyda","ayşe","kerem"}
sonuc = "ceyda" in isimler
isimler.add("cem")
isimler.remove("kerem")
isimler.update(["selin","inci"])
markalar = {"audi","mercedes"}
sonuc = isimler.union(markalar)
print(sonuc)
