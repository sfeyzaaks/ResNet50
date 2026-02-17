
# sayilar = [1,3,5,8,4,77,34]
# harfler =["a","d","b","p"]
# isimler = ["ahmet","ceren","kerim","selcan"]
# sonuc = min(sayilar)
# sonuc = max(sayilar)
# print(sonuc)
# sonuc = sorted(isimler,reverse=True)
# print(sonuc)
# sonuc = max(isimler ,key = lambda x : len(x))
# print(sonuc)

# araclar = [
#      {"title":"audi","price":980000},
#      {"title":"BMW","price":800000}
#  ]
# sonuc = min(araclar,key=lambda u: u["price"])["title"]
# print(sonuc)

# araclar = [
#      {"title":"audi","price":980000},
#      {"title":"BMW","price":800000}
#  ]
# max = 0
# for urun in araclar:
#     if urun["price"]>max:
#         max = urun["price"]
# print(max) 

isimler = ["ayça","samantha"]
sonuc = min(isimler, key = lambda x : len(x))
print(sonuc)