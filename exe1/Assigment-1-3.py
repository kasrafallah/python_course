t = eval(input('Enter temprature of room :'))
type_of_change = eval(input('Enter 1 if you want to convert Celsius to Fahrenheit and \nEnter 2 if you want to convert Fahrenheit to Celsius :'))
if type_of_change == 1:
    print('temprature in fahrenheit is :', 9 / 5 * t + 32)
elif type_of_change == 2:
    print('temprature in celesius is :', 5 / 9 * ( t - 32) )
else:
    print('invalid input')
