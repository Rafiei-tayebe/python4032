n = int(input())
str1 = input()
str2 = input()

count = 0
for index in range(0, n):
    if str1[index] != str2[index]:
        count += 1
        
print(count)