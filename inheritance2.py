
# class Person:
#     def __init__(self,name,surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         print("person nesnesi oluşturuldu.")
#     def info(self):
#         print(self.name,self.surname,self.age)

# class Student(Person):
#     pass
# class Teacher(Person):
#     pass
# p1= Person("esin","şentürk",20)
# print(p1.name,p1.surname,p1.age)
# s1 = Student("kerem","koç",15)
# print(s1.name,s1.surname,s1.age)
# t1 = Teacher("çağla","şahin",45)
# print(t1.name,t1.surname,t1.age)

# p1 = Person("esin","şentürk",20)
# p1.info()
# s1 = Student("kerem","koç",15)
# s1.info()
# t1 = Teacher("çağla","şahin",45)
# t1.info()

class Person:
    def __init__(self,username,name,surname,password):
        self.username = username
        self.name = name
        self.surname = surname
        self.password = password
    def info(self):
        print(self.username,self.name,self.surname,self.password)
p1 = Person("cglaozturk","çağla","öztürk",85738)
p2 = Person("krmylmz","kerem","yılmaz",54549)
p1.info()
p2.info()