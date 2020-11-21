"""
Braxton Phillips
SDEV 220
Chapter 10 Exercise 10.7
Due Nov 21, 2020
"""

#Using to call the randit frunction from the random module to generate random numbers
from random import randint 

counts = [0] * 10 #concatentates 10 copies of 0 sequence
for i in range(1000): #increments up to 1000
    j = randint(0,9) #assigns rand it to j 
    counts[j] += 1 #stores in respective place in seq

print(counts)