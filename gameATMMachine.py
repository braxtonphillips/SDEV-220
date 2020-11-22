"""
Braxton Phillips
SDEV 220
Chapter 12 Exercise 12.3
Due Nov 21, 2020
"""

#Exercise 7.3
class Account:
   def __init__(self, id, balance = 500, annualInterestRate = 0):
       self.__id = id
       self.__balance = balance
       self.__annualInterestRate = annualInterestRate

   def getId(self):
       return self.__id

   def getBalance(self):
       return self.__balance

   def getAnnualInterestRate(self):
       return self.__annualInterestRate

   def getMonthlyInterestRate(self):
       return self.__annualInterestRate / 12

   def setPreviousPrice(self, previousPrice):
       self.previousPrice = previousPrice

   def setCurrentPrice(self, currentPrice):
       self.currentPrice = currentPrice

   def withdraw(self, amount):
       self.__balance -= amount

   def deposit(self, amount):
       self.__balance += amount

   def getMonthlyInterest(self):
       return self.__balance * self.getMonthlyInterestRate()

def main():
  
   accounts = []
  
   #creates 10 accounts
   for i in range(0, 10):
       account = Account(i, 500.0) #creats balance for accounts
       accounts.append(account)
      
   while True:
  
       id = int(input('Enter account id: '))
      
       #checks to see if id is valid and prompts if not
       while id < 0 or id > 9:
           id = int(input('\n Invalid Id! Try Again: '))

       #game loop 
       while True:
          
           print('\n 1 - View Balance \n 2 - Withdraw \n 3 - Deposit \n 4 - Exit ')
          
           selection = int(input('\n Enter your selection: '))
          
           #calling account class
           for acc in accounts:
               if acc.getId() == id: #check for valid id
                   accountObj = acc
                   break
          
           #display balace
           if selection == 1:
               print('\t$',accountObj.getBalance())
              
           #withdrawl process
           elif selection == 2:
               amt = float(input('\nEnter amount to withdraw: '))
               accountObj.withdraw(amt) #calls withdraw method
               print('\nUpdated Balance: \t$', str(accountObj.getBalance())) #updated balance
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
              
           #deposit funds
           elif selection == 3:
               amt = float(input('\nEnter amount to deposit: '))
               accountObj.deposit(amt) #calls deposit method
               print('\nUpdated Balance: \t$', str(accountObj.getBalance()) + " \n")
               print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

           #ends game
           else:
               quit()
          
main()