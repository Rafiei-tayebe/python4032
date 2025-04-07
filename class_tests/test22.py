count = 0
a = 7
x = a - 1  # 6
while x >= 2:
    if a % x == 0: count+=1 # 
    x = x - 1 # 1
    
if count == 0:
    print("is prime")