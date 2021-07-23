num1 = eval(input())
num2 = eval(input())
bmm=1
if num1>1 and num2>1:
    if num1>num2:
        n= num2
    else:
        n =num1
    for i in range(1,n+1):
        if num2%i==0 and num1%i==0:
            bmm =i
    print(bmm)
else:
    print('error')
