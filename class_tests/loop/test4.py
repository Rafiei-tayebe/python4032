n = int(input()) # 6
for i in range(0, n): # [0, 1, 2, 3, 4, 5] i = 1
    for j in range(0, n): #[0, 1, 2, 3, 4, 5] j = 1
        if i == 0 or j ==0 or i == n-1 or j == n-1:
            print('* ', end = '')
        else:
            print('  ', end = '')
    print()