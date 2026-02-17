#value types => string, number
sayi1 = 10
sayi2 = 20

sayi1 = sayi2
sayi2 = 30
print(sayi1,sayi2)

#reference types => lists

x = ["python","java"]
y = ["python","java"]
x = y
y[0] = "html"
print(x,y)