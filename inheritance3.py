

class Person:
   def __init__(self,name,surname,age):
         self.name = name
         self.surname = surname
         self.age = age
         print("person nesnesi oluşturuldu.")
   def info(self):
         print(self.name,self.surname,self.age)

class Student(Person):
    def __init__(self,name,surname,age,number):
         Person.__init__(self,name,surname,age)
         self.number = number
         print("student nesnesi oluşturuldu.")
class Teacher(Person):
    def __init__(self, name, surname, age,branch):
        Person.__init__(self,name, surname, age)
        self.branch = branch
        print("teacher nesnesi oluşturuldu.")



p1 = Person("esin","şentürk",20)
p1.info()
s1 = Student("kerem","koç",15,233)
s1.info()
print(s1.number)
t1 = Teacher("çağla","şahin",45,"chem")
t1.info()
print(t1.branch)