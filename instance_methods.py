#class ##__init__ tanımlamak için kullanılır.
# class User:
#     def __init__(self,username,name,surname,birthday):
#         self.username = username
#         self.name = name
#         self.surname = surname
#         self.birthday = birthday
#     def info(self):
#         return f"{self.username} kullanıcı adıyla {self.name} {self.surname} sisteme kaydedildi."
#     def calculateAge(self):
#         return f"{self.name} kullanıcısının yaşı :{2022-self.birthday}"
# u1 = User("leventert","levent","ertunalılar",1984)
# u2 = User("lertunali","feyza","aksoy",2005)
# print(u1.info())
# print(u2.info())
# print(u1.calculateAge())
# print(u2.calculateAge())

#class kullandığımızda birden fazla person oluşturmamıza gerek kalmaz
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} konuştu.")
#     def eat(self):
#         print(f"{self.name} yedi.")
# insan1 = Person("oğuz")
# insan1.speak()
# insan1.eat()

class Person:
    def __init__(self,username,name,surname,birthday):
        self.name = name
        self.username = username
        self.birthday = birthday
        self.surname = surname
    def info(self):
        return f"{self.username} kullanıcı adıyla {self.name} {self.surname} tarafından giriş yapıldı."
    def calculateAge(self):
        return f"{self.name} {self.surname} adlı kullanıcının yaşı: {2024-self.birthday}"
kullanici1 = Person("metinakyalii","metin","akyalı",1995)
kullanici2 = Person("seldem","selin","demirci",2001)
print(kullanici1.info(),kullanici1.calculateAge())
print(kullanici2.info())
