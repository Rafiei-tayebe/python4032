# #print()
# #input()
# #int()
# #str()
# #float()
# #split()
# #type()
# #round()
# #len()
# #min()
# #max()

# # f(x) = x**2 + 2*x + 1
# def f(x):
#     if type(x) == 'int' :
#         return x**2 + 2*x + 1
#     else:
#         return -1

# def miin(x, y): # x = 4 , y = 9
#     if x < y: return x
#     else: return y
    


# a = f(2) # 9
# b = min(3, 2)
# c  = miin(4,9)
# d  = f("salam")

# e = ["123" , "425" , "145"]
# f = list(map(int, e)) # [123 , 425 , 145]

# def plus1(x):
#     return x+1

# g = list(map(plus1, f)) # [124, 426, 146]

# # 1 2 3 
# a, b, c = map(int, input().split())

f = ["hi", "bye", "salam", "ok"]
print(*f, sep="_")
