import random
lst = []
for i in range (10):
    temp_list =[]
    for j in range(10):
        temp = random.randint(1,100)
        temp_list +=[temp]
    lst += [temp_list]
print(lst)
max_row_4 = max(lst[3])
print(max_row_4)
max_row_10 = max(lst[9])
print(max_row_10)
max_column_2 = 0
min_column_2 = 100
for item in lst:
    if item[1] > max_column_2:
        max_column_2 = item[1]
    if item[1] < min_column_2:
        min_column_2 = item[1]
print(max_column_2)
print(min_column_2)
