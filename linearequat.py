#Braxton Phillips
#SDEV 220
#Chapter 4 Exercises 4.3
#Due Oct 31, 2020

for i in range(0, 6): #counter used to apply users input to variables
    userValues = eval(input('Enter a, b ,c , d, e, f \n'))
    if i == 0:
        a = userValues
        i += 1
    elif i == 1:
        b = userValues
        i += 1
    elif i == 2:
        c = userValues
        i += 1
    elif i == 3:
        d = userValues
        i += 1
    elif i == 4:
        e = userValues
        i += 1
    elif i == 5:
        f = userValues
        i += 1

if (a * d - b * c ) == 0:
    print('The equation has no solution.')
else:
    x = ((e * d) - (b * f)) / ((a * d) - (b * c))
    y = ((a * f) - (e * c)) / ((a * d) - (b * c))
    if x - y == 0:
        print(a, b, c, d, e, f)
    print('The answer for x is', x, 'and the answer for y is', y)
            