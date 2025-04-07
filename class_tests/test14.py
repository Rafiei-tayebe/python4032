a = int(input()) # 511
count = 0

a1 = a % 10 # 1
a2 = (a//10) % 10 # 2
a3 = a // 100 # 1

if a1 + a3 == 2*a2:
    count = count + 1
if a % 3 == 0 :
    count = count + 1
if a3 > a2 and a3 > a1 :
    count = count + 1
    
if count == 3: print("Very Good")
elif count == 2: print("Good")
elif count == 1: print("Normal")
else: print("Bad")



