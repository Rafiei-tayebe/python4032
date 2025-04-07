a = input() # "123"
count = 0

a1 = int(a[2]) 
a2 = int(a[1])
a3 = int(a[0])

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



