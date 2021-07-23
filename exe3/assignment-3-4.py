n = eval(input())
m = eval(input())
temp = 0
for i in range(m):
    for j in range(n):
        print(temp,end=' ')
        temp += 1
        if temp == 9:
            temp = 0
    print()
