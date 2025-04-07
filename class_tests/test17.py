a = input() # "123"
b = input() # "421"

def reverse(a):
    if type(a) == 'str':
        return int(a[2] + a[1] + a[0])

ar = reverse(a)
br = reverse(b)
        
        
ar = int(a[2] + a[1] + a[0]) # 8
br = int(b[2] + b[1] + b[0]) # 124

a = int(a)
b = int(b)
sa = a // 100 # 1
da = (a // 10) % 10 #2
ya = a % 10 # 3
ar = ya*100 + da*10 + sa # 321
br = (b % 10) * 100 + ((b // 10) % 10) * 10 + (b // 100)

if ar < br :
    print(a, '<', b)
elif br < ar:
    print(b, '<', a)
else:
    print(a, '=', b)