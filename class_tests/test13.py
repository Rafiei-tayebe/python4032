import math
op = input()
a = float(input())
if op != 'sqrt' :
    b = float(input())

if op == '+' :
    print('%.6f' %(a+b))
elif op == '-' :
    print('%.6f' %(a-b))
elif op == '/' :
    print('%.6f' %(a/b))
elif op == '*' :
    print('%.6f' %(a*b))
elif op == 'sqrt':
    print('%.6f' %(math.sqrt(a)))
elif op == '%' : 
    print(int(a%b))