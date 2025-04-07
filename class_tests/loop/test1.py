from math import sqrt

def is_odd(n):
    if n%2 == 1: return True
    else: return False
    
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    i = 2
    while i <= int(sqrt(n)) + 1:
        if n % i == 0:
            return False
        i += 1
    return True

def count_prime_devisors(n):
    i = 2
    count = 0
    while i < n:
        if (n % i == 0) and (is_prime(i) == True):
             count += 1
        i += 1
    return count

def is_beautiful_odd(n):
    count = count_prime_devisors(n)
    if is_odd(n) and count != 0 and n % count == 0 and is_prime(count):
        return True
    else: return False
    
def reverse(n): # n = 123
    result = 0
    while n != 0:
        result = result*10 + (n%10) # result = 321
        n = n // 10 # n = 0
    return result
    
    
# test
n = int(input())
number = 1
result = 0
while number <= n:
    if is_beautiful_odd(number) == True:
        #print(number)
        result = result + number
    number += 1
if result == 0: print("NOT FOUND!")
else: print(reverse(result))
