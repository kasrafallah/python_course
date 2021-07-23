lst_q = [ 'a','b','c','d','e','f','h','u','w','r']
lst_a = [ 'A','B','C','D','E','F','H','U','W','R']
from random import randint
counter = 0
lst_temp =[]
mark = 0
while counter < 4:
    temp_index = randint(0,9)
    if not(temp_index in lst_temp):
        lst_temp.append(temp_index)
        print(lst_q[temp_index])
        a_input = input()
        if a_input == lst_a[temp_index]:
            print('corect')
            mark += 1
        else:
            print('wrong')
        counter+=1
print('you persent is',mark/4)
