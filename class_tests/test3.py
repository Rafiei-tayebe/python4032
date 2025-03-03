#a = int(input())
#b = int(input())
#print(a+b)

c = input("enter 2 numbers: ") # c = "10 20"
d = c.split() # d = ["10", "20"]
x1, x2 = c.split() # x1 = "10" , x2 = "20"
x1 = int(x1) # x1 = 10
x2 = int(x2) # x2 = 20
print(x1 + x2)

c = input() # c = "10 20 30"
d = c.split() # d = ["10", "20", "30"]
x1, x2, x3 = c.split() # x1 = "10" , x2 = "20", x3= "30"

print(c[4]) # 0
print(d[1]) # 20
