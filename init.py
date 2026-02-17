
# class Product:
#     def __init__(self):
#         self.name = "mercedes A"
#         self.price = "600000"
#         print("product nesnesi oluşturuldu.")
# p1 = Product()
# p2 = Product()
# print(p1.name,p1.price)
# print(p2.name,p2.price)

# class Product:
#     def __init__(self,name,price,isActive=True): #self ürünü ifade eder
#         self.name = name
#         self.price = price
#         self.isActive = isActive #ürünün var olup olmadığını sorgular
#         print("product nesnesi oluşturuldu.")
# p1 = Product("Mercedes A","600000")
# p2 = Product("BMW","500000",False)
# print(p1.name,p1.price,p1.isActive)
# print(p2.name,p2.price,p2.isActive)



# class Product:
#     def __init__(self,name,price,isActive):
#         self.name = name
#         self.price = price
#         self.isActive = isActive
#         print("product ürün oluşturuldu.")
# p1 = Product("mercedes","1200000",True)
# p2 = Product("audi","1002900",False)
# print(p1.name,p1.price,p1.isActive)
# print(p2.name,p2.price,p2.isActive)


# class Notes:
#     def __init__(self):
#         self.name = "beyza"
#         self.surname = "akça"
#         self.age = 16
#         self.note = 98
# o1 = Notes()
# print("isim:",o1.name,"soyisim:",o1.surname,"yaş:",o1.age,"not:",o1.note)

class Product:
    def __init__(self,name,price,year):
        self.name = name
        self.price = price
        self.year = year
p1 = Product("mercedes",1500000,2021)
print(p1.name,p1.price,p1.year)