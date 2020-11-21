"""
Braxton Phillips
SDEV 220
Chapter 11 Exercise 11.11 
Due Nov 21, 2020
"""

#COnverts number to binarys
def toBinary(num):
    binaryVal = ''
    while num > 0:
        binaryVal = str((num % 2)) + binaryVal #checks for even-ness
        num //= 2 #int div for remainder 
    binaryVal = '0' * (9 - len(binaryVal)) + binaryVal #adds remainder to binaryVal
    return binaryVal 

def main():
    num = int(input('Enter a number between 0 and 511: '))
    binaryVal = toBinary(num)
    ind = 0 #initialization for 
    #creates 3x3 matrix
    for i in range(3):
        for j in range(3):
            if binaryVal[ind] == '0': #check if val needs to be H or T
                print('H', end=' ')
            else:
                print('T', end=' ')
            ind += 1
        print()

main()