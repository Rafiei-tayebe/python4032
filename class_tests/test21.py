a = 5
s = 0
while a > 0: # 
    s = s + a # s = 5 + 4 + 3 + 2 + 1
    a = a - 1 # a = 0
    
print(s) # 15

def sum_to_a(a): # a = 2
    s = 0
    while a > 0: # 
        s = s + a # s = 2 + 1
        a = a - 1 # a = 0
    return s

x = sum_to_a(1000)
print(x)

def factorial(a): # a = 5
    s = 1
    while a > 1: # 
        s = s * a # s = 5 * 4 * 3 * 2
        a = a - 1 # a = 1
    return s
x = factorial(5)
y = factorial(7) + sum_to_a(8) / factorial(2)

