#sorted sadece bir kereliğine sıralarken .sort() şeklinde yapılırsa yeni bir liste oluşturmuş oluruz
sayilar = [2,67,55,43,88,12]
# sayilar.sort()
# print(sayilar)
# sonuc = sorted(sayilar,reverse=True)
# sonuc = sorted((2,67,55,43,88,12))
# print(sonuc)
users = [{"username":"leventert","posts":["post1,post2"],"email":"safey0508@gmail.com"},
         {"username":"feyza","posts":["post1"],"email":"levenert1@gmail.com","password":"93948"}]
sonuc = sorted(users,key=len)
sonuc= sorted(users,key=lambda x :x["username"])
print(sonuc)