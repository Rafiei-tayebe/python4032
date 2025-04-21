line1 = input() # *****oo*oo*ooo***o**oo*oo*ooo*
line2 = input() # oo*ooo***ooo*oo*o*o*o***o*o*o*
line3 = input() # oo*oo*ooo**ooo**ooo**ooo**ooo*

for i in range(0, len(line1), 5) : #[0, 5, 10, 15, 20, 25]
    if line1[i:i+5] == "*****" and line2[i:i+5] == "oo*oo" :
        print('T', end = '')
    elif line1[i:i+5] == "oo*oo":
        print('A', end ='')
    elif line1[i:i+5] == "*ooo*" and line2[i:i+5] == "oo*oo" :
        print('X', end = '')
    elif line2[i:i+5] == "*o*o*" and line1[i:i+5] == "*ooo*":
        print('N', end = '')
    else:
        print('M', end = '')
