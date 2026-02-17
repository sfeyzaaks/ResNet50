
# import random
# sonuc = dir(random) #bilgi verir
# sonuc = random.random() #0 ve 1 arasında rastgele bir sayı üretir
# sonuc = int(random.uniform(10,100)) #10 ve 100 arasında rastgele bir sayı seçer
# sonuc = random.randint(1,100)

# users = ["mehmet","selin","kaan","cenk"]
# isim = "feyza"
# sonuc = users[random.randint(0,len(users)-1)] # 4 kişi var ancak 4.indeks diye bir şey yok o yüzden 1 çıkarırız
# sonuc = random.choice(users)
# sonuc = random.choice(isim)

# liste = list(range(10))
# random.shuffle(liste) #listenin elemanlarını rastgele karıştırır
# liste = range(100)
# sonuc = random.sample(liste,5) #rastgele 5 sayı seçer
# sonuc = random.sample(users,3)
# print(sonuc)

############
#random, uniform, randint,users arasından seçtir,choice,range liste oluştur,shuffle,sample,

import random
sonuc = random.random()
sonuc =int( random.uniform(3,700))
sonuc = random.randint(22,33)
users = ["kerem","kenan","elif","canan"]
sonuc = random.choice(users)
sonuc = users[random.randint(0,len(users)-1)]
sonuc = random.sample(users,3)
liste = list(range(19))

sonuc = random.choice(liste)
random.shuffle(liste)
print(liste)
