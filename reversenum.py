"""
Braxton Phillips
SDEV 220
Chapter 3 Excercise 3.11
Due Oct 31, 2020
"""

userNumber = int(input("Enter a four-digit integer: "))
numReverse = 0 #initialize number that will be revered 

while(userNumber>0):
  remainder = userNumber % 10 #here the modulus is making a reamider out of the last number during each iteration
  numReverse = (numReverse * 10) + remainder #stores the rem ad the new rev num
  userNumber = userNumber // 10
 
print("The reverse number is : ", numReverse)