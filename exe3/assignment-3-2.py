import random
lst = []
for i in range (100):
    temp = random.randint(1,100)
    lst.append(temp)
arr = lst
for i in range(len(lst) - 1):
    for j in range(0, len(lst) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)
lst.sort()
print(lst)
