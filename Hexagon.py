#Braxton Phillips
#SDEV 220
#Chapter 2 Exercise 2.15
#Due Oct 31, 2020

print('********This program will ask for the length of one side of a hexagon. It will then display the respective area and perimeter********\n\n')
userSideLen = float(input('Please enter a length for one side of a hexagon. \n'))
hexArea = (3 * (3 ** .5)) / 2 * (userSideLen ** 2) # ** is used as exponent operator to perform artimatic for area
hexPerimeter = 6 * userSideLen
print('The area is:', hexArea, 'and the perimeter is:', hexPerimeter)

