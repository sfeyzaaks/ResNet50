
# def userInfo(*args):
#     print(type(args)) #demet tarzında veri

# userInfo()
# def userInfo(**kwargs):
#     print(type(kwargs)) #sözlük tarzında veri

# userInfo()


# def userInfo(**kwargs):
#     print(kwargs)
# userInfo(username= "leventert") #sözlük şeklinde leventert yazdı.
# userInfo(username="leventert",password="123456")
#{'username':'leventert,'password':'123456'}

# def userInfo(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
# userInfo(username= "leventert", password= "123456")

def siralama(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(*args)
    print(*kwargs)
siralama(1,2,3,4,5,6,key1="value1",key2="value2")



