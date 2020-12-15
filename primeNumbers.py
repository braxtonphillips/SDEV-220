"""
Braxton PHillips 
SDEV 220 
Chapter 18 Exercise 18.5
Due Dec 19, 2020 
"""

class Stack:
    def __init__(self):
        self.lst = [] #creats list for storing

    def push(self, num): #adds vals 
        self.lst.append(num)

    def pop(self):
        return self.lst.pop()

    def empty(self): #return empty list
        return len(self.lst) == 0


def isPrime(n): #function checks for primeness
    for i in range(2, n):
        if n % i == 0: #arithmetic
            return False
    return n > 1


def main():
    stackVals = Stack()
    for i in range(198): #sets range to 1 over the 50th pn
        if isPrime(i):
            stackVals.push(i)
    print("Prime numbers are")
    while not stackVals.empty():
        print(stackVals.pop())

main()
