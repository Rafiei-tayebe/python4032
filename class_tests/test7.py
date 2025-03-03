import math
a = int(input()) # 1234  --> 4231
r = a % 10 # 4
n = math.floor(math.log10(a)) + 1 # 4
l = a // (10**(n-1)) # 1
m = a % (10**(n-1)) - r # 230
b = r * (10**(n-1)) + m + l # 4231
print(b)

# a = input() # '1234'
# n = len(a) # 4
# print(int(a[n-1] + a[1:n-1] + a[0]))





