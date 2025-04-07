mark = input()
try:
    mark = int(mark)
except:
    print("mark must be a numerical value")
    mark = int(input())
print(mark)