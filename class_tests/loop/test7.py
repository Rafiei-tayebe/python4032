mylist = [1, 10, 90, 12, 17]
number = 50
result = 10000000
result_m1 = mylist[0]
result_m2 = mylist[1]
for i in range(len(mylist)-1) : #[0, 1, 2, 3, 4]
    m1 = mylist[i]
    for j in range(i+1, len(mylist) ):
        m2 = mylist[j]
        if abs(m1+m2-number) < result:
            result = abs(m1+m2-number)
            result_m1 = m1
            result_m2 = m2
            
print(result, result_m1, result_m2 )