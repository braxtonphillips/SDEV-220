"""
Braxton Phillips
SDEV 220
Chapter 7 Exercise 7.3
Due Nov 7, 2020
"""
def main():
   account1 = Account(3345, 35000, 4.5)
   account1.withdraw(2500)
   account1.deposit(3000)
   print(account1.getAccountId())
   print(account1.getBalance())
   print(account1.getMonthlyInterestRate())
   print(account1.getMonthlyInterest())
main()
