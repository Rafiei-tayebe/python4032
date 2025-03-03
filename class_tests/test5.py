import math
a, b, c = input().split() # a = "5" b = "6" c = "1"
a = int(a) # 5
b = int(b) # 6
c = int(c) # 1
delta = math.sqrt((b*b) - (4*a*c))
x1 = (-b - delta) / (2*a)
x2 = (-b + delta) / (2*a)
print('%.3f'%min(x1, x2), '%.3f'%max(x1, x2))

#quera password: python4032
