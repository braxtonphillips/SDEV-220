"""
Braxton Phillips
SDEV 220
Chapter 6 Exercise 6.5
Due Nov 7, 2020
"""


def sortNumbers(userList):
    print('The sorted numbers are:', sorted(userList)) #sorts numbers

def reverseNumbers(userList):
    print('The reverse sorted numbers are:',sorted(userList, reverse = True)) #resure reads list a outputs contents as if [:-1]

def main():
    userList = [] 
  
    # number of elemetns as input 
    print('Enter 3 numbers: ')
  
    # iterating until 3rd num is entereed
    for i in range(0, 3): 
        valList = eval(input()) 
  
        userList.append(valList) # adding the element 
    #calling the funcs to display outputs 
    sortNumbers(userList)
    reverseNumbers(userList)
main()