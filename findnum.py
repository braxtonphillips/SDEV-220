"""
Braxton Phillips
SDEV 220
Chapter 5 Exercise 5.13
Due November 7, 2020
"""

values = [] #creates list that values will be stored in
for i in range(200,401): #creates range of values that will be tested from 200 through 400
    if i % 7 == 0: #modulus checks for divisability by 7 
        values.append(i) #adds i to values list
print(values)