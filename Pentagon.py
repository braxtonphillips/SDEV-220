#Braxton Phillips
#SDEV 220
#Chapter 3 Exercise 3.1
#Due Oct 31, 2020

import math #calling math module for use of functions in line 10 

print('********This program will ask for the length of one side of a pentagon. It will then display the respective area and perimeter********\n')
userSideLen = float(input('Please enter a length from the center to a vertex. \n'))
pentArea = (3 * math.sqrt(3)) / 2 * ((2 * userSideLen * math.sin(math.pi/5)) ** 2) #using sqrt, sin, pi functions with with arithmatic
pentPerimeter = 5 * userSideLen
print('The area is:', format(pentArea,'.2f'), 'and the perimeter is:', pentPerimeter) #using format to have 2 decimal places