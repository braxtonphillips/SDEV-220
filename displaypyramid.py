"""
Braxton Phillips
SDEV 220
Chapter 5 Exercise 5.19
Due Nov 7,2020
"""

userInt = eval(input("Enter the number of lines: \t"))

#if-else is used to determine if user input is valid
if userInt >= 1 and userInt <= 15:
    for i in range(1, userInt + 1):
        for j in range(45 - (3 * i), 0 , -1):
            print(' ', end = '')
        for k in range(i, 0, -1):
            print('{:3d}'.format(k),end="")
        for l in range(2, i + 1 ):
            print('{:3d}'.format(l),end="")
        print()
else:
    print('Invalid Input.')