def f1():
    print("hello world!")
    
def f2():
    return "hello world"

def f3(a):
    a *= 2
    print(a)
    
def f4(a):
    a *= 2
    return a

# f1()
# f2()
# x = f2()
# print("x=", x)
x = f4("3")
print(x)