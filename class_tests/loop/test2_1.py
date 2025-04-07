mylist = [10, 9, 8, 90, 12, 13, 1000]
min_value = mylist[0] # 10

for value in mylist: # value = 1000
    if value < min_value:
        min_value = value # 8
    
print('min value = ', min_value)


sum_value = 0
for value in mylist: # value = 1000
    sum_value += value


def factorial(n): # n=0
    result = 1
    for number in range(2, n+1): # [2, 3, 4, 5]
        result = result*number # 1*2*3*4*5
    return result

def cos(x):
    result = 0
    for n in range(0, 11):
        a =  ( ((-1)**n) / factorial(2*n) ) * (x**(2*n))
        result = result + a
    return result
        
def sum_digits(n): # 8759
    result = 0
    while n != 0:
        d = n % 10 # d = 8
        result += d # result = 9 + 5 + 7 + 8
        n = n // 10 # 0
    return result
    
def sum_digits2(n): # 8759
    result = 0
    n = str(n) # n = "8759"
    for digit in n: # digit = "9"
        result = result + int(digit) # 8 + 7 + 5 + 9
    
    return result
print(sum_digits(8759))

n = int(input()) #8759

while True: # 8759
    result = sum_digits(n) # result = 2
    if result < 10:
        break
    n = result # n = 11
    
print(result)

